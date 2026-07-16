#!/usr/bin/env python3
"""Deterministic replay for mediated-evaluator attribution and selection boundaries."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROTOCOL = HERE / "protocol.json"
OBSERVATIONS = HERE / "observations.json"
REPORT = HERE / "report.json"
REPORT_SHA = HERE / "report.sha256"
TERMINAL_STATES = {"pass", "fail", "unknown", "invalid", "not_attempted"}
REQUIRED_LIMITS = {
    "agent capability", "candidate quality outside the fixture", "cross-domain generalization",
    "expert validity", "mediator superiority", "professional validity", "production fitness",
    "deployment readiness",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(protocol: dict[str, Any], observations: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    candidates = set(protocol.get("candidates", []))
    mediators = {x.get("id") for x in protocol.get("mediators", [])}
    cases = {x.get("case_id"): x for x in observations.get("cases", [])}
    if len(protocol.get("work_shapes", [])) < 2 or len({x.get("domain") for x in protocol.get("work_shapes", [])}) < 2:
        errors.append("at least two unlike domains are required")
    if len(cases) < 5:
        errors.append("at least five adversarial cases are required")
    expected_pairs = {(case_id, candidate, mediator) for case_id in cases for candidate in candidates for mediator in mediators}
    observed_pairs = {(x.get("case_id"), x.get("candidate"), x.get("mediator")) for x in observations.get("attempts", [])}
    if observed_pairs != expected_pairs or len(observations.get("attempts", [])) != len(expected_pairs):
        errors.append("attempt matrix must contain each case x candidate x mediator cell exactly once")
    expected_diags = {d for case in cases.values() for d in case.get("expected_diagnostics", [])}
    if expected_diags != set(protocol.get("required_diagnostics", [])):
        errors.append("case diagnostic inventory does not equal protocol inventory")
    if not REQUIRED_LIMITS <= set(protocol.get("claim_limits", {}).get("unsupported", [])):
        errors.append("required claim limits are missing")
    if set(protocol.get("typed_states", [])) != TERMINAL_STATES:
        errors.append("typed outcome state inventory is incomplete")
    for case in cases.values():
        if set(case.get("mediator_valid", {})) != mediators:
            errors.append(f"{case.get('case_id')}: mediator-valid ledger is incomplete")
        if not isinstance(case.get("source_population"), bool) or not isinstance(case.get("projectable"), bool):
            errors.append(f"{case.get('case_id')}: source/projectable states must be typed booleans")
    for row in observations.get("attempts", []):
        statuses = {x.get("status") for x in row.get("checks", [])}
        if not statuses or not statuses <= TERMINAL_STATES:
            errors.append(f"{row.get('case_id')}/{row.get('candidate')}/{row.get('mediator')}: untyped check state")
        valid = cases.get(row.get("case_id"), {}).get("mediator_valid", {}).get(row.get("mediator"))
        not_attempted = row.get("attempt_status") == "not_attempted_mediator_invalid"
        if valid is False and not not_attempted:
            errors.append(f"{row.get('case_id')}/{row.get('mediator')}: invalid mediator cell was attempted")
        if valid is True and not_attempted:
            errors.append(f"{row.get('case_id')}/{row.get('mediator')}: valid mediator cell was silently dropped")
        if row.get("uptake") == "used" and row.get("action_source") == "none":
            errors.append(f"{row.get('case_id')}: uptake lacks candidate-to-action edge")
        if row.get("uptake") != "used" and str(row.get("action_source", "")).startswith("candidate-claim"):
            errors.append(f"{row.get('case_id')}: action claims candidate provenance without uptake")
    if check_paths:
        for record in protocol.get("contract_reuse", []) + protocol.get("provenance", []):
            path = ROOT / record["path"]
            if not path.is_file():
                errors.append(f"missing provenance path: {record['path']}")
            elif sha(path) != record["sha256"]:
                errors.append(f"provenance hash mismatch: {record['path']}")
    return errors


def scored(row: dict[str, Any]) -> bool:
    return row["attempt_status"] not in {"invalid_output", "completed_unknown_observer", "not_attempted_mediator_invalid"} and all(
        check["status"] in {"pass", "fail"} for check in row["checks"]
    )


def endpoint_success(row: dict[str, Any]) -> bool:
    return scored(row) and all(check["status"] == "pass" for check in row["checks"])


def diagnostics(protocol: dict[str, Any], observations: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cases = {x["case_id"]: x for x in observations["cases"]}
    found: list[dict[str, Any]] = []
    for row in observations["attempts"]:
        case = cases[row["case_id"]]
        locator = f"{row['case_id']}::{row['candidate']}::{row['mediator']}"
        if endpoint_success(row) and row["uptake"] != "used":
            found.append({"code": "endpoint_success_without_candidate_uptake", "locator": locator, "evidence": "check passed but uptake was ignored"})
        if row["claim_count"] == 1 and len(row["checks"]) > 1 and endpoint_success(row):
            found.append({"code": "one_claim_satisfies_multiple_checks", "locator": locator, "evidence": [x["id"] for x in row["checks"]]})
        if case["semantic_alternative_valid"] and row["semantic_check"] == "pass" and any(x["status"] == "fail" for x in row["checks"]):
            found.append({"code": "valid_alternative_rejected_by_projected_oracle", "locator": locator, "evidence": "semantic check passed while projected implementation check failed"})
        cost = row["unsupported_claims"] + row["collateral_cost"]
        if endpoint_success(row) and cost > 0:
            found.append({"code": "positive_success_with_noncompensatory_cost_failure", "locator": locator, "evidence": {"unsupported_claims": row["unsupported_claims"], "collateral_cost": row["collateral_cost"]}})

    rates: dict[str, dict[str, dict[str, Any]]] = {}
    for mediator in (x["id"] for x in protocol["mediators"]):
        rates[mediator] = {}
        for candidate in protocol["candidates"]:
            rows = [x for x in observations["attempts"] if x["mediator"] == mediator and x["candidate"] == candidate]
            eligible = [x for x in rows if scored(x)]
            successes = sum(endpoint_success(x) for x in eligible)
            attributable = sum(
                endpoint_success(x) and x["uptake"] == "used" and x["unsupported_claims"] == 0 and x["collateral_cost"] == 0
                for x in eligible
            )
            rates[mediator][candidate] = {
                "selected_projected_check_pass_numerator": successes,
                "scored_denominator": len(eligible),
                "selected_projected_check_pass_rate": successes / len(eligible) if eligible else None,
                "attributable_noncompensatory_pass_numerator": attributable,
                "attributable_noncompensatory_pass_rate": attributable / len(eligible) if eligible else None,
                "unsupported_claims": sum(x["unsupported_claims"] for x in rows),
                "collateral_cost": sum(x["collateral_cost"] for x in rows),
            }
    alpha, beta = [x["id"] for x in protocol["mediators"]]
    a, b = protocol["candidates"]
    reversal = (
        rates[alpha][a]["selected_projected_check_pass_rate"] > rates[alpha][b]["selected_projected_check_pass_rate"]
        and rates[beta][a]["selected_projected_check_pass_rate"] < rates[beta][b]["selected_projected_check_pass_rate"]
    )
    if reversal:
        found.append({"code": "mediator_rank_reversal", "locator": f"{alpha}<->{beta}", "evidence": rates})
    return found, rates


def build_report(protocol: dict[str, Any], observations: dict[str, Any], *, check_paths: bool = False) -> dict[str, Any]:
    errors = validate(protocol, observations, check_paths=check_paths)
    found, rates = diagnostics(protocol, observations)
    found_codes = {x["code"] for x in found}
    required = set(protocol["required_diagnostics"])
    if found_codes != required:
        errors.append(f"diagnostics mismatch: expected {sorted(required)}, observed {sorted(found_codes)}")
    cases = observations["cases"]
    funnels: dict[str, dict[str, dict[str, int]]] = {}
    for mediator in (x["id"] for x in protocol["mediators"]):
        funnels[mediator] = {}
        for candidate in protocol["candidates"]:
            rows = [x for x in observations["attempts"] if x["mediator"] == mediator and x["candidate"] == candidate]
            funnels[mediator][candidate] = {
                "source_population": sum(x["source_population"] for x in cases),
                "projectable": sum(x["source_population"] and x["projectable"] for x in cases),
                "mediator_valid": sum(x["source_population"] and x["projectable"] and x["mediator_valid"][mediator] for x in cases),
                "attempted": sum(x["attempt_status"] != "not_attempted_mediator_invalid" for x in rows),
                "scored": sum(scored(x) for x in rows),
            }
    state_counts = {state: 0 for state in sorted(TERMINAL_STATES)}
    for row in observations["attempts"]:
        for check in row["checks"]:
            state_counts[check["status"]] += 1
    chains = [{
        "attempt_id": f"{x['case_id']}::{x['candidate']}::{x['mediator']}",
        "candidate_node": f"{x['candidate']}:claims={x['claim_count']}",
        "uptake_edge": x["uptake"],
        "action_node": x["action_source"],
        "check_edges": [{"check_id": c["id"], "outcome": c["status"]} for c in x["checks"]],
        "endpoint_success": endpoint_success(x),
        "attribution_credit": endpoint_success(x) and x["uptake"] == "used" and x["unsupported_claims"] == 0 and x["collateral_cost"] == 0,
    } for x in observations["attempts"]]
    return {
        "package_id": protocol["package_id"],
        "valid": not errors,
        "errors": errors,
        "frozen_hashes": {"protocol": sha(PROTOCOL), "observations": sha(OBSERVATIONS), "replay": sha(Path(__file__))},
        "contract_reuse": protocol["contract_reuse"],
        "funnel_denominators": funnels,
        "typed_check_state_counts": state_counts,
        "candidate_uptake_action_check_chains": chains,
        "diagnostics": found,
        "metric_results": rates,
        "noncompensatory_policy": "Positive projected-check success never erases unsupported-claim or collateral-change cost; attribution credit is reported separately.",
        "licensed_claim": protocol["claim_limits"]["supported"],
        "claim_ceiling": protocol["claim_limits"]["unsupported"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = build_report(load(PROTOCOL), load(OBSERVATIONS), check_paths=args.check_paths)
    if args.write_report:
        REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        REPORT_SHA.write_text(f"{sha(REPORT)}  {REPORT.name}\n")
    print(json.dumps({
        "package_id": report["package_id"], "valid": report["valid"], "errors": report["errors"],
        "diagnostics": sorted({x["code"] for x in report["diagnostics"]}),
        "funnel_denominators": report["funnel_denominators"],
    }, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
