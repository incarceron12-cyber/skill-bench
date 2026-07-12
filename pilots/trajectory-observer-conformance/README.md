# Trajectory-observer evidence conformance

This internal synthetic package tests one reusable boundary: an ordinal trajectory review is a typed observer observation, not a formal outcome, causal diagnosis, user label, or calibrated alert.

## Design and provenance

The matrix operationalizes the AgentLens review's findings that judge views can be truncated or omit final state; unparseable scores can be inconsistently excluded or zero-imputed; narrative evidence needs trajectory locators; inferred “mechanisms” are not intervention-confirmed causes; and formal checks must remain alongside rather than collapse into experiential ratings. Exact review anchors and reused repository contracts are recorded in `conformance.json`.

Two unlike work shapes prevent a coding-only interpretation: a stateful operational workflow and a document-to-decision handoff. Nine predeclared cases cover complete evidence, truncation, missing environment/final-user state, invalid ordinal output, an unlocated narrative, unsupported causal promotion, formal/experiential disagreement, and missingness converted to zero plus an alert.

The replay preserves criterion/rubric/observer/evidence-view identities in the work-shape contracts. Each case separately records the formal observation and its locator. `invalid` and `insufficient_evidence` never become numeric values; a formal pass plus poor observer rating is retained as disagreement, not reconciled by overwriting either observation.

## Replay

```bash
python pilots/trajectory-observer-conformance/validate.py --check-paths --write-report
python -m unittest tests.test_trajectory_observer_conformance
```

`replay-report.json` is the machine-readable diagnostic. All records are builder-authored contract tests. They provide no user-validity, judge-interchangeability, capability, calibrated-alert, production-utility, professional-validity, readiness, or cross-domain-generalization evidence.
