import copy, hashlib, importlib.util, json, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
v1=load(ROOT/"pilots/provenance-observation-derivation/adapter.py","heldout_v1")
v11=load(HERE/"adapter_v1_1.py","heldout_v11")
def replay(write=True):
 manifest=json.loads((HERE/"frozen/manifest.json").read_text()); criteria=v1._load(manifest["criteria"],ROOT); policy=v1._load(manifest["policy"],ROOT); oracle=json.loads((HERE/"oracle-private/expected.json").read_text())
 rows=[]; relation_errors=decision_errors=0
 for case in manifest["cases"]:
  old=v1.derive(case,criteria[case["shape"]],ROOT); old_decision=v1.decide(old)
  primary=v11.derive(case,criteria[case["shape"]],ROOT,policy)
  blind={k:v for k,v in case.items() if k not in {"case_id","shape"}}
  second=v11.derive(blind,list(reversed(criteria[case["shape"]])),ROOT,policy)
  rel=lambda o:{(x["predicate"],x["source_pointer"],x["observed_pointer"]):x["relation"] for x in o["comparisons"]}
  a,b=rel(primary),rel(second); disagreements=sum(a.get(k)!=v for k,v in b.items())+sum(k not in b for k in a)
  decision=v11.decide(primary); relation_errors+=disagreements; decision_errors+=decision!=oracle[case["case_id"]]
  rows.append({"case_id":case["case_id"],"v1_frozen_decision":old_decision,"v1_1_decision":decision,"expected_decision":oracle[case["case_id"]],"relation_disagreements":disagreements})
 base=manifest["cases"][0]; mutations={}
 def reject(name,case,crit=None):
  try: v11.derive(case,crit or criteria["lh"],ROOT,policy); mutations[name]=False
  except (ValueError,TypeError): mutations[name]=True
 bad=copy.deepcopy(base); bad["observed"]["sha256"]="0"*64; reject("hash_mismatch",bad)
 bad=copy.deepcopy(base); bad["observed"]["path"]="../escape.json"; reject("path_escape",bad)
 bad=copy.deepcopy(base); bad["oracle"]="pass"; reject("forbidden_leakage",bad)
 badc=copy.deepcopy(criteria["lh"]); badc[0]["source_pointer"]="/absent"; reject("source_pointer_mismatch",base,badc)
 badc=copy.deepcopy(criteria["lh"]); badc[0]["observed_pointer"]="/absent"; mutations["missing_evidence"]=v11.decide(v11.derive(base,badc,ROOT,policy))=="insufficient_evidence"
 badc=copy.deepcopy(criteria["vendor"]); badc[0]["operator"]="set_equal"; badc[0]["observed_pointer"]="/incident_id"; reject("representation_mismatch",manifest["cases"][1],badc)
 # Set order perturbation against temporary, hash-pinned copies.
 vc=manifest["cases"][1]
 with tempfile.TemporaryDirectory(dir=ROOT) as td:
  p=Path(td)/"o.json"; obj=json.loads((ROOT/vc["observed"]["path"]).read_text()); obj["authorized_actions"].reverse(); obj["blocked_actions"].reverse(); p.write_text(json.dumps(obj))
  altered=copy.deepcopy(vc); altered["observed"]={"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
  mutations["order_perturbation"]=v11.decide(v11.derive(altered,criteria["vendor"],ROOT,policy))=="pass"
 gates={"v1_failure_preserved":all(r["v1_frozen_decision"]=="invalid_artifact_or_environment" for r in rows),"zero_relation_errors":relation_errors==0,"zero_decision_errors":decision_errors==0,"all_mutations":all(mutations.values()),"source_artifacts_predate_task":all(c["authoritative"]["committed_at"]<manifest["task_created_at"] and c["observed"]["committed_at"]<manifest["task_created_at"] for c in manifest["cases"]),"claim_boundaries_false":not any(manifest["claim_boundaries"].values())}
 report={"decision":"qualified_for_exact_heldout_artifacts_only" if all(gates.values()) else "rejected","frozen_v1_failure":"environment was hard-required despite declared not-applicable policy","extension":"generic adapter v1.1; one replay","relation_level":{"errors":relation_errors},"decision_level":{"errors":decision_errors},"gates":gates,"mutations":mutations,"cases":rows,"claim_boundaries":manifest["claim_boundaries"]}
 if write: (HERE/"replay-report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
 return report
if __name__=="__main__": print(json.dumps(replay(),indent=2))
