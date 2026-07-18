# Incident stream Z3P6

## Objective
Determine the current synthetic service state and choose **contain**, **restore**, or **monitor** as of sequence 14.

## Inputs
- E11 — component: gateway; sequence: 11; issuer: gateway owner; signed; state: degraded; impact: high; blast radius: unresolved.
- E12 — component: worker; sequence: 12; issuer: worker owner; signed; state: healthy; impact: low.
- E13 — component: gateway; sequence: 13; issuer: observer; unsigned; state: healthy; impact: low.
- E14 — component: gateway; sequence: 14; issuer: gateway owner; signed; state: degraded; impact: high; blast radius: unresolved.

## Deliverable
Write `action.md` with the chosen bounded action, current component state, a row for every event showing acceptance and before/after state, and a verification condition.

## Fair consequence basis
Only signed events from the stated component owner may establish component state; other events remain visible observations. Sequence updates apply within a component, not across components. If a high-impact component is still degraded while blast radius is unresolved, protect the environment before attempting restoration. Every event and state transition must be auditable.
