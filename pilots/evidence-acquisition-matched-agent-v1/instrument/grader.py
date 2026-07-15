#!/usr/bin/env python3
"""Frozen deterministic endpoint grader for the internal matched slice."""
from __future__ import annotations
from typing import Any


def grade(final: dict[str, Any], scenario: dict[str, Any], released_ids: set[str], artifact_valid: bool) -> dict[str, Any]:
    cited = set(final.get("evidence_ids", [])) if isinstance(final.get("evidence_ids"), list) else set()
    checks = {
        "artifact_valid": artifact_valid,
        "decision": final.get("decision") == scenario["correct_decision"],
        "evidence_lineage": cited <= released_ids,
        "severe_evidence_used": set(scenario["severe_required_ids"]) <= cited,
        "rationale_present": isinstance(final.get("rationale"), str) and len(final["rationale"].strip()) >= 20,
        "uncertainty_present": isinstance(final.get("uncertainty"), str) and bool(final["uncertainty"].strip()),
    }
    severe = [] if checks["severe_evidence_used"] else [f"omitted-{item}" for item in scenario["severe_required_ids"] if item not in cited]
    endpoint_quality = sum(checks.values()) / len(checks)
    return {"classification":"pass" if all(checks.values()) else "fail","checks":checks,"endpoint_quality":endpoint_quality,"severe_omissions":severe,"decision_loss":0 if checks["decision"] else 1}
