#!/usr/bin/env python3
"""Replay the versioned downstream criterion-defect adjudication.

This module does not mutate the retained v2 grader or outcomes.  It evaluates a
new v3 semantic criterion set against builder-authored adversarial cases and the
two retained agent artifacts.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PILOT = Path(__file__).resolve().parent
DEFAULT = PILOT / "downstream-adjudication-v1.json"


def _norm(value: Any) -> str:
    return " ".join(str(value or "").lower().replace("‑", "-").split())


def risk_preserved_v2(value: dict[str, Any]) -> bool:
    """Require an affirmative >=30-day written-notice control, not token copying."""
    text = _norm(value.get("risk_control"))
    duration = re.search(r"(?:at least|minimum(?: of)?|no less than)\s+30\s*[- ]?days?", text)
    written_notice = "notice" in text and any(term in text for term in ("written", "send", "submit", "provide"))
    negated = any(term in text for term in ("ignore", "waive", "under 30", "less than 30", "after the exit"))
    return bool(duration and written_notice and not negated)


def owner_routing_v2(value: dict[str, Any], handoff: dict[str, Any]) -> bool:
    """Preserve action ownership and route the named confirmation separately."""
    owner = _norm(value.get("owner"))
    request = _norm(value.get("requested_confirmation"))
    source_owner = _norm(handoff.get("owner"))
    next_step = _norm(handoff.get("next_step"))
    return owner == source_owner and "database on-call" in request and "failover" in request and "database on-call" in next_step


def evaluate(case: dict[str, Any]) -> bool:
    if case["criterion"] == "risk_preserved_v2":
        return risk_preserved_v2(case["artifact"])
    if case["criterion"] == "owner_routing_v2":
        return owner_routing_v2(case["artifact"], case["handoff"])
    raise ValueError(f"unknown criterion: {case['criterion']}")


def replay(data: dict[str, Any], check_paths: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    results: list[dict[str, Any]] = []
    if data.get("status") != "internal_builder_adjudication_only":
        errors.append("status must remain internal_builder_adjudication_only")
    if data.get("immutability", {}).get("retained_v2_modified") is not False:
        errors.append("retained v2 evidence must remain immutable")
    for record in data.get("adjudications", []):
        required = {"public_basis", "intended_construct", "accepted_alternatives", "evidence_view", "observed_semantic_consequence", "disposition", "prior_outcome_effect"}
        missing = sorted(required - set(record))
        if missing:
            errors.append(f"{record.get('criterion_id')}: missing {missing}")
    for case in data.get("calibration_cases", []):
        observed = evaluate(case)
        results.append({"id": case["id"], "observed": observed, "expected": case["expected"]})
        if observed is not case["expected"]:
            errors.append(f"{case['id']}: observed {observed}, expected {case['expected']}")
    retained: list[dict[str, Any]] = []
    for item in data.get("retained_replays", []):
        artifact_path, handoff_path = ROOT / item["artifact_path"], ROOT / item["handoff_path"]
        if check_paths and (not artifact_path.is_file() or not handoff_path.is_file()):
            errors.append(f"missing retained replay path: {item['id']}")
            continue
        case = {"criterion": item["criterion"], "artifact": json.loads(artifact_path.read_text()), "handoff": json.loads(handoff_path.read_text())}
        observed = evaluate(case)
        retained.append({"id": item["id"], "v2_outcome": item["v2_outcome"], "v3_criterion": "pass" if observed else "fail"})
        if observed is not item["expected_v3"]:
            errors.append(f"{item['id']}: v3 observed {observed}, expected {item['expected_v3']}")
    if check_paths:
        for ref in data.get("evidence", []):
            if not (ROOT / ref["path"]).is_file():
                errors.append(f"missing evidence path: {ref['path']}")
    return {"valid": not errors, "errors": errors, "calibration_cases_replayed": len(results), "calibration_results": results, "retained_replays": retained}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    report = replay(json.loads(args.path.read_text()), args.check_paths)
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
