#!/usr/bin/env python3
"""Retain one isolated v4 provider-coordinate capture probe."""
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
BASE_PATH = ROOT / "scripts/allocation_provider_probe.py"
ADAPTER = ROOT / "scripts/provider_call_telemetry_v4.py"
VALIDATOR_PATH = ROOT / "scripts/validate_allocation_coordinates.py"
MODEL, PROVIDER = "gpt-5.6-sol", "openai-codex"
PROMPT = "Reply with exactly COORDINATE_PROBE_OK. Do not call tools."


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path); assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


def load(path: Path) -> Any: return json.loads(path.read_text(encoding="utf-8"))
def sha256(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path: Path, value: Any) -> None: path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(manifest_path: Path, run_root: Path, attempt_id: str) -> dict[str, Any]:
    if run_root.exists(): raise FileExistsError(f"immutable probe root already exists: {run_root}")
    manifest, base, validator = load(manifest_path), load_module("probe_base", BASE_PATH), load_module("coordinate_validator", VALIDATOR_PATH)
    base.ADAPTER = ADAPTER
    paths = base._materialize(run_root)
    env = {
        "SKILL_BENCH_CALL_EVENT_PATH": "/trial/outputs/call-events.jsonl", "SKILL_BENCH_CALL_PHASE": "direct_observe_act",
        "SKILL_BENCH_ATTEMPT_ID": attempt_id, "SKILL_BENCH_PROVIDER": PROVIDER, "SKILL_BENCH_MODEL": MODEL,
        "SKILL_BENCH_CONFIGURED_SYSTEM_SHA256": manifest["configured_system_sha256"],
        "SKILL_BENCH_COORDINATE_CONTRACT_SHA256": manifest["coordinate_contract_sha256"],
        "SKILL_BENCH_COMPARISON_IDENTITY_SHA256": manifest["comparison_identity_sha256"],
    }
    command = ["/opt/hermes/venv/bin/python", "/opt/telemetry/provider_call_telemetry.py", "run-hermes", "--", "-z", PROMPT, "--usage-file", "/trial/outputs/usage.json", "--model", MODEL, "--provider", PROVIDER, "--toolsets", "file", "--safe-mode"]
    proc = subprocess.run(base._bwrap(paths, command, env), capture_output=True, text=True, timeout=300)
    (run_root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (run_root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    events_path, usage_path = paths["outputs"] / "call-events.jsonl", paths["outputs"] / "usage.json"
    events = validator.load_jsonl(events_path) if events_path.is_file() else []
    usage = load(usage_path) if usage_path.is_file() else None
    errors = validator.validate_manifest(manifest, check_paths=True)
    errors += validator.validate_events(events, manifest, attempt_id=attempt_id, aggregate_usage=usage) if events else ["configured-provider coordinate event ledger absent"]
    included = bool(usage and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0)
    passed = proc.returncode == 0 and len(events) == 1 and not errors and included
    report = {
        "schema_version": "0.4.0", "kind": "configured_provider_coordinate_probe", "attempt_id": attempt_id,
        "passed": passed, "returncode": proc.returncode, "model_calls": len(events),
        "configured_system_sha256": manifest["configured_system_sha256"], "coordinate_contract_sha256": manifest["coordinate_contract_sha256"], "comparison_identity_sha256": manifest["comparison_identity_sha256"],
        "validation": {"passed": not errors, "errors": errors},
        "provider_cost_gate": {"passed": included, "cost_status": usage.get("cost_status") if usage else None, "estimated_cost_usd": usage.get("estimated_cost_usd") if usage else None},
        "isolation": {"substrate": "bubblewrap_mount_namespace", "agent_visible_inputs": ["manifest.json"], "only_writable_task_path": "outputs", "toolsets": ["file"], "live_endpoint_tools": []},
        "retained": {"events": {"path": "outputs/call-events.jsonl", "sha256": sha256(events_path)} if events_path.is_file() else None, "usage": {"path": "outputs/usage.json", "sha256": sha256(usage_path)} if usage_path.is_file() else None, "trace": {"path": "redacted-trace.log", "sha256": sha256(run_root / "redacted-trace.log")}, "stderr": {"path": "launcher-stderr.log", "sha256": sha256(run_root / "launcher-stderr.log")}},
        "decision": "coordinate_capture_gate_passed" if passed else "fail_closed_no_matched_pair", "claim_ceiling": manifest["claim_ceiling"],
        "interpretation": "Configured-provider coordinate conformance only; no allocation/Skill effect, capability, cross-domain, expert/professional validity, safety, economic-value, production, or readiness claim."
    }
    shutil.rmtree(paths["profile"], ignore_errors=True); dump(run_root / "probe-report.json", report); return report


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("manifest", type=Path); parser.add_argument("run_root", type=Path); parser.add_argument("--attempt-id", default="alloc-v4-configured-provider-probe-01")
    args = parser.parse_args(); report = run(args.manifest.resolve(), args.run_root.resolve(), args.attempt_id)
    print(json.dumps({"passed": report["passed"], "model_calls": report["model_calls"], "decision": report["decision"]}, indent=2)); return 0 if report["passed"] else 1


if __name__ == "__main__": raise SystemExit(main())
