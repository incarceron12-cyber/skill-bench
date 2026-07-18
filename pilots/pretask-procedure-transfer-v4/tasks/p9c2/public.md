# Batch decision p9c2

## Objective
Determine the release disposition for every supplied batch at review hour 60.

## Inputs
Batch Q3 requires seals amber and green. Observations: r1 unsigned_note amber intact hour 51; r2 signed_scan amber intact hour 49; r3 signed_scan green intact hour 55.

## Deliverable
Write `outputs/result.json` with `task_id` and a `decisions` array. Each decision must contain `batch_id`, `disposition`, `reason`, `controlling_seals`, and `observation_ids`.

## Fair consequence basis
Every supplied batch must receive a release or quarantine disposition supported by the supplied custody observations.
