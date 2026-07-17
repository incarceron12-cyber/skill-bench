#!/usr/bin/env python3
"""Build the frozen internal source-at-state intervention matrix."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REVIEW = "papers/agent-benchmarks/2026-07-17-bridge-evidence-causal-use-validity.md"


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def canonical_sha(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def source(source_id: str, role: str, content: str, cue: str = "", baseline_available: bool = True) -> dict[str, Any]:
    return {
        "source_id": source_id,
        "role_at_state": role,
        "content": content,
        "content_sha256": sha_text(content),
        "byte_length": len(content.encode()),
        "decision_cue": cue,
        "authority": "builder_authored_synthetic",
        "baseline_available": baseline_available,
    }


def outcome(final: bool, next_op: bool, safety: bool, effort: int) -> dict[str, Any]:
    return {"status": "observed", "final_acceptance": final, "next_operation_valid": next_op, "safety_preserved": safety, "effort_units": effort}


def condition(cid: str, kind: str, out: dict[str, Any], targets: list[str] | None = None, replacement: str | None = None, cue: str | None = None) -> dict[str, Any]:
    intervention: dict[str, Any] = {"kind": kind, "target_source_ids": targets or []}
    if replacement:
        intervention["replacement_source_id"] = replacement
    if cue:
        intervention["masked_cue"] = cue
    return {"condition_id": cid, "intervention": intervention, "outcome": out}


def scenario(shape_id: str, work_shape: str, prefix: dict[str, Any], sources: list[dict[str, Any]], transition_id: str, terminal_id: str, sub_a: str, sub_b: str, stale_id: str, distractor_id: str, base: dict[str, Any], bad_transition: dict[str, Any], bad_terminal_set: dict[str, Any], bad_stale: dict[str, Any]) -> dict[str, Any]:
    neutral_content = "." * next(s["byte_length"] for s in sources if s["source_id"] == transition_id)
    neutral = source(f"{shape_id}-neutral", "neutral_control", neutral_content, baseline_available=False)
    sources = [*sources, neutral]
    config = {"engine": "deterministic_fixture_replay", "version": "1.0", "policy": "frozen_source_order", "stochastic_components": []}
    conditions = [
        condition("baseline", "baseline", base),
        condition("unchanged-replay-1", "unchanged_replay", base),
        condition("unchanged-replay-2", "unchanged_replay", base),
        condition("omit-transition", "omission", bad_transition, [transition_id]),
        condition("neutral-replace-transition", "neutral_replacement", bad_transition, [transition_id], neutral["source_id"]),
        condition("mask-transition-cue", "cue_mask", bad_transition, [transition_id], cue=next(s["decision_cue"] for s in sources if s["source_id"] == transition_id)),
        condition("omit-terminal-single", "omission", base, [terminal_id]),
        condition("equivalent-substitution", "equivalent_source_substitution", base, [terminal_id], sub_b),
        condition("omit-one-substitute", "omission", base, [sub_a]),
        condition("omit-terminal-and-substitutes", "joint_omission", bad_terminal_set, [terminal_id, sub_a, sub_b]),
        condition("stale-substitution", "stale_contradictory_substitution", bad_stale, [transition_id], stale_id),
        condition("omit-distractor", "omission", base, [distractor_id]),
        {"condition_id": "missing-post-state", "intervention": {"kind": "omission", "target_source_ids": [transition_id]}, "outcome": {"status": "invalid_missing_state", "final_acceptance": None, "next_operation_valid": None, "safety_preserved": None, "effort_units": None}},
    ]
    return {
        "shape_id": shape_id,
        "work_shape": work_shape,
        "configured_system": config,
        "configured_system_sha256": canonical_sha(config),
        "frozen_prefix": prefix,
        "frozen_prefix_sha256": canonical_sha(prefix),
        "sources": sources,
        "conditions": conditions,
    }


def materialize_context(scenario: dict[str, Any], intervention: dict[str, Any]) -> list[dict[str, str]]:
    records = [{"source_id": s["source_id"], "content": s["content"]} for s in scenario["sources"] if s["baseline_available"]]
    by_id = {s["source_id"]: s for s in scenario["sources"]}
    kind = intervention["kind"]
    targets = set(intervention["target_source_ids"])
    if kind in {"omission", "joint_omission"}:
        records = [r for r in records if r["source_id"] not in targets]
    elif kind in {"neutral_replacement", "equivalent_source_substitution", "stale_contradictory_substitution"}:
        replacement = by_id[intervention["replacement_source_id"]]
        records = [r for r in records if r["source_id"] not in targets]
        if replacement["source_id"] not in {r["source_id"] for r in records}:
            records.append({"source_id": replacement["source_id"], "content": replacement["content"]})
    elif kind == "cue_mask":
        cue = intervention["masked_cue"]
        records = [{**r, "content": r["content"].replace(cue, "[MASK]")} if r["source_id"] in targets else r for r in records]
    return records


def build() -> dict[str, Any]:
    procurement_sources = [
        source("proc-terminal", "terminal_support", "Authorized memo: supplier A meets the delivery threshold."),
        source("proc-transition", "transition_support", "Registry lookup key: INS-447. Inspect the insurance registry before approval.", "INS-447"),
        source("proc-sub-a", "substitute_support", "Carrier certificate confirms policy INS-447 through December."),
        source("proc-sub-b", "substitute_support", "Regulator mirror confirms policy INS-447 through December.", baseline_available=False),
        source("proc-stale", "stale_contradictory", "Expired note: skip registry inspection and approve immediately.", baseline_available=False),
        source("proc-distractor", "distractor", "Cafeteria renewal is due next quarter."),
    ]
    incident_sources = [
        source("inc-terminal", "terminal_support", "Current runbook: rotate the client certificate, then verify recovery."),
        source("inc-transition", "transition_support", "Alert fingerprint TLS-42 maps to the certificate store inspection step.", "TLS-42"),
        source("inc-sub-a", "substitute_support", "Gateway log independently reports client certificate expiry."),
        source("inc-sub-b", "substitute_support", "Certificate inventory independently reports client certificate expiry.", baseline_available=False),
        source("inc-stale", "stale_contradictory", "Legacy note: disable certificate validation to restore traffic.", baseline_available=False),
        source("inc-distractor", "distractor", "Dashboard theme migration is scheduled for Friday."),
    ]
    data = {
        "version": "1.0.0",
        "status": "internal_synthetic_contract_calibration",
        "design_basis": {
            "charter_objectives": ["B", "C"],
            "mode": "building_and_validation",
            "review_path": REVIEW,
            "review_sha256": hashlib.sha256((ROOT / REVIEW).read_bytes()).hexdigest(),
            "review_locators": ["Unique insight", "Transferable design implications for skill-bench", "Test"],
            "general_hypothesis": "A source can affect the next operation without direct terminal support, and source-set necessity cannot be inferred from one omission.",
            "reused_contracts": ["schemas/benchmark-bundle.schema.json", "schemas/validity-argument.schema.json", "schemas/metric-monitoring.schema.json"],
        },
        "effect_contract": {
            "baseline_minus_variant": ["final_acceptance", "next_operation_valid", "safety_preserved"],
            "variant_minus_baseline": ["effort_units"],
            "aggregation": "none_noncompensatory_vector",
            "invalid_policy": "exclude_from_effect_estimation_and_report_invalid",
            "noise_policy": "unchanged replays must exactly match baseline or all effects for that shape are unresolved_replay_noise",
        },
        "scenarios": [
            scenario("procurement-memo", "evidence-to-decision memo", {"task": "Recommend whether to approve supplier A", "state": "insurance not yet verified"}, procurement_sources, "proc-transition", "proc-terminal", "proc-sub-a", "proc-sub-b", "proc-stale", "proc-distractor", outcome(True, True, True, 5), outcome(False, False, False, 3), outcome(False, True, False, 4), outcome(False, False, False, 2)),
            scenario("incident-brief", "operational incident response brief", {"task": "Diagnose and safely recover the TLS outage", "state": "cause unknown; traffic degraded"}, incident_sources, "inc-transition", "inc-terminal", "inc-sub-a", "inc-sub-b", "inc-stale", "inc-distractor", outcome(True, True, True, 6), outcome(False, False, True, 4), outcome(False, True, False, 5), outcome(True, False, False, 2)),
        ],
        "claim_boundary": {
            "supported": ["The exact frozen fixture deterministically distinguishes transition effects, terminal redundancy, source-set necessity, stale substitution, distractor invariance, invalid state, and replay-noise gating."],
            "unsupported": ["agent capability", "professional validity", "portable document utility", "semantic mediation", "population prevalence", "cross-domain generalization", "deployment readiness", "treatment effect outside this fixture"],
        },
    }
    for sc in data["scenarios"]:
        for cell in sc["conditions"]:
            cell["realized_context_sha256"] = canonical_sha(materialize_context(sc, cell["intervention"]))
    return data


if __name__ == "__main__":
    HERE.mkdir(parents=True, exist_ok=True)
    (HERE / "fixture.json").write_text(json.dumps(build(), indent=2) + "\n")
