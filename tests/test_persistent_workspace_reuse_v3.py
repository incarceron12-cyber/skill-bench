import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];V3=ROOT/"pilots/persistent-workspace-reuse/v3"
def load(p):return json.loads(p.read_text())
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class PersistentWorkspaceReuseV3Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.r=module(V3/"run_study.py","workspace_v3");cls.e=module(V3/"execute_study.py","workspace_v3_execution");cls.p=load(V3/"protocol.json")
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
 def test_execution_report_builder_preserves_strict_denominator(self):
  attempts=[]
  for cell in sorted(self.p["cells"],key=lambda c:c["order"]):
   observed=self.r.grader.canonical_output(cell)
   attempts.append({"cell_id":cell["cell_id"],"shape":cell["shape"],"form_id":cell["form_id"],"condition":cell["condition"],"service_valid":True,"environment_valid":True,"substantively_graded":True,"grade":self.r.grader.grade_value(observed,cell["private_contract"]),"observed_state_delta":{"initial_state":cell["visible"]["current_state"],"reported_final_state":observed["state"],"reported_decision":observed["decision"]},"usage":{"api_calls":1,"total_tokens":10,"estimated_cost_usd":0}})
  report=self.e.build_report(self.p,attempts)
  self.assertEqual(24,report["strict_denominators"]["intended"]);self.assertEqual(24,report["strict_denominators"]["attempted_once"])
  self.assertEqual({"pass":24,"fail":0,"invalid":0},report["classification_counts"]);self.assertEqual(4,report["ceiling_or_incomparability"]["decision_discriminating_forms"])
  self.assertFalse(any(report["claim_boundaries"].values()))
 def test_execution_replays_exactly_when_present(self):
  report=V3/"execution/study-report.json"
  if report.exists():
   value=self.e.replay();self.assertEqual(load(report),value);self.assertFalse(value["posthoc_instrument_audit"]["instrument_valid_for_retained_state_effect"]);self.assertEqual("fail_closed_after_single_campaign",value["posthoc_instrument_audit"]["disposition"])
if __name__=="__main__":unittest.main()
