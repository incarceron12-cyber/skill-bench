# Internal synthetic controlled-vocabulary decision task

Read `source.json` and create `outputs/report.json` with exactly four keys: `decision`, `action`, `evidence_ids`, and `rationale`.

Use the record marked `controlling` when it is applicable to the stated rule. Exclude `outdated` and `advisory` records. `evidence_ids` must contain exactly the controlling record ID. Explain the exclusion using at least one of these disclosed concepts: `lower-rank`, `outdated`, `advisory`, `scope`, or `controlling`.

For this form, choose `decision` from: `closed`, `resolved`, `no_open_discrepancy`.
Choose `action` from: `archive_with_audit_trail`, `retain_evidence_and_close`, `close_case_preserving_records`.
Every listed value in each field is an accepted equivalent. Values not listed are invalid. Do not access external sources.
