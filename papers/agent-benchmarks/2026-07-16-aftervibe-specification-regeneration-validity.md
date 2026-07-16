# AfterVibe: regeneration tests behavioral reconstruction, not authoritative intent or handoff readiness

## Source and evidence status

**Deep review of the complete immutable primary source.** I read the full 27-page arXiv v1 paper, including all eight appendix prompts, and checked the extraction against the local PDF.

- **Paper:** Matteo Paltenghi and Satish Chandra, *AfterVibe: What Remains When the Conversation Ends*
- **Immutable version:** https://arxiv.org/abs/2607.09900v1 (submitted 10 July 2026)
- **Date read:** 2026-07-16 UTC
- **Local PDF:** `data/papers/pdfs/2607.09900v1-aftervibe.pdf` (27 pages; SHA-256 `e03e0b9bfa90468bd8a914ad47cb7c7d8ca801fef6c54caaa76d6e7999a19e5a`)
- **Local text:** `data/papers/text/2607.09900v1-aftervibe.txt` (106,297 bytes; SHA-256 `38c77892cd46ee520203a91b37c84fb91d8e32b17e2740e6a8735f22a8f8ab29`)
- **Metadata:** `data/papers/source/2607.09900v1-metadata.xml`
- **Index:** `data/papers/index.json`
- **Release status at review time:** the Data Availability statement releases the prompt suite through the paper appendix but says no human vibe-coding trajectory dataset with execution environments is openly available (p. 15). The paper contains no project, code, data, or supplementary-package URL. Exact-title, arXiv-ID, author/official-surface web searches and GitHub repository API searches found no verifiable author-owned release. No task records, trajectories, diffs, specs, regenerations, grader traces, per-run scores, analysis code, environments, or paper-time implementation were available for inspection.
- **Tags:** specification recovery, trajectory projection, regeneration, recipient testing, co-derived oracles, best-of-k, handoff validity

> **Timing boundary.** “No release found” means no paper-associated empirical release was linked or locatable on 2026-07-16 UTC. A later release would need a separate immutable revision and paper-correspondence audit.

## One-sentence contribution

AfterVibe introduces a strong **recipient-action falsification pattern**—distill a natural-language specification from a completed conversation and diff, then ask a fresh agent to reimplement from the specification—but its private, outcome-filtered frame; shared source/model lineage; reference-aware graders; same-oracle refinement and selection; weak diversity anchors; and absent human recipient, lifecycle, cost, and release evidence mean the reported scores establish bounded same-repository behavioral reconstructability, not recovered authoritative intent, implementation equivalence, general handoff quality, reviewability, source-of-record fitness, or readiness.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, and C through a general cross-domain hypothesis:

> A durable work artifact should be tested through an independently configured recipient action, while source truth, behavioral sufficiency, artifact equivalence, recipient utility, lifecycle cost, and professional acceptance remain separate claims.

The output need not be code. It could be an incident runbook regenerated into a response plan, a research protocol into an executable analysis, a financial-model specification into a workbook, or a handoff brief into a resumed work state. AfterVibe is more informative than evaluating prose resemblance because a recipient must act. Its central weakness is equally transferable: when artifact, recipient task, oracle, refinement signal, and reference implementation all descend from the same completed episode, success can demonstrate **closed-loop reconstruction around one lineage** without establishing that the artifact recovered the principal's true requirements or will help an independent professional under a changed context.

This is narrow expansion, not a coding scope commitment. Existing task-projection, artifact-admissibility, handoff-usability, configured-system, task-health, metric, trace, and validity machinery can represent the repair; no coding-specific schema follows.

## Research question and defensible claim boundary

The paper asks whether a model can recover an abstract but sufficiently strong specification from the conversation and unified diff of a completed AI-assisted code change, whether verifier feedback can strengthen it, whether independent regenerations remain diverse, whether the graders discriminate selected wrong code, and whether the specification outperforms the developer's review description (Sections 1–4, pp. 1–13).

The strongest defensible empirical claim is:

