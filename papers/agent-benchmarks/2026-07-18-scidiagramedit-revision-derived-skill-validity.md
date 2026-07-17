# SciDiagramEdit: a paper-revision delta is valuable supervision, but not self-authenticating author intent or tacit visual grammar

## Source and review status

**Deep review of the complete immutable v1 primary source and appendices, plus a time-bounded audit of the official arXiv source and promised release surfaces.**

- **Paper:** Yasheng Sun, Zezi Zeng, Yifan Yang, Chong Luo, Wenyi Wang, Ziwei Liu, and Jürgen Schmidhuber, *SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions*, arXiv:2607.15272v1 (16 July 2026), <https://arxiv.org/abs/2607.15272v1>
- **Local PDF:** `data/papers/pdfs/2607.15272v1-scidiagramedit.pdf` (20 pages; 10,626,377 bytes; SHA-256 `26ac91328b15dffdb28d7b4fc0e6b59ca6cc7e4b62fd7abb0adcaf8b5d7d502f`)
- **Full local text:** `data/papers/text/2607.15272v1-scidiagramedit.txt` (104,552 characters; SHA-256 `e5dfb762237e5dfb3fc177b7b494d074c0b0e29e1e2568a660dcf188859eb2db`)
- **Metadata:** `data/papers/source/2607.15272v1-metadata.xml`
- **Official arXiv source:** `data/sources/releases/2607.15272v1-scidiagramedit/arxiv-source.tar` (SHA-256 `d19ef24618f01651d7f8b99fd8eac03ed19b2707ee20c4f35ecf7fe9a8569488`), extracted at `data/sources/releases/2607.15272v1-scidiagramedit/arxiv-source/`
- **Release audit:** `data/sources/releases/2607.15272v1-scidiagramedit/provenance.json`
- **Release boundary:** v1 says the benchmark, instruction–revision pairs, 2,628 atomic annotations, and final Skill will be released, but contains no artifact URL. At the 17 July 2026 UTC audit, the paper, arXiv landing page, and TeX source linked no repository or dataset; exact-title GitHub and Hugging Face API searches returned zero. Benchmark rows, vector sources, split identities, Skills, traces, outputs, judgments, and human votes were unavailable. This is a time-bounded absence finding, not proof against a later or differently named release.
- **Tags:** revision-derived supervision, artifact editing, skill evolution, SVG, author intent, tacit expertise, evaluator coupling, selection, release inspectability

## One-sentence contribution and assessment

SciDiagramEdit introduces a promising source-to-task pattern—mine 364 before/after scientific-figure revisions, reconstruct editable SVGs, author explicit edit instructions and 2,628 checks, then evolve a portable Skill from Editor traces and target comparisons—but the paper observes selected revision deltas and curator/model reconstructions rather than authors' reasons, reports validation-selected configured-package gains without exact split lineage, repeats, uncertainty, or released trial evidence, and evaluates explicit visual edit conformance rather than scientific correctness, argument quality, co-edit utility, tacit expertise transfer, professional validity, or readiness.

## Why this matters for skill-bench

This is a bounded scientific-diagram case for charter objectives A, B, and C, not a proposal to narrow `skill-bench` to figures. Its general question is whether naturally occurring professional artifact revisions can cheaply supply realistic tasks and reusable procedural knowledge:

```text
versioned professional artifacts
→ matched before/after event
→ observed delta
→ candidate rationale or intent
→ authorized task requirement
→ editable task substrate
→ criterion and collateral-preservation observers
→ candidate procedural lesson
→ independent promotion and transfer test
→ recipient/workflow consequence
→ bounded claim
```

The source is important because revision histories are richer than invented prompts: they preserve a real change made in a consequential authoring process. Its central validity mistake is equally important: a changed artifact does not state why it changed, who authorized it, whether every changed element was intended, whether omitted changes were rejected, or which procedure generalizes. Revision evidence is a **candidate critical incident and demonstrated witness**, not self-interpreting expertise.

