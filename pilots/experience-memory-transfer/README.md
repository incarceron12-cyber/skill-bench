# Experience-memory transfer conformance slice

This internal synthetic pilot exercises the evidence-to-action boundary identified in the full LongMemEval-V2 review. It is a cross-domain contract calibration, not a web-agent benchmark or a memory subsystem.

## Executed comparison

The same planted history is exposed under three conditions:

1. `no_memory`;
2. `evidence_only`, where evidence can be retrieved without promotion controls;
3. `provenance_gated_promoted_lesson`, where version, valid time, applicability, contradiction, and supersession are resolved.

Each condition has two non-substitutable outcomes: equivalent-form evidence QA and an unseen-instance artifact/state action. The evidence-only condition intentionally answers QA correctly but adopts a stale observation for action, causing harmful transfer and a recorded quarantine/retry rollback. The promoted condition safely disables the synthetic integration and retains a receipt.

The fixture preserves six trajectory-derived knowledge types: valid procedure, failed attempt, stale observation, scoped gotcha, contradiction, and safe alternative. Every record types source span, environment version, valid time, applicability, attempt, and realization. Condition records preserve `available -> accessed -> adopted` evidence flow.

The OdysseyBench extension adds one hidden requirement with an exact original span, distractor, and later correction/supersession. Six deterministic observations keep raw-history success, summary omission/retrieval failure, stale adoption, required-state failure, collateral-preservation failure, and unavailable-evaluator instrument invalidity distinct. The state contract separately declares required, permitted, forbidden, and preserved state. The unavailable evaluator is explicitly excluded from the capability denominator; it is not scored as agent failure.

## Design rationale and provenance

The fixture implements the review's nonduplicate recommendation to connect retrospective QA and held-out action while reusing the existing compounding-lesson, benchmark-bundle, longitudinal, validity, task-health, and metric contracts. LongMemEval-V2 supports the importance of evidence selection/presentation for retrospective QA; it does **not** empirically support this planted action effect or promotion policy.

Primary repository evidence:

- full review: `papers/agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md`, especially pp. 5–8, 16–26 as mapped there;
- immutable paper: `data/papers/pdfs/2605.12493v1-longmemeval-v2-environment-experience-memory.pdf`;
- release provenance: `data/sources/releases/2605.12493v1-longmemeval-v2/provenance.json`;
- targeted release trace: `data/sources/releases/2605.12493v1-longmemeval-v2/two-item-trace-summary.json`.
- OdysseyBench full review: `papers/agent-benchmarks/2026-07-11-odysseybench-longitudinal-office-memory-validity.md`, especially its evidence-to-consequence chain (lines 91–102), release defects (75–77), and repairs (149–160).

No persistent-memory, Skill-effect, professional competence, agent-capability, prevalence, cross-domain generality, deployment-safety, or release-readiness claim is licensed. There are no stochastic components; a single deterministic replay per cell is therefore explicit rather than presented as uncertainty evidence.

## Replay

```bash
python scripts/validate_experience_memory_transfer.py --check-paths \
  --report pilots/experience-memory-transfer/replay-report.json \
  pilots/experience-memory-transfer/conformance.json
python -m unittest tests.test_experience_memory_transfer -v
```
