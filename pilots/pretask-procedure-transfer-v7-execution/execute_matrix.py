#!/usr/bin/env python3
"""Execute the independently cleared frozen v7 32-row matrix exactly once.

This prospective launcher is outside the frozen v4-v7 instruments. It verifies
all direct and transitive frozen bytes, the audited commit ancestry, zero prior
v7 attempts, retained canary/preflight bytes, and prior provider-included-cost
evidence before materializing rows. One service/cost/environment failure stops
later rows; artifact/check failures remain in strict denominators without retry.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V7 = ROOT / "pilots/pretask-procedure-transfer-v7"
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
HERMES = Path("/home/sam/.hermes/hermes-agent")
PYTHON = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
AUDITED_COMMIT = "0b7f9306ec6c3a18d4f5bba98af3eabd2ea7f200"
MODEL, PROVIDER = "gpt-5.6-sol", "openai-codex"
CLAIMS = {"agent_capability": False, "expert_provenance": False, "production_fitness": False,
          "professional_validity": False, "readiness": False, "transfer": False, "utility": False}
ATTEMPT_STATES = ("attempted", "skipped", "invalid", "service_failed", "environment_failed")
COST_EVIDENCE = V4 / "execution/32-k4n7/outputs/usage.json"
PRIVATE_PROBES = (
    "/home/sam/skill-bench/data/work_queue.json",
    "/home/sam/skill-bench/pilots/pretask-procedure-transfer-v7/checkers/check_endpoint.py",
    "/home/sam/skill-bench/pilots/pretask-procedure-transfer-v7/tasks/k4n7/private.json",
    "/trial/private.json", "/trial/check_endpoint.py",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def inventory(path: Path) -> dict[str, dict[str, Any]]:
    return {p.relative_to(path).as_posix(): {"sha256": sha(p), "bytes": p.stat().st_size}
            for p in sorted(path.rglob("*")) if p.is_file()} if path.exists() else {}


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, check=check, capture_output=True, text=True)


def verify_rows_zero() -> list[dict[str, Any]]:
    rows = load(V7 / "assignments.json")["rows"]
    if (len(rows) != 32 or [r["schedule_index"] for r in rows] != list(range(1, 33))
            or any(r.get("attempts") != 0 for r in rows)):
        raise RuntimeError("v7 assignment schedule is invalid or records a prior attempt")
    for forbidden in (HERE / "execution", HERE / "execution-report.json"):
        if forbidden.exists():
            raise RuntimeError(f"execution evidence already exists; rerun forbidden: {forbidden}")
    return rows


def verify_manifest(path: Path, keys: tuple[str, ...], roles: set[str] | None = None,
                    path_suffixes: tuple[str, ...] | None = None) -> list[dict[str, Any]]:
    """Verify selected manifest rows; old lifecycle prose may evolve, treatments may not."""
    manifest = load(path)
    checked: list[dict[str, Any]] = []
    for key in keys:
        for row in manifest.get(key, []):
            if roles is not None and row.get("role") not in roles:
                continue
            if path_suffixes is not None and not row["path"].endswith(path_suffixes):
                continue
            target = ROOT / row["path"]
            if not target.is_file() or sha(target) != row["sha256"] or (
                    "bytes" in row and target.stat().st_size != row["bytes"]):
                raise RuntimeError("frozen byte drift: " + row["path"])
            checked.append({"path": row["path"], "sha256": row["sha256"], "bytes": target.stat().st_size})
    return checked


def verify_preconditions() -> dict[str, Any]:
    git("fetch", "origin", "main")
    origin = git("rev-parse", "origin/main").stdout.strip()
    if git("merge-base", "--is-ancestor", AUDITED_COMMIT, "origin/main", check=False).returncode != 0:
        raise RuntimeError("audited v7 commit is not an ancestor of origin/main")
    audited_manifest = subprocess.run(
        ["git", "show", f"{AUDITED_COMMIT}:pilots/pretask-procedure-transfer-v7/freeze-manifest.json"],
        cwd=ROOT, check=True, capture_output=True).stdout
    if audited_manifest != (V7 / "freeze-manifest.json").read_bytes():
        raise RuntimeError("v7 manifest differs from exact audited commit")
    checked = verify_manifest(V7 / "freeze-manifest.json", ("components", "external_immutable_bindings"))
    manifest, protocol = load(V7 / "freeze-manifest.json"), load(V7 / "protocol.json")
    zero = {"executor": 0, "model": 0, "provider": 0, "repair": 0, "retry": 0}
    if manifest.get("attempt_ledger") != zero or protocol.get("attempt_ledger") != zero:
        raise RuntimeError("v7 frozen attempt ledger is not zero")
    if manifest.get("claim_ceiling") != CLAIMS or protocol.get("claim_ceiling") != CLAIMS:
        raise RuntimeError("v7 claim ceiling drift")
    # Verify only assigned immutable treatment resources in the older manifests;
    # phase-aware README/tests/reports legitimately changed after their freeze.
    v4_components = verify_manifest(
        V4 / "freeze-manifest.json", ("components",),
        roles={"source_corpus", "reference_control", "defective_control"})
    candidate_components = verify_manifest(
        V4 / "candidate-freeze-manifest.json", ("components",),
        path_suffixes=("/outputs/package.json",))
    hindsight_components = verify_manifest(V4 / "hindsight-freeze-manifest.json", ("components",))
    with tempfile.TemporaryDirectory(prefix="v7-exec-preflight-") as tmp:
        canary = Path(tmp) / "canary.json"; preflight = Path(tmp) / "preflight.json"
        subprocess.run([sys.executable, str(V7 / "run_canaries.py"), "--report", str(canary)], cwd=ROOT, check=True,
                       capture_output=True, text=True, timeout=120)
        subprocess.run([sys.executable, str(V7 / "preflight.py"), "--check-paths", "--report", str(preflight)],
                       cwd=ROOT, check=True, capture_output=True, text=True, timeout=120)
        if canary.read_bytes() != (V7 / "canary-report.json").read_bytes():
            raise RuntimeError("fresh v7 canary report differs from frozen passing bytes")
        if preflight.read_bytes() != (V7 / "preflight-report.json").read_bytes():
            raise RuntimeError("fresh v7 preflight report differs from frozen passing bytes")
    usage = load(COST_EVIDENCE)
    if not (usage.get("model") == MODEL and usage.get("provider") == PROVIDER
            and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
            and usage.get("completed") is True and usage.get("failed") is False):
        raise RuntimeError("provider-reported included USD 0.00 prerequisite is not satisfied")
    return {"audited_commit": AUDITED_COMMIT, "origin_main": origin, "audited_commit_is_ancestor": True,
            "v7_bound_files_checked": len(checked), "v4_components_checked": len(v4_components),
            "candidate_components_checked": len(candidate_components),
            "hindsight_components_checked": len(hindsight_components),
            "canary_rerun": "byte_identical_pass", "preflight_rerun": "byte_identical_pass",
            "zero_v7_attempts": True, "cost_evidence": {"path": COST_EVIDENCE.relative_to(ROOT).as_posix(),
            "sha256": sha(COST_EVIDENCE), "cost_status": usage["cost_status"],
            "estimated_cost_usd": usage["estimated_cost_usd"], "model": MODEL, "provider": PROVIDER},
            "claim_ceiling": CLAIMS}


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
    return ["bwrap", "--die-with-parent", "--new-session", "--unshare-pid", "--proc", "/proc",
            "--dev", "/dev", "--tmpfs", "/tmp", "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin",
            "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64", "--ro-bind", "/etc", "/etc",
            "--dir", "/run/systemd", "--ro-bind", "/run/systemd/resolve", "/run/systemd/resolve",
            "--dir", "/home", "--dir", "/home/sam", "--dir", "/home/sam/.local", "--dir", "/home/sam/.local/share",
            "--dir", "/home/sam/.local/share/uv", "--dir", "/home/sam/.local/share/uv/python",
            "--ro-bind", str(PYTHON), str(PYTHON), "--dir", "/opt/hermes", "--ro-bind", str(HERMES), "/opt/hermes",
            "--bind", str(profile), "/run/hermes-profile", "--ro-bind", str(inputs), "/trial",
            "--bind", str(outputs), "/trial/outputs", "--chdir", "/trial", "--setenv", "HOME", "/home/sam",
            "--setenv", "HERMES_REAL_HOME", "/home/sam", "--setenv", "HERMES_HOME", "/run/hermes-profile",
            "--setenv", "TERMINAL_CWD", "/trial", "--setenv", "PYTHONPATH", "/opt/hermes",
            "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
            "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID", "--unsetenv", "HERMES_SESSION_KEY",
            "--unsetenv", "HERMES_UI_SESSION_ID", "--", *command]


def support_sources(row: dict[str, Any]) -> list[tuple[Path, str]]:
    family = row["family_id"]; name = "epsilon" if family == "family-epsilon" else "zeta"
    other = "zeta" if name == "epsilon" else "epsilon"; condition = row["condition_id"]
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


def materialize(row: dict[str, Any], root: Path) -> dict[str, Path]:
    if root.exists():
        raise RuntimeError("attempt root exists; retry forbidden: " + str(root))
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    inputs.mkdir(parents=True); (inputs / "outputs").mkdir(); outputs.mkdir(); make_profile(profile)
    shutil.copy2(V7 / f"tasks/{row['task_id']}/public.md", inputs / "public-task.md")
    shutil.copy2(V7 / f"tasks/{row['task_id']}/input.json", inputs / "input.json")
    support = support_sources(row)
    if sum(path.stat().st_size for path, _ in support) > 16000:
        raise RuntimeError("treatment retrieval budget exceeded")
    for source, name in support:
        shutil.copy2(source, inputs / name)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


CANARY = r'''import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool
def readable(p):
 v=read_file_tool(p,limit=5).lower(); return not any(x in v for x in ('error','not found','denied','does not exist'))
visible=sorted(x for x in os.listdir('.') if x!='outputs')
r={'cwd':os.getcwd(),'visible':visible,'readable':{p:readable(p) for p in visible},
'private_denied':{p:not readable(p) for p in PRIVATE},'repo_search':search_tool('skill-bench',target='files',path='/home/sam',limit=20)}
r['output_write']='error' not in write_file_tool('outputs/canary.txt','v7-execution-canary\n').lower()
r['outside_write_denied']=any(x in write_file_tool('escape.txt','bad\n').lower() for x in ('error','denied','read-only','permission'))
print(json.dumps(r,sort_keys=True))'''


def full_surface_canary(paths: dict[str, Path], expected: set[str]) -> dict[str, Any]:
    code = "PRIVATE=" + repr(PRIVATE_PROBES) + "\n" + CANARY
    proc = subprocess.run(sandbox(paths["inputs"], paths["outputs"], paths["profile"],
                          ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
    try: observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError): observed = {}
    passed = (proc.returncode == 0 and observed.get("cwd") == "/trial" and set(observed.get("visible", [])) == expected
              and all(observed.get("readable", {}).values()) and all(observed.get("private_denied", {}).values())
              and "skill-bench" not in str(observed.get("repo_search", "")) and observed.get("output_write") is True
              and observed.get("outside_write_denied") is True)
    return {"passed": passed, "returncode": proc.returncode, "expected": sorted(expected), "observed": observed,
            "stderr": proc.stderr[-2000:], "model_calls": 0, "provider_calls": 0, "executor_attempts": 0}


def prompt() -> str:
    return ("Read public-task.md, input.json, and any other support files present in the current task directory. "
            "Complete the public task. Write only the requested strict JSON artifact to outputs/result.json. "
            "Do not write any other task artifact or commentary file.\n")


def run_trial(row: dict[str, Any], paths: dict[str, Path], pre: dict[str, Any]) -> dict[str, Any]:
    before = inventory(paths["inputs"]); text = prompt()
    command = ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", text,
               "--usage-file", "/trial/outputs/usage.json", "--model", MODEL, "--provider", PROVIDER,
               "--toolsets", "file", "--safe-mode"]
    started = datetime.now(timezone.utc).isoformat()
    try:
        proc = subprocess.run(sandbox(paths["inputs"], paths["outputs"], paths["profile"], command),
                              capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired as exc:
        out = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        err = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "timeout")
        proc = subprocess.CompletedProcess(command, 124, out, err)
    finished = datetime.now(timezone.utc).isoformat(); root = paths["inputs"].parent
    (root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8")
    (root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    try: usage = load(paths["outputs"] / "usage.json")
    except (OSError, json.JSONDecodeError): usage = {}
    service_valid = (proc.returncode == 0 and usage.get("completed") is True and usage.get("failed") is False
                     and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
                     and usage.get("model") == MODEL and usage.get("provider") == PROVIDER)
    environment_valid = before == inventory(paths["inputs"])
    result = paths["outputs"] / "result.json"; artifact_valid = False
    if result.is_file():
        try: artifact_valid = isinstance(load(result), dict) and load(result).get("task_id") == row["task_id"]
        except (json.JSONDecodeError, UnicodeDecodeError): pass
    check = subprocess.run([sys.executable, str(V7 / "checkers/check_endpoint.py"), "--candidate", str(result),
                            "--private", str(V7 / f"tasks/{row['task_id']}/private.json")], capture_output=True, text=True)
    try: checked = json.loads(check.stdout)
    except json.JSONDecodeError: checked = {"passed": False, "reason": "checker_invalid_output"}
    state = "attempted" if service_valid and environment_valid else ("service_failed" if not service_valid else "environment_failed")
    report = {**row, "attempts": 1, "attempt_state": state, "attempted": True, "skipped": False, "invalid": False,
              "service_valid": service_valid, "environment_valid": environment_valid, "artifact_valid": artifact_valid,
              "checker_scored": True, "endpoint_pass": checked.get("passed") is True, "checker_result": checked,
              "started_at": started, "finished_at": finished, "launcher_returncode": proc.returncode,
              "configured_system": {"model": MODEL, "provider": PROVIDER, "toolsets": ["file"], "safe_mode": True,
              "max_turns": 40, "declared_context_budget_tokens": 8000, "timeout_seconds": 900,
              "attempts_per_cell": 1, "feedback": "none"}, "input_inventory": before,
              "output_inventory": inventory(paths["outputs"]), "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(),
              "trace_sha256": sha(root / "redacted-trace.log"), "stderr_sha256": sha(root / "launcher-stderr.log"),
              "usage": usage, "preexecution_report_sha256": sha(HERE / "preexecution-report.json"),
              "claim_ceiling": CLAIMS, "repair_attempts": 0, "retry_attempts": 0}
    write_json(root / "trial-report.json", report); shutil.rmtree(paths["profile"], ignore_errors=True)
    return report


def summarize(rows: list[dict[str, Any]], assignments: list[dict[str, Any]], stop: str | None) -> dict[str, Any]:
    exact = []
    by_index = {r["schedule_index"]: r for r in rows}
    for assigned in assignments:
        row = by_index.get(assigned["schedule_index"])
        exact.append({"schedule_index": assigned["schedule_index"], "task_id": assigned["task_id"],
                      "family_id": assigned["family_id"], "condition_id": assigned["condition_id"],
                      "attempt_state": row["attempt_state"] if row else "skipped", "attempted": row is not None,
                      "service_valid": row["service_valid"] if row else False,
                      "environment_valid": row["environment_valid"] if row else False,
                      "artifact_valid": row["artifact_valid"] if row else False,
                      "checker_scored": row["checker_scored"] if row else False,
                      "endpoint_pass": row["endpoint_pass"] if row else False})
    families = ("family-epsilon", "family-zeta"); conditions = sorted({a["condition_id"] for a in assignments})
    rates: dict[str, dict[str, float | None]] = {f: {} for f in families}
    for family in families:
        for condition in conditions:
            subset = [r for r in rows if r["family_id"] == family and r["condition_id"] == condition and r["checker_scored"]]
            rates[family][condition] = sum(r["endpoint_pass"] for r in subset) / len(subset) if len(subset) == 2 else None
    contrasts = {}
    for expression in load(V4 / "protocol.json")["order_and_accounting"]["family_clustered_estimands"]:
        left, right = expression.split(" - "); values = {}
        for family in families:
            a, b = rates[family][left], rates[family][right]; values[family] = a - b if a is not None and b is not None else None
        available = [v for v in values.values() if v is not None]
        contrasts[expression] = {"family_differences": values, "cluster_count": len(available),
                                 "family_clustered_mean_difference": sum(available) / 2 if len(available) == 2 else None}
    states = {state: sum(r["attempt_state"] == state for r in exact) for state in ATTEMPT_STATES}
    return {"study_id": "pretask-procedure-transfer-v7-execution", "status": "complete" if len(rows) == 32 and not stop else "stopped_fail_closed",
            "stop_reason": stop, "denominators": {"intended": 32, "attempted": len(rows),
            "skipped": 32 - len(rows), "invalid": sum(r["attempt_state"] == "invalid" for r in exact),
            "service_valid": sum(r["service_valid"] for r in rows), "environment_valid": sum(r["environment_valid"] for r in rows),
            "artifact_valid": sum(r["artifact_valid"] for r in rows), "checker_scored": sum(r["checker_scored"] for r in rows),
            "endpoint_pass": sum(r["endpoint_pass"] for r in rows)}, "attempt_states": states, "exact_cells": exact,
            "family_condition_pass_rates": rates, "family_clustered_estimands": contrasts,
            "attempts": {"executor": len(rows), "model": len(rows), "provider": len(rows), "repair": 0, "retry": 0},
            "claim_ceiling": CLAIMS, "interpretation": "Bounded internal synthetic configured-system observations only; no capability, expert provenance, transfer, utility, professional validity, production fitness, or readiness claim."}


def main() -> int:
    rows = verify_rows_zero()
    pre_path = HERE / "preexecution-report.json"
    if pre_path.exists():
        raise RuntimeError("preexecution evidence exists; rerun forbidden")
    try:
        pre = verify_preconditions()
        pre.update({"status": "PASS", "checked_at": datetime.now(timezone.utc).isoformat(), "executor_attempts": 0})
    except Exception as exc:
        pre = {"status": "FAIL", "checked_at": datetime.now(timezone.utc).isoformat(), "executor_attempts": 0,
               "error": f"{type(exc).__name__}: {exc}", "claim_ceiling": CLAIMS}
        write_json(pre_path, pre); raise
    write_json(pre_path, pre)
    execution = HERE / "execution"; materialized = []
    for row in rows: materialized.append((row, materialize(row, execution / f"{row['schedule_index']:02d}-{row['task_id']}")))
    canary_root = HERE / ".full-surface-canary"; canary_paths = materialize(rows[0], canary_root)
    expected = {"public-task.md", "input.json"} | {name for _, name in support_sources(rows[0])}
    canary = full_surface_canary(canary_paths, expected); shutil.rmtree(canary_root)
    inventories = []
    for row, paths in materialized:
        expected_files = {"public-task.md", "input.json"} | {name for _, name in support_sources(row)}
        actual = set(inventory(paths["inputs"])) - {"outputs"}
        inventories.append({"schedule_index": row["schedule_index"], "passed": actual == expected_files,
                            "expected": sorted(expected_files), "actual": sorted(actual)})
    canary_report = {"status": "PASS" if canary["passed"] and all(x["passed"] for x in inventories) else "FAIL",
                     "full_file_tool_surface": canary, "materialized_inventory_checks": inventories,
                     "model_calls": 0, "provider_calls": 0, "executor_attempts": 0, "claim_ceiling": CLAIMS}
    write_json(HERE / "execution-canary-report.json", canary_report)
    if canary_report["status"] != "PASS":
        write_json(HERE / "execution-report.json", summarize([], rows, "full-surface canary or materialized inventory failed")); return 1
    observed = []; stop = None
    for row, paths in materialized:
        report = run_trial(row, paths, pre); observed.append(report)
        print(json.dumps({"schedule_index": row["schedule_index"], "attempt_state": report["attempt_state"],
                          "endpoint_pass": report["endpoint_pass"]}), flush=True)
        if not report["service_valid"] or not report["environment_valid"]:
            stop = f"fail-closed service/cost/environment gate at schedule_index {row['schedule_index']}"; break
    summary = summarize(observed, rows, stop); summary["preexecution_report_sha256"] = sha(pre_path)
    summary["execution_canary_report_sha256"] = sha(HERE / "execution-canary-report.json")
    write_json(HERE / "execution-report.json", summary); print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["status"] == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
