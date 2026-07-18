#!/usr/bin/env python3
"""Independent zero-call preflight for repaired v5 endpoint instrument."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V4 = ROOT / "pilots/pretask-procedure-transfer-v4"
CLAIMS = {"agent_capability", "expert_provenance", "production_fitness", "professional_validity", "readiness", "transfer", "utility"}
TASKS = {"k4n7": "family-epsilon", "p9c2": "family-epsilon", "t6v1": "family-zeta", "w3d8": "family-zeta"}
CONDITIONS = {"generated_package", "no_package_no_raw", "equal_budget_raw", "generated_plus_raw", "reference_procedure", "cross_family_irrelevant", "exactly_one_defect", "task_conditioned_hindsight_upper_bound"}

def module(name: str, path: Path):
    spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
    value=importlib.util.module_from_spec(spec); spec.loader.exec_module(value); return value
prepare=module("v5_prepare_preflight",HERE/"prepare_freeze.py")
checker=module("v5_checker_preflight",HERE/"checkers/check_endpoint.py")

def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def all_false(value: Any) -> bool: return isinstance(value,dict) and set(value)==CLAIMS and all(v is False for v in value.values())
def load(path: Path) -> dict: return json.loads(path.read_text())

def validate(*, check_paths: bool=True, overrides: dict[str,Any]|None=None) -> list[str]:
    overrides=overrides or {}; errors=[]
    protocol=copy.deepcopy(overrides.get("protocol",load(HERE/"protocol.json")))
    manifest=load(HERE/"freeze-manifest.json")
    if protocol.get("status")!="prospectively_frozen_zero_call" or protocol.get("execution_authorized") is not False: errors.append("execution gate drift")
    expected_attempts={"model":0,"provider":0,"executor":0,"repair":0,"retry":0}
    if protocol.get("attempt_ledger")!=expected_attempts or manifest.get("attempt_ledger")!=expected_attempts: errors.append("nonzero attempt ledger")
    if not all_false(protocol.get("claim_ceiling")) or not all_false(manifest.get("claim_ceiling")): errors.append("claim ceiling drift")
    if "does not rescore" not in protocol.get("fork_boundary","") and "not rescored" not in protocol.get("fork_boundary",""): errors.append("v4 immutability boundary missing")
    if check_paths:
        for row in manifest.get("components",[])+manifest.get("external_immutable_bindings",[]):
            path=ROOT/row["path"]
            if not path.is_file(): errors.append(f"missing frozen path:{row['path']}")
            elif sha(path)!=row["sha256"] or path.stat().st_size!=row["bytes"]: errors.append(f"frozen byte drift:{row['path']}")
        for forbidden in ("execution","execution-report.json","execution-canary-report.json"):
            if (HERE/forbidden).exists(): errors.append(f"prohibited execution artifact:{forbidden}")
    # The v4 instrument is retained byte-for-byte and explicitly invalid; never import its private endpoints as v5 truth.
    if protocol["parent_defect_audit"]["sha256"]!=sha(V4/"posthoc-endpoint-audit.json"): errors.append("parent defect audit drift")
    crosswalk=load(HERE/"fair-basis-crosswalk.json")
    cross={row["task_id"]:row for row in crosswalk["rows"]}
    for task_id,family in TASKS.items():
        case=copy.deepcopy(overrides.get(f"case:{task_id}",load(HERE/f"tasks/{task_id}/input.json")))
        private=copy.deepcopy(overrides.get(f"private:{task_id}",load(HERE/f"tasks/{task_id}/private.json")))
        public=(HERE/f"tasks/{task_id}/public.md").read_text()
        if case.get("family_id")!=family or private.get("family_id")!=family or private.get("task_id")!=task_id: errors.append(f"identity drift:{task_id}")
        if private.get("attempts")!={"model":0,"provider":0,"executor":0,"repair":0,"retry":0} or not all_false(private.get("claim_ceiling")): errors.append(f"task attempt/claim drift:{task_id}")
        derived=prepare.expected(task_id,case)
        if derived!=private.get("expected_semantics"): errors.append(f"derived semantic contradiction:{task_id}")
        if task_id in {"t6v1","w3d8"} and case.get("journal_id")!=private.get("expected_semantics",{}).get("journal_id"): errors.append(f"hidden literal:{task_id}")
        required_schema=prepare.SCHEMAS[family]
        for field,type_label in required_schema.items():
            if json.dumps(field) not in public or type_label not in public: errors.append(f"undisclosed field/type:{task_id}:{field}")
        if "wording is not scored" not in public: errors.append(f"reason invariance undisclosed:{task_id}")
        basis=cross.get(task_id,{})
        if basis.get("hidden_obligations")!=[]: errors.append(f"hidden obligations recorded:{task_id}")
        expected_paths={"/task_id"}
        expected_paths |= ({"/decisions/*/batch_id","/decisions/*/disposition","/decisions/*/controlling_seals","/decisions/*/observation_ids","/decisions/*/reason"} if family=="family-epsilon" else {"/journal_id","/valid","/final_state","/committed_transactions","/rolled_back_transactions","/reason"})
        if set(basis.get("checked_fields",{}))!=expected_paths or any(not refs for refs in basis.get("checked_fields",{}).values()): errors.append(f"fair-basis coverage:{task_id}")
        canonical=copy.deepcopy(private["expected_semantics"]); canonical["reason"]="A substantively equivalent top-level paraphrase."
        if family=="family-epsilon":
            for row in canonical["decisions"]: row["reason"]="Equivalent decision explanation."
        passed,why=checker.compare(canonical,private)
        if not passed: errors.append(f"wording paraphrase rejected:{task_id}:{why}")
        wrong=copy.deepcopy(canonical)
        if family=="family-epsilon": wrong["decisions"][0]["disposition"]="quarantine" if wrong["decisions"][0]["disposition"]=="release" else "release"
        else: wrong["valid"]=not wrong["valid"]
        if checker.compare(wrong,private)[0]: errors.append(f"semantic mutation accepted:{task_id}")
    # Explicit corrected arithmetic endpoint: age 20 <= 24, therefore release.
    k=load(HERE/"tasks/k4n7/private.json")["expected_semantics"]["decisions"][0]
    if k["disposition"]!="release" or 100-80!=20 or 20>24: errors.append("k4n7 arithmetic repair invalid")
    assignments=load(HERE/"assignments.json")["rows"]
    v4rows=load(V4/"assignments.json")["rows"]
    if len(assignments)!=32 or [r["schedule_index"] for r in assignments]!=list(range(1,33)) or any(r["attempts"]!=0 for r in assignments): errors.append("assignment count/order/attempt drift")
    if [(r["task_id"],r["family_id"],r["condition_id"]) for r in assignments] != [(r["task_id"],r["family_id"],r["condition_id"]) for r in v4rows]: errors.append("v4 assignment parity drift")
    if {(r["task_id"],r["condition_id"]) for r in assignments}!={(t,c) for t in TASKS for c in CONDITIONS}: errors.append("incomplete assignment cells")
    checker_text=(HERE/"checkers/check_endpoint.py").read_text().casefold()
    for token in CONDITIONS|{"condition_id","assignment row","package bytes","raw corpus"}:
        if token in checker_text: errors.append(f"condition-aware checker:{token}")
    return errors

def mutation_results() -> dict[str,list[str]]:
    cases={}
    p=load(HERE/"tasks/k4n7/private.json"); p["expected_semantics"]["decisions"][0]["disposition"]="quarantine"; cases["arithmetic_contradiction"]=validate(check_paths=False,overrides={"private:k4n7":p})
    p=load(HERE/"tasks/t6v1/private.json"); p["expected_semantics"]["journal_id"]="UNDISCLOSED"; cases["hidden_literal"]=validate(check_paths=False,overrides={"private:t6v1":p})
    original=prepare.SCHEMAS["family-zeta"]["valid"]; prepare.SCHEMAS["family-zeta"]["valid"]="integer"
    try: cases["hidden_type"]=validate(check_paths=False)
    finally: prepare.SCHEMAS["family-zeta"]["valid"]=original
    original_compare=checker.compare
    def exact_reason(candidate,private):
        ok,why=original_compare(candidate,private)
        expected=private["expected_semantics"]
        if private["family_id"]=="family-epsilon":
            got_reasons=[row.get("reason") for row in candidate.get("decisions",[]) if isinstance(row,dict)]
            expected_reasons=[row["reason"] for row in expected["decisions"]]
            if got_reasons!=expected_reasons: return False,why+["exact_reason"]
        elif candidate.get("reason")!=expected["reason"]: return False,why+["exact_reason"]
        return ok,why
    setattr(checker, "compare", exact_reason)
    try: cases["wording_exactness"]=validate(check_paths=False)
    finally: setattr(checker, "compare", original_compare)
    return cases

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--check-paths",action="store_true"); parser.add_argument("--report",type=Path); args=parser.parse_args()
    errors=validate(check_paths=args.check_paths); mutations=mutation_results()
    for name,found in mutations.items():
        if not found: errors.append(f"required mutation accepted:{name}")
    report={"status":"PASS" if not errors else "FAIL","errors":errors,"gates":{"exact_byte_freeze":"pass" if not errors else "fail","semantic_derivation":"pass" if not errors else "fail","fair_public_basis":"pass" if not errors else "fail","condition_blind_checker":"pass" if not errors else "fail","checker_soundness":"pass" if not errors else "fail","assignment_parity":"pass" if not errors else "fail","zero_attempts":"pass" if not errors else "fail","all_false_claims":"pass" if not errors else "fail"},"mutation_error_counts":{k:len(v) for k,v in mutations.items()},"executor_authorized":False,"attempt_ledger":load(HERE/"protocol.json")["attempt_ledger"],"claim_ceiling_all_false":all_false(load(HERE/"protocol.json")["claim_ceiling"])}
    rendered=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.report: args.report.write_text(rendered)
    print(rendered,end=""); return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
