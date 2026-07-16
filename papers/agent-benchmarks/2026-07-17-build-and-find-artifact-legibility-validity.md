# BUILD-AND-FIND: recoverable intent and conditional inspection effort do not establish maintainability

## Source and evidence status

**Deep review of the complete immutable primary source.** I read the full 25-page arXiv v1 paper, including Appendices A–N, and checked the layout extraction against the PDF and arXiv source.

- **Paper:** Jhen-Ke Lin, *BUILD-AND-FIND: An Effort-Aware Protocol for Evaluating Agent-Managed Codebases*
- **Immutable version:** https://arxiv.org/abs/2605.06136v1 (submitted 7 May 2026)
- **Date read:** 2026-07-16 UTC
- **Local PDF:** `data/papers/pdfs/2605.06136v1-build-and-find.pdf` (25 pages; SHA-256 `2b872c3cac2668de8a111c812f20e5fb826488bddd58de7f959e9df338d1ac67`)
- **Local text:** `data/papers/text/2605.06136v1-build-and-find.txt` (SHA-256 `b4ab93f27d60abee46ee131a49c571ac9113784065caeff2084854724cee2849`)
- **ArXiv source:** `data/papers/source/2605.06136v1.tar.gz` (SHA-256 `6133e1fbd3cd7640567b79a67ae20d4f2f801b42215c2bcd288a4daa6636faff`)
- **Release provenance:** `data/sources/releases/2605.06136v1-build-and-find/provenance.json`
- **Tags:** artifact legibility, successor inspection, specification traceability, recovery gates, effort estimands, finder affinity

The paper says it releases the harness, task packs, generated repositories, run records, tables, reports, scripts, metadata, licenses, claim-evidence map, and evidence audit (Abstract; Sections 1 and 7, pp. 1–2, 8). Its sole release URL in immutable v1, `https://anonymous.4open.science/r/Build-and-Find/`, redirected to an API endpoint that returned HTTP 401 `not_connected` on 2026-07-16. Exact-title, author, arXiv-ID, and repository searches found no independently identifiable public snapshot. The failed response and search boundary are preserved in the provenance manifest. Consequently, this is a **full-paper/source review but not a release-conformance audit**: no task, artifact, record, rationale, byte ledger, script, manifest, license, or reported table could be independently replayed. Nothing below infers unavailable release contents.

## One-sentence contribution

BUILD-AND-FIND makes a valuable intermediate construct explicit—whether a fresh agent can recover specification-traced choices from another agent’s artifact, with recovery and repeatability gating a within-finder inspection-effort comparison—but its two high-prior synthetic tasks, model-assisted scoring-set audit, outcome-conditioned byte metric, finder interactions, absent clustered uncertainty, and unavailable release support only panel-local **artifact-evidenced label recovery and conditional inspection burden**, not behavioral correctness, intrinsic legibility, human maintainability, successor task success, professional quality, safety, capability, or readiness.

## Why this matters for `skill-bench`

This review advances charter objectives A and B through a cross-domain hypothesis:

> A work product can satisfy selected endpoint checks yet impose very different evidence-recovery burdens on its next recipient; evaluating that burden requires proposition-level source traces, calibrated recipients, correct-and-repeatable recovery gates, explicit evidence views, and effort estimands that do not confuse success selection with usability.

The artifact need not be code. The same pattern applies when a later analyst must recover assumptions from a spreadsheet, an auditor must locate support in a research dossier, an operator must identify thresholds in a runbook, or a reviewer must trace decisions through a design package. BUILD-AND-FIND is distinct from endpoint-only artifact scoring because it asks what information the artifact carries forward. It is also distinct from Handoff Debt and AfterVibe: the finder answers source-traced questions without modifying the artifact, so the protocol isolates **pre-action evidence recovery** rather than takeover success or specification-driven regeneration.

The coding case is a bounded methodological experiment, not a scope commitment. Existing `skill-bench` handoff, artifact-view admissibility, metric, task-health, trace, and validity machinery can represent the useful parts. The evidence does not justify a new coding-specific subsystem.

