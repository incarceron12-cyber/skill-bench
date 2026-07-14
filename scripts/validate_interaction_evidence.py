#!/usr/bin/env python3
"""Replay the domain-neutral interaction-evidence conformance observer.

The observer receives only frozen episode records.  The separate oracle is used
for conformance comparison after classification and is never an evaluator input.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "pilots/interaction-evidence-conformance/episodes.json"
DEFAULT_ORACLE = ROOT / "pilots/interaction-evidence-conformance/private/oracle.json"

REQUIRED_CONDITIONS = {"full_information", "no_channel", "scripted", "simulator"}
REQUIRED_OUTCOMES = {
    "unavailable",
    "unexercised",
    "ignored",
    "justified_rejection",
    "adopted_ineffective",
    "beneficial",
    "harmful_collateral_damage",
    "invalid_environment",
}
REQUIRED_LIMITS = {
    "human collaboration",
    "causal interaction benefit",
    "professional validity",
    "agent capability",
    "safety",
    "production fitness",
    "readiness",
}
REALIZATIONS = {"none", "scripted_policy", "model_simulator"}
TRIGGER_CLOCKS = {"environment_action", "model_turn", "wall_time", "authored_schedule"}
TRIGGER_TYPES = {"fixed_sentinel", "inspected_state", "subtask_boundary", "decision_point", "risk_signal"}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_hash(value: Any) -> str:
    return sha256_bytes(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())


def file_hash(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _classify(case: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> tuple[str, list[str]]:
    errors: list[str] = []
    env = case["environment"]
    channel = case["channel"]
    semantic = case["semantic_disposition"]
    endpoint = case["endpoint_observation"]
    repair = case["repair_observation"]

    if not env["valid"]:
        return "invalid_environment", errors
    if case["condition_id"] == "full_information" and not case["information_missing"]:
        return "full_information_control", errors
    if case["information_missing"] and not channel["available"]:
        return "unavailable", errors
    if channel["available"] and not channel["exercised"]:
        return "unexercised", errors
    if semantic["disposition"] == "ignored":
        return "ignored", errors
    if semantic["disposition"] == "rejected":
        if semantic.get("justified") and semantic.get("basis_evidence"):
            return "justified_rejection", errors
        errors.append(f"{case['case_id']}: rejection lacks a supported justification")
        return "unsupported_rejection", errors
    if semantic["disposition"] == "adopted":
        damaged = bool(repair["collateral_damage_loci"]) or any(
            not item["preserved"] for item in repair["preservation_observations"]
        )
        if damaged:
            return "harmful_collateral_damage", errors
        if not endpoint["target_satisfied"]:
            return "adopted_ineffective", errors
        effect = case["effect_evidence"]
        control = by_id.get(effect.get("matched_control_case_id"))
        if not control:
            errors.append(f"{case['case_id']}: beneficial classification lacks a matched control")
            return "adopted_ineffective", errors
        fixed = (
            control["scenario_id"] == case["scenario_id"]
            and control["work_shape"] == case["work_shape"]
            and control["condition_id"] == "no_channel"
            and control["environment"]["valid"]
            and not control["endpoint_observation"]["target_satisfied"]
            and effect.get("comparison_basis") == "frozen_synthetic_pair"
        )
        if fixed:
            return "beneficial", errors
        errors.append(f"{case['case_id']}: matched contrast does not support the planted benefit label")
        return "adopted_ineffective", errors
    errors.append(f"{case['case_id']}: unsupported semantic disposition")
    return "unclassified", errors


def semantic_errors(package: dict[str, Any], oracle: dict[str, Any], *, check_paths: bool = False) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    if package.get("status") != "internal_calibration_only":
        errors.append("status must remain internal_calibration_only")
    if not REQUIRED_LIMITS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("required claim limits are missing")
    if any(package.get("claims", {}).get(key) for key in ("human_participation", "causal_benefit", "professional_validity", "capability", "safety", "production_fitness", "readiness")):
        errors.append("synthetic conformance data cannot promote human or empirical claims")

    observer = package.get("observer", {})
    if observer.get("name") != "domain-neutral-interaction-observer-v1":
        errors.append("observer identity is not frozen")
    if "oracle" in observer.get("evaluator_inputs", []):
        errors.append("private oracle must remain outside evaluator inputs")
    oracle_ref = package.get("private_oracle", {})
    if oracle_ref.get("path") != str(DEFAULT_ORACLE.relative_to(ROOT)):
        errors.append("private oracle path is not frozen")
    elif DEFAULT_ORACLE.is_file() and oracle_ref.get("sha256") != file_hash(DEFAULT_ORACLE):
        errors.append("private oracle hash mismatch")

    conditions = {item.get("condition_id"): item for item in package.get("condition_matrix", [])}
    if set(conditions) != REQUIRED_CONDITIONS:
        errors.append("condition matrix must contain exactly the four frozen conditions")
    expected_vectors = {
        "full_information": (False, False, "none"),
        "no_channel": (True, False, "none"),
        "scripted": (True, True, "scripted_policy"),
        "simulator": (True, True, "model_simulator"),
    }
    for condition_id, vector in expected_vectors.items():
        item = conditions.get(condition_id, {})
        got = (item.get("information_missing"), item.get("channel_available"), item.get("participant_realization"))
        if got != vector:
            errors.append(f"{condition_id}: treatment vector drift")

    cases = package.get("cases", [])
    by_id = {case.get("case_id"): case for case in cases}
    if not cases or len(by_id) != len(cases) or None in by_id:
        errors.append("case ids must be unique and nonempty")
        return errors, {"valid": False, "classifications": [], "denominators": {}}
    if len({case.get("work_shape") for case in cases}) < 2:
        errors.append("at least two unlike work shapes are required")
    for shape in {case.get("work_shape") for case in cases}:
        observed = {case.get("condition_id") for case in cases if case.get("work_shape") == shape}
        if not REQUIRED_CONDITIONS <= observed:
            errors.append(f"{shape}: all four matched conditions are required")

    classifications: list[dict[str, Any]] = []
    for case in cases:
        case_id = case["case_id"]
        condition = conditions.get(case.get("condition_id"), {})
        requirements = case.get("public_requirements", [])
        if case.get("public_requirements_sha256") != canonical_hash(requirements):
            errors.append(f"{case_id}: public requirements hash mismatch")
        for state_name in ("initial_state", "final_state"):
            state = case.get(state_name, {})
            if state.get("sha256") != canonical_hash(state.get("content")):
                errors.append(f"{case_id}: {state_name} hash mismatch")

        if case.get("information_missing") != condition.get("information_missing"):
            errors.append(f"{case_id}: information treatment differs from condition matrix")
        participant = case.get("participant", {})
        if participant.get("realization") not in REALIZATIONS or participant.get("realization") != condition.get("participant_realization"):
            errors.append(f"{case_id}: participant realization mismatch")
        if participant.get("assigned_role") == "human" or participant.get("claim_label") == "human":
            errors.append(f"{case_id}: synthetic participant is mislabeled human")

        trigger = case.get("trigger", {})
        if trigger.get("clock_type") not in TRIGGER_CLOCKS or trigger.get("trigger_type") not in TRIGGER_TYPES:
            errors.append(f"{case_id}: trigger clock/type is invalid")
        if trigger.get("expected_value") != trigger.get("observed_value"):
            errors.append(f"{case_id}: trigger realization drift")

        channel = case.get("channel", {})
        if channel.get("available") != condition.get("channel_available"):
            errors.append(f"{case_id}: channel availability differs from condition matrix")
        message = case.get("message")
        receipt = case.get("receipt")
        if channel.get("exercised"):
            if not message or message.get("sha256") != sha256_bytes(message.get("content", "").encode()):
                errors.append(f"{case_id}: exercised channel lacks a hash-pinned message")
            if not receipt or not receipt.get("received") or receipt.get("message_sha256") != (message or {}).get("sha256"):
                errors.append(f"{case_id}: message/receipt hash mismatch")
        elif message is not None or receipt is not None:
            errors.append(f"{case_id}: unexercised channel cannot contain message or receipt evidence")

        semantic = case.get("semantic_disposition", {})
        propositions = semantic.get("propositions", [])
        if semantic.get("disposition") in {"adopted", "rejected", "ignored"}:
            if not receipt or not propositions:
                errors.append(f"{case_id}: semantic disposition cannot be inferred from endpoint alone")
        for proposition in propositions:
            if proposition.get("message_sha256") != (message or {}).get("sha256"):
                errors.append(f"{case_id}: proposition is not mapped to the received message")
            if proposition.get("required_authority") not in participant.get("authority_scope", []):
                errors.append(f"{case_id}: participant lacks proposition authority")
        if semantic.get("disposition") == "adopted" and not semantic.get("uptake_evidence", {}).get("trace_event_id"):
            errors.append(f"{case_id}: endpoint-only adoption inference is prohibited")

        repair = case.get("repair_observation", {})
        expected_loci = set(repair.get("expected_protected_loci", []))
        observations = repair.get("preservation_observations", [])
        observed_loci = {item.get("locus") for item in observations}
        if expected_loci != observed_loci:
            errors.append(f"{case_id}: state-damage/preservation ledger is incomplete")
        damaged = {item.get("locus") for item in observations if not item.get("preserved")}
        if damaged != set(repair.get("collateral_damage_loci", [])):
            errors.append(f"{case_id}: collateral-damage ledger does not match preservation observations")
        if semantic.get("disposition") == "adopted" and not repair.get("attempted"):
            errors.append(f"{case_id}: adopted proposition lacks attempted repair")

        burden = case.get("burden", {})
        if set(burden) != {"active_seconds", "wait_seconds", "interruptions", "correction_actions"} or any(not isinstance(value, int) or value < 0 for value in burden.values()):
            errors.append(f"{case_id}: plural burden fields must be nonnegative integers")
        if not case.get("endpoint_observation", {}).get("observer_event_id"):
            errors.append(f"{case_id}: endpoint observation is missing")

        outcome, local_errors = _classify(case, by_id)
        errors.extend(local_errors)
        classifications.append({"case_id": case_id, "work_shape": case["work_shape"], "condition_id": case["condition_id"], "outcome": outcome})

    expected = {item.get("case_id"): item.get("expected_outcome") for item in oracle.get("cases", [])}
    if set(expected) != set(by_id):
        errors.append("oracle and evaluator case inventories differ")
    for item in classifications:
        if expected.get(item["case_id"]) != item["outcome"]:
            errors.append(f"{item['case_id']}: observer got {item['outcome']!r}, oracle expected {expected.get(item['case_id'])!r}")
    observed_outcomes = {item["outcome"] for item in classifications}
    if not REQUIRED_OUTCOMES <= observed_outcomes:
        errors.append(f"planted outcome coverage missing: {sorted(REQUIRED_OUTCOMES - observed_outcomes)}")

    if check_paths:
        for item in package.get("provenance", []):
            candidate = ROOT / item["path"]
            if not candidate.is_file():
                errors.append(f"missing provenance path: {item['path']}")
            elif file_hash(candidate) != item["sha256"]:
                errors.append(f"provenance hash mismatch: {item['path']}")

    counts = Counter(item["outcome"] for item in classifications)
    valid_cases = [case for case in cases if case["environment"]["valid"]]
    opportunity = [case for case in valid_cases if case["information_missing"]]
    exercise = [case for case in opportunity if case["channel"]["available"]]
    uptake = [case for case in exercise if case["channel"]["exercised"] and case.get("receipt", {}).get("received")]
    effect = [case for case in uptake if case["semantic_disposition"]["disposition"] == "adopted" and case["effect_evidence"].get("matched_control_case_id")]
    burden = [case for case in valid_cases if case["channel"]["exercised"]]
    denominators = {
        "environment": {"all": len(cases), "valid": len(valid_cases), "invalid_retained": len(cases) - len(valid_cases)},
        "opportunity": {"eligible_missing_information": len(opportunity), "unavailable": counts["unavailable"]},
        "exercise": {"channel_available": len(exercise), "exercised": sum(case["channel"]["exercised"] for case in exercise)},
        "uptake": {"received_authorized_message": len(uptake), "adopted": sum(case["semantic_disposition"]["disposition"] == "adopted" for case in uptake)},
        "effect": {"matched_adopted_contrasts": len(effect), "beneficial": counts["beneficial"], "harmful": counts["harmful_collateral_damage"]},
        "burden": {
            "exercised_valid_episodes": len(burden),
            "active_seconds": sum(case["burden"]["active_seconds"] for case in burden),
            "wait_seconds": sum(case["burden"]["wait_seconds"] for case in burden),
            "interruptions": sum(case["burden"]["interruptions"] for case in burden),
            "correction_actions": sum(case["burden"]["correction_actions"] for case in burden),
        },
    }
    return errors, {"valid": not errors, "classifications": classifications, "outcome_counts": dict(sorted(counts.items())), "denominators": denominators}


def validate(fixture: Path = DEFAULT_FIXTURE, oracle_path: Path = DEFAULT_ORACLE, *, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(fixture.read_text())
    oracle = json.loads(oracle_path.read_text())
    errors, report = semantic_errors(package, oracle, check_paths=check_paths)
    report["errors"] = errors
    report["fixture_sha256"] = file_hash(fixture)
    report["oracle_sha256"] = file_hash(oracle_path)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--oracle", type=Path, default=DEFAULT_ORACLE)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate(args.fixture, args.oracle, check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered)
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
