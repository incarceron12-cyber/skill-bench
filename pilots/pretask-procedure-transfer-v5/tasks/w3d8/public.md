# Procedure-transfer task w3d8

## Objective
Replay the journal and determine its certified terminal state.

## Inputs
The complete public task input is `input.json`. All identifiers that may be required in the result are disclosed there.

## Deliverable
Write `outputs/result.json` as one JSON object using exactly these public field types:

```json
{
  "committed_transactions": "array<string transaction_id>",
  "final_state": "object or null",
  "journal_id": "string",
  "reason": "non-empty string; wording is not scored",
  "rolled_back_transactions": "array<string transaction_id>",
  "task_id": "string",
  "valid": "boolean"
}
```

`reason` must be a non-empty explanation, but its wording is not scored. Array order is significant for committed and rolled-back transaction chronology; `observation_ids` is compared as a set. No undisclosed identifier or representation is required.

## Fair consequence basis
Apply the supplied family source rules to every event in ascending seq order.
The private checker may enforce only the disclosed types, identifiers, and semantic consequences of those public inputs and source rules.
