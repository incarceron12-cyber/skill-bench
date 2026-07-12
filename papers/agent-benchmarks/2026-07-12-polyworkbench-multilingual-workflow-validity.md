# PolyWorkBench: multilingual composition without a language-effect design

**Source type:** Deep review of the complete immutable arXiv v1 paper, with a complete v2 change audit and official-release search  
**Paper:** Hongliang Li et al., *PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents* (arXiv:2607.06008v1, 7 July 2026)  
**Immutable paper:** https://arxiv.org/abs/2607.06008v1  
**Local PDF (v1):** `data/papers/pdfs/2607.06008v1-polyworkbench.pdf` (SHA-256 `6373c753102b07282ae2acdf319334f640c715d6cac60a7725141ff52c011d8b`, 15 pages)  
**Local text (v1):** `data/papers/text/2607.06008v1-polyworkbench.txt` (SHA-256 `6b1e18ba73083ed98160da5867b72d6fcc5db4fc0ef614644f38c188ca64ee85`)  
**Current v2 PDF:** `data/papers/pdfs/2607.06008v2-polyworkbench.pdf` (SHA-256 `9147ee039e4efb1152144a59f46e56e42c230256ec4c51fea945773e406f950f`, 15 pages)  
**Current v2 text:** `data/papers/text/2607.06008v2-polyworkbench.txt` (SHA-256 `debee4c268673a66ad141026b8138aeaa4fd0efc700eb051fa9c0220bfe2bb0c`)  
**Release audit:** `data/sources/releases/2607.06008v1-polyworkbench/provenance.json`

> **Evidence boundary.** The arXiv API summaries contain no withdrawal or retraction notice. The discoverable official GitHub organization exposes only a static leaderboard site at pinned commit `0d1f7cd3168b2c4f8a83e5b522fc3195d256c959`; no task bundle, source pack, graders, trajectories, harness configuration, license, or downloadable data was found in the recorded searches. No reported trial was reproduced. The paper's task-construction and manual-inspection claims therefore remain author reports, not release-inspected evidence.

## Review judgment

PolyWorkBench identifies an important benchmark-design unit: language belongs on **workflow edges**, not only on task labels. Instructions, evidence, tool interfaces, intermediate representations, and deliverables can each impose different language and locale obligations. Its proposed 67-task portfolio and three-part evaluator also make heterogeneous workplace artifacts more visible than static multilingual QA.

But the experiment does not identify a multilingual effect. There are no matched monolingual equivalents, language swaps, translation-preserving counterfactuals, or factorial controls for language role, domain, artifact type, task difficulty, harness, and model. Per-language means reuse heavily overlapping tasks, have radically unequal support, and confound language with authored content and grader strictness. The paper nevertheless claims degradation “compared to monolingual counterparts” and compounding effects across reasoning and execution without reporting a monolingual comparator or trajectory-level causal analysis (v1 pp. 1–2, 7–9). The evidence supports configured-system scores on an unreleased, multilingual-by-construction task set—not multilingual capability, language-caused degradation, professional authenticity, or deployment reliability.

## One-sentence contribution

PolyWorkBench usefully treats instruction/source/output language assignments as a workflow composition problem, but its unmatched task portfolio cannot separate language-transition difficulty from domain, artifact, task, harness, evaluator, or sampling effects.

## Research question and contribution

The paper asks how language variation affects reasoning and decision trajectories in long-horizon agent workflows (v1 pp. 1–2). It contributes, by author report:

1. 67 manually curated tasks across Commerce (16), Knowledge (11), Legal (15), Localization (11), and Manufacturing (14);
2. baseline (29, estimated 6–8 steps) and stress (38, 8–12 steps) pools;
3. ten named languages assigned across instruction, source, and expected-output roles, with 59/67 tasks said to involve at least three languages;
4. heterogeneous source files and 262 expected output artifacts;
5. task-specific weighted structural `Grade`, executable Pytest, and an LLM judge;
6. 18 model×harness entries over ClaudeCode, OpenClaw, Hermes, and Codex.

The unique research direction is **cross-lingual trajectory coupling**: correctness must survive transformations between language-bearing workflow states. The paper does not operationalize that coupling as a measured path or intervention.

## Methodology and system

### Task provenance and construction

V1 says tasks are “manually curated” and describes domains, source types, estimated steps, time budgets, and expected artifacts (pp. 4–5), but gives no author count, qualifications, native-language proficiency, occupational sampling frame, expert review, public/proprietary-source manifest, rights process, or task-admission details.