> For 68 infrastructure-complete tasks selected from 72 oracle-passing sessions in one private monorepo frame, one undisclosed frontier-model pipeline produced specifications from conversation-plus-diff evidence that yielded a reported mean `regen_score` of 5.06/6 under same-base-repository regeneration and three co-lineaged graders; selected per-task maxima over up to three same-oracle refinement rounds raised the in-loop mean to 5.74.

The evidence does **not** establish that:

- the conversation and accepted diff fully or authoritatively express developer intent;
- regenerated code is extensionally equivalent outside the selected tests, verification clues, and model judge;
- abstraction rather than copied identifiers, repository affordances, model priors, or grader preference causes success;
- the method beats a length- and purpose-matched human-authored specification;
- refinement improves out-of-sample specification quality rather than optimizing one fixed oracle through repeated noisy attempts;
- a human reviewer can understand, verify, approve, maintain, or safely treat the result as source of record;
- a successor benefits under changed state, role, model, organization, or time;
- total lifecycle effort or review burden falls;
- the system is professionally valid, production-fit, safe, reliable, or ready.

## Methodology and system

### Source frame, selection, and missing clustering

The primary `TechInternal` frame begins with multi-turn sessions from a **seven-day window** in one large company monorepo. The curation funnel requires a completed landed diff, a nontrivial code change, and “sufficient conversation context,” yielding 122 candidates. Forty-one are then excluded because the evaluation sandbox or grader infrastructure does not return both flexible-test and verification-condition verdicts. Of the remaining 81, another nine are excluded because the landed, CI-passing change fails at least one extracted grader. The final frame is 72 sessions (Section 4.1.1, pp. 7–8).

Thus only 81/122 (66.4%) of curated candidates are infrastructure-complete and 72/122 (59.0%) enter the final evaluation. The paper usefully reports that excluded infrastructure cases have similar clue/test counts and session durations, and diagnoses four environment mismatches, three extraction failures, and two deleted-test edge cases among the nine oracle failures. But the selection is still **instrument-conditioned**: the measured construct is reconstructability among tasks for which this pipeline can first validate the reference.

The paper alternates among “projects,” “tasks,” and “sessions” without reporting the number of unique repositories/projects, developers, code areas, task families, or repeated contributors. In a monorepo, tasks may share libraries, conventions, tests, authors, model sessions, or ancestry. There is no lineage-cluster manifest, sampling probability, deduplication rule, task-mixture description, or cluster-aware uncertainty. Real internal demand is valuable ecological provenance; it is not a population frame for vibe coding, software work, or knowledge work.

### Evidence views and specification extraction

The source bundle contains the full conversation trajectory (user turns, tool calls, and messages), the final unified diff, metadata including the human review description, observed test commands, and the repository at the base commit. One prompt converts conversation plus diff into:

1. **Intent and Rationale**;
2. **Essential Design Decisions**;
3. **Undiscoverable Facts**; and
4. a declarative behavioral-requirements checklist.

The prompt forbids code, identifiers, paths, and line numbers unless “essential and undiscoverable,” and excludes test-writing instructions (Section 3.2, pp. 4–5; Prompt A.1, pp. 19–20). Dedicated prompts independently extract 5–15 provenance-tagged yes/no verification clues from conversation, metadata, diff, and test commands, and a 1–3-command test manifest from observed validation evidence (Prompts A.3–A.4, pp. 21–23).

This is a thoughtful artifact decomposition. In particular, the explicit `unsupported_by`/provenance fields and counterfactual test for over-specific clues are useful authoring patterns. But “whatever is observable from the session is a sufficient expression of the requirements” is an **assumption**, not a validated finding (Sections 1 and 3.1, pp. 2, 4). A completed session can omit rejected alternatives, unspoken constraints, downstream consumers, safety obligations, organizational conventions, stakeholder disagreement, or errors jointly accepted by developer and agent. The final diff is evidence of what landed, not automatically the principal's whole intent.

The spec and oracle are separated at the immediate text-output level, but not independently grounded: both are produced by the same undisclosed frontier model from overlapping conversation/diff evidence, while ground-truth alignment receives that source evidence directly. Shared extraction errors, model priors, implementation cues, and authoring assumptions can therefore make specification and grader agree. “Not derived from the spec” prevents the simplest circularity; it does not create independent authority or semantic truth.

