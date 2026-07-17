#!/usr/bin/env python3
"""Replay an inert cross-shape deterministic scaffold response matrix."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

PACKAGE = Path(__file__).with_name("package.json")
CASE_CONTENT_SHA256 = "e63b406b95fa6c1b2c20430f43030f7ae6669a85db56ab548774091ff9c1886e"
OBSERVER_CONTRACT_SHA256 = "6ae724ad4be067d5bcd4d47163ccc76a82362c23c508d5b584c8a090366b505e"
ALLOWED_TRUE_CLAIMS = {"exact_synthetic_fixture_detection"}


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load(path: Path = PACKAGE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def pure_cases(instrument: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted((case for case in instrument["cases"] if case["lane"] == "pure"), key=lambda row: row["case_id"])


def validate_package(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    instrument = package.get("instrument", {})
    cases = instrument.get("cases", [])
    ids = [case.get("case_id") for case in cases]
    if len(ids) != len(set(ids)):
        errors.append("case IDs must be unique")
    frozen = instrument.get("frozen_inventories", {})
    observed_pure = sorted(case["case_id"] for case in cases if case.get("lane") == "pure")
    observed_live = sorted(case["case_id"] for case in cases if case.get("lane") == "live")
    if observed_pure != frozen.get("pure_case_ids"):
        errors.append("frozen pure inventory differs from retained pure cases")
    if observed_live != frozen.get("live_case_ids"):
        errors.append("frozen live inventory differs from retained live cases")
    if canonical_sha256(pure_cases(instrument)) != CASE_CONTENT_SHA256:
        errors.append("frozen pure case content hash changed")
    if canonical_sha256(instrument.get("observer_contract", {})) != OBSERVER_CONTRACT_SHA256:
        errors.append("frozen observer contract hash changed")
    shape_ids = {shape["shape_id"] for shape in instrument.get("work_shapes", [])}
    if {case.get("shape_id") for case in cases} - shape_ids:
        errors.append("case references an unknown work shape")
    treatment_ids = [row.get("treatment_id") for row in instrument.get("treatments", [])]
    if len(treatment_ids) != len(set(treatment_ids)):
        errors.append("treatment IDs must be unique")
    true_claims = {key for key, value in instrument.get("claim_boundaries", {}).items() if value}
    if true_claims != ALLOWED_TRUE_CLAIMS:
        errors.append(f"unsupported claim boundary promotion: {sorted(true_claims - ALLOWED_TRUE_CLAIMS)}")
    for row in instrument.get("provenance", []):
        local_path = row.get("local_path")
        if local_path and not (PACKAGE.parents[2] / local_path).exists():
            errors.append(f"provenance path does not exist: {local_path}")
    return errors


def execute_case(case: dict[str, Any], operator: str = "baseline", scope: str = "all") -> dict[str, Any]:
    """Create a fresh stateless runtime and return exact component observations."""
    source = case["source"]
    resolved = "" if operator == "resolve_empty" and case["shape_id"] == scope else source
    normalized = resolved.strip()
    if operator == "equivalent_normalize":
        normalized = normalized.strip()
    persisted: str | None = normalized
    if operator == "persist_drop" and case["shape_id"] == scope:
        persisted = None
    actual = {"resolved": resolved, "normalized": normalized, "persisted": persisted}
    observers = {
        "source_contract": resolved == case["resolved"],
        "transform_contract": normalized == case["normalized"],
        "endpoint_contract": persisted == case["persisted"],
    }
    return {"case_id": case["case_id"], "shape_id": case["shape_id"], "actual": actual, "observers": observers}


def run_lane(instrument: dict[str, Any], operator: str = "baseline", scope: str = "all") -> list[dict[str, Any]]:
    return [execute_case(case, operator, scope) for case in pure_cases(instrument)]


def failed_observers(rows: list[dict[str, Any]]) -> list[str]:
    return sorted({f"{row['shape_id']}:{observer}" for row in rows for observer, passed in row["observers"].items() if not passed})


def treatment_result(instrument: dict[str, Any], treatment: dict[str, Any]) -> dict[str, Any]:
    base = {
        "treatment_id": treatment["treatment_id"],
        "kind": treatment["kind"],
        "lane": treatment["lane"],
    }
    kind = treatment["kind"]
    if kind == "live_only":
        return {**base, "disposition": "unavailable_live_only", "response_matrix": None, "failed_observers": [], "matches_predeclared_topology": None}
    if kind == "case_deletion":
        retained = [case for case in instrument["cases"] if case["case_id"] != treatment["case_id"]]
        intact = sorted(case["case_id"] for case in retained if case["lane"] == "pure") == instrument["frozen_inventories"]["pure_case_ids"]
        return {**base, "disposition": "invalid_instrument", "response_matrix": None, "failed_observers": [], "inventory_canary_passed": intact, "matches_predeclared_topology": not intact}
    if kind == "observer_defect":
        changed = copy.deepcopy(instrument["observer_contract"])
        changed["endpoint_contract"] = "always pass"
        intact = canonical_sha256(changed) == OBSERVER_CONTRACT_SHA256
        return {**base, "disposition": "invalid_observer", "response_matrix": None, "failed_observers": [], "observer_canary_passed": intact, "matches_predeclared_topology": not intact}
    rows = run_lane(instrument, treatment["operator"], treatment["shape_scope"])
    failed = failed_observers(rows)
    expected = sorted(treatment["expected_failed_observers"])
    prohibited = set(treatment["prohibited_failed_observers"])
    topology_matches = failed == expected and not (set(failed) & prohibited)
    if kind == "equivalent_no_effect":
        disposition = "equivalent_no_effect" if not failed and topology_matches else "unexpected_effect"
    else:
        disposition = "detected" if failed and topology_matches else "topology_mismatch"
    return {
        **base,
        "disposition": disposition,
        "response_matrix": rows,
        "failed_observers": failed,
        "expected_failed_observers": expected,
        "prohibited_failed_observers": sorted(prohibited),
        "matches_predeclared_topology": topology_matches,
    }


def replay(package: dict[str, Any] | None = None) -> dict[str, Any]:
    package = load() if package is None else package
    instrument = package["instrument"]
    errors = validate_package(package)
    baseline_first = run_lane(instrument)
    baseline_second = run_lane(instrument)
    baseline_all_pass = all(all(row["observers"].values()) for row in baseline_first)
    baseline_stable = baseline_first == baseline_second
    treatments = [treatment_result(instrument, row) for row in instrument["treatments"]]
    resolved_dispositions = {"detected", "invalid_observer", "invalid_instrument", "equivalent_no_effect", "unavailable_live_only"}
    return {
        "fixture_status": package["fixture_status"],
        "package_sha256": hashlib.sha256(PACKAGE.read_bytes()).hexdigest(),
        "instrument": {"instrument_id": instrument["instrument_id"], "version": instrument["version"]},
        "work_shapes": len(instrument["work_shapes"]),
        "pure_cases": len(pure_cases(instrument)),
        "live_cases": sum(case["lane"] == "live" for case in instrument["cases"]),
        "case_content_sha256": canonical_sha256(pure_cases(instrument)),
        "observer_contract_sha256": canonical_sha256(instrument["observer_contract"]),
        "validation_errors": errors,
        "baseline_canary": {"first_all_passed": baseline_all_pass, "second_equals_first": baseline_stable, "passed": baseline_all_pass and baseline_stable},
        "treatments": treatments,
        "all_pure_treatments_resolved": all(row["disposition"] in resolved_dispositions for row in treatments),
        "real_agent_attempts": 0,
        "real_side_effects": 0,
        "claim_boundaries": instrument["claim_boundaries"],
    }


def main() -> int:
    report = replay()
    print(json.dumps(report, indent=2, sort_keys=True))
    ok = not report["validation_errors"] and report["baseline_canary"]["passed"] and report["all_pure_treatments_resolved"]
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
