# Batch decision k4n7

## Objective
Determine the release disposition for every supplied batch at review hour 100.

## Inputs
Batch L8 requires seals red and blue. Observations: o1 signed_scan red intact hour 90; o2 unsigned_note red broken hour 95; o3 signed_scan blue intact hour 80.

## Deliverable
Write `outputs/result.json` with `task_id` and a `decisions` array. Each decision must contain `batch_id`, `disposition`, `reason`, `controlling_seals`, and `observation_ids`.

## Fair consequence basis
Every supplied batch must receive a release or quarantine disposition supported by the supplied custody observations.
