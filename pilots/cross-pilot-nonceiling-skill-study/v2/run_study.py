#!/usr/bin/env python3
"""Execute and replay the frozen v2 cross-pilot non-ceiling study.

This additive runner consumes protocol.json without modifying the frozen v2
instrument. It fails closed on the pushed pre-call gate, component hashes,
provider-reported included-cost evidence, schedule drift, filesystem isolation,
and denominator drift. Every scheduled attempt is retained exactly once.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
STUDY = Path(__file__).resolve().parent
PROTOCOL_PATH = STUDY / "protocol.json"
EXECUTION = STUDY / "execution"
FROZEN_GATE_COMMIT = "b8a9e72"
BASE_LAUNCHER = ROOT / "pilots/configured-artifact-revision/launcher.py"
CLAIM_KEYS = {
    "cross_domain_generality", "expert_validity", "general_skill_treatment_effect",
    "production_fitness", "professional_validity", "readiness", "safety",
    "task_cluster_capability",
}
USAGE_KEYS = (
    "api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens",
    "estimated_cost_usd", "cost_status", "completed", "failed", "model", "provider",
)


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_module("nonceiling_v2_base_launcher", BASE_LAUNCHER)
grader = load_module("nonceiling_v2_frozen_grader", STUDY / "calibration/grade_calibration.py")
validator = load_module("nonceiling_v2_protocol_validator", STUDY / "validate_protocol.py")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def inventory(root: Path) -> dict[str, dict[str, Any]]:
    return {
        path.relative_to(root).as_posix(): {"sha256": sha(path), "bytes": path.stat().st_size}
        for path in sorted(root.rglob("*")) if path.is_file()
    }


def verify_frozen_gate(protocol: dict[str, Any]) -> dict[str, Any]:
    errors = validator.validate(protocol, check_paths=True)
    if errors:
        raise ValueError(f"frozen protocol invalid: {errors}")
    if set(protocol.get("claim_boundaries", {})) != CLAIM_KEYS or any(protocol["claim_boundaries"].values()):
        raise ValueError("claim ceiling drift")
    calibration = load_json(STUDY / "calibration/calibration-report.json")
    canaries = load_json(STUDY / "preflight/canary-report.json")
    if not calibration.get("passed") or calibration.get("model_calls") != 0:
        raise ValueError("frozen calibration gate is not passing zero-call evidence")
    if not canaries.get("passed") or canaries.get("model_calls") != 0 or len(canaries.get("reports", [])) != 6:
        raise ValueError("frozen six-canary gate is not passing zero-call evidence")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FROZEN_GATE_COMMIT, "HEAD"], cwd=ROOT,
        capture_output=True, text=True,
    )
    if ancestor.returncode != 0:
        raise ValueError(f"required pushed gate commit {FROZEN_GATE_COMMIT} is not an ancestor of HEAD")
    committed = subprocess.run(
        ["git", "show", f"{FROZEN_GATE_COMMIT}:pilots/cross-pilot-nonceiling-skill-study/v2/protocol.json"],
        cwd=ROOT, capture_output=True,
    )
    if committed.returncode != 0 or hashlib.sha256(committed.stdout).hexdigest() != sha(PROTOCOL_PATH):
        raise ValueError("protocol bytes differ from pushed frozen gate commit")
    return {
        "passed": True, "frozen_gate_commit": FROZEN_GATE_COMMIT,
        "protocol_sha256": sha(PROTOCOL_PATH),
        "calibration_report_sha256": sha(STUDY / "calibration/calibration-report.json"),
        "canary_report_sha256": sha(STUDY / "preflight/canary-report.json"),
        "frozen_component_count": len(protocol["frozen_components"]),
    }


def provider_cost_gate() -> dict[str, Any]:
    """Use the newest retained report from this exact provider/model as pre-call evidence."""
    candidates: list[tuple[float, Path, dict[str, Any]]] = []
    for path in ROOT.glob("pilots/**/usage.json"):
        try:
            value = load_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        if (
            value.get("provider") == "openai-codex" and value.get("model") == "gpt-5.6-sol"
            and value.get("cost_status") == "included" and value.get("estimated_cost_usd") == 0.0
            and value.get("completed") is True and value.get("failed") is False
        ):
            candidates.append((path.stat().st_mtime, path, value))
    if not candidates:
        raise ValueError("no retained provider-reported included USD 0.00 evidence for configured system")
    _, path, value = max(candidates)
    report = {
        "passed": True, "kind": "provider_reported_included_cost_pre_call_gate",
        "evidence_path": path.relative_to(ROOT).as_posix(), "evidence_sha256": sha(path),
        "provider": value["provider"], "model": value["model"],
        "cost_status": value["cost_status"], "estimated_cost_usd": value["estimated_cost_usd"],
        "completed": value["completed"], "failed": value["failed"],
        "boundary": "Historical authenticated-provider evidence gates the first call; each new attempt must independently report included USD 0.00 or later calls stop.",
    }
    dump(EXECUTION / "provider-cost-gate.json", report)
    return report


def schedule_row(protocol: dict[str, Any], attempt_id: str) -> dict[str, Any]:
    rows = [row for row in protocol["attempt_schedule"] if row["attempt_id"] == attempt_id]
    if len(rows) != 1:
        raise ValueError(f"attempt not declared exactly once: {attempt_id}")
    return rows[0]


def materialize(root: Path, row: dict[str, Any]) -> dict[str, Path]:
    if root.exists():
        raise FileExistsError(f"one-attempt/no-replacement root already exists: {root}")
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    (inputs / "outputs").mkdir(parents=True)
    outputs.mkdir()
    cluster, condition = row["cluster"], row["skill_condition"]
    shutil.copy2(STUDY / cluster / "public-task.md", inputs / "public-task.md")
    if cluster == "lh":
        shutil.copytree(STUDY / "lh/sources", inputs / "sources")
    else:
        shutil.copytree(STUDY / "vendor/workspace", inputs / "workspace", ignore=shutil.ignore_patterns("protected"))
    if condition == "public_skill":
        shutil.copy2(STUDY / cluster / "public-guide.md", inputs / "public-guide.md")
    elif condition != "no_skill":
        raise ValueError(f"invalid Skill condition: {condition}")
    manifest = {
        "schema_version": "0.2.0", "attempt_id": row["attempt_id"], "cluster": cluster,
        "skill_condition": condition, "inputs": "read_only", "only_writable": "outputs",
        "agent_toolsets": ["file"], "live_endpoint_tools": [],
        "excluded_roles": load_json(PROTOCOL_PATH)["firewalls"]["agent_prohibited_roles"],
    }
    dump(inputs / "manifest.json", manifest)
    base._copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


def private_probes(row: dict[str, Any]) -> list[str]:
    cluster, condition = row["cluster"], row["skill_condition"]
    probes = [
        "/home/sam/skill-bench/data/work_queue.json", "/trial/protocol.json",
        f"/trial/{cluster}/rubrics/independent.json", f"/trial/{cluster}/rubrics/shared.json",
        "/trial/calibration/calibration-report.json", "/trial/other-attempts",
    ]
    if condition == "no_skill":
        probes.append("/trial/public-guide.md")
    if cluster == "vendor":
        probes.append("/trial/workspace/protected/incident-lock.txt")
    return probes


def in_trial_canary(root: Path, row: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Path]]:
    paths = materialize(root, row)
    visible = ["public-task.md", "manifest.json"]
    visible += [p.relative_to(paths["inputs"]).as_posix() for p in sorted(paths["inputs"].rglob("*")) if p.is_file() and p.name != "manifest.json"]
    code = "VISIBLE=" + repr(visible) + "\nPRIVATE=" + repr(private_probes(row)) + "\n" + r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool
def readable(path):
    text=read_file_tool(path,limit=5).lower()
    return not any(x in text for x in ("error reading","not found","permission denied","does not exist"))
obs={"cwd":os.getcwd(),"visible":{p:readable(p) for p in VISIBLE},"private_denied":{p:not readable(p) for p in PRIVATE},"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=20)}
obs["output_write"]="error" not in write_file_tool("outputs/in-trial-canary.txt","ok\n").lower()
obs["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower()
print(json.dumps(obs,sort_keys=True))
'''
    proc = subprocess.run(base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        observed = {}
    passed = (
        proc.returncode == 0 and observed.get("cwd") == "/trial"
        and all(observed.get("visible", {}).values()) and all(observed.get("private_denied", {}).values())
        and "skill-bench" not in str(observed.get("repository_search", ""))
        and observed.get("output_write") is True and observed.get("escape_denied") is True
    )
    report = {
        "passed": passed, "model_calls": 0, "attempt_id": row["attempt_id"],
        "cluster": row["cluster"], "condition": row["skill_condition"],
        "observed": observed, "returncode": proc.returncode, "stderr": proc.stderr[-2000:],
        "input_inventory": inventory(paths["inputs"]),
    }
    dump(root.parent / "in-trial-canary.json", report)
    if not passed:
        shutil.rmtree(paths["profile"], ignore_errors=True)
        raise RuntimeError(f"in-trial canary failed: {row['attempt_id']}")
    return report, paths


def trial_command(prompt: str) -> list[str]:
    return [
        "/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt,
        "--usage-file", "/trial/outputs/usage.json", "--model", "gpt-5.6-sol",
        "--provider", "openai-codex", "--toolsets", "file", "--safe-mode",
    ]


def grade_outputs(row: dict[str, Any], output_dir: Path, input_integrity: bool) -> dict[str, Any]:
    grades = {}
    for lineage in ("independent", "shared"):
        rubric_path = STUDY / row["cluster"] / "rubrics" / f"{lineage}.json"
        rubric = load_json(rubric_path)
        value = grader.grade_lh(output_dir, rubric) if row["cluster"] == "lh" else grader.grade_vendor(output_dir, rubric, input_integrity)
        value["rubric_sha256"] = sha(rubric_path)
        grades[lineage] = value
    return {"identical_output_inventory": inventory(output_dir), "grades": grades}


def run_attempt(protocol: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    root = EXECUTION / "attempts" / row["attempt_id"]
    canary, paths = in_trial_canary(root / "trial", row)
    before = inventory(paths["inputs"])
    prompt = (paths["inputs"] / "public-task.md").read_text(encoding="utf-8")
    if row["skill_condition"] == "public_skill":
        prompt += "\n\nA public procedural guide is available at public-guide.md; use it as optional guidance."
    else:
        prompt += "\n\nNo procedural guide is assigned; complete the disclosed task from supplied inputs."
    proc = subprocess.run(base._bwrap(paths, trial_command(prompt)), capture_output=True, text=True, timeout=900)
    (root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    after = inventory(paths["inputs"])
    changed = sorted(set(before) ^ set(after) | {key for key in before.keys() & after.keys() if before[key] != after[key]})
    usage_path = paths["outputs"] / "usage.json"
    usage = load_json(usage_path) if usage_path.is_file() else {}
    required = set(protocol["clusters"][row["cluster"]]["required_outputs"])
    complete = proc.returncode == 0 and required <= {p.name for p in paths["outputs"].iterdir() if p.is_file()} and usage_path.is_file()
    cost_ok = usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
    service = complete and usage.get("completed") is True and usage.get("failed") is False
    valid_environment = canary["passed"] and not changed
    dual = grade_outputs(row, paths["outputs"], not changed) if service and valid_environment else None
    if dual is not None:
        dump(root / "dual-rubric-grade.json", dual)
    trial = {
        "schema_version": "0.2.0", "kind": "cross_pilot_nonceiling_agent_attempt",
        "attempt_id": row["attempt_id"], "execution_order": row["execution_order"],
        "cluster": row["cluster"], "skill_condition": row["skill_condition"],
        "launcher_invocations": 1, "replacement_for": row["replacement_for"],
        "returncode": proc.returncode, "complete": complete, "service_available": service,
        "valid_environment": valid_environment, "cost_gate_passed": cost_ok,
        "rubric_eligible": bool(service and valid_environment and cost_ok and dual is not None),
        "configured_system": protocol["configured_system"], "protocol_sha256": sha(PROTOCOL_PATH),
        "input_manifest_sha256": sha(paths["inputs"] / "manifest.json"),
        "input_integrity": {"changed_read_only_inputs": changed},
        "artifacts": inventory(paths["outputs"]),
        "usage": {key: usage.get(key) for key in USAGE_KEYS},
        "trace": {"path": "redacted-trace.log", "sha256": sha(root / "redacted-trace.log")},
        "claim_boundaries": protocol["claim_boundaries"],
    }
    dump(root / "trial-report.json", trial)
    shutil.rmtree(paths["profile"], ignore_errors=True)
    if service and not cost_ok:
        raise RuntimeError(f"provider cost gate failed after {row['attempt_id']}; later calls must stop")
    return trial


def retained_record(protocol: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    root = EXECUTION / "attempts" / row["attempt_id"]
    trial_path = root / "trial-report.json"
    if not trial_path.is_file():
        return {
            "attempt_id": row["attempt_id"], "execution_order": row["execution_order"],
            "cluster": row["cluster"], "skill_condition": row["skill_condition"],
            "status": "unstarted", "rubric_eligible": False, "rubric_scores": None,
            "claim_boundaries": protocol["claim_boundaries"],
        }
    trial = load_json(trial_path)
    if (trial["attempt_id"], trial["execution_order"], trial["cluster"], trial["skill_condition"]) != (
        row["attempt_id"], row["execution_order"], row["cluster"], row["skill_condition"]
    ):
        raise ValueError(f"attempt schedule drift: {row['attempt_id']}")
    if trial["launcher_invocations"] != 1 or trial["replacement_for"] is not None:
        raise ValueError(f"retry/replacement drift: {row['attempt_id']}")
    if set(trial["claim_boundaries"]) != CLAIM_KEYS or any(trial["claim_boundaries"].values()):
        raise ValueError(f"attempt claim upgrade: {row['attempt_id']}")
    eligible = trial["rubric_eligible"]
    dual_path = root / "dual-rubric-grade.json"
    scores = None
    if eligible:
        retained = load_json(dual_path)
        replay = grade_outputs(row, root / "trial/outputs", not trial["input_integrity"]["changed_read_only_inputs"])
        if replay != retained:
            raise ValueError(f"dual-rubric replay mismatch: {row['attempt_id']}")
        scores = {key: retained["grades"][key]["score"] for key in ("independent", "shared")}
    return {
        "attempt_id": row["attempt_id"], "execution_order": row["execution_order"],
        "cluster": row["cluster"], "skill_condition": row["skill_condition"],
        "status": "eligible" if eligible else ("service_failure" if not trial["service_available"] else "invalid"),
        "rubric_eligible": eligible, "rubric_scores": scores, "usage": trial["usage"],
        "trial_report_sha256": sha(trial_path),
        "dual_rubric_grade_sha256": sha(dual_path) if dual_path.is_file() else None,
        "claim_boundaries": trial["claim_boundaries"],
    }


def mean(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def sample_sd(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    avg = sum(values) / len(values)
    return round(math.sqrt(sum((value - avg) ** 2 for value in values) / (len(values) - 1)), 6)


def build_report(protocol: dict[str, Any]) -> dict[str, Any]:
    rows = [retained_record(protocol, row) for row in protocol["attempt_schedule"]]
    if len(rows) != 8 or {row["attempt_id"] for row in rows} != {row["attempt_id"] for row in protocol["attempt_schedule"]}:
        raise ValueError("denominator/exclusion drift")
    cells: dict[str, Any] = {}
    for cluster in ("lh", "vendor"):
        cells[cluster] = {}
        for condition in ("no_skill", "public_skill"):
            subset = [row for row in rows if row["cluster"] == cluster and row["skill_condition"] == condition]
            eligible = [row for row in subset if row["rubric_eligible"]]
            scores = {rubric: [row["rubric_scores"][rubric] for row in eligible] for rubric in ("independent", "shared")}
            cells[cluster][condition] = {
                "declared": 2, "retained": len(subset), "eligible": len(eligible),
                "invalid_missing_or_service_failed": 2 - len(eligible), "scores": scores,
                "descriptive": {rubric: {"mean": mean(values), "sample_sd": sample_sd(values), "min": min(values) if values else None, "max": max(values) if values else None} for rubric, values in scores.items()},
            }
    estimands: dict[str, Any] = {}
    for cluster in ("lh", "vendor"):
        contrasts = {}
        for rubric in ("independent", "shared"):
            no = cells[cluster]["no_skill"]["descriptive"][rubric]["mean"]
            skill = cells[cluster]["public_skill"]["descriptive"][rubric]["mean"]
            contrasts[rubric] = round(skill - no, 6) if no is not None and skill is not None else None
        eligible = [row for row in rows if row["cluster"] == cluster and row["rubric_eligible"]]
        within = [round(row["rubric_scores"]["shared"] - row["rubric_scores"]["independent"], 6) for row in eligible]
        estimands[cluster] = {
            "skill_under_independent": contrasts["independent"],
            "skill_under_shared": contrasts["shared"],
            "within_output_shared_minus_independent": {"values": within, "mean": mean(within)},
            "skill_by_rubric_interaction": round(contrasts["shared"] - contrasts["independent"], 6) if None not in contrasts.values() else None,
        }
    report = {
        "schema_version": "0.2.0", "report_id": "cross-pilot-nonceiling-skill-study-v2",
        "protocol": {"path": PROTOCOL_PATH.relative_to(ROOT).as_posix(), "sha256": sha(PROTOCOL_PATH)},
        "frozen_gate_commit": FROZEN_GATE_COMMIT, "declared_attempts": 8,
        "retained_attempts": len(rows), "eligible_attempts": sum(row["rubric_eligible"] for row in rows),
        "attempt_rows": rows, "cells": cells, "estimands_by_cluster": estimands,
        "cluster_heterogeneity": "Two exact cluster contrasts are reported side by side and are not pooled or treated as population samples.",
        "claim_boundaries": protocol["claim_boundaries"],
        "interpretation": "Exact-version, two-cluster internal package contrasts only. Attempts are repeated executions nested in purposively selected synthetic clusters, not independent task samples. No general Skill treatment effect, capability, expert/professional validity, safety, production fitness, cross-domain generality, or readiness claim is licensed.",
    }
    if any(report["claim_boundaries"].values()):
        raise ValueError("report claim upgrade")
    return report


def execute() -> dict[str, Any]:
    protocol = load_json(PROTOCOL_PATH)
    gate = verify_frozen_gate(protocol)
    if EXECUTION.exists():
        raise FileExistsError("execution directory already exists; retry/replacement is prohibited")
    EXECUTION.mkdir()
    dump(EXECUTION / "frozen-gate-verification.json", gate)
    provider_cost_gate()
    for row in protocol["attempt_schedule"]:
        run_attempt(protocol, row)
    report = build_report(protocol)
    dump(EXECUTION / "study-report.json", report)
    return report


def replay() -> dict[str, Any]:
    protocol = load_json(PROTOCOL_PATH)
    verify_frozen_gate(protocol)
    report = build_report(protocol)
    retained = load_json(EXECUTION / "study-report.json")
    if report != retained:
        raise ValueError("study report replay mismatch")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("validate", "execute", "replay"))
    args = parser.parse_args()
    protocol = load_json(PROTOCOL_PATH)
    if args.mode == "validate":
        result = verify_frozen_gate(protocol)
    elif args.mode == "execute":
        result = execute()
    else:
        result = replay()
    print(json.dumps({"mode": args.mode, "status": "verified", "declared_attempts": result.get("declared_attempts", 8), "eligible_attempts": result.get("eligible_attempts")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
