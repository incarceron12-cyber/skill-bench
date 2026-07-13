#!/usr/bin/env python3
"""Prospective vendor-v2 Skill-condition runner with rubric/private-input firewalls."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/vendor-incident-response"
MATRIX = PILOT / "trials/skill-rubric-matrix-v1"
PROTOCOL_PATH = MATRIX / "protocol.json"
GUIDE = MATRIX / "public-procedural-guide.md"
BASE_PATH = ROOT / "scripts/vendor_incident_isolated_launcher.py"

_spec = importlib.util.spec_from_file_location("vendor_base_launcher", BASE_PATH)
assert _spec is not None and _spec.loader is not None
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _condition(protocol: dict[str, Any], attempt_id: str) -> str:
    rows = [row for row in protocol["attempt_schedule"] if row["attempt_id"] == attempt_id]
    if len(rows) != 1:
        raise ValueError(f"attempt must be declared exactly once: {attempt_id}")
    return rows[0]["skill_condition"]


def _snapshot(run_root: Path, condition: str) -> Path:
    inputs = run_root / "inputs"
    if inputs.exists():
        raise FileExistsError(f"run root is not unique/clean: {inputs}")
    (inputs / "workspace").mkdir(parents=True)
    (inputs / "outputs").mkdir()
    shutil.copy2(base.TASK, inputs / "public-task.md")
    for source in base.VISIBLE_SOURCES:
        relative = source.relative_to(PILOT / "workspace")
        target = inputs / "workspace" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    if condition == "public_skill":
        shutil.copy2(GUIDE, inputs / "public-procedural-guide.md")
    elif condition != "no_skill":
        raise ValueError(f"unknown condition: {condition}")
    workspace = [
        {"path": p.relative_to(inputs).as_posix(), "sha256": sha256(p)}
        for p in sorted((inputs / "workspace").rglob("*")) if p.is_file()
    ]
    manifest = {
        "schema_version": "0.1.0",
        "skill_condition": condition,
        "public_task": {"path": "public-task.md", "sha256": sha256(base.TASK)},
        "workspace": workspace,
        "procedural_guide": ({"path": "public-procedural-guide.md", "sha256": sha256(GUIDE)} if condition == "public_skill" else None),
        "excluded_private_inputs": [
            "protocol.json", "rubrics/independent-rubric.json", "rubrics/shared-rubric.json",
            "grade_v2.py", "pilot-manifest.json", "calibration-cases.json",
            "workspace/protected/incident-lock.txt"
        ],
        "policy": {"inputs": "read_only", "only_writable_task_path": "outputs", "agent_toolsets": ["file"], "live_endpoint_tools": []},
    }
    write_json(inputs / "manifest.json", manifest)
    return inputs


def _materialize(run_root: Path, condition: str) -> dict[str, Path]:
    inputs = _snapshot(run_root, condition)
    outputs = run_root / "outputs"
    profile = run_root / ".launcher-profile"
    outputs.mkdir()
    base._copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


def _private_probes(condition: str) -> tuple[str, ...]:
    probes = tuple(base.PRIVATE_PROBES) + (
        "/home/sam/skill-bench/pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/protocol.json",
        "/home/sam/skill-bench/pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/rubrics/independent-rubric.json",
        "/home/sam/skill-bench/pilots/vendor-incident-response/trials/skill-rubric-matrix-v1/rubrics/shared-rubric.json",
        "/trial/protocol.json", "/trial/rubrics/independent-rubric.json", "/trial/rubrics/shared-rubric.json",
    )
    if condition == "no_skill":
        probes += ("/trial/public-procedural-guide.md",)
    return probes


def canary(run_root: Path, condition: str) -> dict[str, Any]:
    paths = _materialize(run_root, condition)
    visible = ["public-task.md"] + ["workspace/" + p.relative_to(PILOT / "workspace").as_posix() for p in base.VISIBLE_SOURCES]
    if condition == "public_skill":
        visible.append("public-procedural-guide.md")
    code = "PRIVATE=" + repr(_private_probes(condition)) + "\nVISIBLE=" + repr(visible) + "\n" + r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool

def readable(path):
    value = read_file_tool(path, limit=5)
    return not any(x in value.lower() for x in ("error", "not found", "denied", "does not exist"))

observed = {
  "observed_cwd": os.getcwd(),
  "visible_inputs_readable": {p: readable(p) for p in VISIBLE},
  "private_reads_denied": {p: not readable(p) for p in PRIVATE},
  "repository_search": search_tool("skill-bench", target="files", path="/home/sam", limit=20),
  "configured_agent_toolsets": ["file"], "live_endpoint_tools": [],
}
write_ok = write_file_tool("outputs/canary.txt", "matrix-isolated-canary\n")
write_bad = write_file_tool("escape.txt", "must-not-write\n")
observed["output_write_succeeded"] = "error" not in write_ok.lower()
observed["outside_write_denied"] = any(x in write_bad.lower() for x in ("error", "denied", "read-only", "permission"))
print(json.dumps(observed, sort_keys=True))
'''
    proc = subprocess.run(base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), text=True, capture_output=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        observed = {}
    passed = (
        proc.returncode == 0 and observed.get("observed_cwd") == "/trial"
        and all(observed.get("visible_inputs_readable", {}).values())
        and all(observed.get("private_reads_denied", {}).values())
        and "skill-bench" not in str(observed.get("repository_search", ""))
        and observed.get("output_write_succeeded") is True
        and observed.get("outside_write_denied") is True
        and observed.get("configured_agent_toolsets") == ["file"]
        and observed.get("live_endpoint_tools") == []
    )
    report = {
        "schema_version": "0.1.0", "kind": "vendor_skill_matrix_outer_envelope_canary",
        "condition": condition, "passed": passed, "model_calls": 0,
        "launcher_sha256": sha256(Path(__file__)), "input_inventory": base._inventory(paths["inputs"]),
        "protected_sha256": sha256(base.PROTECTED), "observed": observed,
        "returncode": proc.returncode, "stderr": proc.stderr[-2000:],
        "limitations": ["Tests configured file-tool/mount visibility, not kernel resistance to an unconfigured terminal tool."],
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    write_json(run_root / "canary-report.json", report)
    if not passed:
        raise RuntimeError(f"fail-closed canary failed: {run_root / 'canary-report.json'}")
    return report


def construction_canary(run_root: Path) -> dict[str, Any]:
    """Prove the independent-rubric construction view excludes guide/private bytes."""
    manifest = load_json(MATRIX / "rubrics/independent-construction-manifest.json")
    inputs = run_root / "inputs"
    outputs = run_root / "outputs"
    profile = run_root / ".launcher-profile"
    if inputs.exists():
        raise FileExistsError(f"run root is not clean: {inputs}")
    inputs.mkdir(parents=True)
    (inputs / "outputs").mkdir()
    outputs.mkdir()
    for source_name in manifest["allowed_inputs"]:
        source = ROOT / source_name
        target = inputs / source.relative_to(PILOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    base._copy_runtime_profile(profile)
    paths = {"inputs": inputs, "outputs": outputs, "profile": profile}
    probes = tuple(str(ROOT / path) for path in manifest["prohibited_inputs"])
    code = "PRIVATE=" + repr(probes) + "\n" + r'''
import json, os
from tools.file_tools import read_file_tool, search_tool

def readable(path):
    value = read_file_tool(path, limit=5)
    return not any(x in value.lower() for x in ("error", "not found", "denied", "does not exist"))
print(json.dumps({"cwd": os.getcwd(), "prohibited_denied": {p: not readable(p) for p in PRIVATE}, "repository_search": search_tool("skill-bench", target="files", path="/home/sam", limit=20)}, sort_keys=True))
'''
    proc = subprocess.run(base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), text=True, capture_output=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        observed = {}
    passed = proc.returncode == 0 and observed.get("cwd") == "/trial" and all(observed.get("prohibited_denied", {}).values()) and "skill-bench" not in str(observed.get("repository_search", ""))
    report = {"kind": "independent_rubric_construction_firewall", "passed": passed, "model_calls": 0, "observed": observed, "allowed_input_inventory": base._inventory(inputs), "manifest_sha256": sha256(MATRIX / "rubrics/independent-construction-manifest.json")}
    shutil.rmtree(profile, ignore_errors=True)
    write_json(run_root / "canary-report.json", report)
    if not passed:
        raise RuntimeError("independent-rubric construction firewall failed")
    return report


def run_trial(run_root: Path, condition: str) -> dict[str, Any]:
    preflight = canary(run_root / "preflight", condition)
    paths = _materialize(run_root / "trial", condition)
    before = base._inventory(paths["inputs"])
    protected_before = sha256(base.PROTECTED)
    condition_instruction = (
        "A public procedural guide is available at public-procedural-guide.md; use it as optional guidance."
        if condition == "public_skill" else
        "No procedural guide is assigned in this condition; complete the public task from its disclosed sources."
    )
    prompt = base.TASK.read_text(encoding="utf-8") + "\n\nCondition instruction: " + condition_instruction
    proc = subprocess.run(base._bwrap(paths, base._trial_command(prompt)), text=True, capture_output=True, timeout=900)
    (run_root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (run_root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    after = base._inventory(paths["inputs"])
    artifacts = {name: {"sha256": sha256(paths["outputs"] / name), "bytes": (paths["outputs"] / name).stat().st_size} for name in base.OUTPUT_NAMES if (paths["outputs"] / name).is_file()}
    workspace_diff = {"changed_read_only_inputs": sorted(set(before) ^ set(after) | {p for p in before.keys() & after.keys() if before[p] != after[p]}), "created_outputs": sorted(artifacts), "protected_unchanged": protected_before == sha256(base.PROTECTED)}
    complete = proc.returncode == 0 and set(base.OUTPUT_NAMES) <= set(artifacts)
    report = {
        "schema_version": "0.1.0", "kind": "vendor_skill_matrix_agent_trial", "attempt_id": run_root.name,
        "blinded_agent_id": True, "skill_condition": condition, "complete": complete, "returncode": proc.returncode,
        "valid_environment": preflight["passed"] and not workspace_diff["changed_read_only_inputs"] and workspace_diff["protected_unchanged"],
        "configured_system": {"hermes_runtime_sha256": sha256(base.HERMES_RUNTIME / "hermes"), "model": "gpt-5.6-sol", "provider": "openai-codex", "toolsets": ["file"], "safe_mode": True, "invocation": "oneshot", "max_turns": 40},
        "task_sha256": sha256(base.TASK), "guide_sha256": sha256(GUIDE) if condition == "public_skill" else None,
        "launcher_sha256": sha256(Path(__file__)), "input_manifest_sha256": sha256(paths["inputs"] / "manifest.json"),
        "artifacts": artifacts, "workspace_diff": workspace_diff,
        "trace": {"path": "redacted-trace.log", "sha256": sha256(run_root / "redacted-trace.log"), "policy": "stdout only; raw provider request/session state and headers not retained"},
        "usage_path": "trial/outputs/usage.json" if "usage.json" in artifacts else None,
        "claim_boundaries": {"general_skill_effect": False, "capability": False, "professional_validity": False, "safety": False, "production_fitness": False, "cross_domain_generality": False, "readiness": False},
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    write_json(run_root / "trial-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("canary", "construction-canary", "run"))
    parser.add_argument("--attempt-id")
    parser.add_argument("--run-root", type=Path)
    args = parser.parse_args()
    protocol = load_json(PROTOCOL_PATH)
    if args.mode == "construction-canary":
        root = (args.run_root or MATRIX / "preflight/independent-construction").resolve()
        report = construction_canary(root)
    else:
        if not args.attempt_id:
            parser.error("--attempt-id is required")
        condition = _condition(protocol, args.attempt_id)
        root = (args.run_root or MATRIX / "attempts" / args.attempt_id).resolve()
        report = canary(root, condition) if args.mode == "canary" else run_trial(root, condition)
    print(json.dumps({"mode": args.mode, "report": report.get("kind"), "passed": report.get("passed"), "complete": report.get("complete"), "valid_environment": report.get("valid_environment")}, indent=2))
    return 0 if report.get("passed", report.get("valid_environment", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
