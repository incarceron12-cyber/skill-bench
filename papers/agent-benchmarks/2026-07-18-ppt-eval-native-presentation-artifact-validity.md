# PPT-Eval: plural artifact views improve edit grading, but an unversioned render transformation and rubric-program validity bound the claim

## Source and review status

**Deep review of the complete immutable primary paper and a commit-pinned official post-v1 release.** I read the complete 41-page arXiv v1 PDF/text and audited all 120 released task records and 120 rubric trees. The repository snapshot is eight days newer than v1, so it is acquisition-time implementation evidence—not proof of the paper-time tasks, decks, rubrics, graders, environments, results, or human study.

- **Paper:** Apurva Gandhi et al., *PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks*, arXiv:2606.31154v1, <https://arxiv.org/abs/2606.31154v1>
- **Venue stated by paper:** ICML 2026, PMLR 306
- **Version read:** immutable v1, submitted 30 June 2026; no withdrawal notice in acquired metadata
- **Date read:** 18 July 2026
- **Local PDF:** `data/papers/pdfs/2606.31154v1-ppt-eval.pdf` (41 pages; SHA-256 `d3ea7dce2a094088c42d25a3630a870f93e3ae8e471723ce48a04d2d4d816fea`)
- **Local full text:** `data/papers/text/2606.31154v1-ppt-eval.txt` (SHA-256 `35f8b10b967ed24dd95ebdc0111eec61b3482dd48294966d098b13bc5ccdbfa9`)
- **Official release audited:** <https://github.com/microsoft/ppteval/tree/1b8b55a29e48fdc65d423689b6f2370ad91beeea>, commit dated 8 July 2026
- **Release provenance:** `data/sources/releases/2606.31154v1-ppt-eval/provenance.json`
- **Static release audit:** `data/sources/releases/2606.31154v1-ppt-eval/release-audit.json`

The 259-file snapshot contains the runner, seven GUI model adapters, Claude Code path, 120 task records, 120 executable rubric files, twelve source-deck URLs, attribution records, and unit-test sources. It contains **no source `.pptx` bytes, cached original slide ZIPs, agent attempts, human attempts or labels, rubric meta-evaluation attempts, criterion outputs, trajectories, result tables, or cost ledger**. All Python source compiles. The unit suite could not be collected in the review environment because `azure.identity` was absent; this is an environment observation, not a released-test failure. End-to-end replay was not possible from released bytes and would additionally require mutable remote decks, OneDrive, PowerPoint Online or local renderers, commercial model endpoints, and credentials.

## One-sentence contribution

PPT-Eval contributes a rare, inspectable mixed-observer instrument for native presentation editing—120 GUI tasks, task-specific executable rubric trees, OOXML/package diffs, rendered-slide judgments, collateral-change checks, partial credit, three-run configured-system results, and a human-authored ordinal meta-evaluation—but its remote PowerPoint-Online normalization, compensation-based “critical” semantics, heterogeneous executable criterion programs, weak alternative-validity evidence, undisclosed empirical artifacts, and non-independent validation cap conclusions at **configured edit-conformance scores under a particular measurement pipeline**, not professional presentation quality, human equivalence, general GUI capability, workflow value, or readiness.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through a bounded presentation-artifact stress case. It does not argue that `skill-bench` should become a PowerPoint benchmark. Presentation editing makes a cross-domain measurement problem concrete:

```text
authorized source state
→ normalized benchmark state
→ public requested delta
→ native structural/package evidence
→ rendered evidence
→ semantic/aesthetic judgment
→ preservation evidence
→ rubric-program aggregation
→ task decision
→ professional use claim
```

PPT-Eval is substantially stronger than endpoint-only office benchmarks in the middle of this chain. It asks whether a requested edit exists, how much of a compound edit was completed, and whether unrelated state changed. It also shows why “multiple evidence views” is not sufficient by itself: every view must have a versioned transformation, criterion-specific admissibility, failure state, invariance policy, and validated observer. A PowerPoint Online render, a `python-pptx` object, an OOXML diff, and a VLM answer are not interchangeable witnesses.

The concrete evidence is unusually useful: the current release is sufficiently inspectable to census all 704 rubric nodes and 481 executable leaves, trace the source-deck hydration path, and identify exact grader semantics. Useful completion is therefore a retain/repair/test account that feeds existing cross-domain artifact-view and rubric contracts without a presentation-specific schema or pilot.

## Research question and defensible claim boundary

The paper asks how well computer-use agents edit presentations in PowerPoint Online when tasks require text, images, tables, graphics, layouts, transitions, and animations, and how partial progress can be measured when several outputs may be valid (Sections 1 and 3, pp. 1–6).

The evidence supports these bounded claims:

