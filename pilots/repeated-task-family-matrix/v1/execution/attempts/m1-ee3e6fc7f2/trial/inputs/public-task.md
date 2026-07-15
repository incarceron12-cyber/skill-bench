# Internal synthetic decision task

Read `source.json`. Create `outputs/report.json` containing exactly these keys: `decision`, `action`, `evidence_ids`, and `rationale`. Use the current highest-authority applicable record; reject superseded or untrusted records. `evidence_ids` must list only the authoritative record(s) supporting the decision. The rationale must state why conflicting evidence was excluded. Do not access external sources.
