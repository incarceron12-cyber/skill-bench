# Validation plan

The pilot is structurally valid but **not releasable and not expert-valid**. Schema validation cannot close these gates.

## Gate sequence

1. **Source audit:** independently compare every `decision-evidence.csv` row with the local full-text extraction/PDF and review; correct transcription or scope errors.
2. **Procedure validity:** at least two benchmark-evaluation experts independently assess both candidate procedures, identify missing valid routes, and adjudicate material disagreements.
3. **Rubric review:** a reviewer who did not author `public-skill.md` checks that each private consequence follows from a public requirement and that no exact private boundary leaked.
4. **Dry runs:** execute at least two agents on the no-skill and public-skill conditions using a rubric independently authored from the source evidence; log invalid environment runs separately.
5. **Failure-signature test:** include outputs intentionally exhibiting (a) aggregate-agreement overclaim and (b) seven-run causal overclaim; require the checks to fail while a cautious, fully sourced alternative passes.
6. **Human calibration:** experts independently label accept/reject readiness and pairwise preference; report disagreement rather than inferring validity from automated agreement.
7. **Ablation continuation:** only after the static dry run, instantiate matched no-skill/public-skill × independent/shared-rubric bundles with pinned task, grader, harness, tool, and feedback hashes.

## Observable release evidence

- all source rows audited with immutable locators;
- two procedures accepted/revised by experts with identities/consent scoped appropriately;
- private/public boundary review passed;
- grader precision/recall reported on planted failures;
- matched-condition trial traces and artifacts retained;
- expert threshold disagreement and adjudication retained;
- expertise-transfer `pilot_validation` and `release_review` gates passed.

Until then, `expert_validity_review` is `failed`, release status is `not_ready`, and any use is internal contract testing only.

## Current internal-calibration evidence

The deterministic `evidence-provenance` slice now classifies all four planted artifacts as intended: one cautious fixture passes; agreement-overclaim, tiny-ablation-overclaim, and malformed-source fixtures fail with coded diagnostics. This exercises provenance preservation only. It does **not** satisfy gate 5 for the private contradiction/causal checks, report population precision/recall, supply an independent rubric, or create agent dry runs. Those remain the next bounded continuation before any expert or release gate can advance.