## Research question and claim boundary

The paper asks whether an agent can learn instruction-driven editing of scientific diagrams from natural arXiv version histories while preserving editable vector primitives, and whether execution traces plus author-revision demonstrations can be distilled into a Skill that improves future edits and transfers across model backbones (Sections 1, 3, and 4, pp. 1–6).

The full paper supports bounded claims that:

1. the authors assembled a selected corpus of 364 before/after figure pairs across 23 arXiv primary subjects and authored 2,628 checklist questions over those retained pairs (Section 3, pp. 3–4);
2. their transformation represents each figure as native SVG primitives plus embedded raster panels and exposes an Editor with filesystem/Python access, rendering/lint/icon tools, and an explicit Skill directory (Sections 3 and 4.2, pp. 3–5);
3. their Coach applies bounded file patches to a top-three Skill frontier using training traces, judge scores, feedback history, and—under the main condition—the target render and target SVG, with validation-score admission (Sections 4.4 and A.2, pp. 6 and 11–12);
4. on the authors' undisclosed test rows, the reported configured system scores 0.932 checklist success, compared with 0.882 for GPT-Image-2 and 0.844 for the strongest listed single-pass SVG baseline, while its automated aesthetic scores remain below the raster regenerators on some measures (Table 2, p. 7);
5. equipping each of four GPT-5.x Editors with a separately evolved Skill raises the reported semantic and aesthetic pairwise win rates by 0.011–0.054 and 0.037–0.076, and reusing the GPT-5.5-evolved Skill on three weaker backbones raises them by 0.018–0.047 and 0.031–0.081 (Table 3, p. 7); and
6. five local graduate-student volunteers forced to choose between paired outputs on 30 test instances prefer the proposed system over two baselines in 54–68% of votes depending on baseline and axis (Section 5.4, Table 4, and Appendix A.3, pp. 8 and 13).

The evidence does **not** establish that the retained visual delta is the paper authors' stated or sole intent; that curators recovered that intent; that the generated SVG is semantically equivalent to the source; that the checklist is complete or independent; that a learned rule is tacit expert knowledge; that test items are independent of training papers, authors, projects, visual templates, or vectorization programs; that Skill gains are reliable over stochastic runs; or that the system improves scientific truth, explanatory argument, reader comprehension, editability in actual authoring software, coauthor workflow, publication outcomes, professional productivity, safety, or readiness.

## Methodology and system reconstruction

### 1. Revision-pair sourcing and retained denominator

The final corpus contains 364 pairs described as “the same figure” across an older and newer arXiv version. The appendix says raw mining is noisy: some pairs are mere raster rerenders or font swaps, while others are wholesale replacements. Curators retain a “meaningful middle band” such as panel additions, relabeling, rerouting, or relayout while preserving enough scaffold to count as an edit (Section 3 and Appendix A.1, pp. 3 and 10–11).

The retained set spans 23 primary subjects, but 73.6% lies in `cs.LG`, `cs.CL`, `cs.CV`, and `cs.RO`; 47% comes from 2023–2024. The 2,628 claims are dominated by relabeling (22.8%) and adding elements (21.4%), while connection changes are 4.2% (Figure 2, p. 4). This is useful descriptive coverage of the retained rows, not a sampling frame for scientific revision work.

Crucial denominators and lineage are absent:

- arXiv snapshot/date, eligible categories, papers and versions scanned;
- candidate papers, version transitions, figures, matched pairs, and exclusion counts;
- how figure identity was matched across changed numbering, captions, page position, or composition;
- duplicate papers, figures, author teams, projects, templates, or serial version transitions;
- whether one paper contributes multiple figures or adjacent version pairs;
- exclusion reasons by stage and curator;
- rights/licence eligibility before and after selection; and
- exact train/validation/test row counts and grouped split policy.

