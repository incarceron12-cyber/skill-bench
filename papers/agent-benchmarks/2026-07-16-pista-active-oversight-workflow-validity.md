# Pista: semantic-diff participation improves inspectability, but does not yet establish effective oversight

## Bottom line

Pista makes a useful interface-level move: instead of showing a finished spreadsheet or a surface cell diff, it pauses at model-generated computational steps, exposes formulas/ranges/explanations, and lets a user ask, edit, branch, and revisit execution. A formative study (`N=8`) and a counterbalanced within-subject study (`N=16`) provide credible evidence that this bundled interface was more inspectable, was preferred, induced more elaborate post-task explanations, and reduced prompt count/length on two short financial-analytics tasks.

The evidence does **not** identify a general oversight effect. The study does not use planted or matched errors, independent defect opportunities, blinded artifact grading, proposition-level intervention traces, pre/post artifact hashes, collateral-preservation checks, trust calibration, or recipient outcomes. Pista also bundles execution decomposition with requirement suggestions, questions, edit suggestions, branching, and extra model calls. “Equivalent capability” therefore does not mean an isolated semantic-diff treatment. Final task success remains similarly low (`0.53` versus `0.50`), while the paper does not report a test of that contrast. The strongest safe claim is about **inspectability and interaction efficiency under one small bundled laboratory workflow**, not error prevention, calibrated reliance, professional utility, or readiness.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and C by testing a general cross-domain hypothesis: surfacing the semantic operation behind an artifact change may make consequential agent work easier to inspect and locally redirect than either a final artifact or a surface diff. The durable evidence is the immutable paper plus two paper-linked, pre-v1 implementation archives. The uncertainty clarified is where active-oversight evidence stops: visibility, self-explanation, feature use, defect detection, semantic adoption, realized repair, preserved integrity, reliance, and professional consequence require different observations.

This is **expansion with consolidation implications**, not a spreadsheet scope commitment. Useful completion means retaining the semantic-diff primitive while refusing to promote self-report, selected anecdotes, or a bundled usability treatment into a general oversight claim.

## Sources and reading record

### Primary paper read in full

- Sadra Sabouri et al., *Auditing and Controlling AI Agent Actions in Spreadsheets*, immutable arXiv v1, 12 pages: <https://arxiv.org/abs/2604.20070v1>
- Local PDF: `data/papers/pdfs/2604.20070v1-pista-active-oversight.pdf`
- Layout-preserving extraction: `data/papers/text/2604.20070v1-pista-active-oversight.txt`
- Metadata: `data/papers/source/2604.20070v1-metadata.xml`
- PDF SHA-256: `55e49221a839853b3317337552ad58f6a6dc6b868358dfa20500dff3874885a8`
- Text SHA-256: `2cc75ef334f0f800540e05320f58f5b4a17a444a3f8d3baed42f29a3ee3ef063`
- The immutable metadata contains no withdrawal or retraction notice. The complete extraction was read through limitations, conclusion, acknowledgments, and references.

Page references below use the PDF page number. Extraction line ranges are supplied where useful.

### Official publication page

- Microsoft Research page: <https://www.microsoft.com/en-us/research/publication/auditing-and-controlling-ai-agent-actions-in-spreadsheets/>
- Archived text: `data/sources/microsoft-research-pista-publication-page.txt`
- Provenance: `data/sources/microsoft-research-pista-publication-page.provenance.json`

The official page confirms publication metadata and the abstract; it is not full-text evidence.

### Paper-linked implementation audit

The paper links two author-lab repositories in footnotes 1–2 (p. 6; extraction lines 335–364). Both captured heads predate immutable-v1 publication, making them unusually useful release-time implementation evidence:

- Front end, commit `a976e0b42e04ecdc49ba0d86eb972b3ea7768097`: `data/sources/releases/2604.20070v1-pista/sheetcheck-ms-add-in.zip`
- Back end, commit `633f9b900e4f7e7b3aecbd324f2c25a0d3b9ac6b`: `data/sources/releases/2604.20070v1-pista/sheetcheck-backend.zip`
- Manifest and checksums: `data/sources/releases/2604.20070v1-pista/manifest.json`

