#!/usr/bin/env python3
"""Build the immutable-parent v0.2 staged-lineage conformance fixture."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PARENT = HERE / "fixture.json"
REVIEW = ROOT / "papers/agent-benchmarks/2026-07-19-autosynthesis-meta-analysis-validity.md"
STAGES = ("protocol", "search", "screen", "study_map", "extract", "transform", "analyze", "report")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def node(case_id: str, stage: str, previous: str | None, status: str = "passed", signature: str | None = None) -> dict[str, Any]:
    artifact_id = f"{case_id}-{stage}"
    return {
        "stage": stage,
        "artifact_id": artifact_id,
        "input_artifact_ids": [] if previous is None else [previous],
        "evidence_locators": [f"synthetic://{case_id}/{stage}/1"],
        "admissibility": status,
        "failure_signature": signature,
    }


def case(shape: str, suffix: str, *, failed_stage: str | None = None, signature: str | None = None,
         reference: float = 0.10, candidate: float = 0.10, tolerance: float = 0.02,
         reference_decision: str = "act", candidate_decision: str = "act",
         authorized_protocol_difference: bool = False) -> dict[str, Any]:
    case_id = f"{shape}-{suffix}"
    chain = []
    previous = None
    for stage in STAGES:
        status = "failed" if stage == failed_stage else "passed"
        if stage == "protocol" and authorized_protocol_difference:
            status = "authorized_divergence"
        item = node(case_id, stage, previous, status, signature if stage == failed_stage else None)
        chain.append(item)
        previous = item["artifact_id"]
    endpoint_close = abs(candidate - reference) <= tolerance
    earliest = failed_stage
    accepted = failed_stage is None
    disposition = "authorized_protocol_difference" if authorized_protocol_difference else ("chain_valid" if accepted else "blocked_by_stage_failure")
    return {
        "case_id": case_id,
        "shape_id": shape,
        "chain": chain,
        "protocol_difference": {
            "present": authorized_protocol_difference,
            "authorized": authorized_protocol_difference,
            "authority_locator": f"synthetic://{case_id}/protocol-approval" if authorized_protocol_difference else None,
        },
        "endpoint": {
            "reference": reference,
            "candidate": candidate,
            "absolute_distance": round(abs(candidate - reference), 6),
            "tolerance": tolerance,
            "within_tolerance": endpoint_close,
            "reference_decision": reference_decision,
            "candidate_decision": candidate_decision,
            "decision_agreement": reference_decision == candidate_decision,
        },
        "expected": {
            "earliest_consequential_break": earliest,
            "stage_chain_accepted": accepted,
            "disposition": disposition,
        },
    }


def build() -> dict[str, Any]:
    cases = []
    for shape in ("controlled-intervention-synthesis", "nonintervention-association-synthesis"):
        cases.extend([
            case(shape, "clean"),
            case(shape, "duplicate-report-dependence", failed_stage="study_map", signature="duplicate_reports_treated_as_independent", candidate=0.11),
            case(shape, "wrong-role-verbatim-number", failed_stage="extract", signature="verbatim_number_bound_to_wrong_group_or_time", candidate=0.10),
            case(shape, "compensating-errors-close-endpoint", failed_stage="extract", signature="offsetting_extraction_errors", candidate=0.10),
            case(shape, "authorized-protocol-difference", candidate=0.16, tolerance=0.02, candidate_decision="defer", authorized_protocol_difference=True),
        ])
    return {
        "version": "2.0.0",
        "status": "internal_synthetic_contract_calibration",
        "immutable_parent": {"path": str(PARENT.relative_to(ROOT)), "sha256": sha256(PARENT), "version": "1.0.0"},
        "design_basis": {
            "review_path": str(REVIEW.relative_to(ROOT)),
            "review_sha256": sha256(REVIEW),
            "review_locators": ["Unique insight: endpoint agreement is a lossy checksum over a staged professional artifact", "Falsifiable cross-domain benchmark slice", "Action items"],
            "charter_objectives": ["B", "C"],
            "general_hypothesis": "A close endpoint cannot compensate for an unresolved consequential lineage break, while a disclosed authorized protocol difference may license a bounded divergent endpoint.",
            "scope_boundary": "The two evidence-synthesis shapes test reusable staged-lineage machinery; neither is a permanent benchmark domain.",
        },
        "stage_order": list(STAGES),
        "rules": {
            "cross_stage_conservation": "every stage after protocol consumes an artifact from the immediately preceding stage",
            "admissible_states": ["passed", "authorized_divergence", "failed"],
            "endpoint_policy": "report distance and decision agreement separately; neither can override a failed stage",
            "earliest_break_policy": "first failed stage in stage_order; authorized_divergence is not a break when authority is present",
        },
        "cases": cases,
        "claim_boundary": {
            "supported": ["The exact frozen synthetic fixture diagnoses planted lineage failures independently of endpoint proximity and preserves authorized protocol divergence as a separate disposition."],
            "unsupported": ["agent capability", "professional validity", "statistical-method validity", "population prevalence", "cross-domain generalization", "deployment readiness", "external treatment effect"],
        },
    }


if __name__ == "__main__":
    (HERE / "lineage-fixture-v0.2.json").write_text(json.dumps(build(), indent=2) + "\n")