The paper says the 364 rows are split `2:1:3` into train, validation, and test (p. 6). Because 364 is not divisible by six, this ratio does not reveal exact counts. More importantly, an item-random split could place figures from the same paper, author group, project, visual template, or sequential revision chain on both sides. Without group identities, the held-out label does not establish independent transport.

### 2. Intent is authored during curation, not naturally observed

The manuscript repeatedly calls the pairs grounded in “the authors' own revision intent” and at one point describes “naturally occurring author-written instructions” (Sections 1 and 3, pp. 1–3). Appendix A.1 is more candid: a raw visual diff seldom makes intent explicit; disambiguation requires surrounding-paper context; and “a useful editing instruction therefore has to be authored, not just extracted” (p. 10).

The curation interface shows the before/after render, a candidate instruction, keep/drop and accurate/inaccurate decisions, an editable field, and a GPT-5.5 chat assistant. The curator typically refines the draft for two or three rounds; the paper says every released annotation is human-confirmed. Parallel panels filter vectorizations and author checklist questions (Appendix A.1 and AI-assistant disclosure, pp. 10–11 and 9).

This changes the provenance claim. The observable evidence is:

```text
paper authors produced version B after version A
+ manuscript context visible to an undisclosed curator
+ GPT-5.5-generated/revised candidate language
+ curator acceptance/editing
= benchmark instruction and checklist
```

No original paper author, coauthor, reviewer, or editor is reported to have supplied or confirmed the reason. A revision can bundle reviewer requests, coauthor preferences, updated results, accidental rerendering, tool migration, deadline constraints, or multiple independent edits. The newer figure is evidence of an accepted final state at one time, not proof that every delta was deliberate, optimal, or generalizable. “Human-confirmed annotation” means curator-confirmed description, not source-author-confirmed intent.

### 3. Editable representation is a model-authored projection

The original figures are not reported as native SVGs. The AutoFigure-Edit-derived pipeline segments raster panels, has an LLM write an SVG template for surrounding schematic content, and embeds original raster crops as `<image>` nodes (Section 3, pp. 3–4). A separate curation panel drops vectorizations whose rendering visibly drifts from the source (Appendix A.1, p. 11).

This is a valuable hybrid representation: it allows local code edits and preserves complex panels. It is not the authors' native project state. At least four objects must remain distinct:

1. the source paper's rendered old figure;
2. the model-authored vectorization of that figure;
3. the source paper's rendered new figure; and
4. the model-authored “target SVG” used by the Coach.

Appendix B.2 instructs the Coach to inspect `target.svg` and asks “how did the ground-truth author solve the same edit?” (pp. 14–15). Unless the unavailable corpus shows otherwise, the paper's own curation description implies that this SVG is reconstructed by the vectorizer rather than authored by the paper's original authors. It can demonstrate one projected realization, but cannot reveal the authors' source-level operations, layer structure, constraints, or procedure.

The paper reports a visual drift filter but no exact candidate/retained/invalid denominator, agreement, pixel/structural threshold, source-to-SVG semantic audit, font or renderer lock, embedded-asset hash, accessibility check, malformed-SVG rate, or native-editor round trip. Editability is asserted from SVG primitives; it is not tested through downstream human co-editing, object selection, semantic grouping, maintainability, or export stability.

### 4. Task and checklist co-construction

Each retained pair has an explicit English instruction and multiple binary or multiple-choice questions. Questions cover named changes and “overall logical coherence”; the total is 2,628, or about 7.2 per retained pair (Section 3, pp. 4–5). The VLM Judge sees candidate output, input, reference, instruction, and each question, then emits an allowed answer. Checklist accuracy is `r_sem`.

This gives interpretable criterion-level observations, but the instrument is co-derived from the same target used to judge and train the Skill. The paper does not report:

- who wrote each instruction/question and with what expertise;
- spontaneous versus model-proposed versus curator-corrected clauses;
- criterion-level evidence locators into the old/new render and paper context;
- completeness, negative requirements, dependencies, applicability, or legitimate alternative edits;
- independent review, inter-rater agreement, ambiguity adjudication, or question revisions;
- whether collateral preservation is exhaustively checked rather than mentioned in the task objective; or
- criterion counts and distributions within each split.

