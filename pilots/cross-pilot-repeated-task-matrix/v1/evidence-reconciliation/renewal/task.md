# Renewal evidence reconciliation

Read `source-pack.json`. Write `outputs/decision.json` with exactly these keys: `decision`, `threshold_result`, `trusted_evidence_ids`, `rejected_evidence_ids`, and `rationale`.

Use only records whose scope is `renewal_population` and authority is `audited_measurement` for the primary threshold. Renewal is allowed only when the trusted lower bound is at least 0.08 and no trusted severe adverse signal is present. Reconcile every supplied record; newer presentation dates do not override authority or scope.