V2 adds an entirely new §3.2 (pp. 4–5): each task is hand-authored by a “domain-familiar annotator”; public sources are used verbatim; proprietary-style artifacts are drafted natively; machine translation is not used for source files; one annotator authors instruction and end-to-end reference; discovered facts are back-injected into sources; and tasks are tested with at least three agents/harnesses before admission. These are consequential additions, not clarifications supported by newly released artifacts. “Domain-familiar” is undefined, one-person source/instruction/reference/grader co-design creates shared-blind-spot and benchmark-shaped-solvability risks, and outcome-conditioned admission can remove tasks that expose current evaluator or agent weaknesses. Back-injecting reference facts ensures discoverability by construction but may produce artificial evidence regularity.

Neither version reports legal/formatting conventions by jurisdiction, native-speaker or professional acceptance, inter-author review, task rejection counts, difficulty calibration, or whether a reference solution is unique. Labels such as legal analysis and manufacturing do not establish professional realism.

### Language allocation is a vector, not a label

The paper correctly distinguishes instruction, source, and output roles (v1 p. 5). Yet it does not publish a task-level matrix in the paper, and the release is absent. It is unclear whether “source language” means one dominant language, any language appearing in any of roughly 9.3 files, or every content-bearing segment; whether structured identifiers/numbers count as language-neutral; which language the tool UI and APIs use; what language internal reasoning uses; or which locale controls dates, decimal separators, currencies, units, collation, legal terminology, and document conventions.

The reported coverage is internally difficult to reconcile. Figure 2's displayed values imply broad per-role counts (for example English source 67/output 66/instruction 61 and Arabic source 30/output 28/instruction 24), while the prose says English “touched” 66 tasks and Arabic appears in one task; Appendix Table 3 likewise says Arabic has `n=1` (v1 pp. 4–5, 13–14). If Figure 2 values are percentages rather than counts, the figure/text do not label or explain that. Consequently, even the denominator behind “per-language mean Grade” is not auditable.

### Environments, tools, and artifacts

The diagrams list browser/search, Python or code editor, spreadsheet, database, calculator, and filesystem tools; tasks produce spreadsheets, reports, JSON, Markdown, legal documents, translations, dashboards, and analyses (v1 pp. 3, 5). The experiment says all harnesses share inputs, 1,800-second timeout, and evaluation protocol while scaffold differs (p. 6).

This is too thin for execution equivalence. There are no versions, images, network policy, locale/encoding settings, font/render availability, office software, browser/search snapshot, database state, filesystem isolation, retries, token budgets, context policy, tool permissions, invalid-run policy, or output collection rules. Those omissions are especially material for multilingual artifacts: shaping Arabic text, CJK fonts, Unicode normalization, spreadsheet locale parsing, right-to-left layout, date/number formats, and PDF extraction can fail in the environment rather than in semantic reasoning.

### Evaluators and evidence views

`Grade` is the primary metric and gives task-specific weighted partial credit; Pytest checks formats, numbers, schemas, API outputs, or behavior where applicable; the judge assesses coherence, completeness, faithfulness, and overall quality under “standardised prompts” (v1 pp. 5–6). No criterion definitions, weights, code, judge model/version/prompt, artifact render/extraction pipeline, judge input language, reference exposure, multilingual calibration, native-human labels, applicability counts, or invalid/abstention handling are supplied.

The three axes are not demonstrated to be independent. The paper reports Grade–Pytest correlation of 0.86 in v1 (0.85 in v2) because they target overlapping structural elements; the judge is weakly correlated and saturated. V1 reports Grade–judge `r=.22`, although its Figure 5 graphic labels `.22`; v2 changes this to `.18`, changes several distribution counts, and changes reverse disagreement from 70 to 97 while still stating `n=1,206` (v1 pp. 8, 13–15; v2 pp. 8, 13–15). Disagreement can reveal construct plurality, but without calibrated multilingual human judgments it does not establish that the judge detects valid “semantic degradations.” A judge may instead react to fluency, verbosity, genre, extraction failures, or language-specific bias.

### Experimental design and metrics

Pass@1 is one run's mean Grade over 67 tasks. “Pass@3” is the per-task best Grade over up to three runs, reported for entries with `nruns ≥ 2` (v1 pp. 6–9). Calling a best-of-two entry Pass@3 is semantically wrong; it also compares systems under unequal attempts. Best-of-k is an operational resampling policy, not evidence that failures are “transient” or that a system can be deployed at higher quality unless a valid selector, added cost, latency, and failure dependence are measured.

The 18 entries are not a crossed model×harness factorial. Availability is sparse, and model versions, provider settings, decoding, prompts, budgets, retries, and dates are not frozen. Same-model harness spreads therefore show configured-run differences, not isolated scaffold causal effects. No confidence intervals, task-clustered uncertainty, exact-instance repetitions for all entries, missing-run ledger, cost, token use, or significance tests are reported.

## Evidence and results

