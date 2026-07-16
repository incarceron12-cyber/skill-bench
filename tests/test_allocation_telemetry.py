import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_allocation_telemetry.py"
MANIFEST = ROOT / "pilots/prospective-allocation-telemetry/v1/manifest.json"
spec = importlib.util.spec_from_file_location("allocation_telemetry", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AllocationTelemetryTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.record = module.zero_call_canary(self.manifest)

    def resign(self, doc):
        payload = {key: value for key, value in doc.items() if key != "ledger_sha256"}
        doc["ledger_sha256"] = module.canonical_hash(payload)

    def test_manifest_and_zero_call_canary_pass(self):
        self.assertEqual(module.validate_manifest(self.manifest, check_paths=True), [])
        self.assertEqual(module.validate_record(self.record, self.manifest), [])
        self.assertEqual(self.record["model_calls"], [])
        self.assertTrue(all(not value for value in self.record["claim_ceiling"].values()))

    def test_rejects_omitted_phase(self):
        doc = copy.deepcopy(self.record)
        doc["phase_totals"].pop("repair")
        self.resign(doc)
        self.assertTrue(any("omitted" in e for e in module.validate_record(doc, self.manifest)))

    def test_rejects_duplicate_call(self):
        doc = copy.deepcopy(self.record)
        call = {"call_id": "c1", "phase": "verification", "wall_time_ms": 1} | {key: 0 for key in module.TOKEN_KEYS}
        doc["model_calls"] = [call, copy.deepcopy(call)]
        self.resign(doc)
        self.assertTrue(any("duplicated model-call" in e for e in module.validate_record(doc, self.manifest)))

    def test_rejects_misphased_call(self):
        doc = copy.deepcopy(self.record)
        doc["model_calls"] = [{"call_id": "c1", "phase": "misc", "wall_time_ms": 0} | {key: 0 for key in module.TOKEN_KEYS}]
        self.resign(doc)
        self.assertTrue(any("misphased" in e for e in module.validate_record(doc, self.manifest)))

    def test_rejects_unhashed_state_and_stale_ledger(self):
        doc = copy.deepcopy(self.record)
        doc["shared_state"]["initial_sha256"] = "unknown"
        errors = module.validate_record(doc, self.manifest)
        self.assertTrue(any("unhashed shared state" in e for e in errors))
        self.assertTrue(any("stale telemetry ledger" in e for e in errors))

    def test_rejects_reordered_scheduled_attempt(self):
        doc = copy.deepcopy(self.record)
        planned = self.manifest["attempt_schedule"][0]
        doc.update(planned)
        doc["within_block_order"] = 2
        self.resign(doc)
        self.assertTrue(any("reordered" in e for e in module.validate_record(doc, self.manifest)))

    def test_rejects_retry_or_replacement(self):
        doc = copy.deepcopy(self.record)
        doc["retry_lineage"]["attempt_number"] = 2
        doc["retry_lineage"]["retry_of"] = "failed-1"
        self.resign(doc)
        self.assertTrue(any("retried or replacement" in e for e in module.validate_record(doc, self.manifest)))

    def test_rejects_presentation_as_adoption(self):
        doc = copy.deepcopy(self.record)
        evidence = {"type": "presentation_only", "sha256": "0" * 64}
        doc["module_flow"]["adoption"] = {"status": "observed", "evidence": evidence}
        self.resign(doc)
        self.assertTrue(any("cannot be inferred as adoption" in e for e in module.validate_record(doc, self.manifest)))

    def test_readiness_fails_closed_on_aggregate_usage(self):
        report = module.assess_launcher_readiness(self.manifest)
        self.assertFalse(report["ready"])
        self.assertEqual(report["fresh_model_calls"], 0)
        self.assertIn("aggregate totals only", report["blockers"][0])
        self.assertEqual(report["decision"], "fail_closed_without_provider_calls")


if __name__ == "__main__":
    unittest.main()