1. The paper and later release define 120 task records over twelve presentation identities, exactly ten tasks per deck: 51 Easy, 39 Medium, and 30 Hard.
2. The released instrument combines native package structure, `python-pptx` state, custom OOXML animation/transition extraction, rendered slide images, and LLM/VLM judgments through task-specific rubric programs.
3. Six annotators reportedly spent about 150 hours revising model-drafted rubrics in two rounds, including a cross-review pass (Section 3.5.3, p. 6).
4. On an author-constructed meta-evaluation of 30 tasks and 2–4 attempts per task, the paper reports Kendall's τb `0.77`, Spearman's ρ `0.84`, and category accuracies from `44.44%` to `100%` (Sections 4.1 and 5.2, pp. 6–9).
5. Under the paper's configured GUI packages, three-run mean success ranges from `0.14` to `0.45`; Claude-4.5-Opus reports `0.45` perfect-score rate and `0.57` average score. A Claude Code/Claude-4.5-Opus API package reports `0.62/0.81`, and five human participants report `0.80/0.90` (Table 1, p. 8).
6. Repeated grading of 61 VLM-using tasks shows low reported variance over five evaluator runs; switching the VLM from Claude-4-Sonnet to GPT-4.1 yields MAE `0.1` and 78.3% of scores within ±0.1 on the evaluated Claude trajectories (Appendix B.5, p. 28).
7. The later release makes the task/rubric program much more inspectable than the paper alone, even though it does not reproduce the empirical tables.

The evidence does **not** establish that the twelve decks sample presentation work; that every hidden criterion is a fair, complete, alternative-tolerant translation of the public request; that the changing PowerPoint Online transformation preserves instrument identity; that rank/category agreement calibrates criterion correctness or a professional threshold; that humans and agents receive equivalent tools, time, or feedback; that one scalar score measures presentation quality; that GUI/API differences isolate interface effects; or that any score supports productivity, substitution, procurement, safety, or readiness.

## Methodology and system

### Task source, selection, and authority

The benchmark starts from twelve publicly available Internet Archive decks, selected for feature diversity and modified into 120 editing tasks (Section 3.3 and Appendix A, pp. 4 and 11–14). The tasks span text changes, bullets, image operations, shapes, diagrams, tables, themes, hyperlinks, transitions, and animations. Difficulty is an expert designation grounded in estimated steps, precision, and feature complexity, but no rater count, assignment, independent agreement, calibration, or outcome-independent rule turns Easy/Medium/Hard into a measured scale.

Tasks are generated with model assistance, filtered for feasibility and duplicate intent, and manually executed before admission (Appendix A.2–A.3, pp. 12–15). This is a useful **solvability-witness process**. It is not a workplace-demand sample: there is no source population of requests, user or recipient, organizational context, original desired outcome, frequency/consequence weighting, rejected-task ledger, author-by-task provenance, or evidence that modifications preserve what the original deck was for. Exactly ten tasks per deck is deliberate coverage, not representative sampling.

The release's `ATTRIBUTION.md` is better than omitting source lineage, but its rights summary should not be accepted mechanically. Its own list records ten Public Domain Mark 1.0 items, one CC BY 4.0 item, and one CC0 item, while the prose says 11 of 12 are Public Domain Mark. More importantly, Public Domain Mark is a status-marking tool, not a license or dedication, and Internet Archive metadata does not itself prove that an uploader held all embedded image/font/content rights. Source URL, uploader, asserted rights marker, benchmark transformation, and actual authorization remain separate fields.

### Hydration creates a transformed benchmark substrate

The most important implementation fact is absent from the paper's high-level results: the released repository does not carry the initial decks. `data/files/PowerPoint/files.txt` supplies twelve mutable download URLs. `hydrate_data.py` then:

1. downloads each remote deck;
2. uploads it to OneDrive;
3. creates an anonymous edit link;
4. opens it in PowerPoint Online through Playwright Chromium;
5. downloads a slide-image ZIP; and
6. downloads the **PowerPoint-Online-mutated** `.pptx`, explicitly rather than copying the source.

This normalization is sensible engineering. Opening the same source in PowerPoint Online can mutate OOXML, so comparing an agent-edited online file against an untouched Internet Archive file would misattribute platform rewrites to the agent. But the normalization is itself part of the instrument:

```text
remote URL bytes + acquisition time
+ OneDrive/PowerPoint Online build and tenant behavior
+ fonts/rendering/browser state
→ normalized PPTX + cached slide ZIP
```

None of those normalized outputs is released or checksum-pinned. A future hydrator may receive different bytes, a changed web application, different font substitutions, altered OOXML canonicalization, or a different renderer. Thus the benchmark's authoritative initial state is not the cited Internet Archive file and not reconstructibly frozen; it is an unversioned remote transformation result.

### Environment and configured systems

The paper evaluates seven GUI systems using their native action spaces with at most 30 model decisions per task, concurrency three, and approximately 3.5 hours per suite run (Section 4.2, p. 7). The systems differ in endpoint, image history, coordinate representation, action vocabulary, parsing, reasoning, and likely provider defaults. The API baseline uses Claude Code, Claude-4.5-Opus, and an Anthropic presentation Skill rather than the GUI environment (Section 4.4 and Appendix G, pp. 7 and 40–41).

