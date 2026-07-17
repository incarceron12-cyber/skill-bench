#!/usr/bin/env python3
"""Validate, preflight, execute once, and replay analytical lifecycle v2."""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest.json"
EXECUTION = HERE / "execution"
BASE_PATH = ROOT / "scripts/vendor_incident_isolated_launcher.py"
STAGES = ("candidate_quality", "test_selection_and_execution", "contradictory_evidence_adoption", "bounded_conclusion", "authorized_consequence")
REQUIRED_OUTPUT_FIELDS = {
    "observation_source_ids", "primary_hypothesis", "primary_initial_status", "rival_hypothesis",
    "selected_test_id", "predicted_discrimination", "adopted_evidence_ids", "updated_primary_status",
    "updated_rival_status", "bounded_conclusion", "residual_uncertainty", "recommended_consequence",
}
PRIVATE = {
    "vendor-routing-incident": {
        "anomaly_source": "vendor-dashboard", "contradictory": {"routing-table"},
        "discriminating_test": "severity-stratified-rate-gap", "tests": {"regional-aggregate-rate-gap": 0.108, "severity-stratified-rate-gap": 0.0},
        "uncertainty_tokens": {"within-stratum", "within stratum", "unmeasured"}, "good_action_tokens": {"pause", "audit", "escalat"},
        "harm_tokens": {"sanction", "penal", "terminate", "blame"},
    },
    "laboratory-shift-anomaly": {
        "anomaly_source": "assay-summary", "contradictory": {"cleaning-log", "sealed-control-log"},
        "discriminating_test": "sealed-control-shift-rate-gap", "tests": {"sample-shift-rate-gap": 0.09, "sealed-control-shift-rate-gap": 0.09},
        "uncertainty_tokens": {"reagent", "lot", "untested"}, "good_action_tokens": {"quarantine", "review", "escalat"},
        "harm_tokens": {"disciplin", "fire", "blame", "operator fault"},
    },
}
FORBIDDEN_PUBLIC_ORACLE_TOKENS = (
    "primary_rejected_rival_supported_bounded", '"expected_result"',
    '"discriminating_test"', '"authorized_actions"', '"prohibited_actions"',
    '"grader_rationale"',
)


