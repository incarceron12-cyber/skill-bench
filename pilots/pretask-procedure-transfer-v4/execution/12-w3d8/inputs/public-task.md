# Journal replay w3d8

## Objective
Replay the supplied journal and determine its certified terminal state.

## Inputs
Events are listed out of order: seq 4 commit C; seq 1 begin C; seq 3 set mode=ready; seq 2 set count=2; seq 5 begin D.

## Deliverable
Write `outputs/result.json` with `task_id`, `journal_id`, `valid`, `final_state`, `committed_transactions`, `rolled_back_transactions`, and `reason`.

## Fair consequence basis
The result must account for every supplied event and must not certify a terminal state while a transaction remains open.
