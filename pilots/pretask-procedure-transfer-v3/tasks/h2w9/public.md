# Capacity packet H

## Objective
Allocate the available units among the listed requests and explain every funded, declined, or excluded outcome.

## Inputs
Opening capacity is 18 units. Six units are protected for requests in pool P until all eligible P requests have been considered.

| Request | Eligible | Priority | Submitted sequence | Quantity | Pool |
|---|---:|---:|---:|---:|---|
| U14 | yes | 5 | 2 | 7 | general |
| U09 | yes | 5 | 1 | 6 | P |
| U22 | no | 9 | 1 | 4 | general |
| U31 | yes | 4 | 3 | 5 | general |
| U07 | yes | 4 | 2 | 6 | P |

## Deliverable
Write `allocation.md` with a row for every request, the processing order, full quantity, outcome, reason, pool effect, and a reconciliation of opening capacity to funded, protected, and unassigned residual units.

## Fair consequence basis
Only eligible requests may receive units. Process eligible requests by priority and a deterministic tie-break using the supplied ordering fields. Requests are indivisible and cannot consume capacity protected for an applicable pool. The totals and residuals must reconcile exactly.
