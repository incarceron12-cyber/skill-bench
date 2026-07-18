# Priced-resource accounting conformance slice

This zero-call, builder-authored package tests a general charter hypothesis: a benchmark can preserve **resource assignment → attempt → consumed quantity → price basis → charged/transferred/omitted cost → artifact observation → consequence absence** without collapsing those states into one cost rank. It spans an incident-evidence review with a failed/replaced attempt and a spreadsheet-reconciliation campaign; neither work shape is a scope commitment or a professional simulation.

## Evidence and contract reuse

`package.json` freezes the complete review `papers/agent-benchmarks/2026-07-18-cost-aware-security-agent-evaluation.md` and the existing benchmark-bundle, metric-monitoring, validity-argument, clean-release, and trial-reconciliation machinery by SHA-256. The review's lines 88–120 distinguish charged and excluded resources, lines 181–199 separate realized/reconstructed/counterfactual/total costs and denominator policies, and lines 244–288 require all-attempt accounting and claim ceilings. No new schema is introduced.

`rate-sheet.json` types six price bases: `realized_ledger`, `reconstructed_rate`, `list_price`, `cached_counterfactual`, `amortized_estimate`, and `human_estimate`. `package.json` retains every attempt and resource row, observation source, assigned cap, quantity/unit, priced amount, charged spend, omitted/transferred status, wall time, observed review minutes, synthetic artifact-check acceptance, and explicit absence of stakeholder consequences.

## Planted distinctions

- The higher-cap campaign (cap 10) realizes charged campaign spend 6; the lower-cap campaign (cap 5 per assignment) realizes 10. Cap is not consumed spend.
- The failed initial incident attempt costs 4 and remains in campaign spend, but is absent from retained-valid spend (2). Both numerators are reported.
- A cached request has counterfactual price 1.29 and realized charge 0.
- Campaign A is cheaper per attempt (3 vs 3.333333), while campaign B is cheaper per canonical valid trial (3.333333 vs 6) and per success using campaign spend (5 vs 6). The reversal makes a one-dimensional rank invalid.

## Run

```bash
python pilots/priced-resource-accounting-conformance/replay.py --check-paths --check-report pilots/priced-resource-accounting-conformance/replay-report.json
python -m unittest tests.test_priced_resource_accounting_conformance
```

To regenerate the retained report after an audited fixture change:

```bash
python pilots/priced-resource-accounting-conformance/replay.py --check-paths --write-report pilots/priced-resource-accounting-conformance/replay-report.json
```

## Claim ceiling

The only licensed claim is that the deterministic replay exactly accounts for this retained synthetic **partial-priced execution** fixture and detects its planted boundary violations. It does not estimate total cost, agent capability, economic efficiency, utility, operational fit, risk, safety, professional validity, production fitness, readiness, or cross-domain generalization. No loss function, stakeholder threshold, stakeholder acceptance, downstream benefit/loss, or realized side effect exists in this package.
