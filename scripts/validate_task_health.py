#!/usr/bin/env python3
"""Validate versioned task-health and lifecycle packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "task-health.schema.json"
INSTRUMENT_TYPES = {"task", "suite", "bundle", "grader", "harness", "environment", "benchmark_version"}
DEFECTS_REQUIRING_VERSION = {"task_defect", "grader_defect", "harness_defect", "environment_defect"}
REQUIRED_HEALTH_SIGNALS = {
    "repeat_stability", "invalid_run_rate", "unresolved_instrument_invalidity",
    "grader_human_disagreement", "saturation", "usage_relevance", "critical_coverage",
}


class ValidationFailure(Exception):
    """Raised when structural, reference, or lifecycle checks fail."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _refs(owner: str, refs: Iterable[str], valid: set[str], label: str, errors: list[str]) -> None:
    for ref in refs:
        if ref not in valid:
            errors.append(f"{owner}: unknown {label} {ref!r}")


def semantic_errors(package: dict[str, Any]) -> list[str]:
    """Return cross-reference, claim-boundary, transition, and versioning errors."""
    errors: list[str] = []
    for items, key, label in (
        (package["artifacts"], "artifact_id", "artifacts"),
        (package["evidence"], "evidence_id", "evidence"),
        (package["task_health_records"], "task_health_id", "task health records"),
    ):
        for duplicate in sorted(_duplicates(item[key] for item in items)):
            errors.append(f"{label}: duplicate {key} {duplicate!r}")

    artifacts = {item["artifact_id"]: item for item in package["artifacts"]}
    evidence = {item["evidence_id"]: item for item in package["evidence"]}
    artifact_ids, evidence_ids = set(artifacts), set(evidence)
    for item in package["evidence"]:
        _refs(f"evidence {item['evidence_id']}", item["artifact_ref_ids"], artifact_ids, "artifact_ref_id", errors)

    for record in package["task_health_records"]:
        owner = f"task health {record['task_health_id']}"
        _refs(owner, [record["task_ref_id"], record["suite_ref_id"]], artifact_ids, "artifact_ref_id", errors)
        if record["task_ref_id"] in artifacts and artifacts[record["task_ref_id"]]["artifact_type"] not in {"task", "bundle"}:
            errors.append(f"{owner}: task_ref_id must reference a task or bundle artifact")
        if record["suite_ref_id"] in artifacts and artifacts[record["suite_ref_id"]]["artifact_type"] not in {"suite", "bundle"}:
            errors.append(f"{owner}: suite_ref_id must reference a suite or bundle artifact")
        _refs(owner, record["origin"]["evidence_ids"], evidence_ids, "evidence_id", errors)
        if record["origin"]["admission_influenced_by_outcomes"] and record["origin"]["selection_stage"] in {"confirmatory", "transfer", "operational"}:
            errors.append(f"{owner}: outcome-influenced admission cannot be labeled confirmatory, transfer, or operational")

        polarities = {case["polarity"] for case in record["contrast_set"]}
        if polarities != {"positive", "negative"}:
            errors.append(f"{owner}: contrast_set requires both positive and negative cases")
        for role in record["operational_roles"]:
            _refs(owner, role["evidence_ids"], evidence_ids, "role evidence_id", errors)
        for attempt in record["reference_attempts"]:
            attempt_owner = f"{owner} reference attempt {attempt['attempt_id']}"
            refs = [attempt["task_ref_id"], attempt["harness_ref_id"], attempt["environment_ref_id"], attempt["output_ref_id"], *attempt["grader_ref_ids"]]
            _refs(attempt_owner, refs, artifact_ids, "artifact_ref_id", errors)
            _refs(attempt_owner, attempt["evidence_ids"], evidence_ids, "evidence_id", errors)
            if attempt["result"] != "pass":
                errors.append(f"{attempt_owner}: a reference witness must pass; failed/invalid attempts are trial evidence, not witnesses")
        for case in record["contrast_set"]:
            _refs(f"{owner} contrast {case['case_id']}", [case["task_ref_id"]], artifact_ids, "task_ref_id", errors)
            _refs(f"{owner} contrast {case['case_id']}", case["evidence_ids"], evidence_ids, "evidence_id", errors)

        signals: dict[str, dict[str, Any]] = {}
        for signal in record["health_evidence"]:
            if signal["signal"] in signals:
                errors.append(f"{owner}: duplicate health signal {signal['signal']!r}")
            signals[signal["signal"]] = signal
            _refs(f"{owner} health signal {signal['signal']}", signal["evidence_ids"], evidence_ids, "evidence_id", errors)
        missing_signals = REQUIRED_HEALTH_SIGNALS - set(signals)
        if missing_signals:
            errors.append(f"{owner}: health_evidence is missing required signals {sorted(missing_signals)}")

        revisions = record["revisions"]
        for revision in revisions:
            _refs(f"{owner} revision {revision['revision_id']}", [*revision["old_artifact_ref_ids"], *revision["new_artifact_ref_ids"]], artifact_ids, "artifact_ref_id", errors)
            _refs(f"{owner} revision {revision['revision_id']}", revision["evidence_ids"], evidence_ids, "evidence_id", errors)
            if set(revision["old_artifact_ref_ids"]) & set(revision["new_artifact_ref_ids"]):
                errors.append(f"{owner} revision {revision['revision_id']}: old and new versions must be distinct artifact records")
            if len(revision["old_artifact_ref_ids"]) == len(revision["new_artifact_ref_ids"]):
                for old_ref, new_ref in zip(revision["old_artifact_ref_ids"], revision["new_artifact_ref_ids"]):
                    if old_ref in artifacts and new_ref in artifacts:
                        if artifacts[old_ref]["artifact_type"] != artifacts[new_ref]["artifact_type"]:
                            errors.append(f"{owner} revision {revision['revision_id']}: replacement artifact types must match")
                        if artifacts[old_ref]["version"] == artifacts[new_ref]["version"]:
                            errors.append(f"{owner} revision {revision['revision_id']}: replacement must have a distinct version")
            if not revision["old_scores_preserved"]:
                errors.append(f"{owner} revision {revision['revision_id']}: old scores must be preserved rather than rewritten")

        for adjudication in record["adjudications"]:
            adj_owner = f"{owner} adjudication {adjudication['adjudication_id']}"
            _refs(adj_owner, [adjudication["original_result_ref_id"], *adjudication["observation_ref_ids"], *adjudication["affected_artifact_ref_ids"], *adjudication["replacement_artifact_ref_ids"]], artifact_ids, "artifact_ref_id", errors)
            _refs(adj_owner, adjudication["evidence_ids"], evidence_ids, "evidence_id", errors)
            observation_types = {artifacts[ref]["artifact_type"] for ref in adjudication["observation_ref_ids"] if ref in artifacts}
            if adjudication["observation_basis"] in {"transcript", "combined"} and "transcript" not in observation_types:
                errors.append(f"{adj_owner}: transcript-grounded adjudication needs a transcript artifact")
            if adjudication["defect_type"] in {"agent_failure", "accepted_alternative"} and adjudication["observation_basis"] not in {"transcript", "combined"}:
                errors.append(f"{adj_owner}: agent-failure or accepted-alternative adjudication requires transcript-grounded observation")
            if adjudication["defect_type"] in DEFECTS_REQUIRING_VERSION:
                if adjudication["decision"] != "revise_instrument" or not adjudication["replacement_artifact_ref_ids"]:
                    errors.append(f"{adj_owner}: instrument defect must create a replacement version")
                matching_revision = any(
                    set(adjudication["affected_artifact_ref_ids"]) <= set(revision["old_artifact_ref_ids"])
                    and set(adjudication["replacement_artifact_ref_ids"]) <= set(revision["new_artifact_ref_ids"])
                    for revision in revisions
                )
                if not matching_revision:
                    errors.append(f"{adj_owner}: instrument defect needs a matching immutable revision record")
                if adjudication["old_score_disposition"] not in {"preserve_as_recorded", "void_but_preserve"}:
                    errors.append(f"{adj_owner}: old result must remain preserved")
            if adjudication["defect_type"] in {"task_defect", "grader_defect", "harness_defect", "environment_defect", "insufficient_observability"} and adjudication["capability_aggregation_disposition"] != "exclude":
                errors.append(f"{adj_owner}: invalid instrument/observation evidence must be excluded from capability aggregation")

        for transition in record["transitions"]:
            trans_owner = f"{owner} transition {transition['transition_id']}"
            _refs(trans_owner, transition["evidence_ids"], evidence_ids, "evidence_id", errors)
            if transition["to_role"] == "regression_guard":
                required = {"repeat_stability", "invalid_run_rate", "unresolved_instrument_invalidity"}
                missing = required - set(signals)
                unacceptable = [name for name in required if signals.get(name, {}).get("status") != "acceptable"]
                if missing or unacceptable:
                    errors.append(f"{trans_owner}: regression graduation requires acceptable repeat stability, invalid-run rate, and unresolved-invalidity evidence")
                evidence_types = {evidence[eid]["evidence_type"] for eid in transition["evidence_ids"] if eid in evidence}
                if "saturation" in evidence_types and evidence_types <= {"saturation"}:
                    errors.append(f"{trans_owner}: saturation alone cannot justify regression graduation")
                if not transition["regression_consequence"].strip():
                    errors.append(f"{trans_owner}: regression graduation requires an owner-defined consequence")

        retirement = record["retirement"]
        _refs(owner, retirement["replacement_task_ref_ids"], artifact_ids, "replacement task_ref_id", errors)
        _refs(owner, retirement["evidence_ids"], evidence_ids, "retirement evidence_id", errors)
        if retirement["status"] == "retired" and not retirement["evidence_ids"]:
            errors.append(f"{owner}: retirement requires evidence and an explicit critical-coverage disposition")

    return errors


def validate_file(package_path: Path, schema_path: Path = DEFAULT_SCHEMA, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    package = json.loads(package_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(package), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(package))
    if check_paths:
        for artifact in package["artifacts"]:
            path = ROOT / artifact["path"]
            if not path.is_file():
                errors.append(f"artifact {artifact['artifact_id']}: path does not exist: {artifact['path']}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
                errors.append(f"artifact {artifact['artifact_id']}: sha256 does not match {artifact['path']}")
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packages", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for package_path in args.packages:
        try:
            validate_file(package_path, args.schema, args.check_paths)
            print(f"VALID {package_path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {package_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
