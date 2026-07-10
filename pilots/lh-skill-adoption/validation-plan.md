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

The original attempted genuine execution did not pass the environment gate. The
retained traces in `ablation/agent-attempts-20260710/` show that the file-tool
root remained `/home/sam`, exposing repository graders, calibration fixtures,
and treatment-adjacent files despite temporary launch directories. The
deterministic audit therefore keeps every original attempt invalid and every
capability/treatment flag false.

A replacement bubblewrap launcher now passes zero-model-call canaries in both
conditions (`ablation/launcher-canaries/*/canary-report.json`). Through the
actual Hermes read/search/write implementations, they observe `/trial` as cwd,
read only the pinned source pack and assigned condition Skill, deny all probed
repository/rubric/calibration paths, deny writes outside `outputs/`, and find no
`skill-bench` path under the isolated home. The launcher exposes only the file
toolset and deletes ephemeral copied credentials after each probe.

The first post-canary `chat --query` retries are retained under
`ablation/isolated-agent-pair-v4/` and `isolated-agent-pair-v5/`. They exposed a
measurement-interface defect in addition to intermittent provider streaming:
Hermes documents `--usage-file` as one-shot-only, so a successful v5
public-skill execution wrote deliverables but no usage record and remained
incomplete. The launcher now uses the tested `-z` one-shot interface; this is a
measurement fix, not a weakened completion gate.

The resulting pinned v6 attempt is summarized with hashes and interpretation
boundaries in `ablation/isolated-agent-pair-v6/pair-summary.json`. Both
filesystem preflights passed. The no-skill arm recorded usage failure after
three OpenAI Codex stream retries and produced no deliverables. The public-skill
arm completed with all deliverables and included usage (57,404 total tokens,
seven API calls, included cost reported as $0.00). Post-hoc grading rejected its
evidence-provenance convention but passed contradiction-reconciliation and
causal-claim-strength. The live output also exposed and fixed two grader defects:
comma-grouped citations such as `[E01, E02]` were not parsed, and unbounded
`prove` regexes falsely matched `improves`; ordered-list numbers are now excluded
from numeric claims. Tests preserve all three regressions.

Because the no-skill arm is incomplete, `condition_effect_permitted=false`.
No expert-validity or release gate changed. A fresh matched pair under one
updated launcher hash remains required when provider streaming succeeds; then
rerun both post-hoc graders and assess comparability without weakening the
stream, evidence, or expert-validation gates. Raw request dumps are excluded
because they can contain authorization headers; retained evidence is limited to
redacted transcripts/stderr, usage, deliverables, canaries, and hashes.
