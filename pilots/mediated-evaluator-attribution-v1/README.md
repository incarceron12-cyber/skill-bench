# Mediated evaluator attribution conformance v1

This is a **zero-call, builder-authored validation package**, not a benchmark result. It tests a cross-domain instrument pattern:

`candidate artifact → observed mediator uptake → mediator action → projected check`.

The two synthetic work shapes are a vendor-risk memo and a laboratory reconciliation workbook. They are deliberately unlike; neither is proposed as the project’s permanent scope. The package advances charter objectives B and C by testing reusable attribution, projection, metric-denominator, configured-system, and validity boundaries.

## What is executable

Run:

```bash
python pilots/mediated-evaluator-attribution-v1/replay.py --check-paths --write-report
python -m unittest tests.test_mediated_evaluator_attribution -v
```

`replay.py` validates frozen provenance hashes, the complete case × candidate × mediator matrix, typed terminal states, mediator-validity missingness, and candidate→uptake→action consistency. It emits `report.json` with:

- source-population, projectable, mediator-valid, attempted, and scored denominators for every configured package;
- candidate→uptake→action→check chains;
- separate selected projected-check and uptake-attributable/noncompensatory rates;
- explicit unknown and invalid observations;
- unsupported-claim and collateral-cost totals; and
- the five planted diagnostics.

## Planted boundaries

1. A projected check passes after the mediator ignores the candidate and independently acts.
2. One candidate claim drives two checks, preventing check count from masquerading as finding count.
3. An independently valid alternative fails an implementation-specific projected oracle.
4. Positive checks pass alongside unsupported claims and a collateral change; those costs fail noncompensatorily.
5. Candidate ordering reverses between two frozen mediators, so no pooled “candidate quality” ranking is licensed.

## Contract reuse and provenance

No c-CRAB-specific schema was added. `protocol.json` pins and reuses:

- `tests/fixtures/valid-task-projection-manifest.json` for requirement/check projection;
- `schemas/benchmark-bundle.schema.json` for configured systems, traces, views, and checks;
- `schemas/metric-monitoring.schema.json` for population, denominator, missingness, and aggregation semantics; and
- `schemas/validity-argument.schema.json` for claim ceilings.

Design evidence is the full paper/release review at `papers/agent-benchmarks/2026-07-17-c-crab-review-test-projection-validity.md`, especially its unique insight, transferable patterns, and concrete changes. The fixture adapts those lessons; it does not reuse c-CRAB data or claim to reproduce its results.

## Claim boundary

The package supports only exact deterministic detection of the planted signatures in these frozen internal records. It provides no evidence of agent capability, real candidate quality, mediator superiority, cross-domain generalization, expert or professional validity, production fitness, or deployment readiness.