The full 21-file front-end and 15-file back-end snapshots were statically inspected. Relevant files include `modules/dagRunner.js`, `modules/executionEngine.js`, `modules/worksheetSnapshot.js`, `modules/rubricManager.js`, `app/server.py`, `app/params.py`, `app/dspy_programs.py`, and `app/llm_logger.py`. The paper does not identify an exact study commit, and the archives contain no participant logs, retained task artifacts, questionnaires, codebook, analysis script, or raw outcome table. Implementation inspection therefore establishes available mechanisms, not exact implementation–study correspondence.

## One-sentence contribution

Pista turns model-generated spreadsheet operations into pauseable semantic-diff objects that users can inspect, question, locally edit, and branch before downstream execution continues.

## Research questions and claim boundary

The paper asks:

1. **Traceability (RQ1):** does Pista improve users' understanding of agent actions relative to a baseline?
2. **Steerability (RQ2):** does it improve detection, correction, and steering toward intended outcomes?

Its contribution is a mixed-initiative Excel agent organized around seven coupled features (pp. 5–6; lines 268–351):

- execution decomposed into steps;
- in-situ explanations;
- formulas, dependencies, and affected ranges surfaced as computation logic;
- localized natural-language editing;
- branched regeneration and navigation;
- editable task requirements before execution;
- suggested questions and edits during execution.

The paper's most reusable conceptual proposal is the **semantic diff**: expose the operation, logic, dependencies, and scope that drive a change, rather than enumerating all changed cells (p. 10; lines 580–647). This is plausibly portable to functions/architectural decisions in code, rhetorical moves in documents, transformations in data work, or design operations in media artifacts.

## Methodology and system

### Formative technology-probe study

Eight participants completed a 15-minute food-warehouse restocking task followed by a 15-minute semi-structured interview (pp. 3–4; lines 129–204). Recruitment used institutional lists, bulletin boards, and snowballing. Participants were 26–30 years old; six used spreadsheets daily, five had more than five years of spreadsheet experience, and all frequently used LLMs. Four were in computer science, two electrical engineering, one linguistics, and one political science—not a sampled population of finance or operational decision makers.

The probe already decomposed execution and allowed localized editing. Two researchers inductively coded interactions and interviews, updating the codebook through negotiated agreement and reporting Cohen's `κ=0.91` (p. 4; lines 188–192). Five challenge families motivated Pista: insufficient rationale, hidden computation/data propagation, fear of edit propagation, difficulty specifying constraints, and uncertainty about what to question.

This is a defensible formative design study. It does not independently validate the resulting seven-feature treatment or establish the prevalence of those challenges in professional spreadsheet work.

### Pista implementation

The paper reports a JavaScript/HTML Excel add-in and Python Flask/DSPy back end. Gemini 3.0 Flash generated code, explanations, decomposition, edits, and requirements; Gemini 3.1 Flash-Lite generated lower-latency scaffolded questions. Office.js snippets execute in Excel, while browser-cached sheet state supports branches (p. 6; lines 335–351).

The release supports the broad architecture:

- `dagRunner.js` stores a graph of states, captures a worksheet snapshot before an edge, runs code, restores snapshots for backward navigation, and regenerates a downstream branch after an edit.
- `executionEngine.js` executes each edge and pauses for user advancement; failed steps may be passed manually before execution continues.
- `dspy_programs.py` defines structured segments with description, affected ranges, explanation, predecessor IDs, Q&A, edit suggestions, parameters, code, manual steps, and optional formula information.
- `params.py` assigns Gemini 3 Flash to code/edit/rubric operations and Gemini 3.1 Flash-Lite to questions.
- `rubricManager.js` and the back-end rubric endpoints scaffold and verify requirements against worksheet context.

The audit also reveals operational boundaries omitted from the high-level account:

1. `worksheetSnapshot.js` caps snapshots at 5,000 used-range cells; above that, capture is skipped. It records conditional-format count but explicitly cannot restore conditional formatting. Capture/restore sections fail softly. Branch reversibility is therefore a bounded implementation property, not a general guarantee of artifact preservation.
2. Navigation can restore a snapshot and re-run code. This demonstrates mechanism availability, not deterministic replay, idempotence, or semantic equivalence across branches.
3. Segment explanations, ranges, Q&A, edit suggestions, and formula metadata are model outputs. The release has structural typing but no independent check that an explanation is faithful, a range is complete, or a claimed dependency is causally correct.
4. The back end has LLM-call logging and an `/interactions` endpoint. The archived front end exposes an endpoint helper but contains no corresponding event-producing `InteractionLogger` implementation. Study logging may have used unarchived code, but the public snapshot cannot verify its event schema or correspondence to analyzed interactions.
5. The released rubric scaffold asks the model to propose non-obvious checks, including unstated concerns. This can be useful assistance, but it also makes “tool-detected issue” an intervention generated inside the Pista condition rather than an independent measure of user oversight.

