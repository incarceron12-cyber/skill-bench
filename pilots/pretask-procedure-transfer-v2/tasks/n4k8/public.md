# Decision packet N4K8

## Objective
Recommend **proceed** or **hold** for the synthetic East expansion decision as of 2026-07-18T08:30:00Z.

## Inputs
- R21 — issuer: expansion owner; scope: East expansion; valid through 2026-07-31; supports proceed; signed.
- R22 — issuer: risk owner; scope: East expansion; valid through 2026-07-31; blocks proceed pending a load test; signed.
- R23 — issuer: risk owner; scope: East support staffing; valid through 2026-07-31; says staffing risk cleared; signed; issued after R22.
- R24 — issuer: finance owner; scope: East expansion; expired 2026-06-30; supports proceed; signed.

## Deliverable
Write `decision.md` containing one recommendation, concise rationale, a row for every supplied record with eligibility/role/effect, and any minimum evidence needed to resolve a hold.

## Fair consequence basis
The recommendation must use only records whose stated issuer, scope, signature, and validity support their use for this decision. A newer record resolves an earlier conflict only when it addresses the same subject and scope. Conflicting or excluded records must remain visible. Proceed requires sufficient independent support and no unresolved applicable blocker; otherwise hold and state what would resolve it.