The release makes many components visible, including 1024×768 model configurations, action adapters, sandbox orchestration, and a strict `score == 1.0` success flag. It also contains newer post-v1 configurations such as GPT-5.5 and Claude Opus 4.7, demonstrating active evolution; repository presence cannot be projected backward into Table 1.

The GUI/API contrast is therefore a comparison of configured packages, not a causal estimate of GUI versus API access. The paper itself notes API feature limits, but task/tool compatibility, model, scaffold, procedural Skill, observation, repair affordances, and output path all change together. A model-specific task-category heatmap likewise mixes task, deck, criterion, tool affordance, and observer difficulty.

### Rubric authoring and executable criterion programs

Claude-4-Sonnet and GPT-4.1 draft rubric trees and leaf programs. Six human experts revise them in two rounds, exchanging decks for cross-review; the paper reports about 150 hours (Section 3.5.3, p. 6). This is a substantive human–model authoring pipeline and a useful response to the labor cost of dense artifact checks.

The release exposes the realized instrument:

- 120 JSON rubric files;
- 704 total nodes, 378 marked critical and 326 non-critical;
- 481 leaf scorers, all embedded Python functions and all syntactically parseable;
- at most two edges from root to leaf;
- lexical evidence of `python-pptx`/`Presentation` in 265 leaves, `ppt_diff` in 201, modified screenshots in 109, original screenshots in 53, `vlm_call` in 107, and `llm_call` in two;
- collateral/unchanged language in 184 leaves across 106 rubrics; and
- only three rubric files with explicit “alternative” or “equivalent” language under a conservative lexical scan.

These are static census facts, not evidence that every function is correct. Each leaf is an executable measurement program with its own target selection, tolerance, exception policy, model prompt, output parsing, and evidence assumptions. For example, the released `3-007.json` checks the added `vCPU4` element through several independent-looking VLM questions plus a text comparison and animation diff. Those leaves can share the same screenshot, object, and prerequisite, so they are correlated observations, not independent evidence.

Embedded code improves inspectability but expands the trusted computing base. Rubric JSON executes Python with presentation paths and model-call functions in global context. The release does not show scorer sandboxing, capability restriction, static safety policy, criterion coverage testing, or planted adversarial artifacts. Syntax validity is only the first gate.

### “Critical” is a weighting label, not a requirement gate

The paper replaces Mind2Web 2's gate-then-average rule with:

`max(0, mean(critical children) - 0.3 × (1 - mean(noncritical children)))`

when both child types exist, and a simple mean otherwise (Section 3.5.2, pp. 5–6). This intentionally rewards partial progress. It also changes the semantics of “critical”:

- a zero critical child can be compensated by other critical children;
- when all children are critical, they simply average;
- a non-critical failure can reduce an otherwise complete score below 1; and
- because released success requires exactly `score == 1.0`, every included non-critical child becomes mandatory for binary success even though it is described as secondary.

Thus partial score and perfect-score rate have different obligation semantics. The partial score is a compensatory progress index; SR is strict conjunction-like only at the final numeric endpoint, including secondary penalties. Neither automatically equals task completion, and neither is calibrated to user acceptance. “Critical,” “mandatory for SR,” “professional blocker,” and “diagnostic checkpoint” should be separate typed properties.

Root-level metadata also drifts: 97 rubric roots are marked critical and 23 non-critical, while only subsets declare aggregation metadata. Whether root criticality matters depends on the external `ai-rubric==0.2.5` implementation and call-time defaults. Exact score identity therefore binds rubric JSON, library version, compute strategy, and non-critical weight—not rubric files alone.

### Native/package diff evidence

`ppteval/verify/ppt/diff.py` is a major strength. It compares presentation packages and extracts slides, titles, layouts, notes, shape counts, text, content hashes, relationships, transitions, and animation effects beyond ordinary `python-pptx` coverage. This enables must-preserve and forbidden-change checks that screenshots cannot support. The audit found collateral-change language in 106 of 120 rubric files, a materially stronger pattern than benchmarks that only inspect requested endpoints.

But native checks have limits:

- OOXML/package differences are representation-sensitive and can change under PowerPoint normalization or save operations;
- object identity and ordering can drift while appearance remains equivalent;
- object property equality does not establish visual acceptability;
- animations/transitions require temporal playback semantics, not only presence of XML records;
- broad “other slides unchanged” checks often compare selected text, counts, or hashes rather than every relevant property; and
- no released alternative-artifact suite shows false-fail behavior on equivalent edits.

The right interpretation is criterion-specific structural evidence, not a canonical truth representation.

### Rendered/VLM evidence and renderer identity

