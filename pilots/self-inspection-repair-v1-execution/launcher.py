#!/usr/bin/env python3
"""Commit-bound, one-shot executor for the frozen self-inspection repair v1 matrix.

This launcher is deliberately outside ``pilots/self-inspection-repair-v1``: no
frozen v1 byte is changed.  It executes each declared assignment at most once,
retains invalid attempts, and treats endpoint observations as internal fixture
evidence only.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FROZEN = ROOT / "pilots/self-inspection-repair-v1"
FREEZE_COMMIT = "7d976a28b9f33337f2f90519964361388b3eae7f"
AUDIT = ROOT / "reports/validation/2026-07-19-self-inspection-repair-v1-freeze-audit.json"
EXECUTION = HERE / "execution"
PREFLIGHT = HERE / "preflight"
BASE_PATH = ROOT / "pilots/configured-artifact-revision/launcher.py"
MODEL = "gpt-5.6-sol"
PROVIDER = "openai-codex"
TERMINAL_STATES = {"criterion_fail", "environment_invalid", "insufficient_evidence", "invalid_artifact", "observer_invalid", "passed", "service_invalid"}
CLAIM_CEILING = {
    "self_correction": False,
    "agent_capability": False,
    "treatment_effect": False,
    "professional_validity": False,
    "utility": False,
    "production_fitness": False,
    "readiness": False,
}


def module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


base = module("repair_execution_base", BASE_PATH)
checker = module("repair_frozen_checker", FROZEN / "checkers/check_fixtures.py")


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root: Path) -> dict[str, dict[str, Any]]:
    return {
        path.relative_to(root).as_posix(): {"sha256": sha(path), "bytes": path.stat().st_size}
        for path in sorted(root.rglob("*")) if path.is_file()
    } if root.exists() else {}


def git_bytes(commit: str, relative: str) -> bytes:
    proc = subprocess.run(
        ["git", "show", f"{commit}:pilots/self-inspection-repair-v1/{relative}"],
        cwd=ROOT, capture_output=True,
    )
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode(errors="replace"))
    return proc.stdout


def prompt_text(task: dict[str, Any], condition: dict[str, Any], prompt_spec: dict[str, Any]) -> str:
    task_doc = load(FROZEN / task["task"])
    source_doc = load(FROZEN / task["source"])
    initial = (FROZEN / task["starting_artifact"]).read_text(encoding="utf-8")
    visible = prompt_spec.get("visible_text_by_task", {}).get(task["task_id"], prompt_spec.get("visible_text", ""))
    extension = ".md" if task["shape"] == "memo" else ".json"
    return (
        "You are completing one bounded internal artifact-repair assignment.\n"
        "The task, source evidence, and common starting artifact below are the complete common context.\n"
        f"TASK:\n{json.dumps(task_doc, indent=2)}\n\nSOURCE:\n{json.dumps(source_doc, indent=2)}\n\n"
        f"COMMON STARTING ARTIFACT:\n{initial}\n\nCONDITION INSTRUCTION:\n{visible}\n\n"
        + (
            "Do not revise the artifact and do not call tools. The launcher retains the starting artifact."
            if not condition["repair_authorized"] else
            f"Produce at most one revision. Write the complete revised artifact to outputs/revised-artifact{extension}. "
            "Also write outputs/repair-record.json as a JSON object with string fields defect_observation, diagnosis, "
            "revision_delta, criterion_local_recheck, collateral_recheck, new_error_assessment. Do not mention or infer "
            "private evaluator material beyond the condition instruction. Work only from allowlisted files and outputs/."
        )
    )


def materialize(root: Path, task: dict[str, Any], condition: dict[str, Any], prompt: str) -> dict[str, Path]:
    if root.exists():
        raise FileExistsError(root)
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    inputs.mkdir(parents=True)
    (inputs / "outputs").mkdir()
    outputs.mkdir()
    (inputs / "public-prompt.txt").write_text(prompt, encoding="utf-8")
    # Source is common public evidence. Native/render files are an additional view only in the declared arm.
    shutil.copy2(FROZEN / task["source"], inputs / "source.json")
    if condition["condition_id"] == "native_render_self_inspection":
        shutil.copy2(FROZEN / task["native_view"], inputs / Path(task["native_view"]).name)
        shutil.copy2(FROZEN / task["render_view"], inputs / Path(task["render_view"]).name)
    dump(inputs / "manifest.json", {
        "assignment_scope": "one frozen assignment",
        "task_id": task["task_id"],
        "condition_id": condition["condition_id"],
        "visible_files": sorted(p.name for p in inputs.iterdir() if p.is_file()),
        "inputs": "read_only",
        "only_writable_path": "outputs",
        "repository_private_files": "excluded",
        "toolsets": ["file"],
    })
    base._copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


CANARY = r'''import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool

def readable(path):
    text=read_file_tool(path,limit=3).lower()
    return not any(x in text for x in ("error reading","not found","permission denied","does not exist"))
visible=VISIBLE
private=["protocol.json","freeze-manifest.json","check_fixtures.py","data/work_queue.json","/home/sam/skill-bench/data/work_queue.json"]
observed={"cwd":os.getcwd(),"visible":{p:readable(p) for p in visible},"private_denied":{p:not readable(p) for p in private},"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=10)}
observed["output_write"]="error" not in write_file_tool("outputs/canary.txt","ok\n").lower()
observed["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower()
print(json.dumps(observed,sort_keys=True))'''


def isolation_canary(assignment: dict[str, Any], task: dict[str, Any], condition: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="repair-v1-canary-") as tmp:
        prompt = prompt_for(assignment, task, condition)
        paths = materialize(Path(tmp) / "trial", task, condition, prompt)
        visible = sorted(p.name for p in paths["inputs"].iterdir() if p.is_file())
        code = "VISIBLE=" + repr(visible) + "\n" + CANARY
        proc = subprocess.run(base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
        try:
            observed = json.loads(proc.stdout.strip().splitlines()[-1])
        except Exception:
            observed = {}
        passed = (
            proc.returncode == 0 and observed.get("cwd") == "/trial"
            and all(observed.get("visible", {}).values())
            and all(observed.get("private_denied", {}).values())
            and observed.get("output_write") is True and observed.get("escape_denied") is True
            and "skill-bench" not in str(observed.get("repository_search", ""))
        )
        return {"assignment_id": assignment["assignment_id"], "passed": passed, "model_calls": 0, "visible_files": visible,
                "observed": observed, "returncode": proc.returncode, "stderr": proc.stderr[-1000:]}


def prompt_for(assignment: dict[str, Any], task: dict[str, Any], condition: dict[str, Any]) -> str:
    prompts = {row["condition_id"]: row for row in load(FROZEN / "prompts.json")["prompts"]}
    return prompt_text(task, condition, prompts[assignment["condition_id"]])


def historical_zero_cost_gate() -> dict[str, Any]:
    candidates = []
    for path in ROOT.glob("pilots/**/usage.json"):
        try:
            usage = load(path)
        except Exception:
            continue
        if (usage.get("provider") == PROVIDER and usage.get("model") == MODEL and usage.get("completed") is True
                and usage.get("failed") is False and usage.get("cost_status") == "included"
                and usage.get("estimated_cost_usd") == 0.0):
            candidates.append((path.stat().st_mtime, path, usage))
    if not candidates:
        return {"passed": False, "model_calls": 0, "reason": "no exact-provider included-zero-cost witness"}
    _, path, usage = max(candidates)
    return {"passed": True, "model_calls": 0, "kind": "historical_no_cost_provider_witness",
            "path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "model": usage["model"],
            "provider": usage["provider"], "cost_status": usage["cost_status"],
            "estimated_cost_usd": usage["estimated_cost_usd"],
            "boundary": "Pre-call feasibility only; each assignment retains its own usage and cost result."}


def launcher_on_origin() -> dict[str, Any]:
    fetch = subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, capture_output=True, text=True)
    rel = Path(__file__).resolve().relative_to(ROOT).as_posix()
    remote = subprocess.run(["git", "show", f"origin/main:{rel}"], cwd=ROOT, capture_output=True)
    local_sha = sha(Path(__file__))
    remote_sha = hashlib.sha256(remote.stdout).hexdigest() if remote.returncode == 0 else None
    return {"passed": fetch.returncode == 0 and remote.returncode == 0 and local_sha == remote_sha,
            "path": rel, "local_sha256": local_sha, "origin_main_sha256": remote_sha,
            "origin_main": subprocess.run(["git", "rev-parse", "origin/main"], cwd=ROOT, capture_output=True, text=True).stdout.strip(),
            "fetch_stderr": fetch.stderr[-1000:], "model_calls": 0}


def equal_envelope(protocol: dict[str, Any]) -> dict[str, Any]:
    shared = ["tool_id", "harness_id", "model_id", "provider_id", "budget_id"]
    conditions = protocol["conditions"]
    passed = all(len({row[key] for row in conditions}) == 1 for key in shared)
    return {"passed": passed, "shared_fields": shared,
            "allowed_differences": ["condition_id", "hidden_criterion_access", "information_treatment", "prompt_source", "repair_authorized"],
            "observed": {key: sorted({row[key] for row in conditions}) for key in shared}, "model_calls": 0}


def preflight(require_origin: bool = True, write: bool = True) -> dict[str, Any]:
    protocol = load(FROZEN / "protocol.json")
    audit = load(AUDIT)
    tasks = {row["task_id"]: row for row in protocol["tasks"]}
    conditions = {row["condition_id"]: row for row in protocol["conditions"]}
    frozen_hashes = []
    for binding in load(FROZEN / "freeze-manifest.json")["bindings"]:
        observed = hashlib.sha256(git_bytes(FREEZE_COMMIT, binding["path"])).hexdigest()
        frozen_hashes.append({"path": binding["path"], "expected": binding["sha256"], "observed": observed, "passed": observed == binding["sha256"]})
    canaries = [isolation_canary(row, tasks[row["task_id"]], conditions[row["condition_id"]]) for row in protocol["assignments"]]
    origin = launcher_on_origin() if require_origin else {"passed": True, "waived_for_test_only": True, "model_calls": 0}
    report = {
        "kind": "self_inspection_repair_v1_execution_preflight", "model_calls": 0,
        "freeze_commit": FREEZE_COMMIT, "independent_audit_sha256": sha(AUDIT),
        "independent_audit_passed": audit.get("status") == "PASS" and audit.get("source_binding", {}).get("resolved_commit") == FREEZE_COMMIT,
        "frozen_commit_bindings": frozen_hashes, "launcher_on_origin": origin,
        "equal_envelope": equal_envelope(protocol), "isolation_canaries": canaries,
        "service_and_cost": historical_zero_cost_gate(), "execution_root_absent": not EXECUTION.exists(),
        "claim_ceiling": CLAIM_CEILING,
    }
    report["passed"] = (
        report["independent_audit_passed"] and all(row["passed"] for row in frozen_hashes)
        and origin["passed"] and report["equal_envelope"]["passed"]
        and all(row["passed"] for row in canaries) and report["service_and_cost"]["passed"]
        and report["execution_root_absent"] and not any(CLAIM_CEILING.values())
    )
    if write:
        dump(PREFLIGHT / "gate-report.json", report)
    return report


def trial_command(prompt: str) -> list[str]:
    return ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt,
            "--usage-file", "/trial/outputs/usage.json", "--model", MODEL,
            "--provider", PROVIDER, "--toolsets", "file", "--safe-mode"]


def parse_candidate(path: Path, shape: str) -> Any:
    if not path.is_file():
        return None
    if shape == "memo":
        return path.read_text(encoding="utf-8")
    try:
        return load(path)
    except Exception:
        return None


def diff_summary(before: str, after: str) -> dict[str, Any]:
    lines = list(difflib.unified_diff(before.splitlines(), after.splitlines(), fromfile="starting", tofile="final", lineterm=""))
    return {"changed": before != after, "unified_diff": lines[:200], "truncated": len(lines) > 200}


def run_assignment(protocol: dict[str, Any], assignment: dict[str, Any]) -> dict[str, Any]:
    tasks = {row["task_id"]: row for row in protocol["tasks"]}
    conditions = {row["condition_id"]: row for row in protocol["conditions"]}
    task, condition = tasks[assignment["task_id"]], conditions[assignment["condition_id"]]
    root = EXECUTION / "assignments" / assignment["assignment_id"]
    prompt = prompt_for(assignment, task, condition)
    paths = materialize(root / "trial", task, condition, prompt)
    dump(root / "information-view.json", {
        "assignment_id": assignment["assignment_id"], "assignment_sha256": assignment["assignment_sha256"],
        "prompt": prompt, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "input_inventory": inventory(paths["inputs"]), "condition": condition,
    })
    initial_path = FROZEN / task["starting_artifact"]
    extension = ".md" if task["shape"] == "memo" else ".json"
    candidate_path = paths["outputs"] / f"revised-artifact{extension}"
    before_inventory = inventory(paths["inputs"])
    started = time.monotonic()
    provider_called = condition["repair_authorized"]
    if provider_called:
        try:
            proc = subprocess.run(base._bwrap(paths, trial_command(prompt)), capture_output=True, text=True, timeout=300)
            stdout, stderr, returncode = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            stderr += "\nlauncher timeout at frozen 300-second wall budget\n"
            returncode = 124
    else:
        shutil.copy2(initial_path, candidate_path)
        stdout, stderr, returncode = "", "", 0
    elapsed = time.monotonic() - started
    (root / "redacted-trace.log").write_text(stdout, encoding="utf-8")
    (root / "launcher-stderr.log").write_text(stderr, encoding="utf-8")
    after_inventory = inventory(paths["inputs"])
    input_integrity = before_inventory == after_inventory
    usage = load(paths["outputs"] / "usage.json") if (paths["outputs"] / "usage.json").is_file() else {}
    if not provider_called:
        usage = {"provider_called": False, "completed": True, "failed": False, "cost_status": "not_applicable", "estimated_cost_usd": 0.0, "api_calls": 0}
        dump(paths["outputs"] / "usage.json", usage)
    service_valid = (not provider_called) or (returncode == 0 and usage.get("completed") is True and usage.get("failed") is False)
    no_cost = (not provider_called) or (usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0)
    candidate = parse_candidate(candidate_path, "memo" if task["shape"] == "memo" else "structured")
    endpoint = checker.evaluate("memo" if task["shape"] == "memo" else "structured", candidate)
    agent_record_path = paths["outputs"] / "repair-record.json"
    try:
        agent_record = load(agent_record_path) if agent_record_path.is_file() else None
    except Exception:
        agent_record = None
    required_record = ["defect_observation", "diagnosis", "revision_delta", "criterion_local_recheck", "collateral_recheck", "new_error_assessment"]
    record_valid = (not provider_called) or (isinstance(agent_record, dict) and all(isinstance(agent_record.get(key), str) and agent_record[key].strip() for key in required_record))
    if not input_integrity:
        terminal = "environment_invalid"
    elif not service_valid or not no_cost:
        terminal = "service_invalid"
    elif candidate is None:
        terminal = "invalid_artifact"
    elif not record_valid:
        terminal = "observer_invalid"
    else:
        terminal = endpoint["terminal_state"]
    initial_text = initial_path.read_text(encoding="utf-8")
    final_text = candidate_path.read_text(encoding="utf-8") if candidate_path.is_file() else ""
    repair_record = {
        "assignment_id": assignment["assignment_id"], "observation_unit": "proposition",
        "defect_observation": agent_record.get("defect_observation") if isinstance(agent_record, dict) else (task["defect_proposition"] if not provider_called else None),
        "diagnosis": agent_record.get("diagnosis") if isinstance(agent_record, dict) else ("not elicited; no repair authorized" if not provider_called else None),
        "revision_delta": {"agent_statement": agent_record.get("revision_delta") if isinstance(agent_record, dict) else "no revision authorized", **diff_summary(initial_text, final_text)},
        "criterion_local_recheck": {"agent_statement": agent_record.get("criterion_local_recheck") if isinstance(agent_record, dict) else None, "endpoint": endpoint.get("endpoint"), "terminal_state": endpoint["terminal_state"]},
        "collateral_recheck": {"agent_statement": agent_record.get("collateral_recheck") if isinstance(agent_record, dict) else None, "preserved": endpoint.get("collateral")},
        "new_error_assessment": {"agent_statement": agent_record.get("new_error_assessment") if isinstance(agent_record, dict) else None, "deterministic_scope": "Only planted endpoint and declared collateral are checked."},
        "cost": {"wall_seconds": round(elapsed, 6), "usage": usage},
    }
    dump(root / "repair-record.json", repair_record)
    trace_path = root / "redacted-trace.log"
    report = {
        "assignment_id": assignment["assignment_id"], "task_id": task["task_id"], "condition_id": condition["condition_id"],
        "assignment_sha256": assignment["assignment_sha256"], "attempt_count": 1, "provider_called": provider_called,
        "starting_artifact": {"path": task["starting_artifact"], "sha256": sha(initial_path)},
        "final_artifact": {"path": candidate_path.relative_to(root).as_posix() if candidate_path.is_file() else None,
                           "sha256": sha(candidate_path) if candidate_path.is_file() else None},
        "redacted_trace": {"path": trace_path.relative_to(root).as_posix(), "sha256": sha(trace_path), "policy": "stdout/final response only; credentials, provider headers, and raw session state excluded"},
        "usage": usage, "input_integrity": input_integrity, "service_valid": service_valid, "no_cost": no_cost,
        "agent_repair_record_valid": record_valid, "deterministic_observation": endpoint, "terminal_state": terminal,
        "outputs": inventory(paths["outputs"]), "claim_ceiling": CLAIM_CEILING,
    }
    if terminal not in TERMINAL_STATES:
        raise AssertionError(terminal)
    dump(root / "attempt-report.json", report)
    shutil.rmtree(paths["profile"], ignore_errors=True)
    return report


def build_report(protocol: dict[str, Any]) -> dict[str, Any]:
    rows = [load(EXECUTION / "assignments" / assignment["assignment_id"] / "attempt-report.json") for assignment in protocol["assignments"]]
    by_task: dict[str, Any] = {}
    for task in protocol["tasks"]:
        task_rows = [row for row in rows if row["task_id"] == task["task_id"]]
        first = next(row for row in task_rows if row["condition_id"] == "no_second_attempt")
        by_task[task["task_id"]] = {
            "first_endpoint": first["deterministic_observation"],
            "final_by_condition": {row["condition_id"]: {"terminal_state": row["terminal_state"], "deterministic_observation": row["deterministic_observation"], "final_sha256": row["final_artifact"]["sha256"]} for row in task_rows},
        }
    conditions = {}
    for condition in protocol["conditions"]:
        xs = [row for row in rows if row["condition_id"] == condition["condition_id"]]
        conditions[condition["condition_id"]] = {
            "declared": 2, "valid_terminal": sum(row["terminal_state"] in {"passed", "criterion_fail"} for row in xs),
            "passed": sum(row["terminal_state"] == "passed" for row in xs),
            "terminal_states": {state: sum(row["terminal_state"] == state for row in xs) for state in sorted(TERMINAL_STATES)},
        }
    return {
        "schema_version": "1.0.0", "report_id": "self-inspection-repair-v1-bounded-execution",
        "freeze_commit": FREEZE_COMMIT, "launcher": {"path": Path(__file__).resolve().relative_to(ROOT).as_posix(), "sha256": sha(Path(__file__))},
        "declared_assignments": 12, "attempts_retained": len(rows), "provider_calls": sum(row["provider_called"] for row in rows),
        "first_and_final_by_task": by_task, "six_condition_contrasts": conditions,
        "assignment_rows": rows, "claim_ceiling": CLAIM_CEILING,
        "interpretation": "One attempt per builder-authored assignment. Descriptive endpoint observations only; no self-correction, capability, treatment-effect, professional, utility, production, or readiness claim is licensed.",
    }


def execute() -> dict[str, Any]:
    gate = preflight(require_origin=True, write=True)
    if not gate["passed"]:
        blocked = {"status": "blocked_before_model_calls", "model_calls": 0, "gate_report": "preflight/gate-report.json", "claim_ceiling": CLAIM_CEILING}
        dump(HERE / "feasibility-report.json", blocked)
        return blocked
    EXECUTION.mkdir(parents=True)
    protocol = load(FROZEN / "protocol.json")
    rows = []
    for assignment in protocol["assignments"]:
        rows.append(run_assignment(protocol, assignment))
        # A nonzero/unknown cost result stops future calls but remains in the complete attempt ledger.
        if rows[-1]["provider_called"] and not rows[-1]["no_cost"]:
            break
    report = build_report(protocol) if len(rows) == 12 else {
        "status": "stopped_on_cost_gate", "attempts_retained": len(rows), "declared_assignments": 12,
        "unstarted_assignments": [row["assignment_id"] for row in protocol["assignments"][len(rows):]], "claim_ceiling": CLAIM_CEILING,
    }
    dump(EXECUTION / "study-report.json", report)
    return report


def replay() -> dict[str, Any]:
    protocol = load(FROZEN / "protocol.json")
    observed = build_report(protocol)
    retained = load(EXECUTION / "study-report.json")
    if observed != retained:
        raise ValueError("study report replay mismatch")
    return observed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("preflight", "execute", "replay"))
    parser.add_argument("--no-origin-check", action="store_true", help="preflight test only; execute always requires origin")
    args = parser.parse_args()
    result = preflight(not args.no_origin_check) if args.mode == "preflight" else execute() if args.mode == "execute" else replay()
    passed = result.get("passed", result.get("attempts_retained") == 12)
    print(json.dumps({"mode": args.mode, "passed": passed, "attempts_retained": result.get("attempts_retained"), "provider_calls": result.get("provider_calls"), "status": result.get("status")}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
