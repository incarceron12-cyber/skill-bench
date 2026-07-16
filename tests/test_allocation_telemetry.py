import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/validate_allocation_telemetry.py"
HOOK = ROOT / "scripts/provider_call_telemetry.py"
MANIFEST = ROOT / "pilots/prospective-allocation-telemetry/v1/manifest.json"
V3_MANIFEST = ROOT / "pilots/prospective-allocation-telemetry/v3/manifest.json"
V3_PROBE = ROOT / "pilots/prospective-allocation-telemetry/v3/configured-provider-probe"
spec = importlib.util.spec_from_file_location("allocation_telemetry", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
hook_spec = importlib.util.spec_from_file_location("provider_call_telemetry", HOOK)
assert hook_spec and hook_spec.loader
hook = importlib.util.module_from_spec(hook_spec)
hook_spec.loader.exec_module(hook)


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

    def native_fixture(self):
        tmp = tempfile.TemporaryDirectory()
        path = Path(tmp.name) / "events.jsonl"
        hook.deterministic_stub(path)
        event = module.load_jsonl(path)[0]
        attempt_id = self.manifest["attempt_schedule"][0]["attempt_id"]
        event["attempt_id"] = attempt_id
        event["call_id"] = attempt_id + ":call:0001"
        event["configured_system_sha256"] = self.manifest["configured_system_sha256"]
        event["phase_declaration_sha256"] = module.canonical_hash({
            "attempt_id": attempt_id, "phase": event["phase"], "call_site": event["call_site"],
        })
        event["event_sha256"] = module.canonical_hash({k: v for k, v in event.items() if k != "event_sha256"})
        aggregate = {"api_calls": 1, "input_tokens": 100, "output_tokens": 21, "cache_read_tokens": 30, "cache_write_tokens": 0, "reasoning_tokens": 5}
        return tmp, event, aggregate

    def test_deterministic_native_stub_reconciles(self):
        tmp, event, aggregate = self.native_fixture()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(module.validate_native_events([event], self.manifest, attempt_id=event["attempt_id"], aggregate_usage=aggregate), [])

    def test_native_mutations_fail_closed(self):
        tmp, base, aggregate = self.native_fixture()
        self.addCleanup(tmp.cleanup)
        duplicate = [copy.deepcopy(base), copy.deepcopy(base)]
        reordered = copy.deepcopy(base); reordered["sequence"] = 2
        spoofed = copy.deepcopy(base); spoofed["phase_source"] = "outcome_text"
        unsupported = copy.deepcopy(base); unsupported["token_coordinates_supported"]["reasoning_tokens"] = False
        retry = copy.deepcopy(base); retry["attempt_id"] = "replacement-attempt"
        changed = copy.deepcopy(base); changed["configured_system_sha256"] = "f" * 64
        mismatch = dict(aggregate); mismatch["input_tokens"] += 1
        mutations = [
            (duplicate, aggregate, "duplicated"), ([reordered], aggregate, "reordered"),
            ([spoofed], aggregate, "phase spoofing"), ([unsupported], aggregate, "unsupported token"),
            ([retry], aggregate, "retry substitution"), ([changed], aggregate, "changed configured-system"),
            ([copy.deepcopy(base)], mismatch, "does not reconcile"),
        ]
        for events, usage, fragment in mutations:
            errors = module.validate_native_events(events, self.manifest, attempt_id=base["attempt_id"], aggregate_usage=usage)
            self.assertTrue(any(fragment in error for error in errors), (fragment, errors))

    def test_v3_configured_provider_probe_is_retained_and_fails_closed(self):
        manifest = json.loads(V3_MANIFEST.read_text(encoding="utf-8"))
        report = json.loads((V3_PROBE / "probe-report.json").read_text(encoding="utf-8"))
        usage = json.loads((V3_PROBE / "outputs/usage.json").read_text(encoding="utf-8"))
        events = module.load_jsonl(V3_PROBE / "outputs/call-events.jsonl")

        self.assertEqual(module.validate_manifest(manifest, check_paths=True), [])
        descriptor = manifest["configured_system"]
        self.assertEqual(module.canonical_hash(descriptor), manifest["configured_system_sha256"])
        errors = module.validate_native_events(
            events, manifest, attempt_id=report["attempt_id"], aggregate_usage=usage,
        )
        self.assertEqual(len(events), 1)
        self.assertEqual(report["model_calls"], 1)
        self.assertEqual(report["decision"], "fail_closed_no_matched_pair")
        self.assertFalse(report["passed"])
        self.assertTrue(report["provider_cost_gate"]["passed"])
        self.assertTrue(any("prompt_tokens" in error for error in errors))
        self.assertTrue(any("cache_write_tokens" in error for error in errors))
        self.assertTrue(all(not value for value in report["claim_ceiling"].values()))


if __name__ == "__main__":
    unittest.main()