`PPTVerifier` detects visual need by searching embedded function source for the string `vlm_call`. It then prefers a sibling ZIP of cached original slides, uses a sibling modified ZIP if present, or generates screenshots. The default is PowerPoint Online; documented local modes include Windows COM, LibreOffice+Poppler, and LibreOffice+Ghostscript. `slide_screenshots_utils.py` also implements fallback across rendering stacks after a primary local conversion fails.

This is operationally robust but measurement-sensitive. PowerPoint Online, desktop PowerPoint, LibreOffice, Poppler, ImageMagick, and Ghostscript can differ in fonts, SmartArt, equations, crop, gradients, animation states, line wrapping, and layout. Automatic fallback can convert a declared renderer failure into a score from a different observer without a corresponding score identity change. Cached originals and freshly generated candidates can also come from different times or transformations. Resolution is propagated from the first original image where possible, but resolution equality does not establish semantic render equivalence.

The retry logic appropriately distinguishes globally missing screenshots as `ScreenshotsUnavailableError`. Yet rubric leaves also contain local `try/except Exception` branches; the static census found 120 such leaves in 55 rubrics and only 34 leaves mentioning the typed screenshot-infrastructure error. Depending on the function, model/parser/observer failure can still become score 0 or partial credit. A complete instrument needs typed `criterion_fail`, `invalid_artifact`, `observer_invalid`, `insufficient_evidence`, and `infrastructure_retry` states at every leaf, not only at the outer screenshot gate.

VLM leaves often reduce open responses through substring tests such as YES/PARTIAL/NO or GOOD/POOR. These parsers and prompts are inspectable, but no released conformance suite tests negation, mixed answers, prompt injection in slide text, low-resolution labels, culturally contingent aesthetics, or valid alternate layouts. A visual judge can answer what a rendered slide appears to show; it cannot prove source identity, editable structure, transition timing, accessibility, or recipient usefulness.

### Natural-language explanation is a presentation layer

Leaf reasons are recursively summarized by an LLM into natural-language feedback (Section 3.5.2 and Appendix D, pp. 6 and 29). This may help users inspect a score, but it is not additional evidence. The explanation model receives child labels, descriptions, scores, and reasons, then paraphrases them. It can improve readability while introducing unsupported causal language. Score observations and explanation generation should remain separately versioned, and explanation faithfulness should be tested against the exact criterion ledger.

## Meta-evaluation: useful ordinal stress testing, not criterion or professional validity

### Constructed progress attempts

For 30 sampled tasks—reported as two or three per file—human annotators create 2–4 artifacts spanning authored categories: No Progress, Some Progress `(0, 0.5)`, Significant Progress `[0.5, 1)`, and Perfect Completion `1` (Section 4.1, p. 6). The rubric score is compared with the intended interval. Table 2 reports 100%, 44.44%, 61.54%, and 88.89% category accuracy plus τb `0.77` and ρ `0.84`.

This is valuable **measurement-program stress testing**: authored artifacts deliberately occupy the score range, reveal missing checks, and expose rubric bugs before agent evaluation. The reported percentages are consistent with small category denominators such as 30/30, 12/27, 16/26, and 24/27 (110 artifacts total), although the paper does not publish counts or the attempt set. That matters because intermediate-class errors are substantial and uncertainty cannot be computed from the paper.

The design does not validate independent human judgment in the usual sense:

1. the same project creates tasks, rubrics, expected progress categories, and attempts;
2. the expected labels are broad authored intervals, not blinded professional acceptance decisions;
3. rubric defects found during meta-evaluation are fixed **after** measurement, so Table 2 evaluates an earlier instrument while Table 1 uses a later undisclosed one;
4. no frozen holdout tests whether those repairs generalize;
5. no independent raters score criterion satisfaction or full artifacts;
6. no inter-human agreement, rater assignment, blinding, adjudication, class confusion, criterion sensitivity, or clustered interval is reported; and
7. naturally occurring agent failures, corrupt packages, renderer disagreements, prompt-injected slides, and structurally different valid completions are not the stated validation population.

The paper's qualitative disagreement cases are appropriately candid: wrong-slide human errors, culturally sensitive emoji judgments, VLM hallucinations, and coarse boundaries between partial classes (Section 5.2 and Appendix B, pp. 9 and 24–28). These examples demonstrate that the evaluator and authored category can disagree for several causal reasons; they do not estimate each reason's prevalence.

### Repeatability is not accuracy

Five repeated grader calls on 61 VLM-using tasks show low mean/median variance, and a second VLM gives MAE 0.1 with 78.3% within ±0.1 (Appendix B.5, p. 28). This supports repeatability on selected existing trajectories. It does not establish correctness: two stable models can share the same blind spot, and MAE 0.1 can change exact-1 success or threshold-near decisions. The paper does not report task-level paired distribution, rank changes, exact-success flips, model prompts/versions, seeds, invalid calls, or intervals.

