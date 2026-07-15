from __future__ import annotations
import importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];PILOT=ROOT/"pilots/evidence-request-interface-v2"
def mod():
 spec=importlib.util.spec_from_file_location("eri_v2",PILOT/"run_study.py");assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class EvidenceRequestInterfaceV2Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.runner=mod()
 def test_v1_audit_is_complete_and_bounded(self):
  audit=json.loads((PILOT/"v1-root-surface-audit.json").read_text());self.assertEqual(4,len(audit["active_attempts"]));self.assertEqual(8,sum(len(x["requests"]) for x in audit["active_attempts"]));self.assertTrue(all("unidentified" in x["root_attribution"] for x in audit["active_attempts"]));self.assertIn("Terminal evidence IDs are a citation proxy, not direct evidence of belief adoption.",audit["claim_limits"])
 def test_structured_synonyms_and_negative_controls_fail_closed(self):
  report=self.runner.parser_canaries();self.assertTrue(report["passed"]);self.assertGreater(len(report["checks"]),20)
  for case in report["checks"]:
   if case["case"]=="negative_control":self.assertEqual([],case["observed"]["mapped_evidence_ids"])
 def test_natural_parser_retains_v1_ambiguity(self):
  scenario=json.loads((ROOT/"pilots/evidence-acquisition-matched-agent-v1/instrument/scenarios/analysis.json").read_text());obs=self.runner.parse_request({"raw_request":"authoritative bot-adjusted retention measurement"},scenario,"natural_request");self.assertEqual("ambiguous",obs["status"]);self.assertEqual({"metric-dictionary","quality-audit"},set(obs["mapped_evidence_ids"]))
 def test_frozen_protocol_and_canaries(self):
  self.assertTrue(self.runner.verify_protocol(False)["passed"]);canary=json.loads((PILOT/"preflight/canary-report.json").read_text());self.assertTrue(canary["passed"]);self.assertEqual(0,canary["model_calls"])
 def test_execution_replays_when_present(self):
  report=PILOT/"execution/study-report.json"
  if not report.exists():self.skipTest("prospective execution not run yet")
  rebuilt=self.runner.replay();self.assertEqual(json.loads(report.read_text()),rebuilt);self.assertEqual(8,rebuilt["denominators"]["intended"]);self.assertEqual(4,len(rebuilt["paired_descriptive_contrasts"]));self.assertTrue(rebuilt["no_pooled_effect"])
 def test_posthoc_flow_audit_preserves_stage_separation(self):
  path=PILOT/"execution/flow-audit.json"
  if not path.exists():self.skipTest("prospective execution not run yet")
  audit=json.loads(path.read_text());self.assertEqual({"intended":8,"retained":8,"eligible":8},audit["denominators"]);self.assertTrue(audit["no_rescoring"])
  self.assertEqual(5,audit["summary"]["natural_request"]["matched"]);self.assertEqual(6,audit["summary"]["structured_request"]["unmatched"])
  self.assertTrue(all("stopping" in row and "parser" in row and "adoption" in row for row in audit["attempt_flows"]))
if __name__=="__main__":unittest.main()
