import copy
import json
import unittest
from pathlib import Path

from scripts.validate_plural_judgment import semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas/fixtures/plural-judgment-conformance.json"

class PluralJudgmentTests(unittest.TestCase):
    def setUp(self):
        self.package = json.loads(FIXTURE.read_text())

    def test_fixture_valid(self):
        validate_file(FIXTURE)

    def test_irreducible_requires_all_gates(self):
        p = copy.deepcopy(self.package)
        p["disagreement_cases"][2]["disposition"] = "irreducible_disagreement"
        self.assertTrue(any("every reducibility gate" in x for x in semantic_errors(p)))

    def test_framework_label_requires_prospective_declaration(self):
        p = copy.deepcopy(self.package)
        p["frameworks"][0]["declared_before_observation"] = False
        self.assertTrue(any("stable prospective" in x for x in semantic_errors(p)))

    def test_unendorsed_aggregate_preserves_dissent(self):
        p = copy.deepcopy(self.package)
        p["aggregations"][0]["dissent_observation_ids"] = ["framework-a1"]
        self.assertTrue(any("every contributing observation" in x for x in semantic_errors(p)))

    def test_policy_output_is_reproducible(self):
        p = copy.deepcopy(self.package)
        p["aggregations"][0]["output"] = 3.5
        self.assertTrue(any("weighted rule" in x for x in semantic_errors(p)))

    def test_consensus_upgrade_is_denied(self):
        p = copy.deepcopy(self.package)
        p["claim_limits"]["unsupported"] = [x for x in p["claim_limits"]["unsupported"] if "expert consensus" not in x]
        self.assertTrue(any("expert consensus" in x for x in semantic_errors(p)))

if __name__ == "__main__": unittest.main()
