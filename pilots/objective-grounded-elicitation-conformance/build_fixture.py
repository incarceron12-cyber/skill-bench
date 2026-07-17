#!/usr/bin/env python3
"""Build deterministic objective-grounded elicitation conformance records.

All people, claims, responses, profiles, and consequences are builder-authored
synthetic fixtures. No model, network, or human call is made.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "pilots/objective-grounded-elicitation-conformance"
PACKS_PATH = PILOT / "claim-packs.json"
OBJECTIVES_PATH = PILOT / "objectives.json"
EPISODES_PATH = PILOT / "episodes.json"
ORACLE_PATH = PILOT / "private/oracle.json"

CONDITIONS = [
    "no_elicitation",
    "fixed_probe",
    "adaptive_probe",
    "oracle_profile",
    "inferred_profile",
    "corrupted_profile",
]
RESOURCE_ENVELOPE = {
    "downstream_steps": 2,
    "downstream_evidence_ids": ["public-brief", "frozen-claim-view"],
    "artifact_slots": 1,
    "state_write_slots": 1,
    "wall_seconds": 30,
}
CLAIM_LIMITS = {
    "human_participation": False,
    "expert_participation": False,
    "elicitation_effect": False,
    "professional_validity": False,
    "scientific_utility": False,
    "capability": False,
    "safety": False,
    "production_fitness": False,
    "readiness": False,
}


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


PACKS = [
    {
        "pack_id": "procurement-decision",
        "structure": "evidence-backed recommendation memo",
        "opening": "The supplier looks suitable, but something about the approval feels unresolved.",
        "claims": [
            {"claim_id": "hosting_region", "requirement": "required", "authority": "synthetic_service_owner", "truth": "eu_only", "sensitive": False, "known": True},
            {"claim_id": "conflict_disclosure", "requirement": "required", "authority": "synthetic_decision_owner", "truth": "minor_conflict_declared", "sensitive": True, "known": True},
            {"claim_id": "transition_preference", "requirement": "optional", "authority": "synthetic_service_owner", "truth": "phased", "sensitive": False, "known": True},
            {"claim_id": "integration_effort", "requirement": "optional", "authority": "none", "truth": None, "sensitive": False, "known": False},
            {"claim_id": "incumbent_price", "requirement": "optional", "authority": "synthetic_finance_owner", "truth": "restricted", "sensitive": True, "known": True},
        ],
        "rivals": ["security qualification is unresolved", "commercial conflict blocks approval", "transition risk alone explains the concern"],
        "consequence": {"type": "artifact", "target": "decision_memo", "check_id": "criterion-procurement-independent-v1", "success_state": "hold_pending_conflict_review"},
    },
    {
        "pack_id": "incident-handoff",
        "structure": "stateful operational handoff",
        "opening": "Recovery is possible, but the next operator should not act on the obvious route yet.",
        "claims": [
            {"claim_id": "rollback_authority", "requirement": "required", "authority": "synthetic_incident_commander", "truth": "commander_only", "sensitive": False, "known": True},
            {"claim_id": "dependency_state", "requirement": "required", "authority": "synthetic_service_owner", "truth": "cache_warmup_incomplete", "sensitive": False, "known": True},
            {"claim_id": "notification_preference", "requirement": "optional", "authority": "synthetic_incident_commander", "truth": "batch_updates", "sensitive": False, "known": True},
            {"claim_id": "root_cause", "requirement": "optional", "authority": "none", "truth": None, "sensitive": False, "known": False},
            {"claim_id": "affected_customer", "requirement": "optional", "authority": "synthetic_privacy_owner", "truth": "restricted", "sensitive": True, "known": True},
        ],
        "rivals": ["rollback is immediately authorized", "dependency state is healthy", "the concern is only communication cadence"],
        "consequence": {"type": "state", "target": "handoff_gate", "check_id": "criterion-incident-independent-v1", "success_state": "escalate_before_rollback"},
    },
]


def claim(pack: dict[str, Any], claim_id: str) -> dict[str, Any]:
    return next(item for item in pack["claims"] if item["claim_id"] == claim_id)


def objectives() -> list[dict[str, Any]]:
    rows = []
    for pack in PACKS:
        required = [item["claim_id"] for item in pack["claims"] if item["requirement"] == "required"]
        optional = [item["claim_id"] for item in pack["claims"] if item["requirement"] == "optional"]
        rows.append({
            "objective_id": f"objective-{pack['pack_id']}-v1",
            "pack_id": pack["pack_id"],
            "beneficiary": "synthetic_work_owner",
            "affected_parties": ["synthetic_operator", "synthetic_subject"],
            "intended_use": "produce one frozen artifact/state consequence without unsupported adoption",
            "required_claim_ids": required,
            "optional_claim_ids": optional,
            "claim_authority": {item["claim_id"]: item["authority"] for item in pack["claims"]},
            "unknown_claim_ids": [item["claim_id"] for item in pack["claims"] if not item["known"]],
            "sensitive_claim_ids": [item["claim_id"] for item in pack["claims"] if item["sensitive"]],
            "rival_interpretations": pack["rivals"],
            "permissible_question_classes": ["required_claim_clarification", "optional_preference", "bounded_unknown"],
            "prohibited_question_classes": ["restricted_value_request", "unrelated_personal_data"],
            "stop_rules": ["all required claims terminal", "burden budget reached", "required claim unauthorized or inaccessible"],
            "escalation_rules": ["required claim contradicted", "required authority unavailable"],
            "burden_budget": {"questions": 2, "active_seconds": 20, "corrections": 1},
            "loss": {"omission": 4, "unsupported_adoption": 7, "unauthorized_disclosure": 9, "delay": 2, "unnecessary_contact": 3},
            "downstream_consequence": pack["consequence"],
            "criterion": {"authored_before_conditions": True, "intervention_blind": True, "criterion_id": pack["consequence"]["check_id"]},
        })
    return rows


def question_event(episode_id: str, index: int, target: str, *, exposed: bool, response: str, locator: str | None) -> dict[str, Any]:
    return {
        "event_id": f"{episode_id}-q{index}",
        "event_type": "question",
        "opportunity": True,
        "target_claim_id": target,
        "question_class": "required_claim_clarification",
        "exposed": exposed,
        "response": response,
        "response_locator": locator,
    }


def claim_event(episode_id: str, index: int, claim_id: str, value: Any, origin: str, status: str, *, locator: str | None = None, unsupported: bool = False, correction: str = "none") -> dict[str, Any]:
    return {
        "event_id": f"{episode_id}-c{index}",
        "event_type": "claim_revision",
        "claim_id": claim_id,
        "value": value,
        "origin": origin,
        "evidence_locator": locator,
        "status": status,
        "unsupported_attribution": unsupported,
        "respondent_disposition": correction,
    }


def make_episode(pack: dict[str, Any], objective: dict[str, Any], condition: str) -> tuple[dict[str, Any], dict[str, Any]]:
    eid = f"{pack['pack_id']}--{condition}"
    required = objective["required_claim_ids"]
    c1, c2 = (claim(pack, cid) for cid in required)
    events: list[dict[str, Any]] = []
    final: dict[str, dict[str, Any]] = {}
    stop = "sufficient_completion"
    expected = "supported_required_claims"
    fidelity = True
    consequence_success = True
    questions = 0
    active = 0
    corrections = 0

    if condition == "no_elicitation":
        events.append(question_event(eid, 0, c1["claim_id"], exposed=False, response="none", locator=None))
        for idx, item in enumerate((c1, c2), 1):
            events.append(claim_event(eid, idx, item["claim_id"], "plausible_guess", "model_inferred", "inferred", unsupported=True))
            final[item["claim_id"]] = {"status": "inferred", "value": "plausible_guess", "source_event_id": events[-1]["event_id"]}
        stop, expected, fidelity, consequence_success = "premature_closure", "premature_closure", False, False
    elif condition in {"fixed_probe", "adaptive_probe"}:
        for idx, item in enumerate((c1, c2), 1):
            locator = f"responses/{eid}.txt#L{idx}"
            events.append(question_event(eid, idx, item["claim_id"], exposed=True, response="answer", locator=locator))
            events.append(claim_event(eid, idx, item["claim_id"], item["truth"], "probed", "confirmed", locator=locator, correction="accepted"))
            final[item["claim_id"]] = {"status": "confirmed", "value": item["truth"], "source_event_id": events[-1]["event_id"]}
        questions, active = 2, 12 if condition == "fixed_probe" else 10
        expected = "supported_required_claims"
        if condition == "fixed_probe":
            optional = next(item for item in pack["claims"] if item["claim_id"] in objective["optional_claim_ids"] and item["known"] and not item["sensitive"])
            events.append(claim_event(eid, 8, optional["claim_id"], optional["truth"], "spontaneous", "confirmed", locator=f"opening/{eid}.txt#L1", correction="accepted"))
        if condition == "adaptive_probe":
            # The first interpretation is explicitly corrected; only the correction survives.
            target = required[0]
            events.insert(1, claim_event(eid, 9, target, "incorrect_initial_interpretation", "respondent_inferred", "contradicted", locator=f"responses/{eid}.txt#L1", correction="corrected"))
            corrections = 1
            final[target] = {"status": "confirmed", "value": c1["truth"], "source_event_id": f"{eid}-c1"}
            expected = "correction_applied"
    elif condition == "oracle_profile":
        for idx, item in enumerate((c1, c2), 1):
            events.append(claim_event(eid, idx, item["claim_id"], item["truth"], "oracle_supplied", "confirmed", locator=f"treatment-profile/{eid}#{item['claim_id']}"))
            final[item["claim_id"]] = {"status": "confirmed", "value": item["truth"], "source_event_id": events[-1]["event_id"]}
        expected = "oracle_profile_control"
    elif condition == "inferred_profile":
        for idx, item in enumerate((c1, c2), 1):
            value = item["truth"] if idx == 1 else "wrong_but_plausible"
            events.append(claim_event(eid, idx, item["claim_id"], value, "model_inferred", "inferred", unsupported=True))
            final[item["claim_id"]] = {"status": "inferred", "value": value, "source_event_id": events[-1]["event_id"]}
        expected, fidelity, consequence_success = "unsupported_profile", False, True
        stop = "unsupported_closure"
    else:  # corrupted_profile
        wrong = "corrupted_value"
        events.append(claim_event(eid, 1, c1["claim_id"], wrong, "model_inferred", "contradicted", unsupported=True, correction="corrected"))
        locator = f"responses/{eid}.txt#L1"
        events.append(question_event(eid, 1, c1["claim_id"], exposed=True, response="answer", locator=locator))
        events.append(claim_event(eid, 2, c1["claim_id"], c1["truth"], "probed", "confirmed", locator=locator, correction="accepted"))
        second_locator = f"responses/{eid}.txt#L2"
        response = "refusal" if pack["pack_id"] == "procurement-decision" else "nonresponse"
        events.append(question_event(eid, 2, c2["claim_id"], exposed=True, response=response, locator=second_locator))
        events.append(claim_event(eid, 3, c2["claim_id"], None, "probed", "escalated", locator=second_locator, correction="accepted"))
        final[c1["claim_id"]] = {"status": "confirmed", "value": c1["truth"], "source_event_id": f"{eid}-c2"}
        final[c2["claim_id"]] = {"status": "escalated", "value": None, "source_event_id": f"{eid}-c3"}
        questions, active, corrections = 2, 9, 1
        stop, expected, fidelity, consequence_success = "justified_escalation", "corruption_corrected_and_escalated", True, False

    resolved = sum(item["status"] in {"confirmed", "contradicted", "unknown", "inaccessible", "unauthorized", "out_of_scope", "escalated"} for item in final.values())
    semantic_uptake = [cid for cid, item in final.items() if item["status"] == "confirmed"]
    unsupported = [cid for cid, item in final.items() if item["status"] == "inferred"]
    episode = {
        "episode_id": eid,
        "pack_id": pack["pack_id"],
        "objective_id": objective["objective_id"],
        "condition": condition,
        "participant_realization": "scripted_simulator" if condition in {"fixed_probe", "adaptive_probe", "corrupted_profile"} else "none",
        "events": events,
        "final_claim_states": final,
        "objective_progress": {"required_total": len(required), "required_terminal": resolved, "required_confirmed": sum(item["status"] == "confirmed" for item in final.values())},
        "semantic_uptake": {"claim_ids": semantic_uptake, "unsupported_claim_ids": unsupported},
        "profile_fidelity": {"supported": fidelity, "basis": "claim_event_replay" if fidelity else "insufficient_or_wrong_support"},
        "consequence": {"type": pack["consequence"]["type"], "target": pack["consequence"]["target"], "success": consequence_success, "event_id": f"{eid}-effect", "criterion_id": pack["consequence"]["check_id"]},
        "stop": {"classification": stop, "event_id": f"{eid}-stop"},
        "burden": {"questions": questions, "active_seconds": active, "corrections": corrections},
        "resource_envelope": RESOURCE_ENVELOPE,
        "claims": dict(CLAIM_LIMITS),
    }
    oracle = {"episode_id": eid, "expected_classification": expected, "expected_final": {cid: {"status": state["status"], "value": state["value"]} for cid, state in final.items()}}
    return episode, oracle


def main() -> int:
    PILOT.mkdir(parents=True, exist_ok=True)
    ORACLE_PATH.parent.mkdir(parents=True, exist_ok=True)
    objective_rows = objectives()
    episodes: list[dict[str, Any]] = []
    oracle_rows: list[dict[str, Any]] = []
    for pack, objective in zip(PACKS, objective_rows):
        for condition in CONDITIONS:
            episode, expected = make_episode(pack, objective, condition)
            episodes.append(episode)
            oracle_rows.append(expected)

    public_packs = []
    for pack in PACKS:
        public_pack = {key: value for key, value in pack.items() if key != "claims"}
        public_pack["claims"] = [
            {key: value for key, value in item.items() if key != "truth"}
            for item in pack["claims"]
        ]
        public_packs.append(public_pack)
    PACKS_PATH.write_text(json.dumps({"version": "1.0.0", "authorship": "builder-authored synthetic", "packs": public_packs}, indent=2, sort_keys=True) + "\n")
    OBJECTIVES_PATH.write_text(json.dumps({"version": "1.0.0", "frozen_before_episodes": True, "objectives": objective_rows}, indent=2, sort_keys=True) + "\n")
    private_truth = {
        pack["pack_id"]: {item["claim_id"]: item["truth"] for item in pack["claims"]}
        for pack in PACKS
    }
    ORACLE_PATH.write_text(json.dumps({"version": "1.0.0", "visibility": "post-classification-conformance-only", "not_evaluator_input": True, "private_claim_truth": private_truth, "episodes": oracle_rows}, indent=2, sort_keys=True) + "\n")

    provenance_paths = [
        "papers/agent-benchmarks/2026-07-17-inciteresearch-prequestion-elicitation-validity.md",
        "papers/agent-benchmarks/2026-07-17-organizational-tacit-knowledge-simulation-validity.md",
        "docs/benchmark-design-taxonomy.md",
        "pilots/interaction-evidence-conformance/README.md",
        "pilots/interaction-evidence-conformance/episodes.json",
        "pilots/interaction-evidence-conformance/private/oracle.json",
        "scripts/validate_interaction_evidence.py",
        "tests/test_interaction_evidence_conformance.py",
    ]
    package = {
        "version": "1.0.0",
        "status": "internal_calibration_only",
        "purpose": "Zero-call conformance test of objective-grounded claim routing and profile fidelity across two unlike work shapes.",
        "condition_matrix": CONDITIONS,
        "observer": {"name": "domain-neutral-objective-elicitation-observer-v1", "evaluator_inputs": ["claim-packs.json", "objectives.json", "episodes.json"], "excluded_inputs": ["private/oracle.json"]},
        "claim_packs": {"path": str(PACKS_PATH.relative_to(ROOT)), "sha256": file_hash(PACKS_PATH)},
        "objectives": {"path": str(OBJECTIVES_PATH.relative_to(ROOT)), "sha256": file_hash(OBJECTIVES_PATH)},
        "private_oracle": {"path": str(ORACLE_PATH.relative_to(ROOT)), "sha256": file_hash(ORACLE_PATH)},
        "resource_envelope": RESOURCE_ENVELOPE,
        "claim_limits": CLAIM_LIMITS,
        "design_evidence": [
            {"path": provenance_paths[0], "locators": ["review lines 21-25", "review lines 152-169", "review lines 235-261"], "supports": "profile claim ladder, oracle/corruption conditions, correction and consequence separation"},
            {"path": provenance_paths[1], "locators": ["review lines 158-176", "review lines 223-255"], "supports": "claim routing, authority, claim-state stopping, burden and synthetic claim ceiling"},
            {"path": provenance_paths[2], "locators": ["lines 161-239"], "supports": "frozen objective, event lineage, terminal claim states, stop errors and separate denominators"},
        ],
        "provenance": [{"path": path, "sha256": file_hash(ROOT / path)} for path in provenance_paths],
        "episodes": episodes,
    }
    EPISODES_PATH.write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
    print(f"wrote 2 claim packs, 2 objectives, {len(episodes)} episodes, and private oracle")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