### Summative study

Sixteen participants aged 21–31 completed two 15-minute financial-analytics tasks in a within-subject design, one task per condition, after a 10-minute road-trip onboarding task (pp. 6–7; lines 302–364). Tasks were adapted from SpreadsheetBench and each had five scored subtasks. A financial-analytics expert reportedly confirmed ambiguity, equal difficulty, self-containment, and timing. Twelve participants were graduate students and four were financial-analytics professionals; spreadsheet experience ranged mostly from one to five years, with three at ten or more.

The baseline stripped Pista's features and directly applied changes before producing a summary. Task and condition were described as counterbalanced. The paper does not report the allocation table, randomization procedure, period/sequence effect, carryover analysis, or whether onboarding exposure was balanced for baseline-specific versus Pista-specific affordances.

Measures were:

- post-task verbal explanations, coded into procedural, mechanistic, formula, error, and specific-reference segments;
- seven-point questionnaire items on helpfulness, control, effort, understanding, detection, correction, and process alignment;
- logs for detected/fixed issues, prompt count/length, and feature use;
- proportion of five requirements judged satisfied from screen recordings (pp. 7–8; lines 368–424).

The paper says explanation raters resolved disagreements by discussion but reports no pre-adjudication reliability. It does not specify who judged task requirements, whether judges were blinded to condition, criterion-level rules, agreement, missingness, or whether final workbooks were retained and independently replayed.

## Evidence and results interpretation

### What the study supports

1. **Perceived traceability and control.** Most questionnaire items favor Pista; the paper reports signed-rank significance for understanding, tracking, formula identification, control, guidance, detection/correction, exploration, helpfulness, and effort (Figure 3, p. 8; lines 434–449).
2. **Richer post-task explanations.** Coded explanation count is higher with Pista (`4.38` versus `2.94`, `p=.015`; pp. 8–9; lines 471–520). This is evidence that participants verbalized more process/formula detail after the Pista condition, though not a direct test of correct understanding or future independent performance.
3. **Less prompting.** Participants used fewer prompts (`2.19`/`3.18` is reported in different passages versus `4.00` baseline) and shorter prompts (`12.9/13` versus `27.63/27.6` words; pp. 7 and 9; lines 368–399, 557–568). Localized edits plausibly reduce the need to restate global context.
4. **Feature uptake.** Branching was used by 15/16 participants; explanations by 10/16; task formulation by 9/16; and computation logic by 6/16 (Table 1, p. 7; lines 383–399). Availability was not equivalent to universal use.
5. **Comparable endpoint score under this study.** Mean requirement success was `0.53` for Pista and `0.50` for baseline (p. 7; lines 425–430). The paper calls these comparable but reports no inferential test or equivalence margin.

### What the study does not establish

1. **Independent error-detection advantage.** Pista sessions averaged `2.12` detected issues versus `1.75` for baseline, but the paper does not report an inferential comparison and Figure 4 combines user- and tool-detected issues. The treatment itself creates additional prompts/checks and visibility. No common planted-error set or matched agent trajectory establishes equal defect opportunity.
2. **Realized correction.** The methods say fixed issues were logged, yet the findings do not report a clear correction estimand, proposition-to-edit linkage, independent re-observation, or criterion-local before/after table.
3. **Error prevention.** The two conditions receive stochastic agent realizations and different affordances. There is no shared initial defective artifact or frozen pre-intervention state. The claim that users caught errors post-hoc review “would have failed to surface” is based on selected observations and participant counterfactual reports, not a matched post-hoc-review arm.
4. **Artifact integrity.** Final success is low in both conditions, is based on five requirements, and lacks native-workbook replay, recalculation, dependency mutation, protected-region checks, or collateral-regression analysis.
5. **Calibrated trust.** Participants report greater trust, but no reliable/unreliable-agent manipulation, confidence–correctness calibration, appropriate acceptance/rejection, or downstream decision loss is measured. One participant explicitly said greater trust reduced verification thoroughness (p. 9; lines 500–515), which is a warning rather than calibration evidence.
6. **Co-ownership as authority or accountability.** Twelve of 16 participants reported greater ownership (p. 9; lines 536–547). This is a meaningful experience outcome, not evidence of informed approval, valid authority transfer, accountability, or recipient acceptance.
7. **Professional utility or readiness.** No team receives, audits, modifies, or makes a decision with the workbook; no real workflow, consequential outcome, maintenance episode, or organizational burden is observed.

