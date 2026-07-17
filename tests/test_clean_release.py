import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_clean_release.py"
MANIFEST = ROOT / "pilots/cross-pilot-clean-release/v1/manifest.json"
SPEC = importlib.util.spec_from_file_location("clean_release", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CleanReleaseTests(unittest.TestCase):
    def setUp(self):
        self.base = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def errors(self, doc, check_paths=False):
        return MODULE.semantic_errors(doc, check_paths=check_paths)

    def test_retained_two_package_release_and_controls_pass(self):
        report = MODULE.validate_release(MANIFEST)
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual("passed_internal_clean_release_conformance", report["status"])
        self.assertEqual(2, report["package_count"])
        self.assertEqual(2, len(report["work_shapes"]))
        self.assertTrue(all(row["passed"] for row in report["control_results"]))
        self.assertTrue(all(value is False for value in report["claim_ceiling"].values()))

    def test_rejects_duplicate_release_task_identity(self):
        doc = copy.deepcopy(self.base)
        doc["packages"][1]["task_ids"][0] = doc["packages"][0]["task_ids"][0]
        self.assertTrue(any("duplicate task identity" in error for error in self.errors(doc)))

    def test_rejects_stale_hash(self):
        doc = copy.deepcopy(self.base)
        doc["packages"][0]["components"][0]["sha256"] = "0" * 64
        self.assertTrue(any("stale hash" in error for error in self.errors(doc, check_paths=True)))

    def test_rejects_non_parsing_evaluator(self):
        doc = copy.deepcopy(self.base)
        with tempfile.NamedTemporaryFile("w", suffix=".py", dir=ROOT, delete=False) as handle:
            handle.write("def broken(:\n")
            path = Path(handle.name)
        try:
            component = doc["packages"][0]["components"][2]
            component["path"] = path.relative_to(ROOT).as_posix()
            component["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            errors = self.errors(doc, check_paths=True)
            self.assertTrue(any("compile check failed" in error for error in errors), errors)
        finally:
            path.unlink()

    def test_rejects_missing_and_mismatched_control_result(self):
        missing = copy.deepcopy(self.base)
        missing["packages"][0]["controls"][0].pop("result_evidence")
        self.assertTrue(any(error.startswith("schema:") for error in self.errors(missing)))
        mismatch = copy.deepcopy(self.base)
        mismatch["packages"][0]["controls"][0]["expected_evidence"][0]["equals"] = "rejected"
        errors = self.errors(mismatch, check_paths=True)
        self.assertTrue(any("result-evidence predicate mismatch" in error for error in errors), errors)

    def test_rejects_conflicting_aggregation_identity(self):
        doc = copy.deepcopy(self.base)
        doc["packages"][1]["aggregation_id"] = "route-macro-v1"
        self.assertTrue(any("conflicting aggregation identity" in error for error in self.errors(doc)))

    def test_rejects_undeclared_containment(self):
        doc = copy.deepcopy(self.base)
        doc["packages"][1]["containment"].pop("network")
        errors = self.errors(doc)
        self.assertTrue(any(error.startswith("schema:") or "containment" in error for error in errors), errors)

    def test_rejects_unpinned_expected_stdout(self):
        doc = copy.deepcopy(self.base)
        doc["packages"][1]["controls"][0]["expected_stdout"]["json_path"] = "tests/fixtures/valid-benchmark-bundle.json"
        self.assertTrue(any("expected stdout file is not a pinned component" in error for error in self.errors(doc)))


if __name__ == "__main__":
    unittest.main()
