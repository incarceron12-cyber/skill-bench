# Stateful observer adversarial conformance

This internal synthetic validation matrix tests the projection boundary identified by the full WorkArena L1 review. Native state is not automatically sufficient evidence: the observer must accept declared semantic alternatives, establish task attribution and stable terminal state, cover preserved collateral regions, and verify cleanup.

The nine predeclared cases span three unlike shapes (list query, record update, and source-grounded answer). They accept reordered and noncanonical-but-extensionally-equivalent queries; reject collateral mutation, duplicate/unrelated records, shared-state collision, pre-satisfaction, reversal, and teardown fingerprint failure; and classify a correct answer without observed source access as `insufficient_evidence`, not semantic failure. `replay-report.json` preserves that distinction machine-readably.

This reuses existing benchmark-bundle, task-health, validity, initial-state, and artifact-transition machinery. It adds no schema or ServiceNow dependency. All cases are builder-authored calibration; they establish no agent capability, professional validity, prevalence, expert validity, or readiness.

Run:

```bash
python pilots/stateful-observer-adversarial/validate.py \
  pilots/stateful-observer-adversarial/conformance.json --check-paths \
  --report pilots/stateful-observer-adversarial/replay-report.json
python -m unittest tests.test_stateful_observer_adversarial -v
```
