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


REALIZATION_STAGES = ("mounted", "installed", "visible", "selected", "invoked", "attempted", "realized")


def _validate_component_locks(locks: list[dict[str, Any]], errors: list[str]) -> dict[str, dict[str, Any]]:
    """Validate immutable mixed-component locks without promoting reachability to exposure."""
    _check_unique(locks, "lock_id", "component_dependency_locks", errors)
    lock_by_id = {item["lock_id"]: item for item in locks}
    for lock in locks:
        prefix = f"component lock {lock['lock_id']}"
        payload = {key: value for key, value in lock.items() if key != "sha256"}
        if lock["sha256"] != canonical_sha256(payload):
            errors.append(f"{prefix}: stale lock sha256")
        _check_unique(lock["components"], "component_id", f"{prefix}.components", errors)
        _check_unique(lock["relations"], "relation_id", f"{prefix}.relations", errors)
        _check_unique(lock["clusters"], "cluster_id", f"{prefix}.clusters", errors)
        components = {item["component_id"]: item for item in lock["components"]}
        collision_members = {
            component_id
            for cluster in lock["clusters"] if cluster["kind"] == "name_collision"
            for component_id in cluster["component_ids"]
        }
        for component in lock["components"]:
            component_id = component["component_id"]
            if component["identity_status"] == "resolved" and component["version"] is None:
                errors.append(f"{prefix}, component {component_id}: resolved identity requires an exact version")
            if component["identity_status"] == "ambiguous" and component_id not in collision_members:
                errors.append(f"{prefix}, component {component_id}: ambiguous identity requires a name_collision cluster")
            for signal in component["signals"]:
                expected = "unresolved" if component["version"] is None else (
                    "affected" if component["version"] in signal["affected_versions"] else "not_affected"
                )
                if signal["match_status"] != expected:
                    errors.append(f"{prefix}, component {component_id}: signal {signal['signal_id']} does not match exact resolved version")
        for cluster in lock["clusters"]:
            unknown = set(cluster["component_ids"]) - set(components)
            if unknown:
                errors.append(f"{prefix}, cluster {cluster['cluster_id']}: unknown components {sorted(unknown)}")
        for relation in lock["relations"]:
            if relation["from_component_id"] not in components or relation["to_component_id"] not in components:
                errors.append(f"{prefix}, relation {relation['relation_id']}: references unknown component")
            if relation["activation"] == "example_only" and not relation["optional"]:
                errors.append(f"{prefix}, relation {relation['relation_id']}: example-only relation must be optional")
    return lock_by_id


def _validate_component_realization(
    realization: dict[str, Any], lock_by_id: dict[str, dict[str, Any]], event_ids: set[str], errors: list[str], prefix: str
) -> None:
    """Validate stage evidence while keeping mount, visibility, action, and consequence distinct."""
    ref = realization["lock"]
    lock = lock_by_id.get(ref["component_id"])
    if lock is None:
        errors.append(f"{prefix}.component_realization: references unknown component lock")
        return
    if (ref["version"], ref["sha256"]) != (lock["version"], lock["sha256"]):
        errors.append(f"{prefix}.component_realization: lock version/hash mismatch")
    component_by_id = {item["component_id"]: item for item in lock["components"]}
    _check_unique(realization["observations"], "component_id", f"{prefix}.component_realization.observations", errors)
    unknown_treatments = set(realization["intended_treatment_component_ids"]) - set(component_by_id)
    if unknown_treatments:
        errors.append(f"{prefix}.component_realization: unknown intended treatment components {sorted(unknown_treatments)}")
    intended = set(realization["intended_treatment_component_ids"])
    unrelated_payload = {
        "components": [item for item in lock["components"] if item["component_id"] not in intended],
        "relations": [item for item in lock["relations"] if item["from_component_id"] not in intended and item["to_component_id"] not in intended],
    }
    if realization["unrelated_lock_sha256"] != canonical_sha256(unrelated_payload):
        errors.append(f"{prefix}.component_realization: stale unrelated lock sha256")
    example_only_targets = {
        item["to_component_id"] for item in lock["relations"] if item["activation"] == "example_only"
    } - {
        item["to_component_id"] for item in lock["relations"] if item["activation"] != "example_only"
    }
    for observation in realization["observations"]:
        component_id = observation["component_id"]
        component = component_by_id.get(component_id)
        if component is None:
            errors.append(f"{prefix}.component_realization: unknown observed component {component_id!r}")
            continue
        if (observation["version"], observation["source_sha256"]) != (component["version"], component["source_sha256"]):
            errors.append(f"{prefix}, component {component_id}: observed version/hash drift from lock")
        _check_unique(observation["stages"], "stage", f"{prefix}, component {component_id}.stages", errors)
        stages = {item["stage"]: item for item in observation["stages"]}
        if set(stages) != set(REALIZATION_STAGES):
            errors.append(f"{prefix}, component {component_id}: realization ladder must contain every stage exactly once")
            continue
        for stage in stages.values():
            if set(stage["event_ids"]) - event_ids:
                errors.append(f"{prefix}, component {component_id}: {stage['stage']} references unknown trace event")
            if stage["status"] == "observed_true" and not stage["event_ids"]:
                errors.append(f"{prefix}, component {component_id}: observed-true {stage['stage']} requires trace evidence")
        if component_id in example_only_targets and stages["installed"]["status"] == "observed_true":
            errors.append(f"{prefix}, component {component_id}: example-only mention cannot become installed treatment state")
        for later, earlier in (("selected", "visible"), ("invoked", "selected"), ("attempted", "invoked"), ("realized", "attempted")):
            if stages[later]["status"] == "observed_true" and stages[earlier]["status"] != "observed_true":
                errors.append(f"{prefix}, component {component_id}: {later} cannot be true without {earlier}")
        attempted = stages["attempted"]
        realized = stages["realized"]
        if attempted["status"] == "observed_true" and "policy_decision" not in attempted:
            errors.append(f"{prefix}, component {component_id}: attempted action requires a policy decision")
        if attempted.get("policy_decision") == "denied" and realized["status"] != "observed_false":
            errors.append(f"{prefix}, component {component_id}: denied attempt cannot be a realized consequence")
        if realized["status"] == "observed_true":
            before, after = realized.get("before_state_sha256"), realized.get("after_state_sha256")
            if before is None or after is None or before == after:
                errors.append(f"{prefix}, component {component_id}: realized consequence requires distinct before/after state hashes")


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


