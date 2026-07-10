#!/usr/bin/env python3
"""Launch and audit fail-closed LH pilot workspaces with bubblewrap.

Design rationale: Hermes file tools resolve relative paths from process cwd, but
cwd alone is not an access boundary. This launcher puts the actual Hermes
process and its file tools in a mount namespace. The task source pack is
read-only, the condition Skill is either read-only or absent, outputs are the
only writable task path, and the skill-bench repository is not mounted.
Provider credentials and the Hermes runtime are mounted only as execution
infrastructure; the agent receives only the ``file`` toolset, so it has no
terminal or network-capable tool. Every paid/model-backed run must first pass
``canary`` through the same mount construction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/lh-skill-adoption"
ABLATION = PILOT / "ablation"
HERMES_RUNTIME = Path("/home/sam/.hermes/hermes-agent")
PYTHON_RUNTIME = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
SOURCE_FILES = (
    PILOT / "source-pack/decision-evidence.csv",
    PILOT / "source-pack/manifest.json",
)
SKILL = PILOT / "public-skill.md"
TASK = PILOT / "ablation/agent-attempts-20260710/no_skill_01/task.md"
PRIVATE_PROBES = (
    "/home/sam/skill-bench/pilots/lh-skill-adoption/rubric-skeleton.json",
    "/home/sam/skill-bench/pilots/lh-skill-adoption/calibration/passing/recommendation.md",
    "/home/sam/skill-bench/data/work_queue.json",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _copy_runtime_profile(destination: Path) -> None:
    source = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    destination.mkdir(parents=True, exist_ok=True)
    # Provider OAuth is shared at the default Hermes root; profile auth may
    # contain only profile-local metadata. Copy into the ephemeral namespace
    # and delete it immediately after execution.
    global_auth = Path(os.environ.get("HERMES_REAL_HOME", str(Path.home()))) / ".hermes/auth.json"
    if global_auth.exists():
        shutil.copy2(global_auth, destination / "auth.json")
    elif (source / "auth.json").exists():
        shutil.copy2(source / "auth.json", destination / "auth.json")
    env_file = source / ".env"
    if env_file.exists():
        shutil.copy2(env_file, destination / ".env")
    # Minimal, pinned surface: no skills, plugins, memory, rules, or fallback.
    (destination / "config.yaml").write_text(
        "model:\n  default: gpt-5.6-sol\n  provider: openai-codex\n"
        "agent:\n  max_turns: 40\nplatform_toolsets:\n  cli:\n    - file\n",
        encoding="utf-8",
    )


def _materialize(condition: str, run_root: Path) -> dict[str, Path]:
    inputs = run_root / "inputs"
    outputs = run_root / "outputs"
    profile = run_root / ".launcher-profile"
    task_root = run_root / ".task-root"
    inputs.mkdir(parents=True)
    outputs.mkdir()
    task_root.mkdir()
    (task_root / "inputs").mkdir()
    (task_root / "outputs").mkdir()
    for source in SOURCE_FILES:
        shutil.copy2(source, inputs / source.name)
    if condition == "public_skill":
        shutil.copy2(SKILL, task_root / "public-skill.md")
    _copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile, "task_root": task_root}


def _bwrap(paths: dict[str, Path], condition: str, command: list[str]) -> list[str]:
    args = [
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
        "--dir", "/opt/hermes",
        "--ro-bind", str(HERMES_RUNTIME), "/opt/hermes",
        "--bind", str(paths["profile"]), "/run/hermes-profile",
        "--ro-bind", str(paths["task_root"]), "/trial",
        "--ro-bind", str(paths["inputs"]), "/trial/inputs",
        "--bind", str(paths["outputs"]), "/trial/outputs",
    ]
    args += [
        "--chdir", "/trial", "--setenv", "HOME", "/home/sam",
        "--setenv", "HERMES_REAL_HOME", "/home/sam",
        "--setenv", "HERMES_HOME", "/run/hermes-profile",
        "--setenv", "TERMINAL_CWD", "/trial",
        "--setenv", "PYTHONPATH", "/opt/hermes",
        "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
        "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID",
        "--unsetenv", "HERMES_SESSION_KEY", "--unsetenv", "HERMES_UI_SESSION_ID",
        "--", *command,
    ]
    return args


CANARY_CODE = r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool

def ok_read(path):
    value = read_file_tool(path, limit=5)
    return "error" not in value.lower() and "not found" not in value.lower()

def denied_read(path):
    value = read_file_tool(path, limit=5)
    return any(x in value.lower() for x in ("error", "not found", "denied", "does not exist"))

result = {
  "observed_cwd": os.getcwd(),
  "input_readable": ok_read("inputs/decision-evidence.csv"),
  "manifest_readable": ok_read("inputs/manifest.json"),
  "skill_readable": ok_read("public-skill.md"),
  "private_reads_denied": {p: denied_read(p) for p in PRIVATE},
  "parent_search": search_tool("skill-bench", target="files", path="/home/sam", limit=20),
}
write_ok = write_file_tool("outputs/canary.txt", "isolated-canary\n")
write_bad = write_file_tool("escape.txt", "must-not-write\n")
result["output_write_succeeded"] = "error" not in write_ok.lower()
result["outside_write_denied"] = any(x in write_bad.lower() for x in ("error", "denied", "read-only", "permission"))
print(json.dumps(result, sort_keys=True))
'''


def canary(condition: str, run_root: Path) -> dict[str, Any]:
    paths = _materialize(condition, run_root)
    code = "PRIVATE=" + repr(PRIVATE_PROBES) + "\n" + CANARY_CODE
    command = ["/opt/hermes/venv/bin/python", "-c", code]
    proc = subprocess.run(_bwrap(paths, condition, command), text=True, capture_output=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1]) if proc.stdout.strip() else {}
    except (json.JSONDecodeError, IndexError):
        observed = {}
    expected_skill = condition == "public_skill"
    passed = (
        proc.returncode == 0
        and observed.get("observed_cwd") == "/trial"
        and observed.get("input_readable") is True
        and observed.get("manifest_readable") is True
        and observed.get("skill_readable") is expected_skill
        and all(observed.get("private_reads_denied", {}).values())
        and "skill-bench" not in str(observed.get("parent_search", ""))
        and observed.get("output_write_succeeded") is True
        and observed.get("outside_write_denied") is True
    )
    report = {
        "schema_version": "0.1.0", "kind": "outer_envelope_canary",
        "condition": condition, "passed": passed, "model_calls": 0,
        "launcher_sha256": sha256(Path(__file__)),
        "source_hashes": {p.name: sha256(p) for p in SOURCE_FILES},
        "skill_sha256": sha256(SKILL) if expected_skill else None,
        "isolation_substrate": "bubblewrap mount namespace",
        "tool_interface": "Hermes tools.file_tools read/search/write",
        "observed": observed, "stderr": proc.stderr[-2000:], "returncode": proc.returncode,
        "limitations": [
            "The canary proves filesystem visibility through the configured file tools, not kernel security against a terminal tool; trials expose no terminal tool.",
            "Provider network transport remains available to the Hermes process, but the agent receives no web, browser, or terminal tool.",
        ],
    }
    # Never retain copied provider credentials or internal runtime state in a
    # benchmark evidence directory. The report records only probe outcomes.
    shutil.rmtree(paths["profile"], ignore_errors=True)
    shutil.rmtree(paths["task_root"], ignore_errors=True)
    write_json(run_root / "canary-report.json", report)
    if not passed:
        raise RuntimeError(f"fail-closed canary failed; see {run_root / 'canary-report.json'}")
    return report


def _trial_command(prompt: str) -> list[str]:
    """Build the pinned one-shot command used by measured trials.

    ``--usage-file`` is intentionally paired with ``-z``: Hermes documents
    usage accounting as a one-shot-only interface. The earlier ``chat
    --query`` form silently ignored the flag and could leave an otherwise
    successful arm unmeasurable.
    """
    return [
        "/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes",
        "-z", prompt, "--usage-file", "/trial/outputs/usage.json",
        "--model", "gpt-5.6-sol", "--provider", "openai-codex",
        "--toolsets", "file", "--safe-mode",
    ]


def run_trial(condition: str, run_root: Path) -> dict[str, Any]:
    preflight = canary(condition, run_root / "preflight")
    paths = _materialize(condition, run_root / "trial")
    prompt = TASK.read_text(encoding="utf-8")
    command = _trial_command(prompt)
    proc = subprocess.run(_bwrap(paths, condition, command), text=True, capture_output=True, timeout=900)
    (run_root / "transcript.log").write_text(proc.stdout, encoding="utf-8")
    (run_root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    # Hermes request dumps can contain provider authorization headers. Never
    # retain raw session state in benchmark evidence; transcript, stderr,
    # usage, deliverables, and their hashes are the auditable surface.
    artifacts = {}
    for name in ("evidence-matrix.csv", "recommendation.md", "usage.json"):
        path = paths["outputs"] / name
        if path.exists():
            artifacts[name] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    complete = proc.returncode == 0 and {"evidence-matrix.csv", "recommendation.md", "usage.json"} <= set(artifacts)
    report = {
        "schema_version": "0.1.0", "kind": "isolated_agent_trial",
        "condition": condition, "complete": complete, "returncode": proc.returncode,
        "valid_environment": preflight["passed"], "capability_evidence": complete and preflight["passed"],
        "condition_effect_permitted": False,
        "configured_system": {
            "model": "gpt-5.6-sol", "provider": "openai-codex",
            "toolsets": ["file"], "safe_mode": True, "invocation": "oneshot",
        },
        "task_sha256": sha256(TASK), "launcher_sha256": sha256(Path(__file__)),
        "artifacts": artifacts,
        "interpretation_boundary": "One attempt in one arm is execution evidence only; no condition effect, professional validity, or release readiness is licensed.",
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    shutil.rmtree(paths["task_root"], ignore_errors=True)
    write_json(run_root / "trial-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("canary", "run"))
    parser.add_argument("--condition", choices=("no_skill", "public_skill"), required=True)
    parser.add_argument("--run-root", type=Path)
    args = parser.parse_args()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_root = (args.run_root or ABLATION / "launcher-canaries" / f"{stamp}-{args.condition}").resolve()
    if args.mode == "canary":
        report = canary(args.condition, run_root)
        summary = {"report": str((run_root / "canary-report.json").relative_to(ROOT)), "passed": report["passed"], "model_calls": 0}
    else:
        report = run_trial(args.condition, run_root)
        summary = {"report": str((run_root / "trial-report.json").relative_to(ROOT)), "complete": report["complete"], "valid_environment": report["valid_environment"]}
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
