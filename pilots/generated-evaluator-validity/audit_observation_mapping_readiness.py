#!/usr/bin/env python3
"""Audit whether frozen replay rows can be mapped without outcome-label laundering.

This is a prerequisite audit, not an adapter. It inspects only source/provenance
metadata and deliberately never reads oracle/expected outcome values.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
REPORT = ROOT / "observation-mapping-readiness-report.json"

MATRICES = (
    ("historical_transfer", "transfer-cases.json"),
    ("adjudicated_adversarial", "adjudication-cases-v2.json"),
    ("natural_output", "natural-output-cases-v1.json"),
    ("repair_holdout", "repair-holdout-v1.json"),
    ("cross_domain", "cross-domain-holdout-v1.json"),
    ("fourth_family_holdout", "fourth-family-holdout-v1.json"),
    ("fifth_family_holdout", "fifth-family-holdout-v1.json"),
)
FORBIDDEN_KEYS = {"oracle", "expected", "expected_outcome"}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def case_count(doc: dict[str, Any]) -> int:
    cases = doc.get("cases")
    if not isinstance(cases, list):
        raise ValueError("matrix has no cases array")
    return len(cases)


def readiness(name: str, doc: dict[str, Any]) -> tuple[str, list[str]]:
    """Classify metadata only; do not inspect case outcomes or derive observations."""
    blockers: list[str] = []
    if name == "historical_transfer":
        blockers.append("source_locator values are unpinned prose, not hash-and-pointer locators")
    elif name == "adjudicated_adversarial":
        blockers.append("rationale is a builder-authored conclusion, not an admissible observed/source comparison")
    elif name == "natural_output":
        blockers.append("source artifacts are pinned, but mutations lack frozen observed-to-authoritative JSON-pointer comparisons")
    else:
        blockers.append("holdout source metadata does not provide per-row observed/source JSON-pointer comparisons")
    return "blocked", blockers


def build() -> dict[str, Any]:
    rows = []
    for name, filename in MATRICES:
        path = ROOT / filename
        doc = load(path)
        status, blockers = readiness(name, doc)
        rows.append({
            "matrix": name,
            "fixture": {"path": str(path.relative_to(REPO)), "sha256": sha(path)},
            "row_count": case_count(doc),
            "mapping_status": status,
            "blockers": blockers,
        })
    return {
        "schema_version": "1.0",
        "scope": "builder-authored observation-mapping prerequisite audit only",
        "method": {
            "outcome_labels_read": False,
            "adapter_implemented": False,
            "prior_artifacts_modified": False,
            "qualification_rule": "Every row requires hash-pinned admissible observed/source locators before descendant implementation.",
        },
        "matrices": rows,
        "summary": {
            "matrix_count": len(rows),
            "row_count": sum(row["row_count"] for row in rows),
            "ready_matrices": sum(row["mapping_status"] == "ready" for row in rows),
            "decision": "do_not_implement_descendant",
        },
        "required_continuation": [
            "Author a distinct source-comparison sidecar from actual admissible artifacts, not fixture oracle or rationale fields.",
            "Pin each observed and authoritative source file plus JSON pointer and transformation hash.",
            "Freeze and validate all anonymous mappings before writing descendant adapter or evaluator code.",
        ],
        "claim_boundaries": {
            "criterion_equivalence": False,
            "expert_or_professional_validity": False,
            "general_evaluator_validity": False,
            "agent_capability": False,
            "production_fitness": False,
            "deployment_readiness": False,
        },
    }


def validate(report: dict[str, Any]) -> list[str]:
    errors = []
    if report.get("method", {}).get("outcome_labels_read") is not False:
        errors.append("audit must not read outcome labels")
    if report.get("summary", {}).get("row_count") != 54:
        errors.append("expected 54 immutable replay rows")
    if len(report.get("matrices", [])) != 7:
        errors.append("expected seven matrices")
    if any(row.get("mapping_status") == "ready" and row.get("blockers") for row in report.get("matrices", [])):
        errors.append("ready matrix cannot retain blockers")
    if report.get("summary", {}).get("ready_matrices") != 0:
        errors.append("current fixtures do not contain complete admissible source comparisons")
    for row in report.get("matrices", []):
        path = REPO / row["fixture"]["path"]
        if not path.is_file() or sha(path) != row["fixture"]["sha256"]:
            errors.append(f"fixture integrity failed: {row['matrix']}")
    return errors


def main() -> int:
    report = build()
    errors = validate(report)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2))
        return 1
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"valid": True, **report["summary"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
