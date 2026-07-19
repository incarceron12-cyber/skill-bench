#!/usr/bin/env python3
"""Condition-blind endpoint/collateral checker for frozen calibration cases."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TERMINAL_STATES = {"passed", "criterion_fail", "invalid_artifact", "insufficient_evidence", "observer_invalid", "environment_invalid", "service_invalid"}


def evaluate(shape, candidate, view_status="available", observer_status="valid"):
    # Deliberately accepts no condition, assignment, prompt, or feedback argument.
    if observer_status != "valid":
        return {"terminal_state": "observer_invalid", "endpoint": None, "collateral": None}
    if view_status != "available":
        return {"terminal_state": "insufficient_evidence", "endpoint": None, "collateral": None}
    if shape == "memo":
        if not isinstance(candidate, str) or not candidate.strip():
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        normalized = " ".join(candidate.lower().replace("**", "").split())
        has_both = "north" in normalized and "south" in normalized
        selected_south = ("select south" in normalized or "recommend south" in normalized)
        has_cost = ("95,000" in normalized or "95000" in normalized)
        endpoint = selected_south and has_cost
        collateral = has_both
    elif shape == "structured":
        if not isinstance(candidate, dict) or not isinstance(candidate.get("allocations"), dict):
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        allocations = candidate["allocations"]
        if set(allocations) != {"ops", "research"} or any(type(v) is not int for v in allocations.values()) or type(candidate.get("declared_total")) is not int:
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        endpoint = sum(allocations.values()) == candidate["declared_total"] == 100 and allocations["ops"] <= 60 and allocations["research"] <= 40
        collateral = set(allocations) == {"ops", "research"}
    else:
        return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
    return {"terminal_state": "passed" if endpoint and collateral else "criterion_fail", "endpoint": endpoint, "collateral": collateral}


def replay(path=HERE / "fixtures" / "calibration.json"):
    data = json.loads(Path(path).read_text())
    rows = []
    for case in data["cases"]:
        result = evaluate(case["shape"], case["candidate"], case["view_status"], case["observer_status"])
        rows.append({"case_id": case["case_id"], "expected": case["expected"], **result})
    return rows


if __name__ == "__main__":
    rows = replay()
    print(json.dumps(rows, indent=2, sort_keys=True))
    raise SystemExit(0 if all(r["expected"] == r["terminal_state"] for r in rows) else 1)