## Human baseline and empirical results

Five participants separate from the six rubric curators—one each from QA, software engineering, marketing, data science, and graduate study—attempt the suite (Section 4.3, p. 7). Table 1 treats these five people as five runs and reports mean `0.80` SR and `0.90` score, with cross-person SD `0.04/0.03` (Appendix E.2, p. 31).

This is a useful convenience-human comparator, not an expert ceiling or matched experiment. The paper omits participant-level PowerPoint proficiency, recruitment, compensation, time limit and actual time, task order, practice, use of search/help, interface/version, retries, failures, missing tasks, and whether the same 30-step or observation constraints applied. Different occupations do not define a sampled population. Cross-person SD mixes person skill with task order and environment; it is not run-to-run human reliability.

The GUI table averages three suite runs per agent. A full nominal GUI design is 120 tasks × seven systems × three runs = 2,520 task attempts, with another 360 for the API baseline and 600 human task-person cells if all participants completed all tasks. The paper does not release a ledger reconciling attempted, environment-valid, agent-valid, artifact-valid, renderer-valid, judge-valid, retried, excluded, and scored cells. Outer orchestration distinguishes some infrastructure failures in the later release, but paper denominators and retry policy are not reconstructible.

The result pattern is descriptive and plausible: configured systems often make partial progress; advanced structure is harder; GUI and API packages have different strengths; three-run suite SDs vary; and 30 steps leaves many tasks unfinished. Yet exact `1.0` SR is hypersensitive to every leaf, floating aggregation, VLM output, non-critical penalty, and renderer. Average score is compensation-based and criterion-tree-dependent. Neither is an externally calibrated rate of acceptable presentations.

The API package's advantage does not show that API access is intrinsically superior. Conversely, a GUI success where `python-pptx` lacks SmartArt or animation support demonstrates feature-access compatibility, not general visual reasoning. All rankings name complete model–harness–environment–rubric–renderer–judge packages.

## Release audit and reproducibility

The post-v1 release is a meaningful contribution. It exposes the exact task registry and rubric programs, custom PPT diff, renderer routing, OneDrive hydration, GUI and CLI paths, strict success semantics, unit-test sources, and MIT-licensed code. All 481 embedded rubric functions parse as Python and the package compiles.

Exact paper reproduction remains weak:

1. **No frozen initial substrate.** Twelve URLs are present, but no source or normalized PPTX/ZIP bytes and no hashes bind the benchmark state.
2. **Remote transformation.** OneDrive and PowerPoint Online mutate and render every deck through an unpinned service/UI path.
3. **No paper result artifacts.** Attempts, screenshots, trajectories, grader outputs, human artifacts/labels, run ledger, and table builder are absent.
4. **No meta-evaluation corpus.** The 30 selected tasks, 110-ish authored attempts, intended categories, pre-fix rubric versions, repair diff, and holdout are absent.
5. **No exact paper-time commit.** The snapshot is eight days post-v1 and already contains later model configurations.
6. **Mutable judges.** Commercial LLM/VLM endpoints, prompts from an external rubric package, and provider behavior define scores.
7. **Renderer variability.** Online, COM, and LibreOffice-derived images are not shown equivalent; local fallback can change the evidence generator.
8. **Dependency breadth.** The package pins some core libraries but includes broad and mutable dependencies such as `screenenv`, `litellm`, and many enterprise extras; no complete lock or execution image is released.
9. **Test boundary.** Static compilation passed; local test collection stopped on an absent Azure dependency; no end-to-end fixture can run without missing decks/services.
10. **Rights summary inconsistency.** Attribution exists but miscounts rights markers and overstates Public Domain Mark semantics.

Reproducibility is therefore **strong for static inspection of the eight-day-post-v1 measurement design, moderate-to-low for assembling a new PPT-Eval-like run while remote services remain compatible, and absent for reproducing v1's exact score and human tables**.

Operational realism is bounded but meaningful. Native `.pptx` editing, existing heterogeneous decks, PowerPoint Online, GUI actions, partial completion, formatting, complex objects, and collateral damage are real artifact-engineering challenges. The tasks remain short explicit edits without stakeholder clarification, source conflict, organization-specific brand standards, narrative restructuring, factual review, accessibility, collaborative revision, approval, handoff, or downstream presentation use. The benchmark measures editing microtasks, not the full work of creating a persuasive, accurate, usable presentation.

## Unique insight: artifact transformations and rubric programs are first-class parts of the benchmark

PPT-Eval's deepest transferable lesson is that **plural evidence views require a transformation-and-program validity record, not merely a list of files and graders**.

The benchmark does not grade “the PowerPoint file” directly. It grades outputs of a chain:

```text
Internet Archive bytes
→ PowerPoint Online normalization
→ normalized OOXML + cached render
→ configured agent mutation
→ downloaded OOXML + cached/fresh render
→ native diff / object queries / model judgments
→ executable leaf programs
→ compensatory tree aggregation
→ exact-1 success decision
```