V1 reports best Pass@1 of .921 for Claude Opus 4.8+ClaudeCode and substantial domain/harness variation (pp. 6–9). It reports weak Grade–judge agreement, high deterministic/judge disagreement, and larger best-of-k headroom for lower-scoring configurations. These descriptive results establish heterogeneity within the authored portfolio.

They do **not** establish the paper's central causal interpretation:

- no monolingual counterpart appears in the design or results;
- no identical task is language-swapped while facts, artifact, tool, and grader remain fixed;
- language support is unequal (Arabic is explicitly `n=1` in Appendix A.2);
- per-language task sets overlap, so columns are neither independent nor compositionally comparable;
- language is entangled with domain, difficulty pool, artifact genre, source count, source quality, output strictness, and evaluator;
- the paper's “comprehension” versus “cross-lingual coordination” failure modes come from unspecified manual inspection, with no coding protocol, counts, agreement, or released traces;
- no intermediate state observation shows that comprehension was initially correct and alignment later drifted;
- no monolingual human baseline or professional threshold establishes task feasibility and output acceptance.

The strongest finding is thus that **scores vary across configured systems and slices of this multilingual portfolio**. The language attribution remains a hypothesis.

## V1 → v2 change audit

V2 is not merely typographic:

1. adds affiliations/work-history notation and changes displayed date metadata;
2. adds the new task sourcing/construction/admission protocol (§3.2), including native drafting, no machine translation, back-injected anchors, three-agent/harness admission tests, and claimed manifest release;
3. reorganizes Table 1 by harness and changes run counts for several entries;
4. changes DeepSeek-v4-Flash+OpenClaw Pass@1 from `.557` to `.708`, its domain/language cells, and its claimed harness spread;
5. changes Qwen-Agent-World+Hermes and DeepSeek+Codex from one to three runs and adds Pass@3 values;
6. changes Grade/Pytest/judge correlations and disagreement/distribution counts while retaining 1,206 task-entry observations;
7. changes the count of entries with repeated runs from 13 to 15.

No change log, released result table, trajectories, or explanation supports forensic reconciliation. Skill-bench should cite the immutable version actually reviewed and treat mutable leaderboard results as new measurements, not silent corrections.

## Unique insight

> **A multilingual workflow is a chain of meaning-preservation obligations, not a bag of language tags.**

For each edge from instruction → evidence → extracted state → calculation/tool state → artifact → grader observation, an evaluation should specify:

1. source and target language/locale;
2. authority and provenance that must survive;
3. invariant semantic fields (entities, numbers, dates, units, negation, modality, scope, exceptions);
4. locale-sensitive fields allowed or required to transform;
5. artifact conventions and downstream reader/use;
6. transformation evidence and accepted equivalences;
7. observer language, representation, and competence;
8. failure location versus earliest supported cause.

This edge-level contract distinguishes source-comprehension failure, semantic transfer loss, locale-format failure, tool-interface mismatch, professional-convention failure, and grader-observation bias. PolyWorkBench motivates this object but reports only coarse task-level roles and outcomes.

## Limitations and validity threats

1. **No identifying comparator.** The central multilingual degradation and compounding claims lack matched monolingual or language-swapped conditions.
2. **Composition confounding.** Languages are inseparable from task, domain, artifact, difficulty, and rubric mixtures.
3. **Coverage ambiguity.** Figure/prose language counts conflict or are unlabeled; Arabic `n=1` cannot support generalization.
4. **Unreleased benchmark.** No inspectable tasks, source packs, criteria, tests, prompts, trajectories, manifests, or results were found despite v2's release claim.
5. **Weak authoring provenance.** “Domain-familiar” is undefined; expertise, native proficiency, rights, review, and acceptance are unreported.
6. **Single-author co-design risk.** Source, instruction, reference, anchors, rubrics, and tests may encode one benchmark-shaped path and shared errors.
7. **Outcome-conditioned admission.** Requiring separation by current agents/evaluators selects for benchmark health against the development systems, not construct validity.
8. **No language-transition trace.** Claimed coordination failures are not localized through observed intermediate states.
9. **Judge unvalidated across languages.** No multilingual human calibration, agreement, evidence-view specification, or bias audit supports semantic-quality interpretation.
10. **Metric dependence.** Grade and Pytest overlap; the judge appears saturated; flattening or informal triangulation does not yield one validated construct.
11. **Unequal attempts.** “Pass@3” includes two-run entries and rewards oracle best-of-k without selector cost or deployable selection evidence.
12. **Sparse harness matrix.** Same-model comparisons are nonrandom, incomplete, and under-specified; harness causality is unsupported.
13. **No dependence-aware uncertainty.** Means and Pearson correlations ignore repeated tasks, shared templates, overlapping language memberships, model×harness clustering, and stochastic runs.
14. **No operational accounting.** Costs, tokens, latency, retries, invalid/infrastructure failures, and selector burden are absent.
15. **Environment under-specification.** Locale, Unicode, font/render, office, search, network, and isolation state can generate language-correlated failures.
16. **No professional criterion.** Workplace labels and structured artifacts do not establish representativeness, legal correctness, stakeholder usability, or consequence.
17. **Version instability.** Material result and method changes arrived in v2 without a change log or inspectable evidence.
18. **Contamination and maintenance unknown.** Public-source overlap, model exposure, search leakage, source freshness, task secrecy, and benchmark evolution policies are unspecified.