A reproducibility-relevant ambiguity remains around tests. Prompt A.1 says test changes are already present in the working directory, while the method says the fresh regeneration begins at the same base commit and receives only the spec. The runtime wrapper tells the agent to focus on production code, and the flexible grader may inspect the reference patch (Prompts A.1, A.5–A.6, pp. 19, 23–24). The paper does not provide a filesystem manifest showing whether source-session tests, changed tests, reference diffs, private graders, or extracted VCs are visible to the regeneration agent. “Only the spec” describes conversational input, not a verified information-flow boundary.

### Blind regeneration and configured-system identity

A fresh model session receives the specification and generic implementation instructions, explores the repository at the same base commit, and edits code. It has no conversational access to the source diff or trajectory (Section 3.4, p. 6; Prompt A.5, p. 23). Separating extraction and implementation contexts is a meaningful blind-recipient control.

Blindness is nevertheless partial and recipient-relative. The repository itself contains naming, APIs, build graph, historical conventions, and possibly tests; the paper explicitly relies on this “environmental grounding hypothesis.” All LLM components use **one unnamed frontier model**: distillation, clue extraction, test extraction, regeneration, grader agents, and refinement (Section 4.2, p. 8). The paper omits model/version, provider, decoding parameters, context policy, harness/version, system prompts beyond the appendix task prompts, tool permissions, filesystem/network isolation, repository/environment hashes, retry/error policy, timeout/budget, and component-level usage. Distinct sessions stop direct context carryover, but do not test cross-model recipient transport or shared-model inductive dependence.

### Three-tier verifier and score topology

The score is:

`regen_score = 3 × flex + 2 × vc + align`,

where `flex` is the fraction of runnable extracted tests passing, `vc` is the fraction of evaluable verification clues satisfied, and `align` is a binary reference-alignment verdict (Section 3.3, pp. 5–6; Appendix A.2, pp. 24–27).

- **Flexible test execution** runs source-session commands and may adapt imports, symbols, module names, and signatures, but not assertions or expected values. It can inspect the reference patch to decide whether a missing test was intentionally removed.
- **Verification-condition checking** asks a repository-reading model agent to label each extracted clue pass/fail/skip from the regenerated change.
- **Ground-truth alignment** gives a model judge the task, spec, conversation, generated code, base repository, and reference patch, then asks for behavioral equivalence.

Plural evidence is preferable to one holistic judge, and the appendix makes the prompts unusually inspectable. Yet the score is an authored utility function rather than a validated scale. The three observations are dependent: they share source evidence, repository, model family, and often behavioral predicates. Weight sensitivity preserves the AfterVibe/human ordering, but does not establish calibration, interval meaning, compensability, or a decision threshold. A partial score can hide a decisive missing obligation, while reference-aware flexible salvage and alignment can prefer reference-shaped solutions.

The paper defines a formal pass threshold `τ` but uses two thresholds in practice: refinement continues below 6.0, whereas diversity labels a rollout passing at ≥5.5 (Sections 3.4–3.5 and 4.6, pp. 6, 11). Neither threshold is tied to expert acceptance, operational loss, or downstream consequence.

### Baseline regeneration and missing outcomes

The baseline mean is 5.06 over **68 of 72** tasks; four runs never reach grading because of serialization, timeout, or startup failures and are excluded. Per-tier reported rates are VC 86.8%, flex 72.1%, and alignment 66.2%; strict all-three success is 54.4% of 68 (about 37 runs) (Section 4.3 and Table 1, pp. 8–9).

Conditional scoring is clearly disclosed, but it makes 5.06 an infrastructure-complete estimand. Counting the approximately 37 strict passes over all 72 selected sessions gives only 51.4% end-to-end strict completion; this is a diagnostic restatement, not a substitute score. There are no confidence intervals, task-clustered intervals, repeated-run outcome models, missingness sensitivity, or stratification by task/developer/project.

### Iterative refinement is same-oracle optimization