Each arrow can alter the observed construct. If the initial normalized bytes are not frozen, the task version is not frozen. If renderer fallback is unrecorded, the visual observer is not identified. If a criterion program catches an observer error as zero, model and infrastructure failure are confounded. If “critical” leaves compensate in the progress score but every non-critical leaf is mandatory for exact success, the same rubric has two different requirement logics. If an LLM summarizes reasons, the explanation is a derivative artifact rather than fresh evidence.

This yields a general contract for editable artifacts:

```text
public requirement and authority
→ frozen source bytes
→ declared normalization/transformation with before/after hashes
→ candidate artifact identity
→ criterion proposition and applicability
→ admissible native/render/behavior/trace view
→ observer version and failure state
→ tolerance and equivalence class
→ dependency/gate/compensation semantics
→ criterion observation
→ task decision and licensed claim
```

A second insight is that a task-specific rubric is software. Its validity obligations include provenance, code review, static safety, tests, positive/negative/alternative fixtures, observer mocks, exception semantics, dependency coverage, versioning, and regression locks. “Human-refined” is authoring provenance; it is not proof that 481 programs jointly implement the intended construct.

A third insight is that partial progress and task completion need separate criterion graphs. A diagnostic progress index may rationally compensate among subgoals. A completion decision should explicitly gate mandatory requirements, preservation, validity, and delivery. Deriving both from one scalar and declaring exact 1 as success makes secondary diagnostics mandatory and hides which obligations truly block acceptance.

## Comparison with adjacent reviewed benchmarks

### OfficeEval

[OfficeEval](2026-07-12-officeeval-standardized-exam-validity.md) has stronger external requirement and weight lineage through NCRE and denser deterministic native-property checks, but its copyrighted instrument is unavailable and its transformed subset threshold is invalid. PPT-Eval is far more inspectable and adds rendered/VLM checks, partial progress, and explicit collateral-change programs. It has weaker external task authority and more mutable observer dependence. Together they show that native properties and rendered judgment are complementary, while neither alone establishes professional presentation quality.

### MBABench

[MBABench](2026-07-11-mbabench-spreadsheet-artifact-validity.md) identifies editable artifacts as behavioral systems and reference solutions as fallible witnesses. PPT-Eval better combines native and rendered evidence and tests requested deltas against an original. It still lacks counterfactual behavior: links, animations, theme behavior, editability, and downstream reuse are mostly inferred from static state. Both use compensatory scores without a stakeholder acceptance threshold and need legitimate-alternative artifacts.

### AIDABench

[AIDABench](2026-07-17-aidabench-end-to-end-artifact-validity.md) routes answers, charts, and files to distinct evaluators but exposes package-closure and mixed-score failures. PPT-Eval is narrower and more coherent, with exact 120-task/120-rubric closure in the static registry and criterion-specific structural/render views. Yet its absent source bytes, normalized artifacts, attempts, and results break end-to-end release closure. Both demonstrate that evaluator routing is necessary but not sufficient; every criterion-to-view-to-result chain must close.

### AgenticVBench and CutVerse

[AgenticVBench](2026-07-16-agenticvbench-expert-temporal-artifact-validity.md) and [CutVerse](2026-07-15-cutverse-temporal-creative-artifact-validity.md) expose the difference between native state, sparse screenshots, rendered temporal behavior, and creative acceptance. PPT-Eval improves static slide-state observation with OOXML and complete-slide renders, but animation and transition XML presence is not playback validity. Its criterion programs need the same signed public-basis, observer, polarity, dependency, and aggregation checks identified in AgenticVBench. A saved slide image cannot prove temporal behavior any more than a video milestone screenshot can.

## Limitations and validity threats

### Content, source, and expertise

1. Twelve Internet Archive decks are a convenience substrate, not a population of presentation work.
2. Exactly ten tasks per deck is designed balance without frequency or consequence weighting.
3. Original users, recipients, purposes, requests, brand rules, and downstream decisions are absent.
4. Model-proposed tasks and feasibility filtering favor operations that current authors/tools can express and grade.
5. Difficulty labels lack assignment, calibration, agreement, or empirical measurement evidence.
6. Task-level author/reviewer identities, qualifications, contribution hours, approval, disagreement, and rejection reasons are unreleased.
7. One manual solve establishes a witness, not necessity, unique difficulty, or coverage of alternatives.
8. Public deck/source exposure creates contamination and direct lookup risk.
9. Internet Archive uploader metadata does not alone prove rights in all embedded content.
10. The attribution file miscounts rights markers and treats Public Domain Mark as a license/dedication.

### Artifact and observer validity

