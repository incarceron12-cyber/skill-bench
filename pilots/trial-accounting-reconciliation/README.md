# Trial-accounting reconciliation gate

This optional, cross-domain gate proves that a frozen expected-assignment set reaches an exhaustive, mutually exclusive set of canonical trial dispositions **before** any score is emitted. It adds no repository schema and does not rewrite historical bundles: the adjacent contracts already represent trial states, missing/invalid/retry policy, aggregation identity, and adjudication; the missing invariant was a reusable assignment-to-score reconciliation check.

## Design basis and provenance

The immediate defect pattern is the full paper/release audit in `papers/agent-benchmarks/2026-07-18-ui-cube-operational-reliability-validity.md`:

- lines 95–105 show that published complex-task percentages are jointly compatible with about 67 results despite 90 declared complex tasks, and distinguish family macro from task micro;
- lines 186–188 identify broad exception handling and absent per-task results as a route to missing executions;
- lines 208–228 require an assigned/started/valid/invalid/infrastructure/timeout/completed/scored ledger and separate estimands.

`expected-assignments.json` freezes the review, immutable paper, and relevant existing contracts by path and SHA-256. It uses two materially unlike work shapes—stateful UI transitions and evidence-grounded decision artifacts—so the mechanism is not a computer-use benchmark commitment. The retained fixture is builder-authored contract calibration, not reconstructed UI-CUBE data.

## Contract

Every manifest assignment has one retry policy and must have exactly one **canonical** ledger row. Additional rows are attempts, not extra assignments, and require an explicit replacement chain plus one canonical selection. Every attempt carries exactly one disposition:

- `not_started`
- `valid_scored`
- `timeout`
- `service_failure`
- `environment_invalid`
- `instrument_invalid`
- `missing_artifact`
- `missing_result`
- `justified_exclusion`

Only `valid_scored` accepts a `pass` or `fail`. Invalid, missing, timed-out, service-failed, and excluded attempts cannot silently enter the success/failure numerator. A justified exclusion requires a reason and evidence locator. The gate rejects unknown assignments, duplicate canonical dispositions, missing rows, retry ambiguity, manifest/component drift, and failure to reconcile canonical disposition count to assigned count.

`task_micro` is pass count over canonical `valid_scored` assignments. `family_macro` is the unweighted mean of separately retained family rates with at least one valid score. Both must be declared independently. In the retained fixture they deliberately differ (`0.5` versus `0.375`), making accidental substitution observable.

The focused mutation suite constructs a 90-assignment complex family with only 67 result rows and verifies that all 23 absent rows are named and the report fails reconciliation. It also plants every defect required by the queue task.

## Run

```bash
python pilots/trial-accounting-reconciliation/reconcile.py \
  --check-paths \
  --check-report pilots/trial-accounting-reconciliation/reconciliation-report.json
python -m unittest tests.test_trial_accounting_reconciliation
```

To intentionally regenerate the retained report after an audited fixture change:

```bash
python pilots/trial-accounting-reconciliation/reconcile.py \
  --check-paths \
  --write-report pilots/trial-accounting-reconciliation/reconciliation-report.json
```

## Claim boundary

Completion licenses only deterministic detection of the planted accounting defects in retained builder-authored fixtures. It does **not** establish agent capability, benchmark reliability, grader accuracy, expert or professional validity, production fitness, population generalization, or readiness.