## Research question and defensible claim boundary

The paper asks whether a finder that cannot see the builder’s hidden specification can recover intended behaviors and design choices from the generated repository, and—when recovery is correct and repeatable—how many novel artifact/tool-call bytes the finder uses (Sections 1 and 3, pp. 1–4).

The strongest defensible empirical claim is:

> In a compile-passing panel of 41 generated Rust repositories from two synthetic task families, twelve pinned model–harness–effort finder configurations achieved reported 98.9% exact-match recovery over 592 artifact-question pairs labeled `implemented-gold`; among finder–task cells with at least one all-correct trial, within-finder relative novel-byte effort differed by builder, with moderate and task-dependent ordering agreement and positive same-family affinity residuals.

The evidence does **not** establish that:

- all hidden specification claims are correct, complete, authoritative, or professionally relevant;
- the repositories behave correctly beyond a root-level compile probe and artifact inspection;
- lower novel-byte effort is an intrinsic artifact property independent of finder policy, tool protocol, stopping, success conditioning, or artifact size;
- exact answers were causally based on artifact evidence rather than priors in unsampled rows;
- one builder generally creates more understandable or maintainable artifacts;
- humans, different recipients, or recipients performing real modifications would realize the same ranking;
- the task pack is representative of software work or other knowledge work;
- the reported package is independently reproducible, contamination-resistant, safe, or ready.

## Methodology and system

### Task → specification → artifact → question → evidence chain

Each of two task families, `scratch_minidb` and `scratch_nanoweb`, contains a hidden repository specification and fifteen four-option questions traced to intended specification items. A builder receives the specification and writes a self-contained Rust codebase. A finder receives a read-only clone of the artifact and the shuffled question bank, but not the specification, and writes `find_answers.json`. Exact-match answers are de-shuffled to canonical options (Sections 3.1 and Appendix A, pp. 3, 11–13).

This is a clean role boundary at the prompt level and a useful trace structure:

```text
hidden specification proposition
→ generated artifact and build record
→ specification-traced question and alternatives
→ finder-visible artifact evidence
→ selected answer plus cited file/symbol/rationale
→ exact-match observation
→ recovery/repeatability gate
→ conditional inspection effort
→ bounded artifact-recipient claim
```

However, a specification trace establishes authored lineage, not truth. The paper reports schema validation and author review of specifications, distractors, traces, and gold answers, but no domain-expert elicitation, independent requirement authority, accepted-alternative review, or evidence that the fifteen questions adequately cover either repository task (Appendix N, pp. 24–25). A finder can recover an author-defined label from code even if the design choice is unnecessary, incomplete, or wrong.

### Configured systems and execution

The panel has twelve configurations: Opus 4.7, Sonnet 4.6, GPT-5.5, GPT-5.4-mini, MiMo-v2.5-pro, and MiMo-v2.5, each at high and low reasoning effort. Claude models use Claude Code 2.1.114, GPT models use Codex CLI 0.124.0, and MiMo uses the Claude Code harness because its API was incompatible with Codex. The benchmark harness is version 0.1.0; Python, Rust, machine, and OS versions are reported (Appendix D and M, pp. 14, 23).

Every model configuration acts as both builder and finder. Two tasks × twelve builders × two build trials produce 48 status-ok artifacts. Each compile-passing artifact is assigned to twelve finders for three trials. Finder prompts, specification hashes, registry identity, adapter family, model, seed, trial, environment hash, and usage are said to be recorded (Appendices A–D, pp. 11–15).

This is better configured-system disclosure than model-name-only evaluation, but not full reproducibility. Provider-side sampling seeds are explicitly outside the record; model snapshots are service labels; system/harness internals, prompts, task assets, network policy, workspace enforcement, retries, and logs are unavailable for inspection. MiMo-versus-Claude comparisons also conflate model with a shared Claude-Code-style harness, while Codex-versus-Claude comparisons conflate model family and native harness.

