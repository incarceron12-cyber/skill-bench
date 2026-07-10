from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from scripts.grade_lh_evidence import grade

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots" / "lh-skill-adoption"
CALIBRATION = PILOT / "calibration"
SOURCE = PILOT / "source-pack" / "decision-evidence.csv"


class LhEvidenceGraderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads((ROOT / "schemas" / "benchmark-bundle.schema.json").read_text(encoding="utf-8"))
        cls.check_result_validator = Draft202012Validator(schema).evolve(schema=schema["$defs"]["checkResult"])

    def run_case(self, name: str, source: Path = SOURCE) -> dict[str, object]:
        case = CALIBRATION / name
        return grade(source, case / "evidence-matrix.csv", case / "recommendation.md")

    def diagnostic_codes(self, result: dict[str, object]) -> set[str]:
        return {str(item).split(" | ", 1)[0] for item in result["evidence"]}

    def test_cautious_fixture_passes_and_conforms_to_check_result_contract(self) -> None:
        result = self.run_case("passing")
        self.assertEqual("passed", result["outcome"])
        self.assertEqual(1, result["score"])
        self.check_result_validator.validate(result)

    def test_agreement_overclaim_fails_scope_and_caveat_preservation(self) -> None:
        result = self.run_case("agreement-overclaim")
        self.assertEqual("failed", result["outcome"])
        self.assertIn("VALUE_SCOPE_MISMATCH", self.diagnostic_codes(result))
        self.check_result_validator.validate(result)

    def test_tiny_ablation_overclaim_fails_scope_and_caveat_preservation(self) -> None:
        result = self.run_case("tiny-ablation-overclaim")
        self.assertEqual("failed", result["outcome"])
        self.assertIn("VALUE_SCOPE_MISMATCH", self.diagnostic_codes(result))
        self.check_result_validator.validate(result)

    def test_malformed_source_is_a_grader_failure_not_a_pass(self) -> None:
        source = CALIBRATION / "malformed-source" / "source.csv"
        result = self.run_case("malformed-source", source)
        self.assertEqual("failed", result["outcome"])
        self.assertIn("MALFORMED_SOURCE", self.diagnostic_codes(result))
        self.check_result_validator.validate(result)

    def test_uncited_numeric_memo_claim_is_rejected(self) -> None:
        case = CALIBRATION / "passing"
        memo = case / "recommendation.md"
        original = memo.read_text(encoding="utf-8")
        temporary = case / "_uncited-test.md"
        try:
            temporary.write_text(original + "\nThe reported agreement was 0.60.\n", encoding="utf-8")
            result = grade(SOURCE, case / "evidence-matrix.csv", temporary)
        finally:
            temporary.unlink(missing_ok=True)
        self.assertIn("UNCITED_MATERIAL_CLAIM", self.diagnostic_codes(result))


if __name__ == "__main__":
    unittest.main()
