from __future__ import annotations

import json
import unittest
from pathlib import Path
from typing import Any, cast

from scripts.diagnose_lh_provenance import ROOT, diagnose


REPORT = ROOT / "pilots/lh-skill-adoption/ablation/provenance-failure-diagnosis.json"


class LhProvenanceDiagnosisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.generated = cast(dict[str, Any], diagnose())
        cls.persisted = cast(dict[str, Any], json.loads(REPORT.read_text(encoding="utf-8")))

    def test_persisted_report_is_exactly_reproducible(self) -> None:
        self.assertEqual(self.persisted, self.generated)

    def test_all_four_historical_results_replay_exactly(self) -> None:
        cases = self.generated["cases"]
        self.assertEqual(4, len(cases))
        self.assertTrue(all(case["replay_exact"] for case in cases))
        self.assertTrue(all(case["historical_outcome"] == "failed" for case in cases))

    def test_frozen_manifest_hashes_current_exact_versions(self) -> None:
        for item in self.generated["frozen_files"]:
            path = ROOT / item["path"]
            self.assertTrue(path.is_file())
            self.assertEqual(path.stat().st_size, item["bytes"])

    def test_diagnosis_separates_artifact_and_grader_failure_signatures(self) -> None:
        counts = self.generated["diagnostic_category_counts"]
        self.assertGreater(counts["artifact_convention_mismatch"], 0)
        self.assertGreater(counts["artifact_realization"], 0)
        self.assertGreater(counts["grader_scope_false_rejection_candidate"], 0)

    def test_parenthetical_counterfactual_is_calibration_only(self) -> None:
        cases = {case["case_id"]: case for case in self.generated["cases"]}
        counterfactual = cases["isolated-agent-pair-v10/no-skill"]["counterfactual_parentheses_to_brackets"]
        self.assertTrue(counterfactual["changed"])
        self.assertEqual("builder_authored_calibration_only", counterfactual["kind"])
        self.assertLess(counterfactual["diagnostic_count"], len(cases["isolated-agent-pair-v10/no-skill"]["diagnostics"]))

    def test_historical_rescoring_and_capability_claims_are_prohibited(self) -> None:
        self.assertFalse(self.generated["minimal_versioned_correction"]["historical_rescore_permitted"])
        self.assertIn("Skill efficacy", self.generated["claims_prohibited"])
        self.assertIn("professional validity", self.generated["claims_prohibited"])


if __name__ == "__main__":
    unittest.main()
