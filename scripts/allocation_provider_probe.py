#!/usr/bin/env python3
"""Run one isolated configured-provider call through allocation telemetry.

This is a capture probe, not a benchmark trial.  It uses the same Hermes model,
provider, invocation, file-only tool envelope, ephemeral profile, and bubblewrap
boundary declared for the prospective allocation study.  The repository-owned
adapter is mounted read-only; only the unique output root is writable.  The
probe is retained exactly once and never authorizes a matched pair by itself.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
HERMES_RUNTIME = Path("/home/sam/.hermes/hermes-agent")
PYTHON_RUNTIME = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
ADAPTER = ROOT / "scripts/provider_call_telemetry.py"
VALIDATOR = ROOT / "scripts/validate_allocation_telemetry.py"
MODEL = "gpt-5.6-sol"
PROVIDER = "openai-codex"
PROBE_PROMPT = "Reply with exactly TELEMETRY_PROBE_OK. Do not call tools."


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_validator() -> Any:
    spec = importlib.util.spec_from_file_location("allocation_validator", VALIDATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load allocation telemetry validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _copy_runtime_profile(destination: Path) -> None:
    source = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    destination.mkdir(parents=True)
    global_auth = Path(os.environ.get("HERMES_REAL_HOME", str(Path.home()))) / ".hermes/auth.json"
    if global_auth.exists():
        shutil.copy2(global_auth, destination / "auth.json")
    elif (source / "auth.json").exists():
        shutil.copy2(source / "auth.json", destination / "auth.json")
    if (source / ".env").exists():
        shutil.copy2(source / ".env", destination / ".env")
    (destination / "config.yaml").write_text(
        f"model:\n  default: {MODEL}\n  provider: {PROVIDER}\n"
        "agent:\n  max_turns: 40\nplatform_toolsets:\n  cli:\n    - file\n",
        encoding="utf-8",
    )


def _materialize(run_root: Path) -> dict[str, Path]:
    if run_root.exists():
        raise FileExistsError(f"immutable probe root already exists: {run_root}")
    inputs = run_root / "inputs"
    outputs = run_root / "outputs"
    profile = run_root / ".profile"
    inputs.mkdir(parents=True)
    outputs.mkdir()
    (inputs / "outputs").mkdir()
    dump(inputs / "manifest.json", {
        "kind": "configured_provider_capture_probe",
        "agent_visible_inputs": ["manifest.json"],
        "inputs": "read_only",
        "only_writable_task_path": "outputs",
        "toolsets": ["file"],
        "live_endpoint_tools": [],
    })
    _copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


def _bwrap(paths: dict[str, Path], command: list[str], env: dict[str, str]) -> list[str]:
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
        "--dir", "/opt/hermes", "--ro-bind", str(HERMES_RUNTIME), "/opt/hermes",
        "--dir", "/opt/telemetry", "--ro-bind", str(ADAPTER), "/opt/telemetry/provider_call_telemetry.py",
        "--bind", str(paths["profile"]), "/run/hermes-profile",
        "--ro-bind", str(paths["inputs"]), "/trial",
        "--bind", str(paths["outputs"]), "/trial/outputs",
        "--chdir", "/trial", "--setenv", "HOME", "/home/sam",
        "--setenv", "HERMES_REAL_HOME", "/home/sam",
        "--setenv", "HERMES_HOME", "/run/hermes-profile",
        "--setenv", "TERMINAL_CWD", "/trial",
        "--setenv", "PYTHONPATH", "/opt/hermes:/opt/telemetry",
        "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
        "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID",
        "--unsetenv", "HERMES_SESSION_KEY", "--unsetenv", "HERMES_UI_SESSION_ID",
    ]
    for key, value in env.items():
        args += ["--setenv", key, value]
    return [*args, "--", *command]


def command() -> list[str]:
    return [
        "/opt/hermes/venv/bin/python", "/opt/telemetry/provider_call_telemetry.py",
        "run-hermes", "--", "-z", PROBE_PROMPT,
        "--usage-file", "/trial/outputs/usage.json",
        "--model", MODEL, "--provider", PROVIDER,
        "--toolsets", "file", "--safe-mode",
    ]


def run_probe(manifest_path: Path, run_root: Path, attempt_id: str) -> dict[str, Any]:
    manifest = load(manifest_path)
    validator = _load_validator()
    paths = _materialize(run_root)
    env = {
        "SKILL_BENCH_CALL_EVENT_PATH": "/trial/outputs/call-events.jsonl",
        "SKILL_BENCH_CALL_PHASE": "direct_observe_act",
        "SKILL_BENCH_ATTEMPT_ID": attempt_id,
        "SKILL_BENCH_PROVIDER": PROVIDER,
        "SKILL_BENCH_MODEL": MODEL,
        "SKILL_BENCH_CONFIGURED_SYSTEM_SHA256": manifest["configured_system_sha256"],
    }
    proc = subprocess.run(_bwrap(paths, command(), env), capture_output=True, text=True, timeout=300)
    (run_root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (run_root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    events_path = paths["outputs"] / "call-events.jsonl"
    usage_path = paths["outputs"] / "usage.json"
    events = validator.load_jsonl(events_path) if events_path.is_file() else []
    usage = load(usage_path) if usage_path.is_file() else None
    errors = validator.validate_native_events(
        events, manifest, attempt_id=attempt_id, aggregate_usage=usage,
    ) if events else ["configured-provider native event ledger is absent"]
    included = bool(
        usage and usage.get("cost_status") == "included"
        and usage.get("estimated_cost_usd") == 0.0
    )
    passed = proc.returncode == 0 and bool(events) and not errors and included
    report = {
        "schema_version": "0.3.0",
        "kind": "configured_provider_capture_probe",
        "attempt_id": attempt_id,
        "passed": passed,
        "model_calls": len(events),
        "returncode": proc.returncode,
        "configured_system_sha256": manifest["configured_system_sha256"],
        "launcher_sha256": sha256(Path(__file__)),
        "adapter_sha256": sha256(ADAPTER),
        "manifest_sha256": sha256(manifest_path),
        "isolation": {
            "substrate": "bubblewrap_mount_namespace",
            "agent_visible_inputs": ["manifest.json"],
            "only_writable_task_path": "outputs",
            "toolsets": ["file"],
            "live_endpoint_tools": [],
        },
        "native_event_validation": {"passed": not errors, "errors": errors},
        "provider_cost_gate": {
            "passed": included,
            "cost_status": usage.get("cost_status") if usage else None,
            "estimated_cost_usd": usage.get("estimated_cost_usd") if usage else None,
        },
        "retained": {
            "events": {"path": "outputs/call-events.jsonl", "sha256": sha256(events_path)} if events_path.is_file() else None,
            "usage": {"path": "outputs/usage.json", "sha256": sha256(usage_path)} if usage_path.is_file() else None,
            "trace": {"path": "redacted-trace.log", "sha256": sha256(run_root / "redacted-trace.log")},
            "stderr": {"path": "launcher-stderr.log", "sha256": sha256(run_root / "launcher-stderr.log")},
        },
        "decision": "capture_ready_for_further_gates" if passed else "fail_closed_no_matched_pair",
        "claim_ceiling": manifest["claim_ceiling"],
        "interpretation": "Capture conformance only; no allocation or Skill effect, capability, professional validity, cost value, production fitness, or readiness claim.",
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    dump(run_root / "probe-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("run_root", type=Path)
    parser.add_argument("--attempt-id", default="alloc-configured-provider-probe-01")
    args = parser.parse_args()
    report = run_probe(args.manifest.resolve(), args.run_root.resolve(), args.attempt_id)
    print(json.dumps({"passed": report["passed"], "model_calls": report["model_calls"], "decision": report["decision"]}, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
