from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts.grade_lh_claims import grade

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "lh-skill-adoption"
CALIBRATION = PILOT / "calibration"
CONFIG = PILOT / "graders" / "independent-claim-rubric.json"


class LhPrivateClaimCalibratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads((ROOT / "schemas" / "benchmark-bundle.schema.json").read_text(encoding="utf-8"))
        cls.validator = Draft202012Validator(schema).evolve(schema=schema["$defs"]["checkResult"])

    def run_case(self, name: str) -> dict[str, dict[str, object]]:
        case = CALIBRATION / name
        results = grade(CONFIG, case / "evidence-matrix.csv", case / "recommendation.md")
        for result in results:
            self.validator.validate(result)
        return {str(result["check_id"]): result for result in results}

    @staticmethod
    def codes(result: dict[str, object]) -> set[str]:
        return {str(item).split(" | ", 1)[0] for item in result["evidence"]}

    def test_cautious_fixture_passes_both_private_conventions(self) -> None:
        results = self.run_case("passing")
        self.assertEqual("passed", results["contradiction-reconciliation"]["outcome"])
        self.assertEqual("passed", results["causal-claim-strength"]["outcome"])

    def test_agreement_overclaim_fails_reconciliation(self) -> None:
        result = self.run_case("agreement-overclaim")["contradiction-reconciliation"]
        self.assertEqual("failed", result["outcome"])
        self.assertIn("MISSING_COUNTEREVIDENCE_GROUP", self.codes(result))
        self.assertIn("AGREEMENT_AS_VALIDITY", self.codes(result))

    def test_salient_effect_without_scope_anchor_fails_causal_check(self) -> None:
        result = self.run_case("tiny-ablation-overclaim")["causal-claim-strength"]
        self.assertEqual("failed", result["outcome"])
        self.assertIn("MISSING_CAUSAL_SCOPE_ANCHOR", self.codes(result))
        self.assertIn("CAUSAL_OVERCLAIM", self.codes(result))

    def test_effect_without_directional_and_controlled_language_fails(self) -> None:
        result = self.run_case("tiny-ablation-overclaim")["causal-claim-strength"]
        self.assertIn("MISSING_CAUSAL_BOUNDARY", self.codes(result))

    def test_comma_grouped_citations_satisfy_evidence_groups(self) -> None:
        case = CALIBRATION / "passing"
        memo = (case / "recommendation.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            grouped = Path(tmp) / "recommendation.md"
            grouped.write_text(
                memo.replace("[E01]", "[E01, E02]").replace("[E05]", "[E05, E06]"),
                encoding="utf-8",
            )
            results = grade(CONFIG, case / "evidence-matrix.csv", grouped)
        outcomes = {str(item["check_id"]): item["outcome"] for item in results}
        self.assertEqual("passed", outcomes["contradiction-reconciliation"])
        self.assertEqual("passed", outcomes["causal-claim-strength"])


if __name__ == "__main__":
    unittest.main()
