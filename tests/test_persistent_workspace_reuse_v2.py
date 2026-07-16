import copy,hashlib,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];V2=ROOT/"pilots/persistent-workspace-reuse/v2"
def load(p):return json.loads(p.read_text())
def module():
 spec=importlib.util.spec_from_file_location("workspace_v2",V2/"run_study.py");assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class PersistentWorkspaceReuseV2Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.r=module();cls.p=load(V2/"protocol.json")
 def test_frozen_matrix_and_v1_preservation(self):
  v=self.r.verify_protocol(False);self.assertTrue(v["passed"],v["errors"]);self.assertEqual(12,len(self.p["schedule"]));self.assertTrue(v["v1_preserved"])
  self.assertEqual({"structured_table":2,"structured_memo":2},{s:sum(f["shape"]==s for f in self.p["forms"].values()) for s in ("structured_table","structured_memo")})
 def test_information_matched_presentations(self):
  for form in self.p["forms"].values():
   history=self.r.presentation(self.p,form,"information_matched_full_history");curated=self.r.presentation(self.p,form,"curated_correct")
   self.assertEqual(history["current_requirements"],curated["current_requirements"]);self.assertEqual(history["current_information"],curated["current_information"]);self.assertEqual(history["base_artifact"],curated["base_artifact"])
   self.assertEqual(history["retained_state"]["objects"][0]["content"],curated["retained_state"]["objects"][0]["content"])
 def test_planted_controls_and_graders(self):
  self.assertTrue(self.r.compatibility_and_authority_canaries(self.p)["passed"])
  for form in self.p["forms"].values():self.assertTrue(self.r.grader.calibration(form)["passed"])
 def test_mutation_detects_prompt_drift(self):
  p=copy.deepcopy(self.p);p["forms"]["table-a"]["retained_fact"]="mutated"
  row=next(x for x in p["schedule"] if x["form_id"]=="table-a" and x["condition"]!="reset")
  self.assertNotEqual(row["model_visible_presentation_sha256"],self.r.canon(self.r.presentation(p,p["forms"]["table-a"],row["condition"])))
 def test_preflight_or_execution_when_present(self):
  pre=V2/"preflight/gate-report.json"
  if pre.exists():
   r=load(pre);self.assertTrue(r["passed"]);self.assertEqual(0,r["model_calls"]);self.assertTrue(all(x["passed"] for x in r["isolation"]))
  report=V2/"execution/study-report.json"
  if report.exists():
   r=load(report);self.assertEqual(self.r.replay(),r);self.assertEqual(12,r["denominators"]["intended"]);self.assertTrue(r["no_pooled_outcome"]);self.assertEqual("unobserved",r["semantic_adoption"])
   self.assertTrue(all(a["launcher_invocations"]==1 for a in r["attempts"]));self.assertFalse(any(r["claim_boundaries"].values()))
if __name__=="__main__":unittest.main()
