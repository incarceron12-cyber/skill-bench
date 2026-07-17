#!/usr/bin/env python3
"""Deterministically replay the disposition/realization crosswalk (zero model calls)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
DIMENSIONS = [
    "boundary_judgment",
    "proceed_realization",
    "handoff_construction",
    "handoff_transport",
    "continuation",
    "consequence",
    "observer_sufficiency",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pointer(document: Any, locator: str) -> Any:
    if locator == "":
        return document
    if not locator.startswith("/"):
        raise ValueError(f"invalid JSON Pointer: {locator!r}")
    value = document
    for raw in locator[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            value = value[int(token)]
        else:
            value = value[token]
    return value


def load_evidence(manifest: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    documents: dict[str, Any] = {}
    verification: list[dict[str, Any]] = []
    for ref, spec in manifest["evidence"].items():
        path = ROOT / spec["path"]
        actual = sha256(path) if path.is_file() else None
        passed = actual == spec["sha256"]
        verification.append(
            {
                "ref": ref,
                "path": spec["path"],
                "expected_sha256": spec["sha256"],
                "actual_sha256": actual,
                "passed": passed,
            }
        )
        if passed and path.suffix == ".json":
            documents[ref] = json.loads(path.read_text())
    return documents, verification


def operand(value: dict[str, Any], documents: dict[str, Any]) -> Any:
    if "literal" in value:
        return value["literal"]
    return pointer(documents[value["ref"]], value["pointer"])


def evaluate(assertion: dict[str, Any], documents: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    op = assertion["op"]
    result = {
        "id": assertion["id"],
        "dimension": assertion["dimension"],
        "op": op,
    }
    if op == "unsupported":
        result.update(status="insufficient_evidence", reason=assertion["reason"])
        return result
    if op == "not_applicable":
        result.update(status="not_applicable", reason=assertion["reason"])
        return result
    if op == "equal":
        left = operand(assertion["left"], documents)
        right = operand(assertion["right"], documents)
        observed = left == right
    elif op == "hash_equal":
        left = evidence[assertion["left_ref"]]["sha256"]
        right = evidence[assertion["right_ref"]]["sha256"]
        observed = left == right
    else:
        raise ValueError(f"unsupported operation {op!r}")
    expected = assertion.get("expect", True)
    result.update(status="pass" if observed == expected else "fail", observed=observed, expected=expected)
    return result


def aggregate(results: list[dict[str, Any]]) -> str:
    statuses = {item["status"] for item in results}
    if "fail" in statuses:
        return "fail"
    if "insufficient_evidence" in statuses:
        return "insufficient_evidence"
    if statuses == {"not_applicable"}:
        return "not_applicable"
    return "pass"


def replay(manifest_path: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text())
    documents, evidence_verification = load_evidence(manifest)
    evidence_ok = all(item["passed"] for item in evidence_verification)
    required = set(manifest["matrix"]["required_cells"])
    observed = {case["id"] for case in manifest["cases"]}
    shapes = {case["shape"] for case in manifest["cases"]}
    cases = []
    for case in manifest["cases"]:
        assertion_results = [
            evaluate(item, documents, manifest["evidence"])
            for item in case["assertions"]
        ] if evidence_ok else []
        dimensions = {
            dimension: aggregate([r for r in assertion_results if r["dimension"] == dimension])
            for dimension in DIMENSIONS
        }
        cases.append(
            {
                "id": case["id"],
                "shape": case["shape"],
                "boundary": case["boundary"],
                "realization": case["realization"],
                "control": case["control"],
                "dimensions": dimensions,
                "assertions": assertion_results,
            }
        )
    errors = []
    if not evidence_ok:
        errors.append("one or more immutable parent hashes failed")
    if observed != required:
        errors.append(f"matrix mismatch: required={sorted(required)} observed={sorted(observed)}")
    if len(shapes) < 2:
        errors.append("fewer than two knowledge-work shapes")
    for case in cases:
        if set(case["dimensions"]) != set(DIMENSIONS):
            errors.append(f"dimension inventory mismatch in {case['id']}")
    return {
        "kind": "disposition_realization_crosswalk_v1_replay",
        "manifest_path": str(manifest_path.relative_to(ROOT)),
        "manifest_sha256": sha256(manifest_path),
        "model_calls": 0,
        "parent_files_modified": False,
        "evidence_verification": evidence_verification,
        "matrix": {
            "required_cells": sorted(required),
            "observed_cells": sorted(observed),
            "complete": observed == required,
            "shape_count": len(shapes),
            "shapes": sorted(shapes),
        },
        "cases": cases,
        "claim_boundaries": manifest["claim_boundaries"],
        "errors": errors,
        "passed": not errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=HERE / "manifest.json")
    parser.add_argument("--output", type=Path, default=HERE / "replay-report.json")
    parser.add_argument("--check", action="store_true", help="Compare generated bytes to the existing report.")
    args = parser.parse_args()
    report = replay(args.manifest.resolve())
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not args.output.is_file() or args.output.read_text() != rendered:
            print("replay report is missing or stale")
            return 1
    else:
        args.output.write_text(rendered)
    print(json.dumps({"passed": report["passed"], "model_calls": 0, "cases": len(report["cases"]), "errors": report["errors"]}))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
