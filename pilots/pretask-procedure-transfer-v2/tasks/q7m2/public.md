# Decision packet Q7M2

## Objective
Recommend **proceed** or **hold** for the synthetic North renewal decision as of 2026-07-18T08:30:00Z.

## Inputs
- R11 — issuer: portfolio owner; scope: North renewal; valid through 2026-07-31; supports proceed; signed.
- R12 — issuer: finance delegate; scope: North renewal; valid through 2026-07-31; supports proceed; signed; independent of R11.
- R13 — issuer: portfolio owner; scope: South renewal; valid through 2026-07-31; blocks proceed; signed.
- R14 — issuer: observer; scope: North renewal; valid through 2026-07-31; blocks proceed; unsigned.

## Deliverable
Write `decision.md` containing one recommendation, concise rationale, a row for every supplied record with eligibility/role/effect, and any minimum evidence needed to resolve a hold.

## Fair consequence basis
The recommendation must use only records whose stated issuer, scope, signature, and validity support their use for this decision. Conflicting or excluded records must remain visible rather than be silently dropped. Proceed requires sufficient independent support and no unresolved applicable blocker; otherwise hold and state what would resolve it.
