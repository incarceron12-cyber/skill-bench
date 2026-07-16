import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "preflight_cross_pilot_suite.py"
MANIFEST = ROOT / "pilots" / "cross-pilot-suite-preflight" / "v1" / "manifest.json"
spec = importlib.util.spec_from_file_location("suite_preflight", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CrossPilotSuitePreflightTests(unittest.TestCase):
    def setUp(self):
        self.base = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def errors(self, doc):
        return module.semantic_errors(doc, check_paths=False)

    def test_frozen_manifest_and_real_commands_pass(self):
        report = module.run_preflight(MANIFEST)
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual(report["status"], "passed_internal_conformance")
        self.assertEqual(len(report["components"]), 3)
        self.assertEqual(len(report["alternate_assembly_sensitivity"]["results"]), 3)
        self.assertTrue(all(row["passed"] for row in report["command_results"]))
        self.assertTrue(all(status in {"unsupported", "blocked"} for status in report["pooled_claims"].values()))

    def test_rejects_stale_hash(self):
        doc = copy.deepcopy(self.base)
        doc["candidate_pool"][0]["artifacts"][0]["sha256"] = "0" * 64
        errors = module.semantic_errors(doc, check_paths=True)
        self.assertTrue(any("stale sha256" in error for error in errors), errors)

    def test_rejects_missing_parent(self):
        doc = copy.deepcopy(self.base)
        doc["candidate_pool"][0]["artifacts"][0]["path"] = "pilots/does-not-exist.json"
        errors = module.semantic_errors(doc, check_paths=True)
        self.assertTrue(any("missing parent artifact" in error for error in errors), errors)

    def test_rejects_duplicate_lineage_presented_as_independent(self):
        doc = copy.deepcopy(self.base)
        for item in doc["candidate_pool"][:2]:
            item["lineage_clusters"] = ["same-lineage"]
            item["presented_as_independent"] = True
        self.assertTrue(any("duplicate lineage presented as independent" in error for error in self.errors(doc)))

    def test_rejects_invalid_service_evidence_as_substantive(self):
        doc = copy.deepcopy(self.base)
        doc["candidate_pool"][1]["substantive_evidence_eligible"] = True
        doc["candidate_pool"][1]["service_evidence"] = "service_invalid"
        self.assertTrue(any("admitted as substantive" in error for error in self.errors(doc)))

    def test_rejects_declared_grader_or_replay_failure(self):
        doc = copy.deepcopy(self.base)
        doc["candidate_pool"][1]["commands"][0]["expected_exit"] = 1
        self.assertTrue(any("expect exit 0" in error for error in self.errors(doc)))
        command = copy.deepcopy(self.base["candidate_pool"][1]["commands"][0])
        result = subprocess.CompletedProcess(command["argv"], 1, "", "planted failure")
        passed, detail = module.check_command_result(command, result)
        self.assertFalse(passed)
        self.assertIn("exit 1", detail)

    def test_rejects_silent_exclusion(self):
        doc = copy.deepcopy(self.base)
        doc["assembly"]["dispositions"].pop()
        self.assertTrue(any("silent exclusion" in error for error in self.errors(doc)))

    def test_rejects_mixture_mismatch(self):
        doc = copy.deepcopy(self.base)
        doc["assembly"]["intended_mixture"]["work_shapes"]["spreadsheet_memo"] = 2
        self.assertTrue(any("mixture mismatch" in error for error in self.errors(doc)))

    def test_rejects_pooled_claim_upgrade_without_supported_components_and_sensitivity(self):
        doc = copy.deepcopy(self.base)
        doc["pooled_claims"]["capability"] = "supported"
        doc["assembly"]["alternate_assembly_sensitivity"]["required"] = False
        errors = self.errors(doc)
        self.assertTrue(any("pooled claim upgrade" in error for error in errors), errors)
        self.assertTrue(any("leave-one-component-out sensitivity" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