## Statistical and measurement audit

The within-subject design is a strength, but reporting weakens identification:

- Figure 3 uses `N=15` while the study reports `N=16`; the missing participant/item policy is unexplained (p. 8, line 448).
- Task and condition are counterbalanced, but no task-by-condition, period, sequence, learning, or carryover results are shown.
- The paper says Bonferroni correction was applied to multiple comparisons “on the same data,” but does not define comparison families, adjusted thresholds, or raw/adjusted p-values (p. 7; lines 401–405).
- Prompt count is analyzed with `t(15)` in one passage, while Figure 4's caption describes Mann–Whitney significance. Prompt length uses `U=3437.5`, but the unit of analysis is not stated; treating individual prompts as independent would be pseudoreplication because prompts are nested in participant sessions.
- Explanation count is a quantity proxy. More coded segments may reflect interface vocabulary/exposure, verbosity, or rehearsal rather than accurate comprehension. No answer key or transfer test scores correctness.
- “Issues detected” mixes human observation and tool-generated surfacing, so opportunity, source, correctness, novelty, severity, and downstream consequence are not separated.
- Requirement satisfaction is not accompanied by item results, blinded ratings, rater agreement, confidence intervals, or a noninferiority/equivalence analysis.
- Qualitative analysis produced 42 codes from interviews/screen recordings, but the summative study reports neither a coding-reliability statistic nor complete codebook, transcript, negative-case protocol, or participant-by-theme matrix.

## Unique insight: semantic diffs are oversight hypotheses, not oversight proof

Pista correctly identifies a mismatch between the **surface unit of change** and the **human unit of judgment**. Five hundred changed cells can be one semantic operation; one visible formula can conceal many dependencies and consequences. A semantic diff can therefore lower inspection cost by presenting an operation, rationale, dependency set, scope, and expected consequences.

But a semantic diff is itself an evaluated artifact. It can omit a dependency, rationalize code after generation, state the wrong affected range, hide a collateral effect, or direct attention away from an unsurfaced defect. Its value requires three independent validations:

1. **Diff fidelity:** does the surfaced operation faithfully and completely correspond to the actual state transition?
2. **Oversight utility:** does showing it improve human detection, diagnosis, decision, or repair relative to admissible alternatives and net of burden?
3. **Consequence validity:** do accepted/rejected interventions preserve required state and improve the downstream artifact or decision?

This yields an evidence ladder that should not be collapsed:

```text
semantic-diff availability
→ user exposure and inspected locator
→ correct comprehension
→ independent defect opportunity
→ supported detection/diagnosis
→ attempted intervention
→ agent receipt and semantic adoption or justified rejection
→ changed state at the intended locus
→ independent realized-correction check
→ collateral-state preservation
→ calibrated reliance and burden
→ recipient acceptance / professional consequence / readiness
```

Pista provides meaningful evidence near the first, second, and attempted-intervention rungs; limited proxy evidence for comprehension; and weak or absent evidence for the rest.

## Comparison with adjacent reviewed evidence

- **DeskCraft:** both show that an authored interaction channel is not human collaboration. DeskCraft's ladder—opportunity, realization, answer, receipt, adoption, repair, burden, recipient consequence—applies directly. Pista adds a decision-time semantic-diff representation and real human participants, but still lacks proposition-level adoption and matched state consequences.
- **AgencyBench:** AgencyBench makes evaluator-derived repair traces and plural artifact views more inspectable, while also showing why disclosed rubric defects estimate oracle-assisted repairability. Pista's generated requirements/questions may similarly disclose where to look. A matched no-new-information, consequence-only, criterion-disclosure, and authorized-human-feedback factorial is needed before attributing repair to semantic visibility.
- **ArtifactCopilot:** both generate evidence packets intended to improve human review. ArtifactCopilot shows that packet production and user confidence do not establish correctness without route completeness and adoption validity. Pista's semantic diff likewise needs raw-state locators, completeness checks, reviewer inspection events, overrides, and decision outcomes.
- **MBABench:** Pista observes formulas and ranges at execution time, but MBABench demonstrates that static formula visibility is not counterfactual workbook integrity. Native package state, pinned recalculation, rendered output, mutation tests, protected regions, and trace evidence remain separate admissible views.
- **Expert-disagreement evidence:** a user's “correct” intervention may encode a framework, preference, or context-specific threshold rather than a factual correction. Pista does not type these cases. Aggregating detection/correction counts without authority, evidence view, criterion interpretation, and decision loss can turn disagreement into a false oracle.
- **Handoff Debt and AgentCo-op:** a semantic diff can be useful to the immediate editor yet insufficient for a successor or later audit. Transport, structural parse, semantic/authority validity, receiver acceptance, next-operation success, and downstream consequence remain separate. Preserved branch history is not a validated handoff.

