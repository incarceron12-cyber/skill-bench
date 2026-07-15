# Internal synthetic controlled-vocabulary decision task

Read `source.json` and create `outputs/report.json` with exactly four keys: `decision`, `action`, `evidence_ids`, and `rationale`.

Use the record marked `controlling` when it is applicable to the stated rule. Exclude `outdated` and `advisory` records. `evidence_ids` must contain exactly the controlling record ID. Explain the exclusion using at least one of these disclosed concepts: `lower-rank`, `outdated`, `advisory`, `scope`, or `controlling`.

For this form, choose `decision` from: `correction_required`, `repair_needed`, `unresolved_duplicate`.
Choose `action` from: `reverse_duplicate_and_reconcile`, `remove_extra_entry_then_balance`, `correct_duplicate_and_verify_total`.
Every listed value in each field is an accepted equivalent. Values not listed are invalid. Do not access external sources.
