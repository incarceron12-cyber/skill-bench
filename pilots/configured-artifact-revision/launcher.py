#!/usr/bin/env python3
"""Run one fail-closed, task-scoped artifact-revision attempt.

The benchmark package and private grader never enter the namespace. The agent
sees a retained snapshot containing only ``public-task.md`` and the four public
workspace sources; ``workspace/protected`` is deliberately absent. All task
inputs are mounted read-only and ``outputs`` is the only writable task path.
Hermes needs provider transport, but the configured agent receives only the
file toolset and therefore has no live-egress-capable tool.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "pilots/configured-artifact-revision"
HERMES_RUNTIME = Path("/home/sam/.hermes/hermes-agent")
PYTHON_RUNTIME = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
TASK = PILOT / "public-revision-request.md"
VISIBLE_SOURCES = (
    PILOT / "original-incident-brief.md",
    ROOT / "pilots/vendor-incident-response/workspace/current/signed-status.json",
)
PROTECTED = ROOT / "pilots/vendor-incident-response/pilot-manifest.json"
PRIVATE_PROBES = (
    "/home/sam/skill-bench/pilots/vendor-incident-response/pilot-manifest.json",
    "/home/sam/skill-bench/pilots/vendor-incident-response/calibration-cases.json",
    "/home/sam/skill-bench/pilots/vendor-incident-response/grade.py",
    "/home/sam/skill-bench/pilots/vendor-incident-response/evidence-chain-audit.json",
    "/home/sam/skill-bench/data/work_queue.json",
    "/trial/workspace/protected/incident-lock.txt",
)
OUTPUT_NAMES = ("revised-incident-brief.md", "usage.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _inventory(root: Path) -> dict[str, dict[str, Any]]:
    result = {}
    if root.exists():
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            result[path.relative_to(root).as_posix()] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    return result


def _copy_runtime_profile(destination: Path) -> None:
    source = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    destination.mkdir(parents=True, exist_ok=True)
    global_auth = Path(os.environ.get("HERMES_REAL_HOME", str(Path.home()))) / ".hermes/auth.json"
    if global_auth.exists():
        shutil.copy2(global_auth, destination / "auth.json")
    elif (source / "auth.json").exists():
        shutil.copy2(source / "auth.json", destination / "auth.json")
    if (source / ".env").exists():
        shutil.copy2(source / ".env", destination / ".env")
    (destination / "config.yaml").write_text(
        "model:\n  default: gpt-5.6-sol\n  provider: openai-codex\n"
        "agent:\n  max_turns: 40\nplatform_toolsets:\n  cli:\n    - file\n",
        encoding="utf-8",
    )


def _snapshot(run_root: Path) -> Path:
    inputs = run_root / "inputs"
    if inputs.exists():
        raise FileExistsError(f"run root is not unique/clean: {inputs}")
    (inputs / "workspace").mkdir(parents=True)
    # The read-only root needs an empty mount point for the writable output bind.
    (inputs / "outputs").mkdir()
    shutil.copy2(TASK, inputs / "public-task.md")
    for source in VISIBLE_SOURCES:
        relative = Path("original-incident-brief.md") if source == PILOT / "original-incident-brief.md" else Path("current/signed-status.json")
        target = inputs / "workspace" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    write_json(inputs / "manifest.json", {
        "schema_version": "0.1.0",
        "public_task": {"path": "public-task.md", "sha256": sha256(TASK)},
        "workspace": [{"path": p.relative_to(inputs).as_posix(), "sha256": sha256(p)} for p in sorted((inputs / "workspace").rglob("*")) if p.is_file()],
        "excluded_private_inputs": ["pilot-manifest.json", "calibration-cases.json", "grade.py", "grader-report.json", "evidence-chain-audit.json", "workspace/protected/incident-lock.txt"],
        "policy": {"inputs": "read_only", "only_writable_task_path": "outputs", "agent_toolsets": ["file"], "live_endpoint_tools": []},
    })
    return inputs


def _materialize(run_root: Path) -> dict[str, Path]:
    inputs = _snapshot(run_root)
    outputs = run_root / "outputs"
    profile = run_root / ".launcher-profile"
    outputs.mkdir()
    _copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


def _bwrap(paths: dict[str, Path], command: list[str]) -> list[str]:
    return [
        "bwrap", "--die-with-parent", "--new-session", "--unshare-pid",
        "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin",
        "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64",
        "--ro-bind", "/etc", "/etc", "--dir", "/run/systemd",
        "--ro-bind", "/run/systemd/resolve", "/run/systemd/resolve",
        "--dir", "/home", "--dir", "/home/sam",
        "--dir", "/home/sam/.local", "--dir", "/home/sam/.local/share",
        "--dir", "/home/sam/.local/share/uv", "--dir", "/home/sam/.local/share/uv/python",
        "--ro-bind", str(PYTHON_RUNTIME), str(PYTHON_RUNTIME),
        "--dir", "/opt/hermes", "--ro-bind", str(HERMES_RUNTIME), "/opt/hermes",
        "--bind", str(paths["profile"]), "/run/hermes-profile",
        "--ro-bind", str(paths["inputs"]), "/trial",
        "--bind", str(paths["outputs"]), "/trial/outputs",
        "--chdir", "/trial", "--setenv", "HOME", "/home/sam",
        "--setenv", "HERMES_REAL_HOME", "/home/sam",
        "--setenv", "HERMES_HOME", "/run/hermes-profile",
        "--setenv", "TERMINAL_CWD", "/trial", "--setenv", "PYTHONPATH", "/opt/hermes",
        "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
        "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID",
        "--unsetenv", "HERMES_SESSION_KEY", "--unsetenv", "HERMES_UI_SESSION_ID",
        "--", *command,
    ]


CANARY_CODE = r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool

def readable(path):
    value = read_file_tool(path, limit=5)
    return not any(x in value.lower() for x in ("error", "not found", "denied", "does not exist"))

def denied(path):
    return not readable(path)

visible = ["public-task.md", "workspace/original-incident-brief.md", "workspace/current/signed-status.json"]
result = {
  "observed_cwd": os.getcwd(),
  "visible_inputs_readable": {p: readable(p) for p in visible},
  "private_reads_denied": {p: denied(p) for p in PRIVATE},
  "repository_search": search_tool("skill-bench", target="files", path="/home/sam", limit=20),
  "configured_agent_toolsets": ["file"],
  "live_endpoint_tools": [],
}
write_ok = write_file_tool("outputs/canary.txt", "revision-isolated-canary\n")
write_bad = write_file_tool("escape.txt", "must-not-write\n")
result["output_write_succeeded"] = "error" not in write_ok.lower()
result["outside_write_denied"] = any(x in write_bad.lower() for x in ("error", "denied", "read-only", "permission"))
print(json.dumps(result, sort_keys=True))
'''


def canary(run_root: Path) -> dict[str, Any]:
    paths = _materialize(run_root)
    code = "PRIVATE=" + repr(PRIVATE_PROBES) + "\n" + CANARY_CODE
    proc = subprocess.run(_bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), text=True, capture_output=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1]) if proc.stdout.strip() else {}
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
        "schema_version": "0.1.0", "kind": "artifact_revision_outer_envelope_canary",
        "passed": passed, "model_calls": 0, "launcher_sha256": sha256(Path(__file__)),
        "input_inventory": _inventory(paths["inputs"]), "protected_sha256": sha256(PROTECTED),
        "isolation_substrate": "bubblewrap mount namespace", "observed": observed,
        "returncode": proc.returncode, "stderr": proc.stderr[-2000:],
        "network_boundary": "No live-egress-capable agent tool is configured. Provider transport remains execution infrastructure and is not a task action channel.",
        "limitations": ["The canary tests the configured file-tool surface and mount visibility, not kernel security against an unconfigured terminal tool."],
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    write_json(run_root / "canary-report.json", report)
    if not passed:
        raise RuntimeError(f"fail-closed canary failed: {run_root / 'canary-report.json'}")
    return report


def _trial_command(prompt: str) -> list[str]:
    return [
        "/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt,
        "--usage-file", "/trial/outputs/usage.json", "--model", "gpt-5.6-sol",
        "--provider", "openai-codex", "--toolsets", "file", "--safe-mode",
    ]


def run_trial(run_root: Path) -> dict[str, Any]:
    preflight = canary(run_root / "preflight")
    paths = _materialize(run_root / "trial")
    before = _inventory(paths["inputs"])
    protected_before = sha256(PROTECTED)
    prompt = TASK.read_text(encoding="utf-8")
    proc = subprocess.run(_bwrap(paths, _trial_command(prompt)), text=True, capture_output=True, timeout=900)
    (run_root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (run_root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    after = _inventory(paths["inputs"])
    artifacts = {name: {"sha256": sha256(paths["outputs"] / name), "bytes": (paths["outputs"] / name).stat().st_size} for name in OUTPUT_NAMES if (paths["outputs"] / name).is_file()}
    workspace_diff = {"changed_read_only_inputs": sorted(set(before) ^ set(after) | {p for p in before.keys() & after.keys() if before[p] != after[p]}), "created_outputs": sorted(artifacts), "protected_unchanged": protected_before == sha256(PROTECTED)}
    complete = proc.returncode == 0 and set(OUTPUT_NAMES) <= set(artifacts)
    report = {
        "schema_version": "0.1.0", "kind": "artifact_revision_isolated_agent_trial",
        "attempt_id": run_root.name, "complete": complete, "returncode": proc.returncode,
        "valid_environment": preflight["passed"] and not workspace_diff["changed_read_only_inputs"] and workspace_diff["protected_unchanged"],
        "configured_system": {"hermes_runtime_sha256": sha256(HERMES_RUNTIME / "hermes"), "model": "gpt-5.6-sol", "provider": "openai-codex", "toolsets": ["file"], "safe_mode": True, "invocation": "oneshot"},
        "task_sha256": sha256(TASK), "launcher_sha256": sha256(Path(__file__)),
        "input_manifest_sha256": sha256(paths["inputs"] / "manifest.json"), "artifacts": artifacts,
        "workspace_diff": workspace_diff, "trace": {"path": "redacted-trace.log", "sha256": sha256(run_root / "redacted-trace.log"), "policy": "stdout only; raw session/request state and provider headers are not retained"},
        "usage_path": "trial/outputs/usage.json" if "usage.json" in artifacts else None,
        "invalid_or_provider_failure_policy": "If preflight fails, inputs mutate, provider exits nonzero, or required outputs/usage are absent, retain the attempt but exclude it from substantive scoring.",
        "claim_boundaries": {"treatment_effect": False, "professional_validity": False, "general_capability": False, "cross_domain_generalization": False, "real_world_safety": False, "release_readiness": False},
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    write_json(run_root / "trial-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("canary", "run"))
    parser.add_argument("--run-root", type=Path)
    args = parser.parse_args()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_root = (args.run_root or PILOT / "trials" / stamp).resolve()
    report = canary(run_root) if args.mode == "canary" else run_trial(run_root)
    report_path = run_root / ("canary-report.json" if args.mode == "canary" else "trial-report.json")
    try:
        display_path = report_path.relative_to(ROOT)
    except ValueError:
        display_path = report_path
    print(json.dumps({"report": str(display_path), "passed": report.get("passed"), "complete": report.get("complete"), "valid_environment": report.get("valid_environment"), "model_calls": report.get("model_calls")}, indent=2))
    return 0 if report.get("passed", report.get("valid_environment", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
