#!/usr/bin/env python3
"""Validate and deterministically replay the longitudinal-decision necessity slice."""
import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_INTERVENTIONS = {"correct", "absent", "irrelevant", "stale", "contradictory"}
REQUIRED_ACTION_KINDS = {"proceed", "alternate_valid_path", "ask", "abstain", "escalate"}
REQUIRED_OUTCOMES = {"supported", "missing", "invalid"}
REQUIRED_UNSUPPORTED = {
    "history-sensitive agent capability", "memory-system improvement", "professional validity",
    "clinical validity", "safety", "production fitness", "deployment readiness",
    "cross-domain generality", "population prevalence", "normative appropriateness",
}


def _time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def semantic_errors(suite, check_paths=False):
    errors = []
    if suite.get("status") != "internal_synthetic_zero_call_conformance":
        errors.append("status must preserve zero-call synthetic scope")
    design = suite.get("design", {})
    for path in design.get("source_reviews", []) + design.get("reused_contracts", []):
        if check_paths and not (ROOT / path).is_file():
            errors.append(f"referenced repository file does not exist: {path}")
    for artifact in design.get("source_artifacts", []):
        path = ROOT / artifact.get("path", "")
        if check_paths and not path.is_file():
            errors.append(f"source artifact does not exist: {artifact.get('path')}")
        elif check_paths and hashlib.sha256(path.read_bytes()).hexdigest() != artifact.get("sha256"):
            errors.append(f"source artifact hash mismatch: {artifact.get('path')}")

    freeze = suite.get("freeze", {})
    if not freeze.get("frozen_before_observation"):
        errors.append("suite must be frozen prospectively before observation")
    if set(freeze.get("required_interventions", [])) != REQUIRED_INTERVENTIONS:
        errors.append("freeze must declare exactly five required interventions")
    if freeze.get("cluster_unit") != "source_work_unit":
        errors.append("cluster unit must be source_work_unit")

    scenarios = suite.get("scenarios", [])
    if len(scenarios) < 2 or len({s.get("domain_shape") for s in scenarios}) < 2:
        errors.append("at least two distinct knowledge-work shapes are required")
    if len({s.get("source_work_unit") for s in scenarios}) != len(scenarios):
        errors.append("scenarios require distinct source-work-unit clusters")
    seen_cells = set()
    outcome_counts = {name: 0 for name in REQUIRED_OUTCOMES}
    for scenario in scenarios:
        sid = scenario.get("scenario_id", "unknown")
        atoms = {a.get("evidence_id"): a for a in scenario.get("evidence_atoms", [])}
        actions = {a.get("action_id"): a for a in scenario.get("actions", [])}
        if {a.get("kind") for a in actions.values()} != REQUIRED_ACTION_KINDS:
            errors.append(f"{sid} must declare proceed, alternative, ask, abstain, and escalate actions")
        for atom in atoms.values():
            required = {"event_time", "record_time", "availability_time", "valid_from", "valid_to", "authority", "relevance", "transformation_lineage"}
            if not required <= set(atom):
                errors.append(f"{sid}/{atom.get('evidence_id')} lacks typed time, authority, or lineage")
                continue
            try:
                if _time(atom["event_time"]) > _time(atom["record_time"]) or _time(atom["record_time"]) > _time(atom["availability_time"]):
                    errors.append(f"{sid}/{atom.get('evidence_id')} violates event <= record <= availability time")
            except (TypeError, ValueError):
                errors.append(f"{sid}/{atom.get('evidence_id')} has invalid time")
        oracle = scenario.get("oracle", {})
        if oracle.get("oracle_type") == "recorded_behavior" or oracle.get("normative_appropriateness"):
            errors.append(f"{sid} launders retrospective behavior into a normative oracle")
        if not oracle.get("declared_before_observation"):
            errors.append(f"{sid} oracle was not declared prospectively")
        witness = scenario.get("recorded_behavior_witness", {})
        if witness.get("used_as_oracle") or witness.get("normative_appropriateness"):
            errors.append(f"{sid} recorded behavior witness cannot inherit normative authority")
        chronology = scenario.get("chronology", {})
        sequences = chronology.get("acceptable_sequences", [])
        if chronology.get("claim") == "unique" and len(sequences) != 1:
            errors.append(f"{sid} falsely claims a unique chronology")
        if not sequences:
            errors.append(f"{sid} must declare acceptable chronology sequences or partial orders")

        conditions = scenario.get("conditions", [])
        if {c.get("condition") for c in conditions} != REQUIRED_INTERVENTIONS:
            errors.append(f"{sid} lacks the exact five matched interventions")
            continue
        correct = next(c for c in conditions if c.get("condition") == "correct")
        absent = next(c for c in conditions if c.get("condition") == "absent")
        irrelevant = next(c for c in conditions if c.get("condition") == "irrelevant")
        if set(correct.get("expected_admissible_action_ids", [])) == set(absent.get("expected_admissible_action_ids", [])):
            errors.append(f"{sid} shows history access but no necessity boundary")
        if set(absent.get("expected_admissible_action_ids", [])) != set(irrelevant.get("expected_admissible_action_ids", [])):
            errors.append(f"{sid} irrelevant history changes the action boundary")
        if correct.get("expected_boundary") == absent.get("expected_boundary"):
            errors.append(f"{sid} correct history does not change the declared boundary")
        for condition in conditions:
            cid = condition.get("condition")
            seen_cells.add((sid, cid))
            available = set(condition.get("available_ids", []))
            visible = set(condition.get("visible_ids", []))
            adopted = set(condition.get("adopted_ids", []))
            admissible = set(condition.get("expected_admissible_action_ids", []))
            if not adopted <= visible <= available <= set(atoms):
                errors.append(f"{sid}/{cid} violates available -> visible -> adopted evidence flow")
            if not admissible or not admissible <= set(actions):
                errors.append(f"{sid}/{cid} has unknown or empty admissible actions")
            if condition.get("selected_action_id") not in admissible:
                errors.append(f"{sid}/{cid} selected action is not in the admissible set")
            outcome = condition.get("outcome")
            if outcome not in outcome_counts:
                errors.append(f"{sid}/{cid} has unknown outcome")
            else:
                outcome_counts[outcome] += 1
            if outcome == "missing" and condition.get("observer_coverage") == "complete":
                errors.append(f"{sid}/{cid} missing outcome requires incomplete observer coverage")
            if outcome == "invalid" and not str(condition.get("observer_coverage", "")).startswith("invalid_"):
                errors.append(f"{sid}/{cid} invalid outcome requires an invalid observer/oracle reason")

    metric = suite.get("metric", {})
    eligible = len(seen_cells)
    if metric.get("eligible_count") != eligible or metric.get("attempted_count") != eligible:
        errors.append("metric eligible/attempted denominator must equal all frozen cells")
    if metric.get("supported_count") != outcome_counts["supported"] or metric.get("missing_count") != outcome_counts["missing"] or metric.get("invalid_count") != outcome_counts["invalid"]:
        errors.append("metric outcome counts do not replay")
    if sum(outcome_counts.values()) != eligible:
        errors.append("missing and invalid cells must remain in the frozen denominator")
    if metric.get("primary_denominator") != "all_frozen_eligible_cells" or metric.get("estimate") is not None:
        errors.append("contract calibration cannot drop cells or report a package-performance estimate")
    if set(outcome_counts) != REQUIRED_OUTCOMES or not all(outcome_counts.values()):
        errors.append("fixture must exercise supported, missing, and invalid policies")

    unsupported = set(suite.get("claim_limits", {}).get("unsupported", []))
    if not REQUIRED_UNSUPPORTED <= unsupported:
        errors.append("claim limits omit required unsupported upgrades")
    return errors


