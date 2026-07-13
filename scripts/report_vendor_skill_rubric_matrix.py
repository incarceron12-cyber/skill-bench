#!/usr/bin/env python3
"""Validate, record, and exactly replay the prospective vendor Skill×rubric matrix."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import math
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/vendor-incident-response"
MATRIX = PILOT / "trials/skill-rubric-matrix-v1"
PROTOCOL_PATH = MATRIX / "protocol.json"
REPORT_PATH = MATRIX / "matrix-report.json"
CLAIM_KEYS = {"general_skill_effect", "capability", "professional_validity", "safety", "production_fitness", "cross_domain_generality", "readiness"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _assert_hash(path: Path, expected: str, role: str) -> None:
    if not path.is_file():
        raise ValueError(f"missing frozen {role}: {path}")
    observed = sha256(path)
    if observed != expected:
        raise ValueError(f"{role} hash drift: expected {expected}, observed {observed}")


def verify_protocol(protocol: dict[str, Any], protocol_path: Path = PROTOCOL_PATH) -> None:
    if protocol_path.resolve() != PROTOCOL_PATH.resolve():
        raise ValueError("only canonical prospective protocol path is allowed")
    schedule = protocol["attempt_schedule"]
    if len(schedule) != 6 or len({row["attempt_id"] for row in schedule}) != 6:
        raise ValueError("schedule must contain six unique blinded attempt IDs")
    counts = {condition: sum(row["skill_condition"] == condition for row in schedule) for condition in ("no_skill", "public_skill")}
    if counts != {"no_skill": 3, "public_skill": 3}:
        raise ValueError(f"condition denominator drift: {counts}")
    if [row["execution_order"] for row in schedule] != list(range(1, 7)):
        raise ValueError("execution order must be frozen and contiguous")
    if any(row["replacement_for"] is not None for row in schedule):
        raise ValueError("replacement attempts are prohibited")
    if protocol["policies"]["attempts_per_condition"] != 3 or protocol["policies"]["replacement_attempts"] != "none" or protocol["policies"]["retry_or_adaptation"] != "none":
        raise ValueError("attempt/retry policy drift")
    if protocol["configured_system"] != {"model": "gpt-5.6-sol", "provider": "openai-codex", "invocation": "oneshot", "safe_mode": True, "toolsets": ["file"], "max_turns": 40}:
        raise ValueError("configured-system drift")
    for component in protocol["frozen_components"]:
        _assert_hash(ROOT / component["path"], component["sha256"], component["role"])
    roles = {x["role"] for x in protocol["frozen_components"]}
    required = {"public_task", "public_guide", "independent_rubric", "shared_rubric", "independent_construction_manifest", "base_launcher", "matrix_launcher", "base_grader", "matrix_scorer"}
    if not required <= roles:
        raise ValueError(f"missing component roles: {sorted(required - roles)}")
    firewall = protocol["firewalls"]
    if set(firewall["agent_prohibited_roles"]) != {"independent_rubric", "shared_rubric", "base_grader", "protocol", "private_checks"}:
        raise ValueError("agent-input firewall drift")
    construction = load_json(ROOT / next(x["path"] for x in protocol["frozen_components"] if x["role"] == "independent_construction_manifest"))
    prohibited = set(construction["prohibited_inputs"])
    if not any(path.endswith("public-procedural-guide.md") for path in prohibited):
        raise ValueError("independent-rubric construction does not prohibit guide")
    if not any(path.endswith("shared-rubric.json") for path in prohibited):
        raise ValueError("independent-rubric construction does not prohibit shared rubric")
    if set(protocol["claim_boundaries"]) != CLAIM_KEYS or any(protocol["claim_boundaries"].values()):
        raise ValueError("unsupported claim upgrade")
    estimands = {x["id"] for x in protocol["estimands"]}
    if estimands != {"skill_under_independent", "skill_under_shared", "rubric_on_identical_outputs", "skill_by_rubric_interaction"}:
        raise ValueError("estimand drift")


def _score_rubric(base_grade: dict[str, Any], rubric: dict[str, Any]) -> dict[str, Any]:
    checks = base_grade["checks"]
    rows = []
    for criterion in rubric["criteria"]:
        unknown = set(criterion["all"]) - set(checks)
        if unknown:
            raise ValueError(f"unknown check in rubric {rubric['rubric_id']}: {sorted(unknown)}")
        passed = all(checks[name] is True for name in criterion["all"])
        rows.append({"criterion_id": criterion["id"], "passed": passed, "points_awarded": criterion["points"] if passed else 0, "points_possible": criterion["points"], "observed_checks": {name: checks[name] for name in criterion["all"]}})
    earned = sum(row["points_awarded"] for row in rows)
    possible = sum(row["points_possible"] for row in rows)
    return {"rubric_id": rubric["rubric_id"], "score": earned, "possible": possible, "proportion": round(earned / possible, 6), "criteria": rows}


def grade_attempt(run: Path, protocol: dict[str, Any], scorer_order: list[str] | None = None) -> dict[str, Any]:
    grader_path = ROOT / next(x["path"] for x in protocol["frozen_components"] if x["role"] == "base_grader")
    grader = _load_module(grader_path, "matrix_base_grader")
    base_grade = grader.grade_trial(run)
    rubrics = {
        "independent": load_json(ROOT / next(x["path"] for x in protocol["frozen_components"] if x["role"] == "independent_rubric")),
        "shared": load_json(ROOT / next(x["path"] for x in protocol["frozen_components"] if x["role"] == "shared_rubric")),
    }
    order = scorer_order or ["independent", "shared"]
    if sorted(order) != ["independent", "shared"]:
        raise ValueError("scorer order must contain each frozen rubric exactly once")
    scored = {name: _score_rubric(base_grade, rubrics[name]) for name in order}
    # Canonical serialization order prevents scorer invocation order becoming evidence.
    canonical = {name: scored[name] for name in ("independent", "shared")}
    return {"base_grade": base_grade, "rubric_grades": canonical}


def _evidence(run: Path, relative: str, role: str) -> dict[str, Any]:
    path = run / relative
    if not path.is_file():
        raise ValueError(f"missing retained evidence: {run.name}/{relative}")
    return {"path": relative, "sha256": sha256(path), "bytes": path.stat().st_size, "role": role}


def record_attempt(protocol: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    run = MATRIX / "attempts" / row["attempt_id"]
    trial_path = run / "trial-report.json"
    if not trial_path.is_file():
        raise ValueError(f"declared attempt missing; no silent exclusion: {row['attempt_id']}")
    trial = load_json(trial_path)
    canary = load_json(run / "preflight/canary-report.json")
    usage_path = run / "trial/outputs/usage.json"
    usage = load_json(usage_path) if usage_path.is_file() else {}
    service_available = trial.get("returncode") == 0 and trial.get("complete") is True and usage.get("completed") is True and usage.get("failed") is False
    if service_available and not (usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0):
        raise ValueError(f"cost gate violated: {row['attempt_id']}")
    valid = bool(service_available and canary.get("passed") and trial.get("valid_environment"))
    grade = grade_attempt(run, protocol, row["scorer_order"])
    write_json(run / "dual-rubric-grade.json", grade)
    retained = [
        _evidence(run, "preflight/canary-report.json", "zero-call condition and private-rubric firewall"),
        _evidence(run, "trial-report.json", "configured-system, condition, environment, and artifact record"),
        _evidence(run, "redacted-trace.log", "stdout-only redacted trace"),
        _evidence(run, "launcher-stderr.log", "launcher/provider stderr"),
        _evidence(run, "dual-rubric-grade.json", "both frozen rubrics over identical output bytes"),
    ]
    for name in ("usage.json", "incident-brief.md", "action-plan.json"):
        if (run / "trial/outputs" / name).is_file():
            retained.append(_evidence(run, f"trial/outputs/{name}", f"retained output {name}"))
    manifest = {
        "schema_version": "0.1.0", "attempt_id": row["attempt_id"], "execution_order": row["execution_order"],
        "skill_condition": row["skill_condition"], "scorer_order": row["scorer_order"], "service_available": service_available,
        "valid_trial": valid, "substantive_denominator_included": valid,
        "observed_outcome": grade["base_grade"]["observed_outcome"] if valid else None,
        "rubric_scores": ({name: grade["rubric_grades"][name]["proportion"] for name in ("independent", "shared")} if valid else None),
        "usage": {key: usage.get(key) for key in ("api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens", "estimated_cost_usd", "cost_status", "completed", "failed")},
        "protocol": {"path": PROTOCOL_PATH.relative_to(ROOT).as_posix(), "sha256": sha256(PROTOCOL_PATH)},
        "retained_evidence": retained, "claim_boundaries": copy.deepcopy(protocol["claim_boundaries"]),
    }
    write_json(run / "execution-manifest.json", manifest)
    return manifest


def verify_attempt(protocol: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    run = MATRIX / "attempts" / row["attempt_id"]
    manifest = load_json(run / "execution-manifest.json")
    if (manifest["attempt_id"], manifest["skill_condition"], manifest["execution_order"], manifest["scorer_order"]) != (row["attempt_id"], row["skill_condition"], row["execution_order"], row["scorer_order"]):
        raise ValueError("condition/order leakage or schedule mismatch")
    if set(manifest["claim_boundaries"]) != CLAIM_KEYS or any(manifest["claim_boundaries"].values()):
        raise ValueError("attempt claim upgrade")
    _assert_hash(ROOT / manifest["protocol"]["path"], manifest["protocol"]["sha256"], "attempt protocol")
    for item in manifest["retained_evidence"]:
        _assert_hash(run / item["path"], item["sha256"], f"{row['attempt_id']} evidence")
    replay = grade_attempt(run, protocol, row["scorer_order"])
    retained = load_json(run / "dual-rubric-grade.json")
    if replay != retained:
        raise ValueError("dual-rubric replay mismatch")
    reverse = grade_attempt(run, protocol, list(reversed(row["scorer_order"])))
    if reverse != retained:
        raise ValueError("scorer-order effect detected")
    return manifest


def _mean(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def _sample_sd(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    mean = sum(values) / len(values)
    return round(math.sqrt(sum((x - mean) ** 2 for x in values) / (len(values) - 1)), 6)


def build_report(protocol: dict[str, Any]) -> dict[str, Any]:
    rows = [verify_attempt(protocol, row) for row in protocol["attempt_schedule"]]
    if len(rows) != 6:
        raise ValueError("silent exclusion detected")
    valid = [row for row in rows if row["valid_trial"]]
    cells: dict[str, dict[str, Any]] = {}
    for condition in ("no_skill", "public_skill"):
        condition_rows = [row for row in rows if row["skill_condition"] == condition]
        valid_rows = [row for row in condition_rows if row["valid_trial"]]
        cells[condition] = {
            "declared_attempts": 3, "retained_attempts": len(condition_rows), "valid_attempts": len(valid_rows),
            "invalid_or_missing_attempts": 3 - len(valid_rows),
            "scores": {rubric: [row["rubric_scores"][rubric] for row in valid_rows] for rubric in ("independent", "shared")},
        }
        for rubric in ("independent", "shared"):
            values = cells[condition]["scores"][rubric]
            cells[condition].setdefault("descriptive", {})[rubric] = {"mean": _mean(values), "sample_sd": _sample_sd(values), "min": min(values) if values else None, "max": max(values) if values else None}
    def contrast(rubric: str) -> float | None:
        a, b = cells["no_skill"]["descriptive"][rubric]["mean"], cells["public_skill"]["descriptive"][rubric]["mean"]
        return round(b - a, 6) if a is not None and b is not None else None
    independent_effect = contrast("independent")
    shared_effect = contrast("shared")
    paired_rubric = [round(row["rubric_scores"]["shared"] - row["rubric_scores"]["independent"], 6) for row in valid]
    report = {
        "schema_version": "0.1.0", "report_id": "vendor-v2-skill-rubric-matrix-v1",
        "protocol": {"path": PROTOCOL_PATH.relative_to(ROOT).as_posix(), "sha256": sha256(PROTOCOL_PATH)},
        "integrity_valid": True, "declared_attempts": 6, "retained_attempts": len(rows), "valid_attempts": len(valid),
        "attempt_rows": [{"attempt_id": row["attempt_id"], "execution_order": row["execution_order"], "skill_condition": row["skill_condition"], "service_available": row["service_available"], "valid_trial": row["valid_trial"], "rubric_scores": row["rubric_scores"], "usage": row["usage"], "execution_manifest_path": (MATRIX / "attempts" / row["attempt_id"] / "execution-manifest.json").relative_to(ROOT).as_posix(), "execution_manifest_sha256": sha256(MATRIX / "attempts" / row["attempt_id"] / "execution-manifest.json")} for row in rows],
        "cells": cells,
        "estimands": {
            "skill_under_independent": independent_effect,
            "skill_under_shared": shared_effect,
            "rubric_on_identical_outputs": {"paired_differences": paired_rubric, "mean_difference": _mean(paired_rubric)},
            "skill_by_rubric_interaction": (round(shared_effect - independent_effect, 6) if shared_effect is not None and independent_effect is not None else None),
        },
        "uncertainty": {
            "attempt_boundary": "Cell means, sample SD, ranges, and all retained rows are descriptive; n=3 per condition is not a powered effect study.",
            "source_task_cluster_boundary": "Exactly one synthetic source-task cluster. Cluster-level uncertainty and cross-task generalization are not estimable; attempts are not independent task samples.",
        },
        "claim_boundaries": copy.deepcopy(protocol["claim_boundaries"]),
        "interpretation": "This prospective internal matrix can describe package differences and rubric-lineage sensitivity on one frozen synthetic task/configured system. It cannot establish a general Skill effect, capability, professional validity, safety, production fitness, cross-domain generality, or readiness.",
    }
    if any(report["claim_boundaries"].values()):
        raise ValueError("report claim upgrade")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("validate", "record", "replay"))
    args = parser.parse_args()
    protocol = load_json(PROTOCOL_PATH)
    verify_protocol(protocol)
    if args.mode == "record":
        for row in protocol["attempt_schedule"]:
            record_attempt(protocol, row)
        write_json(REPORT_PATH, build_report(protocol))
    elif args.mode == "replay":
        replayed = build_report(protocol)
        if replayed != load_json(REPORT_PATH):
            raise ValueError("matrix report replay mismatch")
    print(json.dumps({"mode": args.mode, "protocol": PROTOCOL_PATH.relative_to(ROOT).as_posix(), "status": "verified"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
