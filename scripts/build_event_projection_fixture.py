#!/usr/bin/env python3
"""Generate the frozen internal harness event-projection conformance fixture."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pilots/harness-event-projection-conformance/conformance.json"


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def event(event_id: str, sequence: int, kind: str, producer: str, authority_order: int, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_id": event_id,
        "sequence": sequence,
        "kind": kind,
        "producer": producer,
        "payload": payload,
        "payload_sha256": canonical_hash(payload),
        "provenance": {
            "authority_order": authority_order,
            "capture": "builder_authored_deterministic_executor_fixture",
            "immutable": True,
        },
    }


def visible_entry(source: dict[str, Any], view_id: str) -> dict[str, Any]:
    projection = "structured" if view_id == "structured" else "verbatim"
    if projection == "structured":
        rendered = json.dumps({"kind": source["kind"], "payload": source["payload"]}, sort_keys=True)
    else:
        rendered = f"{source['kind']}: {json.dumps(source['payload'], sort_keys=True)}"
    return {
        "source_event_id": source["event_id"],
        "declared_kind": source["kind"],
        "source_payload_sha256": source["payload_sha256"],
        "canonical_payload": source["payload"],
        "projection": projection,
        "rendered_content": rendered,
        "rendered_content_sha256": hashlib.sha256(rendered.encode()).hexdigest(),
    }


def build_views(ledger: list[dict[str, Any]]) -> list[dict[str, Any]]:
    views = []
    for view_id in ("raw", "structured", "blocked_log", "repair_collapsed", "verification_masked", "cost_pruned"):
        omissions = []
        visible = []
        for source in ledger:
            reason = None
            if view_id == "repair_collapsed" and source["kind"] in {"failure", "repair"}:
                reason = "repair_collapse"
            elif view_id == "verification_masked" and source["kind"] == "verifier_result":
                reason = "verification_mask"
            elif view_id == "cost_pruned" and source["kind"] == "observation":
                reason = "cost_pruning"
            if reason:
                omissions.append({
                    "source_event_id": source["event_id"],
                    "source_payload_sha256": source["payload_sha256"],
                    "reason": reason,
                    "declared_by": "frozen_view_policy_v1",
                })
            else:
                visible.append(visible_entry(source, view_id))
        views.append({
            "view_id": view_id,
            "policy_version": "1.0.0",
            "canonical_ledger_sha256": canonical_hash(ledger),
            "visible_events": visible,
            "omissions": omissions,
        })
    return views


def scenario(scenario_id: str, work_shape: str, ledger: list[dict[str, Any]], endpoints: dict[str, Any]) -> dict[str, Any]:
    return {
        "scenario_id": scenario_id,
        "work_shape": work_shape,
        "task_status": "builder_authored_internal_fixture",
        "canonical_event_ledger": ledger,
        "canonical_event_ledger_sha256": canonical_hash(ledger),
        "agent_views": build_views(ledger),
        "endpoints": endpoints,
    }


allocation = [
    event("alloc-e1", 1, "observation", "source_pack", 1, {"source": "allocation.csv", "rows": 4, "total_budget": 100}),
    event("alloc-e2", 2, "action_attempt", "executor", 2, {"action": "allocate", "method": "unrounded_proportions"}),
    event("alloc-e3", 3, "failure", "environment", 3, {"code": "sum_mismatch", "observed_total": 99}),
    event("alloc-e4", 4, "repair", "executor", 4, {"method": "largest_remainder", "trigger_event_id": "alloc-e3"}),
    event("alloc-e5", 5, "action_result", "environment", 5, {"status": "succeeded", "observed_total": 100}),
    event("alloc-e6", 6, "artifact_write", "artifact_store", 6, {"path": "outputs/allocation.csv", "sha256": "a" * 64}),
    event("alloc-e7", 7, "verifier_result", "verifier", 7, {"verifier": "sum-and-row-check-v1", "result": "pass", "strength": "deterministic"}),
    event("alloc-e8", 8, "outcome", "outcome_grader", 8, {"task_result": "pass", "artifact_usable": True}),
]
allocation_endpoints = {
    "agent_response": {"status": "not_collected_zero_call", "event_ids": []},
    "action": {"status": "fixture_observed", "event_ids": ["alloc-e2", "alloc-e4", "alloc-e5"]},
    "artifact": {"status": "fixture_observed", "event_ids": ["alloc-e6"]},
    "outcome": {"status": "fixture_observed", "event_ids": ["alloc-e7", "alloc-e8"]},
    "elicited_belief_report": {"status": "not_collected", "role": "secondary_diagnostic_only", "event_ids": []},
}

memo = [
    event("memo-e1", 1, "observation", "source_pack", 1, {"source": "brief.md", "claim": "launch-ready", "authority": "draft"}),
    event("memo-e2", 2, "observation", "source_pack", 2, {"source": "audit.md", "claim": "control-failed", "authority": "approved_audit"}),
    event("memo-e3", 3, "action_attempt", "executor", 3, {"action": "assert_launch_ready", "basis": "brief.md"}),
    event("memo-e4", 4, "action_block", "environment", 4, {"reason": "higher_authority_contradiction_unresolved", "blocked_action_event_id": "memo-e3"}),
    event("memo-e5", 5, "action_attempt", "executor", 5, {"action": "write_conditional_recommendation", "basis": ["brief.md", "audit.md"]}),
    event("memo-e6", 6, "action_result", "environment", 6, {"status": "succeeded", "recommendation": "defer_pending_control_repair"}),
    event("memo-e7", 7, "artifact_write", "artifact_store", 7, {"path": "outputs/decision-memo.md", "sha256": "b" * 64}),
    event("memo-e8", 8, "verifier_result", "verifier", 8, {"verifier": "authority-reconciliation-v1", "result": "pass", "strength": "deterministic_fixture"}),
    event("memo-e9", 9, "outcome", "outcome_grader", 9, {"task_result": "pass", "decision_basis_traceable": True}),
]
memo_endpoints = {
    "agent_response": {"status": "not_collected_zero_call", "event_ids": []},
    "action": {"status": "fixture_observed", "event_ids": ["memo-e3", "memo-e4", "memo-e5", "memo-e6"]},
    "artifact": {"status": "fixture_observed", "event_ids": ["memo-e7"]},
    "outcome": {"status": "fixture_observed", "event_ids": ["memo-e8", "memo-e9"]},
    "elicited_belief_report": {"status": "not_collected", "role": "secondary_diagnostic_only", "event_ids": []},
}

scenarios = [
    scenario("allocation-repair", "structured_allocation_artifact", allocation, allocation_endpoints),
    scenario("authority-memo", "evidence_to_decision_memo", memo, memo_endpoints),
]

cases = []
for scenario_id in ("allocation-repair", "authority-memo"):
    for view_id in ("raw", "structured", "blocked_log", "repair_collapsed", "verification_masked", "cost_pruned"):
        cases.append({
            "case_id": f"{scenario_id}-{view_id}-clean",
            "scenario_id": scenario_id,
            "view_id": view_id,
            "mutation": {"operation": "none"},
            "expected_diagnostic": None,
        })

cases.extend([
    {"case_id": "allocation-invented-failure", "scenario_id": "allocation-repair", "view_id": "structured", "mutation": {"operation": "invent_event", "kind": "failure", "event_id": "alloc-invented-failure"}, "expected_diagnostic": "invented_world_event:failure"},
    {"case_id": "allocation-invented-repair", "scenario_id": "allocation-repair", "view_id": "repair_collapsed", "mutation": {"operation": "invent_event", "kind": "repair", "event_id": "alloc-invented-repair"}, "expected_diagnostic": "invented_world_event:repair"},
    {"case_id": "allocation-reordered-authority", "scenario_id": "allocation-repair", "view_id": "raw", "mutation": {"operation": "swap_visible", "source_event_ids": ["alloc-e1", "alloc-e2"]}, "expected_diagnostic": "reordered_authority"},
    {"case_id": "allocation-undeclared-omission", "scenario_id": "allocation-repair", "view_id": "structured", "mutation": {"operation": "drop_undeclared", "source_event_id": "alloc-e3"}, "expected_diagnostic": "undeclared_omission:alloc-e3"},
    {"case_id": "allocation-relabelled-outcome", "scenario_id": "allocation-repair", "view_id": "raw", "mutation": {"operation": "relabel", "source_event_id": "alloc-e8", "kind": "verifier_result"}, "expected_diagnostic": "relabelled_event:alloc-e8"},
    {"case_id": "memo-invented-verifier", "scenario_id": "authority-memo", "view_id": "verification_masked", "mutation": {"operation": "invent_event", "kind": "verifier_result", "event_id": "memo-invented-verifier"}, "expected_diagnostic": "invented_world_event:verifier_result"},
    {"case_id": "memo-invented-action-result", "scenario_id": "authority-memo", "view_id": "blocked_log", "mutation": {"operation": "invent_event", "kind": "action_result", "event_id": "memo-invented-result"}, "expected_diagnostic": "invented_world_event:action_result"},
    {"case_id": "memo-reordered-authority", "scenario_id": "authority-memo", "view_id": "blocked_log", "mutation": {"operation": "swap_visible", "source_event_ids": ["memo-e1", "memo-e2"]}, "expected_diagnostic": "reordered_authority"},
    {"case_id": "memo-undeclared-omission", "scenario_id": "authority-memo", "view_id": "raw", "mutation": {"operation": "drop_undeclared", "source_event_id": "memo-e4"}, "expected_diagnostic": "undeclared_omission:memo-e4"},
    {"case_id": "memo-relabelled-block", "scenario_id": "authority-memo", "view_id": "structured", "mutation": {"operation": "relabel", "source_event_id": "memo-e4", "kind": "action_result"}, "expected_diagnostic": "relabelled_event:memo-e4"},
])

provenance_paths = [
    "papers/agent-benchmarks/2026-07-17-harness-induced-belief-divergence-validity.md",
    "data/papers/pdfs/2607.04528v1-harness-induced-belief-divergence.pdf",
    "tests/fixtures/valid-task-projection-manifest.json",
]
package = {
    "package_id": "harness-event-projection-conformance-v1",
    "version": "1.0.0",
    "status": "internal_synthetic_conformance_only",
    "execution_mode": "zero_call_deterministic_replay",
    "design_rationale": {
        "charter_objectives": ["B", "C"],
        "classification": "building_and_validation",
        "general_hypothesis": "A runtime harness view is auditable only when every visible claim cites an immutable canonical world event and every omission is typed, declared, and policy-authorized.",
        "uncertainty_clarified": "Whether runtime world-to-agent projection can reject invented or reordered evidence without duplicating source-to-task projection machinery.",
        "useful_completion": "Two unlike work shapes expose all six matched views; clean controls pass and balanced planted inventions, relabelings, reorderings, and undeclared omissions fail for the declared reason.",
        "runtime_boundary": "The canonical ledger begins after task construction and records executor/environment/verifier events. Source-to-task IR remains governed by tests/fixtures/valid-task-projection-manifest.json.",
        "notice": "Builder-authored deterministic records only; no model or expert call, real task execution, belief measurement, capability evidence, or professional-validity evidence.",
    },
    "scenarios": scenarios,
    "conformance_cases": cases,
    "claim_limits": {
        "supported": "The repository validator distinguishes 12 clean matched projections and 10 planted projection defects over two builder-authored event ledgers.",
        "unsupported": sorted([
            "agent capability", "belief validity", "behavioral mediation", "professional validity",
            "cross-domain generalization", "production fitness", "deployment readiness",
            "harness treatment effect", "artifact quality", "task success prevalence",
        ]),
    },
    "provenance": [
        {
            "path": path,
            "sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
            "role": "design_evidence" if "harness-induced" in path else "adjacent_contract_boundary",
            "locator": "Transferable lessons and concrete repository actions" if path.endswith(".md") and "harness-induced" in path else "immutable local artifact",
        }
        for path in provenance_paths
    ],
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
print(OUT)
print(hashlib.sha256(OUT.read_bytes()).hexdigest())