def replay(suite):
    cells = []
    for scenario in suite["scenarios"]:
        absent = next(c for c in scenario["conditions"] if c["condition"] == "absent")
        for condition in scenario["conditions"]:
            cells.append({
                "scenario_id": scenario["scenario_id"],
                "condition": condition["condition"],
                "history_available": bool(condition["available_ids"]),
                "history_visible": bool(condition["visible_ids"]),
                "history_adopted": bool(condition["adopted_ids"]),
                "boundary_changed_from_absent": set(condition["expected_admissible_action_ids"]) != set(absent["expected_admissible_action_ids"]),
                "selected_action_admissible": condition["selected_action_id"] in condition["expected_admissible_action_ids"],
                "outcome": condition["outcome"],
                "cluster": scenario["source_work_unit"],
            })
    counts = {name: sum(c["outcome"] == name for c in cells) for name in REQUIRED_OUTCOMES}
    return {"cells": cells, "counts": counts, "frozen_denominator": len(cells), "performance_estimate": None}


def validate_file(path, check_paths=False):
    suite = json.loads(Path(path).read_text(encoding="utf-8"))
    errors = semantic_errors(suite, check_paths)
    if errors:
        raise ValueError("\n".join(errors))
    return suite


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    suite = validate_file(args.path, args.check_paths)
    result = {
        "suite_sha256": hashlib.sha256(args.path.read_bytes()).hexdigest(),
        "replay": replay(suite),
        "claim_scope": "exact deterministic synthetic zero-call conformance only",
    }
    text = json.dumps(result, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
