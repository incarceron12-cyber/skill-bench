# Expert participation and authority-lineage contract v0.1

`expert-participation.schema.json` and `scripts/validate_expert_participation.py`
provide a separate governance layer linked to expertise-transfer contributors.
The contract answers who contributed which bounded unit, for which authorized
purpose, through which transformations, with what reciprocal exchange and
review authority. It does not replace elicitation, task, rubric, or validity
contracts.

## Enforced boundaries

1. **Purpose-specific consent.** Contribution and transformation purposes must
   be allowed and not prohibited by the referenced consent version. Allowed
   operations, comprehension evidence, attribution/license, compensation,
   reciprocal output, withdrawal limits, and reconsent triggers remain explicit.
2. **Provenance is not approval.** A material builder/model/script transform may
   preserve source lineage, but an `expert_approved`/`expert_edited` output
   requires an approved post-transformation review by a domain expert. Synthetic
   derivatives cannot silently inherit their parent's authority state.
3. **Substitution needs held-out evidence.** An approved delegation from expert
   application to a builder, model, or script requires an approved, held-out
   application-fidelity review by a domain expert. Workshop exposure or developer
   confidence is not enough.
4. **Decision rights are scoped.** Author, review, veto, transformation approval,
   release-claim approval, and withdrawal rights are represented separately.
5. **Claims fail closed.** A release expert-grounding claim may name only artifacts
   whose current authority state is expert-authored, expert-edited, or
   expert-approved. Internal schema fixtures cannot license that claim.
6. **No scalar participation score.** The record preserves consent, agency,
   reciprocal value, labor, fidelity, and authority as distinct objects.

## Calibration fixture

`tests/fixtures/valid-expert-participation.json` links by SHA-256 to the existing
expertise-transfer fixture and the full-source participation review. It contains
only a builder and research-review record, uses explicit
`not_applicable_internal_fixture` states, and makes no claim about real consent,
expertise, motivation, comprehension, reciprocity, professional fidelity, or
release validity. Mutation tests construct hypothetical records solely to prove
rejection of:

- synthetic artifacts inheriting expert approval;
- evaluation-only material drifting into training without reconsent;
- developer substitution without held-out expert-fidelity evidence; and
- expert-grounding claims over internal/unreviewed artifacts.

## Design rationale and provenance

| Choice | Rationale | Evidence |
|---|---|---|
| Separate participation lifecycle linked to contributors | The existing expertise-transfer contributor record cannot express evolving use, ownership, reciprocal exchange, transformations, or authority decay. | `papers/agent-benchmarks/2026-07-10-domain-expert-participation-ethnography.md`, Concrete changes 1–3 |
| Versioned purpose and transformation authorization | One-time procedural consent did not resolve contributors' uncertainty about downstream reuse. | same review, Evidence and strength of support; Transferable design pattern 1 |
| Approval does not propagate | The observed chain moved from expert dialogue to unreviewed synthetic data, developer judgment, and model judging without evidence that fidelity survived. | same review, Unique insight; Limitations 7–10 |
| Held-out fidelity before authority delegation | Developers believed workshops enabled expert substitution, but no agreement/fidelity evidence was reported and judge tuning risked circularity. | same review, Observed development sequence 6–7; Unique insight |
| Explicit reciprocal outputs and decision rights | Motivation, trust, learning, influence, fatigue, and concern about displacement can affect who participates and what expertise is captured. | same review, Observed evidence; Transferable design patterns 2–3 |

These choices are project adaptations motivated by one 12-week, compensated,
single-institution ethnography. The paper did not evaluate this contract or a
free/near-zero-cost workflow. Real usefulness requires consented contributors
across domains, observed comprehension, actual reconsent/withdrawal behavior,
expert time and dropout, transformation fidelity, and claim-blocking outcomes.

## Validate

```bash
python scripts/validate_expert_participation.py --check-paths \
  tests/fixtures/valid-expert-participation.json
python -m unittest tests.test_validate_expert_participation -v
```