### Denominator reconstruction

The paper’s main execution counts are arithmetically coherent:

| Stage | Unit | Count |
|---|---:|---:|
| Planned/status-ok artifacts | `2 tasks × 12 builders × 2 trials` | 48 |
| Root compile-pass primary artifacts | artifact | 41 |
| Compile-probe failures | artifact | 7 |
| Primary find records | `41 × 12 finders × 3 trials` | 1,476 |
| Raw primary question rows | `1,476 × 15` | 22,140 |
| Audited implemented-gold artifact-question pairs | pair | 592 of 615 |
| Scored finder-answer rows | `592 × 12 × 3` | 21,312 |
| Excluded non-gold/ambiguous primary answer rows | `23 × 12 × 3` | 828 |
| Artifact-present find records including stress artifacts | `48 × 12 × 3` | 1,728 |
| Artifact-present raw question rows | `1,728 × 15` | 25,920 |
| Spec-only controls | `2 × 12 × 3` | 72 runs / 1,080 rows |
| Question-only controls | `2 × 12 × 3` | 72 runs / 1,080 rows |

The seven compile exclusions are not simply broken code. A post-hoc relaxed probe finds a unique nested Cargo project in six and compiles all six; one artifact has no Rust source. Thus the primary gate mixes packaging/layout conformance with source buildability (Appendix G, pp. 16–17). Retaining a strict artifact-root contract is defensible, but calling all seven “compile-failed” without the sensitivity layer would overstate behavioral failure.

### Implementation audit and scoring-set construction

The paper avoids penalizing a finder for recovering a gold choice that the artifact did not implement. It labels all 720 artifact-question pairs across 48 artifacts as `implemented-gold`, `implemented-non-gold`, or `absent/ambiguous`; only implemented-gold pairs enter recovery scoring. Builder implementation coverage remains separately reported and ranges from 85.0% to 100.0% (Section 4.1 and Appendix H, pp. 5, 17–18).

The repair is conceptually sound: omitted or contrary implementation is a builder failure, not finder misunderstanding. The implementation is also the study’s largest validity threat. An automated triage uses repeated answers from `codex_gpt5_5` and `claude_code_opus_4_7`, both later evaluated as finders, to assign **696 of 720 consensus prelabels**; only 24 pairs enter manual review. The manuscript does not state the exact agreement rule, confidence threshold, artifact evidence required for auto-labeling, reviewer count, blinding, disagreement procedure, or error estimate. Finder outputs therefore help define which claims count as implemented and then those same finder families are scored on the resulting set. This is not necessarily wrong—agreement can nominate review cases—but without independent artifact inspection or a held-out label audit it risks circularly converting stable finder priors into “implementation” truth.

Excluding 23/615 primary pairs from finder scoring also creates a favorable recovery estimand. The paper does co-report implementation coverage, which is essential, but its compact AELS formula does not plainly incorporate implementation coverage; `Ā` is described as audited recovery over formal primary cells. Missing and contrary claims must not disappear when users interpret an artifact-level headline.

### Prior and specification controls

Question-only accuracy is 94.5%, spec-only accuracy 99.9%, artifact-conditioned accuracy 98.9%, and compile-failed diagnostic accuracy 98.8% (Table 1, p. 6). The artifact therefore adds only 4.4 percentage points over the high-prior question-only condition. Three-trial agreement is 86.7% question-only, 99.7% spec-only, and 97.5% formal; 20/30 questions appear to satisfy the question-only “reliable question” criterion versus 29/30 formal (Table 2, p. 6; task detail in Appendix J, pp. 19–20).

These controls are the paper’s most important honesty mechanism. They show that formal exact-match accuracy is near saturation and cannot carry a broad legibility ranking. But they also reveal that the questions often expose their own likely answers. A multiple-choice item can be specification-traced yet still measure ordinary design priors rather than repository communication.

