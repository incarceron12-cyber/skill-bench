#!/usr/bin/env python3
"""Materialize and execute the frozen 32-cell v4 procedure-transfer matrix once.

The launcher verifies both pushed freezes, materializes condition inputs without
private endpoints, runs zero-call isolation/checker canaries, and retains every
scheduled ITT attempt. A service, cost, or isolation failure stops later calls;
artifact/check failures remain in the denominator and never trigger retry.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
HERMES = Path("/home/sam/.hermes/hermes-agent")
PYTHON = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
MODEL = "gpt-5.6-sol"
PROVIDER = "openai-codex"
CLAIMS = {"agent_capability": False, "expert_provenance": False, "production_fitness": False,
          "professional_validity": False, "readiness": False, "transfer": False, "utility": False}
PRIVATE_PROBES = (
    "/home/sam/skill-bench/data/work_queue.json",
    "/home/sam/skill-bench/pilots/pretask-procedure-transfer-v4/checkers/check_endpoint.py",
    "/home/sam/skill-bench/pilots/pretask-procedure-transfer-v4/tasks/k4n7/private.json",
    "/trial/private.json", "/trial/check_endpoint.py",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def inventory(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    return {p.relative_to(path).as_posix(): {"sha256": sha(p), "bytes": p.stat().st_size}
            for p in sorted(path.rglob("*")) if p.is_file()}


def git_bytes(revision: str, path: Path) -> bytes:
    return subprocess.run(["git", "show", f"{revision}:{path.relative_to(ROOT).as_posix()}"],
                          cwd=ROOT, check=True, capture_output=True).stdout


def verify_hash_manifest(manifest_path: Path, origin: str) -> list[dict[str, Any]]:
    if git_bytes(origin, manifest_path) != manifest_path.read_bytes():
        raise RuntimeError(f"manifest differs from pushed {origin}: {manifest_path.name}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checked = []
    for row in manifest["components"]:
        path = ROOT / row["path"]
        actual = sha(path)
        if actual != row["sha256"] or ("bytes" in row and path.stat().st_size != row["bytes"]):
            raise RuntimeError(f"manifest component drift: {row['path']}")
        if hashlib.sha256(git_bytes(origin, path)).hexdigest() != actual:
            raise RuntimeError(f"component not frozen on {origin}: {row['path']}")
        checked.append({"path": row["path"], "sha256": actual, "bytes": path.stat().st_size})
    return checked


def verify_audit_chain() -> dict[str, Any]:
    manifest = json.loads((HERE / "candidate-freeze-manifest.json").read_text(encoding="utf-8"))
    audit_path = ROOT / manifest["audit_log"]["path"]
    if sha(audit_path) != manifest["audit_log"]["sha256"]:
        raise RuntimeError("candidate audit log hash drift")
    previous = None
    events = []
    for line in audit_path.read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("previous_event_sha256") != previous:
            raise RuntimeError("candidate audit chain previous-event mismatch")
        body = dict(event)
        event_hash = body.pop("event_sha256", None)
        calculated = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if event_hash != calculated:
            raise RuntimeError("candidate audit event hash mismatch")
        previous = event_hash
        events.append(event)
    if len(events) != manifest["audit_log"]["events"] or previous != manifest["audit_log"]["terminal_event_sha256"]:
        raise RuntimeError("candidate audit terminal mismatch")
    return {"events": len(events), "terminal_event_sha256": previous, "sha256": sha(audit_path)}


def verify_pushed_freezes() -> dict[str, Any]:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, check=True, capture_output=True)
    origin = subprocess.run(["git", "rev-parse", "origin/main"], cwd=ROOT, check=True,
                            capture_output=True, text=True).stdout.strip()
    candidate = json.loads((HERE / "candidate-freeze-manifest.json").read_text(encoding="utf-8"))
    if git_bytes("origin/main", HERE / "candidate-freeze-manifest.json") != (HERE / "candidate-freeze-manifest.json").read_bytes():
        raise RuntimeError("candidate freeze manifest is not pushed unchanged")
    candidate_components = verify_hash_manifest(HERE / "candidate-freeze-manifest.json", "origin/main")
    hindsight_components = verify_hash_manifest(HERE / "hindsight-freeze-manifest.json", "origin/main")
    if candidate.get("status") != "frozen_valid_candidates" or candidate.get("executor_attempts") != 0:
        raise RuntimeError("candidate freeze does not authorize first execution")
    if candidate.get("aggregate_attempts", {}).get("executor") != 0 or candidate.get("claim_ceiling") != CLAIMS:
        raise RuntimeError("candidate executor/claim gate failed")
    expected = {"family-epsilon": "ab2dab013ca29591a3df6cccc1e22570fd748780a3fd0fa541dd214be57bb2b5",
                "family-zeta": "eee9b0f5c89c31cf3e1afdc4476253c4fc3054f5851ebce7329d0b62d593a399"}
    if candidate.get("candidate_packages") != expected:
        raise RuntimeError("candidate hashes differ from released execution task")
    for family, expected_hash in expected.items():
        path = HERE / "candidate-generation" / family / "outputs/package.json"
        if sha(path) != expected_hash:
            raise RuntimeError(f"candidate hash drift: {family}")
    generation = json.loads((HERE / "generation-audit-report.json").read_text(encoding="utf-8"))
    if generation.get("audit_status") != "PASS" or generation.get("execution_task_may_be_released") is not True:
        raise RuntimeError("independent generation audit does not release execution")
    if generation.get("aggregate_attempts", {}).get("executor") != 0 or generation.get("claim_ceiling") != CLAIMS:
        raise RuntimeError("generation audit execution/claim gate failed")
    # The original zero-call freeze remains exact and pushed as well.
    frozen_components = verify_hash_manifest(HERE / "freeze-manifest.json", "origin/main")
    return {"origin_commit": origin, "candidate_components": len(candidate_components),
            "hindsight_components": len(hindsight_components), "frozen_components": len(frozen_components),
            "candidate_hashes": expected, "audit_chain": verify_audit_chain()}


def make_profile(path: Path) -> None:
    path.mkdir(parents=True)
    hermes_home = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    for source in (Path.home() / ".hermes/auth.json", hermes_home / ".env"):
        if source.exists():
            shutil.copy2(source, path / source.name)
    (path / "config.yaml").write_text(
        f"model:\n  default: {MODEL}\n  provider: {PROVIDER}\n"
        "agent:\n  max_turns: 40\nplatform_toolsets:\n  cli:\n    - file\n", encoding="utf-8")


def sandbox(inputs: Path, outputs: Path, profile: Path, command: list[str]) -> list[str]:
    return ["bwrap", "--die-with-parent", "--new-session", "--unshare-pid",
            "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
            "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin",
            "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64",
            "--ro-bind", "/etc", "/etc", "--dir", "/run/systemd",
            "--ro-bind", "/run/systemd/resolve", "/run/systemd/resolve",
            "--dir", "/home", "--dir", "/home/sam", "--dir", "/home/sam/.local",
            "--dir", "/home/sam/.local/share", "--dir", "/home/sam/.local/share/uv",
            "--dir", "/home/sam/.local/share/uv/python", "--ro-bind", str(PYTHON), str(PYTHON),
            "--dir", "/opt/hermes", "--ro-bind", str(HERMES), "/opt/hermes",
            "--bind", str(profile), "/run/hermes-profile", "--ro-bind", str(inputs), "/trial",
            "--bind", str(outputs), "/trial/outputs", "--chdir", "/trial",
            "--setenv", "HOME", "/home/sam", "--setenv", "HERMES_REAL_HOME", "/home/sam",
            "--setenv", "HERMES_HOME", "/run/hermes-profile", "--setenv", "TERMINAL_CWD", "/trial",
            "--setenv", "PYTHONPATH", "/opt/hermes", "--setenv", "SSL_CERT_FILE",
            "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
            "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID",
            "--unsetenv", "HERMES_SESSION_KEY", "--unsetenv", "HERMES_UI_SESSION_ID", "--", *command]


def support_sources(row: dict[str, Any]) -> list[tuple[Path, str]]:
    family = row["family_id"]
    other = "family-zeta" if family == "family-epsilon" else "family-epsilon"
    condition = row["condition_id"]
    reference_name = "epsilon" if family == "family-epsilon" else "zeta"
    other_name = "zeta" if family == "family-epsilon" else "epsilon"
    sources: list[tuple[Path, str]] = []
    if condition in {"generated_package", "generated_plus_raw"}:
        sources.append((HERE / "candidate-generation" / family / "outputs/package.json", "procedure-package.json"))
    if condition in {"equal_budget_raw", "generated_plus_raw"}:
        sources.append((HERE / "families" / reference_name / "corpus.json", "source-context.json"))
    if condition == "reference_procedure":
        sources.append((HERE / "controls" / reference_name / "reference.json", "procedure-package.json"))
    if condition == "cross_family_irrelevant":
        sources.append((HERE / "controls" / other_name / "reference.json", "procedure-package.json"))
    if condition == "exactly_one_defect":
        sources.append((HERE / "controls" / reference_name / "defective.json", "procedure-package.json"))
    if condition == "task_conditioned_hindsight_upper_bound":
        sources.append((HERE / "hindsight-packages" / f"{family}.json", "procedure-package.json"))
    return sources


def materialize(row: dict[str, Any], root: Path) -> dict[str, Path]:
    if root.exists():
        raise RuntimeError(f"attempt root already exists; retry forbidden: {root}")
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    inputs.mkdir(parents=True); outputs.mkdir(); (inputs / "outputs").mkdir(); make_profile(profile)
    public = HERE / "tasks" / row["task_id"] / "public.md"
    shutil.copy2(public, inputs / "public-task.md")
    support = support_sources(row)
    if sum(path.stat().st_size for path, _ in support) > 16000:
        raise RuntimeError(f"treatment retrieval byte budget exceeded: {row['schedule_index']}")
    for source, name in support:
        shutil.copy2(source, inputs / name)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


CANARY_CODE = r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool

def readable(path):
    value = read_file_tool(path, limit=5)
    return not any(x in value.lower() for x in ("error", "not found", "denied", "does not exist"))
visible = [p for p in os.listdir(".") if p != "outputs"]
result = {
  "cwd": os.getcwd(),
  "visible": visible,
  "visible_readable": {p: readable(p) for p in visible},
  "private_denied": {p: not readable(p) for p in PRIVATE},
  "repository_search": search_tool("skill-bench", target="files", path="/home/sam", limit=20),
}
result["output_write"] = "error" not in write_file_tool("outputs/canary.txt", "v4-canary\n").lower()
result["outside_write_denied"] = any(x in write_file_tool("escape.txt", "bad\n").lower() for x in ("error", "denied", "read-only", "permission"))
print(json.dumps(result, sort_keys=True))
'''


def outer_canary(paths: dict[str, Path], expected: set[str]) -> dict[str, Any]:
    code = "PRIVATE=" + repr(PRIVATE_PROBES) + "\n" + CANARY_CODE
    proc = subprocess.run(sandbox(paths["inputs"], paths["outputs"], paths["profile"],
                                  ["/opt/hermes/venv/bin/python", "-c", code]),
                          text=True, capture_output=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        observed = {}
    passed = (proc.returncode == 0 and observed.get("cwd") == "/trial"
              and set(observed.get("visible", [])) == expected
              and all(observed.get("visible_readable", {}).values())
              and all(observed.get("private_denied", {}).values())
              and "skill-bench" not in str(observed.get("repository_search", ""))
              and observed.get("output_write") is True and observed.get("outside_write_denied") is True)
    return {"passed": passed, "model_calls": 0, "returncode": proc.returncode,
            "expected_visible": sorted(expected), "observed": observed, "stderr": proc.stderr[-2000:]}


def endpoint_canary() -> dict[str, Any]:
    checker = HERE / "checkers/check_endpoint.py"
    before = sha(checker)
    rows = []
    temp = HERE / ".endpoint-canary"
    if temp.exists():
        raise RuntimeError("stale endpoint canary directory")
    temp.mkdir()
    try:
        for task_id in ("k4n7", "p9c2", "t6v1", "w3d8"):
            private = HERE / "tasks" / task_id / "private.json"
            spec = json.loads(private.read_text(encoding="utf-8"))
            passing = temp / f"{task_id}-pass.json"; failing = temp / f"{task_id}-fail.json"
            write_json(passing, spec["expected_endpoint"])
            bad = dict(spec["expected_endpoint"]); bad["task_id"] = "condition-probe-must-fail"
            write_json(failing, bad)
            good_proc = subprocess.run([sys.executable, str(checker), "--candidate", str(passing), "--private", str(private)], capture_output=True, text=True)
            bad_proc = subprocess.run([sys.executable, str(checker), "--candidate", str(failing), "--private", str(private)], capture_output=True, text=True)
            good = json.loads(good_proc.stdout); bad_result = json.loads(bad_proc.stdout)
            rows.append({"task_id": task_id, "pass_canary": good_proc.returncode == 0 and good.get("passed") is True,
                         "fail_canary": bad_proc.returncode != 0 and bad_result.get("passed") is False,
                         "checker_output_keys": sorted(good)})
    finally:
        shutil.rmtree(temp)
    passed = all(r["pass_canary"] and r["fail_canary"] and r["checker_output_keys"] == ["passed", "reason"] for r in rows) and sha(checker) == before
    return {"passed": passed, "model_calls": 0, "checker_sha256": before, "tasks": rows,
            "checker_visibility": ["candidate result.json", "assigned private endpoint"],
            "checker_denied": ["condition identity", "package bytes", "raw corpus", "trace", "usage", "assignment row"]}


def trial_prompt() -> str:
    return ("Read public-task.md and any other support files present in the current task directory. "
            "Complete the public task. Write only the requested strict JSON artifact to outputs/result.json. "
            "Do not write any other task artifact or commentary file.\n")


def run_trial(row: dict[str, Any], paths: dict[str, Path], freeze: dict[str, Any], canary_passed: bool) -> dict[str, Any]:
    before = inventory(paths["inputs"])
    prompt = trial_prompt()
    command = ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt,
               "--usage-file", "/trial/outputs/usage.json", "--model", MODEL, "--provider", PROVIDER,
               "--toolsets", "file", "--safe-mode"]
    started = datetime.now(timezone.utc).isoformat()
    try:
        proc = subprocess.run(sandbox(paths["inputs"], paths["outputs"], paths["profile"], command),
                              capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "timeout")
        proc = subprocess.CompletedProcess(command, 124, stdout, stderr)
    finished = datetime.now(timezone.utc).isoformat()
    root = paths["inputs"].parent
    (root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    after = inventory(paths["inputs"])
    result_path, usage_path = paths["outputs"] / "result.json", paths["outputs"] / "usage.json"
    try:
        usage = json.loads(usage_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        usage = {}
    service_valid = (proc.returncode == 0 and usage.get("completed") is True and usage.get("failed") is False
                     and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
                     and usage.get("model") == MODEL and usage.get("provider") == PROVIDER)
    environment_valid = canary_passed and before == after
    artifact_valid = False
    if result_path.is_file():
        try:
            parsed = json.loads(result_path.read_text(encoding="utf-8"))
            artifact_valid = isinstance(parsed, dict) and parsed.get("task_id") == row["task_id"]
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
    checker = HERE / "checkers/check_endpoint.py"
    private = HERE / "tasks" / row["task_id"] / "private.json"
    check = subprocess.run([sys.executable, str(checker), "--candidate", str(result_path), "--private", str(private)],
                           capture_output=True, text=True)
    try:
        check_result = json.loads(check.stdout)
    except json.JSONDecodeError:
        check_result = {"passed": False, "reason": "checker_invalid_output"}
    report = {**row, "attempts": 1, "started_at": started, "finished_at": finished,
              "configured_system": {"model": MODEL, "provider": PROVIDER, "toolsets": ["file"],
                                    "safe_mode": True, "max_turns": 40, "attempts_per_cell": 1},
              "attempted": True, "service_valid": service_valid, "environment_valid": environment_valid,
              "artifact_valid": artifact_valid, "checker_scored": True, "endpoint_pass": check_result.get("passed") is True,
              "checker_result": check_result, "launcher_returncode": proc.returncode,
              "input_inventory": before, "output_inventory": inventory(paths["outputs"]),
              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
              "trace_sha256": sha(root / "redacted-trace.log"), "stderr_sha256": sha(root / "launcher-stderr.log"),
              "usage": usage, "freeze_verification": freeze, "claim_ceiling": CLAIMS,
              "repair_attempts": 0, "retry_attempts": 0}
    write_json(root / "trial-report.json", report)
    shutil.rmtree(paths["profile"], ignore_errors=True)
    return report


def summarize(rows: list[dict[str, Any]], intended: int, stop_reason: str | None) -> dict[str, Any]:
    conditions = sorted({r["condition_id"] for r in rows})
    families = ("family-epsilon", "family-zeta")
    cell_results = [{"schedule_index": r["schedule_index"], "family_id": r["family_id"], "task_id": r["task_id"],
                     "condition_id": r["condition_id"], "service_valid": r["service_valid"],
                     "environment_valid": r["environment_valid"], "artifact_valid": r["artifact_valid"],
                     "checker_scored": r["checker_scored"], "endpoint_pass": r["endpoint_pass"]} for r in rows]
    rates: dict[str, dict[str, float | None]] = {}
    for family in families:
        rates[family] = {}
        for condition in conditions:
            subset = [r for r in rows if r["family_id"] == family and r["condition_id"] == condition and r["checker_scored"]]
            rates[family][condition] = (sum(r["endpoint_pass"] for r in subset) / len(subset)) if len(subset) == 2 else None
    contrasts = {}
    protocol = json.loads((HERE / "protocol.json").read_text(encoding="utf-8"))
    for expression in protocol["order_and_accounting"]["family_clustered_estimands"]:
        left, right = expression.split(" - ")
        values: dict[str, float | None] = {}
        for family in families:
            left_rate = rates[family].get(left)
            right_rate = rates[family].get(right)
            values[family] = left_rate - right_rate if left_rate is not None and right_rate is not None else None
        available = [v for v in values.values() if v is not None]
        contrasts[expression] = {"family_differences": values,
                                 "family_clustered_mean_difference": sum(available) / len(available) if len(available) == 2 else None,
                                 "cluster_count": len(available)}
    return {"study_id": "pretask-procedure-transfer-v4-execution", "status": "complete" if len(rows) == intended and not stop_reason else "stopped_fail_closed",
            "stop_reason": stop_reason, "denominators": {"intended": intended, "attempted": len(rows),
            "service_valid": sum(r["service_valid"] for r in rows), "environment_valid": sum(r["environment_valid"] for r in rows),
            "artifact_valid": sum(r["artifact_valid"] for r in rows), "checker_scored": sum(r["checker_scored"] for r in rows),
            "endpoint_pass": sum(r["endpoint_pass"] for r in rows)}, "exact_cells": cell_results,
            "family_condition_pass_rates": rates, "family_clustered_estimands": contrasts,
            "attempts": {"executor": len(rows), "model": len(rows), "provider": len(rows), "repair": 0, "retry": 0},
            "claim_ceiling": CLAIMS,
            "interpretation": "Internal synthetic exact-cell and family-clustered endpoint results only. Package conformance and these outcomes do not establish transfer, capability, utility, expert provenance, professional validity, production fitness, or readiness."}


def main() -> int:
    execution = HERE / "execution"
    report_path = HERE / "execution-report.json"
    canary_path = HERE / "execution-canary-report.json"
    if execution.exists() or report_path.exists() or canary_path.exists():
        raise RuntimeError("execution evidence already exists; retry, replacement, and rerun are forbidden")
    freeze = verify_pushed_freezes()
    assignments = json.loads((HERE / "assignments.json").read_text(encoding="utf-8"))["rows"]
    if len(assignments) != 32 or [r["schedule_index"] for r in assignments] != list(range(1, 33)) or any(r["attempts"] != 0 for r in assignments):
        raise RuntimeError("frozen assignment schedule invalid or previously attempted")
    # Materialize all intended rows before any executor call.
    materialized: list[tuple[dict[str, Any], dict[str, Path]]] = []
    for row in assignments:
        materialized.append((row, materialize(row, execution / f"{row['schedule_index']:02d}-{row['task_id']}")))
    # Exercise the real tool surface once, and logically verify every materialized inventory.
    canary_root = HERE / ".execution-canary"
    sample_row = assignments[0]
    canary_paths = materialize(sample_row, canary_root)
    expected = {"public-task.md", "procedure-package.json"}
    outer = outer_canary(canary_paths, expected)
    shutil.rmtree(canary_root)
    inventory_checks = []
    for row, paths in materialized:
        expected_files = {"public-task.md"} | {name for _, name in support_sources(row)}
        actual_files = set(inventory(paths["inputs"])) - {"outputs"}
        inventory_checks.append({"schedule_index": row["schedule_index"], "passed": actual_files == expected_files,
                                 "expected": sorted(expected_files), "actual": sorted(actual_files)})
    endpoint = endpoint_canary()
    canary_report = {"status": "PASS" if outer["passed"] and endpoint["passed"] and all(r["passed"] for r in inventory_checks) else "FAIL",
                     "outer_envelope": outer, "materialized_inventory_checks": inventory_checks,
                     "condition_blind_endpoint": endpoint, "model_calls": 0, "freeze_verification": freeze}
    write_json(canary_path, canary_report)
    if canary_report["status"] != "PASS":
        write_json(report_path, summarize([], 32, "zero-cost isolation or checker canary failed"))
        return 1
    rows = []
    stop_reason = None
    for row, paths in materialized:
        report = run_trial(row, paths, freeze, True)
        rows.append(report)
        print(json.dumps({"schedule_index": row["schedule_index"], "task_id": row["task_id"],
                          "condition_id": row["condition_id"], "service_valid": report["service_valid"],
                          "artifact_valid": report["artifact_valid"], "endpoint_pass": report["endpoint_pass"]}), flush=True)
        if not report["service_valid"] or not report["environment_valid"]:
            stop_reason = f"fail-closed service/cost/isolation gate at schedule_index {row['schedule_index']}"
            break
    summary = summarize(rows, 32, stop_reason)
    summary["canary_report_sha256"] = sha(canary_path)
    summary["freeze_verification"] = freeze
    write_json(report_path, summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
