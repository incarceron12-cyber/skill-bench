# Procedure-transfer task k4n7

## Objective
Determine every batch release disposition.

## Inputs
The complete public task input is `input.json`. All identifiers that may be required in the result are disclosed there.

## Deliverable
Write `outputs/result.json` as one JSON object using exactly these public field types:

```json
{
  "decisions": "array<object>",
  "decisions[].batch_id": "string",
  "decisions[].controlling_seals": "object<string,string observation_id>",
  "decisions[].disposition": "string enum[release,quarantine]",
  "decisions[].observation_ids": "array<string observation_id>",
  "decisions[].reason": "non-empty string; wording is not scored",
  "task_id": "string"
}
```

`reason` must be a non-empty explanation, but its wording is not scored. Array order is significant for committed and rolled-back transaction chronology; `observation_ids` is compared as a set. No undisclosed identifier or representation is required.

## Fair consequence basis
Apply the supplied family source rules to every batch and observation.
The private checker may enforce only the disclosed types, identifiers, and semantic consequences of those public inputs and source rules.