def _validate_resource_envelope(
    contract: dict[str, Any], observation: dict[str, Any], errors: list[str], prefix: str,
) -> None:
    """Fail closed across parent, overlay, observer, attempt, and commit identities."""
    label = f"{prefix}.workspace.resource_envelope"
    operations = contract["operations"]
    _check_unique(operations, "operation_id", f"{label}.operations", errors)
    sequences = [item["sequence"] for item in operations]
    if sequences != sorted(sequences) or len(sequences) != len(set(sequences)):
        errors.append(f"{label}: operations require a complete unique order")
    operation_by_id = {item["operation_id"]: item for item in operations}
    operation_order = {item["operation_id"]: item["sequence"] for item in operations}
    for operation in operations:
        for dependency in operation["depends_on"]:
            if dependency not in operation_by_id or operation_order.get(dependency, 10**9) >= operation["sequence"]:
                errors.append(f"{label} operation {operation['operation_id']}: dependency is missing or not earlier")

    resources = contract["resources"]
    _check_unique(resources, "resource_id", f"{label}.resources", errors)
    resource_by_id = {item["resource_id"]: item for item in resources}
    kinds = {item["kind"] for item in resources}
    if "structured_table" not in kinds or not kinds.intersection({"file_blob", "cache_queue"}):
        errors.append(f"{label}: inventory must include structured and non-table mutable resources")
    region_keys: set[tuple[str, str]] = set()
    canary_by_id: dict[str, dict[str, Any]] = {}
    for resource in resources:
        _check_unique(resource["regions"], "region_id", f"{label} resource {resource['resource_id']}.regions", errors)
        paths = {item["path"] for item in resource["canaries"]}
        if paths != {"foreground", "background"}:
            errors.append(f"{label} resource {resource['resource_id']}: canaries must cover foreground and background")
        for region in resource["regions"]:
            region_keys.add((resource["resource_id"], region["region_id"]))
        for canary in resource["canaries"]:
            if canary["canary_id"] in canary_by_id:
                errors.append(f"{label}: duplicate canary_id {canary['canary_id']!r}")
            canary_by_id[canary["canary_id"]] = canary

    observer = contract["observer"]
    observer_payload = {key: value for key, value in observer.items() if key != "component"}
    if observer["component"]["sha256"] != canonical_sha256(observer_payload):
        errors.append(f"{label}: observer comparator/read-set hash is stale")
    read_keys = {(item["resource_id"], item["region_id"]) for item in observer["read_set"]}
    exclusion_keys = {(item["resource_id"], item["region_id"]) for item in observer["exclusions"]}
    if (read_keys | exclusion_keys) - region_keys:
        errors.append(f"{label}: observer read set or exclusion references an unknown region")
    if read_keys & exclusion_keys:
        errors.append(f"{label}: observer cannot both read and exclude a region")

    if (observation["instrument_id"], observation["version"], observation["session_id"]) != (
        contract["instrument_id"], contract["version"], contract["session_id"]
    ):
        errors.append(f"{label}: instrument/session identity mismatch")
    parent = contract["parent"]
    if observation["start_parent_root_sha256"] != parent["state_root_sha256"]:
        errors.append(f"{label}: trial did not start from the declared parent root")
    parent_changed = observation["end_parent_root_sha256"] != observation["start_parent_root_sha256"]

    _check_unique(observation["canary_results"], "canary_id", f"{label}.canary_results", errors)
    result_by_id = {item["canary_id"]: item for item in observation["canary_results"]}
    if set(result_by_id) != set(canary_by_id):
        errors.append(f"{label}: canary result coverage mismatch")
    canary_failed = False
    for canary_id, declaration in canary_by_id.items():
        result = result_by_id.get(canary_id)
        if result and result["observed"] != declaration["expected"]:
            canary_failed = True

    mutations = observation["mutations"]
    _check_unique(mutations, "mutation_id", f"{label}.mutations", errors)
    mutation_sequences = [item["sequence"] for item in mutations]
    if mutation_sequences != sorted(mutation_sequences) or len(mutation_sequences) != len(set(mutation_sequences)):
        errors.append(f"{label}: mutation ledger must be complete and ordered")
    mutation_by_id = {item["mutation_id"]: item for item in mutations}
    mutation_order = {item["mutation_id"]: item["sequence"] for item in mutations}
    for mutation in mutations:
        if mutation["operation_id"] not in operation_by_id:
            errors.append(f"{label} mutation {mutation['mutation_id']}: unknown operation")
        if (mutation["resource_id"], mutation["region_id"]) not in region_keys:
            errors.append(f"{label} mutation {mutation['mutation_id']}: unknown resource region")
        for dependency in mutation["depends_on"]:
            if dependency not in mutation_by_id or mutation_order.get(dependency, 10**9) >= mutation["sequence"]:
                errors.append(f"{label} mutation {mutation['mutation_id']}: dependency is missing or not earlier")
        key = (mutation["resource_id"], mutation["region_id"])
        expected_observation = "observed" if key in read_keys else "excluded" if key in exclusion_keys else "unobserved"
        if mutation["context_status"] == "untagged":
            expected_observation = "escaped"
        if mutation["observation_status"] != expected_observation:
            errors.append(f"{label} mutation {mutation['mutation_id']}: observation status does not follow context/read-set evidence")
    if not any(item["kind"] == "update" and item["before"] is not None and item["after"] is None and item["observation_status"] == "observed" for item in mutations):
        errors.append(f"{label}: intentional null update was not preserved as an observed mutation")
    if not any(item["kind"] == "increment" for item in mutations):
        errors.append(f"{label}: sequence/global increment case is missing")
    if not any(resource_by_id.get(item["resource_id"], {}).get("kind") in {"file_blob", "cache_queue"} for item in mutations):
        errors.append(f"{label}: non-table blob/cache effect is missing")
    escaped = any(item["observation_status"] == "escaped" for item in mutations)
    background_canary_escaped = any(
        result_by_id.get(canary_id, {}).get("observed") == "escaped"
        for canary_id, declaration in canary_by_id.items() if declaration["path"] == "background"
    )
    if escaped != background_canary_escaped:
        errors.append(f"{label}: escaped mutation and background-canary evidence disagree")
    observer_gap = any(item["observation_status"] in {"excluded", "unobserved"} for item in mutations)

    alternatives = {item["alternative_id"]: item for item in observer["accepted_alternatives"]}
    ambiguous = False
    for match in observation["matches"]:
        if match["resource_id"] not in resource_by_id:
            errors.append(f"{label} match {match['match_id']}: unknown resource")
        if len(match["candidate_item_keys"]) > 1:
            ambiguous = True
            if match["outcome"] != "insufficient_evidence":
                errors.append(f"{label} match {match['match_id']}: ambiguous same-resource candidates must fail closed")
        if "alternative_id" in match:
            alternative = alternatives.get(match["alternative_id"])
            if alternative is None or alternative["resource_id"] != match["resource_id"] or alternative["item_key"] not in match["candidate_item_keys"]:
                errors.append(f"{label} match {match['match_id']}: undeclared or mismatched accepted alternative")
            elif alternative["status"] == "accepted" and len(match["candidate_item_keys"]) == 1 and match["outcome"] != "accepted":
                errors.append(f"{label} match {match['match_id']}: declared unambiguous alternative was not admitted")

    attempt = observation["attempt"]
    expected_attempt = {"completed": "eligible", "failed_evaluation": "failed_attempt", "invalid_environment": "invalid_attempt"}[attempt["status"]]
    if attempt["disposition"] != expected_attempt or not attempt["denominator_included"]:
        errors.append(f"{label}: failed/invalid attempt disposition or denominator is incorrect")
    commit = observation["commit_assessment"]
    selected_operations = set(commit["selected_operation_ids"])
    if selected_operations - set(operation_by_id):
        errors.append(f"{label}: commit selects an unknown operation")
    computed_closure = all(set(operation_by_id[operation_id]["depends_on"]) <= selected_operations for operation_id in selected_operations if operation_id in operation_by_id)
    if commit["dependency_closure"] != computed_closure:
        errors.append(f"{label}: commit dependency-closure label does not replay")
    unsafe_commit = commit["requested"] and (not commit["authorized"] or not computed_closure or commit["stale_base"] or parent_changed)
    if unsafe_commit and commit["decision"] != "reject_commit":
        errors.append(f"{label}: unauthorized, stale, or dependency-incomplete commit was not rejected")
    if not commit["requested"] and commit["decision"] != "discard":
        errors.append(f"{label}: evaluation session must default to discard")
    if commit["decision"] == "commit" and commit["rollback_status"] != "verified":
        errors.append(f"{label}: committed state lacks a verified rollback path")

    expected_overall = "invalid_environment" if (parent_changed or canary_failed or escaped or attempt["status"] == "invalid_environment") else "insufficient_evidence" if (observer_gap or ambiguous or attempt["status"] == "failed_evaluation") else "conformant"
    if observation["overall_disposition"] != expected_overall:
        errors.append(f"{label}: overall disposition does not fail closed from planted evidence")


