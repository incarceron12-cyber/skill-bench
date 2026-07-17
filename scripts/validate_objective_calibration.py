#!/usr/bin/env python3
"""Validate native objective calibration and aggregation-sensitivity packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "objective-calibration.schema.json"


class ValidationFailure(Exception):
    """Raised when structure, provenance, calibration, or aggregation is invalid."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def semantic_errors(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    artifacts = {item["artifact_id"]: item for item in package["artifacts"]}
    evidence = {item["evidence_id"]: item for item in package["evidence"]}
    for duplicate in sorted(_duplicates(item["artifact_id"] for item in package["artifacts"])):
        errors.append(f"artifacts: duplicate artifact_id {duplicate!r}")
    for duplicate in sorted(_duplicates(item["evidence_id"] for item in package["evidence"])):
        errors.append(f"evidence: duplicate evidence_id {duplicate!r}")
    for item in package["evidence"]:
        for ref in item["artifact_ref_ids"]:
            if ref not in artifacts:
                errors.append(f"evidence {item['evidence_id']}: unknown artifact_ref_id {ref!r}")

    for calibration in package["objective_calibrations"]:
        owner = f"objective calibration {calibration['calibration_id']}"
        measurement_ref = calibration["measurement_ref_id"]
        if measurement_ref not in artifacts or artifacts[measurement_ref]["artifact_type"] != "measurement":
            errors.append(f"{owner}: measurement_ref_id must reference a versioned measurement artifact")
        for duplicate in sorted(_duplicates(item["observation_id"] for item in calibration["observations"])):
            errors.append(f"{owner}: duplicate observation_id {duplicate!r}")
        modes = {item["calibration_mode"] for item in calibration["observations"]}
        stages = [item["stage_id"] for item in calibration["observations"] if item["stage_id"] is not None]
        policy = calibration["portfolio_policy"]
        for ref in policy["bridge_evidence_ids"]:
            if ref not in evidence:
                errors.append(f"{owner}: unknown bridge evidence_id {ref!r}")
        for item in calibration["observations"]:
            reference = item["reference"]
            item_owner = f"{owner} observation {item['observation_id']}"
            if reference["method"] == "heuristic" and reference["strength"] == "proven_optimum":
                errors.append(f"{item_owner}: heuristic reference cannot be asserted as a proven optimum")
            if item["calibration_mode"] == "bound_based" and (reference["bound"] is None or reference["strength"] != "valid_bound"):
                errors.append(f"{item_owner}: bound-based calibration requires a valid-bound reference and numeric bound")
            if item["calibration_mode"] == "poor_anchor" and reference["poor_anchor"] is None:
                errors.append(f"{item_owner}: poor-anchor calibration requires a numeric poor anchor")
            if item["calibration_mode"] == "unnormalized" and item["normalized"]["value"] is not None:
                errors.append(f"{item_owner}: unnormalized observation cannot report a normalized value")
            if item["hard_feasibility"] == "failed" and calibration["disposition"] == "accepted":
                errors.append(f"{owner}: a hard-feasibility failure cannot receive an accepted disposition")
        if policy["hard_feasibility_policy"] != "noncompensatory":
            errors.append(f"{owner}: hard feasibility must be noncompensatory")
        if len(modes) > 1 and policy["calibration_mode_pooling"] != "stratified" and not policy["bridge_evidence_ids"]:
            errors.append(f"{owner}: pooling across calibration modes requires declared bridge evidence or stratification")
        threshold = calibration["threshold"]
        if threshold["scope"] == "common_portfolio" and (not policy["estimand"].strip() or not policy["loss_basis"].strip()):
            errors.append(f"{owner}: a common threshold requires a declared portfolio estimand and loss basis")
        if stages and policy["stage_aggregation"] != "not_applicable":
            sensitivity_policies = {item["policy"] for item in policy["sensitivity_outputs"]}
            if len(sensitivity_policies) < 2:
                errors.append(f"{owner}: staged aggregation requires at least two sensitivity outputs")
    return errors


def validate_file(package_path: Path, schema_path: Path = DEFAULT_SCHEMA, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    package = json.loads(package_path.read_text(encoding="utf-8"))
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(Draft202012Validator(schema).iter_errors(package), key=lambda item: list(item.absolute_path))
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
        except (OSError, ValueError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {package_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
