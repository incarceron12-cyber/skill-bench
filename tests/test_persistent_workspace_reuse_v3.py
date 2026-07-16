import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];V3=ROOT/"pilots/persistent-workspace-reuse/v3"
def load(p):return json.loads(p.read_text())
def module():
 spec=importlib.util.spec_from_file_location("workspace_v3",V3/"run_study.py");assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class PersistentWorkspaceReuseV3Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.r=module();cls.p=load(V3/"protocol.json")
 def test_frozen_non_ceiling_matrix_and_prior_preservation(self):
  v=self.r.verify(False);self.assertTrue(v["passed"],v["errors"]);self.assertEqual(24,len(self.p["cells"]));self.assertEqual(24,self.p["strict_denominator"]["intended"])
  self.assertEqual({"structured_change_record":2,"structured_budget_ledger":2},{s:sum(f["shape"]==s for f in self.p["forms"].values()) for s in ("structured_change_record","structured_budget_ledger")})
 def test_only_retained_state_varies_within_form(self):
  for fid in self.p["forms"]:
   cells=[c for c in self.p["cells"] if c["form_id"]==fid];values=[]
   for c in cells:values.append({k:v for k,v in c["visible"].items() if k!="retained_state"})
   self.assertTrue(all(x==values[0] for x in values))
 def test_four_part_contract_discriminates_act_and_withhold(self):
  for cell in self.p["cells"]:
   out=self.r.grader.canonical_output(cell);g=self.r.grader.grade_value(out,cell["private_contract"]);self.assertEqual("pass",g["classification"]);self.assertTrue(all(g["parts"].values()))
  for fid in self.p["forms"]:
   a=next(c for c in self.p["cells"] if c["form_id"]==fid and c["condition"]=="absent");b=next(c for c in self.p["cells"] if c["form_id"]==fid and c["condition"]=="current_authorized")
   self.assertNotEqual(self.r.grader.canonical_output(a)["state"],self.r.grader.canonical_output(b)["state"])
 def test_required_mutation_canaries(self):
  r=self.r.mutation_canaries(self.p);self.assertTrue(r["passed"],r);self.assertEqual({"oracle_leakage","wrong_target","authority_laundering","denominator_drift","artifact_equivalence","late_abstention","missing_recovery","wrong_parameter"},{c["case_id"] for c in r["cases"]})
 def test_stale_conflict_revocation_cannot_be_laundered(self):
  for condition in ("stale","conflicting","revoked"):
   q=copy.deepcopy(self.p);cell=next(c for c in q["cells"] if c["condition"]==condition);cell["private_contract"]["expected_behavior"]="act"
   self.assertTrue(any("authority laundering" in e for e in self.r.semantic_errors(q)))
 def test_preflight_when_present_is_zero_call(self):
  path=V3/"preflight/gate-report.json"
  if path.exists():
   r=load(path);self.assertTrue(r["passed"],r);self.assertEqual(0,r["model_calls"]);self.assertTrue(all(x["passed"] for x in r["isolation"]))
if __name__=="__main__":unittest.main()