The instruction explicitly spells out every intended edit under the stated benchmark scope (Limitations, p. 9). Therefore high `r_sem` measures conformance to a curator-authored explicit target decomposition. It does not test inferring authorial intent, recognizing a latent scientific communication problem, or deciding which edit should be made.

### 5. Editor, Judge, Coach, and Skill evolution

The Editor is a coding-agent subprocess that receives input SVG, instruction, and a top-level `SKILL.md`, with optional workflow/tool files loaded on demand. It has filesystem and Python access plus optional SVG rendering, layout linting, and icon generation (Section 4.2, pp. 4–5). The exact model endpoint, system prompt, tool schemas, context/token budget, maximum actions, retry policy, and evaluation-time stopping behavior are not supplied.

The Judge combines:

- **semantic faithfulness:** mean checklist answer accuracy; and
- **aesthetic preference:** one randomized-order VLM comparison asking whether output is at least as polished as the target.

The composite is multiplicative: `r = r_aes × r_sem`, so one negative aesthetic judgment zeros all semantic credit (Section 4.3, p. 5). This noncompensatory gate may be defensible for candidate promotion, but the paper gives no judge calibration against humans, repeat-call stability, tie/abstention state, uncertainty, position-bias results, criterion confusion, or sensitivity to alternative gates. Calling pairwise VLM judgment “more reliable” than pointwise scoring cites adjacent work rather than validating this exact observer on edited figures.

The Coach sees a minibatch's traces and scores, current Skill, feedback history, and—under the main method—the target PNG and target SVG. It may create or edit up to eight files/patches. A candidate is scored on validation; a top-`K=3` frontier admits it when space remains or it beats the current worst. Training uses two epochs, batch size eight, up to three analyst rounds, four Coach workers, eight Editor workers, and a 600-second Editor timeout (Sections 4.4 and A.2, pp. 6 and 11–12).

The algorithm is clear enough to reveal three selection effects:

1. the “best-so-far” validation curve is monotonic by construction because the system retains the current best;
2. validation is repeatedly reused for proposal admission and final Skill selection, so its terminal score is post-search rather than confirmatory evidence; and
3. feedback history tells the Coach which patches were rejected, making the final artifact a product of validation feedback as well as traces and demonstrations.

The paper omits exact training/validation counts, total evolution steps `T`, candidate count, acceptance/rejection ledger, validation call count, top-frontier trajectories, Skill hashes/diffs, initial scaffold text, prompts, model snapshots, random seeds, API dates, invalid/provider failures, token usage, and per-stage cost. It reports about US$20,000 total API spend across experiments and development but no attributable cost or complete-resource denominator (Appendix A.2, p. 12).

### 6. Comparisons and estimands

Table 2 compares the proposed multi-step Editor/Skill/tool package with three “single-pass” AutoFigure-Edit-style full-SVG emitters and two raster regenerators (p. 7). These are useful configured packages, not isolated model or Skill comparisons. The proposed system has agentic tool use, rendering/lint utilities, evolved guidance, and a distinct control loop; the SVG baselines emit once; raster systems cannot preserve vector structure by design. No matched time, tokens, model calls, retries, tools, or dollar budget is given.

The raster comparison demonstrates a real trade-off: GPT-Image systems score well aesthetically but alter untargeted text/style and produce noneditable rasters in examples. Yet the quantitative instrument does not measure editable structure, object identity, untargeted-element preservation, malformed SVG, or source-level collateral effects. The proposed method's headline “keeping structure editable” is therefore a property of the output format and qualitative examples, not an evaluated comparative outcome.

