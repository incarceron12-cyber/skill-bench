#!/usr/bin/env python3
"""Replay synthetic stateful-observer adversarial cases."""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREDICATES = ("intended_delta", "preserved_region", "task_attributable", "terminal_stable", "cleanup_complete")
NONCLAIMS = {"agent capability", "professional validity", "failure prevalence", "cross-domain generalization", "expert validity", "deployment readiness"}


def classify(case: dict, contract: dict) -> dict:
    undeclared = set(case["applied_invariances"]) - set(contract["accepted_invariances"])
    if undeclared:
        raise ValueError(f"{case['case_id']}: undeclared invariance {sorted(undeclared)}")
    missing = sorted(set(contract["required_views"]) - set(case["observed_views"]))
    if missing:
        return {"outcome": "insufficient_evidence", "diagnostic": "observer_insufficiency:" + ",".join(missing)}
    failed = [name for name in PREDICATES if not case["predicates"][name]]
    if failed:
        return {"outcome": "rejected", "diagnostic": "semantic_failure:" + ",".join(failed)}
    return {"outcome": "accepted", "diagnostic": "semantic_success"}


def replay(data: dict, check_paths: bool = False) -> dict:
    contracts = {x["work_shape"]: x for x in data["observer_contracts"]}
    errors, results = [], []
    if len(contracts) != len(data["observer_contracts"]): errors.append("duplicate observer contract")
    if len(contracts) < 2: errors.append("at least two unlike work shapes required")
    if not NONCLAIMS <= set(data["claim_limits"]["unsupported"]): errors.append("required claim limits missing")
    ids = [x["case_id"] for x in data["cases"]]
    if len(ids) != len(set(ids)): errors.append("duplicate case id")
    for case in data["cases"]:
        if case["work_shape"] not in contracts:
            errors.append(f"{case['case_id']}: missing observer contract"); continue
        if set(case["predicates"]) != set(PREDICATES):
            errors.append(f"{case['case_id']}: predicate coverage mismatch"); continue
        try: observed = classify(case, contracts[case["work_shape"]])
        except ValueError as exc: errors.append(str(exc)); continue
        if observed != case["expected"]: errors.append(f"{case['case_id']}: expected {case['expected']} but observed {observed}")
        results.append({"case_id": case["case_id"], "work_shape": case["work_shape"], **observed, "matched": observed == case["expected"]})
    if check_paths:
        for path in data["design_rationale"]["reused_contracts"] + [x.split("#")[0] for x in data["design_rationale"]["source_locators"]]:
            if not (ROOT / path).is_file(): errors.append(f"missing provenance path: {path}")
    return {"package_id": data["package_id"], "valid": not errors, "errors": errors, "summary": {"cases": len(results), "accepted": sum(x["outcome"] == "accepted" for x in results), "rejected_semantic": sum(x["outcome"] == "rejected" for x in results), "observer_insufficient": sum(x["outcome"] == "insufficient_evidence" for x in results)}, "results": results, "claim_limits": data["claim_limits"]}


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("fixture", type=Path); ap.add_argument("--check-paths", action="store_true"); ap.add_argument("--report", type=Path); args = ap.parse_args()
    report = replay(json.loads(args.fixture.read_text()), args.check_paths)
    text = json.dumps(report, indent=2) + "\n"
    if args.report: args.report.write_text(text)
    print(text, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__": raise SystemExit(main())
