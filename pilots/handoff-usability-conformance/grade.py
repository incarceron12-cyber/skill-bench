#!/usr/bin/env python3
"""Replay synthetic handoff-usability records; not a recipient-use study."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
DEFAULT = Path(__file__).with_name("conformance.json")
DENIED = {"agent capability", "expert approval", "professional validity", "downstream impact", "release readiness"}
DIMS = ("substantive_correctness", "provenance_boundary", "destination_fit", "recipient_usability", "next_operation")

def grade(case: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    state = case["artifact_state"]
    if state == "invalid":
        dims = {key: "not_evaluated" for key in DIMS}; outcome = "invalid_artifact"
    else:
        destination = case["format"] in contract["accepted_formats"] and case["recipient"] == contract["recipient"]
        if state == "missing_evidence":
            dims = {
                "substantive_correctness": "insufficient_evidence",
                "provenance_boundary": "insufficient_evidence",
                "destination_fit": "pass" if destination else "fail",
                "recipient_usability": "pass" if case["recipient_interpretable"] else "fail",
                "next_operation": "insufficient_evidence",
            }
            outcome = "insufficient_evidence"
        else:
            required = set(contract["required_fields"])
            sources = set(case["source_refs"])
            source_ok = bool(sources) and case["source_entailment"] is True
            boundary_ok = (case["boundary_preserved"] is True and
                           not sources.intersection(contract["prohibited_sources"]) and
                           sources <= set(contract["authoritative_sources"]))
            dims = {
                "substantive_correctness": "pass" if source_ok else "fail",
                "provenance_boundary": "pass" if source_ok and boundary_ok else "fail",
                "destination_fit": "pass" if destination and required <= set(case["fields"]) else "fail",
                "recipient_usability": "pass" if case["recipient_interpretable"] is True else "fail",
                "next_operation": "pass" if case["next_operation_executable"] is True else "fail",
            }
            outcome = "pass" if all(v == "pass" for v in dims.values()) else "fail"
    return {"case_id": case["id"], "outcome": outcome, **dims}

def replay(data: dict[str, Any], check_paths: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    if data.get("status") != "internal_synthetic_calibration_only": errors.append("status must remain internal synthetic calibration only")
    if not DENIED <= set(data.get("claim_limits", {}).get("unsupported", [])): errors.append("claim limits missing required non-claims")
    handoffs = {h["id"]: h for h in data.get("handoffs", [])}
    if len(handoffs) < 2 or len({h["artifact_kind"] for h in handoffs.values()}) < 2: errors.append("at least two distinct handoffs are required")
    results = []
    for case in data.get("cases", []):
        contract = handoffs.get(case.get("handoff"))
        if not contract: errors.append(f"{case.get('id')}: unknown handoff"); continue
        result = grade(case, contract); results.append(result)
        observed = {k: result[k] for k in ("outcome", *DIMS)}
        if observed != case.get("expected"): errors.append(f"{case['id']}: replayed {observed}, expected {case.get('expected')}")
    if check_paths:
        for ref in data["design_basis"].values():
            if isinstance(ref, dict) and not (ROOT / ref["path"]).is_file(): errors.append(f"missing provenance path: {ref['path']}")
    return {"valid": not errors, "errors": errors, "cases_replayed": len(results), "results": results}

def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("path", nargs="?", type=Path, default=DEFAULT); p.add_argument("--check-paths", action="store_true")
    args = p.parse_args(); report = replay(json.loads(args.path.read_text()), args.check_paths); print(json.dumps(report, indent=2)); return 0 if report["valid"] else 1
if __name__ == "__main__": raise SystemExit(main())
