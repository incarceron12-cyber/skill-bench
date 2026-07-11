# Dynamic criterion conformance slice

This internal synthetic slice tests the general hypothesis that fixed obligations and response-created claim/consequence checks can remain fair and diagnosable **without sharing a denominator**. It uses a decision memo and an executable notebook so the machinery is not tied to one profession or artifact.

`cases.json` preserves fixed and contingent ledgers, exact trigger locators, public basis/applicability, generator identity, dependencies/overlap, four evidence outcomes, irrelevant-edit stability expectations, and provenance hashes. `scripts/validate_dynamic_criteria.py` validates and grades it deterministically.

Planted checks cover: unsupported/missing trigger (mutation test), criterion-set drift after an irrelevant edit, duplicate overlap exclusion, absent verifier fail-closed behavior, dependency relations, and legitimate `not_applicable`. Fixed completion and contingent outcomes are reported separately. A contradicted criterion is substantive evidence; absent verification is `insufficient_evidence` and blocks capability use rather than restoring a reasoning-only score.

## Evidence mapping

- Triggered claim/consequence criteria and dependency gating: JADE paper §§3.3–3.6, pp. 3–4, 15–17; full review lines 65–86.
- Trigger/public-basis, overlap, four outcomes, generation provenance, fail-closed verification, and plural score families: review lines 128–149 and 197–212; taxonomy §2.3a.
- Missing-evidence fail-open failure being guarded against: review lines 84–86 and 187–193.

Run:

```bash
python scripts/validate_dynamic_criteria.py --check-paths
python -m unittest tests.test_dynamic_criterion_conformance
```

## Claim boundary

The cases are builder-authored contract calibration only. They do not establish agent capability, expert validity, professional readiness, criterion-generator/verifier accuracy, or cross-domain generalization. `eligible_for_narrow_argument` means only that this synthetic record is not blocked by missing verification; no validity argument is supplied here.
