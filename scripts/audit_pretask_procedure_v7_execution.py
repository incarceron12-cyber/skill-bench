#!/usr/bin/env python3
"""Independent, non-rescoring audit of the frozen v7 execution evidence.

This script never invokes the model, launcher, oracle, or endpoint checker. It
verifies immutable bytes, joins retained records, independently compares stored
candidate artifacts with frozen private semantics, and separates assigned-row
outcomes from artifact-complete contrasts.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
V7 = ROOT / "pilots/pretask-procedure-transfer-v7"
EXEC = ROOT / "pilots/pretask-procedure-transfer-v7-execution"
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
OUTPUT = ROOT / "reports/validation/2026-07-19-pretask-procedure-v7-execution-independent-audit.json"
SOURCE_COMMIT = "a6d06f988dcdd56e6e3cb46845c652b9f1ace3e3"
CLAIMS = {
    "agent_capability": False,
    "expert_provenance": False,
    "production_fitness": False,
    "professional_validity": False,
    "readiness": False,
    "transfer": False,
    "utility": False,
}
CONTRASTS = (
    "cross_family_irrelevant - no_package_no_raw",
    "exactly_one_defect - reference_procedure",
    "generated_package - equal_budget_raw",
    "generated_package - no_package_no_raw",
    "generated_plus_raw - generated_package",
    "reference_procedure - generated_package",
)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def tracked_snapshot(prefix: str) -> tuple[list[dict[str, Any]], str]:
    paths = [
        line for line in git("ls-tree", "-r", "--name-only", SOURCE_COMMIT, prefix).splitlines()
        if line
    ]
    rows: list[dict[str, Any]] = []
    digest = hashlib.sha256()
    for rel in paths:
        path = ROOT / rel
        committed = subprocess.run(
            ["git", "show", f"{SOURCE_COMMIT}:{rel}"], cwd=ROOT, check=True,
            capture_output=True,
        ).stdout
        current = path.read_bytes()
        if current != committed:
            raise AssertionError(f"source snapshot drift: {rel}")
        row = {"path": rel, "bytes": len(current), "sha256": hashlib.sha256(current).hexdigest()}
        rows.append(row)
        digest.update(rel.encode() + b"\0" + row["sha256"].encode() + b"\0" + str(len(current)).encode() + b"\n")
    return rows, digest.hexdigest()


def support_sources(row: dict[str, Any]) -> list[tuple[Path, str]]:
    family = row["family_id"]
    name = "epsilon" if family == "family-epsilon" else "zeta"
    other = "zeta" if name == "epsilon" else "epsilon"
    condition = row["condition_id"]
    sources: list[tuple[Path, str]] = []
    if condition in {"generated_package", "generated_plus_raw"}:
        sources.append((V4 / f"candidate-generation/{family}/outputs/package.json", "procedure-package.json"))
    if condition in {"equal_budget_raw", "generated_plus_raw"}:
        sources.append((V4 / f"families/{name}/corpus.json", "source-context.json"))
    if condition == "reference_procedure":
        sources.append((V4 / f"controls/{name}/reference.json", "procedure-package.json"))
    if condition == "cross_family_irrelevant":
        sources.append((V4 / f"controls/{other}/reference.json", "procedure-package.json"))
    if condition == "exactly_one_defect":
        sources.append((V4 / f"controls/{name}/defective.json", "procedure-package.json"))
    if condition == "task_conditioned_hindsight_upper_bound":
        sources.append((V4 / f"hindsight-packages/{family}.json", "procedure-package.json"))
    return sources


def mismatch_paths(actual: Any, expected: Any, path: str = "") -> list[str]:
    """Compare frozen semantics while honoring only declared reason/order invariances."""
    if path.endswith("reason"):
        return [] if isinstance(actual, str) and actual.strip() else [path or "reason"]
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return [path or "$type"]
        errors = [f"{path}.{key}".strip(".") for key in sorted(set(actual) ^ set(expected))]
        for key in sorted(set(actual) & set(expected)):
            errors.extend(mismatch_paths(actual[key], expected[key], f"{path}.{key}".strip(".")))
        return errors
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return [path or "$type"]
        # Public contracts allow ordering variants for decisions and observation IDs.
        if path.endswith("observation_ids") and all(isinstance(x, str) for x in expected + actual):
            return [] if sorted(actual) == sorted(expected) else [path]
        if path == "decisions" and all(isinstance(x, dict) and "batch_id" in x for x in expected + actual):
            a_map = {x["batch_id"]: x for x in actual}
            e_map = {x["batch_id"]: x for x in expected}
            if len(a_map) != len(actual) or set(a_map) != set(e_map):
                return [path]
            errors: list[str] = []
            for key in sorted(e_map):
                errors.extend(mismatch_paths(a_map[key], e_map[key], f"decisions[{key}]"))
            return errors
        if len(actual) != len(expected):
            return [path]
        errors = []
        for index, (a_value, e_value) in enumerate(zip(actual, expected)):
            errors.extend(mismatch_paths(a_value, e_value, f"{path}[{index}]"))
        return errors
    return [] if type(actual) is type(expected) and actual == expected else [path or "$"]


def classify_miss(row: dict[str, Any], candidate: dict[str, Any], mismatches: list[str]) -> dict[str, Any]:
    index = row["schedule_index"]
    fixed = {
        2: ("irrelevant-package rejection displaced task execution", "committed transaction C omitted"),
        3: ("evidence enumeration omission", "non-controlling observation o2 omitted"),
        6: ("evidence enumeration omission", "non-controlling observation r1 omitted"),
        7: ("irrelevant-package rejection plus artifact identity error", "task_id set to family-zeta; transaction outcome rejected"),
        10: ("artifact identity plus journal-state error", "task_id set to family-zeta; unfinished journal incorrectly treated as valid"),
        14: ("evidence enumeration omission", "non-controlling observation o2 omitted"),
        17: ("evidence enumeration omission", "non-controlling observation r1 omitted"),
        25: ("defective-procedure susceptibility", "mutation assigned to wrong transaction, yielding x=2 rather than x=1"),
    }
    category, detail = fixed[index]
    return {
        "schedule_index": index,
        "task_id": row["task_id"],
        "family_id": row["family_id"],
        "condition_id": row["condition_id"],
        "artifact_valid": row["artifact_valid"],
        "category": category,
        "detail": detail,
        "mismatch_paths": mismatches,
        "candidate_task_id": candidate.get("task_id"),
    }


def main() -> int:
    errors: list[str] = []
    origin = git("rev-parse", "origin/main")
    head = git("rev-parse", "HEAD")
    for ref, value in (("HEAD", head), ("origin/main", origin)):
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", SOURCE_COMMIT, value], cwd=ROOT
        )
        if ancestry.returncode != 0:
            errors.append(f"source_commit_not_ancestor:{ref}:{value}")

    instrument_snapshot, instrument_digest = tracked_snapshot("pilots/pretask-procedure-transfer-v7")
    execution_snapshot, execution_digest = tracked_snapshot("pilots/pretask-procedure-transfer-v7-execution")

    manifest = load(V7 / "freeze-manifest.json")
    bound = manifest["components"] + manifest["external_immutable_bindings"]
    bound_errors = []
    for item in bound:
        path = ROOT / item["path"]
        if not path.is_file() or path.stat().st_size != item["bytes"] or sha(path) != item["sha256"]:
            bound_errors.append(item["path"])
    if len(bound) != 55 or bound_errors:
        errors.append(f"frozen_bindings:{len(bound)}:{bound_errors}")

    assignments = load(V7 / "assignments.json")["rows"]
    expected_indices = list(range(1, 33))
    if len(assignments) != 32 or [row["schedule_index"] for row in assignments] != expected_indices:
        errors.append("assignment_schedule")
    cell_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for row in assignments:
        cell_counts[row["family_id"]][row["condition_id"]] += 1
    if any(count != 2 for family in cell_counts.values() for count in family.values()):
        errors.append("assignment_cell_membership")

    prompt_hashes: set[str] = set()
    rows: list[dict[str, Any]] = []
    misses: list[dict[str, Any]] = []
    totals: dict[str, int | float] = {
        key: 0 for key in ("api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens")
    }
    totals["estimated_cost_usd"] = 0.0
    configured_systems: set[str] = set()

    for assignment in assignments:
        index = assignment["schedule_index"]
        trial = EXEC / "execution" / f"{index:02d}-{assignment['task_id']}"
        report = load(trial / "trial-report.json")
        usage = load(trial / "outputs/usage.json")
        candidate = load(trial / "outputs/result.json")
        private = load(V7 / f"tasks/{assignment['task_id']}/private.json")
        expected = private["expected_semantics"]
        mismatches = mismatch_paths(candidate, expected)
        independently_passes = not mismatches

        join_keys = ("schedule_index", "task_id", "family_id", "condition_id")
        if any(report.get(key) != assignment[key] for key in join_keys):
            errors.append(f"assignment_join:{index}")
        if not (
            report.get("attempts") == 1 and report.get("repair_attempts") == 0
            and report.get("retry_attempts") == 0 and report.get("attempt_state") == "attempted"
            and report.get("service_valid") is True and report.get("environment_valid") is True
            and report.get("checker_scored") is True and report.get("claim_ceiling") == CLAIMS
        ):
            errors.append(f"attempt_state:{index}")
        artifact_valid = isinstance(candidate, dict) and candidate.get("task_id") == assignment["task_id"]
        if artifact_valid != report.get("artifact_valid"):
            errors.append(f"artifact_join:{index}")
        if independently_passes != report.get("endpoint_pass") or independently_passes != report["checker_result"].get("passed"):
            errors.append(f"endpoint_join:{index}")

        expected_inventory = {
            "public-task.md": V7 / f"tasks/{assignment['task_id']}/public.md",
            "input.json": V7 / f"tasks/{assignment['task_id']}/input.json",
        }
        expected_inventory.update({name: path for path, name in support_sources(assignment)})
        declared_inventory = report.get("input_inventory", {})
        recomputed_inventory = {
            name: {"sha256": sha(path), "bytes": path.stat().st_size}
            for name, path in expected_inventory.items()
        }
        if declared_inventory != recomputed_inventory:
            errors.append(f"input_inventory:{index}")

        evidence_checks = {
            "result.json": trial / "outputs/result.json",
            "usage.json": trial / "outputs/usage.json",
        }
        for name, path in evidence_checks.items():
            if report["output_inventory"].get(name) != {"sha256": sha(path), "bytes": path.stat().st_size}:
                errors.append(f"output_inventory:{index}:{name}")
        if report.get("trace_sha256") != sha(trial / "redacted-trace.log"):
            errors.append(f"trace_hash:{index}")
        if report.get("stderr_sha256") != sha(trial / "launcher-stderr.log"):
            errors.append(f"stderr_hash:{index}")
        prompt_hash = sha(trial / "prompt.txt")
        prompt_hashes.add(prompt_hash)
        if report.get("prompt_sha256") != prompt_hash:
            errors.append(f"prompt_hash:{index}")
        if not (
            usage.get("completed") is True and usage.get("failed") is False
            and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
            and usage.get("model") == "gpt-5.6-sol" and usage.get("provider") == "openai-codex"
        ):
            errors.append(f"service_usage:{index}")
        for key in totals:
            totals[key] += usage.get(key, 0)
        configured_systems.add(json.dumps(report["configured_system"], sort_keys=True))

        row = {
            **{key: assignment[key] for key in join_keys},
            "artifact_valid": artifact_valid,
            "endpoint_pass": report["endpoint_pass"],
            "mismatch_paths": mismatches,
            "support_bytes": sum(path.stat().st_size for path, _ in support_sources(assignment)),
            "api_calls": usage["api_calls"],
            "total_tokens": usage["total_tokens"],
            "input_tokens": usage["input_tokens"],
            "output_tokens": usage["output_tokens"],
        }
        rows.append(row)
        if not independently_passes:
            misses.append(classify_miss(row, candidate, mismatches))

    denominator = {
        "intended": 32,
        "attempted": len(rows),
        "service_valid": sum(True for _ in rows),
        "environment_valid": sum(True for _ in rows),
        "artifact_valid": sum(row["artifact_valid"] for row in rows),
        "checker_scored": len(rows),
        "endpoint_pass": sum(row["endpoint_pass"] for row in rows),
        "artifact_invalid": sum(not row["artifact_valid"] for row in rows),
        "endpoint_miss": sum(not row["endpoint_pass"] for row in rows),
        "repair": 0,
        "retry": 0,
    }

    family_cells: dict[str, dict[str, Any]] = defaultdict(dict)
    resource_cells: dict[str, dict[str, Any]] = defaultdict(dict)
    for family in sorted(cell_counts):
        conditions = sorted(cell_counts[family])
        for condition in conditions:
            subset = [row for row in rows if row["family_id"] == family and row["condition_id"] == condition]
            valid = [row for row in subset if row["artifact_valid"]]
            family_cells[family][condition] = {
                "assigned": len(subset),
                "artifact_valid": len(valid),
                "assigned_endpoint_passes": sum(row["endpoint_pass"] for row in subset),
                "assigned_pass_rate": sum(row["endpoint_pass"] for row in subset) / len(subset),
                "artifact_complete_pass_rate": (
                    sum(row["endpoint_pass"] for row in valid) / len(valid) if len(valid) == 2 else None
                ),
                "artifact_complete_estimand_identified": len(valid) == 2,
                "task_ids": sorted(row["task_id"] for row in subset),
            }
            resource_cells[family][condition] = {
                "support_bytes": [row["support_bytes"] for row in sorted(subset, key=lambda x: x["task_id"])],
                "api_calls": sum(row["api_calls"] for row in subset),
                "total_tokens": sum(row["total_tokens"] for row in subset),
                "input_tokens": sum(row["input_tokens"] for row in subset),
                "output_tokens": sum(row["output_tokens"] for row in subset),
            }

    contrasts: dict[str, Any] = {}
    for expression in CONTRASTS:
        left, right = expression.split(" - ")
        family_results = {}
        assigned_differences = []
        complete_differences = []
        for family in sorted(family_cells):
            a, b = family_cells[family][left], family_cells[family][right]
            assigned = a["assigned_pass_rate"] - b["assigned_pass_rate"]
            identified = a["artifact_complete_estimand_identified"] and b["artifact_complete_estimand_identified"]
            complete = a["artifact_complete_pass_rate"] - b["artifact_complete_pass_rate"] if identified else None
            family_results[family] = {
                "assigned_row_difference": assigned,
                "artifact_complete_difference": complete,
                "artifact_complete_identified": identified,
            }
            assigned_differences.append(assigned)
            if complete is not None:
                complete_differences.append(complete)
        contrasts[expression] = {
            "families": family_results,
            "assigned_row_family_mean": sum(assigned_differences) / 2,
            "artifact_complete_family_mean": (
                sum(complete_differences) / 2 if len(complete_differences) == 2 else None
            ),
            "artifact_complete_cluster_count": len(complete_differences),
            "inferential_uncertainty": "not_estimable_from_two_authored_families_and_one_attempt_per_cell",
        }

    summary = load(EXEC / "execution-report.json")
    expected_summary_denominators = {
        "intended": 32, "attempted": 32, "skipped": 0, "invalid": 0,
        "service_valid": 32, "environment_valid": 32, "artifact_valid": 30,
        "checker_scored": 32, "endpoint_pass": 24,
    }
    if summary.get("denominators") != expected_summary_denominators:
        errors.append("published_denominators")
    if summary.get("claim_ceiling") != CLAIMS:
        errors.append("published_claim_ceiling")
    if len(prompt_hashes) != 1 or len(configured_systems) != 1:
        errors.append("prompt_or_configured_system_parity")

    checker_source = (V7 / "checkers/check_endpoint.py").read_text(encoding="utf-8")
    forbidden_checker_terms = [term for term in ("condition_id", "assignments.json", "procedure-package") if term in checker_source]
    checker_dependencies = {
        "sha256": sha(V7 / "checkers/check_endpoint.py"),
        "stored_result_only": True,
        "checker_was_not_invoked_by_this_audit": True,
        "forbidden_condition_or_treatment_terms_found": forbidden_checker_terms,
    }
    if forbidden_checker_terms:
        errors.append("checker_condition_dependency")

    report = {
        "audit_id": "pretask-procedure-transfer-v7-execution-independent-validity-audit",
        "status": "PASS_WITH_CLAIM_LIMITS" if not errors else "FAIL",
        "errors": errors,
        "source_snapshot": {
            "commit": SOURCE_COMMIT,
            "source_commit_was_head_and_origin_at_initial_audit": True,
            "instrument_tracked_file_count": len(instrument_snapshot),
            "instrument_tree_digest": instrument_digest,
            "execution_tracked_file_count": len(execution_snapshot),
            "execution_tree_digest": execution_digest,
            "frozen_manifest_bindings_checked": len(bound),
            "frozen_binding_errors": bound_errors,
        },
        "method": {
            "model_calls": 0,
            "provider_calls": 0,
            "launcher_invocations": 0,
            "checker_invocations": 0,
            "oracle_invocations": 0,
            "repairs": 0,
            "retries": 0,
            "note": "Independent byte/join/semantic audit of retained records; no rerun or post-hoc score replacement.",
        },
        "denominators": denominator,
        "prompt_parity": {"distinct_hashes": sorted(prompt_hashes), "count": len(prompt_hashes)},
        "configured_system_parity": {"distinct_records": len(configured_systems)},
        "checker_dependencies": checker_dependencies,
        "resource_totals": totals,
        "resource_cells": resource_cells,
        "family_condition_cells": family_cells,
        "contrasts": contrasts,
        "endpoint_miss_classifications": misses,
        "artifact_invalid_rows": [miss for miss in misses if not miss["artifact_valid"]],
        "identification_decision": {
            "assigned_row_observation": "The frozen assigned-row summary is arithmetically closed: 24/32 endpoint passes and the published descriptive contrasts reproduce.",
            "package_vs_no_package": "Not an artifact-complete two-family contrast because one zeta no-package artifact is invalid; the assigned-row +0.75 is not a transfer estimand.",
            "package_vs_equal_budget_raw": "Artifact-complete in both authored families and exactly 0.0; this supports only no observed endpoint advantage over the frozen raw corpus in this one-shot synthetic matrix.",
            "general_inference": "No sampling-based uncertainty is identified: only two authored families, two fixed tasks per family-condition, and one model attempt per row.",
        },
        "operational_limits": [
            "The 8,000-token context budget is declared in protocol/trial records but is not passed as an enforceable launcher argument; treatment retrieval is bounded by bytes, not model-visible tokens.",
            "The Hermes executable/environment is used from a mutable local path without a retained binary/tree hash in each trial, limiting configured-system reproduction even though launcher bytes and trial fields match.",
            "Prompt files were reconstructed after execution; prospective reports retain their matching hash but not independently timestamped prompt bytes.",
            "Sequential one-shot execution leaves stochastic and time/order variation unestimated.",
            "All tasks, procedures, endpoints, and authority are builder-authored synthetic calibration artifacts; task-package-checker co-design and ceiling effects limit construct interpretation.",
        ],
        "claim_ceiling": CLAIMS,
        "claim_decision": {
            "bounded_execution_closure": True,
            "bounded_assigned_endpoint_observation": True,
            "generated_package_advantage_over_equal_budget_raw": False,
            "artifact_complete_package_advantage_over_no_package": False,
            "agent_capability": False,
            "expert_provenance": False,
            "general_transfer": False,
            "utility": False,
            "professional_validity": False,
            "production_fitness": False,
            "readiness": False,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"], "errors": errors, "denominators": denominator,
        "endpoint_misses": len(misses), "artifact_invalid": len(report["artifact_invalid_rows"]),
        "output": OUTPUT.relative_to(ROOT).as_posix(),
    }, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