Thirty-one of the 68 graded baselines score below 6.0 and enter up to three rounds. For each failed VC, a refinement model sees the original spec, **ground-truth diff**, regenerated diff, failed private VC, and grader rejection reasoning, then rewrites the full specification. A fresh agent reimplements; the same three-tier verifier scores it; tasks exit at 6.0; and the best score across baseline and rounds is retained (Section 3.5, p. 7; Section 4.4, pp. 8–10; Prompt A.2, pp. 20–21).

The reported 5.06→5.74 increase is therefore a **selected in-loop maximum**, monotonically nondecreasing by construction. It bundles:

- privileged reference-diff disclosure to the refiner;
- private-oracle and rejection-reason exposure;
- up to three additional stochastic implementation attempts;
- task-specific early stopping;
- selection on the same score used for feedback;
- no held-out recipient, alternative verifier, fresh task, or post-selection rerun.

Round means for the shrinking residual cohort are 4.68, 4.71, and 4.38; the evidence shows that repeated optimization often finds a higher-scoring candidate, not that each rewrite is intrinsically better. The 84% “success rate” means 26/31 tasks obtain a positive selected delta at least once, not 84% independent solve rate. A valid strengthening claim needs nested train/selection/test evidence or at least a fresh fixed recipient panel and untouched consequence checks after the spec is frozen.

### Abstraction and leakage

The paper compares constrained (~2,117 characters), standard (6,960), and diff-preserving (11,836) specifications. Mean scores are 4.81, 5.06, and 5.55; distinctive diff-token leakage is 23.7%, 38.6%, and 62.6% (Table 3, pp. 9–10). This is useful evidence that greater copied detail predicts higher reference-aligned performance, especially on the holistic judge.

It does not “confirm” abstraction. Compression ratio is a size statistic, not semantic abstraction; the standard spec still reproduces 38.6% of distinctive code tokens. Extraction strategy simultaneously changes length, identifiers, literals, exact contracts, and possibly useful evidence. There is no matched removal of incidental versus essential detail, human abstraction rating, requirement-coverage audit, or causal mediation analysis. The environmental-grounding interpretation is plausible, but repository clues, same-model priors, and reference-aware observers remain alternatives.

### Regeneration multiplicity and diversity

Three regenerations per task yield 200 of 216 possible within-task rollout pairs; 16 pairs are skipped when a rollout produces no patch. Pairwise similarity averages per-file chrF and `difflib` scores over the union of touched files. “Passing” means both runs score ≥5.5. Both-pass pairs have chrF 0.888/`difflib` 0.819, both-fail 0.856/0.749, mixed 0.835/0.740; rollout mean scores are 5.06, 4.87, and 4.99, with mean within-task score SD 0.49 (Section 4.6, pp. 11–12).

The multiplicity is valuable reliability evidence. The inference that these results show substantial structural diversity is weak. A chrF near 0.89 indicates high character overlap, not a demonstrated alternative design. The upper anchor removes one added line from a patch compared with itself (0.982), while the lower anchor compares unrelated tasks (0.180); neither represents a legitimate semantically equivalent alternative implementation. Added-line-only anchors, per-file averaging, shared repository, same model, and no AST/control-flow/API/design analysis further limit interpretation. Both-fail similarity may indicate a systematic spec gap, a shared model prior, a shared repository affordance, or grader coupling; the study cannot identify which.

### Grader falsification evidence

The paper runs each task's VCs and flex tests against three controls: parent/pre-change code, a syntax-preserving LLM deletion of about 50% of diff hunks, and another task's landed code assigned by seeded derangement. Among tasks conditioned to pass both graders on the reference, VCs pass 47.0% of partial, 0% of pre-change, and 1.4% of permuted code; flex passes 42.4%, 58.0%, and 51.4% (Section 4.7 and Table 4, pp. 11–13).

This is one of the paper's strongest methodological choices: an oracle should be challenged with known-worse artifacts, not merely shown to accept its reference. It supports task-specific discrimination for the VC observer under these contrasts. It does not establish soundness, completeness, or professional validity:

