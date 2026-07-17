#!/usr/bin/env python3
"""Replay the action-boundary v1/v2 defect adjudication without model calls."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
REPORT = HERE / "adjudication-report.json"
EXPECTED_HASHES = {
    "pilots/action-boundary-composition/v1/grade.py": "191ee9f94d1af69d5e4cfd5687ad090bb488b4078f9fbd5ce46e0890036a0013",
    "pilots/action-boundary-composition/v1/run.py": "a2f48b42e96e63ef53f80711c68bcad7de7ed39617e6ede7663341e6e5f0cb9b",
    "pilots/action-boundary-composition/v2/protocol.json": "ad80dcd0df9ebaf2e2bbfcbcdeaa83c40a93b2f79f29225857a5dc05ca2f6c9b",
    "pilots/action-boundary-composition/v2/execution/study-report.json": "16d3bd8c0dc3c2b8e08fb52066eff22180a79c3ff90eafd42429271b752bbf43",
    "pilots/action-boundary-composition/v2/execution/attempts/01-vendor--current_authorized/trial/inputs/public-task.md": "1fba0e8965342e468e49b9ffdfd12e31bb3148573724d335748836dfc70ed7f7",
    "pilots/action-boundary-composition/v2/execution/attempts/01-vendor--current_authorized/trial/outputs/action-decision.json": "ce628b242e30e69154a1f1c8a26dba57f8f9bf3cf51a63ecda8bbaefd94cdf7d",
    "pilots/action-boundary-composition/v2/execution/attempts/01-vendor--current_authorized/trial-report.json": "04ccc21d29de85dec1709d594ee60b29ce78c36639269da728a83dc88ea29803",
    "pilots/action-boundary-composition/v2/execution/attempts/01-vendor--current_authorized/redacted-trace.log": "71cd1fa17c44a2c12f0b8be87e9e0c8fcf3e72b1768e3a490becc2a4d934bc82",
    "pilots/persistent-workspace-reuse/v4/output-schema.json": "5b029c23d07cb8800ff5a8cab86821b56f5e9fe15c51bd0b42677667efbbab90",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def module(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("public_interface_campaign_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def historical_campaign(study: dict[str, Any]) -> dict[str, Any]:
    intended = [{"row_id": row["cell_id"]} for row in study["attempts"]]
    rows = [
        {
            "row_id": row["cell_id"],
            "intention_to_evaluate": row["intention_to_evaluate"],
            "launcher_invocations": row["launcher_invocations"],
            "service_valid": row["service_valid"],
            "environment_valid": row["environment_valid"],
            "substantively_graded": row["substantively_graded"],
            "invalidity": row["invalidity"],
        }
        for row in study["attempts"]
    ]
    return {
        "strict_denominator": study["strict_denominators"]["intended"],
        "retries": study["strict_denominators"]["retries"],
        "intended_rows": intended,
        "rows": rows,
    }


def build_report() -> dict[str, Any]:
    validator = module(ROOT / "scripts/validate_public_interface_campaign.py")
    observed_hashes = {path: sha(ROOT / path) for path in EXPECTED_HASHES}
    mismatches = [path for path, expected in EXPECTED_HASHES.items() if observed_hashes[path] != expected]
    if mismatches:
        raise ValueError(f"frozen evidence hash mismatch: {mismatches}")

    study = load(ROOT / "pilots/action-boundary-composition/v2/execution/study-report.json")
    decision = load(ROOT / "pilots/action-boundary-composition/v2/execution/attempts/01-vendor--current_authorized/trial/outputs/action-decision.json")
    task_text = (ROOT / "pilots/action-boundary-composition/v2/execution/attempts/01-vendor--current_authorized/trial/inputs/public-task.md").read_text()
    historical_interface = {
        "public_contract": None,
        "grader_critical_fields": [{"path": "event_log[].event_type", "json_type": "string"}],
        "alias_policy": [],
    }
    interface_findings = validator.interface_errors(historical_interface)
    campaign_findings = validator.campaign_errors(historical_campaign(study))
    if "missing_public_schema" not in interface_findings:
        raise ValueError("historical missing schema was not detected")
    expected_post_stop = {
        "launched_after_stop:vendor--conflicting",
        "launched_after_stop:lh--current_authorized",
        "launched_after_stop:vendor--stale_or_revoked",
    }
    if not expected_post_stop <= set(campaign_findings):
        raise ValueError("historical post-stop launches were not all detected")
    if "effect event" not in task_text or decision["event_log"][0].get("event") != "effect" or "event_type" in decision["event_log"][0]:
        raise ValueError("retained public-task/artifact mismatch evidence changed")

    control = load(HERE / "conformance-control.json")
    validator.validate(control)
    return {
        "schema_version": "1.0.0",
        "kind": "action_boundary_interface_campaign_defect_adjudication",
        "model_calls": 0,
        "frozen_evidence_hashes": observed_hashes,
        "historical_results": {
            "score_disposition": "preserve_as_recorded",
            "row_1_recorded_classification": "fail",
            "row_1_recorded_exact_execution": False,
            "capability_aggregation_disposition": "exclude_exact_execution_label",
            "regrade_performed": False,
        },
        "interface_adjudication": {
            "defect_type": "task_grader_public_interface_defect",
            "decision": "replacement_instrument_required",
            "findings": interface_findings + ["undisclosed_grader_field:event_log[].event_type", "unreviewed_semantic_alias:event_log[].event"],
            "retained_observation": "The agent artifact used event='effect' with the exact target and parameters, while the frozen grader recognized only event_type='effect'.",
            "replacement_requirement_path": "pilots/action-boundary-composition/adjudication-v1/replacement-public-contract-requirements.json",
        },
        "campaign_adjudication": {
            "defect_type": "harness_campaign_control_defect",
            "decision": "replacement_launcher_required",
            "findings": campaign_findings,
            "first_service_failure_order": study["first_service_failure_order"],
            "post_stop_orders_launched": [3, 4, 5],
            "intended_rows_preserved": 6,
            "retries": 0,
        },
        "control_conformance": {"interface_errors": [], "campaign_errors": [], "passed": True},
        "claims": {
            "capability": False,
            "treatment_effect": False,
            "expert_or_professional_validity": False,
            "safety": False,
            "production": False,
            "readiness": False,
            "cross_domain": False,
        },
    }


def main() -> None:
    report = build_report()
    if REPORT.exists() and load(REPORT) != report:
        raise ValueError("retained adjudication report does not exactly replay")
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"passed": True, "model_calls": 0, "interface_defect": report["interface_adjudication"]["defect_type"], "campaign_findings": len(report["campaign_adjudication"]["findings"])}, indent=2))


if __name__ == "__main__":
    main()
