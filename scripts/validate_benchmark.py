#!/usr/bin/env python3
"""Validate skill-bench benchmark bundles structurally and semantically.

JSON Schema catches local shape/type errors. These checks enforce references and
cross-record invariants that JSON Schema cannot express clearly.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "benchmark-bundle.schema.json"


class ValidationFailure(Exception):
    """Raised when one or more validation errors are present."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _check_unique(items: list[dict[str, Any]], key: str, location: str, errors: list[str]) -> None:
    duplicates = _duplicates(item[key] for item in items)
    for duplicate in sorted(duplicates):
        errors.append(f"{location}: duplicate {key} {duplicate!r}")


def semantic_errors(bundle: dict[str, Any]) -> list[str]:
    """Return cross-reference and completed-trial invariant violations."""
    errors: list[str] = []
    task = bundle["task"]
    sources = task["source_pack"]
    primitives = task["domain_primitives"]
    contracts = task["artifact_contracts"]
    checks = task["checks"]
    graders = bundle["graders"]
    trials = bundle["trials"]

    for items, key, location in [
        (sources, "source_id", "task.source_pack"),
        (primitives, "primitive_id", "task.domain_primitives"),
        (contracts, "artifact_id", "task.artifact_contracts"),
        (checks, "check_id", "task.checks"),
        (graders, "grader_id", "graders"),
        (trials, "trial_id", "trials"),
    ]:
        _check_unique(items, key, location, errors)

    source_ids = {item["source_id"] for item in sources}
    artifact_ids = {item["artifact_id"] for item in contracts}
    check_ids = {item["check_id"] for item in checks}
    grader_ids = {item["grader_id"] for item in graders}
    check_by_id = {item["check_id"]: item for item in checks}

    for primitive in primitives:
        for source_id in primitive["source_ids"]:
            if source_id not in source_ids:
                errors.append(f"primitive {primitive['primitive_id']}: unknown source_id {source_id!r}")
        for check_id in primitive["check_ids"]:
            if check_id not in check_ids:
                errors.append(f"primitive {primitive['primitive_id']}: unknown check_id {check_id!r}")

    for check in checks:
        if check["grader_id"] not in grader_ids:
            errors.append(f"check {check['check_id']}: unknown grader_id {check['grader_id']!r}")
        for artifact_id in check["artifact_ids"]:
            if artifact_id not in artifact_ids:
                errors.append(f"check {check['check_id']}: unknown artifact_id {artifact_id!r}")
        for source_id in check["evidence_source_ids"]:
            if source_id not in source_ids:
                errors.append(f"check {check['check_id']}: unknown evidence source_id {source_id!r}")

    required_artifacts = {item["artifact_id"] for item in contracts if item["required"]}
    for trial in trials:
        prefix = f"trial {trial['trial_id']}"
        if trial["task_id"] != task["task_id"] or trial["task_version"] != task["version"]:
            errors.append(f"{prefix}: task identity/version does not match bundle task")

        observed = trial["artifacts"]
        _check_unique(observed, "artifact_id", f"{prefix}.artifacts", errors)
        observed_ids = {item["artifact_id"] for item in observed}
        for artifact_id in observed_ids - artifact_ids:
            errors.append(f"{prefix}: unknown observed artifact_id {artifact_id!r}")

        trace = trial["trace"]
        events = trace["events"]
        _check_unique(events, "event_id", f"{prefix}.trace.events", errors)
        sequences = [event["sequence"] for event in events]
        if len(sequences) != len(set(sequences)):
            errors.append(f"{prefix}.trace.events: event sequence values must be unique")
        if sequences != sorted(sequences):
            errors.append(f"{prefix}.trace.events: events must be ordered by sequence")
        event_ids = {event["event_id"] for event in events}
        for edge in trace["dependencies"]:
            if edge["from_event_id"] not in event_ids or edge["to_event_id"] not in event_ids:
                errors.append(f"{prefix}: trace dependency references unknown event")
            if edge["from_event_id"] == edge["to_event_id"]:
                errors.append(f"{prefix}: trace dependency cannot be a self-loop")

        results = trial["check_results"]
        _check_unique(results, "check_id", f"{prefix}.check_results", errors)
        result_ids = {result["check_id"] for result in results}
        for result in results:
            check = check_by_id.get(result["check_id"])
            if check is None:
                errors.append(f"{prefix}: unknown result check_id {result['check_id']!r}")
                continue
            if result["grader_id"] != check["grader_id"]:
                errors.append(f"{prefix}, check {result['check_id']}: grader_id differs from task check")
            if "root_cause" in result and result["root_cause"] not in check["allowed_root_causes"]:
                errors.append(f"{prefix}, check {result['check_id']}: root cause is not allowed by task check")
            causal_ids = set(result.get("causal_slice_event_ids", []))
            referenced = causal_ids | {result[key] for key in ("root_event_id", "surfaced_at_event_id") if key in result}
            unknown_events = referenced - event_ids
            if unknown_events:
                errors.append(f"{prefix}, check {result['check_id']}: unknown causal event(s) {sorted(unknown_events)}")
            if causal_ids and not {result.get("root_event_id"), result.get("surfaced_at_event_id")} <= causal_ids:
                errors.append(f"{prefix}, check {result['check_id']}: causal slice must include root and surfaced events")

        if trial["status"] == "completed":
            missing_checks = check_ids - result_ids
            extra_checks = result_ids - check_ids
            if missing_checks or extra_checks:
                errors.append(f"{prefix}: completed trial check coverage mismatch; missing={sorted(missing_checks)}, extra={sorted(extra_checks)}")
            missing_artifacts = required_artifacts - observed_ids
            if missing_artifacts:
                errors.append(f"{prefix}: completed trial missing required artifacts {sorted(missing_artifacts)}")
            if result_ids == check_ids:
                total_weight = sum(check_by_id[cid]["weight"] for cid in check_ids)
                expected = sum(check_by_id[result["check_id"]]["weight"] * result["score"] for result in results) / total_weight
                if abs(expected - trial["aggregate_score"]) > 1e-6:
                    errors.append(f"{prefix}: aggregate_score {trial['aggregate_score']} != weighted score {expected:.6f}")

    return errors


def _provenance_local_paths(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        if {"source_type", "locator", "description"} <= value.keys() and "local_path" in value:
            yield value["local_path"]
        for child in value.values():
            yield from _provenance_local_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from _provenance_local_paths(child)


def validate_file(bundle_path: Path, schema_path: Path, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(bundle), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(bundle))
    if check_paths:
        for local_path in _provenance_local_paths(bundle):
            if not (ROOT / local_path).is_file():
                errors.append(f"provenance local_path does not exist: {local_path}")
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundles", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true", help="require provenance local_path files to exist in the repository")
    args = parser.parse_args()
    failed = False
    for bundle_path in args.bundles:
        try:
            validate_file(bundle_path, args.schema, args.check_paths)
            print(f"VALID {bundle_path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {bundle_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