The ten-question low-prior subset is selected after observing question-only three-trial agreement below 90%. It raises artifact lift to 9.0 points (88.9%→97.9%), but remains a small outcome-defined slice with five questions per task. No confidence interval, held-out item pack, or repeated finder-panel confirmation separates genuine artifact information from threshold selection and regression. Low-prior effort further assigns the **whole run’s** bytes to only the selected subset, which the paper correctly calls an upper-bound sensitivity diagnostic (Appendix L, pp. 21–22).

### Recovery, repeatability, and evidence use

Formal accuracy is computed only on audited implemented-gold pairs. A run is all-correct when every eligible question for its artifact is correct. Mean repeated-run accuracy forms a task-level recovery gate, while three-trial agreement and “reliable questions” provide stability context (Section 3.4, pp. 4–5; Tables 2–3, pp. 6–7).

The recovery gate is sensible, but repeatability is thin. There are only three live trials per artifact–finder cell, provider sampling seeds are uncontrolled, and deterministic option shuffling changes order without isolating model stochasticity. The paper reports no binomial or hierarchical uncertainty, no source-task/artifact clustering, and no repeated builder generations beyond two artifacts per builder-task. “96.7% reliable questions” is an item-level panel summary over only thirty authored questions, not evidence of benchmark-wide reliability.

A post-hoc evidence audit samples 72 correct answers, stratified by task, builder family, finder family, and low/high prior. It finds 65 supported, three partially supported, and four unsupported/prior-like; 35/36 low-prior answers are supported. Source files dominate citations, while tests are never the primary cited channel (Section 4.8 and Appendix I, pp. 7–8, 18).

This is useful construct evidence but limited: 72 rows are 0.34% of the 21,312 scored rows; only already-correct answers are sampled; rationales were not required or graded prospectively; no audit of wrong answers tests whether artifact evidence contradicts them; no auditor count, expertise, blinding, agreement, or uncertainty is reported. A rationale can also be post-hoc justification rather than causal evidence use. The audit supports “many sampled correct answers have distinguishing artifact citations,” not “98.9% recovery was artifact-caused.”

### Conditional inspection-effort metric

The key effort unit is `novel_retrieval_bytes + novel_tool_call_bytes`: distinct tool-result bytes delivered to the model plus emitted search/read arguments, excluding system prompts, schemas, transport overhead, and replayed context (Section 3.4 and Appendix F, pp. 4–5, 15–16). Bytes avoid cross-tokenizer comparisons. Artifact scores are normalized only within the same finder–task cell:

1. retain all-correct trials;
2. average their effort for each builder–finder–task cell;
3. divide by the minimum defined builder cost in that finder–task cell;
4. geometrically average those ratios over cells where the builder has at least one all-correct trial;
5. report missing cells separately as coverage.

This is appropriately narrower than raw cross-model token ranking. It holds the recipient and task fixed and refuses to interpret effort without successful recovery. Yet it is not a pure artifact-legibility estimand:

- conditioning on all-correct trials makes effort outcome-selected; a lucky short successful run counts while longer failed inspections vanish;
- a missing cell is excluded from the geometric mean, so low effort and low coverage can coexist and require joint interpretation;
- the minimum-builder denominator is sample-dependent and can move with one unusually cheap successful cell;
- retrieved bytes measure exposed text volume, not verification quality, reasoning burden, search redundancy, latency, or human review;
- tool-call argument bytes partly measure path/query verbosity and adapter serialization rather than artifact inspection;
- artifact size, layout, documentation, source density, and finder stopping policy are bundled rather than factored;
- there are no intervals or source-task-clustered repeated-run estimates;
- builder generation cost is absent from `R_b`, so the metric is recipient-side inspection burden, not lifecycle efficiency.

The paper preserves raw run effort before filtering questions, which avoids pretending unimplemented questions consumed no time. But it then compares conditional means over successful runs, not time/bytes to a valid endpoint with failures censored or penalized. A stronger design would report unconditional budgeted success, success-conditioned cost, and a joint cost-to-reliable-recovery curve separately.