11. Initial benchmark PPTX and slide-image bytes are absent from the release.
12. PowerPoint Online deliberately mutates the initial artifact, but service/build/transformation identity is unpinned.
13. Source URL drift can change task state without task-ID change.
14. Cached original and generated candidate images may differ by time, renderer, fonts, or transformation.
15. Automatic renderer fallback can change the evidence generator without changing the score label.
16. OOXML/package equality can reject equivalent saves or miss visual/behavioral defects.
17. Static transition/animation records do not establish timing, playback, or correct affected objects.
18. VLM screenshots cannot prove editable structure, source binding, accessibility, or temporal behavior.
19. VLM response substring parsing is vulnerable to negation, mixed answers, and prompt injection.
20. No planted renderer-disagreement, adversarial-slide, corrupted-package, or legitimate-alternative suite is released.
21. Exception-to-score behavior remains leaf-specific; observer invalidity can become candidate failure.
22. Natural-language score explanations are model-generated paraphrases, not independent evidence.

### Rubric and metric validity

23. All 481 leaves are arbitrary executable Python programs; syntax validity does not establish semantic correctness or safe execution.
24. Criterion dependence is extensive: several leaves share objects, screenshots, prerequisites, and failure cascades.
25. “Critical” children compensate rather than gate in the partial score.
26. Non-critical children become mandatory for exact-1 success.
27. Exact floating score `1.0` makes SR sensitive to every secondary leaf and model judgment.
28. The `0.3` penalty and equal child means are author policy, not stakeholder utility weights.
29. Tree shape changes effective weighting; correlated subcriteria can count the same defect repeatedly.
30. Alternative-validity language is sparse in the released rubric corpus, and no alternate-artifact validation is released.
31. Broad collateral checks inspect selected state, not necessarily all unrelated content, media, links, metadata, accessibility, and behavior.
32. External `ai-rubric==0.2.5`, runtime defaults, prompts, and model endpoints are part of score identity.
33. No professional acceptance threshold, severity model, repair cost, or asymmetric loss validates either average score or SR.

### Meta-evaluation and human validity

34. Meta-evaluation attempts and labels are project-authored rather than independent field artifacts.
35. Exact per-category denominators are not stated; the percentages imply small intermediate groups.
36. The 30-task sample procedure and selected task IDs are unreleased.
37. No rater assignment, blinding, independent double scoring, inter-human agreement, adjudication, or criterion confusion matrix.
38. Broad progress intervals do not validate exact scores, leaf correctness, or task acceptance.
39. Rubrics were fixed after meta-evaluation, making Table 2 a pre-repair estimate and Table 1 a different instrument.
40. No frozen holdout evaluates the repaired rubric set.
41. Repeatability over selected outputs does not establish accuracy or robustness.
42. Cross-VLM MAE can hide exact-success flips and shared blind spots.
43. Five convenience participants do not define expert, worker, or user performance.
44. Human and agent time, tools, observations, action constraints, and assistance are not shown equivalent.
45. Cross-human SD is not human run reliability and lacks participant-level outcomes.

### Experimental, statistical, and operational validity

46. Model, provider, prompt, image history, action vocabulary, parser, and defaults vary by GUI row.
47. GUI/API comparisons also vary model harness, Skill, tool surface, feedback, and edit mechanism.
48. Three runs support limited descriptive variance but no task-clustered intervals, paired differences, or rank probability.
49. Tasks cluster by twelve shared decks and by repeated rubric/object patterns.
50. No complete attempted/valid/retried/excluded/scored ledger reconciles nominal cells.
51. Infrastructure, artifact, rendering, model, and rubric failures are not fully separated in published tables.
52. Reported failure clusters are generated from rubric explanations without released coding protocol, assignments, agreement, or raw rows.
53. Approximate $54/$62 frontier GUI suite costs omit judge, hydration, human, infrastructure, retry, API-baseline, and maintenance costs.
54. A 30-step explicit edit suite is not a complete presentation-development workflow.
55. No recipient opens, edits, presents, approves, or uses the artifacts.
56. No evidence connects score to productivity, communication quality, factual accuracy, accessibility, customer outcomes, safety, procurement value, or readiness.

### Reproducibility and release correspondence

57. The audited commit postdates v1 by eight days; no exact paper-time tag is identified.
58. Later model configurations demonstrate repository evolution after the reported experiment.
59. Raw agent/human artifacts, labels, criterion outputs, trajectories, and tables are absent.
60. Mutable commercial model/VLM endpoints prevent exact reruns.
61. OneDrive/PowerPoint Online UI automation depends on brittle frame/ribbon/download selectors.
62. No complete lockfile, container image, Office build, font pack, locale, browser build, or tenant state pins execution.
63. The release's source URLs and current code can assemble a new experiment, not reproduce the June paper experiment.

## Transfer to skill-bench

### Retain

