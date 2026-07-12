import copy, hashlib, importlib.util, json, random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent

def load_adapter(path):
 spec=importlib.util.spec_from_file_location("negative_control_adapter",path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def classify(adapter,case,criteria,policy):
 try: return adapter.decide(adapter.derive(case,criteria,ROOT,policy))
 except ValueError as e:
  if str(e)=="source_pointer_mismatch": return "missing_authoritative_evidence"
  if str(e) in {"invalid_representation","invalid_authority_representation"}: return "invalid_artifact_or_environment"
  raise

def replay(write=True):
 frozen=json.loads((HERE/"frozen/cases.json").read_text()); oracle=json.loads((HERE/"oracle-private/expected.json").read_text())
 adapter_path=ROOT/frozen["adapter"]["path"]
 if sha(adapter_path)!=frozen["adapter"]["sha256"]: raise ValueError("adapter_hash_mismatch")
 adapter=load_adapter(adapter_path); rows=[]
 cases=list(reversed(frozen["cases"]))
 for item in cases:
  case={"authoritative":frozen["locators"][item["source"]],"observed":frozen["locators"][item["observed"]]}
  outcome=classify(adapter,case,list(reversed(item["criteria"])),item["policy"])
  rows.append({"control":item["id"],"outcome":outcome,"expected":oracle[item["id"]],"correct":outcome==oracle[item["id"]]})
 # Integrity and blindness probes do not expose oracle/rationale to derive().
 base=frozen["cases"][0]; case={"authoritative":copy.deepcopy(frozen["locators"][base["source"]]),"observed":copy.deepcopy(frozen["locators"][base["observed"]])}
 mutations={}
 def rejected(name,c,crit=None):
  try: adapter.derive(c,crit or base["criteria"],ROOT,base["policy"]); mutations[name]=False
  except (ValueError,TypeError,FileNotFoundError): mutations[name]=True
 bad=copy.deepcopy(case); bad["observed"]["path"]="../escape.json"; rejected("path_escape",bad)
 bad=copy.deepcopy(case); bad["observed"]["sha256"]="0"*64; rejected("hash_mismatch",bad)
 bad=copy.deepcopy(case); bad["oracle"]="pass"; rejected("forbidden_leakage_field",bad)
 badc=copy.deepcopy(base["criteria"]); badc[0]["source_pointer"]="/absent"; rejected("source_pointer_mismatch",case,badc)
 badc=copy.deepcopy(base["criteria"]); badc[0]["observed_pointer"]="/absent"; mutations["observed_pointer_mismatch"]=classify(adapter,case,badc,base["policy"])=="insufficient_evidence"
 serialized=json.dumps(frozen["cases"],sort_keys=True).lower()
 mutations["no_domain_or_shape_identity"]='"domain"' not in serialized and '"shape"' not in serialized and '"family"' not in serialized
 mutations["order_perturbation"]=all(r["correct"] for r in rows)
 gates={"adapter_unchanged":sha(adapter_path)==frozen["adapter"]["sha256"],"all_outcomes_correct":all(r["correct"] for r in rows),"all_mutations_fail_closed":all(mutations.values()),"two_structural_pilots":len({x["source"] for x in frozen["cases"]})>=2,"claim_boundaries_false":not any(frozen["claim_boundaries"].values())}
 report={"decision":"qualified_for_exact_frozen_negative_controls_only" if all(gates.values()) else "rejected","adapter_sha256":sha(adapter_path),"source_commit":frozen["frozen_at_commit"],"controls":sorted(rows,key=lambda x:x["control"]),"mutations":mutations,"gates":gates,"claim_boundaries":frozen["claim_boundaries"]}
 if write: (HERE/"replay-report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
 return report
if __name__=="__main__": print(json.dumps(replay(),indent=2))
