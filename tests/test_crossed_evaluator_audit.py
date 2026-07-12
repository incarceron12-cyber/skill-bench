import importlib.util, json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/"pilots/crossed-evaluator-audit"
spec=importlib.util.spec_from_file_location("crossed_audit",HERE/"audit.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class CrossedEvaluatorAuditTests(unittest.TestCase):
    def test_frozen_inputs_have_no_oracle_fields(self):
        text=(HERE/"evaluator-inputs.json").read_text()
        for forbidden in ('"verdict"','"rationale"','"reference"','"expected"'):
            self.assertNotIn(forbidden,text)

    def test_required_shapes_and_failures(self):
        p=json.loads((HERE/"protocol.json").read_text()); rows=json.loads((HERE/"evaluator-inputs.json").read_text())["cases"]
        self.assertEqual(set(p["work_shapes"]),{r["work_shape"] for r in rows})
        self.assertTrue(set(p["required_failure_types"]).issubset({r["failure_type"] for r in rows}))

    def test_valid_alternative_and_wrong_target(self):
        r=mod.replay(write=False); by={x["case_id"]:x for x in r["rows"]}
        for cid in ("memo-alternate","memo-wrong-target"):
            self.assertEqual(by[cid]["native_deterministic"],"fail")
            self.assertEqual(by[cid]["hybrid_restricted"],"pass")
            self.assertEqual(by[cid]["reference"],"pass")

    def test_missing_view_abstains_and_unsafe_fails(self):
        r=mod.replay(write=False); by={x["case_id"]:x for x in r["rows"]}
        self.assertEqual(by["action-missing-view"]["hybrid_restricted"],"abstain")
        self.assertEqual(by["action-unsafe-superficial"]["hybrid_restricted"],"fail")

    def test_hashes_and_model_claim_are_fail_closed(self):
        r=mod.replay(write=False)
        self.assertTrue(all(len(v)==64 for v in r["frozen_hashes"].values()))
        self.assertEqual(r["model_condition"]["status"],"not_executed")
        self.assertIn("evaluator_superiority",r["excluded_claims"])

if __name__=="__main__": unittest.main()
