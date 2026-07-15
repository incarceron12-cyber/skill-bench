# Internal synthetic controlled-vocabulary decision task

Read `source.json` and create `outputs/report.json` with exactly four keys: `decision`, `action`, `evidence_ids`, and `rationale`.

Use the record marked `controlling` when it is applicable to the stated rule. Exclude `outdated` and `advisory` records. `evidence_ids` must contain exactly the controlling record ID. Explain the exclusion using at least one of these disclosed concepts: `lower-rank`, `outdated`, `advisory`, `scope`, or `controlling`.

For this form, choose `decision` from: `defer`, `postpone`, `not_ready`.
Choose `action` from: `add_capacity_then_reassess`, `increase_resources_and_review`, `close_gap_before_review`.
Every listed value in each field is an accepted equivalent. Values not listed are invalid. Do not access external sources.
