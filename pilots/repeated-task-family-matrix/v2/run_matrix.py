#!/usr/bin/env python3
"""Gate, execute exactly once, and replay repeated task-family matrix v2."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "protocol.json"
EXEC = HERE / "execution"
PREFLIGHT = HERE / "preflight"
BASE = ROOT / "pilots/configured-artifact-revision/launcher.py"


def module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


base = module("matrix_v2_base", BASE)
grader = module("matrix_v2_grader", HERE / "grade.py")


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root: Path) -> dict[str, dict[str, Any]]:
    return {path.relative_to(root).as_posix(): {"sha256": sha(path), "bytes": path.stat().st_size} for path in sorted(root.rglob("*")) if path.is_file()}


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def verify_protocol(protocol: dict, require_pushed: bool = False) -> dict:
    errors = []
    rows = protocol.get("schedule", {}).get("rows", [])
    if len(protocol.get("forms", {})) != 4:
        errors.append("exactly four forms required")
    if len(rows) != 8 or len({row["attempt_id"] for row in rows}) != 8:
        errors.append("eight unique attempts required")
    for key in protocol.get("forms", {}):
        if sum(row["family"] + "/" + row["form"] == key for row in rows) != 2:
            errors.append(f"two repeats required: {key}")
    for component in protocol.get("frozen_components", []):
        path = HERE / component["path"]
        if not path.is_file() or sha(path) != component["sha256"]:
            errors.append(f"component drift: {component['path']}")
    if any(protocol.get("claim_boundaries", {}).values()):
        errors.append("claim ceiling upgraded")
    current_v1 = git("rev-parse", "HEAD:pilots/repeated-task-family-matrix/v1")
    expected_v1 = protocol.get("v1_preservation", {}).get("git_tree_at_freeze")
    if current_v1.returncode or current_v1.stdout.strip() != expected_v1:
        errors.append("v1 tree differs from frozen tree")
    if git("diff", "--quiet", "--", "pilots/repeated-task-family-matrix/v1").returncode:
        errors.append("working tree modifies v1 bytes")
    pushed = None
    if require_pushed:
        fetch = git("fetch", "origin", "main")
        if fetch.returncode:
            errors.append("git fetch origin/main failed")
        remote = subprocess.run(["git", "show", "origin/main:pilots/repeated-task-family-matrix/v2/protocol.json"], cwd=ROOT, capture_output=True)
        if remote.returncode or hashlib.sha256(remote.stdout).hexdigest() != sha(PROTOCOL):
            errors.append("frozen protocol bytes are not on origin/main")
        else:
            pushed = git("rev-parse", "origin/main").stdout.strip()
        instrument_paths = ["pilots/repeated-task-family-matrix/v2/protocol.json", "pilots/repeated-task-family-matrix/v2/forms", "pilots/repeated-task-family-matrix/v2/grade.py", "pilots/repeated-task-family-matrix/v2/run_matrix.py", "pilots/repeated-task-family-matrix/v2/README.md"]
        if git("diff", "--quiet", "origin/main", "--", *instrument_paths).returncode:
            errors.append("tracked v2 instrument differs from origin/main")
    return {"passed": not errors, "errors": errors, "protocol_sha256": sha(PROTOCOL), "component_count": len(protocol["frozen_components"]), "v1_tree_preserved": not any("v1" in item for item in errors), "pushed_commit": pushed}


def materialize(root: Path, key: str) -> dict[str, Path]:
    if root.exists():
        raise FileExistsError(root)
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    inputs.mkdir(parents=True)
    (inputs / "outputs").mkdir()
    outputs.mkdir()
    form = HERE / "forms" / key
    shutil.copy2(form / "public-task.md", inputs / "public-task.md")
    shutil.copy2(form / "source.json", inputs / "source.json")
    dump(inputs / "manifest.json", {"form": key, "inputs": "read_only", "only_writable": "outputs", "agent_toolsets": ["file"], "private_roles_excluded": ["protocol", "private_expected", "task_health", "grader", "preflight", "other_attempts", "repository", "v1"]})
    base._copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


def isolation_canary(key: str) -> dict:
    with tempfile.TemporaryDirectory(prefix="matrix-v2-canary-") as temporary:
        paths = materialize(Path(temporary) / "trial", key)
        code = r'''import json,os
from tools.file_tools import read_file_tool,search_tool,write_file_tool
def ok(p):
 t=read_file_tool(p,limit=3).lower(); return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
private=["private-expected.json","task-health.json","protocol.json","grade.py","../v1/protocol.json","/home/sam/skill-bench/data/work_queue.json"]
o={"cwd":os.getcwd(),"public":{p:ok(p) for p in ["public-task.md","source.json","manifest.json"]},"private_denied":{p:not ok(p) for p in private},"write_output":"error" not in write_file_tool("outputs/canary.txt","ok\n").lower(),"escape_denied":"error" in write_file_tool("escape.txt","bad\n").lower(),"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=10)}
print(json.dumps(o,sort_keys=True))'''
        process = subprocess.run(base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
        try:
            observed = json.loads(process.stdout.strip().splitlines()[-1])
        except Exception:
            observed = {}
        passed = process.returncode == 0 and observed.get("cwd") == "/trial" and all(observed.get("public", {}).values()) and all(observed.get("private_denied", {}).values()) and observed.get("write_output") is True and observed.get("escape_denied") is True and "skill-bench" not in str(observed.get("repository_search", ""))
        return {"form": key, "passed": passed, "model_calls": 0, "observed": observed, "returncode": process.returncode, "stderr": process.stderr[-1000:]}


def calibration(protocol: dict) -> dict:
    rows = []
    all_passed = True
    for key, form_spec in protocol["forms"].items():
        expected = load(HERE / form_spec["authoritative_output"])
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "report.json"
            base_value = {"decision": expected["accepted_decisions"][0], "action": expected["accepted_actions"][0], "evidence_ids": expected["evidence_ids"], "rationale": "The controlling record applies; the other records are outdated or advisory."}
            cases = {"canonical": (base_value, "pass"), "alternative_decision_1": (base_value | {"decision": expected["accepted_decisions"][1]}, "pass"), "alternative_decision_2": (base_value | {"decision": expected["accepted_decisions"][2]}, "pass"), "alternative_action_1": (base_value | {"action": expected["accepted_actions"][1]}, "pass"), "alternative_action_2": (base_value | {"action": expected["accepted_actions"][2]}, "pass"), "wrong_decision_1": (base_value | {"decision": expected["near_neighbor_wrong_decisions"][0]}, "fail"), "wrong_decision_2": (base_value | {"decision": expected["near_neighbor_wrong_decisions"][1]}, "fail"), "wrong_action_1": (base_value | {"action": expected["near_neighbor_wrong_actions"][0]}, "fail"), "wrong_action_2": (base_value | {"action": expected["near_neighbor_wrong_actions"][1]}, "fail"), "wrong_evidence": (base_value | {"evidence_ids": ["NONCONTROLLING"]}, "fail"), "alternative_rationale": (base_value | {"rationale": "A lower-rank record cannot displace the in-scope measurement."}, "pass")}
            observed = {}
            for name, (value, wanted) in cases.items():
                dump(output, value)
                observed[name] = grader.grade(output, expected)["classification"]
            observed["invalid_json"] = "fail" if (output.write_text("not json", encoding="utf-8") or True) and grader.grade(output, expected)["classification"] == "fail" else "unexpected"
            wanted = {name: classification for name, (_, classification) in cases.items()} | {"invalid_json": "fail"}
            passed = observed == wanted
            all_passed &= passed
            rows.append({"form": key, "passed": passed, "accepted_decision_realizations_tested": 3, "accepted_action_realizations_tested": 3, "near_neighbor_wrong_decisions_tested": 2, "near_neighbor_wrong_actions_tested": 2, "results": observed})
    return {"kind": "fair_basis_alternative_and_near_neighbor_calibration", "passed": all_passed, "model_calls": 0, "cases": rows}


def provider_gate() -> dict:
    candidates = []
    for path in ROOT.glob("pilots/**/usage.json"):
        try:
            value = load(path)
        except Exception:
            continue
        if value.get("provider") == "openai-codex" and value.get("model") == "gpt-5.6-sol" and value.get("completed") is True and value.get("failed") is False and value.get("cost_status") == "included" and value.get("estimated_cost_usd") == 0.0:
            candidates.append((path.stat().st_mtime, path, value))
    if not candidates:
        return {"passed": False, "reason": "no exact-provider included-cost witness", "model_calls": 0}
    _, path, value = max(candidates)
    return {"passed": True, "kind": "historical_service_and_cost_canary", "model_calls": 0, "evidence_path": path.relative_to(ROOT).as_posix(), "evidence_sha256": sha(path), "provider": value["provider"], "model": value["model"], "cost_status": value["cost_status"], "estimated_cost_usd": value["estimated_cost_usd"], "boundary": "Historical feasibility only; every declared attempt retains its own result."}


def preflight(require_pushed: bool) -> dict:
    protocol = load(PROTOCOL)
    protocol_result = verify_protocol(protocol, require_pushed)
    isolation = [isolation_canary(key) for key in protocol["forms"]]
    grader_result = calibration(protocol)
    provider = provider_gate()
    report = {"kind": "repeated_matrix_v2_pre_call_gates", "model_calls": 0, "protocol": protocol_result, "isolation_and_leakage": isolation, "grader_calibration_and_mutation": grader_result, "service_and_cost": provider}
    report["passed"] = protocol_result["passed"] and all(item["passed"] for item in isolation) and grader_result["passed"] and provider["passed"]
    dump(PREFLIGHT / "gate-report.json", report)
    return report


def trial_cmd(prompt: str) -> list[str]:
    return ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt, "--usage-file", "/trial/outputs/usage.json", "--model", "gpt-5.6-sol", "--provider", "openai-codex", "--toolsets", "file", "--safe-mode"]


def run_attempt(protocol: dict, row: dict) -> dict:
    root = EXEC / "attempts" / row["attempt_id"]
    key = row["family"] + "/" + row["form"]
    paths = materialize(root / "trial", key)
    before = inventory(paths["inputs"])
    prompt = (paths["inputs"] / "public-task.md").read_text(encoding="utf-8") + "\nWork only from source.json and write the required output under outputs/."
    try:
        process = subprocess.run(base._bwrap(paths, trial_cmd(prompt)), capture_output=True, text=True, timeout=900)
        returncode, stdout, stderr = process.returncode, process.stdout, process.stderr
    except subprocess.TimeoutExpired as exc:
        returncode, stdout, stderr = 124, exc.stdout or "", exc.stderr or "timeout"
    (root / "redacted-trace.log").write_text(stdout, encoding="utf-8")
    (root / "launcher-stderr.log").write_text(stderr, encoding="utf-8")
    changed = before != inventory(paths["inputs"])
    usage = load(paths["outputs"] / "usage.json") if (paths["outputs"] / "usage.json").is_file() else {}
    report_path = paths["outputs"] / "report.json"
    service_valid = returncode == 0 and usage.get("completed") is True and usage.get("failed") is False
    cost_valid = usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
    environment_valid = service_valid and cost_valid and not changed
    grader_valid = environment_valid and report_path.is_file()
    grade_result = grader.grade(report_path, load(HERE / protocol["forms"][key]["authoritative_output"])) if grader_valid else None
    substantive = grader_valid and grade_result is not None
    if grade_result:
        dump(root / "grade.json", grade_result)
    confidence = {"status": "insufficient_evidence", "reason": "No genuinely provider-emitted logprob or calibrated-confidence field was present in retained usage/trace."}
    trial = {**row, "launcher_invocations": 1, "returncode": returncode, "service_valid": service_valid, "cost_valid": cost_valid, "environment_valid": environment_valid, "grader_valid": grader_valid, "substantively_graded": substantive, "input_integrity": not changed, "usage": usage, "grade": grade_result, "confidence_channel": confidence, "artifacts": inventory(paths["outputs"]), "claim_boundaries": protocol["claim_boundaries"]}
    dump(root / "trial-report.json", trial)
    shutil.rmtree(paths["profile"], ignore_errors=True)
    return trial


def wilson(k: int, n: int, z: float = 1.95996398454) -> list[float] | None:
    if not n:
        return None
    proportion = k / n
    denominator = 1 + z * z / n
    center = (proportion + z * z / (2 * n)) / denominator
    half = z * math.sqrt(proportion * (1 - proportion) / n + z * z / (4 * n * n)) / denominator
    return [round(max(0, center - half), 6), round(min(1, center + half), 6)]


def build_report(protocol: dict) -> dict:
    trials = [load(EXEC / "attempts" / row["attempt_id"] / "trial-report.json") if (EXEC / "attempts" / row["attempt_id"] / "trial-report.json").is_file() else {**row, "status": "unstarted", "service_valid": False, "environment_valid": False, "grader_valid": False, "substantively_graded": False, "grade": None} for row in protocol["schedule"]["rows"]]
    denominators = {"intended": len(trials), "service_valid": sum(item["service_valid"] for item in trials), "environment_valid": sum(item["environment_valid"] for item in trials), "grader_valid": sum(item["grader_valid"] for item in trials), "substantively_graded": sum(item["substantively_graded"] for item in trials)}
    substantive = [item for item in trials if item["substantively_graded"]]
    passes = sum(item["grade"]["classification"] == "pass" for item in substantive)
    forms = {}
    for key in protocol["forms"]:
        family, form = key.split("/")
        items = [item for item in trials if item["family"] == family and item["form"] == form]
        graded = [item for item in items if item["substantively_graded"]]
        form_passes = sum(item["grade"]["classification"] == "pass" for item in graded)
        forms[key] = {"intended": 2, "service_valid": sum(item["service_valid"] for item in items), "environment_valid": sum(item["environment_valid"] for item in items), "grader_valid": sum(item["grader_valid"] for item in items), "substantively_graded": len(graded), "passes": form_passes, "pass_rate": form_passes / len(graded) if graded else None, "repeat_agreement": len(graded) == 2 and graded[0]["grade"]["classification"] == graded[1]["grade"]["classification"]}
    severity = {level: {"passed": 0, "failed": 0} for level in ("critical", "major", "minor")}
    for item in substantive:
        for observation in item["grade"]["observations"]:
            severity[observation["severity"]]["passed" if observation["passed"] else "failed"] += 1
    families = {}
    for family in sorted({row["family"] for row in trials}):
        keys = [key for key in forms if key.startswith(family + "/")]
        families[family] = {"forms": len(keys), "intended": sum(item["family"] == family for item in trials), "substantively_graded": sum(item["family"] == family and item["substantively_graded"] for item in trials), "form_pass_rates": [forms[key]["pass_rate"] for key in keys], "descriptive_range": [min(forms[key]["pass_rate"] for key in keys if forms[key]["pass_rate"] is not None), max(forms[key]["pass_rate"] for key in keys if forms[key]["pass_rate"] is not None)] if any(forms[key]["pass_rate"] is not None for key in keys) else None}
    return {"schema_version": "0.2.0", "report_id": "repeated-task-family-matrix-v2", "protocol": {"path": PROTOCOL.relative_to(ROOT).as_posix(), "sha256": sha(PROTOCOL)}, "denominators": denominators, "substantive_outcome": {"passes": passes, "denominator": len(substantive), "rate": passes / len(substantive) if substantive else None, "wilson_95_descriptive": wilson(passes, len(substantive))}, "severity_outcomes": severity, "within_form": forms, "between_family_descriptive": families, "attempt_rows": trials, "confidence_channel": {"status": "insufficient_evidence" if not any(item.get("confidence_channel", {}).get("status") == "available" for item in trials) else "mixed", "available": sum(item.get("confidence_channel", {}).get("status") == "available" for item in trials), "denominator": len(trials)}, "claim_boundaries": protocol["claim_boundaries"], "interpretation": "Internal controlled-vocabulary synthetic evidence only. Small purposive clustered forms prohibit skill, professional/expert validity, general capability, safety, production, readiness, confidence-policy, or population transport claims."}


def execute() -> dict:
    gate = preflight(True)
    if not gate["passed"]:
        blocker = {"status": "blocked_before_model_calls", "gate_report": str((PREFLIGHT / "gate-report.json").relative_to(ROOT)), "failed_gates": gate, "model_calls": 0}
        dump(HERE / "feasibility-report.json", blocker)
        return blocker
    if EXEC.exists():
        raise FileExistsError("execution exists; retries or replacements forbidden")
    EXEC.mkdir()
    protocol = load(PROTOCOL)
    for row in protocol["schedule"]["rows"]:
        run_attempt(protocol, row)
    report = build_report(protocol)
    dump(EXEC / "study-report.json", report)
    return report


def replay() -> dict:
    protocol = load(PROTOCOL)
    rebuilt = build_report(protocol)
    if rebuilt != load(EXEC / "study-report.json"):
        raise ValueError("replay mismatch")
    return rebuilt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["preflight", "execute", "replay"])
    parser.add_argument("--require-pushed", action="store_true")
    args = parser.parse_args()
    result = preflight(args.require_pushed) if args.mode == "preflight" else execute() if args.mode == "execute" else replay()
    print(json.dumps({"mode": args.mode, "passed": result.get("passed", result.get("status") != "blocked_before_model_calls"), "denominators": result.get("denominators"), "status": result.get("status", "verified")}, indent=2))
    return 0 if result.get("passed", result.get("status") != "blocked_before_model_calls") else 1


if __name__ == "__main__":
    raise SystemExit(main())