- positive conditioning makes 100% reference acceptance true by construction;
- parent and unrelated diffs are often easy negatives, not plausible near-miss alternatives;
- deleting 50% of hunks has no calibrated severity or independent semantic label;
- one monorepo-wide permutation can fail because the requested task is absent, without testing subtle false acceptance;
- flex's 51–58% pass rates show many commands are broad build checks rather than task-specific oracles;
- the binary alignment judge receives no negative-control or human calibration study;
- no valid alternative implementation set tests false rejection;
- no expert labels, duplicate graders, agreement, confusion matrix by predicate, adversarial mutations, or post-refinement contamination check are reported.

### Human-description comparator

The comparator is the developer's title, review description, and test plan used verbatim as a blind reimplementation specification. It averages 2,129 characters and scores 4.23 versus AfterVibe's 6,960 characters and 5.06; the configured agent and graders are held fixed (Section 4.8, p. 13).

This is a clean paired comparison of **artifact source packages**, but not a human-versus-machine specification study. The human artifact was authored for reviewers who also see the code, not for blind reconstruction; AfterVibe is 3.27× longer and optimized for the recipient task. There is no human asked to write a self-contained spec under the same template, evidence access, length/time budget, or regeneration objective, nor an AfterVibe summary constrained to the human length. The result supports “the richer extracted package works better for this blind agent” and the authors' audience explanation—not superiority to human specification authoring or reduced human work.

### Compute, cost, and operational burden

The paper reports no API usage, tokens by component, calls, wall time, hardware, dollar cost, engineer time, annotation/review time, storage, retries, or full pipeline failure rate. At minimum, baseline extraction requires multiple model pipelines and one recipient run with three agentic graders; refinement adds up to three fresh implementations and repeated grading, while the diversity study uses three regenerations per task. Calling the specification a “byproduct” does not make this compute, verification, or review free. No evidence compares total lifecycle cost against writing, reviewing, testing, maintaining, or updating a human specification.

## Evidence and claim assessment

### Strongly supported by the manuscript

1. A complete prompt-level design exists for projecting conversation-plus-diff evidence into a structured recipient-facing specification and separate verification artifacts.
2. A fresh-session recipient-action test can expose missing requirements that text-only review may not reveal.
3. In the selected private frame, the reported baseline configured system often reconstructs code that satisfies substantial fractions of the selected observers.
4. VC controls discriminate reference code from parent, heavily degraded, and unrelated-task code much more sharply than extracted test commands.
5. Regeneration is stochastic enough that repeated attempts matter; score means and within-task SDs are reported for three rollouts.
6. More diff-preserving extraction copies more distinctive code tokens and scores higher, especially on reference alignment.
7. The human review description and the longer machine-extracted package are different-purpose artifacts; the latter performs better for the paper's blind reconstruction task.

### Partially supported

- **Behavioral reconstructability:** selected tests, VCs, and a model judge often accept regenerations, but observer completeness and independent truth are unestablished.
- **Abstract sufficiency:** standard specs compress diffs and allow nonidentical outputs, but compression/code overlap and weak diversity anchors do not validate semantic abstraction.
- **Oracle validity:** negative controls show discrimination against easy/wide degradations, but no alternative-valid set, subtle defect panel, human calibration, or alignment-judge audit establishes soundness/completeness.
- **Refinement utility:** best-of-K scores rise on the same oracle after privileged feedback, but held-out post-selection quality and cost-adjusted value are unknown.
- **Real-world grounding:** sessions and landed changes are genuine internal work, but the seven-day, one-company, instrument-filtered, unclustered frame is not a representative work sample.

### Unsupported

- recovered authoritative or complete developer intent;
- implementation or semantic equivalence beyond the selected observers;
- superiority to purpose-matched human-authored specifications;
- independent human reviewability or recipient usability;
- transfer across recipients, repositories, organizations, roles, domains, or time;
- maintainability or source-of-record fitness;
- review, labor, or total lifecycle cost reduction;
- professional validity, production fitness, reliability, safety, or readiness.

## Unique insight

> **Regeneration is a recipient-side falsification instrument, not an identity test for intent.**

The reusable claim ladder is:

