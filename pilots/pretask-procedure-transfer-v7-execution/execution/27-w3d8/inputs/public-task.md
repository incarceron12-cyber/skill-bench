# Procedure-transfer task w3d8

## Objective
Apply the supplied family procedure to the complete public `input.json`.

## Deliverable
Write `outputs/result.json` as exactly one JSON object with this closed shape:

```text
{
  "task_id": string,
  "journal_id": string,
  "valid": boolean,
  "final_state": object | null,
  "committed_transactions": [string transaction_id],
  "rolled_back_transactions": [string transaction_id],
  "reason": non-empty string
}
```

No additional key is permitted at any object level. Repeated JSON keys, `condition_id`, treatment metadata, and uncontracted payloads are invalid. `reason` wording is not scored. Transaction arrays are chronological and ordered.

## Exact JSON policy
Booleans, null, strings, arrays, objects, integer-form numbers, and decimal/exponent-form numbers are distinct. In particular, `true` is not `1`, `false` is not `0`, and `1` is not `1.0`. Object key order and JSON whitespace are not semantic. Non-finite numbers are invalid.

## Fair consequence basis
All identifiers and values needed for the result are in `input.json`; the assigned procedure material supplies the applicable family rules. The checker may enforce only this disclosed contract and consequences of those inputs and rules.
