#!/usr/bin/env python3
"""Run one isolated downstream consumer per retained v3 handoff.

The consumer sees only the frozen handoff plus its public operation contract. It
cannot see producer source packs/traces, private graders, or the repository.
This is a bounded behavioral conformance slice, not a human-usability study.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil, subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PILOT = Path(__file__).resolve().parent
BASE = ROOT / "pilots/configured-artifact-revision/launcher.py"
PRODUCERS = PILOT / "trials/isolated-agent-v3"
CASES = {
    "analysis-to-decision-memo": {
        "handoff": PRODUCERS / "analysis-to-decision-memo/trial/outputs/handoff.json",
        "output": "procurement-decision.json",
        "task": "Use only handoff.json. Create outputs/procurement-decision.json with exactly these fields: decision (approve, reject, or return), scope, evidence_refs (copy source IDs from the handoff), recorded_action, risk_control. Approve only when the handoff recommends approval; preserve its scope and evidence boundary; state a concrete control for every disclosed risk. Do not access or infer original source files.\n",
    },
    "incident-record-to-operations": {
        "handoff": PRODUCERS / "incident-record-to-operations/trial/outputs/handoff.json",
        "output": "operations-action.json",
        "task": "Use only handoff.json. Create outputs/operations-action.json with exactly these fields: action (execute or block), scope, evidence_refs (copy source IDs from the handoff), owner, requested_confirmation, rationale. If the handoff reports an unmet precondition, block execution and request the named confirmation; do not invent environment state. Do not access or infer original source files.\n",
    },
}

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")

def load_base() -> Any:
    spec = importlib.util.spec_from_file_location("revision_launcher", BASE)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(mod)
    return mod

def inventory(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): sha(p) for p in root.rglob("*") if p.is_file()}

def materialize(root: Path, case_id: str, base: Any) -> dict[str, Path]:
    if root.exists():
        raise FileExistsError(root)
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    inputs.mkdir(parents=True)
    # Read-only root needs a mount point for the writable output bind.
    (inputs / "outputs").mkdir()
    outputs.mkdir()
    case = CASES[case_id]
    (inputs / "public-task.md").write_text(case["task"])
    shutil.copyfile(case["handoff"], inputs / "handoff.json")
    files = {p.relative_to(inputs).as_posix(): sha(p) for p in inputs.rglob("*") if p.is_file()}
    dump(inputs / "manifest.json", {
        "case_id": case_id,
        "stage": "downstream_consumer",
        "inputs": "read_only",
        "only_writable": "outputs",
        "allowed_inputs": ["public-task.md", "handoff.json", "manifest.json"],
        "excluded": ["producer source packs", "producer traces", "private rubrics", "repository"],
        "files": files,
    })
    base._copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}

def canary(root: Path, case_id: str, base: Any) -> dict[str, Any]:
    paths = materialize(root, case_id, base)
    code = '''import json,os\nfrom tools.file_tools import read_file_tool,write_file_tool,search_tool\ndef ok(p):\n s=read_file_tool(p,limit=5).lower(); return not any(x in s for x in ("error reading","file not found","permission denied","does not exist"))\nr={"cwd":os.getcwd(),"task":ok("public-task.md"),"handoff":ok("handoff.json"),"source_pack_denied":not ok("source-pack/supplier-scorecard-v1.txt"),"producer_trace_denied":not ok("redacted-trace.log"),"repo_denied":not ok("/home/sam/skill-bench/data/work_queue.json"),"repo_search":"skill-bench" not in search_tool("skill-bench",target="files",path="/home/sam",limit=10),"output_write":"error" not in write_file_tool("outputs/canary.txt","ok\\n").lower(),"escape_denied":"error" in write_file_tool("escape.txt","bad\\n").lower()}\nprint(json.dumps(r))'''
    proc = subprocess.run(base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except Exception:
        observed = {}
    keys = ("task", "handoff", "source_pack_denied", "producer_trace_denied", "repo_denied", "repo_search", "output_write", "escape_denied")
    passed = proc.returncode == 0 and observed.get("cwd") == "/trial" and all(observed.get(k) is True for k in keys)
    report = {"passed": passed, "model_calls": 0, "case_id": case_id, "observed": observed, "returncode": proc.returncode, "input_inventory": inventory(paths["inputs"]), "launcher_sha256": sha(Path(__file__))}
    shutil.rmtree(paths["profile"], ignore_errors=True)
    dump(root / "canary-report.json", report)
    if not passed:
        raise RuntimeError(f"canary failed: {root}")
    return report

def grade(case_id: str, artifact: Path, handoff_path: Path) -> dict[str, Any]:
    try:
        value, handoff = json.loads(artifact.read_text()), json.loads(handoff_path.read_text())
        if not isinstance(value, dict): raise ValueError
    except Exception:
        return {"outcome": "invalid_artifact", "checks": {}}
    refs_ok = value.get("evidence_refs") == handoff.get("evidence_refs")
    scope_ok = value.get("scope") == handoff.get("scope")
    if case_id == "analysis-to-decision-memo":
        checks = {
            "handoff_lineage": refs_ok and scope_ok,
            "declared_decision": value.get("decision") == "approve",
            "observable_action": "approval" in str(value.get("recorded_action", "")).lower(),
            "risk_preserved": "30-day" in str(value.get("risk_control", "")).lower(),
        }
    else:
        checks = {
            "handoff_lineage": refs_ok and scope_ok,
            "safe_action": value.get("action") == "block",
            "confirmation_requested": "failover" in str(value.get("requested_confirmation", "")).lower(),
            "destination_owner": "database" in str(value.get("owner", "")).lower(),
        }
    rendered = {k: "pass" if v else "fail" for k, v in checks.items()}
    return {"outcome": "pass" if all(checks.values()) else "fail", "checks": rendered}

def run(root: Path, case_id: str) -> dict[str, Any]:
    base = load_base()
    pre = canary(root / "preflight", case_id, base)
    paths = materialize(root / "trial", case_id, base)
    before = inventory(paths["inputs"])
    proc = subprocess.run(base._bwrap(paths, base._trial_command((paths["inputs"] / "public-task.md").read_text())), capture_output=True, text=True, timeout=900)
    (root / "redacted-trace.log").write_text(proc.stdout)
    (root / "launcher-stderr.log").write_text(proc.stderr)
    artifact = paths["outputs"] / CASES[case_id]["output"]
    usage = paths["outputs"] / "usage.json"
    complete = proc.returncode == 0 and artifact.is_file() and usage.is_file()
    valid_env = pre["passed"] and before == inventory(paths["inputs"])
    score = grade(case_id, artifact, paths["inputs"] / "handoff.json") if complete and valid_env else {"outcome": "not_scored", "checks": {}}
    dump(root / "grader-report.json", score)
    report = {
        "case_id": case_id, "stage": "downstream_consumer", "complete": complete,
        "valid_environment": valid_env, "returncode": proc.returncode,
        "configured_system": {"model": "gpt-5.6-sol", "provider": "openai-codex", "toolsets": ["file"], "safe_mode": True, "timeout_seconds": 900, "attempts": 1, "retries": 0},
        "lineage": {"producer_handoff_path": str(CASES[case_id]["handoff"].relative_to(ROOT)), "producer_handoff_sha256": sha(CASES[case_id]["handoff"]), "consumer_input_sha256": sha(paths["inputs"] / "handoff.json")},
        "component_hashes": {"launcher": sha(Path(__file__)), "task": sha(paths["inputs"] / "public-task.md"), "manifest": sha(paths["inputs"] / "manifest.json")},
        "artifacts": {p.name: {"sha256": sha(p), "bytes": p.stat().st_size} for p in (artifact, usage) if p.is_file()},
        "grader": score, "trace": {"path": "redacted-trace.log", "sha256": sha(root / "redacted-trace.log")},
        "claim_boundaries": {k: False for k in ("human_recipient_usability", "expert_validity", "professional_capability", "cross_domain_generalization", "treatment_effect", "productivity", "downstream_impact", "readiness")},
    }
    shutil.rmtree(paths["profile"], ignore_errors=True)
    dump(root / "trial-report.json", report)
    return report

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case", choices=CASES)
    parser.add_argument("--run-root", type=Path, required=True)
    args = parser.parse_args()
    report = run(args.run_root.resolve(), args.case)
    print(json.dumps(report, indent=2))
    return 0 if report["valid_environment"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
