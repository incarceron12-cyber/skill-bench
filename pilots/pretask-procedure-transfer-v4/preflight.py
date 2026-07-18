#!/usr/bin/env python3
"""Independent zero-call preflight for pre-task procedure transfer v4."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CLAIMS = {"expert_provenance", "professional_validity", "transfer", "agent_capability", "utility", "production_fitness", "readiness"}
FAMILIES = {"family-epsilon": "epsilon", "family-zeta": "zeta"}
TASKS = {"k4n7": "family-epsilon", "p9c2": "family-epsilon", "t6v1": "family-zeta", "w3d8": "family-zeta"}
CONDITIONS = {"generated_package", "no_package_no_raw", "equal_budget_raw", "generated_plus_raw", "reference_procedure", "cross_family_irrelevant", "exactly_one_defect", "task_conditioned_hindsight_upper_bound"}
FORBIDDEN_CHECKER_TOKENS = CONDITIONS | {"condition_id", "assignment", "package bytes", "raw corpus"}

spec = importlib.util.spec_from_file_location("output_validator", ROOT / "scripts/validate_procedure_generation_output.py")
assert spec and spec.loader
output_validator = importlib.util.module_from_spec(spec); spec.loader.exec_module(output_validator)

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def load(path: Path) -> dict[str, Any]: return json.loads(path.read_text(encoding="utf-8"))
def parse_time(value: str) -> datetime: return datetime.fromisoformat(value.replace("Z", "+00:00"))
def all_false(value: Any) -> bool: return isinstance(value, dict) and set(value) == CLAIMS and all(v is False for v in value.values())
def materials(manifest: dict[str, Any]) -> dict[str, bytes]:
    return {row["path"]: (ROOT / row["path"]).read_bytes() for row in manifest.get("components", []) if (ROOT / row.get("path", "")).is_file()}
def at_pointer(document: dict[str, Any], pointer: str) -> Any:
    value: Any = document
    for token in pointer.lstrip("/").split("/"):
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value
def changed_leaves(left: Any, right: Any, path: str = "") -> list[str]:
    if type(left) is not type(right): return [path or "/"]
    if isinstance(left, dict):
        if set(left) != set(right): return [path or "/"]
        return [item for key in left for item in changed_leaves(left[key], right[key], f"{path}/{key}")]
    if isinstance(left, list):
        if len(left) != len(right): return [path or "/"]
        return [item for index, pair in enumerate(zip(left, right)) for item in changed_leaves(pair[0], pair[1], f"{path}/{index}")]
    return [] if left == right else [path or "/"]

def validate(protocol: dict[str, Any], manifest: dict[str, Any], frozen: dict[str, bytes], *, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    if protocol.get("status") != "prospectively_frozen_zero_call": errors.append("protocol is not at zero-call freeze")
    if not all_false(protocol.get("claim_ceiling")): errors.append("seven-claim ceiling drift")
    expected_attempts = {"intended_generation": 2, "generation": 0, "model": 0, "provider": 0, "executor": 0, "repair": 0, "retry": 0}
    if protocol.get("attempt_ledger") != expected_attempts or manifest.get("attempt_ledger") != expected_attempts: errors.append("nonzero or inconsistent attempt ledger")
    chronology = protocol.get("chronology", {})
    try:
        if not (parse_time(chronology["source_authoring_started_at"]) < parse_time(chronology["all_sources_frozen_at"]) < parse_time(chronology["task_authoring_started_at"]) <= parse_time(chronology["all_tasks_frozen_at"]) < parse_time(chronology["controls_authored_at"]) < parse_time(chronology["protocol_frozen_at"])): errors.append("source/task/control freeze chronology drift")
    except (KeyError, TypeError, ValueError): errors.append("invalid chronology")

    rows = manifest.get("components", []); paths = [row.get("path") for row in rows]
    if len(paths) != len(set(paths)): errors.append("duplicate manifest path")
    required_roles = {"protocol", "source_corpus", "public_task", "private_endpoint", "reference_control", "defective_control", "defect_descriptor", "checker", "assignments", "generation_policy", "interface_import", "prompt_envelope", "contract_schema", "contract_validator", "preflight", "mutation_tests"}
    if not required_roles <= {row.get("role") for row in rows}: errors.append("manifest role inventory incomplete")
    for row in rows:
        data = frozen.get(row.get("path", ""))
        if data is None: errors.append(f"missing frozen component: {row.get('path')}")
        elif sha(data) != row.get("sha256"): errors.append(f"post-freeze byte drift: {row.get('path')}")

    interface = protocol.get("interface_import", {})
    for key in ("guide", "example_source", "example_package"):
        binding = interface.get(key, {}); local = frozen.get(binding.get("path", ""), b"")
        upstream = ROOT / binding.get("upstream_path", "")
        if not upstream.is_file() or local != upstream.read_bytes() or sha(local) != binding.get("sha256"): errors.append(f"interface drift: {key}")
    prompt = interface.get("prompt_envelope", {}); upstream_prompt = ROOT / prompt.get("upstream_path", "")
    if not upstream_prompt.is_file() or sha(upstream_prompt.read_bytes()) != prompt.get("sha256"): errors.append("prompt envelope drift")
    if interface.get("strategy_id") != "guide-plus-unrelated-complete-example-v1": errors.append("interface strategy tuning")

    families = protocol.get("families", [])
    if {row.get("family_id") for row in families} != set(FAMILIES) or len({row.get("structure") for row in families}) != 2: errors.append("family inventory is not two structurally unlike families")
    sources: dict[str, dict[str, Any]] = {}; pids: dict[str, set[str]] = {}
    historical: set[str] = set()
    if check_paths:
        for version in ("pretask-procedure-transfer-v1", "pretask-procedure-transfer-v2", "pretask-procedure-transfer-v3"):
            for path in (ROOT / "pilots" / version).rglob("*"):
                if path.is_file(): historical.add(sha(path.read_bytes()))
    for family in families:
        fid = family["family_id"]; short = FAMILIES[fid]; source_path = family["corpus_path"]
        try: source_bytes = frozen[source_path]; source = json.loads(source_bytes)
        except (KeyError, json.JSONDecodeError): errors.append(f"missing/invalid source: {fid}"); continue
        sources[fid] = source
        if check_paths and sha(source_bytes) in historical: errors.append(f"source reuses v1-v3 exact bytes: {fid}")
        if source.get("family_id") != fid or source.get("family_version") != "1.0.0": errors.append(f"source identity drift: {fid}")
        authority = source.get("authority_scope", {})
        if authority.get("authority") != "builder-authored internal calibration only" or authority.get("origin") != "internal_design_hypothesis" or authority.get("source_url") is not None or not authority.get("scope") or not authority.get("valid_time"): errors.append(f"source authority/scope/time laundering: {fid}")
        ids = {row.get("id") for row in source.get("propositions", [])}; pids[fid] = ids
        if None in ids or len(ids) != len(source.get("propositions", [])): errors.append(f"invalid proposition identity: {fid}")
        for prop in source.get("propositions", []):
            if prop.get("origin") != "internal_design_hypothesis" or prop.get("exact_locator") != f"this file:propositions[{prop.get('id')}]" or not all(prop.get(k) for k in ("authority", "scope", "valid_time")): errors.append(f"untyped proposition provenance: {prop.get('id')}")
            try:
                if parse_time(prop["authored_at"]) >= parse_time(source["frozen_at"]): errors.append(f"proposition authored after source freeze: {prop.get('id')}")
            except (KeyError, TypeError, ValueError): errors.append(f"invalid proposition chronology: {prop.get('id')}")
        for primitive in ("contradictions", "decision_thresholds", "artifact_conventions", "failure_signatures"):
            if not source.get(primitive): errors.append(f"missing primitive {primitive}: {fid}")
        policy_path = f"pilots/pretask-procedure-transfer-v4/generation-policies/{short}.json"; policy = json.loads(frozen.get(policy_path, b"{}"))
        if policy.get("source_corpus_sha256") != sha(source_bytes) or policy.get("allowed_visible_inputs") != ["corpus.json", "interface-guide.md", "example-source.json", "example-package.json"]: errors.append(f"generation source/interface envelope drift: {fid}")
        if set(policy.get("forbidden_tokens", [])) != set(TASKS): errors.append(f"task scrub drift: {fid}")
        ref_path = f"pilots/pretask-procedure-transfer-v4/controls/{short}/reference.json"; defect_path = f"pilots/pretask-procedure-transfer-v4/controls/{short}/defective.json"; desc_path = f"pilots/pretask-procedure-transfer-v4/controls/{short}/defect.json"
        try: ref_bytes=frozen[ref_path]; ref=json.loads(ref_bytes); defect=json.loads(frozen[defect_path]); descriptor=json.loads(frozen[desc_path])
        except (KeyError, json.JSONDecodeError): errors.append(f"missing control: {fid}"); continue
        ref_errors = output_validator.validate_documents(ref, ref_bytes, source, source_bytes, policy)
        if ref_errors: errors.extend(f"invalid source-faithful reference {fid}: {item}" for item in ref_errors)
        changes = changed_leaves(ref, defect); pointer = descriptor.get("json_pointer")
        if descriptor.get("defect_count") != 1 or changes != [pointer] or at_pointer(ref, pointer) != descriptor.get("reference_value") or at_pointer(defect, pointer) != descriptor.get("defective_value") or descriptor.get("source_basis") not in ids: errors.append(f"exactly-one-defect drift: {fid}")

    inventory = protocol.get("task_inventory", [])
    if {row.get("task_id"): row.get("family_id") for row in inventory} != TASKS: errors.append("task inventory drift")
    for row in inventory:
        tid, fid = row.get("task_id"), row.get("family_id"); public_path, private_path = row.get("public_path", ""), row.get("private_path", "")
        try: public_bytes=frozen[public_path]; public=public_bytes.decode(); private=json.loads(frozen[private_path])
        except (KeyError, UnicodeDecodeError, json.JSONDecodeError): errors.append(f"missing/invalid task: {tid}"); continue
        if check_paths and (sha(public_bytes) in historical or sha(frozen[private_path]) in historical): errors.append(f"task reuses v1-v3 exact bytes: {tid}")
        if private.get("task_id") != tid or private.get("family_id") != fid or any(private.get(k) != 0 for k in ("model_attempts", "provider_attempts", "executor_attempts")): errors.append(f"task touched or identity drift: {tid}")
        if not all_false(private.get("claim_ceiling")): errors.append(f"task claim ceiling drift: {tid}")
        for heading in ("## Objective", "## Inputs", "## Deliverable", "## Fair consequence basis"):
            if heading not in public: errors.append(f"public task missing heading: {tid}/{heading}")
        source = sources.get(fid, {})
        for token in source.get("leakage_signatures", []) + [p.get("statement", "") for p in source.get("propositions", [])]:
            if token and token.casefold() in public.casefold(): errors.append(f"complete source procedure leaked into public task: {tid}")
        if any(token in public.casefold() for token in ("expected_endpoint", "private.json", "checker", "condition_id")): errors.append(f"oracle/private exposure in public task: {tid}")
        for check in private.get("checks", []):
            if check.get("public_basis") not in public or not set(check.get("proposition_basis", [])) <= pids.get(fid, set()): errors.append(f"private check lacks exact public/source basis: {tid}/{check.get('id')}")

    conditions = protocol.get("conditions", [])
    if {row.get("condition_id") for row in conditions} != CONDITIONS or any(row.get("resource_envelope_id") != "common-v1" for row in conditions): errors.append("condition inventory or equal envelope drift")
    envelope = protocol.get("equal_envelope", {})
    if set(envelope.get("applies_to_all_conditions", [])) != CONDITIONS or envelope.get("context_budget_tokens") != 8000 or envelope.get("treatment_retrieval_budget_bytes") != 16000 or envelope.get("attempts_per_cell") != 1 or envelope.get("feedback") != "none": errors.append("unequal execution/information envelope")
    if envelope.get("executor") != {"model":"gpt-5.6-sol","provider":"openai-codex","toolsets":["file"],"safe_mode":True,"max_turns":40}: errors.append("executor identity drift")
    assignments = json.loads(frozen.get("pilots/pretask-procedure-transfer-v4/assignments.json", b"{}")); rows = assignments.get("rows", [])
    expected_cells = {(tid, condition) for tid in TASKS for condition in CONDITIONS}
    if {(r.get("task_id"), r.get("condition_id")) for r in rows} != expected_cells or len(rows) != 32 or [r.get("schedule_index") for r in rows] != list(range(1,33)) or any(r.get("attempts") != 0 for r in rows): errors.append("assignment/order/zero-attempt drift")

    checker_path = "pilots/pretask-procedure-transfer-v4/checkers/check_endpoint.py"; checker_text = frozen.get(checker_path, b"").decode("utf-8", errors="replace").casefold()
    for token in FORBIDDEN_CHECKER_TOKENS:
        if token.casefold() in checker_text: errors.append(f"condition-aware checker token: {token}")
    if "expected_endpoint" not in checker_text or "--candidate" not in checker_text or "--private" not in checker_text: errors.append("checker endpoint interface drift")
    visibility = protocol.get("endpoint_separation", {})
    if visibility.get("checker_visibility") != ["candidate final outputs/result.json", "assigned private endpoint record"] or set(visibility.get("checker_denied", [])) != {"condition identity","package bytes","raw corpus","trace","usage","assignment row"}: errors.append("checker visibility separation drift")

    gate = protocol.get("provider_cost_gate", {})
    if gate.get("maximum_estimated_cost_usd_per_attempt") != 0.0 or gate.get("required_cost_status") != "included": errors.append("provider/cost gate drift")
    for path in gate.get("evidence", []):
        try: usage=json.loads(frozen[path])
        except (KeyError, json.JSONDecodeError): errors.append(f"missing provider cost evidence: {path}"); continue
        if not (usage.get("completed") is True and usage.get("failed") is False and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0 and usage.get("model") == gate.get("model") and usage.get("provider") == gate.get("provider")): errors.append(f"provider cost evidence invalid: {path}")

    if check_paths:
        for forbidden in ("generation", "executions", "trials", "hindsight-packages"):
            if (HERE / forbidden).exists(): errors.append(f"prohibited zero-call artifact exists: {forbidden}")
    return errors

def mutation_results(protocol: dict[str, Any], manifest: dict[str, Any], frozen: dict[str, bytes]) -> dict[str, list[str]]:
    cases: dict[str, tuple[dict[str, Any], dict[str, Any], dict[str, bytes]]] = {}
    m=dict(frozen); path="pilots/pretask-procedure-transfer-v4/tasks/k4n7/public.md"; m[path] += b"\nSigned scan outranks an unsigned note.\n"; cases["source_task_leakage"]=(protocol,manifest,m)
    m=dict(frozen); path="pilots/pretask-procedure-transfer-v4/families/epsilon/corpus.json"; m[path] += b" "; cases["post_freeze_edit"]=(protocol,manifest,m)
    m=dict(frozen); path="pilots/pretask-procedure-transfer-v4/interface/interface-guide.md"; m[path] += b"\ntuned\n"; cases["interface_drift"]=(protocol,manifest,m)
    m=dict(frozen); path="pilots/pretask-procedure-transfer-v4/checkers/check_endpoint.py"; m[path] += b"\n# generated_package\n"; cases["condition_aware_grading"]=(protocol,manifest,m)
    m=dict(frozen); path="pilots/pretask-procedure-transfer-v4/controls/epsilon/defect.json"; d=json.loads(m[path]); d["defect_count"]=2; m[path]=json.dumps(d).encode(); cases["defect_drift"]=(protocol,manifest,m)
    p=copy.deepcopy(protocol); p["conditions"][0]["resource_envelope_id"]="larger"; cases["unequal_envelope"]=(p,manifest,frozen)
    m=dict(frozen); path="pilots/pretask-procedure-transfer-v4/tasks/p9c2/public.md"; m[path] += b"\nexpected_endpoint\n"; cases["oracle_exposure"]=(protocol,manifest,m)
    p=copy.deepcopy(protocol); p["attempt_ledger"]["executor"]=1; cases["nonzero_attempt"]=(p,manifest,frozen)
    return {name: validate(p,ma,mo,check_paths=False) for name,(p,ma,mo) in cases.items()}

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--check-paths",action="store_true"); parser.add_argument("--report",type=Path); args=parser.parse_args()
    protocol,manifest=load(HERE/"protocol.json"),load(HERE/"freeze-manifest.json"); frozen=materials(manifest)
    errors=validate(protocol,manifest,frozen,check_paths=args.check_paths); mutations=mutation_results(protocol,manifest,frozen)
    for name,found in mutations.items():
        if not found: errors.append(f"required mutation accepted: {name}")
    report={"status":"PASS" if not errors else "FAIL","errors":errors,"gates":{"provenance_and_chronology":"pass" if not errors else "fail","source_task_separation":"pass" if not errors else "fail","interface_exact_import":"pass" if not errors else "fail","control_and_defect_lineage":"pass" if not errors else "fail","condition_and_envelope_parity":"pass" if not errors else "fail","condition_blind_checker":"pass" if not errors else "fail","exact_byte_freeze":"pass" if not errors else "fail","zero_attempts":"pass" if not errors else "fail"},"mutation_error_counts":{k:len(v) for k,v in mutations.items()},"generation_authorized_after_pushed_commit":not errors,"executor_authorized":False,"attempt_ledger":protocol.get("attempt_ledger"),"claim_ceiling_all_false":all_false(protocol.get("claim_ceiling"))}
    rendered=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.report: args.report.write_text(rendered,encoding="utf-8")
    print(rendered,end=""); return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