Table 3 is the best evidence for a Skill effect because it compares each Editor backbone with and without a Skill and separately transfers the GPT-5.5-evolved Skill to weaker Editors. Still, the paper reports one aggregate per cell with no repeated runs, paired row differences, confidence intervals, task/claim clustered uncertainty, invalid outcomes, negative-item distribution, or per-edit-type heterogeneity. The “evolved” condition can also use a Skill selected on the same corpus lineage, while the transfer condition changes only model consumer—not task family, author/project population, artifact type, tool environment, or verifier. It supports **cross-backbone reuse within one configured benchmark package**, not cross-workflow or professional transport.

The demonstration-aware Coach ablation is qualitative only. Figure 8 shows selected examples with and without target access, and the prose describes different rule types (pp. 14–16). No complete sample, quantitative outcome, candidate denominator, selection policy, or uncertainty is reported. It illustrates a plausible mechanism but does not estimate the effect of target demonstrations.

### 7. Human study

Five uncompensated graduate students in computer science/electrical engineering from the authors' institution each judge all 30 uniformly sampled test instances against both strongest baselines on aesthetic and instruction-following axes. Input, instruction, and randomized anonymous outputs are shown; the target is withheld; no tie option exists. This produces 600 forced-choice trials, or 150 votes per baseline-by-axis cell (Section 5.4 and Appendix A.3, pp. 8 and 13).

This supports a narrow preference result for those 30 items, five repeated raters, two comparators, and forced-choice interface. It does not establish independent observations—the same people rate every item—or professional recipient utility. The paper reports no item/rater distribution, confidence intervals, mixed-effects model, agreement, order/round effects, fatigue, missing trials, calibration, rationale, expertise in scientific illustration, conflicts, or correction history. Participants never co-edit the SVG, judge scientific correctness or argument quality, inspect collateral source changes, or use the result in a paper workflow. The target is withheld, which avoids target imitation but leaves respondents judging only visible instruction fulfillment and polish.

## Evidence interpretation

### What is genuinely learned

1. **Revision histories are a feasible source of realistic candidate edits.** The selected corpus contains complex local changes unlikely to arise from toy prompt generation alone.
2. **Hybrid SVG+raster state is a useful editable stress substrate.** It exposes primitive-level operations while retaining dense panels that are difficult to vectorize.
3. **Target demonstrations can generate concrete procedural hypotheses.** Rules about scoped string replacement, math `<tspan>` layout, viewBox tightening, and post-restructure review are more actionable than generic exhortations (Appendix B.1, pp. 13–15).
4. **A Skill can have consumer-model interactions.** The reported gains differ materially across GPT-5.1–5.5, reinforcing that intervention value belongs to a configured system rather than to a text artifact alone.
5. **Explicit edits still leave implicit failures.** Figure 12 shows stale nodes, dropped connections, and style mismatch even when named clauses are followed (pp. 19–20). This is direct evidence that explicit target conformance does not exhaust artifact integrity.

### What the headline results do not license

- `364` is the retained corpus, not the eligible revision population or a representative sample of scientific editing.
- `2,628` is the number of curator-authored checks, not independent atomic author intentions or complete professional requirements.
- `0.932` checklist success is one configured VLM-observed aggregate, not scientific correctness, reader comprehension, or professional quality.
- monotonic best-validation improvement is a property of best-so-far selection, not evidence of stable online learning.
- Table 3's positive deltas are unrepeated within-package aggregates, not reliable general Skill efficacy or cross-task transfer.
- cross-backbone reuse is consumer transport while task, corpus, tools, and verifier remain fixed; it is not cross-domain or workflow transport.
- five students' forced choices are not author acceptance, expert agreement, co-edit utility, productivity, or publication consequence.
- a reconstructed `target.svg` is not evidence of how the original author edited the figure.
- an observed version delta plus curator prose is not source-author-confirmed intent or tacit visual grammar.

## Unique insight for skill-bench

> **A professional artifact revision is a naturally occurring accepted-state transition, but it has three separable projections: observed delta, authorized intent, and transferable procedure. Benchmark construction must validate each projection rather than treating the final artifact as self-authenticating expertise.**

