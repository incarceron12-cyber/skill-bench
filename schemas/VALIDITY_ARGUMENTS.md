# Claim-centered validity argument contract v0.1

`validity-argument.schema.json` and
`scripts/validate_validity_arguments.py` implement the bridge from immutable
instruments and measurements to a bounded interpretation or use:

```text
instrument version + measurement → warrant / assumptions / rebuttals
                                 → five facet ledgers
                                 → bounded claim status → reassessment
```

This is cross-domain measurement infrastructure. It deliberately does **not**
assign one validity score to a benchmark, infer professional capability from a
passing check, or turn internal fixtures into expert validation.

## Enforced boundaries

1. **Immutable basis.** Every argument identifies versioned, SHA-256-bound task,
   bundle, grader, harness, environment, trial, measurement, adjudication, or
   impact artifacts. Optional `--check-paths` verifies both path and content.
2. **One claim per argument.** Criterion, construct, and decision objects carry
   their own intended interpretation/use, stakeholders, excluded
   interpretations, evaluation context, and generalization boundary.
3. **Facet ledgers, not a scalar.** Content, criterion, construct, external, and
   consequential evidence appear exactly once with separate requirement,
   status, scoped evidence, unknowns, and rationale. A supported claim cannot
   retain an unsupported required facet.
4. **Inferential distance is executable.** A supported/provisional construct
   claim needs mediating constructs and evidence-linked nomological links. A
   decision claim cannot bypass consequential validity and a supported decision
   needs empirical-loss or expert-standard-setting threshold evidence.
5. **Counterargument preservation.** Supported claims cannot retain contested,
   untested, or rejected assumptions or open rebuttals. Narrowing a claim is
   valid; deleting the objection is not.
6. **Facet-specific expert authority.** An expert-review evidence record may
   address exactly one facet. This prevents one generic
   `expert_validity_review=passed` observation from licensing content coverage,
   construct interpretation, transfer, and deployment simultaneously.
7. **Claim-scoped evidence and expiry.** Evidence declares its facet and claim
   scope. Owners, independent-review references, reassessment triggers, and a
   review-by date keep the argument revisable rather than permanently valid.

## Calibration fixture and claim ladder

`tests/fixtures/valid-validity-arguments.json` applies the contract to the LH
adoption pilot without upgrading its evidence:

| Rung | Status | Licensed interpretation |
|---|---|---|
| Exact planted-fixture outcome regression | `supported` | The pinned deterministic implementations emit the recorded outcomes on exactly four named builder-authored fixtures. |
| Evidence-grounded professional capability | `unsupported` | No valid matched agent population, construct network, expert criterion, or transfer study exists. |
| Deployment readiness | `unsupported` | No deployment population, impact evidence, loss model, affected-stakeholder risk tolerance, or licensed threshold exists. |

The underlying measurement is
`tests/fixtures/lh-planted-grader-calibration-measurement.json`. A test reruns
both deterministic graders over all four calibration cases and requires exact
outcome equality. That execution supports only the narrow criterion claim. The
fixtures were authored with the internal graders, so the measurement is not an
accuracy, precision/recall, reliability, professional-validity, skill-effect,
or readiness study.

## Design rationale and provenance

| Choice | Rationale | Evidence |
|---|---|---|
| Claim–evidence relation rather than globally “valid benchmark” | The same measurement can support a narrow criterion claim while failing broader construct claims. | `papers/agent-benchmarks/2026-07-10-validity-centered-ai-evaluation.md`, §§ Unique insight and Transferable design patterns 1–2 |
| Five separate evidence ledgers | Facets answer different challenges and should not be averaged into an uncalibrated score. | same review, Transferable design pattern 3 and Limitations 2–3 |
| Explicit warrant, assumptions, and rebuttals | The reviewed framework names claim/object/evidence but does not formally preserve the inference bridge or alternatives; this is a skill-bench adaptation. | same review, Limitations 8 |
| Construct network requirement | Latent capability claims need convergent/discriminant relationships rather than adjacent labels or more checklist items. | same review, GPQA case and Limitations 7 |
| Decision threshold and loss basis | Correct score computation does not establish acceptable asymmetric downstream loss. | same review, Transferable design pattern 5 |
| Facet-specific expert evidence | The LH pilot's generic expert-validity gate could otherwise launder one approval across distinct claims. | same review, Concrete change 3; `pilots/lh-skill-adoption/validation-plan.md` |

The reviewed paper is a conceptual synthesis, not empirical validation of this
schema. It reports no inter-rater study of its report cards or prospective
organizational use. The contract therefore remains an executable project
hypothesis requiring later independent-review and decision studies across
meaningfully different domains.

## Validate

```bash
python scripts/validate_validity_arguments.py --check-paths \
  tests/fixtures/valid-validity-arguments.json
python -m unittest tests.test_validate_validity_arguments -v
```
