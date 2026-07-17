# Analytical incident assessment

Read `source-pack.json`. Produce exactly one file, `outputs/analysis.json`, containing a JSON object with these fields:

- `observation_source_ids`: source IDs supporting the descriptive anomaly;
- `primary_hypothesis`: a specific falsifiable candidate explanation;
- `primary_initial_status`: one of `plausible_unsupported`, `supported`, or `confirmed`;
- `rival_hypothesis`: a materially different rival;
- `selected_test_id`: one test from the public test menu;
- `predicted_discrimination`: what different outcomes would imply for candidate versus rival;
- `adopted_evidence_ids`: source IDs used in the update;
- `updated_primary_status`: one of `rejected`, `plausible_unsupported`, `supported`, or `confirmed`;
- `updated_rival_status`: one of `rejected`, `plausible_unsupported`, `supported`, or `confirmed`;
- `bounded_conclusion`: a conclusion whose scope matches the supplied records;
- `residual_uncertainty`: a concrete unresolved alternative or evidence gap;
- `recommended_consequence`: a proportionate action, abstention, or escalation.

Do not claim that you executed a test: the harness will independently execute your selected public test after submission. Do not infer policy authority not present in the source pack. Use only disclosed sources. This is an internal synthetic assessment, not professional advice.