This yields a revision-derived evidence ladder:

```text
immutable parent/child artifacts and source rights
→ match identity and complete candidate/exclusion history
→ typed delta with preserved nulls and collateral changes
→ actor/request/channel/timing evidence
→ candidate intent with source-author acceptance, correction, or unresolved status
→ task clause and fair public basis
→ editable substrate and transformation-equivalence evidence
→ plural artifact observers and admissibility
→ candidate procedural rule with demonstration lineage
→ independent promotion on grouped held-out forms
→ transfer edge changing declared dimensions
→ recipient adoption, artifact consequence, burden, and claim ceiling
```

The null states matter. A source-author response of “the visible change was incidental,” “the reviewer requested it,” “the real reason was updated data,” or “this is one acceptable implementation” is valuable evidence. Forcing every delta into one definitive instruction launders ambiguity into ground truth.

## Relation to adjacent reviewed evidence

- **Context-Mediated Domain Adaptation** establishes the edit-to-claim boundary. SciDiagramEdit adds a stronger natural before/after artifact witness and an executable edit task, but has the same missing join from delta to contributor-approved interpretation.
- **Pista** treats semantic diffs as oversight hypotheses requiring fidelity, utility, and consequence validation. SciDiagramEdit needs the inverse check: its curator-authored semantic instruction must faithfully and completely represent the raw visual/state diff.
- **SciVisAgentBench** supplies evaluator-admissibility envelopes. Rendered pairwise aesthetics, SVG source integrity, object-level collateral preservation, and scientific semantics are nonfungible evidence views; no one VLM score can substitute for the others.
- **AgenticVBench** shows that rich artifact views cannot rescue an incoherent criterion contract. Here, explicit instruction, checklist, target render, target SVG, and preservation objective need signed, mechanically consistent criterion semantics.
- **SkillsBench** distinguishes package efficacy, class transfer, and portfolio value. SciDiagramEdit's Table 3 is closest to package efficacy plus consumer-model transport; independently authored equivalent edit classes and workflow-weighted value remain untested.
- **AFTER** supplies the versioned source-to-target transfer edge. SciDiagramEdit does not expose Skill versions, proposal/promotion history, task-author lineage, or an independently authored target edge.
- **GrowLoop** warns that adaptive criterion/probe reuse can become target-conditioned selection. SciDiagramEdit repeatedly selects Skill patches on one validation set and must preserve all candidates and use untouched bridges.

Existing `expertise-transfer`, `expert-participation`, artifact-view/admissibility, compounding-lesson, longitudinal-stream, task-health, metric, and validity-argument machinery can represent the needed lineage and claim ceilings. No diagram-specific schema or duplicate queue task is warranted.

## Reproducibility and operational realism

The manuscript and TeX source are fully inspectable. It provides formulas, pseudocode, broad settings, tool names, example Skill rules, and total API spend. Those details make the conceptual loop understandable.

No empirical release was available at audit time. The paper says “we will release” curated pairs/annotations and “we release” the benchmark/final Skill, but supplies no URL in the PDF, arXiv page, or TeX source. Exact-name GitHub repository search returns `total_count: 0`; Hugging Face dataset/model/space searches return empty arrays. The preserved API responses and source hashes are in `data/sources/releases/2607.15272v1-scidiagramedit/provenance.json`.

Unavailable artifacts include source arXiv IDs/version pairs; retrieval hashes; candidate/drop ledger; vectorized SVGs; instruction/checklist rows; paper/author/project-group split assignments; curation records; initial/candidate/final Skills; prompts; model snapshots; traces; raw judge calls; outputs; retries; costs by condition; human votes; and aggregation code. Therefore none of Tables 2–4, Figure 1, or the qualitative selection process can be recomputed or audited for denominators, leakage, invalidity, or cherry-picking.

