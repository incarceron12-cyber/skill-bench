import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "pilots/prospective-allocation-telemetry/v4/manifest.json"
PROBE = ROOT / "pilots/prospective-allocation-telemetry/v4/configured-provider-probe"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path); assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module


validator = load_module("allocation_coordinates", ROOT / "scripts/validate_allocation_coordinates.py")
adapter = load_module("provider_coordinates", ROOT / "scripts/provider_call_telemetry_v4.py")


class AllocationCoordinateTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def fixture(self):
        temp = tempfile.TemporaryDirectory(); path = Path(temp.name) / "events.jsonl"
        attempt = "alloc-v4-ab-no-skill"
        adapter.deterministic_stub(path, attempt_id=attempt, configured_system_sha256=self.manifest["configured_system_sha256"], contract_sha256=self.manifest["coordinate_contract_sha256"], comparison_sha256=self.manifest["comparison_identity_sha256"])
        event = validator.load_jsonl(path)[0]
        usage = {"api_calls": 1, "input_tokens": 130, "cache_read_tokens": 30, "output_tokens": 21, "reasoning_tokens": 5, "cache_write_tokens": 0}
        return temp, attempt, event, usage

    def resign(self, event):
        event["event_sha256"] = validator.canonical_hash({k: v for k, v in event.items() if k != "event_sha256"})

    def test_manifest_binds_coordinate_contract_and_comparison(self):
        self.assertEqual(validator.validate_manifest(self.manifest, check_paths=True), [])
        contract = self.manifest["coordinate_contract"]
        self.assertEqual(contract["coordinates"]["cache_write_tokens"]["status"], "unavailable")
        self.assertEqual(contract["additive_budget_coordinates"], ["total_input_tokens", "output_tokens"])

    def test_stub_reconciles_supported_coordinates_without_imputation(self):
        temp, attempt, event, usage = self.fixture(); self.addCleanup(temp.cleanup)
        self.assertIsNone(event["coordinates"]["cache_write_tokens"]["value"])
        self.assertEqual(event["imputations"], [])
        self.assertEqual(validator.validate_events([event], self.manifest, attempt_id=attempt, aggregate_usage=usage), [])

    def test_rejects_coordinate_drift_imputation_and_double_counting(self):
        temp, attempt, base, usage = self.fixture(); self.addCleanup(temp.cleanup)
        drift = copy.deepcopy(base); drift["coordinates"]["cache_write_tokens"] = {"status": "supported", "value": 0, "source_field": "invented"}; self.resign(drift)
        imputed = copy.deepcopy(base); imputed["coordinates"]["cache_write_tokens"]["value"] = 0; imputed["imputations"] = ["cache_write_tokens=0"]; self.resign(imputed)
        impossible = copy.deepcopy(base); impossible["coordinates"]["cache_read_tokens"]["value"] = 131; self.resign(impossible)
        for event, fragment in ((drift, "support drift"), (imputed, "coerced or imputed"), (impossible, "exceeds total input")):
            errors = validator.validate_events([event], self.manifest, attempt_id=attempt, aggregate_usage=usage)
            self.assertTrue(any(fragment in error for error in errors), errors)

    def test_rejects_omission_duplicate_reorder_retry_phase_and_identity(self):
        temp, attempt, base, usage = self.fixture(); self.addCleanup(temp.cleanup)
        duplicate = [base, copy.deepcopy(base)]
        reordered = copy.deepcopy(base); reordered["sequence"] = 2; self.resign(reordered)
        retry = copy.deepcopy(base); retry["attempt_id"] = "replacement"; self.resign(retry)
        phase = copy.deepcopy(base); phase["phase_source"] = "output_inferred"; self.resign(phase)
        identity = copy.deepcopy(base); identity["comparison_identity_sha256"] = "f" * 64; self.resign(identity)
        for events, fragment in ((duplicate, "duplicated"), ([reordered], "reordered"), ([retry], "retry substitution"), ([phase], "phase spoofing"), ([identity], "changed comparison-identity")):
            errors = validator.validate_events(events, self.manifest, attempt_id=attempt, aggregate_usage=usage)
            self.assertTrue(any(fragment in error for error in errors), (fragment, errors))

    def test_rejects_asymmetric_condition_support(self):
        temp, _, base, _ = self.fixture(); self.addCleanup(temp.cleanup)
        other = copy.deepcopy(base); other["coordinates"]["cache_read_tokens"]["status"] = "unavailable"; other["coordinates"]["cache_read_tokens"]["value"] = None
        errors = validator.validate_pair({"no_skill": [base], "public_skill": [other]}, self.manifest)
        self.assertIn("asymmetric condition coordinate support", errors)

    def test_retained_configured_provider_probe_passes_once(self):
        report = validator.load(PROBE / "probe-report.json"); usage = validator.load(PROBE / "outputs/usage.json"); events = validator.load_jsonl(PROBE / "outputs/call-events.jsonl")
        self.assertTrue(report["passed"]); self.assertEqual(report["model_calls"], 1)
        self.assertEqual(validator.validate_events(events, self.manifest, attempt_id=report["attempt_id"], aggregate_usage=usage), [])
        event = events[0]
        self.assertEqual(event["coordinates"]["total_input_tokens"]["value"], usage["input_tokens"])
        self.assertEqual(event["coordinates"]["cache_write_tokens"], {"status": "unavailable", "value": None, "source_field": None})
        self.assertTrue(all(not value for value in report["claim_ceiling"].values()))


if __name__ == "__main__": unittest.main()
