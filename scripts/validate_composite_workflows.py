#!/usr/bin/env python3
"""Validate the internal composite-workflow conformance slice."""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "pilots/composite-workflow-conformance/workflows.json"
REQUIRED_LIMITS = {"agent capability", "professional validity", "expert approval", "occupational realism", "causal planning burden", "release readiness"}


def _hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(workflow: dict[str, Any], poll_order: list[str]) -> dict[str, Any]:
    nodes = {node["id"]: node for node in workflow["nodes"]}
    latest = {node_id: False for node_id in nodes}
    milestones: set[str] = set()
    for event in sorted(workflow["events"], key=lambda item: item["sequence"]):
        latest[event["node"]] = event["state"]
        if event["state"]:
            milestones.add(event["node"])

    # Polling only changes observation order. Credit is recomputed from terminal
    # state and dependencies, so an earlier true milestone cannot survive reversal.
    supported: dict[str, bool] = {}
    for node_id in poll_order:
        node = nodes[node_id]
        supported[node_id] = latest[node_id] and all(supported.get(dep, latest[dep]) for dep in node["depends_on"])

    # Diagnose in declared topological order, independent of poll order.
    canonical_supported: dict[str, bool] = {}
    earliest = None
    for node in workflow["nodes"]:
        ok = latest[node["id"]] and all(canonical_supported[dep] for dep in node["depends_on"])
        canonical_supported[node["id"]] = ok
        if earliest is None and not ok:
            earliest = node["id"]
    product = Decimal("1")
    for node in workflow["nodes"]:
        product *= Decimal(node["atomic_success"])
    return {
        "poll_order": poll_order,
        "milestones_observed": sorted(milestones),
        "terminal_node_support": canonical_supported,
        "terminal_success": all(canonical_supported.values()),
        "earliest_unsupported_dependency": earliest,
        "independent_composite_success": format(product, ".4f"),
    }


def validate(path: Path = DEFAULT_FIXTURE, check_paths: bool = False) -> dict[str, Any]:
    package = json.loads(path.read_text())
    errors: list[str] = []
    if package.get("status") != "internal_calibration_only":
        errors.append("status must remain internal_calibration_only")
    if not REQUIRED_LIMITS <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("required synthetic-fixture claim limits are missing")
    if len({workflow.get("work_shape") for workflow in package.get("workflows", [])}) < 2:
        errors.append("two unlike work shapes are required")

    results = []
    for workflow in package.get("workflows", []):
        nodes = workflow.get("nodes", [])
        ids = [node.get("id") for node in nodes]
        if len(ids) != len(set(ids)) or not ids:
            errors.append(f"{workflow.get('id')}: node ids must be unique and nonempty")
            continue
        seen: set[str] = set()
        for node in nodes:
            if any(dep not in seen for dep in node.get("depends_on", [])):
                errors.append(f"{workflow['id']}:{node['id']}: dependencies must form a declared topological DAG")
            seen.add(node["id"])
            if not node.get("produces") or not node.get("consumes") or not node.get("equivalent_paths"):
                errors.append(f"{workflow['id']}:{node['id']}: state and equivalent paths are required")
        if not any(event.get("reversal") for event in workflow.get("events", [])) and workflow["id"] == "approval-ledger":
            errors.append("approval-ledger: planted reversal is required")
        for event in workflow.get("events", []):
            if event.get("node") not in ids or event.get("path") not in next(n for n in nodes if n["id"] == event.get("node"))["equivalent_paths"]:
                errors.append(f"{workflow['id']}: event uses unknown node or undeclared path")
        attestation = workflow.get("reset_attestation", {})
        if attestation.get("before_fingerprint") != attestation.get("after_fingerprint") or attestation.get("collision_test") != "passed":
            errors.append(f"{workflow['id']}: reset attestation does not restore the fingerprint")
        if set(attestation.get("enumerated_side_effects", [])) != set(attestation.get("teardown_outcomes", {})):
            errors.append(f"{workflow['id']}: reset side-effect ledger is incomplete")

        run_results = [evaluate(workflow, order) for order in workflow.get("poll_orders", [])]
        if len(run_results) < 2 or any(set(result["poll_order"]) != set(ids) for result in run_results):
            errors.append(f"{workflow['id']}: at least two complete poll orders are required")
        signatures = {(r["terminal_success"], r["earliest_unsupported_dependency"]) for r in run_results}
        if len(signatures) != 1:
            errors.append(f"{workflow['id']}: terminal result depends on polling order")
        expected = workflow["expected"]
        for result in run_results:
            for field in ("terminal_success", "earliest_unsupported_dependency", "independent_composite_success"):
                if result[field] != expected[field]:
                    errors.append(f"{workflow['id']}: {field} got {result[field]!r}, expected {expected[field]!r}")
        results.append({"workflow_id": workflow["id"], "runs": run_results})

    if check_paths:
        for item in package.get("provenance", []):
            candidate = ROOT / item["path"]
            if not candidate.is_file():
                errors.append(f"missing provenance path: {item['path']}")
            elif _hash(candidate) != item["sha256"]:
                errors.append(f"hash mismatch: {item['path']}")
    return {"valid": not errors, "errors": errors, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    report = validate(args.path, args.check_paths)
    print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