Operational realism is mixed. Positives include genuine revision-derived targets, editable outputs, code-level tools, explicit target demonstrations, per-clause checks, collateral-preservation intent, and a nontrivial cost disclosure. Missing are native authoring files, real author/coauthor requests, integration with an actual drawing/paper tool, author approval, concurrent edits, comments, undo/version control, renderer and font pinning, safe sandbox/network policy, file integrity, API failure handling, latency/tokens by task, human correction time, merge conflicts, accessibility, scientific verification, publication workflow outcomes, and maintenance under model/tool drift.

## Limitations and validity threats

1. The initial arXiv sampling frame, snapshot, eligible population, and candidate denominators are absent.
2. Figure-pair identity and version-transition matching procedures are under-specified.
3. Retention targets a curator-defined “meaningful middle band,” creating unknown selection effects.
4. Candidate, retained, dropped, invalid-vectorization, and annotation-failure counts are absent.
5. Paper, figure, author, project, template, and serial-revision clustering are unreported.
6. Exact split counts are omitted despite a `2:1:3` ratio that does not divide 364 exactly.
7. Split grouping is unknown, so corpus-lineage leakage cannot be excluded.
8. Four computer-science categories contribute 73.6% of retained rows; 47% comes from 2023–2024.
9. The source paper authors do not report or confirm revision reasons.
10. Coauthor, reviewer, editor, updated-result, tool, and incidental causes are not typed.
11. “Author-written instructions” conflicts with the disclosed GPT-5.5-plus-curator authoring process.
12. Human confirmation is curator confirmation, not source-author authorization.
13. Curator identities, qualifications, assignment, calibration, and agreement are absent.
14. Instruction and checklist proposal/correction lineage is unreleased.
15. The newer figure is one accepted state, not necessarily the sole or optimal solution.
16. Original figures are projected into hybrid SVGs by segmentation and an LLM.
17. The “target SVG” appears reconstructed, not authored by the source-paper author.
18. Vectorization visual-drift criteria, observers, thresholds, repeats, and exclusion counts are absent.
19. Visual equivalence does not establish structural, semantic, font, accessibility, or native-editor equivalence.
20. Source rights are delegated to original licences while selected-pair eligibility is not released.
21. Instructions explicitly enumerate intended changes, so latent intent and problem recognition are outside scope.
22. Checklists are co-derived from the same target and are not independently validated.
23. Checklist completeness, negative obligations, dependencies, alternatives, and collateral coverage are unknown.
24. The VLM Judge sees target, instruction, and curator questions, creating criterion/target coupling.
25. One binary aesthetic judgment gates all semantic credit without calibration or sensitivity analysis.
26. Judge repeats, uncertainty, invalid outputs, position effects, and human criterion agreement are absent.
27. Editor, Coach, and Judge endpoints/snapshots, complete prompts, and API dates are unpinned.
28. Evaluation tool budgets and stopping/retry policies are under-specified.
29. Baselines are unequal treatment bundles with different tools, steps, media, and editability.
30. No quantitative source-structure, editability, untargeted-element, or collateral-change metric is reported.
31. Validation is repeatedly reused for candidate admission and final Skill selection.
32. Figure 1's best-so-far monotonicity is guaranteed by retention policy.
33. Total steps, candidates, validation calls, accepted/rejected patches, and Skill hashes are absent.
34. Two epochs over an undisclosed exact training count do not reveal exposure per row.
35. Table 2 and Table 3 provide no repeats, task rows, paired differences, confidence intervals, or clustered uncertainty.
36. Invalid environment/provider/editor/judge attempts and denominator policy are absent.
37. Positive aggregate Skill effects can hide neutral and harmful task/edit classes.
38. Cross-backbone transfer holds corpus, artifact type, tools, and verifier fixed.
39. The demonstration-aware Coach ablation is selected qualitative evidence only.
40. Approximate US$20,000 total spend combines experiments and development without condition allocation.
41. Five local graduate students are not a representative expert, author, reader, or production-user panel.
42. All five rate all 30 items, but analysis treats only pooled vote fractions.
43. Forced choice without tie/abstention can exaggerate weak preference.
44. Human agreement, rater/item effects, uncertainty, order, fatigue, and missingness are unreported.
45. The human study does not test source inspection, co-editing, repair, productivity, or consequence.
46. Scientific truth, argument coherence, result fidelity, accessibility, and reader comprehension are not validated.
47. Figure 12 itself demonstrates implicit collateral failures outside the explicit checklist framing.
48. No code, benchmark rows, Skills, traces, outputs, judgments, votes, or result code were available at audit time.
49. Closed model/tool dependence and absent snapshots prevent exact reproduction even if rows later appear.
50. No longitudinal drift, maintenance, safety, publication, or professional-workflow evidence is reported.

