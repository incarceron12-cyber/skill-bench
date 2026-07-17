#!/usr/bin/env python3
"""Validate and replay objective-grounded elicitation conformance episodes.

The observer classifies public episode records first. The frozen private oracle is
loaded only to compare classifications and expected final states afterward.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from scripts.validate_provenance_boundary import validate_record
except ModuleNotFoundError:  # Direct `python scripts/...` execution.
    from validate_provenance_boundary import validate_record

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/objective-grounded-elicitation-conformance"
DEFAULT_FIXTURE = PILOT / "episodes.json"
DEFAULT_ORACLE = PILOT / "private/oracle.json"
CANONICAL_PATH = "docs/benchmark-design-taxonomy.md"
CANONICAL_ROLE = "objective_grounded_elicitation_design_basis"
REQUIRED_CONDITIONS = {"no_elicitation", "fixed_probe", "adaptive_probe", "oracle_profile", "inferred_profile", "corrupted_profile"}
TERMINAL = {"confirmed", "contradicted", "unknown", "inaccessible", "unauthorized", "out_of_scope", "escalated"}
ORIGINS = {"spontaneous", "probed", "respondent_inferred", "model_inferred", "oracle_supplied"}
RESPONSES = {"answer", "refusal", "nonresponse", "none"}
REQUIRED_FALSE_CLAIMS = {"human_participation", "expert_participation", "elicitation_effect", "professional_validity", "scientific_utility", "capability", "safety", "production_fitness", "readiness"}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_ref(package: dict[str, Any], key: str, errors: list[str]) -> dict[str, Any]:
    ref = package.get(key, {})
    path = ROOT / ref.get("path", "missing")
    if not path.is_file():
        errors.append(f"missing {key} file: {ref.get('path')}")
        return {}
    if ref.get("sha256") != file_hash(path):
        errors.append(f"{key} hash mismatch")
    return json.loads(path.read_text())


def classify(episode: dict[str, Any]) -> str:
    condition = episode["condition"]
    events = episode["events"]
    if condition == "no_elicitation":
        return "premature_closure"
    if condition == "oracle_profile":
        return "oracle_profile_control"
    if condition == "inferred_profile":
        return "unsupported_profile"
    if condition == "corrupted_profile":
        corrected = any(event.get("event_type") == "claim_revision" and event.get("respondent_disposition") == "corrected" for event in events)
        escalated = any(state.get("status") == "escalated" for state in episode["final_claim_states"].values())
        return "corruption_corrected_and_escalated" if corrected and escalated else "corruption_unresolved"
    if condition == "adaptive_probe" and any(event.get("respondent_disposition") == "corrected" for event in events):
        return "correction_applied"
    return "supported_required_claims"


def validate(fixture: Path = DEFAULT_FIXTURE, oracle_path: Path = DEFAULT_ORACLE, *, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(fixture.read_text())
    errors: list[str] = []
    if package.get("status") != "internal_calibration_only":
        errors.append("status must remain internal_calibration_only")
    if package.get("observer", {}).get("name") != "domain-neutral-objective-elicitation-observer-v1":
        errors.append("observer identity is not frozen")
    evaluator_inputs = package.get("observer", {}).get("evaluator_inputs", [])
    if any("oracle" in value or "private/" in value for value in evaluator_inputs):
        errors.append("private oracle leaked into evaluator inputs")
    if set(package.get("condition_matrix", [])) != REQUIRED_CONDITIONS:
        errors.append("condition matrix must contain exactly six frozen conditions")
    if set(package.get("claim_limits", {})) != REQUIRED_FALSE_CLAIMS or any(package.get("claim_limits", {}).values()):
        errors.append("synthetic package cannot promote human, expert, empirical, professional, or readiness claims")

    boundary_ref = package.get("canonical_provenance", {})
    boundary_path = ROOT / boundary_ref.get("path", "missing")
    if not boundary_path.is_file():
        errors.append("missing canonical provenance boundary")
    elif boundary_ref.get("sha256") != file_hash(boundary_path):
        errors.append("canonical provenance boundary hash mismatch")
    else:
        try:
            boundary_report = validate_record(
                json.loads(boundary_path.read_text()),
                expected_path=CANONICAL_PATH,
                expected_role=CANONICAL_ROLE,
            )
        except json.JSONDecodeError:
            errors.append("canonical provenance boundary is not valid JSON")
        else:
            errors.extend(f"canonical provenance: {error}" for error in boundary_report["errors"])

    packs_doc = _load_ref(package, "claim_packs", errors)
    objectives_doc = _load_ref(package, "objectives", errors)
    if any("truth" in item for pack in packs_doc.get("packs", []) for item in pack.get("claims", [])):
        errors.append("private claim truth leaked into observer claim packs")
    packs = {item["pack_id"]: item for item in packs_doc.get("packs", [])}
    objectives = {item["objective_id"]: item for item in objectives_doc.get("objectives", [])}
    if len(packs) < 2 or len({item.get("structure") for item in packs.values()}) < 2:
        errors.append("at least two structurally unlike claim packs are required")
    if not objectives_doc.get("frozen_before_episodes"):
        errors.append("objectives must be prospectively frozen")

    episodes = package.get("episodes", [])
    by_id = {episode.get("episode_id"): episode for episode in episodes}
    if not episodes or len(by_id) != len(episodes) or None in by_id:
        errors.append("episode ids must be unique and nonempty")
    for pack_id in packs:
        observed = {episode.get("condition") for episode in episodes if episode.get("pack_id") == pack_id}
        if observed != REQUIRED_CONDITIONS:
            errors.append(f"{pack_id}: all six matched conditions are required")

    resource_hash = None
    classifications = []
    question_counts = Counter()
    claim_counts = Counter()
    stop_counts = Counter()
    consequence_counts = Counter()
    burden_totals = Counter()

    for episode in episodes:
        eid = episode["episode_id"]
        pack = packs.get(episode.get("pack_id"))
        objective = objectives.get(episode.get("objective_id"))
        if not pack or not objective or objective.get("pack_id") != episode.get("pack_id"):
            errors.append(f"{eid}: pack/objective join is invalid")
            continue
        if episode.get("condition") not in REQUIRED_CONDITIONS:
            errors.append(f"{eid}: unknown condition")
        if episode.get("participant_realization") not in {"none", "scripted_simulator"}:
            errors.append(f"{eid}: simulator-to-human/expert promotion")
        if any(episode.get("claims", {}).get(key) for key in REQUIRED_FALSE_CLAIMS):
            errors.append(f"{eid}: simulator cannot promote human/expert or empirical claims")

        envelope = episode.get("resource_envelope")
        current_resource_hash = hashlib.sha256(json.dumps(envelope, sort_keys=True).encode()).hexdigest()
        resource_hash = resource_hash or current_resource_hash
        if current_resource_hash != resource_hash or envelope != package.get("resource_envelope"):
            errors.append(f"{eid}: unmatched downstream resources")

        criterion = objective.get("criterion", {})
        if not criterion.get("authored_before_conditions") or not criterion.get("intervention_blind"):
            errors.append(f"{eid}: criterion/intervention coupling")
        if episode.get("consequence", {}).get("criterion_id") != criterion.get("criterion_id"):
            errors.append(f"{eid}: consequence criterion drift")

        event_ids: set[str] = set()
        claim_events: dict[str, dict[str, Any]] = {}
        corrected_claims: set[str] = set()
        for event in episode.get("events", []):
            event_id = event.get("event_id")
            if not event_id or event_id in event_ids:
                errors.append(f"{eid}: event ids must be unique and nonempty")
            event_ids.add(event_id)
            if event.get("event_type") == "question":
                question_counts["opportunities"] += bool(event.get("opportunity"))
                question_counts["exposures"] += bool(event.get("exposed"))
                response = event.get("response")
                if response not in RESPONSES:
                    errors.append(f"{eid}: unsupported response class")
                else:
                    question_counts[response] += 1
                if response in {"answer", "refusal", "nonresponse"} and not event.get("exposed"):
                    errors.append(f"{eid}: answer/refusal/nonresponse without question exposure")
                if response in {"answer", "refusal", "nonresponse"} and not event.get("response_locator"):
                    errors.append(f"{eid}: realized response lacks exact locator")
            elif event.get("event_type") == "claim_revision":
                claim_id = event.get("claim_id")
                claim_counts[event.get("origin")] += 1
                if event.get("origin") not in ORIGINS:
                    errors.append(f"{eid}: unsupported claim origin")
                if event.get("origin") == "model_inferred" and event.get("status") == "confirmed":
                    errors.append(f"{eid}: unsupported profile promotion")
                if event.get("status") == "confirmed" and not event.get("evidence_locator"):
                    errors.append(f"{eid}: confirmed claim lacks exact locator")
                if event.get("unsupported_attribution") and event.get("status") == "confirmed":
                    errors.append(f"{eid}: unsupported attribution promoted to confirmed")
                if event.get("respondent_disposition") == "corrected":
                    corrected_claims.add(claim_id)
                claim_events[event_id] = event
            else:
                errors.append(f"{eid}: unknown event type")

        final = episode.get("final_claim_states", {})
        required = set(objective.get("required_claim_ids", []))
        if set(final) != required:
            errors.append(f"{eid}: every required claim needs one final state")
        terminal = 0
        confirmed = 0
        unsupported_final = set()
        for claim_id, state in final.items():
            source = claim_events.get(state.get("source_event_id"))
            if claim_id in corrected_claims and state.get("status") not in {"confirmed", "escalated"}:
                errors.append(f"{eid}: ignored correction for {claim_id}")
            if not source or source.get("claim_id") != claim_id or source.get("status") != state.get("status") or source.get("value") != state.get("value"):
                errors.append(f"{eid}: ignored correction or final claim/source mismatch for {claim_id}")
            terminal += state.get("status") in TERMINAL
            confirmed += state.get("status") == "confirmed"
            if state.get("status") == "inferred" or (source or {}).get("unsupported_attribution"):
                unsupported_final.add(claim_id)
        progress = episode.get("objective_progress", {})
        if progress != {"required_total": len(required), "required_terminal": terminal, "required_confirmed": confirmed}:
            errors.append(f"{eid}: objective progress does not replay from final claims")
        uptake = episode.get("semantic_uptake", {})
        expected_uptake = {cid for cid, state in final.items() if state.get("status") == "confirmed"}
        if set(uptake.get("claim_ids", [])) != expected_uptake or set(uptake.get("unsupported_claim_ids", [])) != unsupported_final:
            errors.append(f"{eid}: semantic uptake/unsupported attribution ledger mismatch")
        if episode.get("profile_fidelity", {}).get("supported") and unsupported_final:
            errors.append(f"{eid}: profile fidelity inferred from artifact success despite unsupported claims")

        stop = episode.get("stop", {}).get("classification")
        stop_counts[stop] += 1
        if stop == "sufficient_completion" and terminal < len(required):
            errors.append(f"{eid}: premature closure mislabeled sufficient")
        if stop == "justified_escalation" and not any(state.get("status") == "escalated" for state in final.values()):
            errors.append(f"{eid}: escalation stop lacks escalated required claim")
        if stop == "premature_closure" and terminal == len(required):
            errors.append(f"{eid}: premature-closure label conflicts with terminal inventory")

        burden = episode.get("burden", {})
        budget = objective.get("burden_budget", {})
        if any(not isinstance(burden.get(key), int) or burden.get(key) < 0 for key in ("questions", "active_seconds", "corrections")):
            errors.append(f"{eid}: burden fields must be nonnegative integers")
        if any(burden.get(key, 0) > budget.get(key, -1) for key in ("questions", "active_seconds", "corrections")):
            errors.append(f"{eid}: excess burden")
        actual_questions = sum(event.get("event_type") == "question" and event.get("exposed") for event in episode.get("events", []))
        if burden.get("questions") != actual_questions:
            errors.append(f"{eid}: question burden does not equal realized exposure")
        burden_totals.update(burden)
        consequence_counts["success" if episode.get("consequence", {}).get("success") else "not_success"] += 1
        classifications.append({"episode_id": eid, "pack_id": episode["pack_id"], "condition": episode["condition"], "classification": classify(episode)})

    # Only now compare public-record classifications with the unavailable oracle.
    oracle = json.loads(oracle_path.read_text())
    if package.get("private_oracle", {}).get("path") != str(oracle_path.relative_to(ROOT)) or package.get("private_oracle", {}).get("sha256") != file_hash(oracle_path):
        errors.append("private oracle path/hash mismatch")
    if not oracle.get("not_evaluator_input"):
        errors.append("oracle must declare that it is not evaluator input")
    expected = {item["episode_id"]: item for item in oracle.get("episodes", [])}
    if set(expected) != set(by_id):
        errors.append("oracle and episode inventories differ")
    for row in classifications:
        oracle_row = expected.get(row["episode_id"], {})
        if row["classification"] != oracle_row.get("expected_classification"):
            errors.append(f"{row['episode_id']}: classification differs from frozen oracle")
        observed_final = {cid: {"status": state["status"], "value": state["value"]} for cid, state in by_id[row["episode_id"]]["final_claim_states"].items()}
        if observed_final != oracle_row.get("expected_final"):
            errors.append(f"{row['episode_id']}: final claim states differ from frozen oracle")

    if check_paths:
        for item in package.get("provenance", []):
            path = ROOT / item.get("path", "missing")
            if not path.is_file():
                errors.append(f"missing provenance path: {item.get('path')}")
            elif item.get("sha256") != file_hash(path):
                errors.append(f"provenance hash mismatch: {item.get('path')}")

    denominators = {
        "episodes": {"all": len(episodes), "by_condition": dict(sorted(Counter(item.get("condition") for item in episodes).items()))},
        "questions": dict(sorted(question_counts.items())),
        "claim_origins": dict(sorted(claim_counts.items())),
        "objective": {"required_claim_slots": sum(item.get("objective_progress", {}).get("required_total", 0) for item in episodes), "required_terminal": sum(item.get("objective_progress", {}).get("required_terminal", 0) for item in episodes), "required_confirmed": sum(item.get("objective_progress", {}).get("required_confirmed", 0) for item in episodes)},
        "profile": {"supported": sum(item.get("profile_fidelity", {}).get("supported", False) for item in episodes), "unsupported_attribution_episodes": sum(bool(item.get("semantic_uptake", {}).get("unsupported_claim_ids")) for item in episodes)},
        "consequence": dict(sorted(consequence_counts.items())),
        "stop": dict(sorted(stop_counts.items())),
        "burden": dict(sorted(burden_totals.items())),
    }
    return {"valid": not errors, "classifications": classifications, "denominators": denominators, "errors": errors, "fixture_sha256": file_hash(fixture), "oracle_sha256": file_hash(oracle_path)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--oracle", type=Path, default=DEFAULT_ORACLE)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate(args.fixture, args.oracle, check_paths=args.check_paths)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered)
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
