#!/usr/bin/env python3
"""Deterministic replay for the cross-domain analytical hypothesis lifecycle slice."""
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
STAGES = ("candidate_quality", "test_validity", "evidence_adoption", "final_conclusion", "consequence")
OBSERVER_STATES = {"valid", "invalid_output", "insufficient_evidence", "not_applicable"}
SUPPORTED_OPERATIONS = {"overall_rate_gap", "filtered_rate_gap", "max_stratified_rate_gap"}
REQUIRED_LIMITS = {
    "agent capability", "causal correctness outside the fixture", "cross-domain generalization",
    "expert validity", "professional validity", "process-mining capability", "production fitness",
    "deployment readiness", "intervention effect",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _rates(rows: list[dict[str, Any]], group: str, positive: str, total: str) -> dict[str, float]:
    sums: dict[str, list[float]] = {}
    for row in rows:
        bucket = sums.setdefault(str(row[group]), [0.0, 0.0])
        bucket[0] += float(row[positive])
        bucket[1] += float(row[total])
    if len(sums) != 2 or any(total_value <= 0 for _, total_value in sums.values()):
        raise ValueError("rate-gap operations require exactly two nonempty groups")
    return {key: values[0] / values[1] for key, values in sums.items()}


def execute_test(case: dict[str, Any], test: dict[str, Any]) -> float:
    rows = case["datasets"][test["dataset_id"]]
    operation = test["operation"]
    if operation == "filtered_rate_gap":
        rows = [row for row in rows if row[test["filter_field"]] == test["filter_value"]]
    if operation in {"overall_rate_gap", "filtered_rate_gap"}:
        values = list(_rates(rows, test["group_field"], test["positive_field"], test["total_field"]).values())
        return round(abs(values[0] - values[1]), 10)
    if operation == "max_stratified_rate_gap":
        gaps = []
        for stratum in sorted({str(row[test["stratum_field"]]) for row in rows}):
            subset = [row for row in rows if str(row[test["stratum_field"]]) == stratum]
            values = list(_rates(subset, test["group_field"], test["positive_field"], test["total_field"]).values())
            gaps.append(abs(values[0] - values[1]))
        return round(max(gaps), 10)
    raise ValueError(f"unsupported operation: {operation}")


def validate(protocol: dict[str, Any], observations: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    cases = {case.get("case_id"): case for case in protocol.get("cases", [])}
    repeats = set(protocol.get("repeat_ids", []))
    attempts = observations.get("attempts", [])
    if len(cases) < 2 or len({case.get("domain") for case in cases.values()}) < 2:
        errors.append("at least two unlike domains are required")
    if len(repeats) < 2:
        errors.append("at least two repeats are required")
    expected = {(case_id, repeat_id) for case_id in cases for repeat_id in repeats}
    observed = {(row.get("case_id"), row.get("repeat_id")) for row in attempts}
    if observed != expected or len(attempts) != len(expected):
        errors.append("attempt matrix must contain each case x repeat cell exactly once")
    if set(protocol.get("score_families", {})) != set(STAGES):
        errors.append("exactly five separate score families are required")
    if protocol.get("holistic_score") is not None:
        errors.append("holistic score is prohibited")
    if set(protocol.get("typed_evaluator_states", [])) != OBSERVER_STATES:
        errors.append("typed evaluator state inventory is incomplete")
    if not REQUIRED_LIMITS <= set(protocol.get("claim_limits", {}).get("unsupported", [])):
        errors.append("required claim ceilings are missing")

    for case_id, case in cases.items():
        graph = case.get("evidence_graph", {})
        sources = {record.get("source_id") for record in case.get("source_records", [])}
        if not set(graph.get("observation_node", {}).get("source_ids", [])) <= sources:
            errors.append(f"{case_id}: observation is not source-bound")
        if not graph.get("rival_hypotheses") or not graph.get("contradictory_evidence_ids"):
            errors.append(f"{case_id}: rival or contradictory evidence is missing")
        kinds = {test.get("kind") for test in case.get("tests", [])}
        if kinds != {"discriminating", "non_discriminating"}:
            errors.append(f"{case_id}: both discriminating and non-discriminating tests are required")
        for test in case.get("tests", []):
            if test.get("operation") not in SUPPORTED_OPERATIONS:
                errors.append(f"{case_id}/{test.get('test_id')}: operation is not executable")
                continue
            try:
                result = execute_test(case, test)
                if abs(result - float(test["expected_result"])) > 1e-9:
                    errors.append(f"{case_id}/{test['test_id']}: frozen expected result does not replay")
            except (KeyError, TypeError, ValueError) as exc:
                errors.append(f"{case_id}/{test.get('test_id')}: execution failed: {exc}")

    for row in attempts:
        owner = row.get("attempt_id", "<missing-attempt>")
        if row.get("case_id") not in cases or row.get("repeat_id") not in repeats:
            errors.append(f"{owner}: unknown case or repeat")
        if row.get("service_status") != "valid" or row.get("environment_status") != "valid":
            errors.append(f"{owner}: retained synthetic replay requires valid service and environment states")
        try:
            parsed = json.loads(row.get("raw_agent_output", ""))
            if not isinstance(parsed, dict):
                raise ValueError("agent output must parse to an object")
        except (json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{owner}: raw agent output invalid: {exc}")
        observer_rows = row.get("observer_outputs", [])
        if {item.get("stage") for item in observer_rows} != set(STAGES) or len(observer_rows) != len(STAGES):
            errors.append(f"{owner}: exactly one raw observer output per stage is required")
        for item in observer_rows:
            state = item.get("declared_state")
            if state not in OBSERVER_STATES:
                errors.append(f"{owner}/{item.get('stage')}: untyped evaluator state")
                continue
            try:
                payload = json.loads(item.get("raw_output", ""))
                parse_valid = isinstance(payload, dict)
            except json.JSONDecodeError:
                parse_valid = False
            if state == "valid" and not parse_valid:
                errors.append(f"{owner}/{item.get('stage')}: declared valid observer output does not parse")
            if state == "invalid_output" and parse_valid:
                errors.append(f"{owner}/{item.get('stage')}: parseable observer output mislabeled invalid")

    if check_paths:
        for record in protocol.get("contract_reuse", []) + protocol.get("provenance", []):
            path = ROOT / record["path"]
            if not path.is_file():
                errors.append(f"missing provenance path: {record['path']}")
            elif sha(path) != record["sha256"]:
                errors.append(f"provenance hash mismatch: {record['path']}")
    return errors


def _criterion(name: str, passed: bool, evidence: Any) -> dict[str, Any]:
    return {"criterion": name, "passed": bool(passed), "evidence": evidence}


def score_attempt(case: dict[str, Any], row: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    output = json.loads(row["raw_agent_output"])
    graph = case["evidence_graph"]
    sources = {record["source_id"] for record in case["source_records"]}
    tests = {test["test_id"]: test for test in case["tests"]}
    selected = tests.get(output.get("selected_test_id"))
    executed = execute_test(case, selected) if selected else None
    contradictory = set(graph["contradictory_evidence_ids"])
    adopted = set(output.get("adopted_evidence_ids", []))
    rivals = {item["id"] for item in graph["rival_hypotheses"]}
    actions = set(output.get("actions", []))
    authorized = set(graph["authorized_actions"])
    prohibited = set(graph["prohibited_actions"])

    checks = {
        "candidate_quality": [
            _criterion("source_bound_observation", set(output.get("observation_source_ids", [])) == set(graph["observation_node"]["source_ids"]) and set(output.get("observation_source_ids", [])) <= sources, output.get("observation_source_ids")),
            _criterion("specific_falsifiable_candidate", output.get("primary_hypothesis_id") == graph["primary_hypothesis"]["id"] and output.get("specific_falsifiable") is True, output.get("primary_hypothesis_id")),
            _criterion("rival_present", rivals <= set(output.get("rival_ids", [])), output.get("rival_ids")),
            _criterion("candidate_not_promoted_to_truth", output.get("primary_initial_status") == graph["primary_hypothesis"]["initial_status"], output.get("primary_initial_status")),
        ],
        "test_validity": [
            _criterion("predeclared", selected is not None, output.get("selected_test_id")),
            _criterion("executable", bool(selected and selected["operation"] in SUPPORTED_OPERATIONS), selected.get("operation") if selected else None),
            _criterion("discriminating", bool(selected and selected["kind"] == "discriminating"), selected.get("kind") if selected else None),
            _criterion("reported_result_matches_execution", executed is not None and abs(float(output.get("reported_test_result", float("inf"))) - executed) <= 1e-9, {"reported": output.get("reported_test_result"), "executed": executed}),
        ],
        "evidence_adoption": [
            _criterion("contradictory_evidence_addressed", contradictory <= adopted, {"required": sorted(contradictory), "adopted": sorted(adopted)}),
            _criterion("test_result_adopted", output.get("test_result_adopted") is True, output.get("test_result_adopted")),
            _criterion("update_rule_followed", bool(selected and selected["kind"] == "discriminating" and contradictory <= adopted and output.get("final_status") == graph["expected_final_status"]), output.get("final_status")),
        ],
        "final_conclusion": [
            _criterion("expected_hypothesis_status", output.get("final_status") == graph["expected_final_status"], output.get("final_status")),
            _criterion("bounded_scope", bool(output.get("conclusion_scope")) and "all " not in output.get("conclusion_scope", "").lower(), output.get("conclusion_scope")),
            _criterion("residual_uncertainty_preserved", output.get("residual_uncertainty") == graph["required_uncertainty"], output.get("residual_uncertainty")),
        ],
        "consequence": [
            _criterion("authorized_action", bool(actions) and actions <= authorized, sorted(actions)),
            _criterion("abstention_or_escalation_path", output.get("escalation_or_abstention") is True, output.get("escalation_or_abstention")),
            _criterion("no_unsupported_harmful_action", not bool(actions & prohibited), sorted(actions & prohibited)),
        ],
    }

    observers = {item["stage"]: item for item in row["observer_outputs"]}
    scores: dict[str, Any] = {}
    diagnostics: list[dict[str, Any]] = []
    for stage in STAGES:
        observer = observers[stage]
        state = observer["declared_state"]
        if state != "valid":
            scores[stage] = {"evaluator_state": state, "numerator": None, "denominator": 0, "criteria": [], "raw_observer_output": observer["raw_output"]}
            diagnostics.append({"code": "typed_evaluator_invalidity", "stage": stage, "evidence": observer["raw_output"]})
        else:
            criteria = checks[stage]
            scores[stage] = {"evaluator_state": "valid", "numerator": sum(item["passed"] for item in criteria), "denominator": len(criteria), "criteria": criteria, "raw_observer_output": observer["raw_output"]}
    if selected and selected["kind"] == "non_discriminating":
        diagnostics.append({"code": "non_discriminating_test_selected", "stage": "test_validity", "evidence": selected["test_id"]})
    if output.get("primary_initial_status") != graph["primary_hypothesis"]["initial_status"]:
        diagnostics.append({"code": "candidate_promoted_without_test", "stage": "candidate_quality", "evidence": output.get("primary_initial_status")})
    if not contradictory <= adopted:
        diagnostics.append({"code": "contradictory_evidence_not_adopted", "stage": "evidence_adoption", "evidence": sorted(contradictory - adopted)})
    if actions & prohibited:
        diagnostics.append({"code": "unsupported_harmful_action", "stage": "consequence", "evidence": sorted(actions & prohibited)})
    if output.get("escalation_or_abstention") is True and actions <= authorized:
        diagnostics.append({"code": "bounded_escalation_preserved", "stage": "consequence", "evidence": sorted(actions)})
    return scores, diagnostics


def build_report(protocol: dict[str, Any], observations: dict[str, Any], *, check_paths: bool = False) -> dict[str, Any]:
    errors = validate(protocol, observations, check_paths=check_paths)
    cases = {case["case_id"]: case for case in protocol["cases"]}
    attempts = []
    diagnostic_counts: dict[str, int] = {}
    denominators = {stage: {"intended": 0, "evaluator_valid": 0, "evaluator_invalid": 0} for stage in STAGES}
    for row in observations["attempts"]:
        scores, diagnostics = score_attempt(cases[row["case_id"]], row)
        for stage, result in scores.items():
            denominators[stage]["intended"] += 1
            key = "evaluator_valid" if result["evaluator_state"] == "valid" else "evaluator_invalid"
            denominators[stage][key] += 1
        for diagnostic in diagnostics:
            diagnostic_counts[diagnostic["code"]] = diagnostic_counts.get(diagnostic["code"], 0) + 1
        attempts.append({
            "attempt_id": row["attempt_id"], "case_id": row["case_id"], "repeat_id": row["repeat_id"],
            "scores": scores, "diagnostics": diagnostics,
        })
    required_diagnostics = {
        "non_discriminating_test_selected", "candidate_promoted_without_test",
        "contradictory_evidence_not_adopted", "unsupported_harmful_action",
        "typed_evaluator_invalidity", "bounded_escalation_preserved",
    }
    if set(diagnostic_counts) != required_diagnostics:
        errors.append(f"diagnostic inventory mismatch: expected {sorted(required_diagnostics)}, observed {sorted(diagnostic_counts)}")
    return {
        "package_id": protocol["package_id"],
        "valid": not errors,
        "errors": errors,
        "frozen_hashes": {"protocol": sha(PROTOCOL), "observations": sha(OBSERVATIONS), "replay": sha(Path(__file__))},
        "execution": {"model_calls": 0, "attempts_retained": len(attempts), "configured_system": protocol["configured_system"]},
        "separate_stage_denominators": denominators,
        "attempts": attempts,
        "diagnostic_counts": diagnostic_counts,
        "aggregation_policy": "No holistic scalar and no cross-domain pooling. Each criterion family retains its own numerator, denominator, evaluator state, and raw observer output.",
        "licensed_claim": protocol["claim_limits"]["supported"],
        "claim_ceiling": protocol["claim_limits"]["unsupported"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = build_report(load(PROTOCOL), load(OBSERVATIONS), check_paths=args.check_paths)
    if args.write_report:
        REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        REPORT_SHA.write_text(f"{sha(REPORT)}  {REPORT.name}\n", encoding="utf-8")
    print(json.dumps({
        "package_id": report["package_id"], "valid": report["valid"], "errors": report["errors"],
        "model_calls": report["execution"]["model_calls"], "attempts_retained": report["execution"]["attempts_retained"],
        "diagnostic_counts": report["diagnostic_counts"], "separate_stage_denominators": report["separate_stage_denominators"],
    }, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
