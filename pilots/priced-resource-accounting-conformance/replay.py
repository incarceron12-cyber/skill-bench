#!/usr/bin/env python3
"""Deterministic fail-closed replay for partial priced-resource accounting."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DEFAULT_PACKAGE = HERE / "package.json"
DEFAULT_RATES = HERE / "rate-sheet.json"
REQUIRED_BASES = {
    "realized_ledger", "reconstructed_rate", "list_price",
    "cached_counterfactual", "amortized_estimate", "human_estimate",
}
BLOCKED_CLAIMS = {"efficiency", "utility", "operational_fit", "risk", "total_cost", "professional_validity"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=0, abs_tol=1e-9)


def safe_ratio(numerator: float, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def replay(package: dict[str, Any] | None = None, rates: dict[str, Any] | None = None, *, check_paths: bool = False) -> dict[str, Any]:
    if package is None:
        package = json.loads(DEFAULT_PACKAGE.read_text())
    if rates is None:
        rates = json.loads(DEFAULT_RATES.read_text())
    errors: list[str] = []

    if package.get("status") != "internal_builder_authored_calibration_only" or package.get("zero_call") is not True:
        errors.append("package must remain explicit zero-call internal calibration")
    campaigns = {row.get("campaign_id"): row for row in package.get("campaigns", [])}
    if len(campaigns) < 2 or len({row.get("work_shape") for row in campaigns.values()}) < 2:
        errors.append("at least two structurally unlike campaigns are required")
    if package.get("rate_sheet", {}).get("rate_sheet_id") != rates.get("rate_sheet_id") or package.get("rate_sheet", {}).get("version") != rates.get("version"):
        errors.append("rate-sheet identity drift")

    rate_by_id = {row.get("rate_id"): row for row in rates.get("rates", [])}
    if len(rate_by_id) != len(rates.get("rates", [])):
        errors.append("rate IDs must be unique")
    if {row.get("price_basis") for row in rates.get("rates", [])} != REQUIRED_BASES:
        errors.append("rate sheet must preserve all six distinct price bases")

    assignments: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for campaign in campaigns.values():
        consequence = campaign.get("consequence_observation", {})
        if consequence.get("observed") is not False or any(consequence.get(key) is not None for key in ("stakeholder_artifact_accepted", "downstream_loss_or_benefit", "risk_or_side_effect")):
            errors.append(f"{campaign.get('campaign_id')}: synthetic artifact status was laundered into stakeholder consequence")
        for assignment in campaign.get("assignments", []):
            aid = assignment.get("assignment_id")
            if aid in assignments:
                errors.append(f"duplicate assignment ID: {aid}")
            assignments[aid] = (campaign, assignment)

    attempts = package.get("attempts", [])
    attempt_ids = [row.get("attempt_id") for row in attempts]
    if len(attempt_ids) != len(set(attempt_ids)):
        errors.append("attempt IDs must be unique")
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    observed_bases: set[str] = set()
    observed_families: set[str] = set()
    totals: dict[str, dict[str, Any]] = {
        cid: {"assigned_cap": row["assigned_budget"]["cap"], "attempt_count": 0, "canonical_valid_count": 0, "success_count": 0, "campaign_charged_spend": 0.0, "retained_valid_charged_spend": 0.0, "counterfactual_priced_amount": 0.0, "omitted_or_transferred_priced_amount": 0.0, "wall_seconds": 0, "human_review_minutes_observed": 0.0}
        for cid, row in campaigns.items()
    }
    for attempt in attempts:
        aid = attempt.get("attempt_id", "<missing>")
        assignment_id = attempt.get("assignment_id")
        campaign_id = attempt.get("campaign_id")
        grouped[assignment_id].append(attempt)
        if assignment_id not in assignments:
            errors.append(f"{aid}: unknown assignment")
            continue
        expected_campaign = assignments[assignment_id][0]["campaign_id"]
        if campaign_id != expected_campaign:
            errors.append(f"{aid}: campaign/assignment mismatch")
            continue
        total = totals[campaign_id]
        total["attempt_count"] += 1
        total["wall_seconds"] += attempt.get("wall_seconds", 0)
        total["human_review_minutes_observed"] += attempt.get("human_review_minutes_observed", 0)
        valid = attempt.get("disposition") == "valid_scored"
        if attempt.get("valid_scored") is not valid:
            errors.append(f"{aid}: disposition and valid_scored disagree")
        if valid and attempt.get("success") not in {True, False}:
            errors.append(f"{aid}: valid scored attempt needs boolean success")
        if not valid and attempt.get("success") is not None:
            errors.append(f"{aid}: invalid/failed attempt cannot carry success")
        resources = attempt.get("resources", [])
        if not resources:
            errors.append(f"{aid}: resource ledger is empty")
        attempt_charge = 0.0
        for resource in resources:
            rid = resource.get("resource_id", "<missing>")
            rate = rate_by_id.get(resource.get("rate_id"))
            if rate is None:
                errors.append(f"{aid}/{rid}: unknown rate")
                continue
            if resource.get("price_basis") != rate.get("price_basis") or resource.get("resource_family") != rate.get("resource_family") or resource.get("unit") != rate.get("unit"):
                errors.append(f"{aid}/{rid}: rate, family, unit, or price-basis drift")
            if not resource.get("observation_source"):
                errors.append(f"{aid}/{rid}: observation source missing")
            if resource.get("cost_boundary") not in {"included", "omitted", "transferred"}:
                errors.append(f"{aid}/{rid}: invalid cost boundary")
            quantity = resource.get("quantity")
            if not isinstance(quantity, (int, float)) or quantity < 0:
                errors.append(f"{aid}/{rid}: invalid quantity")
                continue
            if rate.get("unit_price") is not None and not close(resource.get("priced_amount", -1), quantity * rate["unit_price"]):
                errors.append(f"{aid}/{rid}: priced amount does not replay from frozen rate")
            charge = resource.get("charged_spend")
            if not isinstance(charge, (int, float)) or charge < 0:
                errors.append(f"{aid}/{rid}: invalid charged spend")
                continue
            if resource.get("price_basis") in {"cached_counterfactual", "amortized_estimate", "human_estimate"} and charge != 0:
                errors.append(f"{aid}/{rid}: counterfactual/estimate was laundered into realized charge")
            if resource.get("cost_boundary") != "included" and charge != 0:
                errors.append(f"{aid}/{rid}: omitted/transferred amount cannot enter charged spend")
            observed_bases.add(resource["price_basis"])
            observed_families.add(resource["resource_family"])
            attempt_charge += charge
            if resource["price_basis"] == "cached_counterfactual":
                total["counterfactual_priced_amount"] += resource["priced_amount"]
            if resource["cost_boundary"] in {"omitted", "transferred"}:
                total["omitted_or_transferred_priced_amount"] += resource["priced_amount"]
        total["campaign_charged_spend"] += attempt_charge
        if attempt.get("canonical") and valid:
            total["canonical_valid_count"] += 1
            total["retained_valid_charged_spend"] += attempt_charge
            total["success_count"] += int(attempt["success"])

    for assignment_id, (campaign, assignment) in assignments.items():
        rows = grouped.get(assignment_id, [])
        if not rows:
            errors.append(f"{assignment_id}: assigned attempt missing")
            continue
        selected = [row for row in rows if row.get("canonical") is True]
        if len(selected) != 1 or selected[0].get("attempt_id") != assignment.get("canonical_attempt_id"):
            errors.append(f"{assignment_id}: canonical attempt selection mismatch")
        policy = assignment.get("retry_policy")
        if policy == "none" and (len(rows) != 1 or rows[0].get("replacement_for_attempt_id") is not None):
            errors.append(f"{assignment_id}: undeclared retry")
        if policy == "declared_canonical_attempt":
            if len(rows) < 2 or selected[0].get("replacement_for_attempt_id") not in {row.get("attempt_id") for row in rows if not row.get("canonical")}:
                errors.append(f"{assignment_id}: retry chain missing or ambiguous")

    if observed_bases != REQUIRED_BASES:
        errors.append("attempt rows do not exercise all six price bases")
    if not {"model_inference", "external_tool", "infrastructure", "human_review"} <= observed_families:
        errors.append("resource-family coverage is incomplete")

    for total in totals.values():
        for key in ("campaign_charged_spend", "retained_valid_charged_spend", "counterfactual_priced_amount", "omitted_or_transferred_priced_amount"):
            total[key] = round(total[key], 6)
        total["cost_per_attempt"] = safe_ratio(total["campaign_charged_spend"], total["attempt_count"])
        total["campaign_cost_per_valid"] = safe_ratio(total["campaign_charged_spend"], total["canonical_valid_count"])
        total["campaign_cost_per_success"] = safe_ratio(total["campaign_charged_spend"], total["success_count"])
        total["retained_valid_cost_per_success"] = safe_ratio(total["retained_valid_charged_spend"], total["success_count"])

    ordered = sorted(totals)
    higher = max(totals.items(), key=lambda item: item[1]["assigned_cap"])
    lower = min(totals.items(), key=lambda item: item[1]["assigned_cap"])
    higher_cap_lower_spend = higher[1]["assigned_cap"] > lower[1]["assigned_cap"] and higher[1]["campaign_charged_spend"] < lower[1]["campaign_charged_spend"]
    if not higher_cap_lower_spend:
        errors.append("planted higher-cap/lower-spend distinction is missing")
    retry_omission_preserved = any(t["campaign_charged_spend"] > t["retained_valid_charged_spend"] for t in totals.values())
    if not retry_omission_preserved:
        errors.append("failed retry was omitted from both campaign and retained-valid views")
    cached_counterfactual_preserved = any(t["counterfactual_priced_amount"] > 0 for t in totals.values())
    if not cached_counterfactual_preserved:
        errors.append("cached/free counterfactual price is missing")

    rank_by_attempt = sorted(ordered, key=lambda cid: totals[cid]["cost_per_attempt"])
    rank_by_valid = sorted(ordered, key=lambda cid: totals[cid]["campaign_cost_per_valid"])
    denominator_rank_reversal = rank_by_attempt != rank_by_valid
    if not denominator_rank_reversal:
        errors.append("denominator-choice rank reversal is missing")
    if package.get("report_policy", {}).get("one_dimensional_cost_rank") is not None:
        errors.append("one-dimensional cost ranking is prohibited")
    if package.get("denominator_policies") != ["all_attempt_records", "canonical_valid_scored", "canonical_successes", "retained_valid_only"]:
        errors.append("denominator policies were omitted or conflated")

    claims = package.get("claim_assertions", {})
    if claims.get("partial_priced_execution") is not True:
        errors.append("narrow partial-priced-execution claim is missing")
    for claim in BLOCKED_CLAIMS:
        if claims.get(claim) is not False:
            errors.append(f"unsupported claim upgrade: {claim}")
    decision = package.get("decision_policy", {})
    has_decision_basis = all(decision.get(key) is not None for key in ("frozen_loss_function", "frozen_acceptance_threshold", "stakeholder_consequence_evidence"))
    if has_decision_basis:
        errors.append("synthetic fixture must not fabricate stakeholder decision evidence")
    if not package.get("claim_ceiling"):
        errors.append("claim ceiling missing")

    if check_paths:
        rate_path = ROOT / package.get("rate_sheet", {}).get("path", "")
        if not rate_path.is_file() or sha256(rate_path) != sha256(DEFAULT_RATES):
            errors.append("rate-sheet path missing or differs from replayed bytes")
        for lock in package.get("component_locks", []):
            path = ROOT / lock.get("path", "")
            if not path.is_file():
                errors.append(f"missing locked source: {lock.get('path')}")
            elif sha256(path) != lock.get("sha256"):
                errors.append(f"locked source hash drift: {lock.get('path')}")

    report = {
        "schema_version": "1.0.0",
        "report_id": "priced-resource-accounting-conformance-report-v1",
        "valid": not errors,
        "errors": errors,
        "input_identity": {"package_sha256": sha256(DEFAULT_PACKAGE) if package == json.loads(DEFAULT_PACKAGE.read_text()) else "mutated_in_memory", "rate_sheet_sha256": sha256(DEFAULT_RATES)},
        "campaigns": {key: totals[key] for key in ordered},
        "price_bases_observed": sorted(observed_bases),
        "resource_families_observed": sorted(observed_families),
        "planted_distinctions": {
            "higher_cap_lower_spend": higher_cap_lower_spend,
            "failed_retry_separate_from_retained_valid_cost": retry_omission_preserved,
            "cached_counterfactual_separate_from_charge": cached_counterfactual_preserved,
            "denominator_rank_reversal": denominator_rank_reversal,
            "rank_by_campaign_cost_per_attempt": rank_by_attempt,
            "rank_by_campaign_cost_per_valid": rank_by_valid,
            "one_dimensional_rank": None,
        },
        "claim_disposition": {
            "supported": ["exact accounting of retained synthetic partial-priced execution rows"],
            "blocked": sorted(BLOCKED_CLAIMS | {"agent_capability", "safety", "production_fitness", "readiness", "cross_domain_generalization"}),
            "reason": "No frozen stakeholder loss/threshold or observed stakeholder consequence exists; price bases and denominators are non-interchangeable.",
        },
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    parser.add_argument("--rate-sheet", type=Path, default=DEFAULT_RATES)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--write-report", type=Path)
    parser.add_argument("--check-report", type=Path)
    args = parser.parse_args()
    package = json.loads(args.package.read_text())
    rates = json.loads(args.rate_sheet.read_text())
    report = replay(package, rates, check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        args.write_report.write_text(rendered)
    if args.check_report and (not args.check_report.is_file() or args.check_report.read_text() != rendered):
        report["valid"] = False
        report["errors"].append("retained report does not match deterministic replay")
        rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
