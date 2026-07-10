# Metric specification and monitoring contract v0.1

`metric-monitoring.schema.json` and
`scripts/validate_metric_monitoring.py` implement the operating-layer bridge from
immutable observations to a population estimate and a governed action:

```text
trial/check observation
  → eligible population + handling + computation + uncertainty
    → versioned metric estimate
      → baseline + threshold/loss + alert/audit/remediation/rollback
```

This is cross-domain measurement infrastructure. It does **not** combine score
families, make a metric label self-defining, convert synthetic examples into a
production population, or allow a monitoring threshold to license a capability
or readiness claim.

## Enforced boundaries

1. **Immutable basis.** Metrics reference SHA-256-bound tasks/bundles, checks,
   graders, configured systems, validity arguments, measurements, candidate
   catalogs, baselines, source populations, or fidelity studies. Optional
   `--check-paths` verifies repository paths and bytes.
2. **Population before statistic.** Every metric declares the unit, eligible
   event, inclusion/exclusion, sampling, exact time/version window, cluster
   keys, source-population kind, and target boundary.
3. **Observable before label.** A predicate has evidence locators, an explicit
   outcome mapping, and an insufficient-evidence state. “Tool selection” also
   requires a versioned candidate catalog, availability rule, equivalence rule,
   and unknown-alternative policy.
4. **No silent denominator changes.** Missing, invalid, delayed, retried, and
   duplicate observations each have predeclared handling. Rate estimates are
   arithmetically checked and keep their counts.
5. **Dependence and uncertainty remain visible.** Aggregation, weighting,
   clustering/dependence, uncertainty method, slices, and minimum support are
   separate fields. Exact fixture enumeration cannot masquerade as population
   uncertainty.
6. **Synthetic provenance is not representativeness.** A bounded or
   representative synthetic/simulated-population claim requires typed
   target-population fidelity evidence; a `representative` claim must be
   supported. The positive fixture makes no such claim.
7. **Actions bind exact metric versions.** Monitoring policies identify the
   metric version, baseline/window/comparability rule, threshold and loss basis,
   alert route, audit outcomes/burden, remediation evidence, rollback, owner,
   and expiry. Production actions cannot use a calibration-only baseline,
   provisional threshold, unbridged version pooling, or fixture enumeration as
   uncertainty.

## Calibration fixture

`tests/fixtures/valid-metric-monitoring.json` specifies one narrow metric over
`tests/fixtures/lh-planted-grader-calibration-measurement.json`:

- **eligible population:** exactly eight named builder-authored
  case-by-check cells planted to emit `failed`;
- **estimate:** 8/8 (`1.0`) for pinned local bytes;
- **use:** internal deterministic regression alert only;
- **fidelity:** no external representativeness claim;
- **forbidden claims:** grader reliability, semantic correctness, agent
  capability, professional quality, Skill efficacy, production fitness, and
  deployment readiness.

A test resolves all eight JSON locators against the immutable measurement and
confirms the observed literals. This is useful executable contract calibration,
not an independent accuracy study: fixture cases, expected outcomes, graders,
and this metric were co-authored within the project.

## Design rationale and provenance

| Choice | Rationale | Evidence |
|---|---|---|
| Separate check observation, metric, and action records | A per-trial result does not define a population estimand or operational trigger. | `docs/concepts/amazon-production-agent-evaluation.md`, “Unique insight” and “Concrete transfer” |
| Candidate catalog/equivalence contract for tool selection | Logged-tool equality, acceptable alternatives, availability, and semantic judgment compute different quantities. | same concept note, “Tool descriptions are part of the configured treatment” |
| Missing/invalid/delayed/retry/duplicate policies | Agent, provider, grader, and labeling failures must not silently become negatives or disappear from denominators. | same concept note, limitations 7–8; `papers/agent-benchmarks/2026-07-10-agentrewardbench-judge-reliability.md`, Metrics and limitations 21–22 |
| Clustered/sliced uncertainty and explicit loss | Pooled judge precision varies across task families, shared tasks induce dependence, and preferred errors depend on use. | AgentRewardBench review, “Metrics, uncertainty, and decision use” and patterns 3–4 |
| Criterion dependence and eligible criterion populations | Fine-grained rubric labels can overlap; missing grader states and additive weighting do not define calibrated artifact quality. | `papers/agent-benchmarks/2026-07-10-researchrubrics-expert-rubric-authoring.md`, Rubric construction and concrete change 5 |
| Fidelity gate for synthetic/simulated populations | Historical or generated provenance does not establish target-population prevalence, ambiguity, or failure-mode coverage. | Amazon concept note, “Synthetic golden data has a transformation boundary” |
| Versioned threshold/action lifecycle | Drift can come from traffic, instruments, tools, judges, or interventions; alerts need owners, audit burden, remediation, and rollback. | Amazon concept note, “Continuous monitoring changes the sampling problem” |

Amazon's article is an official production experience report, not a controlled
or quantitative validation of this contract. The two paper reviews supply
additional measurement threats, not proof that this schema is sufficient. The
contract remains an executable project hypothesis requiring later use across
meaningfully different domains, independent metric review, backtests, and
real-population fidelity studies.

## Validate

```bash
python scripts/validate_metric_monitoring.py --check-paths \
  tests/fixtures/valid-metric-monitoring.json
python -m unittest tests.test_validate_metric_monitoring -v
```
