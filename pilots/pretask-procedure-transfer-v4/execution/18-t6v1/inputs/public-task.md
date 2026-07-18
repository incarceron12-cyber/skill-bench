# Journal replay t6v1

## Objective
Replay the supplied journal and determine its certified terminal state.

## Inputs
Events: seq 1 begin A; seq 2 set x=1; seq 3 begin B; seq 4 set x=2; seq 5 rollback B; seq 6 commit A.

## Deliverable
Write `outputs/result.json` with `task_id`, `journal_id`, `valid`, `final_state`, `committed_transactions`, `rolled_back_transactions`, and `reason`.

## Fair consequence basis
The result must account for every supplied event and must not certify mutations discarded by rollback.
