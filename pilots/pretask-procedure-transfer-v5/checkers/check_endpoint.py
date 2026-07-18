#!/usr/bin/env python3
"""Condition-blind typed semantic endpoint checker for v5."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any

def strict_bool(value: Any) -> bool: return type(value) is bool

def compare(candidate: Any, private: dict[str, Any]) -> tuple[bool, list[str]]:
    expected = private["expected_semantics"]
    errors: list[str] = []
    if not isinstance(candidate, dict): return False, ["artifact_not_object"]
    if candidate.get("task_id") != expected["task_id"] or not isinstance(candidate.get("task_id"), str): errors.append("task_id")
    family = private["family_id"]
    if family == "family-epsilon":
        decisions = candidate.get("decisions")
        if not isinstance(decisions, list): return False, errors + ["decisions_type"]
        by_id = {row.get("batch_id"): row for row in decisions if isinstance(row, dict) and isinstance(row.get("batch_id"), str)}
        expected_by_id = {row["batch_id"]: row for row in expected["decisions"]}
        if set(by_id) != set(expected_by_id) or len(decisions) != len(expected_by_id): errors.append("batch_ids")
        for batch_id, want in expected_by_id.items():
            got = by_id.get(batch_id, {})
            if got.get("disposition") != want["disposition"] or not isinstance(got.get("disposition"), str): errors.append(f"{batch_id}:disposition")
            controls = got.get("controlling_seals")
            if not isinstance(controls, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in controls.items()) or controls != want["controlling_seals"]: errors.append(f"{batch_id}:controlling_seals")
            observed = got.get("observation_ids")
            if not isinstance(observed, list) or not all(isinstance(v, str) for v in observed) or set(observed) != set(want["observation_ids"]) or len(observed) != len(set(observed)): errors.append(f"{batch_id}:observation_ids")
            row_reason = got.get("reason")
            if not isinstance(row_reason, str) or not row_reason.strip(): errors.append(f"{batch_id}:reason_type_or_empty")
    else:
        reason = candidate.get("reason")
        if not isinstance(reason, str) or not reason.strip(): errors.append("reason_type_or_empty")
        if candidate.get("journal_id") != expected["journal_id"] or not isinstance(candidate.get("journal_id"), str): errors.append("journal_id")
        if not strict_bool(candidate.get("valid")) or candidate.get("valid") != expected["valid"]: errors.append("valid")
        final_state = candidate.get("final_state")
        if final_state is not None and not isinstance(final_state, dict): errors.append("final_state_type")
        if final_state != expected["final_state"]: errors.append("final_state")
        for field in ("committed_transactions", "rolled_back_transactions"):
            value = candidate.get(field)
            if not isinstance(value, list) or not all(isinstance(v, str) for v in value) or value != expected[field]: errors.append(field)
    return not errors, errors

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--candidate",type=Path,required=True); parser.add_argument("--private",type=Path,required=True); args=parser.parse_args()
    try:
        candidate=json.loads(args.candidate.read_text()); private=json.loads(args.private.read_text()); passed,errors=compare(candidate,private)
    except (OSError,json.JSONDecodeError,KeyError,TypeError) as exc:
        passed,errors=False,["invalid_or_missing_artifact:"+type(exc).__name__]
    print(json.dumps({"passed":passed,"errors":errors},sort_keys=True)); return 0 if passed else 1

if __name__ == "__main__": raise SystemExit(main())
