#!/usr/bin/env python3
"""Build the frozen, builder-authored interaction conformance fixture."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR))

from scripts.validate_interaction_evidence import ROOT, canonical_hash, file_hash, sha256_bytes

PILOT = ROOT / "pilots/interaction-evidence-conformance"
FIXTURE = PILOT / "episodes.json"
ORACLE = PILOT / "private/oracle.json"

CONDITIONS = [
    {"condition_id": "full_information", "information_missing": False, "channel_available": False, "participant_realization": "none"},
    {"condition_id": "no_channel", "information_missing": True, "channel_available": False, "participant_realization": "none"},
    {"condition_id": "scripted", "information_missing": True, "channel_available": True, "participant_realization": "scripted_policy"},
    {"condition_id": "simulator", "information_missing": True, "channel_available": True, "participant_realization": "model_simulator"},
]

REQUIREMENTS = {
    "decision_memo": [
        "Recommend approve, hold, or reject using the frozen evidence threshold.",
        "State unresolved sensitivity rather than deleting it.",
        "Preserve the evidence appendix identifier.",
    ],
    "workspace_repair": [
        "Restore the current service route after the incident update.",
        "Preserve the audit lock and unrelated customer-note state.",
        "Record the applied revision and verification result.",
    ],
}

INITIAL = {
    "decision_memo": {"recommendation": "hold", "threshold": 0.80, "sensitivity_note": "unresolved", "appendix_id": "EV-17"},
    "workspace_repair": {"route": "legacy", "audit_lock": "sealed", "customer_note": "retain", "revision": 1},
}


def _message(content: str) -> dict[str, str]:
    return {"content": content, "sha256": sha256_bytes(content.encode())}


def _participant(condition: str) -> dict[str, Any]:
    realization = next(item["participant_realization"] for item in CONDITIONS if item["condition_id"] == condition)
    if realization == "none":
        return {"realization": "none", "assigned_role": "none", "claim_label": "none", "authority_scope": [], "policy_id": "none"}
    return {
        "realization": realization,
        "assigned_role": "synthetic_decision_owner",
        "claim_label": "synthetic_fixture",
        "authority_scope": ["threshold_revision", "route_revision", "preference_revision"],
        "policy_id": "script-v1" if realization == "scripted_policy" else "simulator-placeholder-v1",
    }


def make_case(
    case_id: str,
    shape: str,
    condition: str,
    expected: str,
    *,
    final: dict[str, Any] | None = None,
    exercised: bool = False,
    message_text: str | None = None,
    authority: str = "threshold_revision",
    disposition: str = "not_applicable",
    justified: bool = False,
    endpoint: bool = False,
    environment_valid: bool = True,
    preserved: dict[str, bool] | None = None,
    matched_control: str | None = None,
) -> tuple[dict[str, Any], dict[str, str]]:
    info_missing = next(item["information_missing"] for item in CONDITIONS if item["condition_id"] == condition)
    available = next(item["channel_available"] for item in CONDITIONS if item["condition_id"] == condition)
    requirements = REQUIREMENTS[shape]
    initial = INITIAL[shape]
    final_content = final or dict(initial)
    message = _message(message_text) if message_text is not None else None
    if exercised and message is None:
        raise ValueError(f"{case_id}: exercised fixtures require message text")
    receipt = (
        {"received": True, "receipt_event_id": f"evt-{case_id}-receipt", "message_sha256": message["sha256"]}
        if exercised and message is not None
        else None
    )
    propositions = []
    if message:
        propositions = [{
            "proposition_id": f"prop-{case_id}",
            "text": message_text,
            "message_sha256": message["sha256"],
            "required_authority": authority,
        }]
    protected = list(initial)
    preserved_map = preserved or {key: True for key in protected}
    observations = [{"locus": key, "preserved": preserved_map[key]} for key in protected]
    damage = [key for key, value in preserved_map.items() if not value]
    semantic: dict[str, Any] = {
        "disposition": disposition,
        "propositions": propositions,
        "uptake_evidence": {"trace_event_id": f"evt-{case_id}-uptake"} if disposition == "adopted" else {},
        "justified": justified,
        "basis_evidence": ["public-requirement-2"] if disposition == "rejected" and justified else [],
    }
    case = {
        "case_id": case_id,
        "scenario_id": f"scenario-{shape}",
        "work_shape": shape,
        "condition_id": condition,
        "information_missing": info_missing,
        "public_requirements": requirements,
        "public_requirements_sha256": canonical_hash(requirements),
        "initial_state": {"content": initial, "sha256": canonical_hash(initial)},
        "final_state": {"content": final_content, "sha256": canonical_hash(final_content)},
        "participant": _participant(condition),
        "trigger": {
            "clock_type": "authored_schedule",
            "trigger_type": "decision_point" if shape == "decision_memo" else "inspected_state",
            "expected_value": "before_commit",
            "observed_value": "before_commit",
            "trigger_event_id": f"evt-{case_id}-trigger",
        },
        "channel": {"channel_type": "clarification", "available": available, "exercised": exercised},
        "message": message,
        "receipt": receipt,
        "semantic_disposition": semantic,
        "repair_observation": {
            "attempted": disposition == "adopted",
            "repair_event_ids": [f"evt-{case_id}-repair"] if disposition == "adopted" else [],
            "changed_loci": [key for key in final_content if final_content.get(key) != initial.get(key)],
            "expected_protected_loci": protected,
            "preservation_observations": observations,
            "collateral_damage_loci": damage,
        },
        "endpoint_observation": {"target_satisfied": endpoint, "observer_event_id": f"evt-{case_id}-endpoint"},
        "effect_evidence": {
            "matched_control_case_id": matched_control,
            "comparison_basis": "frozen_synthetic_pair" if matched_control else "none",
        },
        "burden": {
            "active_seconds": 4 if exercised else 0,
            "wait_seconds": 2 if exercised else 0,
            "interruptions": 1 if exercised else 0,
            "correction_actions": 1 if expected == "harmful_collateral_damage" else 0,
        },
        "environment": {"valid": environment_valid, "setup_event_id": f"evt-{case_id}-setup", "invalid_reason": None if environment_valid else "planted_state_hash_mismatch"},
    }
    return case, {"case_id": case_id, "expected_outcome": expected}


def main() -> int:
    PILOT.mkdir(parents=True, exist_ok=True)
    ORACLE.parent.mkdir(parents=True, exist_ok=True)
    cases: list[dict[str, Any]] = []
    expected: list[dict[str, str]] = []

    specs = [
        make_case("memo-full", "decision_memo", "full_information", "full_information_control", endpoint=True),
        make_case("memo-no-channel", "decision_memo", "no_channel", "unavailable", endpoint=False),
        make_case("memo-script-unexercised", "decision_memo", "scripted", "unexercised", endpoint=False),
        make_case("memo-script-ignored", "decision_memo", "scripted", "ignored", exercised=True, message_text="Raise the approval threshold to 0.90.", disposition="ignored", endpoint=False),
        make_case("memo-sim-rejected", "decision_memo", "simulator", "justified_rejection", exercised=True, message_text="Delete the unresolved sensitivity note.", authority="preference_revision", disposition="rejected", justified=True, endpoint=True),
        make_case("memo-sim-beneficial", "decision_memo", "simulator", "beneficial", exercised=True, message_text="Raise the approval threshold to 0.90.", disposition="adopted", endpoint=True, final={"recommendation": "reject", "threshold": 0.90, "sensitivity_note": "unresolved", "appendix_id": "EV-17"}, matched_control="memo-no-channel"),
        make_case("workspace-full", "workspace_repair", "full_information", "full_information_control", endpoint=True),
        make_case("workspace-no-channel", "workspace_repair", "no_channel", "unavailable", endpoint=False),
        make_case("workspace-script-ineffective", "workspace_repair", "scripted", "adopted_ineffective", exercised=True, message_text="Route traffic through service-v2.", authority="route_revision", disposition="adopted", endpoint=False, final={"route": "legacy", "audit_lock": "sealed", "customer_note": "retain", "revision": 2}),
        make_case("workspace-script-beneficial", "workspace_repair", "scripted", "beneficial", exercised=True, message_text="Route traffic through service-v2.", authority="route_revision", disposition="adopted", endpoint=True, final={"route": "service-v2", "audit_lock": "sealed", "customer_note": "retain", "revision": 2}, matched_control="workspace-no-channel"),
        make_case("workspace-sim-harmful", "workspace_repair", "simulator", "harmful_collateral_damage", exercised=True, message_text="Route traffic through service-v2.", authority="route_revision", disposition="adopted", endpoint=True, final={"route": "service-v2", "audit_lock": "open", "customer_note": "retain", "revision": 2}, preserved={"route": True, "audit_lock": False, "customer_note": True, "revision": True}),
        make_case("workspace-sim-invalid", "workspace_repair", "simulator", "invalid_environment", exercised=True, message_text="Route traffic through service-v2.", authority="route_revision", disposition="adopted", endpoint=True, environment_valid=False, final={"route": "service-v2", "audit_lock": "sealed", "customer_note": "retain", "revision": 2}),
    ]
    for case, oracle_row in specs:
        cases.append(case)
        expected.append(oracle_row)

    oracle = {
        "oracle_version": "1.0.0",
        "visibility": "post-classification-conformance-only",
        "not_evaluator_input": True,
        "authorship": "builder-authored synthetic labels",
        "cases": expected,
    }
    ORACLE.write_text(json.dumps(oracle, indent=2, sort_keys=True) + "\n")

    provenance_paths = [
        "papers/agent-benchmarks/2026-07-14-deskcraft-interactive-workflow-validity.md",
        "papers/agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md",
        "data/papers/pdfs/2606.03103v1-deskcraft.pdf",
        "data/papers/pdfs/2607.04329v1-has-bench.pdf",
        "data/sources/releases/2606.03103v1-deskcraft/provenance.json",
    ]
    package = {
        "package_version": "1.0.0",
        "status": "internal_calibration_only",
        "purpose": "Exercise the interaction evidence ladder over two unlike retained work shapes without model or human calls.",
        "observer": {
            "name": "domain-neutral-interaction-observer-v1",
            "evaluator_inputs": ["episodes.json:cases", "episodes.json:condition_matrix"],
            "excluded_inputs": ["private/oracle.json", "paper claims", "participant social-role labels"],
        },
        "private_oracle": {"path": str(ORACLE.relative_to(ROOT)), "sha256": file_hash(ORACLE)},
        "condition_matrix": CONDITIONS,
        "claims": {
            "human_participation": False,
            "causal_benefit": False,
            "professional_validity": False,
            "capability": False,
            "safety": False,
            "production_fitness": False,
            "readiness": False,
        },
        "claim_limits": {"unsupported": [
            "human collaboration",
            "causal interaction benefit",
            "professional validity",
            "agent capability",
            "safety",
            "production fitness",
            "readiness",
        ]},
        "provenance": [{"path": path, "sha256": file_hash(ROOT / path)} for path in provenance_paths],
        "design_evidence": [
            {"source": provenance_paths[0], "locators": ["pp. 6-12", "review lines 171-201", "review lines 271-282"], "supports": "opportunity/trigger/receipt/adoption/repair/effect/burden separation and matched conditions"},
            {"source": provenance_paths[1], "locators": ["pp. 4-6", "review lines 102-115", "review lines 161-172"], "supports": "participant realization, authority-bearing events, availability/exercise/uptake/effect and plural burden"},
        ],
        "work_shapes": [
            {"work_shape": "decision_memo", "structure": "evidence-backed recommendation artifact with retained uncertainty"},
            {"work_shape": "workspace_repair", "structure": "stateful operational repair with protected unrelated state"},
        ],
        "cases": cases,
    }
    FIXTURE.write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")
    print(f"wrote {FIXTURE.relative_to(ROOT)} ({len(cases)} cases)")
    print(f"wrote {ORACLE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
