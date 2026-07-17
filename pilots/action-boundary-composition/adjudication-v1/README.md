# Action-boundary composition v1/v2 defect adjudication

This additive, zero-call package preserves `pilots/action-boundary-composition/v1`
and `v2` byte-for-byte. It advances charter objectives C and D by turning two
observed failures into reusable pre-execution checks rather than another model
replication.

## Decisions

1. **Public-interface defect.** The frozen public task asks for an “effect event”
but supplies no normative output schema and never discloses the grader-critical
`event_type` key. The sole service-valid artifact records the semantically clear
`{"event": "effect", ...}` form; the frozen grader accepts only
`event_type == "effect"`. The historical fail and `exact_execution=false` score
remain immutable, but that exact-execution label is excluded from capability
evidence. This is an instrument-interface defect, not evidence that the model
did not attempt the requested synthetic effect.
2. **Campaign-control defect.** The frozen runner constructs all rows in a list
comprehension and has no stop gate. After service invalidity at order 2, orders
3, 4, and 5 were launched. They remain intention-to-evaluate rows and retained
invalid protocol deviations; order 6 remains not launched. No row is deleted,
retried, substituted, or regraded.
3. **Replacement requirements only.** `replacement-public-contract-requirements.json`
is a normative-schema requirement for any future distinct instrument. It is not
v3, a repaired historical grader, or permission to rerun v1/v2. A replacement
must disclose every grader-critical path/type or predeclare a reviewed semantic
alias policy, and its launcher must stop before the next row after service or
environment invalidity while finalizing interruption and all remaining ITT rows.

`replay_adjudication.py` verifies exact retained hashes, reconstructs both defect
findings, exercises the reusable validator, and reproduces
`adjudication-report.json`. `tests/test_action_boundary_interface_campaign.py`
plants undisclosed-name/type, unreviewed alias, missing schema, post-stop launch,
denominator deletion, retry, and timeout/interruption-finalization mutations.

This package licenses no capability, treatment-effect, expert/professional
validity, safety, production, readiness, or cross-domain claim.
