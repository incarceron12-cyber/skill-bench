import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "pilots/pretask-procedure-transfer-v3"
SPEC = importlib.util.spec_from_file_location("pretask_v3_generation_audit", PILOT / "audit_generation.py")
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class PretaskProcedureTransferV3GenerationTests(unittest.TestCase):
    def test_retained_invalid_attempts_pass_audit_and_fail_gate(self):
        result = AUDIT.audit()
        self.assertEqual(result["audit_status"], "PASS")
        self.assertEqual(result["generation_gate"], "fail")
        self.assertFalse(result["downstream_authorized"])
        self.assertEqual(result["aggregate_attempts"], {"generation": 2, "model": 2, "provider": 2, "repair": 0, "executor": 0})
        self.assertTrue(all(value is False for value in result["claim_boundaries"].values()))
        self.assertTrue(all(row["independent_validation"] == "invalid" for row in result["observations"].values()))

    def test_retry_count_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            shutil.copytree(PILOT / "generation", base / "generation")
            report_path = base / "generation/family-gamma/report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["provider_attempts"] = 2
            report_path.write_text(json.dumps(report), encoding="utf-8")
            result = AUDIT.audit(base)
            self.assertEqual(result["audit_status"], "FAIL")
            self.assertTrue(any("attempt count" in error for error in result["errors"]))

    def test_downstream_directory_is_rejected_after_failed_gate(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            shutil.copytree(PILOT / "generation", base / "generation")
            (base / "controls").mkdir()
            result = AUDIT.audit(base)
            self.assertEqual(result["audit_status"], "FAIL")
            self.assertFalse(result["downstream_authorized"])
            self.assertTrue(any("downstream directory" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
