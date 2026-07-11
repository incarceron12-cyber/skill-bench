# Outcome-evidence bounds conformance slice

This internal synthetic calibration slice exercises existing evidence-view, environment-validity, metric, task-health, and validity semantics together; it adds no schema. Its design basis is the full-source review `papers/agent-benchmarks/2026-07-11-outcome-evidence-score-bounds.md`, especially the native/evidence/stronger-claim split (lines 21–50) and repository implications (lines 97–126), grounded in the immutable paper PDF and text hashes recorded in `conformance.json`.

The locked corpus spans two unlike work shapes: a stateful operational workflow and a document-to-decision handoff. It deliberately keeps five concepts separate:

1. the released/native success or failure label;
2. evidence support, contradiction, or insufficiency;
3. a benchmark/evaluator conflict flag;
4. a stronger professional-condition result; and
5. typed denominator inclusion or proven pre-run exclusion.

For each cell, `N=P+F+U` is the valid-start fixed denominator. The calculator emits `[P/N,(P+U)/N]` as an exact rational and decimal identification interval, not a confidence interval. A decisive contradiction is classified by the supported outcome while preserving the original native label and conflict. Unknown is never converted to success or failure. A stronger-condition failure cannot rewrite supported native success. Only a canary-proven pre-run invalid environment is excluded; post-start failures remain.

The two synthetic intervals overlap, so directional ranking is explicitly unresolved. This is not evidence of equality.

Run:

```bash
python pilots/outcome-evidence-bounds/grade.py --check-paths
python -m unittest tests.test_outcome_evidence_bounds
```

These builder-authored records demonstrate deterministic contract behavior only. They support no agent capability, grader reliability, expert validity, professional readiness, population ranking, or cross-domain generalization claim.