## Transfer to skill-bench: retain, repair, test

### Retain

- Use immutable before/after professional artifacts as candidate critical incidents and demonstrated witnesses.
- Preserve editable native or hybrid state rather than evaluating only flattened renders.
- Keep explicit instructions, criterion-level checks, and target demonstrations as separate versioned objects.
- Represent procedural knowledge as trigger–failure–rule entries with scoped verification, not generic advice.
- Evaluate Skill effects as configured interventions and test consumer-model interactions.
- Keep explicit failures where named changes pass but collateral or implicit integrity fails.

### Repair

- Add complete eligible→candidate→matched→retained→vector-valid→annotated→split denominators and exclusion reasons.
- Group splits by paper, author/project, figure lineage, and template; publish exact counts and overlap audits.
- Type each task clause as `source-author-stated`, `reviewer/coauthor-stated`, `curator-inferred`, `model-proposed`, `author-confirmed`, `corrected`, `rejected`, or `unresolved`.
- Preserve raw rendered deltas separately from intent interpretations and source-level procedures.
- Record transformation lineage and equivalence checks for old/new render, reconstructed SVG, embedded assets, renderer/fonts, and native-editor round trips.
- Add plural observers for instruction clauses, untargeted elements, object structure, malformed state, visual quality, scientific semantics, and recipient acceptance; fail closed when a view is insufficient.
- Freeze initial Skill, every candidate patch, parent hash, training evidence, validation outcomes, rejection reason, and final promotion.
- Report intended, attempted, valid, invalid, retained, failed, and successful denominators per configured condition, plus paired clustered uncertainty and complete resource use.

### Test

1. **Intent audit:** sample revision pairs; ask original authors or authorized contributors to independently state the reason, inspect the curator instruction, mark incidental/missing/alternative changes, and scope allowed benchmark use. Estimate proposition-level acceptance, correction, rejection, and unresolved rates.
2. **Grouped transport:** evolve only on papers/authors/projects/templates disjoint from test, then test independently curated equivalent edit classes with an alternate checklist author and observer.
3. **Projection falsification:** plant visually equivalent but structurally broken SVGs, structurally sound alternate renderings, stale untargeted nodes, dropped links, font drift, inaccessible labels, and scientific-content corruption. Require each observer to accept, reject, or abstain for the declared reason.
4. **Skill factorial:** no Skill versus frozen evolved Skill × same versus independent criterion author × with versus without target demonstration, under matched Editor/tool/budget envelopes and repeated seeds.
5. **Recipient consequence:** have domain authors complete real edit-and-repair tasks with and without the package; measure adoption, correction, residual defects, native-file integrity, elapsed/human time, and downstream author/reader acceptance.

## Action items

- **No new queue task.** The evidence refines existing expertise-transfer, participation/authority, artifact-view admissibility, compounding-lesson, longitudinal transfer, task-health, metric, and validity-argument contracts. A diagram-specific build would duplicate those homes.
- For any future revision-derived pilot, require the revision-derived evidence ladder above before labeling a delta as expert intent or a rule as tacit expertise.
- Re-audit the artifact surfaces if the promised benchmark/Skill release appears; until then, mark all corpus, split, Skill, trace, grader, and human-result claims manuscript-only and non-recomputable.
