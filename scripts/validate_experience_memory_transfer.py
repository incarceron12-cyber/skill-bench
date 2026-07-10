#!/usr/bin/env python3
"""Validate and replay the synthetic experience-memory transfer conformance slice."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KINDS = {"valid_procedure", "failed_attempt", "stale_observation", "scoped_gotcha", "contradiction", "safe_alternative"}
REQUIRED_CONDITIONS = {"no_memory", "evidence_only", "provenance_gated_promoted_lesson"}
REQUIRED_UNSUPPORTED = {"professional competence", "population prevalence", "cross-domain generality", "deployment safety", "release readiness"}


def semantic_errors(package, check_paths=False):
    errors = []
    design = package.get("design", {})
    if package.get("status") != "internal_synthetic_contract_calibration":
        errors.append("status must preserve synthetic calibration scope")
    for key in ("source_review", "source_provenance"):
        value = design.get(key)
        if not value or (check_paths and not (ROOT / value).is_file()):
            errors.append(f"design.{key} must reference an existing repository file")
    provenance_path = ROOT / design.get("source_provenance", "")
    if provenance_path.is_file():
        provenance = json.loads(provenance_path.read_text())
        if provenance.get("code", {}).get("archive_sha256") != design.get("source_release_sha256"):
            errors.append("source release hash does not match provenance manifest")
    if check_paths:
        for path in design.get("reused_contracts", []):
            if not (ROOT / path).is_file(): errors.append(f"reused contract does not exist: {path}")

    trajectories = package.get("trajectory_history", [])
    by_id = {t.get("id"): t for t in trajectories}
    if {t.get("kind") for t in trajectories} != REQUIRED_KINDS:
        errors.append("trajectory history must contain exactly the six required knowledge kinds")
    for t in trajectories:
        for field in ("source_span", "environment_version", "valid_time", "applicability", "attempted", "realized"):
            if field not in t: errors.append(f"{t.get('id')} lacks {field}")
    stale = next((t for t in trajectories if t.get("kind") == "stale_observation"), {})
    contradiction = next((t for t in trajectories if t.get("kind") == "contradiction"), {})
    if contradiction.get("contradicts") != stale.get("id") or not stale.get("superseded_by"):
        errors.append("stale evidence must have explicit contradiction and supersession lineage")
    failed = next((t for t in trajectories if t.get("kind") == "failed_attempt"), {})
    if not failed.get("attempted") or failed.get("realized"):
        errors.append("failed attempt must distinguish attempt from realization")

    probes = package.get("probes", [])
    if {p.get("estimand") for p in probes} != {"evidence_grounded_recall", "held_out_action_benefit"}:
        errors.append("QA and held-out action must remain separate estimands")
    if len({p.get("lineage_cluster") for p in probes}) != len(probes):
        errors.append("equivalent-form QA and held-out action require distinct lineage clusters")

    conditions = package.get("conditions", [])
    if {c.get("condition") for c in conditions} != REQUIRED_CONDITIONS:
        errors.append("three matched memory conditions are required")
    for c in conditions:
        available = set(c.get("available_evidence_ids", []))
        if not available <= set(by_id): errors.append(f"{c.get('condition')} references unknown available evidence")
        for stage in ("qa", "action"):
            accessed = set(c.get(stage, {}).get("accessed_ids", []))
            adopted = set(c.get(stage, {}).get("adopted_ids", []))
            if not adopted <= accessed <= available:
                errors.append(f"{c.get('condition')} {stage} must preserve available -> accessed -> adopted ordering")
    cell = next((c for c in conditions if c.get("condition") == "evidence_only"), {})
    if not cell.get("qa", {}).get("correct") or not cell.get("action", {}).get("harmful_transfer") or not cell.get("action", {}).get("rollback"):
        errors.append("evidence-only cell must plant correct QA, harmful transfer, and rollback evidence")
    promoted = next((c for c in conditions if c.get("condition") == "provenance_gated_promoted_lesson"), {})
    if not promoted.get("action", {}).get("safe") or not promoted.get("action", {}).get("receipt_emitted"):
        errors.append("promoted lesson cell must realize the declared safe action and receipt")

    execution = package.get("execution", {})
    if execution.get("stochastic_components") and execution.get("repetitions_per_cell", 0) < 2:
        errors.append("stochastic components require repeated cells")
    if execution.get("cluster_unit") != "source_lineage_cluster":
        errors.append("source-lineage clustering must be declared")
    unsupported = set(package.get("claim_limits", {}).get("unsupported", []))
    if not REQUIRED_UNSUPPORTED <= unsupported:
        errors.append("claim limits omit required non-claims")
    return errors


def replay(package):
    return {
        c["condition"]: {
            "qa_correct": c["qa"]["correct"],
            "action_safe": c["action"]["safe"],
            "harmful_transfer": c["action"]["harmful_transfer"],
            "evidence_access_count": len(c["qa"]["accessed_ids"]) + len(c["action"]["accessed_ids"]),
            "evidence_adoption_count": len(c["qa"]["adopted_ids"]) + len(c["action"]["adopted_ids"]),
        } for c in package["conditions"]
    }


def validate_file(path, check_paths=False):
    package = json.loads(Path(path).read_text())
    errors = semantic_errors(package, check_paths)
    if errors: raise ValueError("\n".join(errors))
    return package


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    package = validate_file(args.path, args.check_paths)
    result = {"package_sha256": hashlib.sha256(args.path.read_bytes()).hexdigest(), "cells": replay(package), "claim_scope": "exact deterministic synthetic fixture only"}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__": main()
