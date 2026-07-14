# Layered procedure-instrument contract v0.2

`procedure-instrument-layers.schema.json` and
`scripts/validate_procedure_instrument_layers.py` repair the falsified
format-agnostic boundary of procedure-package v0.1 without weakening or rewriting
that tabular calibration contract. The new record reports three questions
independently:

1. **Package:** inventory, version, role, scored-run access, answer-bearing tool,
   and prohibited-oracle conformance.
2. **Environment:** adapter/runtime identity, shape contract, and observed
   deterministic replay readiness.
3. **Trial:** procedure events, final artifact or terminal state, endpoint
   observation, and predeclared accepted alternatives.

A pass at one layer cannot license a claim at another. Evidence is typed
`complete`, `partial`, `unavailable`, or `prohibited`, always with a reason and
an immutable source binding. `unavailable` is not converted to failure or pass;
`prohibited` denotes evidence intentionally excluded from the scored surface and
is not an observed result.

## Supported shapes and outcomes

The outer record supports `tabular_mock_tool` and
`stateful_terminal_state`. Shape support means the inventory can be represented;
it does not mean the runtime or a trial was observed. Every layer derives one of
`pass`, `fail`, `insufficient_evidence`, or `prohibited` and compares it to the
reported result. Claims are separately scoped to one layer and can be
`supported` only when that exact layer passes.

The validator fails closed on:

- an unenforced access boundary, exposed/unverified oracle, or answer-bearing
  tool while preserving the finding as a package-layer failure;
- missing or partial runtime/replay evidence promoted to an environment pass;
- missing final state, trace-derived endpoint substitution, invented accepted
  alternatives, or unavailable observations promoted to a trial result;
- source hash drift, duplicate/unknown provenance, and cross-layer claim
  promotion.

This boundary composes with artifact-view admissibility in the benchmark bundle:
a representation or trace is not a final artifact merely because a grader can
read it. Trial results remain inputs to task-health records and claim-centered
validity arguments; they do not establish task fitness, construct validity, or
readiness themselves.

## Frozen migration

`pilots/procedure-package-released-validation/layered-migration-freeze.json` was
written before implementation. It freezes the unchanged v0.1 calibration, both
released adapters, both prior adapter reports, and both raw v0.1 rejection
reports by SHA-256. The migrated records are:

| Record | Shape | Package | Environment | Trial |
|---|---|---:|---:|---:|
| `schemas/fixtures/procedure-instrument-layers-builder.json` | tabular mock tool | pass | pass | pass |
| `pilots/procedure-package-released-validation/sop-bench-aircraft-inspection.layered.json` | tabular mock tool | fail: answer-bearing tools/access | insufficient evidence | insufficient evidence |
| `pilots/procedure-package-released-validation/anchor-2000.layered.json` | stateful terminal state | fail: exposed oracle access | insufficient evidence | insufficient evidence |

The builder pass is only exact internal calibration. The released records make
no professional-correctness, expert-approval, capability, safety,
production-fitness, or deployment-readiness claim.

## Evidence and adaptation rationale

- `pilots/procedure-package-released-validation/REPORT.md` lines 18–34 and 45–71
  provide the observed v0.1 non-applicability, unavailable runtime/trial evidence,
  exposed-oracle findings, and three-layer repair requirement.
- The frozen SOP and Anchor adapter manifests/reports provide exact role,
  availability, runtime, and access observations; migration does not fill their
  gaps from prose or alter source bytes.
- `schemas/PROCEDURE_PACKAGE.md` lines 18–43 preserves the useful v0.1 internal
  role, oracle, endpoint, and procedure checks.
- `schemas/TASK_HEALTH.md` lines 19–46 and `schemas/VALIDITY_ARGUMENTS.md` lines
  17–42 establish that an observed trial remains distinct from task fitness and
  licensed interpretation. The per-layer claim gate is a skill-bench adaptation
  tested here only on internal and frozen static records.

## Validate

```bash
python scripts/validate_procedure_instrument_layers.py --check-paths \
  --report-dir pilots/procedure-package-released-validation/reports \
  schemas/fixtures/procedure-instrument-layers-builder.json \
  pilots/procedure-package-released-validation/sop-bench-aircraft-inspection.layered.json \
  pilots/procedure-package-released-validation/anchor-2000.layered.json
python -m unittest tests.test_procedure_instrument_layers -v
```
