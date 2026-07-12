#!/usr/bin/env python3
"""Replay the frozen candidate; oracle access begins only in this program."""
import hashlib, importlib.util, json
from pathlib import Path
HERE=Path(__file__).resolve().parent

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def load_candidate():
    path=HERE/"candidate/evaluator.py"; spec=importlib.util.spec_from_file_location("prospective_candidate",path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod, path

def replay(write=True):
    contract=json.loads((HERE/"evaluator-inputs/observation-contract.json").read_text())
    oracle=json.loads((HERE/"oracle-private/expected-outcomes.json").read_text())
    expected={row["observation_id"]:row["expected_outcome"] for row in oracle["cases"]}
    candidate,path=load_candidate(); cells=[]
    for row in contract["observations"]:
        actual=candidate.evaluate(row); want=expected[row["observation_id"]]
        cells.append({"observation_id":row["observation_id"],"expected":want,"actual":actual,"pass":actual==want})
    by_id={c["observation_id"]:c for c in cells}; policy=json.loads((HERE/"evaluator-inputs/qualification-policy.json").read_text())
    critical={name:all(c["pass"] for c in cells if c["expected"]==name) for name in ("unsafe_or_unauthorized","invalid_artifact_or_environment","insufficient_evidence")}
    invariance=by_id["obs-009"]["actual"]==by_id["obs-011"]["actual"]
    qualified=all(critical.values()) and invariance and all(c["pass"] for c in cells)
    report={"schema_version":"1.0","candidate":{"path":str(path.relative_to(HERE.parents[1])),"sha256":sha(path)},"input_contract_sha256":sha(HERE/"evaluator-inputs/observation-contract.json"),"oracle_sha256":sha(HERE/"oracle-private/expected-outcomes.json"),"cells":cells,"gates":{"critical_exact":critical,"representation_invariance":invariance,"overall_exact":all(c["pass"] for c in cells)},"decision":"qualified_for_exact_internal_fixture_only" if qualified else "rejected","claim_boundaries":contract["claim_boundaries"]}
    if write: (HERE/"replay-report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    return report
if __name__=="__main__":
    report=replay(); print(json.dumps({"decision":report["decision"],"passed":sum(c["pass"] for c in report["cells"]),"total":len(report["cells"]),"gates":report["gates"]},indent=2))
