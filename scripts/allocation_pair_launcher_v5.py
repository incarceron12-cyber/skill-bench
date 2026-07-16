#!/usr/bin/env python3
"""Freeze, preflight, execute once, and replay the v5 allocation AB pair.

This additive launcher never modifies or reuses v1-v4 evidence.  It binds the
v4 provider-native coordinate identities to the frozen LH task, both parent
rubrics, a task-scoped bubblewrap envelope, immutable attempt IDs/order, state
hashes, artifact/trace/usage inventories, and a fail-closed guide-flow rule.
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
PILOT = ROOT / "pilots/prospective-allocation-telemetry"
V4 = PILOT / "v4"
V5 = PILOT / "v5"
MANIFEST_PATH = V5 / "manifest.json"
PARENT = ROOT / "pilots/cross-pilot-nonceiling-skill-study/v2"
RUNTIME = Path("/home/sam/.hermes/hermes-agent")
PYTHON_RUNTIME = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
ADAPTER = ROOT / "scripts/provider_call_telemetry_v4.py"
ADOPTION_RULE = V5 / "adoption-observation-rule.json"
CLAIMS = ("allocation_effect", "skill_effect", "capability", "cross_domain", "expert_validity", "professional_validity", "safety", "cost_value", "production_fitness", "readiness")
REQUIRED_OUTPUTS = {"evidence-matrix.csv", "recommendation.md", "usage.json", "call-events.jsonl"}


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


coordinates = load_module("allocation_coordinates_v5", ROOT / "scripts/validate_allocation_coordinates.py")
grader = load_module("allocation_parent_grader_v5", PARENT / "calibration/grade_calibration.py")
base = load_module("allocation_base_launcher_v5", ROOT / "pilots/configured-artifact-revision/launcher.py")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def inventory(root: Path, *, exclude_private: bool = False) -> dict[str, dict[str, Any]]:
    result = {}
    if not root.exists():
        return result
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if exclude_private and any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        result[path.relative_to(root).as_posix()] = {"sha256": sha(path), "bytes": path.stat().st_size}
    return result


def validate_manifest(doc: dict[str, Any], *, check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    parent = load(V4 / "manifest.json")
    if doc.get("schema_version") != "0.5.0":
        errors.append("unsupported v5 manifest version")
    for key in ("coordinate_contract_sha256", "configured_system_sha256", "comparison_identity_sha256"):
        if doc.get(key) != parent.get(key):
            errors.append(f"v4 identity drift: {key}")
    expected_schedule = [("alloc-v4-ab-no-skill", "no_skill", 1), ("alloc-v4-ab-public-skill", "public_skill", 2)]
    observed = [(x.get("attempt_id"), x.get("condition"), x.get("within_block_order")) for x in doc.get("attempt_schedule", [])]
    if observed != expected_schedule or any(x.get("attempt_number") != 1 or x.get("replacement_for") is not None for x in doc.get("attempt_schedule", [])):
        errors.append("ordered retain-once AB schedule drift")
    if doc.get("forbidden_attempt_ids") != ["alloc-v4-configured-provider-probe-01"]:
        errors.append("retained v4 probe replay prohibition missing")
    if set(doc.get("claim_ceiling", {})) != set(CLAIMS) or any(doc.get("claim_ceiling", {}).values()):
        errors.append("claim ceiling upgrade")
    roles = {x.get("role") for x in doc.get("frozen_components", [])}
    required_roles = {"v4_manifest", "v4_probe_report", "launcher", "coordinate_adapter", "adoption_rule", "parent_protocol", "public_task", "public_skill", "measurement_source", "ablation_source", "summary_source", "independent_rubric", "shared_rubric", "dual_rubric_grader"}
    if roles != required_roles:
        errors.append("frozen component role set drift")
    for ref in doc.get("frozen_components", []):
        path = ROOT / str(ref.get("path", ""))
        if not coordinates.valid_hash(ref.get("sha256")):
            errors.append(f"invalid component hash: {ref.get('path')}")
        elif check_paths and (not path.is_file() or sha(path) != ref["sha256"]):
            errors.append(f"stale frozen component: {ref.get('path')}")
    rule = load(ADOPTION_RULE)
    if doc.get("adoption_observation_rule_sha256") != sha(ADOPTION_RULE) or rule.get("inference_policy") != "presentation_or_artifact_similarity_never_implies_invocation_or_adoption":
        errors.append("adoption observation rule drift")
    if parent.get("attempt_schedule") != doc.get("parent_attempt_schedule"):
        errors.append("v4 parent schedule not retained exactly")
    return errors


def _copy_profile(destination: Path) -> None:
    base._copy_runtime_profile(destination)


def materialize(root: Path, row: dict[str, Any]) -> dict[str, Path]:
    if root.exists():
        raise FileExistsError(f"immutable attempt root already exists: {root}")
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    (inputs / "sources").mkdir(parents=True)
    (inputs / "outputs").mkdir()
    outputs.mkdir()
    shutil.copy2(PARENT / "lh/public-task.md", inputs / "public-task.md")
    for source in sorted((PARENT / "lh/sources").iterdir()):
        if source.is_file():
            shutil.copy2(source, inputs / "sources" / source.name)
    if row["condition"] == "public_skill":
        shutil.copy2(PARENT / "lh/public-guide.md", inputs / "public-guide.md")
    dump(inputs / "manifest.json", {
        "schema_version": "0.5.0", "attempt_id": row["attempt_id"], "condition": row["condition"],
        "within_block_order": row["within_block_order"], "comparison_identity_sha256": load(MANIFEST_PATH)["comparison_identity_sha256"],
        "inputs": "read_only", "only_writable": "outputs", "agent_toolsets": ["file"], "live_endpoint_tools": [],
        "excluded_roles": ["rubrics", "grader", "protocol", "adoption_rule", "other_attempt", "repository", "v1_v4_evidence"],
    })
    _copy_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


def bwrap(paths: dict[str, Path], command: list[str], env: dict[str, str] | None = None) -> list[str]:
    args = [
        "bwrap", "--die-with-parent", "--new-session", "--unshare-pid", "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin", "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64",
        "--ro-bind", "/etc", "/etc", "--dir", "/run/systemd", "--ro-bind", "/run/systemd/resolve", "/run/systemd/resolve",
        "--dir", "/home", "--dir", "/home/sam", "--dir", "/home/sam/.local", "--dir", "/home/sam/.local/share", "--dir", "/home/sam/.local/share/uv", "--dir", "/home/sam/.local/share/uv/python",
        "--ro-bind", str(PYTHON_RUNTIME), str(PYTHON_RUNTIME), "--dir", "/opt/hermes", "--ro-bind", str(RUNTIME), "/opt/hermes",
        "--dir", "/instrument", "--ro-bind", str(ADAPTER), "/instrument/provider_call_telemetry_v4.py",
        "--bind", str(paths["profile"]), "/run/hermes-profile", "--ro-bind", str(paths["inputs"]), "/trial", "--bind", str(paths["outputs"]), "/trial/outputs",
        "--chdir", "/trial", "--setenv", "HOME", "/home/sam", "--setenv", "HERMES_REAL_HOME", "/home/sam", "--setenv", "HERMES_HOME", "/run/hermes-profile",
        "--setenv", "TERMINAL_CWD", "/trial", "--setenv", "PYTHONPATH", "/opt/hermes", "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
        "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID", "--unsetenv", "HERMES_SESSION_KEY", "--unsetenv", "HERMES_UI_SESSION_ID",
    ]
    for key, value in sorted((env or {}).items()):
        args += ["--setenv", key, value]
    return [*args, "--", *command]


CANARY = r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool
def readable(p):
 t=read_file_tool(p,limit=5).lower(); return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
obs={"cwd":os.getcwd(),"visible":{p:readable(p) for p in VISIBLE},"private_denied":{p:not readable(p) for p in PRIVATE},"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=20)}
obs["output_write"]="error" not in write_file_tool("outputs/canary.txt","ok\n").lower()
obs["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower()
print(json.dumps(obs,sort_keys=True))
'''


def isolation_canary(row: dict[str, Any], root: Path) -> dict[str, Any]:
    paths = materialize(root, row)
    visible = ["public-task.md", "manifest.json", "sources/measurement-evidence.csv", "sources/ablation-evidence.csv", "sources/adoption-summary.md"]
    if row["condition"] == "public_skill":
        visible.append("public-guide.md")
    private = ["/home/sam/skill-bench/data/work_queue.json", "/trial/rubrics/independent.json", "/trial/adoption-observation-rule.json", "/trial/other-attempt"]
    if row["condition"] == "no_skill":
        private.append("/trial/public-guide.md")
    code = "VISIBLE=" + repr(visible) + "\nPRIVATE=" + repr(private) + "\n" + CANARY
    proc = subprocess.run(bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
    try:
        obs = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        obs = {}
    passed = proc.returncode == 0 and obs.get("cwd") == "/trial" and all(obs.get("visible", {}).values()) and all(obs.get("private_denied", {}).values()) and "skill-bench" not in str(obs.get("repository_search", "")) and obs.get("output_write") is True and obs.get("escape_denied") is True
    report = {"attempt_id": row["attempt_id"], "condition": row["condition"], "passed": passed, "model_calls": 0, "observed": obs, "input_inventory": inventory(paths["inputs"]), "returncode": proc.returncode, "stderr": proc.stderr[-2000:]}
    shutil.rmtree(paths["profile"], ignore_errors=True)
    dump(root.parent / f"canary-{row['condition']}.json", report)
    if not passed:
        raise RuntimeError(f"isolation canary failed: {row['condition']}")
    return report


def grade(output_dir: Path) -> dict[str, Any]:
    grades = {}
    for lineage in ("independent", "shared"):
        rubric_path = PARENT / "lh/rubrics" / f"{lineage}.json"
        value = grader.grade_lh(output_dir, load(rubric_path))
        value["rubric_sha256"] = sha(rubric_path)
        grades[lineage] = value
    return {"identical_output_inventory": inventory(output_dir), "grades": grades}


def preflight() -> dict[str, Any]:
    manifest = load(MANIFEST_PATH)
    errors = validate_manifest(manifest, check_paths=True)
    execution = V5 / "execution"
    if execution.exists():
        errors.append("v5 execution root already exists; replay/replacement forbidden")
    probe = load(V4 / "configured-provider-probe/probe-report.json")
    if probe.get("attempt_id") != "alloc-v4-configured-provider-probe-01" or not probe.get("passed") or probe.get("model_calls") != 1:
        errors.append("retained v4 configured-provider probe invalid")
    calibration = grader.run()
    if not calibration.get("passed") or calibration.get("model_calls") != 0:
        errors.append("parent dual-rubric calibration replay failed")
    cost = load(V4 / "configured-provider-probe/outputs/usage.json")
    if cost.get("cost_status") != "included" or cost.get("estimated_cost_usd") != 0.0 or cost.get("completed") is not True or cost.get("failed") is not False:
        errors.append("included-cost/service gate failed")
    canaries = []
    if not errors:
        canary_root = V5 / "preflight-work"
        if canary_root.exists():
            shutil.rmtree(canary_root)
        for row in manifest["attempt_schedule"]:
            canaries.append(isolation_canary(row, canary_root / row["condition"] / "trial"))
        shutil.rmtree(canary_root, ignore_errors=True)
    report = {
        "schema_version": "0.5.0", "kind": "allocation_pair_preflight", "passed": not errors,
        "model_calls": 0, "errors": errors, "gates": {"coordinate": not coordinates.validate_manifest(load(V4 / "manifest.json"), check_paths=True), "isolation": len(canaries) == 2 and all(x["passed"] for x in canaries), "service": not any("service" in x for x in errors), "environment": len(canaries) == 2, "grader": calibration.get("passed") is True, "order": not any("schedule" in x for x in errors), "state": manifest.get("state_policy", {}).get("initial_sha256") == manifest.get("state_policy", {}).get("final_sha256"), "adoption_observability": not any("adoption" in x for x in errors), "included_cost": not any("cost" in x for x in errors)},
        "v4_probe": {"path": "pilots/prospective-allocation-telemetry/v4/configured-provider-probe/probe-report.json", "sha256": sha(V4 / "configured-provider-probe/probe-report.json"), "replayed": False},
        "calibration_replay_sha256": canonical_hash(calibration), "canaries": [{"attempt_id": x["attempt_id"], "condition": x["condition"], "input_inventory": x["input_inventory"]} for x in canaries],
        "decision": "execute_ordered_pair_once" if not errors else "fail_closed_without_model_calls", "claim_ceiling": manifest["claim_ceiling"],
    }
    dump(V5 / "preflight-report.json", report)
    return report


def observe_flow(row: dict[str, Any], trace: Path, outputs: Path) -> dict[str, Any]:
    rule = load(ADOPTION_RULE)
    presentation = {"status": "observed" if row["condition"] == "public_skill" else "not_applicable", "evidence": {"type": "mounted_input", "sha256": sha(PARENT / "lh/public-guide.md")} if row["condition"] == "public_skill" else None}
    invocation = {"status": "unavailable" if row["condition"] == "public_skill" else "not_applicable", "evidence": None, "reason": rule["invocation"]["unavailable_reason"] if row["condition"] == "public_skill" else None}
    adoption = {"status": "not_observed" if row["condition"] == "public_skill" else "not_applicable", "evidence": None, "reason": rule["adoption"]["not_observed_reason"] if row["condition"] == "public_skill" else None}
    return {"presentation": presentation, "invocation": invocation, "adoption": adoption, "artifact_outcome": {"status": "observed" if outputs.exists() else "unavailable", "evidence": {"type": "artifact_inventory", "sha256": canonical_hash(inventory(outputs))} if outputs.exists() else None}, "resources": {"status": "observed" if (outputs / "usage.json").is_file() else "unavailable", "evidence": {"type": "usage_and_native_call_ledgers", "usage_sha256": sha(outputs / "usage.json"), "events_sha256": sha(outputs / "call-events.jsonl")} if (outputs / "usage.json").is_file() and (outputs / "call-events.jsonl").is_file() else None}}


def run_attempt(manifest: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    root = V5 / "execution" / row["attempt_id"]
    paths = materialize(root / "trial", row)
    before = inventory(paths["inputs"])
    prompt = (paths["inputs"] / "public-task.md").read_text(encoding="utf-8")
    prompt += "\n\nA public procedural guide is available at public-guide.md; it is optional guidance." if row["condition"] == "public_skill" else "\n\nNo procedural guide is assigned; complete the disclosed task from supplied inputs."
    env = {
        "SKILL_BENCH_CALL_PHASE": "direct_observe_act", "SKILL_BENCH_ATTEMPT_ID": row["attempt_id"], "SKILL_BENCH_PROVIDER": "openai-codex", "SKILL_BENCH_MODEL": "gpt-5.6-sol",
        "SKILL_BENCH_CONFIGURED_SYSTEM_SHA256": manifest["configured_system_sha256"], "SKILL_BENCH_COORDINATE_CONTRACT_SHA256": manifest["coordinate_contract_sha256"], "SKILL_BENCH_COMPARISON_IDENTITY_SHA256": manifest["comparison_identity_sha256"], "SKILL_BENCH_CALL_EVENT_PATH": "/trial/outputs/call-events.jsonl",
    }
    command = ["/opt/hermes/venv/bin/python", "/instrument/provider_call_telemetry_v4.py", "run-hermes", "--", "-z", prompt, "--usage-file", "/trial/outputs/usage.json", "--model", "gpt-5.6-sol", "--provider", "openai-codex", "--toolsets", "file", "--safe-mode"]
    proc = subprocess.run(bwrap(paths, command, env), capture_output=True, text=True, timeout=900)
    trace = root / "redacted-trace.log"; trace.parent.mkdir(parents=True, exist_ok=True); trace.write_text(proc.stdout, encoding="utf-8")
    (root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    after = inventory(paths["inputs"])
    changed = sorted(set(before) ^ set(after) | {x for x in before.keys() & after.keys() if before[x] != after[x]})
    outputs = inventory(paths["outputs"])
    usage = load(paths["outputs"] / "usage.json") if (paths["outputs"] / "usage.json").is_file() else {}
    events = coordinates.load_jsonl(paths["outputs"] / "call-events.jsonl") if (paths["outputs"] / "call-events.jsonl").is_file() else []
    coordinate_errors = coordinates.validate_events(events, load(V4 / "manifest.json"), attempt_id=row["attempt_id"], aggregate_usage=usage) if events else ["missing native provider-call ledger"]
    complete = proc.returncode == 0 and REQUIRED_OUTPUTS <= set(outputs)
    cost_ok = usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
    service_ok = usage.get("completed") is True and usage.get("failed") is False
    environment_ok = not changed
    dual = grade(paths["outputs"]) if complete and cost_ok and service_ok and environment_ok and not coordinate_errors else None
    if dual is not None:
        dump(root / "dual-rubric-grade.json", dual)
    report = {
        "schema_version": "0.5.0", "kind": "allocation_pair_attempt", "attempt_id": row["attempt_id"], "condition": row["condition"], "within_block_order": row["within_block_order"], "attempt_number": 1, "replacement_for": None, "launcher_invocations": 1,
        "identities": {key: manifest[key] for key in ("coordinate_contract_sha256", "configured_system_sha256", "comparison_identity_sha256")}, "initial_state_sha256": manifest["state_policy"]["initial_sha256"], "final_state_sha256": manifest["state_policy"]["final_sha256"],
        "isolation": {"bubblewrap": True, "input_inventory_before": before, "input_inventory_after": after, "changed_read_only_inputs": changed, "only_writable": "outputs"},
        "returncode": proc.returncode, "validity": {"coordinate": not coordinate_errors, "service": service_ok, "environment": environment_ok, "grader": dual is not None, "included_cost": cost_ok}, "coordinate_errors": coordinate_errors,
        "artifact_inventory": outputs, "usage": usage, "trace": {"path": trace.relative_to(ROOT).as_posix(), "sha256": sha(trace), "policy": "stdout only; no raw credential/session/request capture"}, "module_flow": observe_flow(row, trace, paths["outputs"]),
        "dual_rubric_grade": {"path": (root / "dual-rubric-grade.json").relative_to(ROOT).as_posix(), "sha256": sha(root / "dual-rubric-grade.json")} if dual is not None else None,
        "claim_ceiling": manifest["claim_ceiling"],
    }
    dump(root / "trial-report.json", report)
    shutil.rmtree(paths["profile"], ignore_errors=True)
    if service_ok and not cost_ok:
        raise RuntimeError("included-cost gate failed; stop later calls")
    return report


def execute() -> dict[str, Any]:
    report = preflight()
    if not report["passed"]:
        return report
    manifest = load(MANIFEST_PATH)
    execution = V5 / "execution"
    if execution.exists():
        raise FileExistsError("v5 pair already executed; replay/replacement forbidden")
    execution.mkdir()
    rows = []
    for row in manifest["attempt_schedule"]:
        rows.append(run_attempt(manifest, row))
    pair_errors = []
    event_sets = {}
    for row in manifest["attempt_schedule"]:
        event_path = execution / row["attempt_id"] / "trial/outputs/call-events.jsonl"
        event_sets[row["condition"]] = coordinates.load_jsonl(event_path) if event_path.is_file() else []
    if all(event_sets.values()):
        pair_errors += coordinates.validate_pair(event_sets, load(V4 / "manifest.json"))
    else:
        pair_errors.append("matched pair native event sets incomplete")
    summary = {
        "schema_version": "0.5.0", "kind": "allocation_pair_summary", "pair_executed_once": True, "attempts": [{"attempt_id": x["attempt_id"], "condition": x["condition"], "validity": x["validity"], "module_flow": x["module_flow"], "dual_rubric_grade": x["dual_rubric_grade"]} for x in rows],
        "pair_coordinate_errors": pair_errors, "substantive_pair_valid": not pair_errors and all(all(x["validity"].values()) for x in rows),
        "separate_reporting": ["presentation", "invocation", "adoption", "artifact_outcome", "resources"], "interpretation": "One ordered internal synthetic AB pair. Presentation is not invocation or adoption; no effect, capability, professional, economic-value, production, or readiness claim is licensed.", "claim_ceiling": manifest["claim_ceiling"],
    }
    dump(execution / "pair-summary.json", summary)
    return summary


def replay() -> dict[str, Any]:
    manifest = load(MANIFEST_PATH)
    errors = validate_manifest(manifest, check_paths=True)
    summary_path = V5 / "execution/pair-summary.json"
    if not summary_path.is_file():
        raise FileNotFoundError("no retained v5 pair summary")
    summary = load(summary_path)
    for row in manifest["attempt_schedule"]:
        root = V5 / "execution" / row["attempt_id"]
        trial = load(root / "trial-report.json")
        if trial["attempt_id"] != row["attempt_id"] or trial["condition"] != row["condition"] or trial["within_block_order"] != row["within_block_order"] or trial["launcher_invocations"] != 1:
            errors.append(f"attempt/order/retry drift: {row['attempt_id']}")
        if trial["dual_rubric_grade"]:
            replayed = grade(root / "trial/outputs")
            if canonical_hash(replayed) != canonical_hash(load(root / "dual-rubric-grade.json")):
                errors.append(f"dual rubric replay drift: {row['attempt_id']}")
    return {"passed": not errors, "errors": errors, "summary_sha256": sha(summary_path), "substantive_pair_valid": summary.get("substantive_pair_valid")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("validate", "preflight", "execute", "replay"))
    args = parser.parse_args()
    if args.mode == "validate":
        errors = validate_manifest(load(MANIFEST_PATH), check_paths=True); result = {"passed": not errors, "errors": errors, "model_calls": 0}
    elif args.mode == "preflight":
        result = preflight()
    elif args.mode == "execute":
        result = execute()
    else:
        result = replay()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("passed", result.get("pair_executed_once", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
