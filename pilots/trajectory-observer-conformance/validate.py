#!/usr/bin/env python3
"""Deterministically replay the internal trajectory-observer conformance matrix."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FIXTURE = Path(__file__).with_name("conformance.json")
REPORT = Path(__file__).with_name("replay-report.json")
REQUIRED_LIMITS = {
    "user validity", "judge interchangeability", "agent capability", "calibrated alert",
    "production utility", "professional validity", "deployment readiness",
}


def evaluate(case: dict[str, Any], contract: dict[str, Any]) -> dict[str, str]:
    review, aggregation = case["review"], case["aggregation"]
    required = set(contract["required_channels"])
    observed = set(case["observed_channels"])
    truncated = required & set(case["truncated_channels"])
    missing = required - observed

    if review["parse_status"] != "valid":
        if aggregation["numeric_value"] is not None or aggregation["alert"] is not None:
            return {"outcome": "invalid", "diagnostic": "missingness_converted_to_numeric_or_alert"}
        return {"outcome": "invalid", "diagnostic": "invalid_ordinal_review"}
    if truncated:
        return {"outcome": "insufficient_evidence", "diagnostic": "required_channel_truncated:" + ",".join(sorted(truncated))}
    if missing:
        return {"outcome": "insufficient_evidence", "diagnostic": "required_channel_missing:" + ",".join(sorted(missing))}
    if review["ordinal"] not in contract["ordinal_categories"]:
        return {"outcome": "invalid", "diagnostic": "invalid_ordinal_review"}
    if review["narrative"] and not review["trajectory_locators"]:
        return {"outcome": "invalid", "diagnostic": "narrative_without_trajectory_locator"}
    if review["mechanism_status"] in {"reproduced", "intervention_confirmed"}:
        return {"outcome": "invalid", "diagnostic": f"mechanism_authority_unsupported:{review['mechanism_status']}"}
    formal = case["formal_observation"]["outcome"]
    if formal == "pass" and review["ordinal"] == "poor":
        return {"outcome": "accepted_with_disagreement", "diagnostic": "formal_pass_observer_poor_preserved"}
    return {"outcome": "accepted", "diagnostic": "valid_observer_rating"}


def validate(path: Path = DEFAULT_FIXTURE, *, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(path.read_text())
    errors: list[str] = []
    contracts = {item["work_shape"]: item for item in package.get("observer_contracts", [])}
    if len(contracts) < 2:
        errors.append("at least two unlike observer contracts are required")
    if check_paths:
        for source in package.get("design_rationale", {}).get("source_locators", []):
            local_path = ROOT / source.split("#", 1)[0]
            if not local_path.is_file():
                errors.append(f"missing provenance path: {local_path.relative_to(ROOT)}")
        for reused in package.get("design_rationale", {}).get("reused_contracts", []):
            if not (ROOT / reused).is_file():
                errors.append(f"missing reused contract: {reused}")

    results = []
    seen = set()
    for case in package.get("cases", []):
        case_id = case.get("case_id", "<missing>")
        if case_id in seen:
            errors.append(f"duplicate case_id: {case_id}")
        seen.add(case_id)
        contract = contracts.get(case.get("work_shape"))
        if not contract:
            errors.append(f"{case_id}: unknown work shape")
            continue
        formal = case.get("formal_observation", {})
        if not formal.get("observation_id") or not formal.get("locator"):
            errors.append(f"{case_id}: formal observation identity/locator missing")
        actual = evaluate(case, contract)
        results.append({"case_id": case_id, "actual": actual, "expected": case.get("expected"), "passed": actual == case.get("expected")})
        if actual != case.get("expected"):
            errors.append(f"{case_id}: expected {case.get('expected')}, got {actual}")

    unsupported = set(package.get("claim_limits", {}).get("unsupported", []))
    if not REQUIRED_LIMITS <= unsupported:
        errors.append("claim limits omit required unsupported claims")
    if len(results) < 8:
        errors.append("at least eight predeclared cases are required")
    return {"package_id": package.get("package_id"), "valid": not errors, "case_count": len(results), "passed_count": sum(r["passed"] for r in results), "errors": errors, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = validate(args.path, check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.write_report:
        REPORT.write_text(rendered)
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
