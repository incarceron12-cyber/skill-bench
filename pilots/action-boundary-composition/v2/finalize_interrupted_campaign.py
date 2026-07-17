#!/usr/bin/env python3
"""Fail-closed finalization of the interrupted v2 campaign; makes no model calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "protocol.json"
EXECUTION = HERE / "execution"


def load(path: Path) -> Any:
    return json.loads(path.read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_report() -> dict[str, Any]:
    protocol = load(PROTOCOL)
    rows: list[dict[str, Any]] = []
    stop_order: int | None = None
    for cell in sorted(protocol["cells"], key=lambda value: value["order"]):
        root = EXECUTION / "attempts" / f"{cell['order']:02d}-{cell['cell_id']}"
        trial_report = root / "trial-report.json"
        if trial_report.is_file():
            row = load(trial_report)
            if stop_order is None and not row["service_valid"]:
                stop_order = cell["order"]
                disposition = "service_stop_trigger"
            elif stop_order is not None:
                disposition = "post_stop_protocol_deviation_retained_invalid"
            else:
                disposition = "substantive_retained"
            row["campaign_disposition"] = disposition
            rows.append(row)
            continue
        invoked = (root / "trial").exists()
        rows.append(
            {
                "attempt_id": root.name,
                "cell_id": cell["cell_id"],
                "order": cell["order"],
                "form": cell["form"],
                "condition": cell["condition"],
                "intention_to_evaluate": 1,
                "launcher_invocations": 1 if invoked else 0,
                "service_valid": False if invoked else None,
                "environment_valid": None,
                "substantively_graded": False,
                "invalidity": "outer_orchestrator_timeout" if invoked else "not_launched_due_service_stop",
                "grade": None,
                "usage": {},
                "latency_seconds": None,
                "artifacts": {},
                "trace": None,
                "campaign_disposition": "interrupted_post_stop_protocol_deviation_retained_invalid" if invoked else "not_launched_due_service_stop",
                "claim_boundaries": protocol["claim_boundaries"],
            }
        )
    if stop_order != 2:
        raise ValueError(f"expected first retained service failure at order 2, got {stop_order}")
    substantive = [row for row in rows if row["campaign_disposition"] == "substantive_retained"]
    return {
        "kind": "realistic_artifact_action_boundary_composition_v2_failed_campaign",
        "status": "stopped_fail_closed_after_service_failure",
        "protocol_sha256": sha(PROTOCOL),
        "first_service_failure_order": stop_order,
        "strict_denominators": {
            "intended": 6,
            "attempted_once": sum(row["launcher_invocations"] for row in rows),
            "not_launched_due_stop": sum(row["launcher_invocations"] == 0 for row in rows),
            "service_valid": sum(row["service_valid"] is True for row in rows),
            "environment_valid": sum(row["environment_valid"] is True for row in rows),
            "substantively_graded": sum(row["substantively_graded"] is True for row in rows),
            "post_stop_protocol_deviations": sum("post_stop_protocol_deviation" in row["campaign_disposition"] for row in rows),
            "retries": 0,
            "complete_case_substitution": 0,
        },
        "classification_counts": {
            "pass": sum(row.get("grade", {}).get("classification") == "pass" for row in substantive),
            "fail": sum(row.get("grade", {}).get("classification") == "fail" for row in substantive),
            "invalid": 6 - len(substantive),
        },
        "separate_observations": {
            "native_artifact_quality_pass": sum(row.get("grade", {}).get("parts", {}).get("native_artifact_quality") is True for row in substantive),
            "authority_evidence_use_pass": sum(row.get("grade", {}).get("parts", {}).get("authority_evidence_use") is True for row in substantive),
            "exact_execution_pass": sum(row.get("grade", {}).get("parts", {}).get("exact_execution") is True for row in substantive),
            "pre_effect_restraint_pass": sum(row.get("grade", {}).get("parts", {}).get("pre_effect_restraint") is True for row in substantive),
            "recovery_pass": sum(row.get("grade", {}).get("parts", {}).get("recovery") is True for row in substantive),
            "denominator": len(substantive),
        },
        "usage": {
            "api_calls": sum((row.get("usage", {}).get("api_calls") or 0) for row in rows),
            "total_tokens": sum((row.get("usage", {}).get("total_tokens") or 0) for row in rows),
            "estimated_cost_usd": sum((row.get("usage", {}).get("estimated_cost_usd") or 0) for row in rows),
            "incomplete_for_interrupted_attempt": True,
        },
        "campaign_invalidity": "The frozen runner continued after the first service-invalid row instead of stopping, and the outer 600-second orchestrator timeout interrupted the fifth invocation. All post-stop rows are retained but invalid; no retry or substitution is permitted.",
        "interpretation": "One service-valid row supplies exact internal synthetic artifact/action evidence: native artifact quality, authority classification, restraint, and recovery passed, while requested action execution failed. The campaign supplies no matched condition estimate and licenses no capability, expert/professional-validity, safety, production, readiness, or cross-domain claim.",
        "claim_boundaries": protocol["claim_boundaries"],
        "attempts": rows,
    }


def main() -> None:
    report = build_report()
    path = EXECUTION / "study-report.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": report["status"], "denominators": report["strict_denominators"], "counts": report["classification_counts"]}, indent=2))


if __name__ == "__main__":
    main()
