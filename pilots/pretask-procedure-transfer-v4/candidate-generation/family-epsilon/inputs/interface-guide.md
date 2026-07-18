# Source-only procedure-package serialization guide

Produce exactly one JSON object conforming to `procedure-generation-output.schema.json`.

## Representation rules

1. `package_id` is a nonempty lowercase identifier. Never use `null`.
2. `proposition_bindings` and `clauses` are reciprocal: each binding lists exactly the clauses whose `proposition_basis` contains that proposition.
3. Every contradiction, decision threshold, artifact convention, and failure signature in the source must appear exactly once in its matching output array or exactly once in `omissions` under its singular `source_kind`.
4. Every projected primitive has exactly four fields: `item_id`, `source_object_id`, `proposition_basis`, and `content`.
5. **`content` is always one JSON string, never an object or array.** If a source primitive contains structured fields, serialize their meaning into a concise sentence. For example: `"Deliverable: review register. Required fields: item_id, state, reason."`
6. `proposition_basis` exactly copies the source primitive's `propositions` or `basis` array.
7. Do not add task text, checks, endpoints, answers, or professional claims. All seven claim-ceiling values remain `false`.
8. Return no prose, markdown fence, or second file. Write only `outputs/package.json`.

The adjacent example demonstrates shape and typing only. It is not authority for the case corpus and its identifiers or content must not be copied into the case output.