There is also an unresolved manuscript inconsistency. Section 4.5 reports low-effort GPT-5.5 `R_b = 1.151` (p. 7), while AELS Table 9 reports `R_b = 1.137` for `codex_gpt5_5_low` (p. 16). Both are described as the conditional total-byte view; unavailable records prevent determining whether one uses a different panel or is stale. The discrepancy is small but matters because the paper’s main discriminative outcome is effort.

### Finder calibration, ranking, and affinity

Finder-specific calibration shows why high formal accuracy is insufficient. Opus and GPT-5.5 finders have 99%+ formal recovery but negative lift over their own saturated question-only controls; Sonnet and MiMo variants often gain more from the artifact. A post-calibration script reportedly selects Sonnet high/low for routine use and MiMo-pro-low as a prior-stress auditor (Appendix E, pp. 14–15).

This is a strong conceptual point: a recipient is part of the measurement instrument. But the selector is post-calibration on the same two tasks, and the release needed to inspect thresholds or recompute selection is unavailable. The study does not validate selected finders on a held-out task pack.

Kendall ordering agreement is moderate in most slices but task-dependent, especially at low effort. Same-family affinity residuals are positive for OpenAI/Codex (+0.076), Anthropic/Claude (+0.041), and MiMo (+0.027) (Section 4.6–4.7 and Appendix K, pp. 7, 20–21). Those results directly undermine universal builder rankings: “legibility” is a relation between artifact conventions and recipient policy. Affinity residuals are descriptive, however. They do not separate shared style, shared model priors, harness family, task composition, or chance, and no uncertainty accompanies the 12×12 matrix.

### Resource use and operational realism

The formal artifact-present tables sum to about 1,102.4 million vendor tokens; controls add 19.2 million, consistent with the paper’s “more than 1.1B” statement (Appendix M–N, pp. 23–25). Build means range from about 1.9M to 15.3M tokens per run and finder means from 120k to 923k. This is a costly protocol for thirty questions over two task families. The release provides no dollars, energy, human audit time, or marginal information-per-cost analysis.

Operational realism is bounded. Separate builders/finders, repository-sized artifacts, read-only inspection, compile probes, append-only records, and explicit file/symbol evidence resemble real handoffs. But tasks are synthetic, questions are fixed multiple choice, recipients perform no modification or consequential decision, all work is provider-mediated, and no human reviewer, issue history, CI, code review, security analysis, stakeholder clarification, or maintenance episode is observed. The result is a calibrated communication-artifact probe, not a professional software-maintenance evaluation.

## Evidence and claim assessment

### Strongly supported by the manuscript

1. Artifact-side recovery is a coherent intermediate construct distinct from behavioral testing and downstream modification.
2. The builder–finder role split and specification-traced question bank provide an inspectable protocol design.
3. The reported execution and scoring denominators reconcile from 48 artifacts to 41 primary artifacts, 1,476 runs, 22,140 raw rows, 592 eligible pairs, and 21,312 scored rows.
4. Question-only accuracy is high enough that raw recovery accuracy is not a discriminative artifact ranking in this task pack.
5. Co-reporting implementation coverage prevents unimplemented claims from being silently treated as finder errors.
6. Within-finder conditional byte effort and missing-cell coverage differ across reported builders.
7. Finder calibration, rank agreement, and affinity show that recipient configuration changes the observed artifact comparison.
8. Six of seven strict compile exclusions are layout-contract failures with buildable nested crates, not generic source compilation failures.

### Partially supported

- **Artifact-evidenced recovery:** most sampled correct rationales cite distinguishing artifact evidence, but the sample is tiny, correct-only, post-hoc, and unreplicated.
- **Agent-facing legibility:** lower same-finder bytes after recovery is consistent with easier location, but success conditioning, stopping, tool serialization, artifact size, and finder policy remain bundled.
- **Implementation coverage:** the three-way label is useful, but 96.7% of labels originate from model-output consensus involving evaluated finders, with under-specified independent review.
- **Repeatability:** three trials show high panel agreement, but do not establish stable task-, artifact-, or provider-level reliability.
- **Low-prior validity:** the selected slice has larger artifact lift and strong sampled citations, but it is small, post-selected, and lacks held-out confirmation.
- **Finder selection:** calibration rules can reject saturated instruments, but selection on the same task pack is not transport validation.