```text
principal / stakeholder requirements and authority
→ source conversation, actions, corrections, accepted artifact, and omitted context
→ proposition-level specification with evidence lineage and uncertainty
→ frozen recipient-visible environment and protected-evidence boundary
→ independently configured recipient interpretation and implementation
→ admissible behavioral checks and accepted-alternative set
→ artifact/state consequence and collateral preservation
→ recipient verification, clarification, rework, and cost
→ changed-context / changed-recipient transport
→ maintenance under source, environment, and requirement drift
→ expert/user acceptance and bounded professional claim
```

AfterVibe observes a real source episode, projects a specification, runs a same-repository recipient, and applies selected checks. It does not independently validate the first link, all consequences, recipient diversity, transport, maintenance, or acceptance. This yields six durable distinctions:

1. **Source observability is not authoritative intent.** A conversation and landed diff may be the best available evidence while remaining incomplete or jointly mistaken.
2. **Behavioral sufficiency is not implementation equivalence.** Passing selected predicates shows compatibility with an observation set, not equality of all relevant behaviors.
3. **Independent session is not independent lineage.** A fresh context prevents memory carryover, but the same model family, source bundle, repository, and reference-aware observers can preserve common-mode assumptions.
4. **Recipient success is not recipient utility.** One agent may reconstruct by repository search and model priors while a human reviewer still cannot understand, approve, or maintain the artifact.
5. **Same-oracle improvement is not general artifact improvement.** Feedback, stopping, and best-of-K selection require a held-out post-selection observer or recipient panel.
6. **Current reconstruction is not lifecycle fitness.** A source-of-record claim requires change detection, conflict handling, versioning, rollback, alternate futures, maintenance cost, and owner acceptance.

### Comparison with adjacent reviewed evidence

- **Handoff Debt:** freezes an interrupted work state and varies successor-visible context, measuring takeover outcomes and effort. AfterVibe instead freezes a pre-change base and asks for reconstruction from a post-hoc intent projection. Together they show that handoff quality is relational: state fidelity, recipient sufficiency, endpoint quality, rework, and lifecycle cost need separate outcomes. Neither validates human or professional handoff.
- **MAG:** projects a successful action trace into local user instructions but does not let an independent recipient consume the guide. AfterVibe supplies the missing recipient-action pattern, while retaining the same projection-validity risk: source success and shared lineage do not certify proposition truth, omissions, alternatives, or maintainability.
- **AgentCo-op:** typed transport does not establish semantic or receiver-use validity. AfterVibe advances to receiver execution, but selected reconstruction success still does not validate authority, alternate recipients, downstream effects, or repair causality.
- **Task projection/specification machinery:** Anchor and the repository's task-projection manifest distinguish shared generation lineage from semantic equivalence. AfterVibe's spec, VCs, tests, and reference code are multiple projections of overlapping source evidence; bidirectional coverage, independent sentinels, and accepted-alternative checks remain necessary.
- **Artifact admissibility:** each grader sees a different representation and reference entitlement. Test logs, code/diff views, repository state, conversation, and reference patch must be explicit criterion-specific evidence views; “three tiers” does not make every view sufficient or independent.
- **Task health and validity arguments:** the 41 infrastructure exclusions, nine reference-oracle failures, four baseline nulls, control pass rates, refinement exposure, and versioned grader behavior are task-health evidence. They license a bounded detection/reconstruction claim, not source-of-record or readiness promotion.

## Limitations and validity threats

