# Incident stream V8R1

## Objective
Determine the current synthetic data-service state and choose **contain**, **restore**, or **monitor** as of sequence 24.

## Inputs
- E21 — component: ingest; sequence: 21; issuer: ingest owner; signed; state: degraded; impact: medium; blast radius: bounded.
- E22 — component: storage; sequence: 22; issuer: storage owner; signed; state: healthy; impact: low.
- E23 — component: ingest; sequence: 23; issuer: ingest owner; signed; state: healthy; impact: low; verification: backlog drained.
- E24 — component: storage; sequence: 24; issuer: observer; unsigned; state: degraded; impact: high.

## Deliverable
Write `action.md` with the chosen bounded action, current component state, a row for every event showing acceptance and before/after state, and a verification condition.

## Fair consequence basis
Only signed events from the stated component owner may establish component state; other events remain visible observations. Sequence updates apply within a component, not across components. Choose the least disruptive authorized action when no high-impact unresolved degradation remains. Every event and state transition must be auditable.