### Unsupported

- behavioral correctness or full specification conformance;
- human readability or maintainability;
- successful audit, modification, extension, or preservation;
- intrinsic or recipient-independent artifact legibility;
- universal builder/model ranking;
- representative software or knowledge-work capability;
- total lifecycle efficiency or cost-effectiveness;
- security, safety, production fitness, professional validity, or readiness.

## Unique insight

> **Artifact legibility is a recovery-gated relation among propositions, evidence views, recipients, and stopping policies—not a scalar property of the artifact.**

BUILD-AND-FIND’s strongest contribution is not its ranking. It is the insistence that effort becomes interpretable only after the recipient recovers the relevant claim correctly and reliably. The paper’s own controls then force a second correction: even gated effort is recipient- and policy-relative.

For `skill-bench`, the reusable chain is:

```text
authoritative requirement / decision proposition
→ artifact realization and implementation-status evidence
→ recipient-visible representation and protected-evidence boundary
→ question / next-operation demand with accepted alternatives
→ recipient configured system and inspection policy
→ observed evidence access, citation, answer, and confidence
→ repeated correct recovery gate
→ endpoint-aware inspection / verification burden
→ downstream action and preserved consequences
→ lifecycle cost and bounded validity claim
```

Four separations follow:

1. **Traceability is not implementation.** A question can trace to a specification item that the artifact omits or contradicts. Coverage must remain a builder-side outcome.
2. **Correct recovery is not artifact-caused recovery.** Question wording and domain priors can yield the right label. Evidence access, citation entailment, restricted-view interventions, and prior controls are separate observations.
3. **Conditional effort is not intrinsic legibility.** It depends on recipient family, harness, tools, budget, stopping, success selection, and artifact representation. A claim must name this configured relation.
4. **Recovery is not successor utility.** Knowing which option is encoded does not show that a recipient can verify behavior, modify safely, preserve constraints, explain the design to a human, or maintain it under change.

### Relation to adjacent reviewed evidence

- **Handoff Debt** freezes partial work and varies predecessor context, observing continuation outcomes and effort. BUILD-AND-FIND freezes a completed artifact and asks source-traced questions. The latter provides a pre-action recovery diagnostic; the former provides a recipient-action test. Neither establishes human maintainability.
- **AfterVibe** asks a fresh recipient to regenerate behavior from an extracted specification. BUILD-AND-FIND reverses the information direction: the specification is hidden and the artifact must communicate selected choices. Together they motivate bidirectional tests—artifact→proposition recovery and proposition→artifact action—without treating either as authoritative-intent identity.
- **MAG** evaluates trace-derived procedural guides but lacks a real guide-consuming intervention. BUILD-AND-FIND contributes a recipient panel, prior controls, and evidence citation, while still stopping short of consequential use.
- **Artifact-view admissibility** supplies the correct implementation home: source, tests, documentation, configuration, and rendered views can carry different predicates, and a grader should state which representations are sufficient. BUILD-AND-FIND’s citation audit suggests source dominates this pack; restricted-view interventions remain unrun.
- **Metric/task-health/validity contracts** should preserve every denominator, scoring-set revision, finder calibration, missing cell, metric version, and claim ceiling. A saturated question bank can remain useful as a regression or effort probe without supporting a broad capability claim.

## Limitations and validity threats

