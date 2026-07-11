import copy
import json
import unittest
from pathlib import Path

from scripts.validate_information_flow_entitlements import semantic_errors, validate_file

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas/fixtures/information-flow-entitlement-conformance.json"

class InformationFlowEntitlementTests(unittest.TestCase):
    def setUp(self): self.package = json.loads(FIXTURE.read_text())

    def test_fixture_and_provenance_paths_validate(self):
        validate_file(FIXTURE, check_paths=True)

    def test_raw_disclosure_to_team_is_rejected(self):
        p = copy.deepcopy(self.package)
        o = p["observations"][2]
        o.update(representation="raw", transformation_id=None, content="dialysis appointment", outcome="permitted")
        self.assertTrue(any("outcome must be prohibited" in e for e in semantic_errors(p)))

    def test_surface_substitution_into_shared_memory_is_detected(self):
        p = copy.deepcopy(self.package)
        p["observations"][3]["outcome"] = "permitted"
        self.assertTrue(any("outcome must be prohibited" in e for e in semantic_errors(p)))

    def test_raw_detail_hidden_under_sanitized_label_is_rejected(self):
        p = copy.deepcopy(self.package)
        p["observations"][2]["content"] += " because of a dialysis appointment"
        errors = semantic_errors(p)
        self.assertTrue(any("raw fingerprint propagated" in e for e in errors))

    def test_access_does_not_imply_raw_use(self):
        p = copy.deepcopy(self.package)
        p["observations"][1].update(representation="raw", transformation_id=None, content="dialysis appointment", outcome="permitted")
        self.assertTrue(any("outcome must be prohibited" in e for e in semantic_errors(p)))

    def test_unpinned_transformation_is_rejected(self):
        p = copy.deepcopy(self.package)
        p["observations"][2]["transformation_id"] = "missing-transform"
        self.assertTrue(any("lacks matching transformation" in e for e in semantic_errors(p)))

    def test_expired_entitlement_is_rejected(self):
        p = copy.deepcopy(self.package)
        p["observations"][2]["timestamp"] = "2026-07-13T10:00:00Z"
        self.assertTrue(any("outcome must be prohibited" in e for e in semantic_errors(p)))

    def test_claim_upgrade_is_rejected(self):
        p = copy.deepcopy(self.package)
        p["claim_limits"]["unsupported"].remove("deployment safety")
        self.assertTrue(any("non-claims" in e for e in semantic_errors(p)))

if __name__ == "__main__": unittest.main()
