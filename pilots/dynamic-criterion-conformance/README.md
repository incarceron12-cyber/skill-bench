# Dynamic criterion conformance slice

This internal synthetic slice tests the general hypothesis that fixed obligations and response-created claim/consequence checks can remain fair and diagnosable **without sharing a denominator**. It uses a decision memo and an executable notebook so the machinery is not tied to one profession or artifact.

`cases.json` preserves fixed and contingent ledgers, exact trigger locators, public basis/applicability, generator identity, dependencies/overlap, four evidence outcomes, irrelevant-edit stability expectations, and provenance hashes. `instance-conformance.json` adds independently versioned and payload-hashed task, source, reference, and rubric components with typed entity/deliverable/date/topic predicates and evidence locators. `scripts/validate_dynamic_criteria.py` validates and grades both fixtures deterministically while leaving the original `cases.json` bytes unchanged.

Planted checks cover: unsupported/missing trigger (mutation test), criterion-set drift after an irrelevant edit, duplicate overlap exclusion, absent verifier fail-closed behavior, dependency relations, and legitimate `not_applicable`. Fixed completion and contingent outcomes are reported separately. A contradicted criterion is substantive evidence; absent verification is `insufficient_evidence` and blocks capability use rather than restoring a reasoning-only score.

The instance-conformance slice contains four assignments: an aligned screenplay set, the XpertBench-observed shape of a screenplay task paired with a digital-clock lesson rubric, a same-work-shape supplier/date substitution, and an aligned alternate HTML representation. A task declares which typed predicates each role must carry; the validator compares those predicates directly. It does not branch on assignment/component IDs, domain labels, payload keywords, rationale text, or stored expected outcomes. Component-hash failures invalidate the package; planted semantic substitutions remain structurally valid calibration records but report `conformant: false` with role/dimension-specific missing or conflicting values. Representation is admitted when it is not a task-required identity predicate.

## Evidence mapping

- Triggered claim/consequence criteria and dependency gating: JADE paper §§3.3–3.6, pp. 3–4, 15–17; full review lines 65–86.
- Trigger/public-basis, overlap, four outcomes, generation provenance, fail-closed verification, and plural score families: review lines 128–149 and 197–212; taxonomy §2.3a.
- Missing-evidence fail-open failure being guarded against: review lines 84–86 and 187–193.
- Cross-instance task/rubric projection drift: XpertBench v4 Appendix A.3, pp. 18–19; local text lines 880–932; full review lines 99–114 and 241–252. The matched Appendix A.5 rubric at pp. 23–25/local text lines 1106–1189 supplies the aligned comparison shape. Builder-authored source/reference projections are explicitly labeled because XpertBench did not release those components.

Run:

```bash
python scripts/validate_dynamic_criteria.py --check-paths
python -m unittest tests.test_dynamic_criterion_conformance
```

## Claim boundary

The cases are builder-authored contract calibration only. They do not establish agent capability, expert validity, professional readiness, criterion-generator/verifier accuracy, or cross-domain generalization. `eligible_for_narrow_argument` means only that this synthetic record is not blocked by missing verification; no validity argument is supplied here.
