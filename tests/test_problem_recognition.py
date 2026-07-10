import copy, json, unittest
from pathlib import Path
from scripts.validate_problem_recognition import replay, semantic_errors, validate_file
ROOT=Path(__file__).resolve().parents[1]; FIXTURE=ROOT/"pilots/problem-recognition-intervention/conformance.json"
class ProblemRecognitionTests(unittest.TestCase):
 def setUp(self): self.p=json.loads(FIXTURE.read_text())
 def test_fixture_and_provenance(self): validate_file(FIXTURE,check_paths=True)
 def test_replay_separates_stages_and_invalidity(self):
  rows=replay(self.p); self.assertTrue(rows[0]["recognition"]); self.assertTrue(rows[0]["execution"]); self.assertEqual(rows[-1]["disposition"],"invalid_environment"); self.assertIsNone(rows[-1]["recognition"])
 def test_label_template_leakage_rejected(self):
  p=copy.deepcopy(self.p); p["conditions"][0]["forbidden_disclosure"].remove("expected_label"); self.assertTrue(any("leakage" in x for x in semantic_errors(p)))
 def test_framed_condition_drift_rejected(self):
  p=copy.deepcopy(self.p); p["observations"].pop(0); self.assertTrue(any("drift" in x for x in semantic_errors(p)))
 def test_cue_only_cannot_be_execution(self):
  p=copy.deepcopy(self.p); p["scoring_policy"]["execution_gate"]=["cue_extraction"]; self.assertTrue(any("collapsed" in x for x in semantic_errors(p)))
 def test_action_without_supported_framing_rejected(self):
  p=copy.deepcopy(self.p); p["observations"][0]["problem_framing"]=False; self.assertTrue(any("without supported framing" in x for x in semantic_errors(p)))
 def test_claim_upgrade_rejected(self):
  p=copy.deepcopy(self.p); p["validity_record"]["unsupported"].remove("professional competence"); self.assertTrue(any("non-claims" in x for x in semantic_errors(p)))
if __name__=="__main__": unittest.main()
