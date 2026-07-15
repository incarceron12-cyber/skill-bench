import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "pilots/repeated-task-family-matrix/v1"

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_runner():
    spec = importlib.util.spec_from_file_location("repeated_matrix_runner", STUDY / "run_matrix.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class RepeatedTaskFamilyMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol = load(STUDY / "protocol.json")
        cls.report = load(STUDY / "execution/study-report.json")
        cls.runner = load_runner()

    def test_frozen_protocol_has_two_families_four_forms_and_two_repeats(self):
        self.assertTrue(self.runner.verify_protocol(self.protocol)["passed"])
        self.assertEqual({v["family"] for v in self.protocol["forms"].values()}, {"evidence", "incident"})
        self.assertEqual(len(self.protocol["forms"]), 4)
        for key in self.protocol["forms"]:
            self.assertEqual(sum(r["family"] + "/" + r["form"] == key for r in self.protocol["schedule"]["rows"]), 2)

    def test_all_frozen_component_hashes_resolve(self):
        for component in self.protocol["frozen_components"]:
            self.assertEqual(sha(STUDY / component["path"]), component["sha256"])

    def test_report_replays_and_preserves_every_declared_attempt_once(self):
        self.assertEqual(self.runner.build_report(self.protocol), self.report)
        ids = [r["attempt_id"] for r in self.report["attempt_rows"]]
        self.assertEqual(len(ids), 8)
        self.assertEqual(len(set(ids)), 8)
        self.assertTrue(all(r.get("launcher_invocations") == 1 for r in self.report["attempt_rows"]))
        self.assertTrue(all(r["service_available"] and r["valid_trial"] for r in self.report["attempt_rows"]))

    def test_confidence_channel_fails_closed(self):
        self.assertEqual(self.report["confidence_channel"], {"status": "insufficient_evidence", "coverage": 0, "denominator": 8})
        self.assertTrue(all(r["confidence_channel"]["status"] == "insufficient_evidence" for r in self.report["attempt_rows"]))

    def test_adjudication_blocks_substantive_interpretation_without_rescoring(self):
        audit = load(STUDY / "instrument-adjudication.json")
        self.assertEqual(audit["status"], "instrument_defect_blocks_substantive_use")
        self.assertEqual(sha(STUDY / "execution/study-report.json"), audit["evidence"]["study_report"]["sha256"])
        self.assertEqual(sha(STUDY / "grade.py"), audit["evidence"]["grader"]["sha256"])
        self.assertIn("within-form substantive reliability", audit["prohibited_interpretations"])
        obs = audit["evidence"]["study_report"]["observations"]
        self.assertEqual((obs["decision_exact_failures"], obs["action_exact_failures"], obs["evidence_id_passes"]), (8, 8, 8))

if __name__ == "__main__":
    unittest.main()
