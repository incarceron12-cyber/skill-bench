#!/usr/bin/env python3
"""Validate versioned population metrics and governed monitoring policies."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "metric-monitoring.schema.json"
REF_TYPES = {
    "task_ref_ids": {"task", "bundle"},
    "check_ref_ids": {"check", "grader", "bundle"},
    "grader_ref_ids": {"grader"},
    "system_ref_ids": {"configured_system", "bundle"},
    "validity_ref_ids": {"validity_argument"},
}


class ValidationFailure(Exception):
    """Raised when structural, reference, estimand, or action checks fail."""


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


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def semantic_errors(package: dict[str, Any]) -> list[str]:
    """Return cross-reference, population, fidelity, estimate, and alert errors."""
    errors: list[str] = []
    for items, key, label in (
        (package["artifacts"], "artifact_id", "artifacts"),
        (package["evidence"], "evidence_id", "evidence"),
        (package["metrics"], "metric_id", "metrics"),
        (package["monitoring_policies"], "policy_id", "monitoring policies"),
    ):
        for duplicate in sorted(_duplicates(item[key] for item in items)):
            errors.append(f"{label}: duplicate {key} {duplicate!r}")

    artifacts = {item["artifact_id"]: item for item in package["artifacts"]}
    evidence = {item["evidence_id"]: item for item in package["evidence"]}
    metrics = {item["metric_id"]: item for item in package["metrics"]}
    artifact_ids, evidence_ids = set(artifacts), set(evidence)

    for item in package["evidence"]:
        _refs(f"evidence {item['evidence_id']}", item["artifact_ref_ids"], artifact_ids, "artifact_ref_id", errors)

    for metric in package["metrics"]:
        owner = f"metric {metric['metric_id']}"
        for field, allowed_types in REF_TYPES.items():
            _refs(owner, metric[field], artifact_ids, field[:-1], errors)
            for ref in metric[field]:
                if ref in artifacts and artifacts[ref]["artifact_type"] not in allowed_types:
                    errors.append(f"{owner}: {field} reference {ref!r} has incompatible artifact type {artifacts[ref]['artifact_type']!r}")

        window = metric["population"]["window"]
        if _parse_time(window["end"]) <= _parse_time(window["start"]):
            errors.append(f"{owner}: population window end must be after start")

        candidate = metric["candidate_policy"]
        tool_selection = "tool selection" in (metric["construct"] + " " + metric["observable"]["predicate"]).lower()
        if tool_selection and candidate["applicability"] != "required":
            errors.append(f"{owner}: tool-selection metrics require an eligible candidate catalog and equivalence policy")
        if candidate["applicability"] == "required":
            ref = candidate["catalog_ref_id"]
            if ref is None or ref not in artifacts or artifacts[ref]["artifact_type"] != "candidate_catalog":
                errors.append(f"{owner}: required candidate policy must reference a versioned candidate_catalog artifact")
            if candidate["unknown_alternative_policy"] == "not_applicable":
                errors.append(f"{owner}: required candidate policy must govern unknown alternatives")
        elif candidate["catalog_ref_id"] is not None:
            errors.append(f"{owner}: not-applicable candidate policy cannot reference a catalog")

        fidelity = metric["fidelity"]
        _refs(owner, fidelity["evidence_ids"], evidence_ids, "fidelity evidence_id", errors)
        if fidelity["representativeness_claim"] == "none":
            if fidelity["status"] != "not_claimed":
                errors.append(f"{owner}: no representativeness claim must have status not_claimed")
        else:
            fidelity_evidence = [evidence[eid] for eid in fidelity["evidence_ids"] if eid in evidence and evidence[eid]["evidence_type"] == "fidelity_evaluation"]
            if not fidelity_evidence:
                errors.append(f"{owner}: synthetic/simulated representativeness requires target-population fidelity evidence")
            if fidelity["representativeness_claim"] == "representative" and fidelity["status"] != "supported":
                errors.append(f"{owner}: representative claim requires supported fidelity status")
        if metric["population"]["population_kind"] in {"synthetic", "simulated"} and fidelity["representativeness_claim"] == "representative" and not fidelity["dimensions"]:
            errors.append(f"{owner}: synthetic representativeness requires declared fidelity dimensions")

        measurement_ids = {ref for ref, artifact in artifacts.items() if artifact["artifact_type"] in {"measurement", "baseline_measurement"}}
        for estimate in metric["observed_estimates"]:
            estimate_owner = f"{owner} estimate {estimate['window_id']}"
            _refs(estimate_owner, [estimate["measurement_ref_id"]], measurement_ids, "measurement_ref_id", errors)
            if estimate["window_id"] != window["window_id"]:
                errors.append(f"{estimate_owner}: estimate window must match the metric population window")
            if estimate["numerator"] > estimate["denominator"] and metric["computation"]["kind"] == "rate":
                errors.append(f"{estimate_owner}: rate numerator cannot exceed denominator")
            expected = estimate["numerator"] / estimate["denominator"]
            if metric["computation"]["kind"] == "rate" and not math.isclose(estimate["value"], expected, rel_tol=0, abs_tol=1e-12):
                errors.append(f"{estimate_owner}: rate value does not equal numerator / denominator")

        uncertainty = metric["computation"]["uncertainty"]
        if uncertainty["method"] == "exact_enumeration" and "exact" not in uncertainty["justification"].lower():
            errors.append(f"{owner}: exact enumeration needs an explicit exact finite-population justification")

    for policy in package["monitoring_policies"]:
        owner = f"monitoring policy {policy['policy_id']}"
        metric = metrics.get(policy["metric_id"])
        if metric is None:
            errors.append(f"{owner}: unknown metric_id {policy['metric_id']!r}")
            continue
        if policy["metric_version"] != metric["version"]:
            errors.append(f"{owner}: policy metric_version must equal the referenced immutable metric version")
        baseline = policy["baseline"]
        if baseline["metric_version"] != metric["version"]:
            errors.append(f"{owner}: baseline metric_version must match the monitored metric version or use a separately bridged metric specification")
        if baseline["window_id"] != metric["population"]["window"]["window_id"] and baseline["type"] == "none_calibration":
            errors.append(f"{owner}: calibration baseline must name the exact calibration window")
        if baseline["artifact_ref_id"] is not None:
            _refs(owner, [baseline["artifact_ref_id"]], artifact_ids, "baseline artifact_ref_id", errors)
            if baseline["artifact_ref_id"] in artifacts and artifacts[baseline["artifact_ref_id"]]["artifact_type"] not in {"measurement", "baseline_measurement"}:
                errors.append(f"{owner}: baseline must reference a measurement artifact")
        if policy["scope"] == "production":
            if baseline["type"] == "none_calibration" or baseline["artifact_ref_id"] is None:
                errors.append(f"{owner}: production monitoring requires a versioned baseline measurement")
            if metric["population"]["window"]["instrument_version_policy"] == "bridge_validated_versions" and not metric["population"]["window"]["interventions"]:
                errors.append(f"{owner}: pooled production drift across versions requires recorded bridge/intervention evidence")
            if metric["computation"]["uncertainty"]["method"] in {"not_estimated", "exact_enumeration"}:
                errors.append(f"{owner}: production alert requires population uncertainty, not no estimate or fixture enumeration")
        if policy["threshold"]["minimum_support"] < metric["computation"]["minimum_support"]:
            errors.append(f"{owner}: alert minimum support cannot undercut the metric minimum support")
        if policy["threshold"]["basis"] == "provisional_policy" and policy["scope"] == "production":
            errors.append(f"{owner}: provisional threshold cannot trigger production action")

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
        except (OSError, ValueError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {package_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
