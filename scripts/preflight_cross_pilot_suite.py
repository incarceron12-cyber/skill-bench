#!/usr/bin/env python3
"""Fail-closed, zero-call cross-pilot suite assembly preflight.

This runner inventories immutable parent packages, executes only declared local
validators/graders/exact replays, and assembles internal conformance evidence.
It never launches an agent and never upgrades parent claim ceilings.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_COMMAND_KINDS = {"validator", "grader_replay", "exact_replay"}
ALLOWED_DECISIONS = {"admitted_internal_conformance", "excluded"}
PROHIBITED_CLAIMS = {
    "cross_domain_coverage", "capability", "expert_validity",
    "professional_validity", "safety", "privacy", "production_fitness",
    "public_release", "readiness",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic_errors(manifest: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "suite_id", "purpose", "candidate_pool", "assembly",
        "public_private_boundary", "missing_invalid_policy", "pooled_claims",
        "limitations",
    }
    missing = required - set(manifest)
    if missing:
        return [f"missing top-level fields: {sorted(missing)}"]

    candidates = manifest.get("candidate_pool", [])
    if not isinstance(candidates, list) or len(candidates) < 3:
        errors.append("candidate_pool must contain at least three components")
        return errors
    ids = [item.get("component_id") for item in candidates if isinstance(item, dict)]
    if len(ids) != len(set(ids)) or any(not item for item in ids):
        errors.append("component_ids must be present and unique")
    by_id = {item.get("component_id"): item for item in candidates if isinstance(item, dict)}

    for component_id, item in by_id.items():
        for key in (
            "construct", "unit_of_work", "work_shape", "artifact_types",
            "lineage_clusters", "configured_system_eligibility", "evidence_boundary",
            "artifacts", "commands", "health", "substantive_evidence_eligible",
            "claim_ceiling",
        ):
            if key not in item:
                errors.append(f"{component_id}: missing {key}")
        if not item.get("lineage_clusters"):
            errors.append(f"{component_id}: at least one lineage cluster is required")
        if item.get("substantive_evidence_eligible") and item.get("service_evidence") != "service_valid":
            errors.append(f"{component_id}: invalid/service-failed evidence admitted as substantive")
        ceiling = item.get("claim_ceiling", {})
        if set(ceiling) != PROHIBITED_CLAIMS or any(ceiling.values()):
            errors.append(f"{component_id}: claim ceiling must explicitly keep all prohibited claims false")
        for artifact in item.get("artifacts", []):
            path_text = artifact.get("path")
            if not path_text or not artifact.get("sha256") or not artifact.get("git_blob"):
                errors.append(f"{component_id}: artifact requires path, sha256, and git_blob")
                continue
            if check_paths:
                path = ROOT / path_text
                if not path.is_file():
                    errors.append(f"{component_id}: missing parent artifact {path_text}")
                    continue
                if sha256(path) != artifact["sha256"]:
                    errors.append(f"{component_id}: stale sha256 for {path_text}")
                blob = subprocess.run(
                    ["git", "hash-object", path_text], cwd=ROOT,
                    capture_output=True, text=True,
                )
                if blob.returncode or blob.stdout.strip() != artifact["git_blob"]:
                    errors.append(f"{component_id}: git/blob identity mismatch for {path_text}")
                head = subprocess.run(
                    ["git", "rev-parse", f"HEAD:{path_text}"], cwd=ROOT,
                    capture_output=True, text=True,
                )
                if head.returncode or head.stdout.strip() != artifact["git_blob"]:
                    errors.append(f"{component_id}: parent is absent or differs at HEAD: {path_text}")
        commands = item.get("commands", [])
        if not commands:
            errors.append(f"{component_id}: at least one command is required")
        for command in commands:
            if command.get("kind") not in ALLOWED_COMMAND_KINDS:
                errors.append(f"{component_id}: command kind is not allowlisted")
            if command.get("zero_cost") is not True or command.get("expected_exit") != 0:
                errors.append(f"{component_id}: commands must be zero-cost and expect exit 0")
            argv = command.get("argv", [])
            rendered = " ".join(str(part) for part in argv)
            if not argv or any(token in rendered for token in (" hermes ", "--provider", "--model", "execute_study.py execute")):
                errors.append(f"{component_id}: command could launch an agent or is empty")
            check = command.get("result_check", {})
            if check.get("type") not in {"exit_only", "exact_json", "workspace_replay"}:
                errors.append(f"{component_id}: command result_check is not fail-closed")

    assembly = manifest.get("assembly", {})
    dispositions = assembly.get("dispositions", [])
    disposition_ids = [item.get("component_id") for item in dispositions if isinstance(item, dict)]
    if set(disposition_ids) != set(by_id) or len(disposition_ids) != len(set(disposition_ids)):
        errors.append("every candidate must have exactly one explicit disposition; silent exclusion is forbidden")
    admitted = []
    for disposition in dispositions:
        component_id = disposition.get("component_id")
        if disposition.get("decision") not in ALLOWED_DECISIONS or not disposition.get("reason"):
            errors.append(f"{component_id}: invalid or unexplained disposition")
        if disposition.get("decision") == "admitted_internal_conformance":
            admitted.append(component_id)
    intended = assembly.get("intended_mixture", {}).get("work_shapes", {})
    realized: dict[str, int] = {}
    for component_id in admitted:
        if component_id in by_id:
            shape = by_id[component_id].get("work_shape")
            if isinstance(shape, str) and shape:
                realized[shape] = realized.get(shape, 0) + 1
            else:
                errors.append(f"{component_id}: work_shape must be a non-empty string")
    if intended != realized:
        errors.append(f"mixture mismatch: intended {intended}, realized {realized}")

    for left_index, left_id in enumerate(admitted):
        left = by_id.get(left_id, {})
        if not left.get("presented_as_independent", False):
            continue
        for right_id in admitted[left_index + 1:]:
            right = by_id.get(right_id, {})
            if right.get("presented_as_independent", False) and set(left.get("lineage_clusters", [])) & set(right.get("lineage_clusters", [])):
                errors.append(f"duplicate lineage presented as independent: {left_id}, {right_id}")

    sensitivity = assembly.get("alternate_assembly_sensitivity", {})
    claims = manifest.get("pooled_claims", {})
    for claim in PROHIBITED_CLAIMS:
        if claims.get(claim) not in {"unsupported", "blocked"}:
            errors.append(f"pooled claim upgrade forbidden: {claim}")
    if any(status not in {"unsupported", "blocked"} for status in claims.values()):
        errors.append("pooled claim upgrade forbidden")
    if sensitivity.get("required") is not True or sensitivity.get("method") != "leave_one_component_out":
        errors.append("pooled assembly requires declared leave-one-component-out sensitivity")
    if assembly.get("dependence", {}).get("unresolved") is None:
        errors.append("dependence.unresolved must be explicit")
    return errors


def check_command_result(command: dict[str, Any], result: subprocess.CompletedProcess[str]) -> tuple[bool, str]:
    if result.returncode != command["expected_exit"]:
        return False, f"exit {result.returncode}, expected {command['expected_exit']}"
    check = command["result_check"]
    kind = check["type"]
    if kind == "exit_only":
        return True, "declared validator exited 0"
    try:
        observed = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return False, f"stdout is not JSON: {exc}"
    if kind == "exact_json":
        expected_path = ROOT / check["expected_path"]
        if not expected_path.is_file():
            return False, f"missing expected replay file {check['expected_path']}"
        if observed != load(expected_path):
            return False, "grader stdout differs from retained report"
        return True, "grader output exactly matches retained report"
    if observed.get("passed") is not True:
        return False, "workspace replay did not report passed=true"
    report = load(ROOT / check["report_path"])
    protocol = load(ROOT / check["protocol_path"])
    denom = report.get("strict_denominators", {})
    intended = denom.get("intended")
    if intended != 24 or any(denom.get(key) != intended for key in ("attempted_once", "service_valid", "environment_valid", "substantively_graded")):
        return False, "workspace replay retains missing, service-invalid, environment-invalid, or ungraded cells"
    if any(protocol.get("claim_boundaries", {}).values()):
        return False, "workspace protocol claim ceiling upgraded"
    return True, "exact replay passed with all 24 intended cells retained and valid"


def run_preflight(manifest_path: Path) -> dict[str, Any]:
    manifest = load(manifest_path)
    errors = semantic_errors(manifest, check_paths=True)
    command_records = []
    if not errors:
        by_id = {item["component_id"]: item for item in manifest["candidate_pool"]}
        for disposition in manifest["assembly"]["dispositions"]:
            component = by_id[disposition["component_id"]]
            for command in component["commands"]:
                result = subprocess.run(
                    command["argv"], cwd=ROOT, capture_output=True, text=True,
                    timeout=command.get("timeout_seconds", 120),
                )
                passed, detail = check_command_result(command, result)
                command_records.append({
                    "component_id": component["component_id"],
                    "command_id": command["command_id"],
                    "kind": command["kind"],
                    "argv": command["argv"],
                    "exit_status": result.returncode,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "passed": passed,
                    "detail": detail,
                })
                if not passed:
                    errors.append(f"{component['component_id']}/{command['command_id']}: {detail}")

    dispositions = manifest.get("assembly", {}).get("dispositions", [])
    admitted = [item["component_id"] for item in dispositions if item.get("decision") == "admitted_internal_conformance"]
    by_id = {item.get("component_id"): item for item in manifest.get("candidate_pool", [])}
    leave_one_out = []
    for omitted in admitted:
        remaining = [item for item in admitted if item != omitted]
        mixture: dict[str, int] = {}
        for item in remaining:
            shape = by_id[item]["work_shape"]
            mixture[shape] = mixture.get(shape, 0) + 1
        leave_one_out.append({
            "omitted_component_id": omitted,
            "remaining_components": remaining,
            "realized_work_shapes": mixture,
            "pooled_claim_status_unchanged": all(value in {"unsupported", "blocked"} for value in manifest.get("pooled_claims", {}).values()),
        })
    components = []
    command_by_component: dict[str, list[dict[str, Any]]] = {}
    for record in command_records:
        command_by_component.setdefault(record["component_id"], []).append(record)
    dispositions_by_id = {item.get("component_id"): item for item in dispositions}
    for component_id, component in by_id.items():
        records = command_by_component.get(component_id, [])
        components.append({
            "component_id": component_id,
            "hash_integrity": not any(component_id in error and ("sha256" in error or "blob" in error or "parent" in error) for error in errors),
            "task_health": component.get("health", {}).get("task"),
            "grader_health": component.get("health", {}).get("grader"),
            "service_evidence": component.get("service_evidence"),
            "substantive_evidence_eligible": component.get("substantive_evidence_eligible"),
            "disposition": dispositions_by_id.get(component_id),
            "commands_passed": bool(records) and all(record["passed"] for record in records),
        })
    return {
        "report_version": "0.1.0",
        "suite_id": manifest.get("suite_id"),
        "manifest": {"path": manifest_path.relative_to(ROOT).as_posix(), "sha256": sha256(manifest_path)},
        "status": "passed_internal_conformance" if not errors else "failed_closed",
        "passed": not errors,
        "errors": errors,
        "components": components,
        "command_results": command_records,
        "realized_mixture": manifest.get("assembly", {}).get("intended_mixture", {}).get("work_shapes", {}) if not errors else {},
        "dependence": manifest.get("assembly", {}).get("dependence"),
        "alternate_assembly_sensitivity": {"method": "leave_one_component_out", "results": leave_one_out},
        "pooled_claims": manifest.get("pooled_claims"),
        "report_claim_boundary": "Internal deterministic composability only; no cross-domain coverage, capability, expert/professional validity, safety, privacy, production, public-release, or readiness claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.validate_only:
        manifest = load(args.manifest)
        errors = semantic_errors(manifest, check_paths=True)
        report = {"passed": not errors, "errors": errors}
    else:
        report = run_preflight(args.manifest.resolve())
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
