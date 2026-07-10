#!/usr/bin/env python3
"""Fail-closed cross-record evidence-chain audit.

This intentionally composes existing records rather than introducing an ECBD
schema. It verifies immutable artifact references and JSON Pointers, requires a
complete intended-use-to-validity chain with edge-level warrants, and prevents
claims from being upgraded across unsupported links or explicit blockers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
STAGES = (
    "intended_use",
    "construct_or_criterion",
    "requirement_or_item_affordance",
    "response_evidence_view",
    "grader_observation_or_check",
    "metric",
    "validity_claim",
)
SUPPORT = {"supported", "provisional", "unsupported", "unknown", "contradicted"}
CLAIM_SUPPORT = {"supported", "provisional", "unsupported", "unknown", "contradicted", "blocked"}


class AuditFailure(Exception):
    """Raised when an audit has broken references or licenses an invalid claim."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    repeated: set[str] = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return repeated


def resolve_pointer(document: Any, pointer: str) -> Any:
    """Resolve an RFC 6901 JSON Pointer, failing rather than guessing."""
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise KeyError("JSON Pointer must be empty or start with '/'")
    current = document
    for raw in pointer[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, list):
            current = current[int(token)]
        elif isinstance(current, dict):
            current = current[token]
        else:
            raise KeyError(f"cannot descend through {type(current).__name__}")
    return current