def resource_envelope_errors(contract: dict[str, Any], observation: dict[str, Any]) -> list[str]:
    """Return semantic errors for a generic cross-resource envelope pair."""
    errors: list[str] = []
    _validate_resource_envelope(contract, observation, errors, "resource-envelope")
    return errors


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


def _validate_context_compression(
    contract: dict[str, Any], observation: dict[str, Any] | None,
    event_by_id: dict[str, dict[str, Any]], errors: list[str], prefix: str,
) -> None:
    """Validate lossy-state lineage without collapsing fidelity, sufficiency, and cost."""
    invariants = contract["invariants"]
    _check_unique(invariants, "invariant_id", "task.context_compression.invariants", errors)
    invariant_by_id = {item["invariant_id"]: item for item in invariants}
    required_kinds = {"entity", "value", "modality", "valid_time", "provenance", "contradiction", "required_literal", "secret_handle", "artifact_state"}
    if {item["kind"] for item in invariants} != required_kinds:
        errors.append("task.context_compression: invariants must cover every planted corruption kind")
    required_treatments = {"full_context", "reset_only", "structured_reformat_only", "compression"}
    if set(contract["treatments"]) != required_treatments:
        errors.append("task.context_compression: require full-context, reset-only, structured-reformat-only, and compression treatments")
    required_probes = set(contract["required_probes"])
    if not {"next_action", "alternate_future"} <= required_probes:
        errors.append("task.context_compression: next-action and alternate-future probes are mandatory")
    if observation is None:
        return
    if (observation["instrument_id"], observation["version"]) != (contract["instrument_id"], contract["version"]):
        errors.append(f"{prefix}.context_compression: instrument identity/version mismatch")
    events = observation["events"]
    _check_unique(events, "compression_event_id", f"{prefix}.context_compression.events", errors)
    if not required_treatments <= {item["treatment"] for item in events}:
        errors.append(f"{prefix}.context_compression: matched treatment coverage is incomplete")
    raw_hash = contract["raw_evidence"]["sha256"]
    for item in events:
        label = f"{prefix}.context_compression event {item['compression_event_id']}"
        trace_event = event_by_id.get(item["trace_event_id"])
        if trace_event is None or trace_event.get("kind") != "context_compression" or trace_event.get("compression_event_id") != item["compression_event_id"]:
            errors.append(f"{label}: missing or mismatched context_compression trace event")
        if item["raw_input_sha256"] != raw_hash or not item["raw_evidence_preserved"]:
            errors.append(f"{label}: immutable authoritative raw evidence was not preserved")
        treatment = item["treatment"]
        expected_trigger = {"full_context": "none", "reset_only": "session_reset", "structured_reformat_only": "manual_reformat", "compression": "token_threshold"}[treatment]
        if item["trigger"]["kind"] != expected_trigger:
            errors.append(f"{label}: trigger is confounded with declared treatment")
        compressor = item["compressor"]
        if (treatment == "compression") != (compressor is not None):
            errors.append(f"{label}: compressor configuration must appear only in compression treatment")
        if treatment == "compression" and item["output_sha256"] == item["raw_input_sha256"]:
            errors.append(f"{label}: compression output identity cannot equal raw input identity")

        invariant_results = item["invariant_results"]
        _check_unique(invariant_results, "invariant_id", f"{label}.invariant_results", errors)
        if {row["invariant_id"] for row in invariant_results} != set(invariant_by_id):
            errors.append(f"{label}: invariant result coverage mismatch")
        invariant_outcomes = [row["outcome"] for row in invariant_results]
        expected_fidelity = "insufficient_evidence" if "insufficient_evidence" in invariant_outcomes else "failed" if "failed" in invariant_outcomes else "passed"
        if item["outcomes"]["fidelity"] != expected_fidelity:
            errors.append(f"{label}: fidelity outcome does not fail closed from invariant evidence")

        probe_results = item["probe_results"]
        _check_unique(probe_results, "probe", f"{label}.probe_results", errors)
        probe_by_kind = {row["probe"]: row for row in probe_results}
        if set(probe_by_kind) != required_probes:
            errors.append(f"{label}: probe result coverage mismatch")
        for probe in ("next_action", "alternate_future"):
            if probe in probe_by_kind and item["outcomes"]["decision_sufficiency"][probe] != probe_by_kind[probe]["outcome"]:
                errors.append(f"{label}: {probe} sufficiency outcome does not replay from probe evidence")

        efficiency = item["outcomes"]["efficiency"]
        if treatment == "full_context" and efficiency["outcome"] != "baseline":
            errors.append(f"{label}: full-context efficiency must remain the baseline")
        if treatment != "compression" and efficiency["compressor_calls"] != 0:
            errors.append(f"{label}: control treatment cannot include compressor calls")
        if treatment == "compression" and efficiency["compressor_calls"] < 1:
            errors.append(f"{label}: compression treatment requires measured compressor calls")