1. Private data and environments prevent task-level audit or replay.
2. No author-owned empirical release was linked or found at review time.
3. The seven-day, one-company, one-monorepo frame is not population sampling.
4. “Sufficient conversation context” is an unspecified judgmental inclusion rule.
5. The final 72 are conditioned on infrastructure completion and reference acceptance by the tested graders.
6. Forty-one of 122 curated candidates fail before complete reference grading.
7. Nine CI-passing landed changes fail the extracted reference oracle, demonstrating instrument/environment mismatch.
8. Four of 72 baseline recipients never reach grading and are excluded from score aggregates.
9. Unique projects, repositories, developers, task families, code regions, and lineage clusters are not reported.
10. No source-, developer-, project-, or task-family-clustered uncertainty is reported.
11. Conversation observability is assumed sufficient for developer requirements without elicitation or stakeholder validation.
12. Accepted behavior can contain jointly accepted defects or omitted external obligations.
13. Spec and VCs share conversation/diff evidence and one unnamed model family.
14. Ground-truth alignment sees conversation, reference patch, and repository, creating reference dependence.
15. Flexible test salvage may inspect the reference patch and introduces model-mediated test adaptation.
16. Regeneration-agent access to changed tests, reference artifacts, private grader files, network, and other protected evidence is not attested.
17. All model components use one unnamed frontier model, blocking configured-system reproduction and cross-recipient transport claims.
18. Model snapshot, decoding, harness, tools, budgets, isolation, retries, and environment identities are absent.
19. The 0–6 weights and 5.5/6.0 thresholds lack stakeholder-loss or expert-acceptance calibration.
20. Grader outputs are dependent but aggregated as compensable components.
21. Missing runs are omitted rather than included in a primary end-to-end denominator.
22. No confidence intervals or significance tests accompany baseline, human comparison, or selected improvement.
23. Refinement receives the reference diff, failed private VC, and grader reasoning.
24. Refinement and best-of-K selection reuse the same oracle with no held-out confirmation.
25. Up to three extra implementation attempts confound artifact improvement with additional inference opportunity.
26. Early stopping and shrinking residual cohorts make round means noncomparable.
27. Compression ratio does not measure semantic abstraction.
28. Standard specifications still copy 38.6% of distinctive diff tokens under the paper's leakage metric.
29. Extraction variants bundle length, literals, identifiers, contracts, and detail level.
30. Pairwise chrF near 0.89 is high overlap, not demonstrated design diversity.
31. Diversity anchors—self minus one line and unrelated tasks—do not bound valid alternative implementations.
32. Sixteen of 216 rollout pairs are unavailable because a rollout has no patch.
33. Negative controls are conditioned on reference-pass tasks.
34. Parent/unrelated-task controls are easy negatives; partial-hunk deletion has no calibrated semantic severity.
35. No valid-alternative panel estimates grader false rejection.
36. The alignment judge receives no human calibration, negative controls, or agreement study.
37. The human comparator is 3.27× shorter and written for code-visible review, not blind reconstruction.
38. No purpose-, template-, evidence-, time-, or length-matched human specification condition exists.
39. No human reviews or uses an AfterVibe spec.
40. No changed-context, delayed-recipient, cross-model, cross-repository, or maintenance study exists.
41. No compute, usage, wall-time, hardware, API, engineering, review, or lifecycle cost is reported.
42. The paper's “source of record” and primary-review-artifact vision is explicitly future work, not an evaluated outcome.
43. One private coding environment does not establish cross-domain knowledge-work transfer.
44. No evidence supports professional validity, production fitness, safety, or readiness.

## Reproducibility and operational realism

**Protocol inspectability is moderate to strong.** The immutable paper provides all eight core prompts, the score equation, source funnel, aggregate denominators, baseline/refinement/abstraction/diversity/control tables, and qualitative failure explanations. Another team could implement a related regeneration test.

**Exact result reproducibility is absent.** Reproduction requires immutable task membership and exclusions; source conversation/diff/metadata bundles; specs and refinements; base and landed repository hashes; protected-artifact manifests; test/VC records; all recipient patches; grader traces and verdicts; model and harness identities; environments; retries and missingness; component usage; task clusters; analysis code; and per-run results. None is available. Aggregate tables cannot support independent uncertainty, false-positive/false-negative audit, selection correction, or cost reconstruction.

**Operational realism is meaningful at the source but narrow at the recipient.** Landed monorepo changes, multi-turn conversations, developer corrections, real test commands, infrastructure failures, and repository exploration are stronger than synthetic issue-only tasks. Yet recipient work is a fresh AI reconstruction for the same codebase, not human review, team handoff, maintenance, incident response, permission transfer, clarification, concurrent change, deployment, or downstream use. The study tests a private software reconstruction pipeline, not whether specifications can replace code review or become trusted organizational records.

## Transfer to `skill-bench`

### Retain