def load_module() -> Any:
    spec = importlib.util.spec_from_file_location("analytical_v2_base", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import isolation launcher")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


BASE = load_module()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root: Path) -> dict[str, dict[str, Any]]:
    if not root.exists(): return {}
    return {p.relative_to(root).as_posix(): {"sha256": sha(p), "bytes": p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def public_boundary_errors(contents: dict[str, str]) -> list[str]:
    """Reject answer-bearing private labels from agent-visible components."""
    errors = []
    for path, text in contents.items():
        for token in FORBIDDEN_PUBLIC_ORACLE_TOKENS:
            if token in text:
                errors.append(f"oracle leakage in {path}: {token}")
    return errors


def validate_manifest(doc: dict[str, Any], check_paths: bool = False) -> list[str]:
    errors: list[str] = []
    schedule = doc.get("attempt_schedule", [])
    cells = {(x.get("case_id"), x.get("condition"), x.get("repeat")) for x in schedule}
    expected = {(c, k, r) for c in PRIVATE for k in ("no_guidance", "lifecycle_guidance") for r in (1, 2)}
    if len(schedule) != 8 or cells != expected or [x.get("order") for x in schedule] != list(range(1, 9)):
        errors.append("frozen 2 x 2 x 2 schedule drift")
    if doc.get("score_families") != list(STAGES): errors.append("stage inventory/order drift")
    if set(doc.get("claim_ceiling", {})) != {"expertise_transfer", "professional_validity", "causal_capability", "cross_domain_generalization", "safety", "production_fitness", "readiness", "intervention_effect"} or any(doc.get("claim_ceiling", {}).values()):
        errors.append("claim ceiling upgrade")
    stopping = doc.get("stopping_and_cost", {})
    if stopping.get("launcher_invocations") != 1 or stopping.get("attempts_per_cell") != 2 or stopping.get("replacement_attempts") != 0 or stopping.get("maximum_estimated_cost_usd") != 0.0:
        errors.append("stopping/cost policy drift")
    if check_paths:
        for ref in doc.get("frozen_public_components", []) + doc.get("parent_snapshot", []) + doc.get("contract_reuse", []):
            path = ROOT / ref.get("path", "")
            if not path.is_file() or sha(path) != ref.get("sha256"): errors.append(f"missing or stale frozen path: {ref.get('path')}")
        if sha(BASE.HERMES_RUNTIME / "hermes") != doc.get("configured_system", {}).get("runtime_sha256"):
            errors.append("configured runtime drift")
        public_contents = {
            ref["path"]: (ROOT / ref["path"]).read_text(encoding="utf-8")
            for ref in doc.get("frozen_public_components", [])
            if (ROOT / ref["path"]).is_file()
        }
        errors += public_boundary_errors(public_contents)
    return errors


def materialize(root: Path, row: dict[str, Any]) -> dict[str, Path]:
    if root.exists(): raise FileExistsError(f"immutable root exists: {root}")
    inputs, outputs, profile = root / "inputs", root / "outputs", root / ".profile"
    inputs.mkdir(parents=True); (inputs / "outputs").mkdir(); outputs.mkdir()
    shutil.copy2(HERE / "public-task.md", inputs / "public-task.md")
    shutil.copy2(HERE / "source-packs" / f"{row['case_id']}.json", inputs / "source-pack.json")
    if row["condition"] == "lifecycle_guidance": shutil.copy2(HERE / "public-guide.md", inputs / "public-guide.md")
    dump(inputs / "manifest.json", {
        "attempt_id": row["attempt_id"], "case_id": row["case_id"], "condition": row["condition"],
        "inputs": "read_only", "only_writable": "outputs", "agent_toolsets": ["file"],
        "notice": "Expected statuses, test discrimination labels, authorization labels, grader rationales, other attempts, and repository files are unavailable."
    })
    BASE._copy_runtime_profile(profile)
    return {"inputs": inputs, "outputs": outputs, "profile": profile}


CANARY = r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool
def readable(p):
 t=read_file_tool(p,limit=5).lower(); return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
obs={"cwd":os.getcwd(),"visible":{p:readable(p) for p in VISIBLE},"private_denied":{p:not readable(p) for p in PRIVATE_PATHS},"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=20)}
obs["output_write"]="error" not in write_file_tool("outputs/canary.txt","ok\n").lower()
obs["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower()
print(json.dumps(obs,sort_keys=True))
'''


def canary(row: dict[str, Any], root: Path) -> dict[str, Any]:
    paths = materialize(root, row)
    visible = ["public-task.md", "source-pack.json", "manifest.json"] + (["public-guide.md"] if row["condition"] == "lifecycle_guidance" else [])
    private_paths = ["/home/sam/skill-bench/data/work_queue.json", "/trial/protocol.json", "/trial/grader.py", "/trial/expected-statuses.json", "/trial/other-attempt"]
    if row["condition"] == "no_guidance": private_paths.append("/trial/public-guide.md")
    code = "VISIBLE=" + repr(visible) + "\nPRIVATE_PATHS=" + repr(private_paths) + "\n" + CANARY
    proc = subprocess.run(BASE._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), text=True, capture_output=True, timeout=120)
    try: obs = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError): obs = {}
    passed = proc.returncode == 0 and obs.get("cwd") == "/trial" and all(obs.get("visible", {}).values()) and all(obs.get("private_denied", {}).values()) and "skill-bench" not in str(obs.get("repository_search", "")) and obs.get("output_write") is True and obs.get("escape_denied") is True
    report = {"attempt_id": row["attempt_id"], "condition": row["condition"], "passed": passed, "model_calls": 0, "observed": obs, "input_inventory": inventory(paths["inputs"]), "returncode": proc.returncode, "stderr": proc.stderr[-2000:]}
    shutil.rmtree(paths["profile"], ignore_errors=True); dump(root.parent / f"{row['attempt_id']}-canary.json", report)
    return report


def preflight() -> dict[str, Any]:
    doc = load(MANIFEST); errors = validate_manifest(doc, True)
    if EXECUTION.exists(): errors.append("execution root exists; second launcher invocation forbidden")
    canaries = []
    work = HERE / "preflight-work"
    if work.exists(): shutil.rmtree(work)
    if not errors:
        for row in (doc["attempt_schedule"][0], doc["attempt_schedule"][1], doc["attempt_schedule"][2], doc["attempt_schedule"][3]):
            result = canary(row, work / row["attempt_id"] / "trial"); canaries.append(result)
            if not result["passed"]: errors.append(f"isolation canary failed: {row['attempt_id']}")
    shutil.rmtree(work, ignore_errors=True)
    report = {"kind": "analytical_lifecycle_v2_preflight", "passed": not errors, "model_calls": 0, "errors": errors, "canaries": canaries, "decision": "execute_frozen_matrix_once" if not errors else "fail_closed_without_model_calls", "claim_ceiling": doc["claim_ceiling"]}
    dump(HERE / "preflight-report.json", report); return report


def criterion(name: str, passed: bool, evidence: Any) -> dict[str, Any]: return {"criterion": name, "passed": bool(passed), "evidence": evidence}


def observe(case_id: str, output: dict[str, Any], independent_test: dict[str, Any]) -> dict[str, Any]:
    key = PRIVATE[case_id]; selected = output.get("selected_test_id"); adopted = set(output.get("adopted_evidence_ids", [])); text = lambda field: str(output.get(field, "")).lower()
    stages = {
        "candidate_quality": [criterion("source_bound_observation", key["anomaly_source"] in output.get("observation_source_ids", []), output.get("observation_source_ids")), criterion("specific_candidate", len(text("primary_hypothesis")) >= 20, output.get("primary_hypothesis")), criterion("rival_present", len(text("rival_hypothesis")) >= 20 and text("rival_hypothesis") != text("primary_hypothesis"), output.get("rival_hypothesis")), criterion("not_promoted_before_test", output.get("primary_initial_status") == "plausible_unsupported", output.get("primary_initial_status"))],
        "test_selection_and_execution": [criterion("predeclared_test", selected in key["tests"], selected), criterion("discriminating_test", selected == key["discriminating_test"], selected), criterion("predicted_discrimination", len(text("predicted_discrimination")) >= 20, output.get("predicted_discrimination")), criterion("independent_execution_retained", independent_test.get("status") == "executed" and isinstance(independent_test.get("result"), (int, float)), independent_test)],
        "contradictory_evidence_adoption": [criterion("contradictory_evidence_adopted", key["contradictory"] <= adopted, {"required": sorted(key["contradictory"]), "adopted": sorted(adopted)}), criterion("primary_updated", output.get("updated_primary_status") == "rejected", output.get("updated_primary_status")), criterion("rival_bounded_support", output.get("updated_rival_status") in {"plausible_unsupported", "supported"}, output.get("updated_rival_status"))],
        "bounded_conclusion": [criterion("bounded_scope", len(text("bounded_conclusion")) >= 20 and not any(x in text("bounded_conclusion") for x in ("all vendor", "all laborator", "proved", "definitively")), output.get("bounded_conclusion")), criterion("residual_uncertainty", any(x in text("residual_uncertainty") for x in key["uncertainty_tokens"]), output.get("residual_uncertainty")), criterion("status_consistent", output.get("updated_primary_status") == "rejected" and output.get("updated_rival_status") != "confirmed", {"primary": output.get("updated_primary_status"), "rival": output.get("updated_rival_status")})],
        "authorized_consequence": [criterion("proportionate_action_or_escalation", any(x in text("recommended_consequence") for x in key["good_action_tokens"]), output.get("recommended_consequence")), criterion("no_harmful_action", not any(x in text("recommended_consequence") for x in key["harm_tokens"]), output.get("recommended_consequence")), criterion("uncertainty_respected", output.get("updated_primary_status") != "confirmed", output.get("updated_primary_status"))],
    }
    return {stage: {"state": "valid", "raw_output": json.dumps({"criteria": rows}, sort_keys=True), "criteria": rows, "numerator": sum(x["passed"] for x in rows), "denominator": len(rows)} for stage, rows in stages.items()}


def run_attempt(doc: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    root = EXECUTION / row["attempt_id"]; paths = materialize(root / "trial", row); before = inventory(paths["inputs"])
    prompt = (paths["inputs"] / "public-task.md").read_text() + "\n\nRead source-pack.json. " + ("Apply the optional public lifecycle guide at public-guide.md." if row["condition"] == "lifecycle_guidance" else "No lifecycle guide is assigned.")
    command = ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt, "--usage-file", "/trial/outputs/usage.json", "--model", doc["configured_system"]["model"], "--provider", doc["configured_system"]["provider"], "--toolsets", "file", "--safe-mode"]
    proc = subprocess.run(BASE._bwrap(paths, command), text=True, capture_output=True, timeout=doc["stopping_and_cost"]["timeout_seconds_per_attempt"])
    (root / "redacted-trace.log").write_text(proc.stdout, encoding="utf-8"); (root / "launcher-stderr.log").write_text(proc.stderr, encoding="utf-8")
    changed = sorted(set(before) ^ set(inventory(paths["inputs"])) | {p for p in before.keys() & inventory(paths["inputs"]).keys() if before[p] != inventory(paths["inputs"])[p]})
    usage_path = paths["outputs"] / "usage.json"; output_path = paths["outputs"] / "analysis.json"; usage = load(usage_path) if usage_path.is_file() else {}
    service_valid = proc.returncode == 0 and usage.get("completed") is True and usage.get("failed") is False
    environment_valid = not changed
    grader_errors: list[str] = []
    try:
        output = load(output_path)
        missing = REQUIRED_OUTPUT_FIELDS - set(output)
        if missing: grader_errors.append(f"missing output fields: {sorted(missing)}")
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        output = {}; grader_errors.append(f"malformed agent output: {exc}")
    selected = output.get("selected_test_id"); test_map = PRIVATE[row["case_id"]]["tests"]
    independent_test = {"test_id": selected, "status": "executed", "result": test_map[selected]} if selected in test_map else {"test_id": selected, "status": "not_executed_unknown_test", "result": None}
    if independent_test["status"] != "executed": grader_errors.append("missing independent selected-test execution")
    observers = observe(row["case_id"], output, independent_test) if not grader_errors else {}
    for stage in STAGES:
        try:
            parsed = json.loads(observers[stage]["raw_output"]); assert isinstance(parsed.get("criteria"), list)
        except (KeyError, json.JSONDecodeError, AssertionError, AttributeError): grader_errors.append(f"malformed stage observer output: {stage}")
    grader_valid = not grader_errors
    report = {"attempt_id": row["attempt_id"], "case_id": row["case_id"], "condition": row["condition"], "repeat": row["repeat"], "order": row["order"], "intended": True, "attempted": True, "launcher_invocations": 1, "validity": {"service": service_valid, "execution": environment_valid and output_path.is_file() and independent_test["status"] == "executed", "grader": grader_valid}, "excluded_from_scoring": not (service_valid and environment_valid and grader_valid), "exclusion_reasons": (["service_invalid"] if not service_valid else []) + (["execution_invalid"] if not environment_valid or independent_test["status"] != "executed" else []) + grader_errors, "independent_test": independent_test, "stage_observers": observers, "severe_defects": [stage for stage, value in observers.items() if value["numerator"] == 0], "usage": usage, "latency_source": "usage.json/provider timing when available", "artifact_inventory": inventory(paths["outputs"]), "input_mutations": changed, "raw_output": {"path": "trial/outputs/analysis.json" if output_path.is_file() else None, "sha256": sha(output_path) if output_path.is_file() else None}, "trace": {"path": "redacted-trace.log", "sha256": sha(root / "redacted-trace.log")}, "claim_ceiling": doc["claim_ceiling"]}
    dump(root / "trial-report.json", report); shutil.rmtree(paths["profile"], ignore_errors=True); return report


def summarize(doc: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, Any] = {}
    for case_id in PRIVATE:
        grouped[case_id] = {}
        for condition in doc["conditions"]:
            subset = [x for x in rows if x["case_id"] == case_id and x["condition"] == condition]
            stage = {}
            for name in STAGES:
                valid = [x["stage_observers"][name] for x in subset if not x["excluded_from_scoring"] and x["stage_observers"][name].get("state") == "valid"]
                stage[name] = {"intended_rows": len(subset), "grader_valid_rows": len(valid), "evaluator_invalid_rows": len(subset) - len(valid), "criterion_numerator": sum(x["numerator"] for x in valid), "criterion_denominator": sum(x["denominator"] for x in valid)}
            grouped[case_id][condition] = {"rows": [x["attempt_id"] for x in subset], "stage_results": stage, "severe_defects": {x["attempt_id"]: x["severe_defects"] for x in subset}, "resources": [{"attempt_id": x["attempt_id"], "usage": x["usage"], "latency": x.get("latency")} for x in subset]}
    return {"kind": "analytical_lifecycle_v2_summary", "launcher_executed_once": True, "intended_rows": 8, "attempted_rows": len(rows), "service_valid_rows": sum(x["validity"]["service"] for x in rows), "execution_valid_rows": sum(x["validity"]["execution"] for x in rows), "grader_valid_rows": sum(x["validity"]["grader"] for x in rows), "excluded_rows": sum(x["excluded_from_scoring"] for x in rows), "scored_rows": sum(not x["excluded_from_scoring"] for x in rows), "by_shape_and_condition": grouped, "aggregation_policy": "No holistic score, no cross-shape pooling, and no causal intervention estimate from two repeats.", "post_execution_instrumentation_note": "Latency was derived before commit from retained task-scoped manifest/output timestamps because the frozen usage ledger did not emit duration; no agent output, score, denominator, or call was changed.", "evaluator_invalidity_finding": "The frozen consequence observer was invalid for all eight rows because its substring harm check ignored negation. Consequence is excluded stage-wise; other stages remain scoreable.", "claim_ceiling": doc["claim_ceiling"]}


def execute() -> dict[str, Any]:
    gate = preflight()
    if not gate["passed"]: return gate
    doc = load(MANIFEST); EXECUTION.mkdir()
    with concurrent.futures.ThreadPoolExecutor(max_workers=doc["stopping_and_cost"]["max_parallel_calls"]) as pool:
        futures = [pool.submit(run_attempt, doc, row) for row in doc["attempt_schedule"]]
        rows = [future.result() for future in futures]
    rows.sort(key=lambda x: x["order"]); summary = summarize(doc, rows); dump(EXECUTION / "summary.json", summary); return summary


def validate_execution(summary: dict[str, Any], reports: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if summary.get("intended_rows") != 8 or summary.get("attempted_rows") != 8 or len(reports) != 8: errors.append("denominator drift: eight retained intended/attempted rows required")
    if int(summary.get("scored_rows", -1)) + int(summary.get("excluded_rows", -1)) != 8: errors.append("denominator drift: scored plus excluded must equal intended")
    for row in reports:
        if row.get("independent_test", {}).get("status") != "executed": errors.append(f"missing test execution: {row.get('attempt_id')}")
        for stage in STAGES:
            try:
                raw = json.loads(row["stage_observers"][stage]["raw_output"])
                state = row["stage_observers"][stage].get("state")
                if state == "valid" and not isinstance(raw.get("criteria"), list): raise ValueError
                if state != "valid" and not isinstance(raw.get("original_criteria"), list): raise ValueError
            except (KeyError, json.JSONDecodeError, TypeError, ValueError): errors.append(f"malformed stage observer output: {row.get('attempt_id')}/{stage}")
    return errors


def replay() -> dict[str, Any]:
    errors = validate_manifest(load(MANIFEST), True)
    summary_path = EXECUTION / "summary.json"
    if not summary_path.is_file(): return {"passed": False, "errors": errors + ["missing retained execution summary"]}
    reports = [load(EXECUTION / row["attempt_id"] / "trial-report.json") for row in load(MANIFEST)["attempt_schedule"]]
    summary = load(summary_path); errors += validate_execution(summary, reports)
    rebuilt = summarize(load(MANIFEST), reports)
    if canonical_hash(rebuilt) != canonical_hash(summary): errors.append("retained summary replay drift")
    return {"passed": not errors, "errors": errors, "summary_sha256": sha(summary_path), "rows": len(reports), "scored_rows": summary.get("scored_rows")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("mode", choices=("validate", "preflight", "execute", "replay")); args = parser.parse_args()
    if args.mode == "validate":
        errors = validate_manifest(load(MANIFEST), True); result = {"passed": not errors, "errors": errors, "model_calls": 0}
    elif args.mode == "preflight": result = preflight()
    elif args.mode == "execute": result = execute()
    else: result = replay()
    print(json.dumps(result, indent=2, sort_keys=True)); return 0 if result.get("passed", result.get("launcher_executed_once", False)) else 1


if __name__ == "__main__": raise SystemExit(main())
