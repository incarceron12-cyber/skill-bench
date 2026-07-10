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

The deterministic `evidence-provenance` slice classifies all four planted artifacts as intended. An independently versioned internal rubric and calibrator also make the two private boundaries executable: the cautious fixture passes both; agreement-overclaim fails contradiction reconciliation; tiny-ablation-overclaim fails causal scope and claim strength. This is fixture classification, not population precision/recall or expert validity. The rubric was implemented independently from pinned evidence but was not blindly authored by an independent human.

The task-only preflight now materializes and validates all four matched conditions with pinned task, skill, rubric, tool, harness, feedback-policy, artifact, and grader-result hashes. It replays one identical builder-authored fixture, not an agent output; therefore `capability_evidence=false` and it cannot estimate either treatment effect. Shared-rubric human checks remain explicitly unexecuted.

The first attempted genuine execution did not pass the environment gate. The
retained traces in `ablation/agent-attempts-20260710/` show that the file-tool
root remained `/home/sam`, exposing repository graders, calibration fixtures,
and treatment-adjacent files despite temporary launch directories. The
concurrent pair also collided in one output directory. The deterministic audit
therefore keeps every attempt invalid and every capability/treatment flag
false. Before another paid/model-backed run, a launcher must prove with a
canary that (a) cwd is task-scoped, (b) only the declared source pack plus the
condition's skill is visible, (c) outputs resolve inside a unique trial root,
and (d) the agent cannot discover repository rubric/calibration files. Only
then should fresh matched execution and qualified human adjudication proceed.
