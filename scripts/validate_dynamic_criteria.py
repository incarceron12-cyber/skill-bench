#!/usr/bin/env python3
"""Validate and grade the internal fixed-versus-contingent criterion slice."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "pilots/dynamic-criterion-conformance/cases.json"
OUTCOMES = {"supported", "contradicted", "insufficient_evidence", "not_applicable"}
REQUIRED_LIMITS = {"agent capability", "expert validity", "professional readiness", "cross-domain generalization"}


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
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
