# Retained-campaign trial-accounting validation v1

This additive package applies the reusable fixed-denominator gate in the parent directory to two materially different, byte-preserved empirical campaigns:

- `persistent-workspace-reuse/v3`: 24 state-transition assignments across structured change records and budget ledgers; and
- `action-boundary-composition/v2`: six realistic artifact/action assignments across incident-response and evidence-memo forms, including service failure, invalid post-stop launches, interruption, and one unlaunched row.

It advances Charter objectives B and C by testing whether the synthetic reconciliation mechanism transfers to retained execution evidence. It does not reinterpret the campaigns or narrow `skill-bench` to either work shape.

## Provenance and transformation boundary

Each `*-mapping.json` is an explicit assignment-level sidecar. Intended assignments and order come only from the prospectively frozen `protocol.json#/cells`; completed outputs are never used to construct the assignment inventory. Native study rows supply attempted/service/environment/artifact/graded state only after that inventory is fixed. Every protocol, study report, available trial report, retained trace, retained output, adjudication, gate, and mapping transform is path- and SHA-256-locked. Parent bytes are not modified.

The sidecars declare the mapping-transform hash, mapping-rule hash, public exclusion basis, no-retry/no-replacement policy, stop semantics, native locators, canonical dispositions, and exact intended → attempted → service-valid → environment-valid → artifact-valid → graded → scored totals. `validate.py` independently reconstructs those mappings from locked native records and invokes the existing gate.

A small backward-compatible repair in `../reconcile.py` admits an explicit `null` rate when there are zero valid scored rows. This was genuinely unrepresentable before this validation: the action-boundary adjudication invalidates its sole historical grade for capability aggregation. Numeric-rate behavior is unchanged.

## Retained reconciliation

| Campaign | Intended | Attempted | Service-valid | Environment-valid | Artifact-valid | Graded | Scored |
|---|---:|---:|---:|---:|---:|---:|---:|
| persistent-workspace-reuse v3 | 24 | 24 | 24 | 24 | 24 | 24 | 24 |
| action-boundary-composition v2 | 6 | 5 | 1 | 4 | 1 | 1 | 0 |

The v3 accounting and protocol both reconcile. The v2 accounting reconciles, but protocol conformance remains false: three post-stop launches exactly match the existing zero-call adjudication. The sole native grade remains preserved in its parent report but maps to `instrument_invalid`, not a pass/fail score, because the adjudication found an undisclosed grader-critical field. No invalid row is converted into agent failure.

## Verification

```bash
python pilots/trial-accounting-reconciliation/retained-campaign-validation-v1/validate.py --check-paths
python -m unittest tests.test_retained_campaign_trial_accounting -v
```

`--generate` is an audited maintenance operation that deterministically rewrites sidecars and reports after an intentional transform change. Normal verification does not rewrite files. Mutation tests reject dropped intended rows, complete-case denominator substitution, duplicate canonical attempts, hidden post-stop launches, retry/replacement laundering, invalid rows scored as failures, unjustified exclusions, and parent/transform hash drift.

## Claim boundary

Passing reports establish only deterministic, exhaustive accounting transfer for these two retained campaigns and detection of the planted mutations. They make no agent-capability, treatment-effect, reliability, expert/professional-validity, production, safety, cross-domain, or readiness claim.
