#!/usr/bin/env python3
"""Audit criterion predictions at leaf, task-score, ranking, and decision levels."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "cases.json"
REPORT = HERE / "audit-report.json"
POLICIES = {"fail_closed", "fail_open", "abstain"}
SEVERITIES = {"low", "medium", "high", "critical"}


class AuditError(ValueError):
    """Raised when the prediction contract is malformed."""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expand_task(task: dict[str, Any]) -> list[dict[str, Any]]:
    leaves: list[dict[str, Any]] = []
    for group in task["criterion_groups"]:
        for index in range(group["count"]):
            leaves.append({
                "criterion_id": f"{group['group_id']}:{index + 1}",
                "truth": group["truth"],
                "prediction": group["prediction"],
                "valid": group["valid"],
                "weight": float(group["weight_each"]),
                "severity": group["severity"],
            })
    return leaves


def validate_fixture(fixture: dict[str, Any]) -> None:
    if set(fixture["invalid_policies"]) != POLICIES:
        raise AuditError("fixture must exercise fail_closed, fail_open, and abstain")
    if not 0 <= fixture["decision_threshold"] <= 1:
        raise AuditError("decision_threshold must be in [0, 1]")
    ids: set[str] = set()
    sizes: list[int] = []
    for task in fixture["tasks"]:
        if task["task_id"] in ids:
            raise AuditError(f"duplicate task_id {task['task_id']!r}")
        ids.add(task["task_id"])
        groups = task.get("criterion_groups", [])
        if not groups:
            raise AuditError(f"{task['task_id']}: criterion_groups required")
        group_ids: set[str] = set()
        for group in groups:
            if group["group_id"] in group_ids:
                raise AuditError(f"{task['task_id']}: duplicate group_id")
            group_ids.add(group["group_id"])
            if not isinstance(group["count"], int) or group["count"] <= 0:
                raise AuditError(f"{task['task_id']}/{group['group_id']}: count must be positive integer")
            if group["truth"] not in (0, 1):
                raise AuditError(f"{task['task_id']}/{group['group_id']}: truth must be binary")
            if group["valid"] and group["prediction"] not in (0, 1):
                raise AuditError(f"{task['task_id']}/{group['group_id']}: valid prediction must be binary")
            if not group["valid"] and group["prediction"] is not None:
                raise AuditError(f"{task['task_id']}/{group['group_id']}: invalid prediction must be null")
            if not isinstance(group["weight_each"], (int, float)) or group["weight_each"] <= 0:
                raise AuditError(f"{task['task_id']}/{group['group_id']}: weight must be positive")
            if group["severity"] not in SEVERITIES:
                raise AuditError(f"{task['task_id']}/{group['group_id']}: unknown severity")
        sizes.append(sum(group["count"] for group in groups))
    if not sizes or max(sizes) / min(sizes) < 10:
        raise AuditError("fixture must include at least a 10x task-size contrast")


def apply_policy(leaves: list[dict[str, Any]], policy: str) -> list[dict[str, Any]]:
    if policy not in POLICIES:
        raise AuditError(f"unknown invalid policy {policy!r}")
    output = []
    for leaf in leaves:
        if leaf["valid"]:
            output.append({**leaf, "effective_prediction": leaf["prediction"]})
        elif policy == "fail_closed":
            output.append({**leaf, "effective_prediction": 0})
        elif policy == "fail_open":
            output.append({**leaf, "effective_prediction": 1})
    return output


def confusion(rows: list[dict[str, Any]]) -> dict[str, Any]:
    counts = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}
    for row in rows:
        truth, prediction = row["truth"], row["effective_prediction"]
        counts[{(1, 1): "tp", (0, 0): "tn", (0, 1): "fp", (1, 0): "fn"}[(truth, prediction)]] += 1
    f1s = []
    for positive in (1, 0):
        tp = sum(row["truth"] == positive and row["effective_prediction"] == positive for row in rows)
        fp = sum(row["truth"] != positive and row["effective_prediction"] == positive for row in rows)
        fn = sum(row["truth"] == positive and row["effective_prediction"] != positive for row in rows)
        denominator = 2 * tp + fp + fn
        f1s.append((2 * tp / denominator) if denominator else 0.0)
    return {**counts, "class_macro_f1": sum(f1s) / 2, "accuracy": sum(row["truth"] == row["effective_prediction"] for row in rows) / len(rows)}


def weighted_score(rows: list[dict[str, Any]], field: str) -> float:
    return sum(row["weight"] * row[field] for row in rows) / sum(row["weight"] for row in rows)


def competition_ranks(values: dict[str, float]) -> dict[str, int]:
    return {key: 1 + sum(other > value for other in values.values()) for key, value in values.items()}


def task_rows(fixture: dict[str, Any], policy: str) -> list[dict[str, Any]]:
    threshold = fixture["decision_threshold"]
    results = []
    for task in fixture["tasks"]:
        all_leaves = expand_task(task)
        evaluated = apply_policy(all_leaves, policy)
        invalid_count = sum(not leaf["valid"] for leaf in all_leaves)
        truth_root = weighted_score(all_leaves, "truth")
        predicted_root = weighted_score(evaluated, "effective_prediction")
        truth_pass = truth_root >= threshold
        predicted_pass = None if policy == "abstain" and invalid_count else predicted_root >= threshold
        consequential = [row for row in evaluated if row["severity"] in {"high", "critical"}]
        results.append({
            "task_id": task["task_id"],
            "leaf_count": len(all_leaves),
            "evaluated_leaf_count": len(evaluated),
            "invalid_count": invalid_count,
            "leaf_metrics": confusion(evaluated),
            "consequential_confusion": confusion(consequential) if consequential else None,
            "truth_root_score": truth_root,
            "predicted_root_score": predicted_root,
            "root_absolute_error": abs(predicted_root - truth_root),
            "truth_threshold_pass": truth_pass,
            "predicted_threshold_pass": predicted_pass,
            "threshold_flip": None if predicted_pass is None else predicted_pass != truth_pass,
        })
    return results


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    pooled_source = []
    # Reconstructing from confusion counts is sufficient for pooled binary metrics.
    for row in rows:
        c = row["leaf_metrics"]
        pooled_source.extend([{"truth": 1, "effective_prediction": 1}] * c["tp"])
        pooled_source.extend([{"truth": 0, "effective_prediction": 0}] * c["tn"])
        pooled_source.extend([{"truth": 0, "effective_prediction": 1}] * c["fp"])
        pooled_source.extend([{"truth": 1, "effective_prediction": 0}] * c["fn"])
    true_scores = {row["task_id"]: row["truth_root_score"] for row in rows}
    pred_scores = {row["task_id"]: row["predicted_root_score"] for row in rows}
    true_ranks, pred_ranks = competition_ranks(true_scores), competition_ranks(pred_scores)
    rank_rows = [{
        "task_id": task_id,
        "truth_rank": true_ranks[task_id],
        "predicted_rank": pred_ranks[task_id],
        "absolute_rank_change": abs(pred_ranks[task_id] - true_ranks[task_id]),
    } for task_id in true_scores]
    decidable = [row for row in rows if row["threshold_flip"] is not None]
    consequential_counts = {key: 0 for key in ("tp", "tn", "fp", "fn")}
    for row in rows:
        if row["consequential_confusion"]:
            for key in consequential_counts:
                consequential_counts[key] += row["consequential_confusion"][key]
    return {
        "pooled_leaf_class_macro_f1": confusion(pooled_source)["class_macro_f1"],
        "equal_task_class_macro_f1": sum(row["leaf_metrics"]["class_macro_f1"] for row in rows) / len(rows),
        "mean_root_absolute_error": sum(row["root_absolute_error"] for row in rows) / len(rows),
        "threshold_flip_rate_among_decidable": sum(row["threshold_flip"] for row in decidable) / len(decidable),
        "threshold_flip_task_ids": [row["task_id"] for row in decidable if row["threshold_flip"]],
        "abstained_task_ids": [row["task_id"] for row in rows if row["predicted_threshold_pass"] is None],
        "consequential_confusion": consequential_counts,
        "mean_absolute_rank_change": sum(row["absolute_rank_change"] for row in rank_rows) / len(rank_rows),
        "rank_effects": rank_rows,
    }


def percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    index = round((len(ordered) - 1) * probability)
    return ordered[index]


def clustered_bootstrap(rows: list[dict[str, Any]], replicates: int, seed: int) -> dict[str, Any]:
    if len(rows) < 2 or replicates <= 0:
        return {"method": "not_estimated", "reason": "requires at least two tasks and positive replicates"}
    rng = random.Random(seed)
    draws = {key: [] for key in ("equal_task_class_macro_f1", "mean_root_absolute_error", "threshold_flip_rate_among_decidable")}
    for _ in range(replicates):
        sample = [rng.choice(rows) for _ in rows]
        draws["equal_task_class_macro_f1"].append(
            sum(row["leaf_metrics"]["class_macro_f1"] for row in sample) / len(sample)
        )
        draws["mean_root_absolute_error"].append(
            sum(row["root_absolute_error"] for row in sample) / len(sample)
        )
        decidable = [row for row in sample if row["threshold_flip"] is not None]
        if decidable:
            draws["threshold_flip_rate_among_decidable"].append(
                sum(row["threshold_flip"] for row in decidable) / len(decidable)
            )
    return {
        "method": "task_cluster_nonparametric_bootstrap",
        "replicates": replicates,
        "seed": seed,
        "interval": "percentile_95",
        "estimates": {
            key: {
                "lower": percentile(values, 0.025),
                "upper": percentile(values, 0.975),
                "effective_replicates": len(values),
            }
            for key, values in draws.items()
        },
        "limitation": "Five authored tasks are the complete configured fixture, not a random domain sample; intervals show task-cluster sensitivity only. Draws with no decidable task are omitted from the threshold-flip interval and counted through effective_replicates.",
    }


def build_report() -> dict[str, Any]:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    validate_fixture(fixture)
    policies = {}
    for policy in fixture["invalid_policies"]:
        rows = task_rows(fixture, policy)
        policies[policy] = {
            "semantics": {
                "fail_closed": "Invalid predictions enter leaf and root metrics as zero and remain counted as invalid.",
                "fail_open": "Invalid predictions enter leaf and root metrics as one and remain counted as invalid.",
                "abstain": "Invalid leaves are excluded and weights renormalized; any affected task has no threshold decision.",
            }[policy],
            "summary": summarize(rows),
            "clustered_uncertainty": clustered_bootstrap(rows, fixture["bootstrap"]["replicates"], fixture["bootstrap"]["seed"]),
            "tasks": rows,
        }
    return {
        "report_version": "0.1",
        "generated_by": "pilots/judge-decision-validity-audit/audit.py",
        "fixture_id": fixture["fixture_id"],
        "configured_population": fixture["configured_population"],
        "decision_threshold": fixture["decision_threshold"],
        "estimand_warning": "Pooled-leaf agreement, equal-task agreement, root-score error, ranks, consequential confusion, and threshold decisions are distinct estimands and are not interchangeable.",
        "policies": policies,
        "claim_boundaries": fixture["claim_boundaries"],
        "provenance": {
            "fixture": str(FIXTURE.relative_to(ROOT)),
            "fixture_sha256": sha256(FIXTURE),
            "review": "papers/agent-benchmarks/2026-07-15-paperbench-replication-rubric-validity.md",
            "release_audit": "data/sources/releases/2504.01848v3-paperbench/audit.json"
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed report differs from deterministic replay")
    args = parser.parse_args()
    rendered = json.dumps(build_report(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not REPORT.is_file() or REPORT.read_text(encoding="utf-8") != rendered:
            raise SystemExit("STALE audit-report.json; run audit.py without --check")
        print(f"VALID {REPORT.relative_to(ROOT)}")
    else:
        REPORT.write_text(rendered, encoding="utf-8")
        print(f"WROTE {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
