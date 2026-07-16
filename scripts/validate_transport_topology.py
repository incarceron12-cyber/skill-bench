#!/usr/bin/env python3
"""Validate logical-call -> transport-attempt projections without replaying calls."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
COORDINATES = (
    "total_input_tokens", "cache_read_tokens", "output_tokens",
    "reasoning_tokens", "cache_write_tokens",
)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _source(path: str, expected_hash: str, errors: list[str], check_paths: bool) -> Path:
    resolved = ROOT / path
    if check_paths and (not resolved.is_file() or sha256(resolved) != expected_hash):
        errors.append(f"stale source: {path}")
    return resolved


def _expected_resource(events: list[dict[str, Any]], coordinate: str) -> dict[str, Any]:
    known = [event["coordinates"][coordinate]["value"] for event in events
             if event["coordinates"][coordinate].get("value") is not None]
    unknown = [event["call_id"] for event in events
               if event["coordinates"][coordinate].get("value") is None]
    if known and unknown:
        status, value = "lower_bound", sum(known)
    elif known:
        status, value = "complete", sum(known)
    else:
        status, value = "unavailable", None
    return {"status": status, "observed_value": value, "unknown_transport_attempt_ids": unknown}


def validate(doc: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if doc.get("schema_version") != "0.6.0":
        errors.append("unsupported topology version")
    if doc.get("projection_method") != "ordered_error_run_until_success_or_terminal_ledger_end":
        errors.append("undeclared projection method")
    if doc.get("projection_authority") != "posthoc_reconstruction_not_native_provider_identity":
        errors.append("retry topology authority overstated")
    if doc.get("substantive_pair_valid") is not False:
        errors.append("invalid pair restored")
    if any(doc.get("claim_ceiling", {}).values()):
        errors.append("claim ceiling upgrade")

    for arm in doc.get("attempts", []):
        arm_id = arm.get("benchmark_attempt_id")
        event_ref, usage_ref = arm.get("source_events", {}), arm.get("aggregate_usage", {})
        event_path = _source(event_ref.get("path", ""), event_ref.get("sha256", ""), errors, check_paths)
        usage_path = _source(usage_ref.get("path", ""), usage_ref.get("sha256", ""), errors, check_paths)
        if not event_path.is_file() or not usage_path.is_file():
            errors.append(f"missing retained sources: {arm_id}")
            continue
        events, usage = load_jsonl(event_path), load(usage_path)
        by_id = {event.get("call_id"): event for event in events}
        if len(by_id) != len(events):
            errors.append(f"duplicate retained event identity: {arm_id}")

        flattened: list[str] = []
        success_index = 0
        logical_calls = arm.get("logical_calls", [])
        for logical_sequence, logical in enumerate(logical_calls, 1):
            expected_id = f"{arm_id}:logical:{logical_sequence:04d}"
            if logical.get("logical_call_id") != expected_id or logical.get("sequence") != logical_sequence:
                errors.append(f"unstable or reordered logical call: {arm_id}")
            transports = logical.get("transport_attempts", [])
            if not transports:
                errors.append(f"logical call without transport attempt: {expected_id}")
                continue
            for order, transport in enumerate(transports, 1):
                source_id = transport.get("source_call_id")
                flattened.append(source_id)
                event = by_id.get(source_id)
                if event is None:
                    errors.append(f"orphaned transport attempt: {source_id}")
                    continue
                if transport.get("transport_attempt_id") != source_id:
                    errors.append(f"mislinked transport attempt identity: {source_id}")
                if transport.get("order") != order:
                    errors.append(f"reordered transport attempt: {expected_id}")
                expected_retry = None if order == 1 else transports[order - 2].get("transport_attempt_id")
                if transport.get("retry_of_transport_attempt_id") != expected_retry:
                    errors.append(f"retry causality mismatch: {source_id}")
                actual_outcome = "success" if event.get("error") is None else "error"
                if transport.get("outcome") != actual_outcome:
                    errors.append(f"transport outcome mismatch: {source_id}")
                if event.get("sequence") != events.index(event) + 1:
                    errors.append(f"retained event sequence mismatch: {source_id}")
                if transport.get("source_event_sha256") != event.get("event_sha256"):
                    errors.append(f"mislinked source event hash: {source_id}")
                prior_event = by_id.get(expected_retry) if order > 1 else None
                prior_error = prior_event.get("error") if prior_event else None
                expected_cause = prior_error.get("type") if isinstance(prior_error, dict) else None
                if transport.get("retry_cause") != expected_cause:
                    errors.append(f"retry cause mismatch: {source_id}")
            source_events = [by_id.get(t.get("source_call_id")) for t in transports]
            if all(source_events):
                outcomes = [event.get("error") is None for event in source_events]
                declared = logical.get("service_outcome")
                if declared == "success":
                    success_index += 1
                    if outcomes[-1] is not True or any(outcomes[:-1]):
                        errors.append(f"false logical success: {expected_id}")
                    if logical.get("aggregate_success_index") != success_index:
                        errors.append(f"aggregate success linkage mismatch: {expected_id}")
                elif declared == "terminal_failure":
                    if any(outcomes) or logical.get("aggregate_success_index") is not None:
                        errors.append(f"false terminal failure: {expected_id}")
                    if logical_sequence != len(logical_calls):
                        errors.append(f"nonterminal logical failure: {expected_id}")
                else:
                    errors.append(f"unknown logical service outcome: {expected_id}")

        retained_order = [event.get("call_id") for event in events]
        if flattened != retained_order:
            if len(flattened) != len(set(flattened)):
                errors.append(f"duplicated transport attempt: {arm_id}")
            missing = set(retained_order) - set(flattened)
            if missing:
                errors.append(f"omitted transport attempt: {arm_id}")
            if not missing and len(flattened) == len(retained_order):
                errors.append(f"reordered transport ledger: {arm_id}")
        if usage.get("api_calls") != len(logical_calls):
            errors.append(f"aggregate logical-call count mismatch: {arm_id}")
        if arm.get("successful_logical_calls") != success_index:
            errors.append(f"successful logical-call count mismatch: {arm_id}")
        terminal_count = sum(x.get("service_outcome") == "terminal_failure" for x in logical_calls)
        if arm.get("terminal_failed_logical_calls") != terminal_count:
            errors.append(f"terminal logical-call count mismatch: {arm_id}")
        expected_service = "completed" if usage.get("completed") and not usage.get("failed") else "terminal_failure"
        if arm.get("service_outcome") != expected_service:
            errors.append(f"service outcome mismatch: {arm_id}")

        for coordinate in COORDINATES:
            observed = arm.get("resource_evidence", {}).get(coordinate)
            expected = _expected_resource(events, coordinate)
            if observed != expected:
                errors.append(f"resource evidence mismatch or hidden imputation: {arm_id}:{coordinate}")
        linkage = arm.get("aggregate_linkage", {})
        if linkage.get("status") == "available":
            if not usage.get("completed"):
                errors.append(f"aggregate linkage falsely available: {arm_id}")
            expected = {
                "successful_calls": success_index,
                "total_input_tokens": usage.get("input_tokens", 0) + usage.get("cache_read_tokens", 0),
                "cache_read_tokens": usage.get("cache_read_tokens"),
                "output_tokens": usage.get("output_tokens"),
                "reasoning_tokens": usage.get("reasoning_tokens"),
            }
            if linkage.get("successful_call_aggregate") != expected:
                errors.append(f"aggregate-success mismatch: {arm_id}")
        elif linkage.get("status") == "unavailable":
            if linkage.get("successful_call_aggregate") is not None:
                errors.append(f"unavailable aggregate imputed: {arm_id}")
        else:
            errors.append(f"unknown aggregate linkage status: {arm_id}")
    return errors


def mutation_report(doc: dict[str, Any]) -> dict[str, Any]:
    cases: list[tuple[str, dict[str, Any], str]] = []
    def case(name: str, fragment: str, mutate: Any) -> None:
        value = copy.deepcopy(doc); mutate(value); cases.append((name, value, fragment))
    calls = lambda d: d["attempts"][0]["logical_calls"]
    case("omitted_attempt", "omitted transport", lambda d: calls(d)[2]["transport_attempts"].pop(0))
    case("duplicated_attempt", "duplicated transport", lambda d: calls(d)[2]["transport_attempts"].append(copy.deepcopy(calls(d)[2]["transport_attempts"][-1])))
    case("reordered_attempt", "reordered transport", lambda d: calls(d)[2]["transport_attempts"].reverse())
    case("orphaned_attempt", "orphaned transport", lambda d: calls(d)[2]["transport_attempts"][0].update(source_call_id="orphan"))
    case("mislinked_attempt", "mislinked transport attempt identity", lambda d: calls(d)[2]["transport_attempts"][0].update(transport_attempt_id="mislinked"))
    case("false_terminal_success", "false logical success", lambda d: d["attempts"][1]["logical_calls"][-1].update(service_outcome="success", aggregate_success_index=3))
    case("aggregate_success_mismatch", "aggregate-success mismatch", lambda d: d["attempts"][0]["aggregate_linkage"]["successful_call_aggregate"].update(output_tokens=0))
    case("hidden_imputation", "hidden imputation", lambda d: d["attempts"][1]["resource_evidence"]["cache_write_tokens"].update(status="complete", observed_value=0))
    rows = []
    for name, value, fragment in cases:
        errors = validate(value)
        rows.append({"case": name, "expected_error_fragment": fragment, "detected": any(fragment in e for e in errors), "errors": errors})
    retained_audit = []
    for arm in doc["attempts"]:
        events = load_jsonl(ROOT / arm["source_events"]["path"])
        retained_audit.append({
            "benchmark_attempt_id": arm["benchmark_attempt_id"],
            "transport_attempts": len(events),
            "logical_calls": len(arm["logical_calls"]),
            "successful_logical_calls": arm["successful_logical_calls"],
            "terminal_failed_logical_calls": arm["terminal_failed_logical_calls"],
            "service_outcome": arm["service_outcome"],
            "resource_evidence": arm["resource_evidence"],
            "aggregate_linkage": arm["aggregate_linkage"],
        })
    return {"schema_version": "0.6.0", "baseline_passed": not validate(doc, check_paths=True),
            "retained_audit": retained_audit, "substantive_pair_valid": False, "mutations": rows,
            "all_mutations_detected": all(row["detected"] for row in rows), "model_calls": 0,
            "interpretation": "Internal conformance and read-only projection audit only; no pair, effect, capability, cost-value, professional, production, or readiness claim."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topology", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--mutation-report", action="store_true")
    parser.add_argument("--report-output", type=Path)
    args = parser.parse_args(); doc = load(args.topology)
    if args.mutation_report:
        report = mutation_report(doc)
        rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if args.report_output:
            args.report_output.parent.mkdir(parents=True, exist_ok=True)
            args.report_output.write_text(rendered, encoding="utf-8")
        print(rendered, end="")
        return 0 if report["baseline_passed"] and report["all_mutations_detected"] else 1
    errors = validate(doc, check_paths=args.check_paths)
    print(json.dumps({"passed": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
