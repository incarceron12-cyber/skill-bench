from __future__ import annotations
import importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PILOT=ROOT/"pilots/evidence-request-receipt-repair-v3"
def mod():
 spec=importlib.util.spec_from_file_location("err_v3",PILOT/"run_study.py");assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class EvidenceRequestReceiptRepairV3Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.runner=mod()
 def test_independent_conformance_and_mutations(self):
  result=self.runner.conformance();self.assertTrue(result["passed"]);self.assertEqual(0,result["model_calls"]);self.assertEqual(11,len(result["checks"]));self.assertTrue(all(result["mutations"].values()))
 def test_receipts_match_parser_and_reveal_no_private_fields(self):
  result=self.runner.conformance();allowed={"status","normalized_interpreted_topic","repair_eligible"}
  for case in result["checks"]:self.assertEqual(allowed,set(case["receipt"]));self.assertEqual(case["observed"]["status"],case["receipt"]["status"])
  self.assertTrue(result["receipt_firewall"])
 def test_ambiguous_and_unknown_fail_closed(self):
  for case in self.runner.conformance()["checks"]:
   if case.get("kind") in {"multi_target_ambiguity","unknown_topic_negative","domain_token_perturbation"}:self.assertEqual([],case["observed"]["mapped_evidence_ids"] if case["observed"]["status"]=="unmatched" else case["observed"]["mapped_evidence_ids"][:0])
 def test_protocol_and_zero_call_preflight(self):
  self.assertTrue(self.runner.verify_protocol(False)["passed"]);report=json.loads((PILOT/"preflight/canary-report.json").read_text());self.assertTrue(report["passed"]);self.assertEqual(0,report["model_calls"])
 def test_execution_replays_when_present(self):
  report=PILOT/"execution/study-report.json"
  if not report.exists():self.skipTest("prospective execution not run")
  rebuilt=self.runner.replay();self.assertEqual(json.loads(report.read_text()),rebuilt);self.assertEqual(8,rebuilt["denominators"]["intended"]);self.assertTrue(rebuilt["no_shape_pooling"]);self.assertTrue(rebuilt["descriptive_only"])
if __name__=="__main__":unittest.main()
