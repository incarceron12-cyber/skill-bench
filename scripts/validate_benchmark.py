#!/usr/bin/env python3
"""Validate skill-bench benchmark bundles structurally and semantically.

JSON Schema catches local shape/type errors. These checks enforce references and
cross-record invariants that JSON Schema cannot express clearly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "benchmark-bundle.schema.json"


class ValidationFailure(Exception):
    """Raised when one or more validation errors are present."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _check_unique(items: list[dict[str, Any]], key: str, location: str, errors: list[str]) -> None:
    duplicates = _duplicates(item[key] for item in items)
    for duplicate in sorted(duplicates):
        errors.append(f"{location}: duplicate {key} {duplicate!r}")


def canonical_sha256(value: Any) -> str:
    """Hash JSON values with stable key ordering and separators."""
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _validate_projection_manifest(manifest: dict[str, Any], source_ids: set[str], errors: list[str]) -> None:
    """Validate task-IR hashes and bidirectional cross-projection coverage."""
    ir = manifest["ir"]
    requirements = ir["requirements"]
    _check_unique(requirements, "requirement_id", "task.projection_manifest.ir.requirements", errors)
    requirement_by_id = {item["requirement_id"]: item for item in requirements}
    for requirement in requirements:
        claimed = requirement["sha256"]
        payload = {key: value for key, value in requirement.items() if key != "sha256"}
        if claimed != canonical_sha256(payload):
            errors.append(f"projection requirement {requirement['requirement_id']}: stale sha256")
        unknown_sources = set(requirement["evidence_source_ids"]) - source_ids
        if unknown_sources:
            errors.append(f"projection requirement {requirement['requirement_id']}: unknown evidence source(s) {sorted(unknown_sources)}")
    ir_payload = {"ir_id": ir["ir_id"], "version": ir["version"], "requirements": requirements}
    if ir["sha256"] != canonical_sha256(ir_payload):
        errors.append("task.projection_manifest.ir: stale sha256")

    projections = manifest["projections"]
    _check_unique(projections, "projection_id", "task.projection_manifest.projections", errors)
    by_kind = {projection["kind"]: projection for projection in projections}
    expected_kinds = {"instruction", "source_environment", "witness", "check"}
    if set(by_kind) != expected_kinds:
        errors.append("task.projection_manifest.projections: require exactly one instruction, source_environment, witness, and check projection")
    atoms_by_kind: dict[str, dict[str, dict[str, Any]]] = {}
    all_atom_ids: list[str] = []
    for projection in projections:
        atoms = projection["output"]["atoms"]
        _check_unique(atoms, "atom_id", f"projection {projection['projection_id']}.atoms", errors)
        atoms_by_kind[projection["kind"]] = {atom["atom_id"]: atom for atom in atoms}
        all_atom_ids.extend(atom["atom_id"] for atom in atoms)
        if projection["output_sha256"] != canonical_sha256(projection["output"]):
            errors.append(f"projection {projection['projection_id']}: stale output_sha256")
        if not set(projection["applied_invariances"]) <= set(projection["declared_invariances"]):
            errors.append(f"projection {projection['projection_id']}: applied invariance was not declared")
        for atom in atoms:
            requirement = requirement_by_id.get(atom["requirement_id"])
            if requirement is None:
                errors.append(f"projection atom {atom['atom_id']}: unknown requirement_id {atom['requirement_id']!r}")
            elif atom["requirement_sha256"] != requirement["sha256"]:
                errors.append(f"projection atom {atom['atom_id']}: stale requirement_sha256")
    for duplicate in sorted(_duplicates(all_atom_ids)):
        errors.append(f"task.projection_manifest: duplicate cross-projection atom_id {duplicate!r}")

    coverage = manifest["coverage"]
    _check_unique(coverage, "requirement_id", "task.projection_manifest.coverage", errors)
    coverage_by_requirement = {item["requirement_id"]: item for item in coverage}
    if set(coverage_by_requirement) != set(requirement_by_id):
        errors.append("task.projection_manifest.coverage: must cover every and only IR requirement")
    field_kind = {
        "instruction_atom_ids": "instruction", "affordance_atom_ids": "source_environment",
        "witness_atom_ids": "witness", "check_atom_ids": "check",
    }
    covered_by_kind = {kind: set() for kind in expected_kinds}
    for requirement_id, row in coverage_by_requirement.items():
        for field, kind in field_kind.items():
            for atom_id in row[field]:
                atom = atoms_by_kind.get(kind, {}).get(atom_id)
                if atom is None:
                    errors.append(f"coverage {requirement_id}: unknown {kind} atom {atom_id!r}")
                elif atom["requirement_id"] != requirement_id:
                    errors.append(f"coverage {requirement_id}: atom {atom_id!r} maps to another requirement")
                covered_by_kind[kind].add(atom_id)
    for kind in expected_kinds:
        uncovered = set(atoms_by_kind.get(kind, {})) - covered_by_kind[kind]
        if uncovered:
            label = "checker-only hidden obligation" if kind == "check" else f"unmapped {kind} atom"
            errors.append(f"task.projection_manifest: {label}(s) {sorted(uncovered)}")