1. Only two synthetic Rust task families and thirty questions are studied.
2. Task/specification authority rests on author review; no independent domain or professional validation is reported.
3. Specification-traced questions do not establish construct coverage or consequence relevance.
4. Question-only accuracy is 94.5%, leaving only 4.4 points of artifact-conditioned lift.
5. The low-prior subset contains only ten post-selected questions.
6. No held-out task pack confirms finder calibration or low-prior effects.
7. Four of six model families share native harness with family; model and harness effects are not factorially separated.
8. MiMo uses Claude Code, adding a non-native harness treatment.
9. Provider model snapshots and sampling seeds are not frozen.
10. Two build trials and three finder trials provide weak stochastic characterization.
11. Tasks, artifacts, and repeated trials are clustered, but no clustered uncertainty or hierarchical model is reported.
12. The logical view selects successful replacements after infrastructure failures; selection rules cannot be audited.
13. Root compile pass is not behavioral correctness.
14. Six “compile failures” are actually one-level layout violations with buildable nested crates.
15. The implementation audit uses selected evaluated finders to prelabel 696/720 pairs.
16. The consensus-prelabel rule, reviewer protocol, blinding, agreement, and error rate are absent.
17. Excluding non-gold/ambiguous claims creates a favorable finder-recovery set; implementation coverage must remain visible.
18. AELS’s arbitrary `η=0.1` has no stakeholder-loss calibration and can invite false scalar ranking.
19. It is unclear whether AELS fully penalizes omitted implementation rather than only missing recovery cells.
20. Exact-match multiple choice can reward question priors and option elimination.
21. The evidence audit samples only 72 correct answers—0.34% of scored rows.
22. Evidence citations are retrospective structured fields, not proof of causal use.
23. No wrong-answer, omission, contradiction, or accepted-alternative evidence audit is reported.
24. No auditor expertise, duplicate labels, adjudication, or agreement is reported.
25. Conditional effort drops failed runs and averages only all-correct attempts.
26. Missing all-correct cells are excluded from `R_b`; coverage is separate rather than integrated into the estimand.
27. Min-normalization is panel- and outlier-dependent.
28. Novel bytes include tool-call argument serialization and omit reasoning, verification quality, latency, and human burden.
29. Whole-run bytes are assigned to low-prior subsets, so subset effort is not identified.
30. No confidence intervals accompany effort scores, ranks, or affinity residuals.
31. The reported GPT-5.5-low `R_b` is 1.151 in Section 4.5 but 1.137 in Table 9.
32. Positive same-family affinity is descriptive and may reflect style, priors, harness, or chance.
33. Public task packs are contamination-prone; private packs are proposed but not evidenced.
34. More than 1.1B reported tokens produce a narrow two-task panel; dollar and human costs are absent.
35. No downstream modification, preservation, audit, or changed-requirement outcome is measured.
36. No human readability, maintainability, code-review, security, or professional-use study is conducted.
37. The claimed release is unavailable, blocking task, artifact, record, script, metric, and license audit.
38. Live reruns depend on mutable provider services and CLIs.

## Reproducibility and operational realism

Protocol reproducibility is **moderate from the paper**: the full source provides pseudocode, formulas, seeds, model/harness labels, versions, machine details, panel counts, metric definitions, control design, and aggregate tables. Denominator arithmetic and the stated aggregate token scale can be reconstructed.

Result reproducibility is **poor at review time**. The only claimed release endpoint is unavailable, and no immutable mirror was found. Therefore the 48 artifacts, 720 implementation labels, 1,872 formal/control records, 21,312 scored rows, rationales, byte-accounting events, environment hashes, generated reports, and analysis scripts cannot be inspected. The `1.151`/`1.137` effort discrepancy cannot be resolved, and model-assisted prelabels cannot be independently audited. The immutable source archive contains manuscript and figure/table assets, not the empirical package claimed in the paper.

Operational realism is useful but narrow. Generated repositories genuinely mediate between separate agents, and the protocol records packaging, read-only inspection, evidence citations, repeat runs, and recipient effort. Yet fixed MCQs substitute for natural successor goals, compile replaces behavioral verification, and no recipient must act on recovered information. The protocol should be treated as an artifact-communication diagnostic that can precede—not replace—counterfactual successor actions and professional review.

## Transfer to `skill-bench`

### Preserve