def semantic_errors(audit: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    required_top = {"audit_version", "audit_id", "purpose", "artifacts", "nodes", "edges", "suite_assembly", "claims", "audit_limits"}
    missing_top = required_top - set(audit)
    if missing_top:
        return [f"missing top-level fields: {sorted(missing_top)}"]

    artifacts_list = audit.get("artifacts", [])
    nodes_list = audit.get("nodes", [])
    edges_list = audit.get("edges", [])
    claims_list = audit.get("claims", [])
    for values, key, label in (
        (artifacts_list, "artifact_id", "artifact"),
        (nodes_list, "node_id", "node"),
        (edges_list, "edge_id", "edge"),
        (claims_list, "claim_id", "claim"),
    ):
        if not isinstance(values, list):
            errors.append(f"{label}s must be a list")
            continue
        for duplicate in sorted(_duplicates(item.get(key, "") for item in values if isinstance(item, dict))):
            errors.append(f"duplicate {label} id {duplicate!r}")

    artifacts = {item.get("artifact_id"): item for item in artifacts_list if isinstance(item, dict)}
    loaded: dict[str, Any] = {}
    for artifact_id, artifact in artifacts.items():
        if not artifact_id or not artifact.get("path") or not artifact.get("sha256"):
            errors.append(f"artifact {artifact_id!r}: artifact_id, path, and sha256 are required")
            continue
        path = ROOT / artifact["path"]
        if check_paths:
            if not path.is_file():
                errors.append(f"artifact {artifact_id}: path does not exist: {artifact['path']}")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != artifact["sha256"]:
                errors.append(f"artifact {artifact_id}: sha256 does not match {artifact['path']}")
        if path.is_file() and path.suffix == ".json":
            try:
                loaded[artifact_id] = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"artifact {artifact_id}: cannot load JSON: {exc}")

    def check_locator(owner: str, locator: Any) -> None:
        if not isinstance(locator, dict):
            errors.append(f"{owner}: locator must be an object")
            return
        artifact_id = locator.get("artifact_id")
        pointer = locator.get("pointer")
        if artifact_id not in artifacts:
            errors.append(f"{owner}: unknown artifact_id {artifact_id!r}")
            return
        if not isinstance(pointer, str):
            errors.append(f"{owner}: pointer must be a JSON Pointer string")
            return
        if artifact_id not in loaded:
            errors.append(f"{owner}: locators require a JSON artifact, got {artifact_id!r}")
            return
        try:
            resolve_pointer(loaded[artifact_id], pointer)
        except (KeyError, IndexError, ValueError, TypeError) as exc:
            errors.append(f"{owner}: unresolved pointer {artifact_id}{pointer}: {exc}")

    nodes = {item.get("node_id"): item for item in nodes_list if isinstance(item, dict)}
    stages = [item.get("stage") for item in nodes_list if isinstance(item, dict)]
    if stages != list(STAGES):
        errors.append(f"nodes must contain the seven ordered stages exactly once: {list(STAGES)}")
    for node_id, node in nodes.items():
        if not node_id or not node.get("label") or not node.get("scope"):
            errors.append(f"node {node_id!r}: node_id, label, and scope are required")
        check_locator(f"node {node_id}", node.get("record_ref"))

    edges = {item.get("edge_id"): item for item in edges_list if isinstance(item, dict)}
    if len(edges_list) != len(STAGES) - 1:
        errors.append("the primary evidence chain must contain exactly six adjacent edges")
    for index, edge in enumerate(edges_list):
        edge_id = edge.get("edge_id", f"index-{index}")
        expected_from = nodes_list[index].get("node_id") if index < len(nodes_list) else None
        expected_to = nodes_list[index + 1].get("node_id") if index + 1 < len(nodes_list) else None
        if edge.get("from_node") != expected_from or edge.get("to_node") != expected_to:
            errors.append(f"edge {edge_id}: must connect adjacent ordered stages")
        if edge.get("from_node") not in nodes or edge.get("to_node") not in nodes:
            errors.append(f"edge {edge_id}: unknown endpoint")
        status = edge.get("support_status")
        if status not in SUPPORT:
            errors.append(f"edge {edge_id}: invalid support_status {status!r}")
        if not str(edge.get("warrant", "")).strip():
            errors.append(f"edge {edge_id}: warrant is required")
        if not str(edge.get("scope", "")).strip():
            errors.append(f"edge {edge_id}: scope is required")
        if not str(edge.get("claim_consequence", "")).strip():
            errors.append(f"edge {edge_id}: claim_consequence is required")
        evidence = edge.get("evidence_locators", [])
        counterevidence = edge.get("counterevidence_locators", [])
        if not isinstance(evidence, list) or not isinstance(counterevidence, list):
            errors.append(f"edge {edge_id}: evidence and counterevidence locators must be lists")
            continue
        for position, locator in enumerate(evidence):
            check_locator(f"edge {edge_id} evidence[{position}]", locator)
        for position, locator in enumerate(counterevidence):
            check_locator(f"edge {edge_id} counterevidence[{position}]", locator)
        if status == "supported" and not evidence:
            errors.append(f"edge {edge_id}: supported edge requires evidence")
        if status == "supported" and counterevidence:
            errors.append(f"edge {edge_id}: supported edge cannot retain unresolved counterevidence")

    assembly = audit.get("suite_assembly", {})
    required_assembly = {
        "eligible_pool", "exclusions", "lineage_clusters", "intended_mixture", "realized_mixture",
        "selection_seed", "evidence_precision_target", "dependence", "missing_invalid_policy",
        "alternate_assembly_sensitivity", "suite_sufficiency",
    }
    missing_assembly = required_assembly - set(assembly) if isinstance(assembly, dict) else required_assembly
    if missing_assembly:
        errors.append(f"suite_assembly missing fields: {sorted(missing_assembly)}")
    elif assembly["suite_sufficiency"].get("status") not in CLAIM_SUPPORT:
        errors.append("suite_assembly.suite_sufficiency has invalid status")
    else:
        sensitivity = assembly["alternate_assembly_sensitivity"]
        sufficiency = assembly["suite_sufficiency"]
        if sufficiency.get("status") in {"supported", "provisional"}:
            if len(assembly.get("eligible_pool", [])) < 2:
                errors.append("suite sufficiency cannot be upgraded from a one-task eligible pool")
            if sensitivity.get("status") != "supported":
                errors.append("suite sufficiency requires supported alternate-assembly sensitivity")
            if assembly.get("dependence", {}).get("unresolved"):
                errors.append("suite sufficiency cannot be upgraded with unresolved dependence")

    edge_ids = set(edges)
    for claim in claims_list:
        claim_id = claim.get("claim_id", "<missing>")
        status = claim.get("status")
        if status not in CLAIM_SUPPORT:
            errors.append(f"claim {claim_id}: invalid status {status!r}")
        required_edges = claim.get("required_edge_ids", [])
        unknown = set(required_edges) - edge_ids
        if unknown:
            errors.append(f"claim {claim_id}: unknown required edges {sorted(unknown)}")
        if not str(claim.get("scope", "")).strip() or not claim.get("prohibited_interpretations"):
            errors.append(f"claim {claim_id}: scope and prohibited_interpretations are required")
        for position, blocker in enumerate(claim.get("blockers", [])):
            check_locator(f"claim {claim_id} blocker[{position}]", blocker)
        if status in {"supported", "provisional"}:
            bad_edges = [edge_id for edge_id in required_edges if edges.get(edge_id, {}).get("support_status") != "supported"]
            if bad_edges:
                errors.append(f"claim {claim_id}: unsupported claim upgrade across edges {bad_edges}")
            if claim.get("blockers"):
                errors.append(f"claim {claim_id}: supported/provisional claim retains explicit blockers")

    return errors


def validate_file(path: Path, *, check_paths: bool = False) -> None:
    audit = json.loads(path.read_text(encoding="utf-8"))
    errors = semantic_errors(audit, check_paths=check_paths)
    if errors:
        raise AuditFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audits", nargs="+", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for path in args.audits:
        try:
            validate_file(path, check_paths=args.check_paths)
            print(f"VALID {path}")
        except (OSError, json.JSONDecodeError, AuditFailure) as exc:
            failed = True
            print(f"INVALID {path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
