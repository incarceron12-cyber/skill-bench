#!/usr/bin/env python3
"""Compute fixed-denominator outcome-evidence bounds for synthetic records."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
DEFAULT = Path(__file__).with_name("conformance.json")
DENIED = {"agent capability", "expert validity", "professional readiness", "population ranking"}
VALID_NATIVE = {"success", "failure"}
VALID_EVIDENCE = {"supported", "contradicted", "insufficient_evidence"}


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def classify(record: dict[str, Any]) -> str:
    """Return P/F/U without mutating the released evaluator label."""
    if record["evidence_state"] == "insufficient_evidence":
        return "U"
    if record["evidence_state"] == "supported":
        return "P" if record["native_label"] == "success" else "F"
    # A decisive contradiction supports the opposite outcome and remains a conflict.
    return "F" if record["native_label"] == "success" else "P"


def aggregate(records: list[dict[str, Any]]) -> dict[str, Any]:
    excluded = [r for r in records if r["inclusion"]["status"] == "excluded"]
    included = [r for r in records if r["inclusion"]["status"] == "included"]
    counts = {k: 0 for k in "PFU"}
    for record in included:
        counts[classify(record)] += 1
    n = len(included)
    if not n:
        raise ValueError("fixed valid-start denominator must be nonzero")
    lower, upper = Fraction(counts["P"], n), Fraction(counts["P"] + counts["U"], n)
    return {
        "N": n, "P": counts["P"], "F": counts["F"], "U": counts["U"],
        "bounds": {"lower": float(lower), "upper": float(upper), "exact": [str(lower), str(upper)]},
        "unknown_share": float(Fraction(counts["U"], n)),
        "excluded": [{"record_id": r["id"], "reason": r["inclusion"]["reason"]} for r in excluded],
    }


def replay(data: dict[str, Any], check_paths: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    if data.get("status") != "internal_synthetic_calibration_only":
        errors.append("status must remain internal synthetic calibration only")
    if not DENIED <= set(data.get("claim_limits", {}).get("unsupported", [])):
        errors.append("claim limits omit required non-claims")
    records = data.get("records", [])
    if canonical_hash(records) != data.get("locked_records_sha256"):
        errors.append("locked record hash mismatch")
    ids = [r.get("id") for r in records]
    if len(ids) != len(set(ids)):
        errors.append("record ids must be unique")
    for r in records:
        if r.get("native_label") not in VALID_NATIVE or r.get("evidence_state") not in VALID_EVIDENCE:
            errors.append(f"{r.get('id')}: invalid native/evidence state")
        inclusion = r.get("inclusion", {})
        if inclusion.get("status") == "excluded" and inclusion.get("cause") != "proven_pre_run_environment_invalidity":
            errors.append(f"{r.get('id')}: only proven pre-run invalidity may be excluded")
        if inclusion.get("status") == "included" and inclusion.get("cause") == "proven_pre_run_environment_invalidity":
            errors.append(f"{r.get('id')}: proven pre-run invalidity must be excluded")
        if r.get("stronger_condition") not in {"pass", "fail", "not_applicable", "insufficient_evidence"}:
            errors.append(f"{r.get('id')}: invalid stronger condition")
    cells: dict[str, dict[str, Any]] = {}
    for cell in data.get("cells", []):
        selected = [r for r in records if r["cell_id"] == cell["id"]]
        try: observed = aggregate(selected)
        except ValueError as exc: errors.append(f"{cell['id']}: {exc}"); continue
        cells[cell["id"]] = observed
        if observed != cell.get("expected"):
            errors.append(f"{cell['id']}: aggregate mismatch")
    comparisons = []
    for spec in data.get("comparisons", []):
        left, right = cells.get(spec["left"]), cells.get(spec["right"])
        if not left or not right: continue
        if left["bounds"]["lower"] > right["bounds"]["upper"]: result = "left_direction_supported"
        elif right["bounds"]["lower"] > left["bounds"]["upper"]: result = "right_direction_supported"
        else: result = "unresolved_overlapping_identification_intervals"
        comparisons.append({"id": spec["id"], "result": result})
        if result != spec["expected"]: errors.append(f"{spec['id']}: comparison mismatch")
    if check_paths:
        for source in data.get("design_basis", {}).values():
            path = ROOT / source["path"]
            if not path.is_file(): errors.append(f"missing provenance path: {source['path']}"); continue
            if source.get("sha256") and hashlib.sha256(path.read_bytes()).hexdigest() != source["sha256"]:
                errors.append(f"provenance hash mismatch: {source['path']}")
    preserved = [{k: r[k] for k in ("id", "cell_id", "native_label", "evidence_state", "benchmark_conflict", "stronger_condition")} | {"classification": None if r["inclusion"]["status"] == "excluded" else classify(r)} for r in records]
    return {"valid": not errors, "errors": errors, "locked_records_sha256": data.get("locked_records_sha256"), "cells": cells, "comparisons": comparisons, "records": preserved}


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("path", nargs="?", type=Path, default=DEFAULT); parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args(); report = replay(json.loads(args.path.read_text()), args.check_paths); print(json.dumps(report, indent=2)); return 0 if report["valid"] else 1
if __name__ == "__main__": raise SystemExit(main())