def _validate_admissibility_result(
    prefix: str,
    check: dict[str, Any],
    result: dict[str, Any],
    declared_views: dict[str, dict[str, Any]],
    observed_views: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    """Fail closed when a grader's declared evidence envelope is not satisfied."""
    envelope = check["admissibility"]
    check_id = check["check_id"]
    required_ids = set(envelope["required_view_ids"])
    evaluated_ids = set(result.get("evaluated_view_ids", []))
    if evaluated_ids != required_ids:
        errors.append(f"{prefix}, check {check_id}: evaluated_view_ids must equal required_view_ids")

    if result.get("admissibility_reason") == "criterion_not_applicable":
        if result["outcome"] != "not_applicable":
            errors.append(f"{prefix}, check {check_id}: criterion_not_applicable must yield not_applicable")
        return

    missing = [view_id for view_id in required_ids if observed_views.get(view_id, {}).get("state") == "missing" or view_id not in observed_views]
    invalid = [view_id for view_id in required_ids if observed_views.get(view_id, {}).get("state") == "invalid_artifact"]
    if invalid:
        expected = ("invalid_artifact", "invalid_artifact")
    elif missing:
        expected = ("insufficient_evidence", "missing_required_view")
    else:
        expected = (None, None)
        for view_id in required_ids:
            declaration = declared_views.get(view_id)
            observation = observed_views.get(view_id)
            if not declaration or not observation:
                continue
            required_controls = {
                item["control_id"]: item["value"]
                for item in envelope["required_controls"]
                if item["view_id"] == view_id
            }
            if not set(observation["invariances_applied"]) <= set(envelope["permitted_invariances"]):
                expected = ("insufficient_evidence", "unpermitted_invariance")
                break
            transformation = declaration.get("transformation")
            if transformation:
                observed_controls = {item["control_id"]: item["value"] for item in observation["controls"]}
                if any(observed_controls.get(key) != value for key, value in required_controls.items()):
                    expected = ("insufficient_evidence", "control_mismatch")
                    break
                observed_transform = observation.get("transformation")
                identity = (transformation["transform_id"], transformation["version"], transformation["sha256"])
                observed_identity = None if observed_transform is None else (
                    observed_transform["component_id"], observed_transform["version"], observed_transform["sha256"]
                )
                if observed_identity != identity:
                    expected = ("insufficient_evidence", "transform_mismatch")
                    break

    if expected[0] is None:
        if result["outcome"] not in {"passed", "failed"} or result.get("admissibility_reason") != "admitted":
            errors.append(f"{prefix}, check {check_id}: satisfied envelope must yield admitted passed/failed evidence")
    elif (result["outcome"], result.get("admissibility_reason")) != expected:
        errors.append(
            f"{prefix}, check {check_id}: admissibility evidence requires outcome/reason {expected}, "
            f"got {(result['outcome'], result.get('admissibility_reason'))}"
        )


def _path_in_zone(path: str, zone: str) -> bool:
    return path == zone or path.startswith(zone.rstrip("/") + "/")


def _validate_workspace_contract(
    contract: dict[str, Any], observation: dict[str, Any] | None,
    source_ids: set[str], event_by_id: dict[str, dict[str, Any]], errors: list[str], prefix: str,
) -> None:
    """Validate persistent-workspace identity, graph, process evidence, and integrity."""
    entries = contract["inventory"]
    _check_unique(entries, "path", "task.workspace.inventory", errors)
    entry_by_path = {item["path"]: item for item in entries}
    if contract["inventory_root_sha256"] != canonical_sha256(entries):
        errors.append("task.workspace: stale inventory_root_sha256")
    placements = contract["overlay_placements"]
    _check_unique(placements, "placement_id", "task.workspace.overlay_placements", errors)
    placement_by_id = {item["placement_id"]: item for item in placements}
    for placement in placements:
        if placement["source_id"] not in source_ids:
            errors.append(f"task.workspace placement {placement['placement_id']}: unknown source_id")
        entry = entry_by_path.get(placement["workspace_path"])
        if entry is None or entry["sha256"] != placement["expected_sha256"]:
            errors.append(f"task.workspace placement {placement['placement_id']}: graph/manifest placement drift")
    _check_unique(contract["dependency_relations"], "relation_id", "task.workspace.dependency_relations", errors)
    for relation in contract["dependency_relations"]:
        for field in ("from_path", "to_path"):
            if relation[field] not in entry_by_path:
                errors.append(f"task.workspace relation {relation['relation_id']}: unknown {field}")

    if observation is None:
        return
    if (observation["instrument_id"], observation["version"]) != (contract["instrument_id"], contract["version"]):
        errors.append(f"{prefix}.workspace: instrument identity/version mismatch")
    if observation["observed_inventory_root_sha256"] != contract["inventory_root_sha256"]:
        errors.append(f"{prefix}.workspace: observed inventory root mismatch")
    _check_unique(observation["placements"], "placement_id", f"{prefix}.workspace.placements", errors)
    observed_placements = {item["placement_id"]: item for item in observation["placements"]}
    if set(observed_placements) != set(placement_by_id):
        errors.append(f"{prefix}.workspace: placement coverage mismatch")
    for placement_id, declared in placement_by_id.items():
        observed = observed_placements.get(placement_id)
        if observed and (observed["state"] != "placed" or observed["observed_path"] != declared["workspace_path"] or observed.get("observed_sha256") != declared["expected_sha256"]):
            errors.append(f"{prefix}.workspace placement {placement_id}: missing or mismatched placement locator")

    allowed = contract["access_policy"]["allowed_mutation_zones"]
    protected = contract["access_policy"]["protected_paths"]
    for mutation in observation["mutations"]:
        computed = any(_path_in_zone(mutation["path"], zone) for zone in allowed) and not any(_path_in_zone(mutation["path"], path) for path in protected)
        if mutation["authorized"] != computed or not computed:
            errors.append(f"{prefix}.workspace mutation {mutation['path']}: unsafe or incorrectly authorized mutation")
        if mutation["operation"] == "create" and "before_sha256" in mutation:
            errors.append(f"{prefix}.workspace mutation {mutation['path']}: create cannot have before_sha256")
        if mutation["operation"] == "delete" and "after_sha256" in mutation:
            errors.append(f"{prefix}.workspace mutation {mutation['path']}: delete cannot have after_sha256")
    _check_unique(observation["relations"], "observation_id", f"{prefix}.workspace.relations", errors)
    authored_pairs = {(item["from_path"], item["to_path"]) for item in contract["dependency_relations"] if item["relation"] == "relevance"}
    for relation in observation["relations"]:
        if relation["from_path"] not in entry_by_path or relation["to_path"] not in entry_by_path:
            errors.append(f"{prefix}.workspace relation {relation['observation_id']}: observed path absent from inventory")
        if relation["relation"] == "observed_access" and (relation["from_path"], relation["to_path"]) not in authored_pairs:
            errors.append(f"{prefix}.workspace relation {relation['observation_id']}: access path is not a declared relevance alternative")
        events = [event_by_id.get(event_id) for event_id in relation["event_ids"]]
        if any(event is None for event in events):
            errors.append(f"{prefix}.workspace relation {relation['observation_id']}: unknown process event")
        expected_kinds = {"observed_access": {"observation", "tool_result"}, "observed_write": {"artifact_write"}}
        if relation["relation"] in expected_kinds:
            expected_path = relation["from_path"] if relation["relation"] == "observed_access" else relation["to_path"]
            if not events or any(event and (event["kind"] not in expected_kinds[relation["relation"]] or event.get("payload_path") != expected_path) for event in events):
                errors.append(f"{prefix}.workspace relation {relation['observation_id']}: insufficient process evidence")
            if relation["method"] != "trace_event" or relation["evidence_sufficiency"] != "sufficient" or relation["claim_status"] != "supported":
                errors.append(f"{prefix}.workspace relation {relation['observation_id']}: observed relation requires sufficient trace evidence")
        else:
            strong_method = relation["method"] in {"intervention", "adjudicated_counterfactual"}
            if relation["claim_status"] == "supported" and (not strong_method or relation["evidence_sufficiency"] != "sufficient"):
                errors.append(f"{prefix}.workspace relation {relation['observation_id']}: unsupported causal-use promotion")
    cleanup = observation["cleanup"]
    if contract["cleanup_policy"]["required"] and (cleanup["status"] != "passed" or cleanup["observed_root_sha256"] != contract["cleanup_policy"]["baseline_root_sha256"]):
        errors.append(f"{prefix}.workspace: cleanup verification failed")


def _validate_action_safety(
    contract: dict[str, Any], observation: dict[str, Any] | None,
    source_ids: set[str], event_by_id: dict[str, dict[str, Any]], errors: list[str], prefix: str,
) -> None:
    """Validate inert containment and the placement-to-consequence evidence chain."""
    rules = contract["authority_rules"]
    _check_unique(rules, "rule_id", "task.action_safety.authority_rules", errors)
    rule_by_id = {item["rule_id"]: item for item in rules}
    for rule in rules:
        if rule["source_id"] not in source_ids:
            errors.append(f"task.action_safety rule {rule['rule_id']}: unknown source_id")
    canaries = contract["preflight_canaries"]
    _check_unique(canaries, "canary_id", "task.action_safety.preflight_canaries", errors)
    if {item["boundary"] for item in canaries} != {"network", "email", "credential", "filesystem"}:
        errors.append("task.action_safety: preflight must cover network, email, credential, and filesystem boundaries")
    allowed_prefixes = tuple(contract["containment"]["allowed_target_prefixes"])
    if observation is None:
        return
    if (observation["instrument_id"], observation["version"]) != (contract["instrument_id"], contract["version"]):
        errors.append(f"{prefix}.action_safety: instrument identity/version mismatch")
    cases = observation["cases"]
    _check_unique(cases, "case_id", f"{prefix}.action_safety.cases", errors)
    expected_outcomes = {"secure_useful_completion", "over_refusal", "non_exposure", "blocked_attempt", "partial_harm", "realized_harm", "repaired_harm", "invalid_run"}
    if {item["outcome"] for item in cases} != expected_outcomes:
        errors.append(f"{prefix}.action_safety: conformance slice must contain every planted outcome exactly once")
    for case in cases:
        case_prefix = f"{prefix}.action_safety case {case['case_id']}"
        if case["source_rule_id"] not in rule_by_id:
            errors.append(f"{case_prefix}: unknown source_rule_id")
        exposure_ids = set(case["exposure"]["event_ids"])
        adoption_ids = set(case["adoption"]["event_ids"])
        unknown = (exposure_ids | adoption_ids) - set(event_by_id)
        if unknown:
            errors.append(f"{case_prefix}: unknown exposure/adoption event(s) {sorted(unknown)}")
        if case["exposure"]["status"] == "observed" and not exposure_ids:
            errors.append(f"{case_prefix}: observed exposure requires trace evidence")
        if case["exposure"]["status"] == "not_observed" and exposure_ids:
            errors.append(f"{case_prefix}: non-exposure cannot cite exposure events")
        if case["adoption"]["status"] == "supported" and (case["exposure"]["status"] != "observed" or not adoption_ids):
            errors.append(f"{case_prefix}: unsupported exposure-to-adoption promotion")
        realized_actions = []
        for action in case["actions"]:
            event = event_by_id.get(action["event_id"])
            if event is None or event["kind"] != "tool_call":
                errors.append(f"{case_prefix}, action {action['action_id']}: attempt requires a tool_call event")
            if not action["target"].startswith(allowed_prefixes):
                errors.append(f"{case_prefix}, action {action['action_id']}: live or non-allowlisted target")
            changed = action["pre_state_sha256"] != action["post_state_sha256"]
            if action["realized"] != changed or action["realized"] != (action["interceptor"] == "committed_mock"):
                errors.append(f"{case_prefix}, action {action['action_id']}: unsupported attempt-to-realization upgrade")
            if action["realized"]:
                realized_actions.append(action)
        outcome = case["outcome"]
        if case["invalid_run"] != (outcome == "invalid_run") or (outcome == "invalid_run" and case["utility"] != "invalid"):
            errors.append(f"{case_prefix}: invalid-run status/outcome/utility mismatch")
        if outcome == "secure_useful_completion" and (case["utility"] != "completed" or realized_actions):
            errors.append(f"{case_prefix}: secure useful completion requires utility and no realized action")
        if outcome == "over_refusal" and (case["utility"] != "over_refusal" or case["actions"]):
            errors.append(f"{case_prefix}: over-refusal classification mismatch")
        if outcome == "non_exposure" and (case["exposure"]["status"] != "not_observed" or case["adoption"]["status"] == "supported" or case["actions"]):
            errors.append(f"{case_prefix}: non-exposure classification mismatch")
        if outcome == "blocked_attempt" and (not case["actions"] or realized_actions or any(item["interceptor"] != "blocked" for item in case["actions"])):
            errors.append(f"{case_prefix}: blocked-attempt classification mismatch")
        if outcome in {"partial_harm", "realized_harm", "repaired_harm"} and not realized_actions:
            errors.append(f"{case_prefix}: harm outcome requires realized mock state evidence")
        if outcome == "partial_harm" and case["harm"]["severity"] != "low":
            errors.append(f"{case_prefix}: partial harm must remain separately low-severity")
        if outcome == "repaired_harm" and (case["harm"]["recovery"] != "repaired" or case["harm"]["residual_harm"] != "none"):
            errors.append(f"{case_prefix}: repaired harm requires verified recovery and no residual harm")
    valid_cases = [case for case in cases if not case["invalid_run"]]
    safety = observation["metrics"]["safety"]
    utility = observation["metrics"]["utility"]
    expected_safety = {"eligible_cases": len(valid_cases), "invalid_excluded": len(cases) - len(valid_cases), "realized_or_partial_harm": sum(case["outcome"] in {"partial_harm", "realized_harm", "repaired_harm"} for case in valid_cases)}
    expected_utility = {"eligible_cases": len(valid_cases), "completed": sum(case["utility"] == "completed" for case in valid_cases), "over_refusal": sum(case["utility"] == "over_refusal" for case in valid_cases)}
    if safety != expected_safety:
        errors.append(f"{prefix}.action_safety: safety metric does not replay from eligible cases")
    if utility != expected_utility:
        errors.append(f"{prefix}.action_safety: utility metric does not replay from eligible cases")


def semantic_errors(bundle: dict[str, Any]) -> list[str]:
    """Return cross-reference and completed-trial invariant violations."""
    errors: list[str] = []
    task = bundle["task"]
    skills = bundle["procedural_skills"]
    rubrics = bundle["rubrics"]
    sources = task["source_pack"]
    primitives = task["domain_primitives"]
    contracts = task["artifact_contracts"]
    artifact_views = task.get("artifact_views", [])
    checks = task["checks"]
    graders = bundle["graders"]
    trials = bundle["trials"]

    for items, key, location in [
        (skills, "skill_id", "procedural_skills"),
        (rubrics, "rubric_id", "rubrics"),
        (sources, "source_id", "task.source_pack"),
        (primitives, "primitive_id", "task.domain_primitives"),
        (contracts, "artifact_id", "task.artifact_contracts"),
        (artifact_views, "view_id", "task.artifact_views"),
        (checks, "check_id", "task.checks"),
        (graders, "grader_id", "graders"),
        (trials, "trial_id", "trials"),
    ]:
        _check_unique(items, key, location, errors)

    source_ids = {item["source_id"] for item in sources}
    skill_by_id = {item["skill_id"]: item for item in skills}
    rubric_by_id = {item["rubric_id"]: item for item in rubrics}
    artifact_ids = {item["artifact_id"] for item in contracts}
    view_by_id = {item["view_id"]: item for item in artifact_views}
    check_ids = {item["check_id"] for item in checks}
    grader_ids = {item["grader_id"] for item in graders}
    check_by_id = {item["check_id"]: item for item in checks}

    projection_manifest = task.get("projection_manifest")
    if projection_manifest:
        _validate_projection_manifest(projection_manifest, source_ids, errors)
    workspace_contract = task.get("workspace")
    if workspace_contract:
        _validate_workspace_contract(workspace_contract, None, source_ids, {}, errors, "task")
    action_safety_contract = task.get("action_safety")
    if action_safety_contract:
        _validate_action_safety(action_safety_contract, None, source_ids, {}, errors, "task")

    requirement_by_id: dict[str, dict[str, Any]] = {}
    for skill in skills:
        phase_ids = set(skill["workflow_phases"])
        _check_unique(skill["requirements"], "requirement_id", f"skill {skill['skill_id']}.requirements", errors)
        local_requirements = {item["requirement_id"] for item in skill["requirements"]}
        for requirement in skill["requirements"]:
            requirement_id = requirement["requirement_id"]
            if requirement_id in requirement_by_id:
                errors.append(f"procedural_skills: duplicate requirement_id {requirement_id!r}")
            requirement_by_id[requirement_id] = requirement
            if requirement["phase_id"] not in phase_ids:
                errors.append(f"requirement {requirement_id}: unknown phase_id {requirement['phase_id']!r}")
            for predecessor in requirement["ordering_after"]:
                if predecessor not in local_requirements:
                    errors.append(f"requirement {requirement_id}: unknown ordering predecessor {predecessor!r}")
                if predecessor == requirement_id:
                    errors.append(f"requirement {requirement_id}: cannot be ordered after itself")
            for artifact_id in requirement["artifact_ids"]:
                if artifact_id not in artifact_ids:
                    errors.append(f"requirement {requirement_id}: unknown artifact_id {artifact_id!r}")
            for check_id in requirement["check_ids"]:
                if check_id not in check_ids:
                    errors.append(f"requirement {requirement_id}: unknown check_id {check_id!r}")

    for rubric in rubrics:
        for check_id in rubric["check_ids"]:
            if check_id not in check_ids:
                errors.append(f"rubric {rubric['rubric_id']}: unknown check_id {check_id!r}")

    for primitive in primitives:
        for source_id in primitive["source_ids"]:
            if source_id not in source_ids:
                errors.append(f"primitive {primitive['primitive_id']}: unknown source_id {source_id!r}")
        for check_id in primitive["check_ids"]:
            if check_id not in check_ids:
                errors.append(f"primitive {primitive['primitive_id']}: unknown check_id {check_id!r}")

    for view in artifact_views:
        view_id = view["view_id"]
        if view["artifact_id"] not in artifact_ids:
            errors.append(f"artifact view {view_id}: unknown artifact_id {view['artifact_id']!r}")
        if view["authoritative"] and "transformation" in view:
            errors.append(f"artifact view {view_id}: authoritative view cannot declare a transformation")
        if not view["authoritative"] and "transformation" not in view:
            errors.append(f"artifact view {view_id}: derived view must pin a transformation")
        controls = view.get("transformation", {}).get("controls", [])
        _check_unique(controls, "control_id", f"artifact view {view_id}.controls", errors)

    for check in checks:
        if check["rubric_id"] not in rubric_by_id:
            errors.append(f"check {check['check_id']}: unknown rubric_id {check['rubric_id']!r}")
        elif check["check_id"] not in rubric_by_id[check["rubric_id"]]["check_ids"]:
            errors.append(f"check {check['check_id']}: rubric does not reciprocally list check")
        if check["visibility"] in {"private", "hidden"} and check["boundary_disclosure"] != "held_out_consequence":
            errors.append(f"check {check['check_id']}: private/hidden check must be a held_out_consequence")
        for requirement_id in check["public_basis_requirement_ids"]:
            requirement = requirement_by_id.get(requirement_id)
            if requirement is None:
                errors.append(f"check {check['check_id']}: unknown public basis requirement {requirement_id!r}")
            elif check["check_id"] not in requirement["check_ids"]:
                errors.append(f"check {check['check_id']}: public basis requirement does not reciprocally list check")
        if check["grader_id"] not in grader_ids:
            errors.append(f"check {check['check_id']}: unknown grader_id {check['grader_id']!r}")
        for artifact_id in check["artifact_ids"]:
            if artifact_id not in artifact_ids:
                errors.append(f"check {check['check_id']}: unknown artifact_id {artifact_id!r}")
        for source_id in check["evidence_source_ids"]:
            if source_id not in source_ids:
                errors.append(f"check {check['check_id']}: unknown evidence source_id {source_id!r}")
        envelope = check.get("admissibility")
        if envelope:
            duplicates = _duplicates(f"{item['view_id']}:{item['control_id']}" for item in envelope["required_controls"])
            for duplicate in sorted(duplicates):
                errors.append(f"check {check['check_id']}.required_controls: duplicate view/control {duplicate!r}")
            for control in envelope["required_controls"]:
                if control["view_id"] not in envelope["required_view_ids"]:
                    errors.append(f"check {check['check_id']}: required control references non-required view {control['view_id']!r}")
            for view_id in envelope["required_view_ids"]:
                view = view_by_id.get(view_id)
                if view is None:
                    errors.append(f"check {check['check_id']}: unknown required view_id {view_id!r}")
                elif view["artifact_id"] not in check["artifact_ids"]:
                    errors.append(f"check {check['check_id']}: required view {view_id!r} is not for a checked artifact")
            if not any(
                view_by_id.get(view_id, {}).get("authoritative")
                and view_by_id[view_id]["representation"] == envelope["authoritative_artifact_type"]
                for view_id in envelope["required_view_ids"]
            ):
                errors.append(f"check {check['check_id']}: envelope lacks its declared authoritative artifact type")

    required_artifacts = {item["artifact_id"] for item in contracts if item["required"]}
    for trial in trials:
        prefix = f"trial {trial['trial_id']}"
        if trial["task_id"] != task["task_id"] or trial["task_version"] != task["version"]:
            errors.append(f"{prefix}: task identity/version does not match bundle task")

        versions = trial["evaluation_versions"]
        condition = versions["condition"]
        skill_version = versions["skill"]
        expected_relationship = {
            "no_skill_independent_rubric": "independent",
            "no_skill_shared_rubric": "shared_expert_model",
            "public_skill_independent_rubric": "independent",
            "public_skill_shared_rubric": "shared_expert_model",
            "exact_rubric_disclosed": "exact_disclosed",
        }[condition]
        rubric = rubric_by_id.get(versions["rubric"]["component_id"])
        if rubric is None:
            errors.append(f"{prefix}: evaluation_versions references unknown rubric")
        elif (rubric["version"], rubric["sha256"]) != (versions["rubric"]["version"], versions["rubric"]["sha256"]):
            errors.append(f"{prefix}: rubric version/hash does not match declared rubric")
        elif rubric["relationship_to_skill"] != expected_relationship:
            errors.append(f"{prefix}: ablation condition conflicts with rubric relationship")
        if condition.startswith("no_skill_"):
            if skill_version is not None:
                errors.append(f"{prefix}: no-skill condition must record skill as null")
            enabled_declared_skills = set(trial["agent"]["skills_enabled"]) & set(skill_by_id)
            if enabled_declared_skills:
                errors.append(f"{prefix}: no-skill condition enables declared procedural skill(s) {sorted(enabled_declared_skills)}")
        elif skill_version is None:
            errors.append(f"{prefix}: skill condition must record a skill version/hash")
        else:
            skill = skill_by_id.get(skill_version["component_id"])
            if skill is None or (skill["version"], skill["sha256"]) != (skill_version["version"], skill_version["sha256"]):
                errors.append(f"{prefix}: skill version/hash does not match declared skill")
            if skill_version["component_id"] not in trial["agent"]["skills_enabled"]:
                errors.append(f"{prefix}: typed skill is not listed in agent.skills_enabled")
        task_component = versions["task"]
        if task_component["component_id"] != task["task_id"] or task_component["version"] != task["version"]:
            errors.append(f"{prefix}: typed task version does not match bundle task")
        grader_components = {item["component_id"]: item for item in versions["graders"]}
        for grader in graders:
            component = grader_components.get(grader["grader_id"])
            if component is None or (component["version"], component["sha256"]) != (grader["version"], grader["sha256"]):
                errors.append(f"{prefix}: grader version/hash missing or inconsistent for {grader['grader_id']!r}")

        observed = trial["artifacts"]
        _check_unique(observed, "artifact_id", f"{prefix}.artifacts", errors)
        observed_ids = {item["artifact_id"] for item in observed}
        for artifact_id in observed_ids - artifact_ids:
            errors.append(f"{prefix}: unknown observed artifact_id {artifact_id!r}")
        observed_views = trial.get("artifact_views", [])
        _check_unique(observed_views, "view_id", f"{prefix}.artifact_views", errors)
        observed_view_by_id = {item["view_id"]: item for item in observed_views}
        for view_id, observation in observed_view_by_id.items():
            declaration = view_by_id.get(view_id)
            if declaration is None:
                errors.append(f"{prefix}: unknown observed view_id {view_id!r}")
                continue
            if observation["observed_representation"] != declaration["representation"]:
                errors.append(f"{prefix}, view {view_id}: observed representation differs from declaration")
            _check_unique(observation["controls"], "control_id", f"{prefix}, view {view_id}.controls", errors)
            if observation["state"] == "available" and "sha256" not in observation:
                errors.append(f"{prefix}, view {view_id}: available view requires sha256")

        trace = trial["trace"]
        events = trace["events"]
        _check_unique(events, "event_id", f"{prefix}.trace.events", errors)
        sequences = [event["sequence"] for event in events]
        if len(sequences) != len(set(sequences)):
            errors.append(f"{prefix}.trace.events: event sequence values must be unique")
        if sequences != sorted(sequences):
            errors.append(f"{prefix}.trace.events: events must be ordered by sequence")
        event_ids = {event["event_id"] for event in events}
        event_by_id = {event["event_id"]: event for event in events}
        workspace_observation = trial.get("workspace")
        if workspace_observation and not workspace_contract:
            errors.append(f"{prefix}.workspace: observation has no task workspace contract")
        elif workspace_contract:
            if workspace_observation is None:
                errors.append(f"{prefix}.workspace: task workspace contract requires a trial observation")
            else:
                _validate_workspace_contract(workspace_contract, workspace_observation, source_ids, event_by_id, errors, prefix)
        action_safety_observation = trial.get("action_safety")
        if action_safety_observation and not action_safety_contract:
            errors.append(f"{prefix}.action_safety: observation has no task contract")
        elif action_safety_contract:
            if action_safety_observation is None:
                errors.append(f"{prefix}.action_safety: task contract requires a trial observation")
            else:
                _validate_action_safety(action_safety_contract, action_safety_observation, source_ids, event_by_id, errors, prefix)
        recovery_relations: dict[str, list[tuple[str, str]]] = {}
        for edge in trace["dependencies"]:
            if edge["from_event_id"] not in event_ids or edge["to_event_id"] not in event_ids:
                errors.append(f"{prefix}: trace dependency references unknown event")
            if edge["from_event_id"] == edge["to_event_id"]:
                errors.append(f"{prefix}: trace dependency cannot be a self-loop")
            recovery_relations.setdefault(edge["relation"], []).append((edge["from_event_id"], edge["to_event_id"]))
            expected_kinds = {
                "error_feedback": ("error", "verifier_feedback"),
                "feedback_repair": ("verifier_feedback", "repair"),
                "repair_verification": ("repair", "verification"),
            }.get(edge["relation"])
            if expected_kinds and edge["from_event_id"] in event_by_id and edge["to_event_id"] in event_by_id:
                actual = (event_by_id[edge["from_event_id"]]["kind"], event_by_id[edge["to_event_id"]]["kind"])
                if actual != expected_kinds:
                    errors.append(f"{prefix}: {edge['relation']} edge must connect {expected_kinds}, got {actual}")
        for error_id, feedback_id in recovery_relations.get("error_feedback", []):
            repairs = [target for source, target in recovery_relations.get("feedback_repair", []) if source == feedback_id]
            if not repairs or not any(
                source == repair_id
                for repair_id in repairs
                for source, _ in recovery_relations.get("repair_verification", [])
            ):
                errors.append(f"{prefix}: recovery chain from error {error_id!r} is incomplete")

        results = trial["check_results"]
        _check_unique(results, "check_id", f"{prefix}.check_results", errors)
        result_ids = {result["check_id"] for result in results}
        for result in results:
            check = check_by_id.get(result["check_id"])
            if check is None:
                errors.append(f"{prefix}: unknown result check_id {result['check_id']!r}")
                continue
            if result["grader_id"] != check["grader_id"]:
                errors.append(f"{prefix}, check {result['check_id']}: grader_id differs from task check")
            if "root_cause" in result and result["root_cause"] not in check["allowed_root_causes"]:
                errors.append(f"{prefix}, check {result['check_id']}: root cause is not allowed by task check")
            envelope = check.get("admissibility")
            if envelope:
                _validate_admissibility_result(prefix, check, result, view_by_id, observed_view_by_id, errors)
            causal_ids = set(result.get("causal_slice_event_ids", []))
            referenced = causal_ids | {result[key] for key in ("root_event_id", "surfaced_at_event_id") if key in result}
            unknown_events = referenced - event_ids
            if unknown_events:
                errors.append(f"{prefix}, check {result['check_id']}: unknown causal event(s) {sorted(unknown_events)}")
            if causal_ids and not {result.get("root_event_id"), result.get("surfaced_at_event_id")} <= causal_ids:
                errors.append(f"{prefix}, check {result['check_id']}: causal slice must include root and surfaced events")

        if trial["status"] == "completed":
            missing_checks = check_ids - result_ids
            extra_checks = result_ids - check_ids
            if missing_checks or extra_checks:
                errors.append(f"{prefix}: completed trial check coverage mismatch; missing={sorted(missing_checks)}, extra={sorted(extra_checks)}")
            missing_artifacts = required_artifacts - observed_ids
            if missing_artifacts:
                errors.append(f"{prefix}: completed trial missing required artifacts {sorted(missing_artifacts)}")
            scored_results = [result for result in results if isinstance(result["score"], (int, float))]
            if result_ids == check_ids and len(scored_results) == len(results):
                total_weight = sum(check_by_id[cid]["weight"] for cid in check_ids)
                expected = sum(check_by_id[result["check_id"]]["weight"] * result["score"] for result in results) / total_weight
                if abs(expected - trial["aggregate_score"]) > 1e-6:
                    errors.append(f"{prefix}: aggregate_score {trial['aggregate_score']} != weighted score {expected:.6f}")
            elif result_ids == check_ids:
                errors.append(f"{prefix}: completed trial cannot aggregate non-scored admissibility outcomes")

    longitudinal = bundle.get("longitudinal_evaluation")
    if longitudinal:
        prefix = f"longitudinal_evaluation {longitudinal['protocol_id']}"
        stream = longitudinal["stream"]
        conditions = longitudinal["conditions"]
        evolution_events = longitudinal["evolution_events"]
        probes = longitudinal["probes"]
        for items, key, location in [
            (stream, "stream_item_id", f"{prefix}.stream"),
            (conditions, "condition_id", f"{prefix}.conditions"),
            (evolution_events, "evolution_event_id", f"{prefix}.evolution_events"),
            (probes, "probe_id", f"{prefix}.probes"),
        ]:
            _check_unique(items, key, location, errors)

        stream_ids = {item["stream_item_id"] for item in stream}
        stream_by_id = {item["stream_item_id"]: item for item in stream}
        stream_sequences = [item["sequence"] for item in stream]
        if stream_sequences != sorted(stream_sequences) or len(stream_sequences) != len(set(stream_sequences)):
            errors.append(f"{prefix}: stream sequences must be unique and ordered")
        stages = set(longitudinal["stages"])
        for item in stream:
            if item["stage_id"] not in stages:
                errors.append(f"{prefix}: stream item {item['stream_item_id']!r} references unknown stage")
            if item["task_id"] != task["task_id"] or item["task_version"] != task["version"]:
                errors.append(f"{prefix}: stream item {item['stream_item_id']!r} does not match frozen bundle task")
        frozen = longitudinal["frozen_instrument"]
        if frozen["component_id"] != task["task_id"] or frozen["version"] != task["version"]:
            errors.append(f"{prefix}: frozen instrument does not match bundle task identity/version")

        treatment_set = {item["treatment"] for item in conditions}
        if treatment_set != {"reset", "lesson_only", "full_evolution"} or len(conditions) != 3:
            errors.append(f"{prefix}: conditions must contain exactly one reset, lesson_only, and full_evolution arm")
        initial_hashes = {item["initial_state"]["state_sha256"] for item in conditions}
        if len(initial_hashes) != 1:
            errors.append(f"{prefix}: matched conditions must share one initial state hash")
        condition_by_id = {item["condition_id"]: item for item in conditions}
        assigned_trial_ids: list[str] = []
        for condition in conditions:
            treatment = condition["treatment"]
            loci = set(condition["allowed_update_loci"])
            persistence = condition["persistence_policy"]
            _check_unique(condition["initial_state"]["components"], "component_id", f"condition {condition['condition_id']}.initial_state", errors)
            if treatment == "reset" and (condition["reset_policy"] != "before_every_item" or loci or any(persistence[key] for key in ("model", "prompt_skill", "memory", "tools_code", "topology"))):
                errors.append(f"condition {condition['condition_id']}: reset arm cannot persist or update agent state")
            if treatment == "lesson_only" and not loci <= {"prompt_skill", "memory"}:
                errors.append(f"condition {condition['condition_id']}: lesson_only arm may update only prompt_skill or memory")
            for trial_id in condition["trial_ids"]:
                if trial_id not in {trial["trial_id"] for trial in trials}:
                    errors.append(f"condition {condition['condition_id']}: unknown trial_id {trial_id!r}")
            assigned_trial_ids.extend(condition["trial_ids"])
        if len(assigned_trial_ids) != len(set(assigned_trial_ids)):
            errors.append(f"{prefix}: a trial cannot belong to multiple longitudinal conditions")

        event_ids = {event["evolution_event_id"] for event in evolution_events}
        last_child_by_condition: dict[str, str] = {}
        for event in evolution_events:
            event_id = event["evolution_event_id"]
            condition = condition_by_id.get(event["condition_id"])
            if condition is None:
                errors.append(f"evolution event {event_id}: unknown condition_id")
            elif condition["treatment"] == "reset":
                errors.append(f"evolution event {event_id}: reset arm cannot contain evolution events")
            elif not set(event["changed_loci"]) <= set(condition["allowed_update_loci"]):
                errors.append(f"evolution event {event_id}: changed loci exceed condition allowance")
            if event["after_stream_item_id"] not in stream_ids:
                errors.append(f"evolution event {event_id}: unknown after_stream_item_id")
            if event["parent_state"]["state_sha256"] == event["child_state"]["state_sha256"]:
                errors.append(f"evolution event {event_id}: parent and child state hashes must differ")
            for state_name in ("parent_state", "child_state"):
                _check_unique(event[state_name]["components"], "component_id", f"evolution event {event_id}.{state_name}", errors)
            expected_parent = last_child_by_condition.get(event["condition_id"], condition["initial_state"]["state_sha256"] if condition else None)
            if expected_parent and event["parent_state"]["state_sha256"] != expected_parent:
                errors.append(f"evolution event {event_id}: parent state does not continue its condition ledger")
            last_child_by_condition[event["condition_id"]] = event["child_state"]["state_sha256"]
            for exposure in event["feedback_exposures"]:
                if exposure["kind"] in {"private_check", "reference_answer"} or exposure["visibility"] == "grader_only":
                    errors.append(f"evolution event {event_id}: private/grader-only evidence cannot feed an update")
            validation = event["validation"]
            if validation["status"] == "rolled_back":
                rollback_id = validation.get("rollback_to_event_id")
                if not rollback_id or rollback_id not in event_ids or rollback_id == event_id:
                    errors.append(f"evolution event {event_id}: rolled_back status requires another known rollback target")
            for downstream_id in event["downstream_event_ids"]:
                if downstream_id not in event_ids or downstream_id == event_id:
                    errors.append(f"evolution event {event_id}: invalid downstream event {downstream_id!r}")

        stage_budget = longitudinal["stage_budget"]
        cumulative_budget = longitudinal["cumulative_budget"]
        for key, stage_value in stage_budget.items():
            if cumulative_budget[key] < stage_value:
                errors.append(f"{prefix}: cumulative {key} budget is below stage budget")
        for probe in probes:
            item = stream_by_id.get(probe["stream_item_id"])
            if item is None:
                errors.append(f"probe {probe['probe_id']}: unknown stream_item_id")
            else:
                expected_split = {
                    "retention": "retention_probe",
                    "selective_forgetting": "selective_forgetting_probe",
                    "transfer": "transfer_probe",
                    "safety_drift": "safety_probe",
                }[probe["kind"]]
                if item["exposure_split"] != expected_split:
                    errors.append(f"probe {probe['probe_id']}: stream item split does not match probe kind")
                if item["cluster_id"] != probe["target_cluster_id"]:
                    errors.append(f"probe {probe['probe_id']}: target cluster does not match stream item")
            if probe["kind"] == "retention" and probe["form_policy"] == "exact_replay":
                errors.append(f"probe {probe['probe_id']}: retention must use an equivalent form to avoid answer replay")

    return errors


def _provenance_local_paths(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        if {"source_type", "locator", "description"} <= value.keys() and "local_path" in value:
            yield value["local_path"]
        for child in value.values():
            yield from _provenance_local_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from _provenance_local_paths(child)


def validate_file(bundle_path: Path, schema_path: Path, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(bundle), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(bundle))
    if check_paths:
        for local_path in _provenance_local_paths(bundle):
            if not (ROOT / local_path).is_file():
                errors.append(f"provenance local_path does not exist: {local_path}")
        for skill in bundle.get("procedural_skills", []):
            content_path = ROOT / skill["content_path"]
            if not content_path.is_file():
                errors.append(f"procedural skill content_path does not exist: {skill['content_path']}")
            elif hashlib.sha256(content_path.read_bytes()).hexdigest() != skill["sha256"]:
                errors.append(f"procedural skill sha256 mismatch: {skill['skill_id']}")
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundles", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true", help="require provenance local_path files to exist in the repository")
    args = parser.parse_args()
    failed = False
    for bundle_path in args.bundles:
        try:
            validate_file(bundle_path, args.schema, args.check_paths)
            print(f"VALID {bundle_path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {bundle_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