## Reproducibility and operational realism

**Paper inspectability: moderate.** Both immutable versions specify portfolio counts, broad roles, metrics, and aggregate tables. V2 gives a more concrete author-reported construction pipeline.

**Artifact inspectability and exact reproduction: very low.** The official static site has no executable release; model/harness/environment/judge identities are incomplete; raw outputs, criteria, tests, result tables, and attrition are absent. Material v1/v2 changes cannot be independently reconstructed.

**Operational realism: plausible substrate, unvalidated work.** Multilingual files, spreadsheets, contracts, receipts, logs, localization formats, and multi-artifact deliverables are credible ingredients. Authored scenarios, back-injected anchors, no occupational sampling, no stakeholder trial, unspecified environments, and no expert acceptance leave authenticity and consequence unestablished. Maintenance would require language/locale expertise, source-rights and freshness review, renderer/tool locks, grader recalibration, bridge cases, and versioned results.

## Transfer to skill-bench

### Retain

- Treat language as independently typed instruction/source/tool/output/grader roles.
- Preserve heterogeneous native artifacts and plural structural/functional/semantic evidence.
- Report configured model+harness outcomes rather than model-only scores.
- Keep domain, artifact, language, and difficulty slices visible rather than trusting one aggregate.
- Use grader disagreement diagnostically rather than automatically averaging it away.

### Repair

1. Add edge-level language/locale and meaning-preservation records to existing task/source/artifact/check contracts, including authority, numeric/unit/date/modality invariants, allowed localization transforms, and observer language.
2. Build matched equivalent forms: native monolingual, instruction-swapped, source-swapped, output-swapped, full multilingual, and locale-format controls while freezing facts, artifact requirements, environment, rubric, and configured system.
3. Use qualified bilingual/domain reviewers to establish equivalence and record disagreements; do not treat machine or analyst translation as inherited expert approval.
4. Separate source comprehension, cross-language semantic transfer, tool/locale execution, artifact convention, and grader-language bias in traces and root-cause labels.
5. Report task-level language-role incidence and denominators; model overlap/dependence among multilingual memberships and template families.
6. Calibrate judges against multilingual expert observations using identical evidence views, invalid/abstention states, and language-specific agreement/uncertainty.
7. Pin Unicode normalization, locale, fonts, renderers, spreadsheet parsing, office software, search/network, and artifact extraction as trial components.
8. Replace unequal “Pass@3” with explicit attempt policy, valid selector, total cost/latency, and per-attempt/reliability estimands.
9. Version tasks, sources, graders, leaderboard measurements, and change reasons independently; preserve bridge cases across revisions.
10. Bound claims to the exact workflow-language edges, languages, domains, artifact types, and configured systems supported.

## Relevance

PolyWorkBench is directly relevant as early evidence that multilinguality should be represented throughout an agent workflow rather than as one metadata field. Its most useful transfer is a cross-domain **language-transition validity boundary**, not its aggregate leaderboard. It does not justify narrowing skill-bench to localization or any named language.

## Concrete changes

1. **Build/validation task:** add a compact multilingual edge-equivalence conformance slice to the existing benchmark-bundle/artifact-view machinery: one invariant fact pack; matched instruction/source/output language substitutions; numeric/date/unit/negation/authority invariants; pinned locale/render environment; bilingual observations; and planted semantic, formatting, provenance, and grader-language failures.
2. **Consolidation:** add PolyWorkBench to the multilingual/workflow landscape with a bounded claim: strong motivation and broad authored composition; weak causal attribution, release inspectability, professional validation, uncertainty, and reproducibility.

## Claim boundary

The immutable v1 paper establishes that the authors describe 67 multilingual-by-construction workplace tasks and report aggregate Grade/Pytest/judge results for 18 model×harness entries. V2 adds an author-reported construction protocol and materially revises runs, scores, correlations, and disagreement counts. The discoverable official release establishes only a static leaderboard site. These sources do not establish a causal multilingual penalty, compounding trajectory effect, language-general capability, task equivalence, judge validity across languages, professional authenticity, isolated harness effects, best-of-k deployability, exact reproducibility, safety, productivity, or deployment readiness.
