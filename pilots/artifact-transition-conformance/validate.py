#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path


def replay(data: dict) -> dict:
    contract = data["contract"]
    predicate_kinds = {p["id"]: p["kind"] for p in contract["predicates"]}
    if set(predicate_kinds.values()) != {"must_change", "must_preserve", "forbidden_change"}:
        raise ValueError("contract must cover all three predicate kinds")
    rows = []
    for case in data["cases"]:
        if case.get("initial_sha256", contract["initial_sha256"]) != contract["initial_sha256"]:
            raise ValueError(f"{case['id']}: initial identity mismatch")
        if not set(case["invariances"]) <= set(contract["permitted_invariances"]):
            raise ValueError(f"{case['id']}: undeclared invariance")
        if set(case["predicate_results"]) != set(predicate_kinds):
            raise ValueError(f"{case['id']}: predicate coverage mismatch")
        invalid = case["forward_status"] == "invalid_parse"
        forward = (not invalid and all(case["predicate_results"][pid] is True for pid, kind in predicate_kinds.items() if kind == "must_change"))
        preservation = (not invalid and all(case["predicate_results"][pid] is True for pid, kind in predicate_kinds.items() if kind != "must_change"))
        if case["recovered_status"] == "not_attempted": recovery = None
        else: recovery = case["recovered_status"] == "valid" and case.get("recovered_sha256") == contract["initial_sha256"]
        outcome = "invalid_artifact" if invalid else ("passed" if forward and preservation else "forward_failed" if not forward and preservation else "preservation_failed" if forward else "forward_and_preservation_failed")
        observed = {"forward": forward, "preservation": preservation, "recovery": recovery, "outcome": outcome}
        if observed != case["expected"]:
            raise ValueError(f"{case['id']}: expected {case['expected']} but replayed {observed}")
        rows.append({"case_id": case["id"], **observed})
    return {"version": data["version"], "status": "passed", "cases_replayed": len(rows), "claim_boundary": data["contract"]["claims"], "results": rows}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = replay(json.loads(args.fixture.read_text()))
    text = json.dumps(report, indent=2) + "\n"
    if args.report: args.report.write_text(text)
    print(text, end="")
    return 0

if __name__ == "__main__": raise SystemExit(main())
