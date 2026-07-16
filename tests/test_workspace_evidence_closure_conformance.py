from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "workspace-evidence-closure-conformance"
spec = importlib.util.spec_from_file_location("workspace_evidence_closure", PILOT / "run.py")
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class WorkspaceEvidenceClosureConformanceTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads((PILOT / "fixture.json").read_text(encoding="utf-8"))

    def test_eight_cases_replay_at_predeclared_layers(self):
        report = module.build_report(self.fixture)
        self.assertEqual(8, report["summary"]["total_cases"])
        self.assertEqual(8, report["summary"]["exact_matches"])
        self.assertEqual(6, report["summary"]["planted_failures_detected_at_expected_layers"])
        self.assertTrue(report["summary"]["all_exact"])

    def test_committed_machine_report_is_exact_replay(self):
        expected = json.loads((PILOT / "report.json").read_text(encoding="utf-8"))
        self.assertEqual(expected, module.build_report(self.fixture))

    def test_mutations_are_diagnostically_separate(self):
        rows = {row["case_id"]: row for row in module.build_report(self.fixture)["results"]}
        expected = {
            "target-omission": ["obligation_closure"],
            "numerically-failing-predicate": ["predicate_closure"],
            "stale-execution-hash": ["byte_lineage"],
            "vacuous-self-consistent-source-trace": ["source_entailment"],
            "locator-only-report": ["report_handoff"],
            "stale-rendered-artifact": ["report_handoff"],
        }
        for case_id, layers in expected.items():
            self.assertEqual(layers, rows[case_id]["observed_failing_layers"], case_id)

    def test_legitimate_alternative_is_not_exact_witness_matching(self):
        case = next(item for item in self.fixture["cases"] if item["case_id"] == "legitimate-alternative-implementation")
        workspace = module.apply_mutation(self.fixture["base_workspace"], case["mutation"])
        result = module.evaluate(workspace, self.fixture["frozen_obligation_inventory"])
        self.assertEqual("passed", result["overall"])
        artifact = next(item for item in workspace["artifacts"] if item["target_id"] == "target-total")
        self.assertEqual("reduce", artifact["payload"]["implementation"])
        self.assertNotEqual(
            self.fixture["base_workspace"]["artifacts"][0]["accepted_sha256"],
            artifact["accepted_sha256"],
        )

    def test_inventory_hash_and_authority_fail_closed(self):
        inventory = copy.deepcopy(self.fixture["frozen_obligation_inventory"])
        inventory["obligations"][0]["requirement"] = "Actor-rewritten denominator"
        result = module.evaluate(self.fixture["base_workspace"], inventory)
        self.assertEqual("failed", result["layers"]["obligation_closure"]["outcome"])
        self.assertTrue(any("hash mismatch" in reason for reason in result["layers"]["obligation_closure"]["reasons"]))

        inventory = copy.deepcopy(self.fixture["frozen_obligation_inventory"])
        inventory["author_role"] = "evaluated_actor"
        result = module.evaluate(self.fixture["base_workspace"], inventory)
        self.assertEqual("failed", result["layers"]["obligation_closure"]["outcome"])

    def test_false_claim_upgrade_is_rejected(self):
        fixture = copy.deepcopy(self.fixture)
        fixture["claim_boundary"]["scientific_correctness"] = True
        with self.assertRaisesRegex(ValueError, "cannot license"):
            module.build_report(fixture)

    def test_provenance_paths_and_hashes_are_checked(self):
        fixture = copy.deepcopy(self.fixture)
        fixture["provenance"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "provenance path/hash mismatch"):
            module.build_report(fixture)


if __name__ == "__main__":
    unittest.main()
