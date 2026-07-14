# Adoption evidence reconciliation

Read `source-pack.json`. Write `outputs/decision.json` with exactly these keys: `decision`, `threshold_result`, `trusted_evidence_ids`, `rejected_evidence_ids`, and `rationale`.

Use only records whose scope is `all_teams` and authority is `controlled_measurement` for the primary threshold. Adoption is allowed only when the trusted lower bound is at least 0.10 and no trusted severe adverse signal is present. Reconcile every supplied record; do not treat a summary or out-of-scope subgroup as primary evidence.
