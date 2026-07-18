# Capacity packet C

## Objective
Produce an auditable assignment of a fixed slot budget to the submitted work bundles.

## Inputs
Opening capacity is 15 slots. Five slots are protected for pool R until eligible R bundles have been considered.

| Bundle | Eligible | Priority | Submitted sequence | Quantity | Pool |
|---|---:|---:|---:|---:|---|
| B03 | yes | 8 | 4 | 8 | general |
| B18 | yes | 8 | 4 | 5 | R |
| B11 | yes | 7 | 2 | 4 | general |
| B27 | yes | 6 | 1 | 5 | R |
| B05 | no | 10 | 1 | 3 | general |

## Deliverable
Write `assignment.md` containing each bundle's eligibility, rank, requested quantity, complete outcome, reason, affected pool, and a closing equation for funded, protected, and unassigned slots.

## Fair consequence basis
Exclude ineligible bundles with a reason. Rank the remainder by priority and resolve ties deterministically from the supplied sequence and identifier. Fund only complete bundles that fit the total and protected-pool limits. Account for every opening slot in the closing equation.
