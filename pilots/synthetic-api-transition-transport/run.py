#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from adapters import ReferenceAdapter, SyntheticAdapter, initial_state


def _pointer(value: Any, pointer: str) -> Any:
    current = value
    for part in pointer.strip("/").split("/") if pointer != "/" else []:
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current


def _diff(before: Any, after: Any, path: str = "") -> list[dict[str, Any]]:
    if isinstance(before, dict) and isinstance(after, dict):
        rows: list[dict[str, Any]] = []
        for key in sorted(set(before) | set(after)):
            child = f"{path}/{key}"
            if key not in before:
                rows.append({"path": child, "before": None, "after": after[key]})
            elif key not in after:
                rows.append({"path": child, "before": before[key], "after": None})
            else:
                rows.extend(_diff(before[key], after[key], child))
        return rows
    if before != after:
        return [{"path": path or "/", "before": before, "after": after}]
    return []


def _criterion(criterion: dict[str, Any], before: dict[str, Any], after: dict[str, Any], responses: list[dict[str, Any]]) -> tuple[bool, Any]:
    kind = criterion["kind"]
    if kind == "response_statuses":
        observed = [r["status"] for r in responses]
    elif kind == "response_bodies_absent":
        observed = all(r.get("body") is None for r in responses)
    elif kind == "path_equals":
        observed = _pointer(after, criterion["path"])
    elif kind == "revision_delta":
        observed = after["revision"] - before["revision"]
    elif kind == "audit_delta":
        observed = len(after["audit"]) - len(before["audit"])
    elif kind == "etag_changed":
        observed = after["etag"] != before["etag"]
    elif kind == "unchanged_state":
        observed = after == before
    else:
        raise ValueError(f"unknown criterion kind: {kind}")
    return observed == criterion["expected"], observed


def _covered(change_path: str, read_sets: set[str]) -> bool:
    return any(change_path == read or change_path.startswith(read + "/") or read.startswith(change_path + "/") for read in read_sets)


def run_adapter(adapter_type: type, suite: dict[str, Any]) -> dict[str, Any]:
    cases = []
    for case in suite["cases"]:
        adapter = adapter_type(suite["initial_state"])
        before = adapter.snapshot()
        initial_etag = before["etag"]
        responses: list[dict[str, Any]] = []
        invalid_reason = None
        try:
            for action in case["actions"]:
                response = adapter.execute(copy.deepcopy(action), initial_etag)
                if not isinstance(response, dict) or "status" not in response:
                    raise ValueError("missing typed response status")
                responses.append(response)
        except Exception as exc:  # fail-closed boundary is itself reported
            invalid_reason = f"{type(exc).__name__}: {exc}"
        after = adapter.snapshot()
        changes = _diff(before, after)
        criterion_rows = []
        if invalid_reason is None:
            for criterion in case["criteria"]:
                passed, observed = _criterion(criterion, before, after, responses)
                criterion_rows.append({
                    "criterion_id": criterion["id"],
                    "passed": passed,
                    "expected": criterion["expected"],
                    "observed": observed,
                    "read_set": criterion["read_set"],
                })
        read_sets = {p for c in case["criteria"] for p in c["read_set"] if not p.startswith("/responses")}
        uncovered = [row["path"] for row in changes if not _covered(row["path"], read_sets)]
        cases.append({
            "case_id": case["id"],
            "run_status": "invalid" if invalid_reason else "valid",
            "invalid_reason": invalid_reason,
            "responses": responses,
            "before_sha256": hashlib.sha256(json.dumps(before, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            "after_sha256": hashlib.sha256(json.dumps(after, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            "transition_diff": changes,
            "observer_coverage": {
                "declared_state_read_set": sorted(read_sets),
                "changed_paths": [row["path"] for row in changes],
                "covered_changed_paths": len(changes) - len(uncovered),
                "total_changed_paths": len(changes),
                "uncovered_changed_paths": uncovered,
            },
            "criteria": criterion_rows,
            "criterion_score": None if invalid_reason else sum(r["passed"] for r in criterion_rows) / len(criterion_rows),
            "strict_pass": None if invalid_reason else all(r["passed"] for r in criterion_rows),
        })
    valid = [c for c in cases if c["run_status"] == "valid"]
    return {
        "adapter": adapter_type.name,
        "cases": cases,
        "summary": {
            "valid_runs": len(valid),
            "invalid_runs": len(cases) - len(valid),
            "strict_passes": sum(c["strict_pass"] is True for c in valid),
            "strict_denominator": len(valid),
            "criteria_passed": sum(r["passed"] for c in valid for r in c["criteria"]),
            "criteria_total": sum(len(c["criteria"]) for c in valid),
        },
    }


def build_report(suite: dict[str, Any]) -> dict[str, Any]:
    reference = run_adapter(ReferenceAdapter, suite)
    synthetic = run_adapter(SyntheticAdapter, suite)
    if reference["summary"]["strict_passes"] != len(suite["cases"]):
        raise ValueError("reference adapter does not satisfy the frozen prospective suite")

    ref_cases = {c["case_id"]: c for c in reference["cases"]}
    syn_cases = {c["case_id"]: c for c in synthetic["cases"]}
    case_transport = []
    criterion_transport = []
    for case in suite["cases"]:
        rid = case["id"]
        ref = ref_cases[rid]
        syn = syn_cases[rid]
        case_transport.append({
            "case_id": rid,
            "reference_strict_pass": ref["strict_pass"],
            "synthetic_strict_pass": syn["strict_pass"],
            "strict_verdict_transports": ref["strict_pass"] == syn["strict_pass"],
            "final_state_identical": ref["after_sha256"] == syn["after_sha256"],
        })
        rr = {row["criterion_id"]: row for row in ref["criteria"]}
        sr = {row["criterion_id"]: row for row in syn["criteria"]}
        for criterion in case["criteria"]:
            cid = criterion["id"]
            criterion_transport.append({
                "case_id": rid,
                "criterion_id": cid,
                "reference_pass": rr[cid]["passed"],
                "synthetic_pass": sr[cid]["passed"],
                "verdict_transports": rr[cid]["passed"] == sr[cid]["passed"],
            })

    suite_bytes = json.dumps(suite, sort_keys=True, separators=(",", ":")).encode()
    return {
        "report_version": "1.0.0",
        "suite_id": suite["suite_id"],
        "suite_canonical_sha256": hashlib.sha256(suite_bytes).hexdigest(),
        "design_status": "frozen_builder_authored_conformance_slice",
        "adapters": [reference, synthetic],
        "transport": {
            "strict_cases_transporting": sum(r["strict_verdict_transports"] for r in case_transport),
            "strict_cases_total": len(case_transport),
            "criteria_transporting": sum(r["verdict_transports"] for r in criterion_transport),
            "criteria_total": len(criterion_transport),
            "case_results": case_transport,
            "criterion_results": criterion_transport,
        },
        "invalid_run_policy": suite["invalid_run_policy"],
        "claim_ceiling": suite["claim_ceiling"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", type=Path, default=Path(__file__).with_name("suite.json"))
    parser.add_argument("--report", type=Path, default=Path(__file__).with_name("report.json"))
    args = parser.parse_args()
    suite = json.loads(args.suite.read_text())
    report = build_report(suite)
    text = json.dumps(report, indent=2) + "\n"
    args.report.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