1. **Task-specific executable rubric programs.** They make hidden measurement logic inspectable and permit native, rendered, semantic, and preservation checks.
2. **Plural artifact views.** Route native package state, rendered appearance, temporal behavior, and traces according to criterion needs.
3. **Explicit original→modified comparison.** Requested delta and collateral preservation should both be scored.
4. **Progress diagnostics separate from binary success reporting.** Partial evidence is more informative than endpoint-only pass/fail.
5. **Human review of model-drafted rubrics.** Preserve draft, revisions, author/reviewer roles, and labor rather than claiming automation.
6. **Constructed progress fixtures.** No/some/significant/perfect artifacts are useful instrument tests when frozen and complemented by adversarial/alternative cases.
7. **Repeated judge and agent trials.** Keep both, but preserve their different uncertainty and failure semantics.

### Repair

1. **Freeze every transformation.** Bind source bytes, normalized bytes, rendered bytes, transformation code/service/build, fonts, locale, timestamps, and before/after hashes to task version.
2. **Record realized observer identity.** A fallback renderer must create a different observation record, never silently inherit the requested mode.
3. **Give each criterion a view contract.** Declare proposition, public basis, applicability, evidence required, observer, tolerance, equivalence class, failure state, dependencies, polarity, severity, and claim ceiling.
4. **Treat rubric code as a tested instrument.** Require static safety, sandboxing, positive/negative/partial/alternative/adversarial fixtures, observer mocks, exception checks, dependency analysis, regression locks, and criterion-level ownership.
5. **Split progress from acceptance.** Use a compensatory progress graph for diagnosis and an explicit gate graph for mandatory completion, artifact validity, preservation, safety, and delivery.
6. **Type invalidity.** Distinguish substantive criterion failure, invalid artifact, unavailable view, observer error, infrastructure failure, timeout, and insufficient evidence at leaf and task levels.
7. **Validate alternatives and transformations.** Include structurally different but visually/semantically valid edits, equivalent saves, renderer variants, and OOXML rewrites.
8. **Validate temporal properties temporally.** Animation and transition criteria require pinned playback/window evidence, not XML presence or static slide renders alone.
9. **Release empirical closure.** Publish exact task/rubric/source/render hashes, attempt ledger, artifacts, criterion outputs, grader calls, human labels, repair diffs, table builder, and cost rows.
10. **Separate source rights evidence.** Record uploader assertion, legal basis, embedded-asset caveats, transformations, attribution obligations, and review status without promoting a status mark into a license.

### Test before stronger claims

1. Criterion false-pass/false-fail rates on held-out planted defects and legitimate alternatives.
2. Cross-renderer equivalence and exact-SR sensitivity.
3. Human–human and observer–human agreement on independently sampled, blinded artifacts with clustered intervals and abstention.
4. Score stability under rubric refactoring that preserves propositions but changes tree shape.
5. Whether exact-1, explicit mandatory gates, and recipient acceptance agree.
6. Matched GUI/API interventions that hold model, task, budget, observation, and repair policy as constant as possible.
7. Recipient edit/reuse/presentation trials, accessibility review, and downstream communication outcomes before professional-quality or workflow-value claims.

## Concrete repository actions

1. Preserve `data/sources/releases/2606.31154v1-ppt-eval/release-audit.json` as the static census and timing-boundary record.
2. In the next artifact-view/rubric consolidation, add the transformation-program chain: source bytes → normalization → candidate → admissible view → observer realization → executable criterion → typed outcome → aggregation → claim.
3. Reuse PPT-Eval as a cross-domain conformance case: plant an unpinned renderer fallback, a “critical” child that compensates, a non-critical child that blocks exact success, an observer exception converted to zero, and a structurally different valid artifact. Existing validators should reject or type each condition.
4. Keep PPT-Eval at a strong methodological/release-inspectability tier but below professional-validity, human-equivalence, and readiness tiers until frozen substrate, result closure, independent criterion validation, and recipient evidence exist.
5. **No new queue task added.** The implications map to existing benchmark-bundle, artifact-view admissibility, criterion/rubric, task-health, configured-system, metric, provenance, and validity machinery. A PowerPoint-specific schema or pilot would duplicate scope and violate the queue instruction.

## Assessment

**Evidence tier:** complete immutable paper plus substantive eight-day-post-v1 task/rubric release; strong static inspectability, weak empirical reconstruction.

**Most reusable contribution:** executable task-specific rubrics that combine native artifact state, rendered slides, semantic judgments, partial progress, and collateral-change checks.

**Most serious validity boundary:** the score depends on an unfrozen PowerPoint Online normalization/render chain and 481 heterogeneous rubric programs whose “critical” semantics, alternatives, exceptions, observer identities, and human validation are not sufficient for completion or professional-quality claims.

**Safe claim for skill-bench:** PPT-Eval demonstrates that mixed native/render/model observers and executable partial-credit rubrics can produce a far more diagnostic presentation-edit conformance instrument than endpoint-only grading. It does not demonstrate that its score is a stable, renderer-invariant, professionally calibrated measure of presentation quality, human equivalence, general computer-use capability, productivity, or readiness.
