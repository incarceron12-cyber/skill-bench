#!/usr/bin/env python3
"""Validate and grade the internal fixed-versus-contingent criterion slice."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "pilots/dynamic-criterion-conformance/cases.json"
DEFAULT_INSTANCE_FIXTURE = ROOT / "pilots/dynamic-criterion-conformance/instance-conformance.json"
OUTCOMES = {"supported", "contradicted", "insufficient_evidence", "not_applicable"}
REQUIRED_LIMITS = {"agent capability", "expert validity", "professional readiness", "cross-domain generalization"}
COMPONENT_ROLES = {"task", "source", "reference", "rubric"}
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def grade(case: dict[str, Any]) -> dict[str, Any]:
    fixed = Counter(item["outcome"] for item in case["fixed"])
    contingent: Counter[str] = Counter()
    counted: set[str] = set()
    blocked = False
    for item in case["contingent"]:
        if item["relation"] == "duplicate":
            continue
        counted.add(item["id"])
        contingent[item["outcome"]] += 1
        if item["applicability"] == "applicable" and (not item.get("verifier") or item["outcome"] == "insufficient_evidence"):
            blocked = True
    return {"fixed": dict(fixed), "contingent": dict(contingent), "counted_contingent_ids": sorted(counted), "capability_evidence": "blocked" if blocked else "eligible_for_narrow_argument"}


def _predicate_set(component: dict[str, Any]) -> set[tuple[str, str]]:
    return {(item.get("dimension"), item.get("value")) for item in component.get("predicates", [])}


def validate_instance_conformance(path: Path = DEFAULT_INSTANCE_FIXTURE, check_paths: bool = False) -> dict[str, Any]:
    """Validate integrity and evaluate task-defined cross-role predicates.

    Assignment conformance is reported per assignment rather than folded into package
    validity because this fixture intentionally contains planted substitutions.
    """
    package = json.loads(path.read_text())
    errors: list[str] = []
    if package.get("status") != "internal_calibration_only":
        errors.append("instance fixture status must remain internal_calibration_only")
    if not REQUIRED_LIMITS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("instance fixture required claim limits are missing")

    components = package.get("components", [])
    component_ids = [item.get("id") for item in components]
    if len(component_ids) != len(set(component_ids)):
        errors.append("component ids must be unique")
    by_id = {item.get("id"): item for item in components}
    for component in components:
        label = component.get("id", "<missing-component-id>")
        if component.get("role") not in COMPONENT_ROLES:
            errors.append(f"{label}: invalid component role")
        if not SEMVER.fullmatch(str(component.get("version", ""))):
            errors.append(f"{label}: version must be semantic x.y.z")
        payload = component.get("payload")
        if not isinstance(payload, str) or not payload:
            errors.append(f"{label}: payload is required")
        elif hashlib.sha256(payload.encode("utf-8")).hexdigest() != component.get("sha256"):
            errors.append(f"{label}: payload hash mismatch")
        locators = component.get("evidence_locators", [])
        if not locators or not all(isinstance(value, str) and value for value in locators):
            errors.append(f"{label}: evidence locators are required")
        predicates = component.get("predicates", [])
        if not predicates or any(not item.get("dimension") or not item.get("value") for item in predicates):
            errors.append(f"{label}: typed predicates are incomplete")
        if len(_predicate_set(component)) != len(predicates):
            errors.append(f"{label}: duplicate typed predicate")

    results: list[dict[str, Any]] = []
    assignment_ids: set[str] = set()
    for assignment in package.get("assignments", []):
        assignment_id = assignment.get("id")
        if not assignment_id or assignment_id in assignment_ids:
            errors.append("assignment ids must be present and unique")
        assignment_ids.add(assignment_id)
        selected: dict[str, dict[str, Any]] = {}
        structurally_complete = True
        for role in COMPONENT_ROLES:
            component = by_id.get(assignment.get(role))
            if component is None:
                errors.append(f"{assignment_id}: unknown {role} component")
                structurally_complete = False
            elif component.get("role") != role:
                errors.append(f"{assignment_id}: assigned {role} has role {component.get('role')}")
                structurally_complete = False
            else:
                selected[role] = component
        issues: list[dict[str, Any]] = []
        if structurally_complete:
            task = selected["task"]
            task_predicates = _predicate_set(task)
            requirements = task.get("requirements", [])
            if not requirements:
                errors.append(f"{task.get('id')}: task requirements are required")
            for requirement in requirements:
                dimension = requirement.get("dimension")
                value = requirement.get("value")
                required_in = requirement.get("required_in", [])
                if not dimension or not value or (dimension, value) not in task_predicates:
                    errors.append(f"{task.get('id')}: requirement is not grounded in its task predicates")
                    continue
                if not required_in or any(role not in COMPONENT_ROLES - {"task"} for role in required_in):
                    errors.append(f"{task.get('id')}: requirement has invalid required roles")
                    continue
                for role in required_in:
                    observed = _predicate_set(selected[role])
                    if (dimension, value) not in observed:
                        observed_values = sorted(observed_value for observed_dimension, observed_value in observed if observed_dimension == dimension)
                        issues.append({
                            "role": role,
                            "dimension": dimension,
                            "required_value": value,
                            "observed_values": observed_values,
                            "failure": "conflict" if observed_values else "missing",
                        })
        results.append({"assignment_id": assignment_id, "conformant": structurally_complete and not issues, "issues": issues})

    if check_paths:
        for item in package.get("provenance", []):
            candidate = ROOT / item["path"]
            if not candidate.is_file():
                errors.append(f"missing provenance path: {item['path']}")
            elif _hash(candidate) != item.get("sha256"):
                errors.append(f"hash mismatch: {item['path']}")
            if not item.get("locators"):
                errors.append(f"missing provenance locators: {item.get('path')}")
    return {"valid": not errors, "errors": errors, "results": results}


def validate(path: Path = DEFAULT_FIXTURE, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(path.read_text())
    errors: list[str] = []
    if package.get("status") != "internal_calibration_only":
        errors.append("status must remain internal_calibration_only")
    if not REQUIRED_LIMITS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("required claim limits are missing")
    if len({case.get("work_shape") for case in package.get("cases", [])}) < 2:
        errors.append("at least two unlike work shapes are required")
    generator = package.get("generator", {})
    if not all(generator.get(k) is not None for k in ("model", "prompt_sha256", "seed", "skill_version")):
        errors.append("criterion-generation identity is incomplete")

    results = []
    for case in package.get("cases", []):
        all_items = case.get("fixed", []) + case.get("contingent", [])
        ids = [item.get("id") for item in all_items]
        if len(ids) != len(set(ids)):
            errors.append(f"{case.get('id')}: criterion ids must be unique")
        contingent_ids = {item.get("id") for item in case.get("contingent", [])}
        for item in all_items:
            if item.get("outcome") not in OUTCOMES or not item.get("public_basis"):
                errors.append(f"{case.get('id')}:{item.get('id')}: invalid outcome or missing public basis")
        for item in case.get("contingent", []):
            trigger = item.get("trigger", {})
            if not trigger.get("locator") or not trigger.get("text"):
                errors.append(f"{case['id']}:{item.get('id')}: contingent criterion lacks supported trigger")
            if item.get("applicability") not in {"applicable", "not_applicable"}:
                errors.append(f"{case['id']}:{item.get('id')}: invalid applicability")
            if item.get("applicability") == "not_applicable" and item.get("outcome") != "not_applicable":
                errors.append(f"{case['id']}:{item.get('id')}: not-applicable criterion must abstain")
            if item.get("relation") == "duplicate" and item.get("overlap_with") not in contingent_ids:
                errors.append(f"{case['id']}:{item.get('id')}: duplicate lacks valid overlap target")
            if any(dep not in contingent_ids for dep in item.get("depends_on", [])):
                errors.append(f"{case['id']}:{item.get('id')}: unknown dependency")
        expected_ids = case.get("irrelevant_edit", {}).get("expected_contingent_ids", [])
        if set(expected_ids) != contingent_ids:
            errors.append(f"{case['id']}: criterion-set drift under irrelevant edit")
        result = grade(case)
        if result["fixed"] != case["expected"]["fixed"] or result["contingent"] != case["expected"]["contingent"] or result["capability_evidence"] != case["expected"]["capability_evidence"]:
            errors.append(f"{case['id']}: graded result differs from expected separate score families")
        results.append({"case_id": case["id"], **result})

    if check_paths:
        for item in package.get("provenance", []):
            candidate = ROOT / item["path"]
            if not candidate.is_file():
                errors.append(f"missing provenance path: {item['path']}")
            elif _hash(candidate) != item["sha256"]:
                errors.append(f"hash mismatch: {item['path']}")
    return {"valid": not errors, "errors": errors, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    report = validate(args.path, args.check_paths)
    if args.path.resolve() == DEFAULT_FIXTURE.resolve():
        instance_report = validate_instance_conformance(check_paths=args.check_paths)
        report["instance_conformance"] = instance_report
        report["valid"] = report["valid"] and instance_report["valid"]
        report["errors"].extend(instance_report["errors"])
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