1. **Insert a pre-action recovery layer.** For selected consequential artifact propositions, ask a recipient that lacks the source pack to recover the encoded decision before undertaking the next operation.
2. **Trace each probe to a public-basis requirement and artifact realization.** Keep authoritative requirement, intended answer, accepted alternatives, artifact evidence, and implementation status distinct.
3. **Gate effort on reliable recovery.** Never call an artifact efficient because a recipient stopped early while answering incorrectly or inconsistently.
4. **Use recipient panels and report interactions.** Same-artifact recipient differences are evidence, not nuisance to average away.
5. **Run question-only/source-only and restricted-view controls.** Estimate priors and identify whether source, formulas, metadata, tests, comments, or rendered output actually carry the information.
6. **Preserve denominator ladders.** Artifact-present, structurally valid, behaviorally valid, implementation-eligible, scored, all-correct, and effort-contributing units must remain separate.

### Repair before reuse

1. **Independently label artifact realization.** Automated finder agreement may triage, but a held-out deterministic or qualified review must establish implemented/contrary/absent/ambiguous status, with disagreement and provenance.
2. **Pre-register low-prior probes.** Develop them on one pack and validate on another rather than selecting items from the same question-only outcomes.
3. **Require prospective evidence locators.** Grade citation existence, entailment, scope, valid time, and alternative exclusion for all answers, not only a small correct-only sample.
4. **Use accepted-alternative and corrupted-artifact controls.** Include equivalent structures, misleading documentation, stale metadata, omitted claims, and behaviorally correct but opaque artifacts.
5. **Report three effort views:** unconditional budgeted reliable-recovery rate; success-conditioned inspection/verification cost; and a joint cost-to-reliable-recovery frontier with failures/censoring explicit.
6. **Decompose effort.** Separate bytes opened, unique claims inspected, searches, validations, wall time, tokens, model calls, retries, and human review. Do not treat tool JSON length as professional burden.
7. **Cluster at the source work unit.** Repeat recipients while preserving task/artifact blocks, and report intervals for the exact displayed statistic.
8. **Add a consequential successor test.** After recovery, ask the recipient to modify, audit, explain, preserve, or decide; score endpoint quality and collateral effects separately from recovery.
9. **Count lifecycle cost.** Include authoring, artifact generation, indexing, recipient inspection, verification, failures, and expert audit.
10. **Keep claim ceilings machine-readable.** Recovery evidence can license a configured recipient–artifact relation, not human maintainability or professional readiness.

## Concrete repository actions

1. **No new build task.** The nonduplicate requirements fit existing handoff/counterfactual, artifact-view admissibility, metric-monitoring, task-health, trace, and validity contracts. A new “legibility schema” would duplicate current machinery.
2. Route this review to the next synthesis pass to add a recovery-gated handoff rung between structural/semantic artifact validity and successor action: `artifact proposition → independent realization label → recipient evidence view → prior-controlled repeated recovery → endpoint-aware effort → downstream consequence`.
3. If a future pilot uses this pattern, run one small cross-domain pair (for example spreadsheet assumptions and research-memo evidence) with pre-registered low-prior probes, an independently labeled corrupted-artifact set, two unlike recipients, and a real next-operation outcome before scaling model calls.
4. Revisit release conformance only if an immutable public BUILD-AND-FIND snapshot becomes available; preserve a new timing boundary rather than silently treating a later repository as paper-time code.

## Action items

- [x] Read the complete immutable v1 PDF/text and Appendices A–N.
- [x] Inspect the arXiv source archive and verify the sole release locator.
- [x] Reconcile artifact-present, compile-pass, eligible-pair, scored-row, control, and token denominators.
- [x] Audit prior/spec controls, implementation-label construction, repeatability, evidence sampling, conditional effort, affinity, and compile-layout sensitivity.
- [x] Preserve the unavailable-release boundary without inferring release contents.
- [x] Compare nonduplicatively with Handoff Debt, AfterVibe, MAG, artifact-view admissibility, and existing metric/task-health/validity machinery.
- [x] Define bounded transfer and claim ceilings without adding a duplicate build task.
