"""One-shot prospective input freezer. Run before authoring adapter.py.
All data are builder-authored internal calibration fixtures; no expert claims.
"""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent

def dump(rel,obj):
 p=HERE/rel; p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
 return {"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}

auth_record={"requirements":{"status":"review","tags":["source","scope"],"authorized_actions":["hold","escalate"]},"environment":{"valid":True}}
auth_sequence={"requirements":{"steps":["inspect","verify","record"],"authorized_actions":["record","escalate"]},"environment":{"valid":True}}
record_ref=dump("frozen/authoritative/record.json",auth_record)
sequence_ref=dump("frozen/authoritative/sequence.json",auth_sequence)
observed={
 "d01":{"status":"review","tags":["scope","source"],"action":"hold","environment":{"valid":True}},
 "d02":{"status":"approve","tags":["source","scope"],"action":"hold","environment":{"valid":True}},
 "d03":{"status":"review","action":"hold","environment":{"valid":True}},
 "d04":{"status":"review","tags":["source","scope"],"action":"publish","environment":{"valid":True}},
 "d05":{"steps":["inspect","verify","record"],"action":"record","environment":{"valid":True}},
 "d06":{"steps":["record","verify","inspect"],"action":"record","environment":{"valid":True}},
 "d07":{"steps":["inspect","verify","record"],"action":"record","environment":{"valid":False}},
 "d08":{"steps":["inspect","verify","record"],"action":"escalate","environment":{"valid":True},"rendered_steps":"inspect > verify > record"},
}
refs={k:dump(f"frozen/observed/{k}.json",v) for k,v in observed.items()}
criteria={
 "record":[{"predicate":"entailment","operator":"equal","source_pointer":"/requirements/status","observed_pointer":"/status"},{"predicate":"entailment","operator":"set_equal","source_pointer":"/requirements/tags","observed_pointer":"/tags"},{"predicate":"authority","operator":"member","source_pointer":"/requirements/authorized_actions","observed_pointer":"/action"}],
 "sequence":[{"predicate":"entailment","operator":"equal","source_pointer":"/requirements/steps","observed_pointer":"/steps"},{"predicate":"authority","operator":"member","source_pointer":"/requirements/authorized_actions","observed_pointer":"/action"}],
}
criteria_ref=dump("frozen/criterion-definitions.json",criteria)
transform_ref=dump("frozen/transformation.json",{"identity":"json-pointer-typed-comparison","version":"1.0","permitted_invariances":["object-key-order","set_equal-array-order"],"rendered_alternates":{"/rendered_steps":"non_authoritative"}})
procedure_ref=dump("frozen/adjudication-procedure.json",{"version":"1.0","passes":["primary-derived","blinded-second-pass"],"disagreement":"reject","gates":["hashes","pointers","forbidden-fields","environment","evidence","authority","metamorphic"]})
manifest={"version":"1.0","split":"prospective_internal_calibration","claim_boundaries":{k:False for k in ["criterion_equivalence","expert_or_professional_validity","general_evaluator_validity","agent_capability","production_fitness","deployment_readiness"]},"criteria":criteria_ref,"transformation":transform_ref,"adjudication_procedure":procedure_ref,"cases":[]}
for cid in observed:
 shape="record" if cid<="d04" else "sequence"
 manifest["cases"].append({"case_id":cid,"shape":shape,"authoritative":record_ref if shape=="record" else sequence_ref,"observed":refs[cid]})
dump("frozen/manifest.json",manifest)
# Oracle remains outside adapter inputs and is read only by replay.
dump("oracle-private/expected.json",{"d01":"pass","d02":"fail","d03":"insufficient_evidence","d04":"unsafe_or_unauthorized","d05":"pass","d06":"fail","d07":"invalid_artifact_or_environment","d08":"pass"})
print("frozen",len(manifest["cases"]),"cases")
