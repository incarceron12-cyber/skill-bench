#!/usr/bin/env python3
"""Build, validate, and replay the zero-call persistent-workspace reuse pilot."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONDITIONS = (
    "reset",
    "information_matched_full_history",
    "curated_correct",
    "curated_stale",
    "curated_conflicting",
    "curated_revoked",
    "deterministic_artifact_rerun",
)
WORK_SHAPES = ("tabular_procurement_refresh", "structured_policy_memo_refresh")
UNSUPPORTED_CLAIMS = {
    "general memory capability",
    "Skill effect",
    "professional validity",
    "privacy compliance",
    "collaboration benefit",
    "production reliability",
    "deployment readiness",
}


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()


def hashed(record: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(record)
    result["sha256"] = canonical_sha256(record)
    return result


def composition_hash(object_ids: list[str], by_id: dict[str, dict[str, Any]]) -> str:
    return canonical_sha256([{"object_id": oid, "sha256": by_id[oid]["sha256"]} for oid in object_ids])


def table_transform(data: dict[str, Any]) -> dict[str, Any]:
    """Pinned v2 migration: key, type, unit, category, join, and semantic changes."""
    owners = {row["supplier_id"]: row["owner"] for row in data["owners"]}
    category_map = {"A": "critical", "B": "standard"}
    rows = []
    for row in data["spend"]:
        rows.append({
            "supplier_id": int(row["vendor_code"].removeprefix("V")),
            "spend_usd": int(row["spend_thousands"]) * 1000,
            "risk_category": category_map[row["legacy_band"]],
            "owner": owners[int(row["vendor_code"].removeprefix("V"))],
            "requires_review": category_map[row["legacy_band"]] == "critical" and int(row["spend_thousands"]) * 1000 >= 100000,
        })
    return {"artifact_type": "structured_table", "rows": rows}


def memo_transform(data: dict[str, Any]) -> dict[str, Any]:
    """Pinned structured-memo refresh from current, authority-ranked evidence."""
    current = [item for item in data["evidence"] if item["authority"] == "policy_owner" and item["status"] == "current"]
    return {
        "artifact_type": "structured_memo",
        "decision": "escalate" if any(item["threshold_usd"] <= data["exposure_usd"] for item in current) else "monitor",
        "basis_ids": [item["id"] for item in current],
        "exposure_usd": data["exposure_usd"],
        "preserved_appendix": data["preserved_appendix"],
    }


def build_package() -> dict[str, Any]:
    table_input = {
        "spend": [
            {"vendor_code": "V101", "spend_thousands": "125", "legacy_band": "A"},
            {"vendor_code": "V202", "spend_thousands": "40", "legacy_band": "B"},
        ],
        "owners": [{"supplier_id": 101, "owner": "operations"}, {"supplier_id": 202, "owner": "finance"}],
    }
    memo_input = {
        "exposure_usd": 75000,
        "evidence": [
            {"id": "policy-current", "authority": "policy_owner", "status": "current", "threshold_usd": 50000},
            {"id": "policy-advisory", "authority": "analyst", "status": "current", "threshold_usd": 100000},
        ],
        "preserved_appendix": "control-register-v3",
    }
    table_output = table_transform(table_input)
    memo_output = memo_transform(memo_input)
    objects = [
        hashed({"object_id": "table-current-spec", "version": "2.0", "kind": "current_requirement", "originating_authority": "synthetic_task_owner", "accessor_permission": "read", "valid_time": {"from": "2026-07-01T00:00:00Z", "to": None}, "state": "current", "payload": "Use integer supplier_id, USD base units, current categories, supplier_id owner join, and review semantics."}),
        hashed({"object_id": "table-stale-spec", "version": "1.0", "kind": "requirement", "originating_authority": "synthetic_task_owner", "accessor_permission": "read", "valid_time": {"from": "2025-01-01T00:00:00Z", "to": "2026-06-30T23:59:59Z"}, "state": "stale", "payload": "Use vendor_code, thousands, legacy bands, and vendor_code join."}),
        hashed({"object_id": "table-conflict", "version": "2.0-draft", "kind": "requirement", "originating_authority": "unapproved_analyst", "accessor_permission": "read", "valid_time": {"from": "2026-07-01T00:00:00Z", "to": None}, "state": "conflicting", "payload": "Treat only standard suppliers as requiring review."}),
        hashed({"object_id": "table-revoked", "version": "1.1", "kind": "connector", "originating_authority": "synthetic_data_steward", "accessor_permission": "revoked", "valid_time": {"from": "2026-01-01T00:00:00Z", "to": "2026-06-30T23:59:59Z"}, "state": "revoked", "payload": "Legacy supplier connector grant."}),
        hashed({"object_id": "table-artifact-v1", "version": "1.0", "kind": "executable_artifact", "originating_authority": "internal_fixture_builder", "accessor_permission": "execute", "valid_time": {"from": "2026-01-01T00:00:00Z", "to": None}, "state": "current", "payload": "table_transform-v2-pinned"}),
        hashed({"object_id": "memo-current-spec", "version": "3.0", "kind": "current_requirement", "originating_authority": "synthetic_policy_owner", "accessor_permission": "read", "valid_time": {"from": "2026-07-01T00:00:00Z", "to": None}, "state": "current", "payload": "Use owner-authorized current threshold; preserve control appendix."}),
        hashed({"object_id": "memo-stale-spec", "version": "2.0", "kind": "requirement", "originating_authority": "synthetic_policy_owner", "accessor_permission": "read", "valid_time": {"from": "2025-01-01T00:00:00Z", "to": "2026-06-30T23:59:59Z"}, "state": "stale", "payload": "Escalation threshold is 100000 USD."}),
        hashed({"object_id": "memo-conflict", "version": "3.0-draft", "kind": "requirement", "originating_authority": "unapproved_analyst", "accessor_permission": "read", "valid_time": {"from": "2026-07-01T00:00:00Z", "to": None}, "state": "conflicting", "payload": "Analyst advisory overrides policy owner."}),
        hashed({"object_id": "memo-revoked", "version": "2.1", "kind": "source", "originating_authority": "synthetic_policy_owner", "accessor_permission": "revoked", "valid_time": {"from": "2026-01-01T00:00:00Z", "to": "2026-06-30T23:59:59Z"}, "state": "revoked", "payload": "Withdrawn exception permits monitor decision."}),
        hashed({"object_id": "memo-artifact-v1", "version": "1.0", "kind": "executable_artifact", "originating_authority": "internal_fixture_builder", "accessor_permission": "execute", "valid_time": {"from": "2026-01-01T00:00:00Z", "to": None}, "state": "current", "payload": "memo_transform-v1-pinned"}),
    ]
    by_id = {item["object_id"]: item for item in objects}
    shape_specs = {
        "tabular_procurement_refresh": {
            "current_object": "table-current-spec", "stale": "table-stale-spec", "conflict": "table-conflict", "revoked": "table-revoked", "artifact": "table-artifact-v1",
            "current_input": table_input, "expected_output": table_output,
            "compatibility_changes": [
                {"dimension": "type", "change": "string vendor code to integer supplier_id", "handled_by": "table_transform-v2-pinned"},
                {"dimension": "unit", "change": "thousands to USD base units", "handled_by": "table_transform-v2-pinned"},
                {"dimension": "key", "change": "vendor_code to supplier_id", "handled_by": "table_transform-v2-pinned"},
                {"dimension": "category", "change": "A/B to critical/standard", "handled_by": "table_transform-v2-pinned"},
                {"dimension": "join", "change": "owner join now uses integer supplier_id", "handled_by": "table_transform-v2-pinned"},
                {"dimension": "semantic", "change": "review means critical AND spend_usd >= 100000", "handled_by": "table_transform-v2-pinned"},
            ],
        },
        "structured_policy_memo_refresh": {
            "current_object": "memo-current-spec", "stale": "memo-stale-spec", "conflict": "memo-conflict", "revoked": "memo-revoked", "artifact": "memo-artifact-v1",
            "current_input": memo_input, "expected_output": memo_output,
            "compatibility_changes": [
                {"dimension": "unit", "change": "threshold and exposure normalized to USD", "handled_by": "memo_transform-v1-pinned"},
                {"dimension": "category", "change": "free-text recommendation to escalate/monitor decision", "handled_by": "memo_transform-v1-pinned"},
                {"dimension": "semantic", "change": "current policy-owner threshold outranks analyst advisory", "handled_by": "memo_transform-v1-pinned"},
            ],
        },
    }
    cells = []
    for shape, spec in shape_specs.items():
        for condition in CONDITIONS:
            ids = {
                "reset": [],
                "information_matched_full_history": [spec["current_object"], spec["stale"], spec["conflict"], spec["revoked"], spec["artifact"]],
                "curated_correct": [spec["current_object"], spec["artifact"]],
                "curated_stale": [spec["stale"], spec["artifact"]],
                "curated_conflicting": [spec["current_object"], spec["conflict"], spec["artifact"]],
                "curated_revoked": [spec["revoked"], spec["artifact"]],
                "deterministic_artifact_rerun": [spec["current_object"], spec["artifact"]],
            }[condition]
            execution_mode = "deterministic_artifact_rerun" if condition == "deterministic_artifact_rerun" else "agent_mediated_reuse"
            if condition == "curated_stale":
                disposition, reason = "rejected", "stale_authority"
            elif condition == "curated_conflicting":
                disposition, reason = "rejected", "unresolved_conflict"
            elif condition == "curated_revoked":
                disposition, reason = "rejected", "revoked_permission"
            elif condition == "deterministic_artifact_rerun":
                disposition, reason = "accepted", "pinned_transform_and_semantic_checks_passed"
            else:
                disposition, reason = "insufficient_evidence", "agent_trial_not_run_zero_call_preflight_only"
            visibility = "not_applicable" if execution_mode == "deterministic_artifact_rerun" else "not_observed"
            cell = {
                "cell_id": f"{shape}--{condition}", "work_shape": shape, "condition": condition,
                "execution_mode": execution_mode,
                "estimand": "deterministic_artifact_conformance" if execution_mode == "deterministic_artifact_rerun" else "agent_mediated_workspace_reuse",
                "matched_base": {"current_requirements_sha256": canonical_sha256(spec["current_object"]), "current_information_sha256": canonical_sha256(spec["current_input"]), "base_artifact_available": True, "budget": {"model_calls": 0, "wall_seconds": 5, "input_bytes": 10000}},
                "retained_object_ids": ids, "composition_sha256": composition_hash(ids, by_id),
                "observations": {"accessor_permission_checked": True, "model_visibility": visibility, "model_access": visibility, "model_adoption": visibility, "artifact_state_delta": "observed" if execution_mode == "deterministic_artifact_rerun" else "not_observed", "collateral_preservation": "passed" if execution_mode == "deterministic_artifact_rerun" else "not_observed"},
                "criterion": {"criterion_id": "safe-current-reuse", "disposition": disposition, "reason": reason, "evidence_object_ids": ids},
            }
            if execution_mode == "deterministic_artifact_rerun":
                cell["rerun"] = {"transform_id": spec["artifact"], "transform_sha256": by_id[spec["artifact"]]["sha256"], "input_sha256": canonical_sha256(spec["current_input"]), "output_sha256": canonical_sha256(spec["expected_output"]), "compatibility_dimensions": [item["dimension"] for item in spec["compatibility_changes"]]}
            cells.append(cell)
    package = {
        "package_id": "persistent-workspace-reuse-v1", "version": "1.0.0", "status": "internal_synthetic_zero_call_conformance_only",
        "design": {
            "charter_objectives": ["B", "C"], "mode": "building_and_validation",
            "general_hypothesis": "Typed authority, validity, composition, and semantic compatibility gates distinguish reusable workspace state from stale or revoked state, while deterministic artifact refresh remains a separate estimand from agent-mediated reuse.",
            "useful_completion": "Replay fourteen prospective cells across two artifact shapes and fail closed on stale, conflicting, revoked, semantically incompatible, or conflated evidence.",
            "source_review": "papers/agent-benchmarks/2026-07-16-shared-selective-persistent-memory-validity.md",
            "adjacent_pilot": "pilots/experience-memory-transfer/conformance.json",
            "persistent_workspace_fixture": "tests/fixtures/valid-persistent-workspace-conformance.json",
            "longitudinal_contract": "schemas/LONGITUDINAL_EVALUATION.md",
            "artifact_admissibility_fixture": "tests/fixtures/valid-artifact-admissibility-bundle.json",
        },
        "frozen_protocol": {"protocol_sha256": "", "evaluation_time": "2026-07-16T00:00:00Z", "conditions": list(CONDITIONS), "work_shapes": list(WORK_SHAPES), "base_matching_rule": "Within each work shape, current requirements, current information, base artifact availability, and budgets are identical; retained-object composition is the intended treatment.", "agent_trials": "not_run", "zero_call_first": True},
        "retained_objects": objects, "work_shape_specs": shape_specs, "cells": cells,
        "claim_limits": {"supported": ["The exact zero-call fixture replays its declared hashes, authority gates, compatibility migrations, and criterion dispositions."], "unsupported": sorted(UNSUPPORTED_CLAIMS)},
    }
    frozen = copy.deepcopy(package["frozen_protocol"])
    frozen.pop("protocol_sha256")
    package["frozen_protocol"]["protocol_sha256"] = canonical_sha256(frozen)
    return package


def semantic_errors(package: dict[str, Any], check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    if package.get("status") != "internal_synthetic_zero_call_conformance_only":
        errors.append("status must preserve zero-call synthetic scope")
    design = package.get("design", {})
    for key in ("source_review", "adjacent_pilot", "persistent_workspace_fixture", "longitudinal_contract", "artifact_admissibility_fixture"):
        if not design.get(key) or (check_paths and not (ROOT / design[key]).is_file()):
            errors.append(f"design.{key} must reference an existing repository file")
    protocol = package.get("frozen_protocol", {})
    frozen = copy.deepcopy(protocol)
    declared_protocol_hash = frozen.pop("protocol_sha256", None)
    if declared_protocol_hash != canonical_sha256(frozen): errors.append("frozen protocol hash mismatch")
    if tuple(protocol.get("conditions", [])) != CONDITIONS or tuple(protocol.get("work_shapes", [])) != WORK_SHAPES:
        errors.append("frozen treatment matrix coverage mismatch")
    if not protocol.get("zero_call_first") or protocol.get("agent_trials") != "not_run":
        errors.append("this slice must remain a zero-call preflight")
    objects = package.get("retained_objects", [])
    by_id = {item.get("object_id"): item for item in objects}
    if len(by_id) != len(objects): errors.append("retained object IDs must be unique")
    for item in objects:
        payload = {key: value for key, value in item.items() if key != "sha256"}
        if item.get("sha256") != canonical_sha256(payload): errors.append(f"retained object hash mismatch: {item.get('object_id')}")
        if item.get("state") == "revoked" and item.get("accessor_permission") != "revoked": errors.append("revoked object launders accessor permission")
    specs = package.get("work_shape_specs", {})
    dimensions = {change.get("dimension") for spec in specs.values() for change in spec.get("compatibility_changes", [])}
    if not {"type", "unit", "key", "category", "join", "semantic"} <= dimensions:
        errors.append("typed compatibility coverage is incomplete")
    cells = package.get("cells", [])
    expected_cells = {(shape, condition) for shape in WORK_SHAPES for condition in CONDITIONS}
    if {(cell.get("work_shape"), cell.get("condition")) for cell in cells} != expected_cells or len(cells) != len(expected_cells):
        errors.append("fourteen-cell work-shape/treatment coverage mismatch")
    base_by_shape: dict[str, set[str]] = {shape: set() for shape in WORK_SHAPES}
    for cell in cells:
        shape, condition = cell.get("work_shape"), cell.get("condition")
        ids = cell.get("retained_object_ids", [])
        if any(oid not in by_id for oid in ids): errors.append(f"{cell.get('cell_id')}: unknown retained object")
        elif cell.get("composition_sha256") != composition_hash(ids, by_id): errors.append(f"{cell.get('cell_id')}: composition hash mismatch")
        base_by_shape.setdefault(shape, set()).add(canonical_sha256(cell.get("matched_base")))
        criterion = cell.get("criterion", {})
        if not set(criterion.get("evidence_object_ids", [])) <= set(ids): errors.append(f"{cell.get('cell_id')}: missing observation links")
        expected = {"curated_stale": ("rejected", "stale_authority"), "curated_conflicting": ("rejected", "unresolved_conflict"), "curated_revoked": ("rejected", "revoked_permission")}.get(condition)
        if expected and (criterion.get("disposition"), criterion.get("reason")) != expected:
            errors.append(f"{cell.get('cell_id')}: unsafe authority disposition")
        mode = cell.get("execution_mode")
        estimand = cell.get("estimand")
        if condition == "deterministic_artifact_rerun":
            if mode != "deterministic_artifact_rerun" or estimand != "deterministic_artifact_conformance": errors.append(f"{cell.get('cell_id')}: rerun-as-agent conflation")
            rerun = cell.get("rerun", {})
            spec = specs.get(shape, {})
            actual = table_transform(spec.get("current_input", {})) if shape == WORK_SHAPES[0] else memo_transform(spec.get("current_input", {}))
            declared_dimensions = set(rerun.get("compatibility_dimensions", []))
            required_dimensions = {item.get("dimension") for item in spec.get("compatibility_changes", [])}
            if not required_dimensions <= declared_dimensions or "semantic" not in declared_dimensions:
                errors.append(f"{cell.get('cell_id')}: semantic incompatibility is not covered")
            if rerun.get("output_sha256") != canonical_sha256(actual) or actual != spec.get("expected_output"):
                errors.append(f"{cell.get('cell_id')}: deterministic output does not replay")
            artifact = by_id.get(spec.get("artifact"), {})
            if rerun.get("transform_sha256") != artifact.get("sha256"):
                errors.append(f"{cell.get('cell_id')}: transformation hash mismatch")
            if criterion.get("disposition") != "accepted": errors.append(f"{cell.get('cell_id')}: passing deterministic rerun must be accepted")
        elif mode != "agent_mediated_reuse" or estimand != "agent_mediated_workspace_reuse":
            errors.append(f"{cell.get('cell_id')}: execution-mode/estimand mismatch")
    for shape, hashes in base_by_shape.items():
        if len(hashes) != 1: errors.append(f"{shape}: matched base or budget drift")
    if not UNSUPPORTED_CLAIMS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("claim limits omit required non-claims")
    return errors


def replay(package: dict[str, Any]) -> dict[str, Any]:
    cells = {cell["cell_id"]: {"execution_mode": cell["execution_mode"], "estimand": cell["estimand"], "disposition": cell["criterion"]["disposition"], "reason": cell["criterion"]["reason"]} for cell in package["cells"]}
    return {
        "cell_count": len(cells), "cells": cells,
        "disposition_counts": {key: sum(cell["disposition"] == key for cell in cells.values()) for key in ("accepted", "rejected", "insufficient_evidence")},
        "agent_trials_run": 0, "model_calls": 0,
        "estimand_status": {"deterministic_artifact_conformance": "observed_exact_fixture_only", "agent_mediated_workspace_reuse": "not_estimated"},
    }


def validate_file(path: Path, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(path.read_text())
    errors = semantic_errors(package, check_paths)
    if errors: raise ValueError("\n".join(errors))
    return package


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--refresh", action="store_true", help="write the canonical generated package before validating")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.refresh:
        args.path.parent.mkdir(parents=True, exist_ok=True)
        args.path.write_text(json.dumps(build_package(), indent=2) + "\n")
    package = validate_file(args.path, args.check_paths)
    result = {"package_sha256": hashlib.sha256(args.path.read_bytes()).hexdigest(), "protocol_sha256": package["frozen_protocol"]["protocol_sha256"], **replay(package), "claim_scope": "exact deterministic synthetic zero-call fixture only"}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