def _validate_storage_retention(
    contract: dict[str, Any], observation: dict[str, Any] | None,
    errors: list[str], prefix: str,
) -> None:
    """Validate retention stocks against typed utility, lineage, and lifecycle evidence."""
    required_conditions = {"raw", "none", "cas", "summary_only", "selective_private_deletion"}
    required_utilities = {
        "conversation_reconstruction", "request_reconstruction", "executable_replay",
        "between_turn_resume", "workflow_recovery", "provenance_query", "causal_diagnosis",
        "grader_replay", "handoff", "selective_deletion",
    }
    if set(contract["conditions"]) != required_conditions:
        errors.append("task.storage_retention: require raw, none, CAS, summary-only, and selective-private-deletion conditions")
    if set(contract["required_utilities"]) != required_utilities:
        errors.append("task.storage_retention: required utility predicate coverage is incomplete")
    _check_unique(contract["channels"], "channel_id", "task.storage_retention.channels", errors)
    channel_ids = {item["channel_id"] for item in contract["channels"]}
    if not {"setup", "execution", "evaluator", "local", "remote"} <= set(contract["boundaries"]):
        errors.append("task.storage_retention: setup/execution/evaluator and local/remote boundaries are mandatory")
    for channel in contract["channels"]:
        if not channel["included"] and not channel.get("exclusion_reason"):
            errors.append(f"task.storage_retention channel {channel['channel_id']}: excluded channel requires a reason")
    if observation is None:
        return
    if (observation["instrument_id"], observation["version"]) != (contract["instrument_id"], contract["version"]):
        errors.append(f"{prefix}.storage_retention: instrument identity/version mismatch")
    if observation["fixed_trace_sha256"] != contract["fixed_trace_sha256"]:
        errors.append(f"{prefix}.storage_retention: fixed-trace identity mismatch")
    results = observation["condition_results"]
    _check_unique(results, "condition", f"{prefix}.storage_retention.condition_results", errors)
    if {item["condition"] for item in results} != required_conditions:
        errors.append(f"{prefix}.storage_retention: matched condition coverage is incomplete")
    attempt_statuses: set[str] = set()
    for result in results:
        condition = result["condition"]
        label = f"{prefix}.storage_retention condition {condition}"
        _check_unique(result["attempts"], "attempt_id", f"{label}.attempts", errors)
        attempt_statuses.update(item["status"] for item in result["attempts"])
        representations = result["representations"]
        _check_unique(representations, "representation_id", f"{label}.representations", errors)
        representation_by_id = {item["representation_id"]: item for item in representations}
        for item in representations:
            if item["channel_id"] not in channel_ids:
                errors.append(f"{label}, representation {item['representation_id']}: unknown channel_id")
            source_id = item.get("source_representation_id")
            if source_id and source_id not in representation_by_id:
                errors.append(f"{label}, representation {item['representation_id']}: broken representation lineage")
            if bool(source_id) != bool(item.get("transformation_id")):
                errors.append(f"{label}, representation {item['representation_id']}: transformed representation requires source and transformation identities")
        measured_bytes = sum(item["bytes"] for item in representations)
        if result["retained_bytes"] != measured_bytes:
            errors.append(f"{label}: retained_bytes does not equal representation bytes")
        if abs(result["byte_days"] - result["retained_bytes"] * result["retention_days"]) > 1e-6:
            errors.append(f"{label}: byte_days does not replay from retained bytes and duration")
        shared = result["shared_store"]
        if shared["growth_bytes"] != shared["after_bytes"] - shared["before_bytes"]:
            errors.append(f"{label}: shared-store growth does not replay")
        utilities = result["utility_results"]
        _check_unique(utilities, "utility", f"{label}.utility_results", errors)
        if {item["utility"] for item in utilities} != required_utilities:
            errors.append(f"{label}: utility predicate coverage mismatch")
        utility_by_id = {item["utility"]: item for item in utilities}
        if condition == "none" and (representations or result["retained_bytes"] != 0):
            errors.append(f"{label}: no-persistence condition retained state")
        if condition == "none" and any(item["outcome"] == "passed" for item in utilities if item["utility"] != "selective_deletion"):
            errors.append(f"{label}: no-persistence condition cannot pass retention-dependent utility")
        transformation_ids = {item["transformation_id"] for item in result["transformations"]}
        for item in representations:
            if item.get("transformation_id") and item["transformation_id"] not in transformation_ids:
                errors.append(f"{label}, representation {item['representation_id']}: missing transformation evidence")
        if condition == "selective_private_deletion":
            private_retained = [item["representation_id"] for item in representations if item["privacy"] in {"private", "restricted"}]
            deletion_passed = result["deletions"] and all(item["outcome"] == "passed" for item in result["deletions"])
            if private_retained or not deletion_passed or utility_by_id["selective_deletion"]["outcome"] != "passed":
                errors.append(f"{label}: selective deletion requires passed deletion evidence and no retained private representation")
        if result["remote_canary"]["observed"] == "detected" and utility_by_id["selective_deletion"]["outcome"] == "passed":
            errors.append(f"{label}: remote canary detection contradicts passed selective deletion")
    if not {"failed", "invalid_service"} <= attempt_statuses:
        errors.append(f"{prefix}.storage_retention: conformance slice must preserve failed and invalid-service attempt residue")


