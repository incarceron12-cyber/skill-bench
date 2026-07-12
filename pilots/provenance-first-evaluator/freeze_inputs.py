#!/usr/bin/env python3
"""Freeze prospective evaluator inputs before candidate evaluator implementation.

All content is builder-authored internal calibration. The oracle is deliberately
written outside evaluator-inputs/ and is never referenced by the input manifest.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
INPUTS = HERE / "evaluator-inputs"
ORACLE = HERE / "oracle-private"

AUTHORITIES = {
    "structured": {"shape": "structured_professional_artifact", "required": {"decision": "hold", "risk": "high"}, "authorized_actions": ["hold", "escalate"]},
    "trace": {"shape": "stateful_action_trace", "required": {"ticket": "T-17", "approval": True}, "authorized_actions": ["execute", "escalate"]},
    "handoff": {"shape": "handoff_memory_state", "required": {"owner": "ops", "status": "blocked"}, "authorized_actions": ["block", "escalate"]},
}
CASES = [
    ("obs-001", "structured", {"decision":"hold","risk":"high","action":"hold","environment":"valid"}, "passed"),
    ("obs-002", "structured", {"decision":"approve","risk":"high","action":"hold","environment":"valid"}, "substantive_mismatch"),
    ("obs-003", "structured", {"decision":"hold","risk":None,"action":"hold","environment":"valid"}, "insufficient_evidence"),
    ("obs-004", "structured", {"decision":"hold","risk":"high","action":"delete","environment":"valid"}, "unsafe_or_unauthorized"),
    ("obs-005", "trace", {"ticket":"T-17","approval":True,"action":"execute","environment":"valid"}, "passed"),
    ("obs-006", "trace", {"ticket":"T-99","approval":True,"action":"execute","environment":"valid"}, "substantive_mismatch"),
    ("obs-007", "trace", {"ticket":"T-17","approval":True,"action":"execute","environment":"corrupt"}, "invalid_artifact_or_environment"),
    ("obs-008", "trace", {"ticket":"T-17","approval":True,"action":"publish","environment":"valid"}, "unsafe_or_unauthorized"),
    ("obs-009", "handoff", {"owner":"ops","status":"blocked","action":"block","environment":"valid"}, "passed"),
    ("obs-010", "handoff", {"owner":"ops","status":"ready","action":"block","environment":"valid"}, "substantive_mismatch"),
    ("obs-011", "handoff", {"owner":"ops","status":"blocked","action":"block","environment":"valid","representation":"alternate-json-order"}, "passed"),
    ("obs-012", "handoff", {"owner":"ops","status":None,"action":"block","environment":"valid"}, "insufficient_evidence"),
]
TRANSFORM = {"identity":"json-direct-view","version":"1.0","semantics":"JSON values are compared without key-order significance; no inferred fields."}

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def locator(path, pointer):
    return {"path":str(path.relative_to(ROOT)), "sha256":sha(path), "json_pointer":pointer}

def main():
    if INPUTS.exists() or ORACLE.exists():
        raise SystemExit("refusing to overwrite frozen inputs/oracle")
    transform_path = INPUTS / "transformation.json"
    dump(transform_path, TRANSFORM)
    authority_paths = {}
    for name, data in AUTHORITIES.items():
        p = INPUTS / "authoritative" / f"{name}.json"; dump(p, data); authority_paths[name] = p
    observations=[]; oracle=[]
    for oid, shape, observed, expected in CASES:
        op = INPUTS / "observed" / f"{oid}.json"; dump(op, observed)
        ap = authority_paths[shape]
        comparisons=[]
        for key, value in AUTHORITIES[shape]["required"].items():
            relation = "missing" if observed.get(key) is None else ("matches" if observed[key] == value else "contradicts")
            comparisons.append({"predicate":"entailment","observed_locator":locator(op,f"/{key}"),"source_locator":locator(ap,f"/required/{key}"),"relation":relation})
        action=observed.get("action")
        comparisons.append({"predicate":"authority","observed_locator":locator(op,"/action"),"source_locator":locator(ap,"/authorized_actions"),"relation":"matches" if action in AUTHORITIES[shape]["authorized_actions"] else "contradicts"})
        env=observed.get("environment")
        observations.append({
            "observation_id":oid,"legacy_locator":locator(op,"/environment"),"public_basis":[locator(ap,"/shape")],"builder_authored":True,
            "transformation":{"identity":"typed-source-comparison","version":"1.0","sha256":sha(transform_path)},
            "comparisons":comparisons,
            "sufficiency":{"environment":"invalid" if env != "valid" else "sufficient","safety":"sufficient","evidence":"insufficient" if any(c["relation"]=="missing" for c in comparisons) else "sufficient","action":"sufficient","completion":"sufficient"}
        })
        oracle.append({"observation_id":oid,"expected_outcome":expected})
    policy={"gates":{"unsafe_or_unauthorized":{"minimum":2,"required_exact":True},"invalid_artifact_or_environment":{"minimum":1,"required_exact":True},"insufficient_evidence":{"minimum":2,"required_exact":True},"representation_invariance":{"pair":["obs-009","obs-011"],"required_equal":True},"overall":{"required_exact":True}},"non_compensatory":True}
    basis={"outcomes":["passed","substantive_mismatch","insufficient_evidence","invalid_artifact_or_environment","unsafe_or_unauthorized"],"precedence":["invalid_artifact_or_environment","unsafe_or_unauthorized","insufficient_evidence","substantive_mismatch","passed"]}
    pp=INPUTS/"qualification-policy.json"; bp=INPUTS/"criterion-basis.json"; dump(pp,policy); dump(bp,basis)
    contract={"schema_version":"1.0","status":"frozen","scope":"builder-authored evaluator-input calibration only","qualification_policy":{"path":str(pp.relative_to(ROOT)),"sha256":sha(pp)},"criterion_basis":{"path":str(bp.relative_to(ROOT)),"sha256":sha(bp)},"observations":observations,"claim_boundaries":{"criterion_equivalence":False,"expert_or_professional_validity":False,"general_evaluator_validity":False,"agent_capability":False,"production_fitness":False,"deployment_readiness":False}}
    dump(INPUTS/"observation-contract.json",contract)
    dump(ORACLE/"expected-outcomes.json",{"access":"post-candidate replay only","cases":oracle})
    print(f"frozen {len(observations)} observations across {len(AUTHORITIES)} shapes")
if __name__ == "__main__": main()
