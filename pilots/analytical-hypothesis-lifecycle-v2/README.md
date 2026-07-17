# Analytical hypothesis lifecycle configured-agent trial v2

This is the versioned descendant of the byte-preserved `analytical-hypothesis-lifecycle-v1` conformance fixture. It tests a general analytical-work hypothesis across two unlike synthetic work shapes; it is not a vendor-operations or laboratory scope commitment.

## Question and frozen design

Can natural configured-agent outputs be observed as separate links in this chain without turning evaluator failure into agent failure?

`source-bound observation → candidate + rival → discriminating-test selection → independent execution → contradictory-evidence adoption → bounded conclusion → proportionate consequence/escalation`

Before model calls, `manifest.json` froze:

- vendor-incident and laboratory-quality work shapes;
- no-guidance versus public lifecycle-guidance conditions;
- two repeats per shape/condition (eight intended rows);
- order, configured system, task/source hashes, v1 parent hashes, isolation, stopping, zero-cost, invalidity, denominator, and claim policies;
- five separate score families with no holistic score or cross-shape pooling; and
- private exclusion of expected statuses, discriminating-test labels, authorization labels, grader rationales, other attempts, and repository files.

The four zero-call condition/shape canaries passed before the launcher ran. The frozen launcher then ran exactly once. Each task namespace exposed only the matched public task and source pack, plus `public-guide.md` in the guidance condition. The harness independently executed the selected public test after terminal submission.

## Retained result

All **8/8 intended rows** were attempted, service-valid, execution-valid, grader-parse-valid, and retained. Each selected and independently executed the discriminating test. The provider reported **35 calls, 164,045 total tokens, included cost $0.00**. Task-manifest-to-output latency was **29.990–60.419 seconds** (mean **35.954 seconds**); this filesystem-based latency was added before commit because the provider usage ledger did not emit duration, and it changed no output, score, denominator, or call.

Stage results remain separate:

| work shape | condition | candidate | test selection/execution | contradictory-evidence adoption | bounded conclusion | consequence |
|---|---:|---:|---:|---:|---:|---:|
| vendor incident | no guidance | 8/8 | 8/8 | 4/6 | 4/6 | evaluator invalid (0/2 rows eligible) |
| vendor incident | lifecycle guidance | 8/8 | 8/8 | 4/6 | 5/6 | evaluator invalid (0/2 rows eligible) |
| laboratory anomaly | no guidance | 8/8 | 8/8 | 2/6 | 4/6 | evaluator invalid (0/2 rows eligible) |
| laboratory anomaly | lifecycle guidance | 8/8 | 8/8 | 6/6 | 6/6 | evaluator invalid (0/2 rows eligible) |

These two repeats suggest only a candidate pattern: lifecycle guidance coincided with better evidence adoption and bounded conclusions in the laboratory shape, but not a uniform difference in the vendor shape. They do not support an intervention estimate.

### Evaluator invalidity discovered

The frozen consequence observer used a negation-blind harmful-keyword check. All eight natural outputs explicitly recommended abstaining from sanction, discipline, or blame, but mentioning those prohibited acts triggered the rule. The retained reports preserve the original criterion outputs and classify `authorized_consequence` as `invalid_evaluator_rule` with denominator zero, rather than imputing eight agent failures. This is a useful stress result and a precise continuation requirement: a future instrument version needs a calibrated action/negation parser, while this version must remain immutable.

## Reproduction and tests

Do **not** execute the launcher again; replacement attempts are prohibited. Replay retained evidence:

```bash
python pilots/analytical-hypothesis-lifecycle-v2/launcher.py replay
python -m unittest tests.test_analytical_hypothesis_lifecycle_v2 -v
```

Mutation tests reject oracle leakage, malformed stage-observer output, missing independent test execution, and denominator drift. `execution/` retains every raw output, redacted trace, usage ledger, independent test result, stage observation, validity state, exclusion decision, and summary.

## Claim boundary

This internal synthetic matrix makes no expertise-transfer, professional-validity, causal-capability, cross-domain-generalization, safety, production-fitness, readiness, or intervention-effect claim. It establishes only that eight configured attempts were validly retained, four stage families could be replayed separately, and the fifth frozen observer failed on natural negated-action language.