## Limitations and validity threats

1. The formative sample is young, technical, and university-centered; it does not estimate professional oversight needs.
2. The summative sample has 12 graduate students and only four financial-analytics professionals.
3. Two short, closed, 15-minute financial-analytics tasks do not cover long, open-ended, collaborative, high-consequence work.
4. One unspecified financial expert's task confirmation is not task-family validation or participant-population validity.
5. Five requirements per task supply a coarse endpoint and no severity, dependency, preservation, or decision threshold.
6. The within-subject counterbalancing procedure and allocation are not released.
7. No period, task, sequence, fatigue, learning, or carryover analysis is reported.
8. Survey `N=15` versus study `N=16` is unexplained.
9. The baseline and Pista conditions differ in a seven-feature bundle, model-call topology, information, editing scope, state history, and scaffolding—not only transparency.
10. The extra requirements/questions/edit suggestions can create evaluator cues and defect opportunities unavailable to baseline users.
11. Agent stochasticity means conditions may not contain equivalent defects.
12. No planted-defect, frozen-state, shared-artifact, or replay design identifies detection or repair effects.
13. “Issues” are not typed by source, truth, novelty, severity, or consequence.
14. User- and tool-detected issues are combined in headline visualization.
15. Fixed issues are named in methods but not reported through a reproducible correction table.
16. No proposition-level link connects observation, correction, generated branch, changed cells, re-verification, and collateral effects.
17. Success scoring lacks released criteria, item outcomes, blinded assessment, and rater reliability.
18. Comparable success is asserted without an equivalence margin or reported test.
19. Explanation-segment count is not correctness, transfer, or decision quality.
20. Prompt-length analysis may use nested prompts as independent units; the unit and clustering are unspecified.
21. Multiple-comparison families and adjusted p-values are absent.
22. Qualitative results rely on selected quotes and an unreleased 42-code analysis without summative reliability.
23. Feature-use counts do not establish feature correctness, necessity, or causal utility.
24. Self-reported trust, control, and ownership do not establish calibrated reliance or valid accountability.
25. No misleading semantic-diff, omitted-dependency, false-explanation, or overtrust control tests calibrated distrust.
26. No tokens, API cost, wall time, latency, verification time, correction time, or branch-review burden is reported.
27. Snapshot restoration is capped and incomplete in the release; conditional formatting is not restored.
28. Model-generated explanations/ranges/dependencies are not independently checked for faithfulness or completeness.
29. The released interaction-log path is incomplete at the front-end event-production layer, and no study logs are released.
30. The paper does not pin exact code commits, prompts, endpoint dates, decoding, seeds, retries, invalid outputs, or service failures.
31. No raw surveys, interviews, videos, workbooks, traces, task allocation, score rows, or analysis code are public.
32. Pre-v1 repository heads support implementation availability but do not prove they are the exact study builds.
33. No real recipient, downstream decision, delayed audit, maintenance episode, team handoff, or deployment outcome is observed.
34. The paper's broad claim that meaningful oversight “requires” participation is stronger than the two-task bundled usability evidence.

## Reproducibility and operational realism

**Paper inspectability is good; empirical reproducibility is poor.** The immutable paper supplies the architecture, participants, tasks, feature set, measures, aggregate results, questionnaire figure, feature counts, and headline tests. The two pre-v1 repositories expose a substantial mechanism-level implementation rather than a post-paper placeholder. That permits inspection of segment schemas, model assignments, snapshots, branching, execution, rubrics, and logging affordances.