def semantic_errors(bundle: dict[str, Any]) -> list[str]:
    """Return cross-reference and completed-trial invariant violations."""
    errors: list[str] = []
    task = bundle["task"]
    skills = bundle["procedural_skills"]
    rubrics = bundle["rubrics"]
    sources = task["source_pack"]
    references = task.get("reference_materials", [])
    primitives = task["domain_primitives"]
    contracts = task["artifact_contracts"]
    artifact_views = task.get("artifact_views", [])
    checks = task["checks"]
    graders = bundle["graders"]
    trials = bundle["trials"]
    component_locks = bundle.get("component_dependency_locks", [])
    component_lock_by_id = _validate_component_locks(component_locks, errors)
    realization_pairs: dict[str, list[tuple[str, str, dict[str, Any]]]] = {}

    for items, key, location in [
        (skills, "skill_id", "procedural_skills"),
        (rubrics, "rubric_id", "rubrics"),
        (sources, "source_id", "task.source_pack"),
        (references, "reference_id", "task.reference_materials"),
        (primitives, "primitive_id", "task.domain_primitives"),
        (contracts, "artifact_id", "task.artifact_contracts"),
        (artifact_views, "view_id", "task.artifact_views"),
        (checks, "check_id", "task.checks"),
        (graders, "grader_id", "graders"),
        (trials, "trial_id", "trials"),
    ]:
        _check_unique(items, key, location, errors)

    source_ids = {item["source_id"] for item in sources}
    reference_by_id = {item["reference_id"]: item for item in references}
    skill_by_id = {item["skill_id"]: item for item in skills}
    rubric_by_id = {item["rubric_id"]: item for item in rubrics}
    artifact_ids = {item["artifact_id"] for item in contracts}
    view_by_id = {item["view_id"]: item for item in artifact_views}
    check_ids = {item["check_id"] for item in checks}
    grader_ids = {item["grader_id"] for item in graders}
    check_by_id = {item["check_id"]: item for item in checks}

    # This optional authoring preflight closes the criterion prose-to-arithmetic
    # chain. Existing bundles remain valid until they opt into signed criteria.
    signed_ids = {item["check_id"] for item in checks if "signed_criterion" in item}
    aggregation_by_id: dict[str, tuple[dict[str, Any], str]] = {}
    for rubric in rubrics:
        policies = rubric.get("aggregation_policies", [])
        _check_unique(policies, "aggregation_id", f"rubric {rubric['rubric_id']}.aggregation_policies", errors)
        for policy in policies:
            aggregation_id = policy["aggregation_id"]
            if aggregation_id in aggregation_by_id:
                errors.append(f"rubrics: duplicate aggregation_id {aggregation_id!r}")
            aggregation_by_id[aggregation_id] = (policy, rubric["rubric_id"])
            unknown = set(policy["check_ids"]) - check_ids
            if unknown:
                errors.append(f"aggregation {aggregation_id}: unknown check_ids {sorted(unknown)}")
            if policy["clipping"]["lower"] >= policy["clipping"]["upper"]:
                errors.append(f"aggregation {aggregation_id}: clipping lower must be less than upper")
            required = {
                check_id for check_id in policy["check_ids"]
                if check_by_id.get(check_id, {}).get("signed_criterion", {}).get("score", {}).get("role")
                in {"hard_gate", "required_scored"}
            }
            if policy["clipping"]["enabled"] and required and policy["required_failure_policy"] == "may_mask":
                errors.append(f"aggregation {aggregation_id}: clipping may mask required failures {sorted(required)}")

    prerequisite_graph: dict[str, set[str]] = {check_id: set() for check_id in signed_ids}
    for check in checks:
        criterion = check.get("signed_criterion")
        if not criterion:
            continue
        check_id = check["check_id"]
        if criterion["proposition_sha256"] != canonical_sha256(criterion["proposition"]):
            errors.append(f"check {check_id}: stale signed criterion proposition_sha256")
        mapping = criterion["pass_mapping"]
        expected_true = "pass" if criterion["polarity"] == "desirable_state" else "fail"
        if mapping["proposition_true"] != expected_true or mapping["proposition_false"] == expected_true:
            errors.append(f"check {check_id}: pass/fail mapping conflicts with criterion polarity")
        basis_requirement_ids = {item["requirement_id"] for item in criterion["public_basis"]}
        if basis_requirement_ids != set(check["public_basis_requirement_ids"]):
            errors.append(f"check {check_id}: signed criterion public basis does not match check requirement basis")
        for basis in criterion["public_basis"]:
            if basis["relation"] == "exact" and canonical_sha256(basis["semantic_value"]) != canonical_sha256(criterion["semantic_value"]):
                errors.append(f"check {check_id}: exact public basis contradicts criterion semantic value")
            if basis["relation"] == "reviewed_equivalent" and (basis["review_status"] != "reviewed" or not basis.get("review_provenance")):
                errors.append(f"check {check_id}: reviewed equivalence lacks review provenance")
            if basis["relation"] != "reviewed_equivalent" and basis["review_status"] != "not_required":
                errors.append(f"check {check_id}: non-equivalence basis has inconsistent review status")
        score = criterion["score"]
        aggregation = aggregation_by_id.get(score["aggregation_id"])
        if not aggregation or aggregation[1] != check["rubric_id"] or check_id not in aggregation[0]["check_ids"]:
            errors.append(f"check {check_id}: signed score has missing or non-reciprocal aggregation identity")
        expected_scores = {"reward": (score["magnitude"], 0), "penalty": (0, -score["magnitude"]), "none": (0, 0)}[score["direction"]]
        if (score["on_pass"], score["on_fail"]) != expected_scores:
            errors.append(f"check {check_id}: signed contributions conflict with direction/magnitude")
        role_directions = {
            "hard_gate": {"none"}, "required_scored": {"reward"}, "optional_preference": {"reward"},
            "penalty": {"penalty"}, "diagnostic_only": {"none"},
        }
        if score["direction"] not in role_directions[score["role"]]:
            errors.append(f"check {check_id}: score role conflicts with direction")
        if score["role"] in {"hard_gate", "diagnostic_only"} and score["magnitude"] != 0:
            errors.append(f"check {check_id}: gate/diagnostic magnitude must be zero")
        if score["role"] == "penalty" and criterion["polarity"] == "desirable_state" and not score["inversion"]:
            errors.append(f"check {check_id}: desirable-state penalty requires explicit inversion")
        if score["role"] != "penalty" and score["inversion"]:
            errors.append(f"check {check_id}: inversion is only defined for an explicit penalty")
        for dependency in criterion["dependencies"]:
            target = dependency["check_id"]
            if target not in signed_ids:
                errors.append(f"check {check_id}: dangling signed criterion dependency {target!r}")
            if target == check_id:
                errors.append(f"check {check_id}: signed criterion cannot depend on itself")
            if dependency["relation"] == "prerequisite" and target in signed_ids:
                prerequisite_graph[check_id].add(target)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit_signed(check_id: str) -> None:
        if check_id in visiting:
            errors.append(f"signed criteria: cyclic prerequisite dependency at {check_id!r}")
            return
        if check_id in visited:
            return
        visiting.add(check_id)
        for target in prerequisite_graph[check_id]:
            visit_signed(target)
        visiting.remove(check_id)
        visited.add(check_id)

    for signed_id in sorted(signed_ids):
        visit_signed(signed_id)

    projection_manifest = task.get("projection_manifest")
    if projection_manifest:
        _validate_projection_manifest(projection_manifest, source_ids, errors)
    workspace_contract = task.get("workspace")
    if workspace_contract:
        _validate_workspace_contract(workspace_contract, None, source_ids, {}, errors, "task")
    action_safety_contract = task.get("action_safety")
    if action_safety_contract:
        _validate_action_safety(action_safety_contract, None, source_ids, {}, errors, "task")
    context_compression_contract = task.get("context_compression")
    if context_compression_contract:
        _validate_context_compression(context_compression_contract, None, {}, errors, "task")
    storage_retention_contract = task.get("storage_retention")
    if storage_retention_contract:
        _validate_storage_retention(storage_retention_contract, None, errors, "task")

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

    for reference in references:
        reference_id = reference["reference_id"]
        if reference["source_id"] not in source_ids:
            errors.append(f"reference {reference_id}: unknown source_id {reference['source_id']!r}")
        if reference["release_status"] == "public" and reference["exposure_status"] == "not_observed" and "exposure_policy" not in reference:
            errors.append(f"reference {reference_id}: public target marked not_observed requires a versioned exposure policy")
        if reference["exposure_status"] == "observed_exposed" and not reference["exposure_evidence"]:
            errors.append(f"reference {reference_id}: observed exposure requires evidence")

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
        comparison = check.get("reference_comparison")
        if comparison:
            relation = comparison["relation"]
            reference_id = comparison["reference_id"]
            if reference_id not in reference_by_id:
                errors.append(f"check {check['check_id']}: unknown comparison reference {reference_id!r}")
            if comparison["observer_evidence_sufficiency"] == "sufficient" and not comparison["observer_evidence_locators"]:
                errors.append(f"check {check['check_id']}: sufficient observer evidence requires locators")
            execution_relations = {"execution_reproduced", "metric_matched", "metric_improved_under_matched_protocol", "surpasses_reference"}
            evidence_types = set(comparison["observer_evidence_types"])
            if relation in execution_relations and not evidence_types.intersection({"command_trace", "execution_result"}):
                errors.append(f"check {check['check_id']}: execution comparison cannot be supported from report prose alone")
            verification = comparison["independent_verification"]
            if verification["state"] == "passed" and not verification["evidence_locators"]:
                errors.append(f"check {check['check_id']}: passed independent verification requires evidence")
            if relation in {"metric_improved_under_matched_protocol", "surpasses_reference"}:
                if "matched_baseline" not in comparison:
                    errors.append(f"check {check['check_id']}: {relation} requires matched baseline identity and protocol")
                if verification["state"] != "passed":
                    errors.append(f"check {check['check_id']}: {relation} requires passed independent verification")
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
        component_realization = trial.get("component_realization")
        if component_realization:
            _validate_component_realization(component_realization, component_lock_by_id, event_ids, errors, prefix)
            realization_pairs.setdefault(component_realization["pair_id"], []).append((
                trial["trial_id"], condition, component_realization
            ))
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
        context_compression_observation = trial.get("context_compression")
        if context_compression_observation and not context_compression_contract:
            errors.append(f"{prefix}.context_compression: observation has no task contract")
        elif context_compression_contract:
            if context_compression_observation is None:
                errors.append(f"{prefix}.context_compression: task contract requires a trial observation")
            else:
                _validate_context_compression(context_compression_contract, context_compression_observation, event_by_id, errors, prefix)
        storage_retention_observation = trial.get("storage_retention")
        if storage_retention_observation and not storage_retention_contract:
            errors.append(f"{prefix}.storage_retention: observation has no task contract")
        elif storage_retention_contract:
            if storage_retention_observation is None:
                errors.append(f"{prefix}.storage_retention: task contract requires a trial observation")
            else:
                _validate_storage_retention(storage_retention_contract, storage_retention_observation, errors, prefix)
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

    for pair_id, records in realization_pairs.items():
        conditions = {condition for _, condition, _ in records}
        if len(records) != 2 or not any(item.startswith("no_skill_") for item in conditions) or not any(
            item.startswith("public_skill_") for item in conditions
        ):
            errors.append(f"component realization pair {pair_id}: requires exactly one no-skill and one public-skill arm")
            continue
        unrelated_hashes = {record[2]["unrelated_lock_sha256"] for record in records}
        if len(unrelated_hashes) != 1:
            errors.append(f"component realization pair {pair_id}: unrelated lock hashes differ across Skill arms")

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
        compression = bundle.get("task", {}).get("context_compression")
        if compression:
            raw = compression["raw_evidence"]
            raw_path = ROOT / raw["path"]
            if not raw_path.is_file():
                errors.append(f"context compression raw evidence does not exist: {raw['path']}")
            elif hashlib.sha256(raw_path.read_bytes()).hexdigest() != raw["sha256"]:
                errors.append("context compression raw evidence sha256 mismatch")
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
