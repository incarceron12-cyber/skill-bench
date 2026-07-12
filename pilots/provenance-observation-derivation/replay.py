import copy, hashlib, json, tempfile
from pathlib import Path
import adapter
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent

def replay(write=True):
 manifest=json.loads((HERE/"frozen/manifest.json").read_text())
 criteria_doc=adapter._load(manifest["criteria"],ROOT)
 oracle=json.loads((HERE/"oracle-private/expected.json").read_text())
 rows=[]; relation_errors=0; decision_errors=0
 for case in manifest["cases"]:
  primary=adapter.derive(case,criteria_doc[case["shape"]],ROOT)
  blind={k:v for k,v in case.items() if k not in {"case_id","shape"}}
  second=adapter.derive(blind,list(reversed(criteria_doc[case["shape"]])),ROOT)
  p_rel={(x["predicate"],x["source_pointer"],x["observed_pointer"]):x["relation"] for x in primary["comparisons"]}
  s_rel={(x["predicate"],x["source_pointer"],x["observed_pointer"]):x["relation"] for x in second["comparisons"]}
  disagreements=sum(p_rel.get(k)!=v for k,v in s_rel.items())+sum(k not in s_rel for k in p_rel)
  relation_errors+=disagreements
  decision=adapter.decide(primary); expected=oracle[case["case_id"]]
  decision_errors+=decision!=expected
  rows.append({"case_id":case["case_id"],"relation_disagreements":disagreements,"derived_decision":decision,"expected_decision":expected})
 # Representation/order metamorphics: JSON object order and declared set order must not alter relations.
 base=manifest["cases"][0]; original=adapter.derive(base,criteria_doc["record"],ROOT)
 with tempfile.TemporaryDirectory(dir=ROOT) as td:
  tmp=Path(td); source=json.loads((ROOT/base["authoritative"]["path"]).read_text()); observed=json.loads((ROOT/base["observed"]["path"]).read_text())
  source={k:source[k] for k in reversed(source)}; observed={k:observed[k] for k in reversed(observed)}; observed["tags"]=list(reversed(observed["tags"]))
  sp=tmp/"s.json"; op=tmp/"o.json"; sp.write_text(json.dumps(source)); op.write_text(json.dumps(observed))
  loc=lambda p:{"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
  altered={"authoritative":loc(sp),"observed":loc(op)}
  metamorphic=adapter.derive(altered,criteria_doc["record"],ROOT)==original
 # Explicit fail-closed mutation probes.
 mutations={}
 def rejected(name,case,criteria=criteria_doc["record"]):
  try: adapter.derive(case,criteria,ROOT); mutations[name]=False
  except ValueError: mutations[name]=True
 bad=copy.deepcopy(base); bad["observed"]["sha256"]="0"*64; rejected("hash_mismatch",bad)
 bad=copy.deepcopy(base); bad["observed"]["path"]="../outside.json"; rejected("path_escape",bad)
 badcriteria=copy.deepcopy(criteria_doc["record"]); badcriteria[0]["observed_pointer"]="/absent"; missing=adapter.derive(base,badcriteria,ROOT); mutations["missing_evidence"]=adapter.decide(missing)=="insufficient_evidence"
 badcriteria=copy.deepcopy(criteria_doc["record"]); badcriteria[0]["source_pointer"]="/absent"; rejected("source_pointer_mismatch",base,badcriteria)
 bad=copy.deepcopy(base); bad["expected_outcome"]="pass"; rejected("leakage_field",bad)
 mutations["authority_conflict"]=rows[3]["derived_decision"]=="unsafe_or_unauthorized"
 mutations["invalid_environment"]=rows[6]["derived_decision"]=="invalid_artifact_or_environment"
 mutations["alternate_representation"]=rows[7]["derived_decision"]=="pass"
 gates={"zero_relation_disagreements":relation_errors==0,"zero_final_decision_errors":decision_errors==0,"metamorphic_invariance":metamorphic,"all_mutations":all(mutations.values()),"claim_boundaries_false":not any(manifest["claim_boundaries"].values())}
 report={"decision":"qualified_for_exact_internal_fixture_only" if all(gates.values()) else "rejected","relation_level":{"errors":relation_errors},"final_decision_level":{"errors":decision_errors},"gates":gates,"mutations":mutations,"cases":rows,"claim_boundaries":manifest["claim_boundaries"]}
 if write: (HERE/"replay-report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
 return report
if __name__=="__main__": print(json.dumps(replay(),indent=2))
