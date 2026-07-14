#!/usr/bin/env python3
"""Replay compensatory and dependency-gated progress on pinned/synthetic rubrics."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "cases.json"
REPORT = HERE / "replay-report.json"
ARCHIVE = ROOT / "data/sources/releases/2504.01848v3-paperbench/openai-frontier-evals-paperbench-51052ced.zip"
ARCHIVE_SHA256 = "be40897c77e7bdfd21cce12410445a570510fcc93ebe278bcf6ff67193b6024b"
MEMBER = "frontier-evals-51052ced-paperbench/project/paperbench/data/papers/semantic-self-consistency/rubric.json"
MEMBER_SHA256 = "d3fadf651538936b86cef230bcf842634150f4cef6985aa19611346238506915"
COMMIT = "51052cede8cc608f95bb00346635e03759013e5a"
STATES = {"supported", "contradicted", "invalid", "insufficient_evidence", "not_applicable"}


class ReplayError(ValueError):
    """Fixture, provenance, or deterministic replay error."""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def children(node: dict[str, Any]) -> list[dict[str, Any]]:
    return node.get("sub_tasks", node.get("criteria", []))


def topology(node: dict[str, Any]) -> tuple[int, int]:
    kids = children(node)
    if not kids:
        return 1, 1
    parts = [topology(child) for child in kids]
    return 1 + sum(part[0] for part in parts), sum(part[1] for part in parts)


def recursive_weighted(node: dict[str, Any], leaf_values: dict[str, float | None]) -> float | None:
    kids = children(node)
    if not kids:
        return leaf_values[node["id"]]
    applicable = [(child, recursive_weighted(child, leaf_values)) for child in kids]
    applicable = [(child, value) for child, value in applicable if value is not None]
    if not applicable:
        return None
    denominator = sum(float(child["weight"]) for child, _ in applicable)
    return sum(float(child["weight"]) * float(value) for child, value in applicable) / denominator


def expression_refs(expr: dict[str, Any]) -> list[str]:
    if "criterion" in expr:
        return [expr["criterion"]]
    key = "all" if "all" in expr else "any"
    return [ref for item in expr[key] for ref in expression_refs(item)]


def validate_fixture(fixture: dict[str, Any]) -> None:
    seen_cases: set[str] = set()
    for case in fixture["cases"]:
        if case["case_id"] in seen_cases:
            raise ReplayError(f"duplicate case_id {case['case_id']!r}")
        seen_cases.add(case["case_id"])
        criteria = case["criteria"]
        ids = [item["id"] for item in criteria]
        if len(ids) != len(set(ids)):
            raise ReplayError(f"{case['case_id']}: criterion IDs must be unique")
        known = set(ids)
        for item in criteria:
            if item["state"] not in STATES:
                raise ReplayError(f"{case['case_id']}/{item['id']}: unknown state")
            if not isinstance(item["weight"], (int, float)) or item["weight"] <= 0:
                raise ReplayError(f"{case['case_id']}/{item['id']}: weight must be positive")
            if not item.get("evidence"):
                raise ReplayError(f"{case['case_id']}/{item['id']}: evidence locator required")
            for ref in expression_refs(item["depends_on"]) if "depends_on" in item else []:
                if ref not in known:
                    raise ReplayError(f"{case['case_id']}/{item['id']}: unknown dependency {ref!r}")
                if ref == item["id"]:
                    raise ReplayError(f"{case['case_id']}/{item['id']}: self dependency")
        if not set(case["mandatory_ids"]).issubset(known):
            raise ReplayError(f"{case['case_id']}: unknown mandatory criterion")


def evaluate_case(case: dict[str, Any], threshold: float) -> dict[str, Any]:
    by_id = {item["id"]: item for item in case["criteria"]}
    resolving: set[str] = set()
    memo: dict[str, bool] = {}

    def expr_satisfied(expr: dict[str, Any]) -> bool:
        if "criterion" in expr:
            return effective(expr["criterion"])
        if "all" in expr:
            return all(expr_satisfied(item) for item in expr["all"])
        return any(expr_satisfied(item) for item in expr["any"])

    def effective(criterion_id: str) -> bool:
        if criterion_id in memo:
            return memo[criterion_id]
        if criterion_id in resolving:
            raise ReplayError(f"{case['case_id']}: dependency cycle at {criterion_id!r}")
        resolving.add(criterion_id)
        item = by_id[criterion_id]
        value = item["state"] == "supported" and (
            "depends_on" not in item or expr_satisfied(item["depends_on"])
        )
        resolving.remove(criterion_id)
        memo[criterion_id] = value
        return value

    compensatory_values = {
        item["id"]: None if item["state"] == "not_applicable" else (1.0 if item["state"] == "supported" else 0.0)
        for item in case["criteria"]
    }
    gated_values = {
        item["id"]: None if item["state"] == "not_applicable" else (1.0 if effective(item["id"]) else 0.0)
        for item in case["criteria"]
    }
    root = {"id": "root", "weight": 1, "criteria": case["criteria"]}
    compensatory = recursive_weighted(root, compensatory_values)
    gated = recursive_weighted(root, gated_values)
    if compensatory is None or gated is None:
        raise ReplayError(f"{case['case_id']}: case must contain an applicable criterion")
    applicable = [item for item in case["criteria"] if item["state"] != "not_applicable"]
    invalid = [item["id"] for item in case["criteria"] if item["state"] == "invalid"]
    insufficient = [item["id"] for item in case["criteria"] if item["state"] == "insufficient_evidence"]
    mandatory_complete = all(effective(item) for item in case["mandatory_ids"])
    headline_eligible = not invalid and not insufficient
    criterion_evidence = [
        {
            "criterion_id": item["id"],
            "state": item["state"],
            "dependency_refs": expression_refs(item["depends_on"]) if "depends_on" in item else [],
            "effective_supported": effective(item["id"]) if item["state"] != "not_applicable" else None,
            "evidence": item["evidence"],
        }
        for item in case["criteria"]
    ]
    return {
        "case_id": case["case_id"],
        "description": case["description"],
        "compensatory_progress": round(float(compensatory), 12),
        "dependency_gated_progress": round(float(gated), 12),
        "dependency_complete_pathway_rate": round(sum(effective(item["id"]) for item in applicable) / len(applicable), 12),
        "score_delta_gated_minus_compensatory": round(float(gated) - float(compensatory), 12),
        "invalid_criterion_ids": invalid,
        "insufficient_evidence_criterion_ids": insufficient,
        "not_applicable_criterion_ids": [item["id"] for item in case["criteria"] if item["state"] == "not_applicable"],
        "mandatory_complete": mandatory_complete,
        "headline_eligible": headline_eligible,
        "compensatory_threshold_pass": float(compensatory) >= threshold,
        "gated_completion_claim_pass": headline_eligible and mandatory_complete and float(gated) >= threshold,
        "criterion_evidence": criterion_evidence,
    }


def ranks(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    """Return competition ranks so equal scores never create alphabetical rank effects."""
    values = [row[field] for row in rows]
    return {
        row["case_id"]: 1 + sum(value > row[field] for value in values)
        for row in rows
    }


def build_report() -> dict[str, Any]:
    if sha256(ARCHIVE) != ARCHIVE_SHA256:
        raise ReplayError("pinned PaperBench archive hash mismatch")
    with zipfile.ZipFile(ARCHIVE) as archive:
        source_bytes = archive.read(MEMBER)
    if hashlib.sha256(source_bytes).hexdigest() != MEMBER_SHA256:
        raise ReplayError("pinned rubric member hash mismatch")
    source_rubric = json.loads(source_bytes)
    node_count, leaf_count = topology(source_rubric)
    source_leaf_ids: list[str] = []

    def collect(node: dict[str, Any]) -> None:
        if not children(node):
            source_leaf_ids.append(node["id"])
        for child in children(node):
            collect(child)

    collect(source_rubric)
    all_supported = recursive_weighted(source_rubric, {item: 1.0 for item in source_leaf_ids})
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    validate_fixture(fixture)
    rows = [evaluate_case(case, fixture["threshold"]) for case in fixture["cases"]]
    comp_ranks = ranks(rows, "compensatory_progress")
    gated_ranks = ranks(rows, "dependency_gated_progress")
    for row in rows:
        row["compensatory_rank"] = comp_ranks[row["case_id"]]
        row["dependency_gated_rank"] = gated_ranks[row["case_id"]]
        row["rank_change_gated_minus_compensatory"] = gated_ranks[row["case_id"]] - comp_ranks[row["case_id"]]
    threshold_flips = [
        row["case_id"] for row in rows
        if row["compensatory_threshold_pass"] != row["gated_completion_claim_pass"]
    ]
    rank_changes = [row["case_id"] for row in rows if row["rank_change_gated_minus_compensatory"] != 0]
    return {
        "report_version": "0.1",
        "fixture_id": fixture["fixture_id"],
        "generated_by": "pilots/dependency-gated-score-replay/replay.py",
        "source_rubric": {
            "archive_path": str(ARCHIVE.relative_to(ROOT)),
            "archive_sha256": ARCHIVE_SHA256,
            "official_commit": COMMIT,
            "member_path": MEMBER,
            "member_sha256": MEMBER_SHA256,
            "paper_id": "semantic-self-consistency",
            "root_id": source_rubric["id"],
            "node_count": node_count,
            "leaf_count": leaf_count,
            "all_supported_recursive_score": all_supported,
            "interpretation": "The pinned released tree is replayed only to verify topology, identity, and recursive sibling-weighted aggregation. Its prose dependencies were not inferred into synthetic gates.",
        },
        "metric_contract_mapping": {
            "unit": "synthetic graded criterion tree",
            "eligible_population": [case["case_id"] for case in fixture["cases"]],
            "population_kind": "synthetic_exact_enumeration",
            "compensatory_observable": "recursive sibling-weighted local criterion state",
            "gated_observable": "same weights after recursive prerequisite/conjunction/alternative gating",
            "invalid_policy": "zero for PaperBench-compatible progress replay; separately fail closed for headline eligibility",
            "insufficient_evidence_policy": "zero for progress; separately fail closed for headline eligibility",
            "not_applicable_policy": "exclude and renormalize sibling weights",
            "uncertainty": "not estimated; exact deterministic fixture enumeration",
            "threshold": fixture["threshold"],
        },
        "summary": {
            "case_count": len(rows),
            "threshold_flip_case_ids": threshold_flips,
            "rank_change_case_ids": rank_changes,
            "invalid_case_ids": [row["case_id"] for row in rows if row["invalid_criterion_ids"]],
            "insufficient_evidence_case_ids": [row["case_id"] for row in rows if row["insufficient_evidence_criterion_ids"]],
            "mean_compensatory_progress": round(sum(row["compensatory_progress"] for row in rows) / len(rows), 12),
            "mean_dependency_gated_progress": round(sum(row["dependency_gated_progress"] for row in rows) / len(rows), 12),
        },
        "cases": rows,
        "claim_boundaries": fixture["claim_boundaries"],
        "provenance": {
            "review": "papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md",
            "release_audit": "data/sources/releases/2504.01848v3-paperbench/audit.json",
            "fixture": str(FIXTURE.relative_to(ROOT)),
            "fixture_sha256": sha256(FIXTURE),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed report differs from deterministic replay")
    args = parser.parse_args()
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not REPORT.is_file() or REPORT.read_text(encoding="utf-8") != rendered:
            raise SystemExit("STALE replay-report.json; run replay.py without --check")
        print(f"VALID {REPORT.relative_to(ROOT)} ({len(report['cases'])} cases)")
    else:
        REPORT.write_text(rendered, encoding="utf-8")
        print(f"WROTE {REPORT.relative_to(ROOT)} ({len(report['cases'])} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
