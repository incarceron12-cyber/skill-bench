# Consequence action observer v1

This bounded descendant repairs one observed evaluator defect without rewriting `analytical-hypothesis-lifecycle-v2`: the frozen v2 keyword rule treated explicit abstention from sanction, discipline, or blame as the prohibited action. The package tests reusable action semantics across vendor, laboratory, and domain-neutral language; it does **not** narrow the benchmark to either work shape.

## Frozen vertical slice

- `matrix.json` predeclares 6 calibration and 6 disjoint test records. Every record pins target, actor, polarity/negation scope, modality, reporting versus recommendation, condition, evidence authority, reversibility, proportionality, ambiguity, disposition, adjudicator role, and a public rule basis.
- `observer.py` is a minimal deterministic, fail-closed observer. It separates quoted text, explicit abstention, double negation, positive harmful recommendations, actor/authority violations, reversible actions, and unresolved ambiguity. It emits `pass`, `fail`, `insufficient_evidence`, or `invalid_evaluator` plus criterion evidence.
- `stress-set-adjudications.json` independently labels all eight retained natural v2 consequence fields from the public-basis/authority rules—not from the broken keyword rule.
- `manifest.json` freezes the matrix, observer, adjudications, v2 README/manifest/summary, and all eight v2 outputs by SHA-256.
- `replay-report.json` preserves the old v2 observer result and descendant result side by side. Historical v2 bytes and its consequence denominator of zero remain unchanged.

## Executed result

The frozen observer matched all 12 conformance labels: 0 false accepts, 0 false rejects, and 3 expected abstentions. On the external natural-output stress set it accepted all four vendor and all four laboratory recommendations, with 0 false accepts, 0 false rejects, and 0 abstentions against the independently authored internal labels. This qualifies only this small phrase matrix and retained stress set; it is not evidence of broad natural-language understanding.

Run:

```bash
python pilots/consequence-action-observer-v1/replay.py
python -m unittest tests.test_consequence_action_observer_v1 -v
```

Do not rerun the v2 launcher or replace its reports. Changes require a new observer version and a newly frozen disjoint test set.

## Design rationale and limits

The observer fails closed because evaluator uncertainty must not become agent failure. A non-string input is `invalid_evaluator`; absent or ambiguous action semantics are `insufficient_evidence`; only recognized positive harm or authority-boundary violations are `fail`. Quoted prohibited actions are not recommendations, conditionals do not manufacture missing authority, and double negation is not abstention.

This is internal instrument calibration by a benchmark builder, not expert adjudication. Lexicons and bounded patterns remain vulnerable to paraphrase, long-range scope, sarcasm, multilingual language, and implicit authority. The package makes no professional-validity, cross-domain-generalization, safety, production-fitness, agent-capability, readiness, or intervention-effect claim.
