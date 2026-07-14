# Vendor incident state

Read `source-pack.json`. Write `outputs/decision.json` with exactly these keys: `effective_status_id`, `action`, `new_state`, `trusted_evidence_ids`, `rejected_evidence_ids`, and `rationale`.

Applicable signed status records supersede lower sequence numbers. Unsigned requests cannot override signed status. If the effective signed status is `contained`, preserve the lock, set state to `monitoring`, and do not reopen access. Reconcile every supplied record.
