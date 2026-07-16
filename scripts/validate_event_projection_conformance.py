#!/usr/bin/env python3
"""Audit canonical runtime-event ledgers and declared agent-view projections.

This pilot-specific validator governs the runtime world-event -> agent-view boundary.
It intentionally does not validate source-to-task projection or infer agent beliefs.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "pilots/harness-event-projection-conformance/conformance.json"
REQUIRED_VIEWS = {
    "raw",
    "structured",
    "blocked_log",
    "repair_collapsed",
    "verification_masked",
    "cost_pruned",
}
WORLD_KINDS = {
    "observation",
    "action_attempt",
    "action_block",
    "action_result",
    "failure",
    "repair",
    "artifact_write",
    "verifier_result",
    "outcome",
}
INVENTION_KINDS = {"failure", "repair", "verifier_result", "action_result"}
ALLOWED_OMISSIONS = {
    "raw": {},
    "structured": {},
    "blocked_log": {},
    "repair_collapsed": {"failure": "repair_collapse", "repair": "repair_collapse"},
    "verification_masked": {"verifier_result": "verification_mask"},
    "cost_pruned": {"observation": "cost_pruning"},
}
REQUIRED_NONCLAIMS = {
    "agent capability",
    "belief validity",
    "behavioral mediation",
    "professional validity",
    "cross-domain generalization",
    "production fitness",
    "deployment readiness",
}


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _validate_projection(scenario: dict[str, Any], view: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    scenario_id = scenario["scenario_id"]
    view_id = view.get("view_id", "<missing>")
    prefix = f"{scenario_id}/{view_id}"
    ledger = scenario["canonical_event_ledger"]
    if view.get("canonical_ledger_sha256") != canonical_hash(ledger):
        errors.append(f"{prefix}:canonical_ledger_reference_mismatch")
    by_id = {event["event_id"]: event for event in ledger}
    visible = view.get("visible_events", [])
    visible_ids: list[str] = []
    visible_sequences: list[int] = []

    for entry in visible:
        source_id = entry.get("source_event_id")
        source = by_id.get(source_id)
        if source is None:
            kind = entry.get("declared_kind", "unknown")
            diagnostic = f"invented_world_event:{kind}" if kind in INVENTION_KINDS else f"unknown_source_event:{source_id}"
            errors.append(f"{prefix}:{diagnostic}")
            continue
        visible_ids.append(source_id)
        visible_sequences.append(source["sequence"])
        if entry.get("declared_kind") != source["kind"]:
            errors.append(f"{prefix}:relabelled_event:{source_id}")
        if entry.get("source_payload_sha256") != source["payload_sha256"]:
            errors.append(f"{prefix}:source_hash_mismatch:{source_id}")
        if entry.get("canonical_payload") != source["payload"]:
            errors.append(f"{prefix}:canonical_payload_drift:{source_id}")
        if entry.get("rendered_content_sha256") != hashlib.sha256(entry.get("rendered_content", "").encode()).hexdigest():
            errors.append(f"{prefix}:render_hash_mismatch:{source_id}")
        if entry.get("projection") not in {"verbatim", "structured"}:
            errors.append(f"{prefix}:unknown_projection:{source_id}")

    if len(visible_ids) != len(set(visible_ids)):
        errors.append(f"{prefix}:duplicate_visible_source")
    if visible_sequences != sorted(visible_sequences):
        errors.append(f"{prefix}:reordered_authority")

    omissions = view.get("omissions", [])
    omission_by_id = {item.get("source_event_id"): item for item in omissions}
    if len(omission_by_id) != len(omissions) or None in omission_by_id:
        errors.append(f"{prefix}:duplicate_or_empty_omission")
    visible_set = set(visible_ids)
    omitted_set = set(omission_by_id)
    ledger_set = set(by_id)
    for event_id in sorted(ledger_set - visible_set - omitted_set):
        errors.append(f"{prefix}:undeclared_omission:{event_id}")
    for event_id in sorted((visible_set | omitted_set) - ledger_set):
        errors.append(f"{prefix}:unknown_projection_reference:{event_id}")
    for event_id in sorted(visible_set & omitted_set):
        errors.append(f"{prefix}:event_both_visible_and_omitted:{event_id}")

    allowed = ALLOWED_OMISSIONS.get(view_id, {})
    for event_id, omission in omission_by_id.items():
        source = by_id.get(event_id)
        if source is None:
            continue
        expected_reason = allowed.get(source["kind"])
        if omission.get("reason") != expected_reason:
            errors.append(f"{prefix}:unauthorized_omission:{event_id}")
        if omission.get("source_payload_sha256") != source["payload_sha256"]:
            errors.append(f"{prefix}:omission_hash_mismatch:{event_id}")

    # Raw/structured/blocked-log are lossless controls. Other policies may omit
    # only their specifically typed events; they may never create net successes.
    if view_id in {"raw", "structured", "blocked_log"} and omissions:
        errors.append(f"{prefix}:lossless_control_has_omissions")
    return errors


def validate_base(package: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if package.get("status") != "internal_synthetic_conformance_only":
        errors.append("package status must remain internal_synthetic_conformance_only")
    if package.get("execution_mode") != "zero_call_deterministic_replay":
        errors.append("execution mode must remain zero_call_deterministic_replay")
    if not REQUIRED_NONCLAIMS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("required non-claims missing")
    scenarios = package.get("scenarios", [])
    if len(scenarios) != 2 or len({item.get("work_shape") for item in scenarios}) != 2:
        errors.append("exactly two unlike work shapes are required")
    if len({item.get("scenario_id") for item in scenarios}) != len(scenarios):
        errors.append("scenario ids must be unique")

    for scenario in scenarios:
        scenario_id = scenario.get("scenario_id", "<missing>")
        ledger = scenario.get("canonical_event_ledger", [])
        if scenario.get("canonical_event_ledger_sha256") != canonical_hash(ledger):
            errors.append(f"{scenario_id}: canonical ledger hash mismatch")
        ids = [event.get("event_id") for event in ledger]
        sequences = [event.get("sequence") for event in ledger]
        if not ledger or len(ids) != len(set(ids)) or None in ids:
            errors.append(f"{scenario_id}: canonical event ids must be unique and nonempty")
        if sequences != list(range(1, len(ledger) + 1)):
            errors.append(f"{scenario_id}: canonical event sequence must be contiguous and ordered")
        authorities: list[int] = []
        for event in ledger:
            if event.get("kind") not in WORLD_KINDS:
                errors.append(f"{scenario_id}: unknown canonical event kind:{event.get('kind')}")
            if event.get("payload_sha256") != canonical_hash(event.get("payload")):
                errors.append(f"{scenario_id}: canonical payload hash mismatch:{event.get('event_id')}")
            if event.get("provenance", {}).get("authority_order") is None:
                errors.append(f"{scenario_id}: event lacks authority order:{event.get('event_id')}")
            else:
                authorities.append(event["provenance"]["authority_order"])
            if event.get("producer") not in {"source_pack", "executor", "environment", "artifact_store", "verifier", "outcome_grader"}:
                errors.append(f"{scenario_id}: invalid producer:{event.get('event_id')}")
        if authorities != sorted(authorities):
            errors.append(f"{scenario_id}: canonical authority order drift")

        views = scenario.get("agent_views", [])
        if {view.get("view_id") for view in views} != REQUIRED_VIEWS or len(views) != len(REQUIRED_VIEWS):
            errors.append(f"{scenario_id}: exact six matched view policies required")
        for view in views:
            errors.extend(_validate_projection(scenario, view))

        endpoints = scenario.get("endpoints", {})
        if set(endpoints) != {"agent_response", "action", "artifact", "outcome", "elicited_belief_report"}:
            errors.append(f"{scenario_id}: response/action/artifact/outcome/belief endpoints must remain separate")
        if endpoints.get("elicited_belief_report", {}).get("role") != "secondary_diagnostic_only":
            errors.append(f"{scenario_id}: elicited belief report promoted above secondary diagnostic")
        for endpoint in ("action", "artifact", "outcome"):
            if not endpoints.get(endpoint, {}).get("event_ids"):
                errors.append(f"{scenario_id}: {endpoint} endpoint lacks canonical events")

    if check_paths:
        for item in package.get("provenance", []):
            path = ROOT / item.get("path", "")
            if not path.is_file():
                errors.append(f"missing provenance path:{item.get('path')}")
            elif item.get("sha256") != file_hash(path):
                errors.append(f"provenance hash mismatch:{item.get('path')}")
    return errors


def _apply_mutation(package: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    mutated = copy.deepcopy(package)
    mutated.pop("conformance_cases", None)
    scenario = next(item for item in mutated["scenarios"] if item["scenario_id"] == case["scenario_id"])
    view = next(item for item in scenario["agent_views"] if item["view_id"] == case["view_id"])
    mutation = case["mutation"]
    operation = mutation["operation"]
    if operation == "none":
        return mutated
    if operation == "invent_event":
        payload = {"invented": True, "claim": mutation["kind"]}
        view["visible_events"].append({
            "source_event_id": mutation["event_id"],
            "declared_kind": mutation["kind"],
            "source_payload_sha256": canonical_hash(payload),
            "canonical_payload": payload,
            "projection": "structured",
            "rendered_content": json.dumps(payload, sort_keys=True),
            "rendered_content_sha256": hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest(),
        })
    elif operation == "swap_visible":
        by_source = {item["source_event_id"]: index for index, item in enumerate(view["visible_events"])}
        left, right = mutation["source_event_ids"]
        i, j = by_source[left], by_source[right]
        view["visible_events"][i], view["visible_events"][j] = view["visible_events"][j], view["visible_events"][i]
    elif operation == "drop_undeclared":
        source_id = mutation["source_event_id"]
        view["visible_events"] = [item for item in view["visible_events"] if item["source_event_id"] != source_id]
        view["omissions"] = [item for item in view["omissions"] if item["source_event_id"] != source_id]
    elif operation == "relabel":
        source_id = mutation["source_event_id"]
        entry = next(item for item in view["visible_events"] if item["source_event_id"] == source_id)
        entry["declared_kind"] = mutation["kind"]
    else:
        raise ValueError(f"unknown mutation operation:{operation}")
    return mutated


def evaluate_cases(package: dict[str, Any]) -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    results: list[dict[str, Any]] = []
    cases = package.get("conformance_cases", [])
    ids = [case.get("case_id") for case in cases]
    if len(ids) != len(set(ids)) or None in ids:
        errors.append("conformance case ids must be unique and nonempty")
    defect_counts = Counter()
    shape_counts = Counter()
    for case in cases:
        mutated = _apply_mutation(package, case)
        observed_errors = validate_base(mutated)
        expected = case.get("expected_diagnostic")
        matched = (not observed_errors) if expected is None else any(expected in error for error in observed_errors)
        results.append({
            "case_id": case["case_id"],
            "work_shape": next(item["work_shape"] for item in package["scenarios"] if item["scenario_id"] == case["scenario_id"]),
            "view_id": case["view_id"],
            "expected_diagnostic": expected,
            "observed_errors": observed_errors,
            "matched": matched,
        })
        shape_counts[case["scenario_id"]] += 1
        if expected:
            defect_counts[expected.split(":", 1)[0]] += 1
        if not matched:
            errors.append(f"case replay mismatch:{case['case_id']}")
    required_defects = {"invented_world_event", "reordered_authority", "undeclared_omission", "relabelled_event"}
    if not required_defects <= set(defect_counts):
        errors.append("planted defect coverage incomplete")
    if len(shape_counts) != 2 or len(set(shape_counts.values())) != 1:
        errors.append("conformance cases must be balanced across work shapes")
    return errors, results


def validate(path: Path = DEFAULT_FIXTURE, *, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(path.read_text())
    errors = validate_base(package, check_paths=check_paths)
    case_errors, cases = evaluate_cases(package)
    errors.extend(case_errors)
    return {
        "valid": not errors,
        "package_id": package.get("package_id"),
        "fixture_sha256": file_hash(path),
        "errors": errors,
        "summary": {
            "scenarios": len(package.get("scenarios", [])),
            "views": sum(len(item.get("agent_views", [])) for item in package.get("scenarios", [])),
            "cases": len(cases),
            "matched": sum(item["matched"] for item in cases),
            "world_events": sum(len(item.get("canonical_event_ledger", [])) for item in package.get("scenarios", [])),
            "endpoint_families": ["agent_response", "action", "artifact", "outcome", "elicited_belief_report"],
        },
        "cases": cases,
        "claim_limits": package.get("claim_limits"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate(args.path, check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered)
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