Exact reproduction is blocked by absent study builds, task files, initial workbooks, generated trajectories, condition order, participant records, questionnaires, codebook, raw logs, final artifacts, rater decisions, statistical data, and analysis scripts. Mutable preview model endpoints further limit replay. A new run of the archived code would be evidence about that configured snapshot, not a reproduction unless study correspondence and inputs were established.

**Operational realism is mixed.** Native Excel, formulas, multi-sheet operations, direct artifact mutation, branching, failures, and short finance-derived tasks are more realistic than answer-only evaluation. Yet the study is a one-hour lab interaction with no organizational roles, real work products, existing stakeholder constraints, delayed consequences, recipient handoff, maintenance, or production service ledger. It evaluates an interaction concept, not professional oversight performance.

## Transfer to skill-bench

### Retain

1. Treat semantic operation, affected range, dependencies, rationale, and expected consequences as a reviewable artifact distinct from a surface diff.
2. Pause at decision- or consequence-bearing transitions rather than every low-level operation.
3. Preserve branch lineage and immutable pre-intervention state for comparison and rollback.
4. Allow localized questions and edits while retaining the original trajectory.
5. Keep understanding, interaction effort, detection, correction, artifact quality, trust, ownership, and cost as separate outcomes.

### Repair

1. Validate semantic-diff fidelity against raw pre/post native state and dependency observers; permit `incomplete`, `contradicted`, and `insufficient_evidence` outcomes.
2. Type each issue and intervention by source, authority, evidence locator, public/private information, severity, requested change, and valid scope.
3. Link exposure, inspection, detection, edit, receipt, adoption/rejection, changed loci, re-observation, collateral regression, and endpoint consequence.
4. Use a frozen defective artifact or identical pre-intervention trajectory across conditions so error opportunity is shared.
5. Factor visibility from scaffolding and control: surface-only diff; verified semantic diff; semantic diff plus ask; plus local edit; plus requirement/question suggestions; and misleading/incomplete-diff controls.
6. Grade native state, recalculation, rendered output, preservation, task requirements, and human/recipient acceptance through criterion-specific admissible views.
7. Measure review and intervention burden—time, actions, tokens, latency, attention, verification, rework, and lifecycle cost—not prompt length alone.
8. Test trust calibration with reliable, unreliable, omitted-dependency, and false-rationale cases; score appropriate inspect/accept/reject/escalate behavior.
9. Cluster analysis by participant and task, report period/sequence effects, define missingness, and publish paired item-level transitions.
10. Keep the claim ceiling: a semantic-diff interface can be inspectable and useful without proving effective oversight, professional validity, or readiness.

## Concrete repository actions

- Added this full-text and implementation-audited deep review.
- Updated the paper index from source-acquired/pending to deep-review complete with exact artifact paths and release boundary.
- Added Pista to topic navigation as an active-oversight and semantic-diff validity case.
- **No new queue task added.** The completed interaction-evidence consolidation, feedback/recovery edges, artifact-view admissibility, configured-system identity, task-health, metric, validity, handoff, and evidence-chain machinery already provide homes for every requirement. Pista supplies planted validation cases—faithful versus incomplete/misleading semantic diff, shared defect opportunity, proposition-level adoption, preserved state, calibrated reliance, and burden—not a nonduplicate subsystem.
- The grouped synthesis index was not changed in this review run. Pista reinforces, rather than overturns, the existing interaction and feedback ladders; a later consolidation can place it alongside DeskCraft and AgencyBench without narrowing the project to spreadsheets.

## Assessment

- **Evidence tier:** B — complete immutable paper read; official publication page verified; both author-linked pre-v1 implementation archives inspected; empirical records absent.
- **Most reusable contribution:** semantic diffs as operation-level, decision-time inspection objects tied to localized branchable intervention.
- **Strongest evidence:** greater perceived inspectability/control, richer post-task explanations, high branch use, and reduced prompt burden in a small counterbalanced two-task lab study.
- **Most serious validity flaw:** the treatment bundles visibility, requirements, questions, edits, branching, and extra model-generated cues without matched defect opportunities or proposition-level repair evidence.
- **Most serious safety warning:** increased trust sometimes reduced verification thoroughness, while semantic-diff faithfulness and completeness were not tested.
- **Safe claim:** under one bundled Excel workflow with 16 mostly graduate-student participants, Pista made agent actions easier to inspect and discuss and made redirection less prompt-intensive without measurably improving the reported five-requirement endpoint mean. It does not establish general error prevention, calibrated oversight, professional utility, co-ownership validity, or deployment readiness.
