#!/usr/bin/env python3
"""Validate skill-bench benchmark bundles structurally and semantically.

JSON Schema catches local shape/type errors. These checks enforce references and
cross-record invariants that JSON Schema cannot express clearly.
"""
from __future__ import annotations

import argparse
import hashlib
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
    skills = bundle["procedural_skills"]
    rubrics = bundle["rubrics"]
    sources = task["source_pack"]
    primitives = task["domain_primitives"]
    contracts = task["artifact_contracts"]
    checks = task["checks"]
    graders = bundle["graders"]
    trials = bundle["trials"]

    for items, key, location in [
        (skills, "skill_id", "procedural_skills"),
        (rubrics, "rubric_id", "rubrics"),
        (sources, "source_id", "task.source_pack"),
        (primitives, "primitive_id", "task.domain_primitives"),
        (contracts, "artifact_id", "task.artifact_contracts"),
        (checks, "check_id", "task.checks"),
        (graders, "grader_id", "graders"),
        (trials, "trial_id", "trials"),
    ]:
        _check_unique(items, key, location, errors)

    source_ids = {item["source_id"] for item in sources}
    skill_by_id = {item["skill_id"]: item for item in skills}
    rubric_by_id = {item["rubric_id"]: item for item in rubrics}
    artifact_ids = {item["artifact_id"] for item in contracts}
    check_ids = {item["check_id"] for item in checks}
    grader_ids = {item["grader_id"] for item in graders}
    check_by_id = {item["check_id"]: item for item in checks}

    requirement_by_id: dict[str, dict[str, Any]] = {}
    for skill in skills:
        phase_ids = set(skill["workflow_phases"])
        _check_unique(skill["requirements"], "requirement_id", f"skill {skill['skill_id']}.requirements", errors)
        local_requirements = {item["requirement_id"] for item in skill["requirements"]}
        for requirement in skill["requirements"]:
            requirement_id = requirement["requirement_id"]
            if requirement_id in requirement_by_id:
                errors.append(f"procedural_skills: duplicate requirement_id {requirement_id!r}")
            requirement_by_id[requirement_id] = requirement
            if requirement["phase_id"] not in phase_ids:
                errors.append(f"requirement {requirement_id}: unknown phase_id {requirement['phase_id']!r}")
            for predecessor in requirement["ordering_after"]:
                if predecessor not in local_requirements:
                    errors.append(f"requirement {requirement_id}: unknown ordering predecessor {predecessor!r}")
                if predecessor == requirement_id:
                    errors.append(f"requirement {requirement_id}: cannot be ordered after itself")
            for artifact_id in requirement["artifact_ids"]:
                if artifact_id not in artifact_ids:
                    errors.append(f"requirement {requirement_id}: unknown artifact_id {artifact_id!r}")
            for check_id in requirement["check_ids"]:
                if check_id not in check_ids:
                    errors.append(f"requirement {requirement_id}: unknown check_id {check_id!r}")

    for rubric in rubrics:
        for check_id in rubric["check_ids"]:
            if check_id not in check_ids:
                errors.append(f"rubric {rubric['rubric_id']}: unknown check_id {check_id!r}")

    for primitive in primitives:
        for source_id in primitive["source_ids"]:
            if source_id not in source_ids:
                errors.append(f"primitive {primitive['primitive_id']}: unknown source_id {source_id!r}")
        for check_id in primitive["check_ids"]:
            if check_id not in check_ids:
                errors.append(f"primitive {primitive['primitive_id']}: unknown check_id {check_id!r}")

    for check in checks:
        if check["rubric_id"] not in rubric_by_id:
            errors.append(f"check {check['check_id']}: unknown rubric_id {check['rubric_id']!r}")
        elif check["check_id"] not in rubric_by_id[check["rubric_id"]]["check_ids"]:
            errors.append(f"check {check['check_id']}: rubric does not reciprocally list check")
        if check["visibility"] in {"private", "hidden"} and check["boundary_disclosure"] != "held_out_consequence":
            errors.append(f"check {check['check_id']}: private/hidden check must be a held_out_consequence")
        for requirement_id in check["public_basis_requirement_ids"]:
            requirement = requirement_by_id.get(requirement_id)
            if requirement is None:
                errors.append(f"check {check['check_id']}: unknown public basis requirement {requirement_id!r}")
            elif check["check_id"] not in requirement["check_ids"]:
                errors.append(f"check {check['check_id']}: public basis requirement does not reciprocally list check")
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

        versions = trial["evaluation_versions"]
        condition = versions["condition"]
        skill_version = versions["skill"]
        expected_relationship = {
            "no_skill_independent_rubric": "independent",
            "no_skill_shared_rubric": "shared_expert_model",
            "public_skill_independent_rubric": "independent",
            "public_skill_shared_rubric": "shared_expert_model",
            "exact_rubric_disclosed": "exact_disclosed",
        }[condition]
        rubric = rubric_by_id.get(versions["rubric"]["component_id"])
        if rubric is None:
            errors.append(f"{prefix}: evaluation_versions references unknown rubric")
        elif (rubric["version"], rubric["sha256"]) != (versions["rubric"]["version"], versions["rubric"]["sha256"]):
            errors.append(f"{prefix}: rubric version/hash does not match declared rubric")
        elif rubric["relationship_to_skill"] != expected_relationship:
            errors.append(f"{prefix}: ablation condition conflicts with rubric relationship")
        if condition.startswith("no_skill_"):
            if skill_version is not None:
                errors.append(f"{prefix}: no-skill condition must record skill as null")
            enabled_declared_skills = set(trial["agent"]["skills_enabled"]) & set(skill_by_id)
            if enabled_declared_skills:
                errors.append(f"{prefix}: no-skill condition enables declared procedural skill(s) {sorted(enabled_declared_skills)}")
        elif skill_version is None:
            errors.append(f"{prefix}: skill condition must record a skill version/hash")
        else:
            skill = skill_by_id.get(skill_version["component_id"])
            if skill is None or (skill["version"], skill["sha256"]) != (skill_version["version"], skill_version["sha256"]):
                errors.append(f"{prefix}: skill version/hash does not match declared skill")
            if skill_version["component_id"] not in trial["agent"]["skills_enabled"]:
                errors.append(f"{prefix}: typed skill is not listed in agent.skills_enabled")
        task_component = versions["task"]
        if task_component["component_id"] != task["task_id"] or task_component["version"] != task["version"]:
            errors.append(f"{prefix}: typed task version does not match bundle task")
        grader_components = {item["component_id"]: item for item in versions["graders"]}
        for grader in graders:
            component = grader_components.get(grader["grader_id"])
            if component is None or (component["version"], component["sha256"]) != (grader["version"], grader["sha256"]):
                errors.append(f"{prefix}: grader version/hash missing or inconsistent for {grader['grader_id']!r}")

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
        event_by_id = {event["event_id"]: event for event in events}
        recovery_relations: dict[str, list[tuple[str, str]]] = {}
        for edge in trace["dependencies"]:
            if edge["from_event_id"] not in event_ids or edge["to_event_id"] not in event_ids:
                errors.append(f"{prefix}: trace dependency references unknown event")
            if edge["from_event_id"] == edge["to_event_id"]:
                errors.append(f"{prefix}: trace dependency cannot be a self-loop")
            recovery_relations.setdefault(edge["relation"], []).append((edge["from_event_id"], edge["to_event_id"]))
            expected_kinds = {
                "error_feedback": ("error", "verifier_feedback"),
                "feedback_repair": ("verifier_feedback", "repair"),
                "repair_verification": ("repair", "verification"),
            }.get(edge["relation"])
            if expected_kinds and edge["from_event_id"] in event_by_id and edge["to_event_id"] in event_by_id:
                actual = (event_by_id[edge["from_event_id"]]["kind"], event_by_id[edge["to_event_id"]]["kind"])
                if actual != expected_kinds:
                    errors.append(f"{prefix}: {edge['relation']} edge must connect {expected_kinds}, got {actual}")
        for error_id, feedback_id in recovery_relations.get("error_feedback", []):
            repairs = [target for source, target in recovery_relations.get("feedback_repair", []) if source == feedback_id]
            if not repairs or not any(
                source == repair_id
                for repair_id in repairs
                for source, _ in recovery_relations.get("repair_verification", [])
            ):
                errors.append(f"{prefix}: recovery chain from error {error_id!r} is incomplete")

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
        for skill in bundle.get("procedural_skills", []):
            content_path = ROOT / skill["content_path"]
            if not content_path.is_file():
                errors.append(f"procedural skill content_path does not exist: {skill['content_path']}")
            elif hashlib.sha256(content_path.read_bytes()).hexdigest() != skill["sha256"]:
                errors.append(f"procedural skill sha256 mismatch: {skill['skill_id']}")
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