1. **Recipient-action falsification:** require a separate configured recipient to act from the candidate artifact rather than scoring prose resemblance alone.
2. **Artifact/oracle separation:** derive candidate guidance and private consequences through separately versioned pipelines, while recognizing that source/model independence must also be tested.
3. **Plural verification:** combine execution, proposition-level checks, and holistic artifact/state review without collapsing their meanings prematurely.
4. **Known-worse controls:** test observers against parent state, planted omissions, contradictions, stale facts, and unrelated artifacts.
5. **Repeated recipients:** preserve stochastic outcome distributions and no-output cases.
6. **Abstraction/leakage diagnostics:** track compression and copied source tokens as diagnostics, not proof of semantic abstraction.

### Repair

1. **Start with an authority ledger.** Type each requirement proposition by source span, speaker/actor authority, acceptance status, valid time, confidence, contradiction, omission risk, and stakeholder review. Do not define intent as whatever happened.
2. **Attest the recipient envelope.** Freeze environment/workspace hashes and prove which repository, tests, references, private checks, network resources, prior memory, and tool surfaces are visible.
3. **Cross lineage.** Evaluate at least extraction model × recipient model/harness, and use independently authored or adjudicated consequence checks so fresh context is not mistaken for independent evidence.
4. **Separate claim levels.** Score source-intent recovery, selected behavioral sufficiency, accepted-alternative compatibility, recipient execution, preservation/collateral effects, clarification/rework, maintainability, and professional acceptance independently.
5. **Use a held-out refinement design.** Split feedback observers from final observers; freeze the selected artifact; rerun fresh recipients; and report all attempts, not just the maximum.
6. **Calibrate observers bidirectionally.** Include clean references, subtle planted defects, valid alternate implementations, invalid artifacts, missing evidence, and human/expert adjudication. Estimate false acceptance and false rejection by criterion family.
7. **Match the human comparator.** Ask humans/experts to author the same recipient-facing artifact under equal source access, purpose, structure, time/length budget, and review entitlement; retain ordinary summaries as a separate ecological baseline.
8. **Measure recipient and lifecycle cost.** Include extraction, validation, recipient search, clarification, implementation, retries, grading, human review, storage, drift detection, updates, and downstream failures.
9. **Test alternate futures.** Reuse the frozen artifact with a delayed recipient, changed implementation affordance, alternate valid route, rollback, audit, or requirement update.
10. **Use source-level clusters.** Preserve session/developer/project/task-family ancestry and resample at the highest shared lineage unit.

## Concrete repository actions

1. **No new build task.** The findings fit existing task-projection, evidence-proposition, artifact-admissibility, handoff-usability, trace, configured-system, task-health, metric, and validity contracts. A coding-specific regeneration schema would duplicate machinery and narrow scope.
2. **No duplicate recipient pilot.** MAG and Handoff Debt already imply a small frozen-state recipient falsification with valid, omitted, stale, and alternate-route artifacts. AfterVibe adds two requirements to that future validation: cross extraction/recipient lineage and held-out post-refinement observers.
3. **Consolidate later.** When the queued handoff/guide synthesis is next updated, integrate the general chain `source episode → authority-typed specification → protected recipient envelope → independent action → held-out consequences → rework/lifecycle cost`, preserving distinct claim ceilings for intent recovery, behavioral reconstruction, recipient usability, maintenance, and professional acceptance.

## Review checklist

- [x] Read the complete immutable v1 PDF/text, including all appendix prompts.
- [x] Verified local PDF/text identity and 27-page metadata.
- [x] Reconstructed the 122→81→72 source funnel and 68-task baseline denominator.
- [x] Audited evidence views, extraction, recipient isolation, grader topology, weights, thresholds, missingness, refinement, abstraction, diversity, controls, and human comparator.
- [x] Distinguished best-of-K same-oracle optimization from held-out artifact improvement.
- [x] Distinguished source observability, behavioral sufficiency, implementation equivalence, recipient utility, lifecycle cost, professional validity, production fitness, and readiness.
- [x] Searched author/official/GitHub surfaces and documented the paper-time absent-release boundary.
- [x] Compared directly with Handoff Debt, MAG, AgentCo-op, task projection, artifact admissibility, and task health.
- [x] Reused existing repository machinery rather than adding a coding-specific contract.
