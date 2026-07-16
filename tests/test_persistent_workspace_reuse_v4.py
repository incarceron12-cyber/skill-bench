import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];V4=ROOT/"pilots/persistent-workspace-reuse/v4"
def load(p):return json.loads(p.read_text())
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class PersistentWorkspaceReuseV4Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.r=module(V4/"run_study.py","workspace_v4");cls.p=load(V4/"protocol.json")
 def test_frozen_unseen_matrix_and_prior_preservation(self):
  v=self.r.verify(False);self.assertTrue(v["passed"],v["errors"]);self.assertEqual(24,len(self.p["cells"]));self.assertEqual(24,self.p["strict_denominator"]["intended"])
  self.assertEqual({"structured_change_record":2,"structured_budget_ledger":2},{s:sum(f["shape"]==s for f in self.p["forms"].values()) for s in ("structured_change_record","structured_budget_ledger")})
 def test_only_retained_state_varies_within_form(self):
  for fid in self.p["forms"]:
   values=[{k:v for k,v in c["visible"].items() if k!="retained_state"} for c in self.p["cells"] if c["form_id"]==fid]
   self.assertTrue(all(x==values[0] for x in values))
 def test_public_schema_and_canonical_alternative_serialization(self):
  for cell in self.p["cells"]:
   out=self.r.grader.canonical_output(cell);self.assertEqual("pass",self.r.grader.grade_value(out,cell["private_contract"])["classification"])
   alt={k:out[k] for k in reversed(list(out))};alt["event_log"]=[{k:e[k] for k in reversed(list(e))} for e in out["event_log"]]
   self.assertEqual("pass",self.r.grader.grade_value(alt,cell["private_contract"])["classification"])
 def test_interface_and_leakage_mutations(self):
  r=self.r.mutation_canaries(self.p);self.assertTrue(r["passed"],r)
  required={"task_label_leakage","prompt_label_leakage","alternate_event_key","string_recovery","late_abstention","wrong_parameter","denominator_drift","old_form_reuse","canonical_output","alternative_serialization"}
  self.assertTrue(required.issubset({c["case_id"] for c in r["cases"]}))
 def test_preflight_when_present_is_zero_call(self):
  path=V4/"preflight/gate-report.json"
  if path.exists():
   r=load(path);self.assertTrue(r["passed"],r);self.assertEqual(0,r["model_calls"]);self.assertTrue(all(x["passed"] for x in r["isolation"]))
if __name__=="__main__":unittest.main()
