# Paper Review: MBABench — Static Workbook Judgment Is Not Yet Counterfactual Artifact Validation

- **Paper:** https://arxiv.org/abs/2605.22664v4
- **Authors:** Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, Yilin Meng, Joshua Fan, Adam Shen, Yili Liu, Ali Bauyrzhan, Siri Du, Haoyang Liu, Daniel Guetta, Hongseok Namkoong
- **Date read:** 2026-07-11
- **Venue / source:** arXiv preprint
- **Version read:** immutable v4, 22 June 2026
- **Local PDF:** `data/papers/pdfs/2605.22664v4-mbabench-evaluating-llm-agents-on-end-to-end-sprea.pdf` (40 pages; SHA-256 `c98bf65e717d0573cb6130f184e84e5a633236d5672c8c98167e91a5f634cd6f`)
- **Local text:** `data/papers/text/2605.22664v4-mbabench-evaluating-llm-agents-on-end-to-end-sprea.txt` (SHA-256 `fcabf603ccfcf5bd01daf4cc65ac16e7553bba7b32f4371961739eb4c5d57aa7`)
- **Official code inspected:** https://github.com/namkoong-lab/MBABench/tree/c56319bea67fa5bfea8ed8010e93a88e1b8877e5 (post-v4 commit at 22 June 2026 17:48 UTC)
- **Official data inspected:** https://huggingface.co/datasets/namkoong-lab/mbabench-modeloff/tree/867fb5395b8e3fc28606dc681ba5ea284340ddd2 (38 ModelOff tasks; 113 files; two complete task triples downloaded)
- **Release provenance:** `data/sources/releases/2605.22664v4-mbabench/provenance.json`
- **Tags:** spreadsheets, finance, artifact-evaluation, llm-judge, recalculation, formula-provenance, formatting, configured-systems, validity

## One-sentence contribution

MBABench makes an important construct correction—professional spreadsheet work is the production of a complete, reviewable, editable workbook rather than a correct cell—and contributes authentic finance cases, configured GUI/API execution paths, a 17-criterion Accuracy/Formula/Format rubric, and expert-checked LLM judgments; but the reported professional-quality score is still mostly a **static comparison of serialized workbook cells against one reference**, with no direct counterfactual mutation test, no workbook rendering for charts and layout, incompletely released validation/results, criterion-level rather than deployment-level judge evidence, and paper/release scoring drift.

## Why this matters for skill-bench

MBABench directly advances charter objectives A, B, and C. It targets a consequential knowledge-work artifact whose usefulness depends on several simultaneous properties: numerical correctness, accounting identities, dependency flow, native formulas, assumption editability, auditability, workbook organization, and presentation. Its central claim—that final-answer checking misses hardcoded but numerically correct outputs and off-by-one formulas whose current values happen to match—is persuasive and strongly relevant to `skill-bench`.

The paper also exposes the next validity boundary. A workbook is valuable because another person can **change it and trust what happens next**. MBABench describes this counterfactual property but primarily grades a static serialization containing cached display values, formulas, and selected cell formatting. This evidence can suggest maintainability; it does not demonstrate it. The strongest transferable lesson is therefore not merely “grade formulas and formatting.” It is:

> Treat an editable artifact as a behavioral system. Validate its current state, dependency structure, rendered views, and responses to authoritative perturbations separately.

This remains a spreadsheet-methodology case, not a reason to narrow `skill-bench` to finance. The same distinction applies to editable analyses, slide decks with linked charts, executable visualizations, CAD files, database-backed reports, and decision models.

## Research question and claim boundary

The paper asks whether current LLM agents can produce end-to-end financial workbooks at professional quality, how such quality should be decomposed, whether an LLM judge can assess it reliably, and how model/harness performance changes with task difficulty.

The evidence supports several bounded claims:

1. The collected competition/training cases are substantially larger and more interconnected than single-cell spreadsheet benchmarks: the paper reports 33× more cells in mean and 93× more function calls in median than SpreadsheetBench (Table 1, p. 4).
2. Static final-value checks miss consequential defects such as hardcoded results and coincidentally correct formulas (Section 5, pp. 6–7).
3. On 408 criterion labels drawn from selected agent attempts, the paper’s judges agree strongly but imperfectly with expert annotations: 0.92 accuracy, 0.88 balanced accuracy, and 0.85 F1 overall; the agentic and non-agentic variants differ materially (Appendix E.2, p. 38).
4. Under the evaluated configured systems, Claude Web has the highest reported composite score, 69.1/100, and scores fall with author-assigned difficulty (Section 6, pp. 7–9).
5. Harness realization matters: agents using the same broad model family but different Excel/web/API interfaces produce materially different artifacts.

The evidence does **not** establish a calibrated threshold for professional acceptability, reliable behavior after assumption changes, validity for visually judged dashboards, representative coverage of finance work, causal superiority of a model family or interface, human parity, or production readiness. The 69.1 score is a weighted rubric summary, not an observed rate of workbooks that a finance organization accepted, reused, or used for a decision.

## Methodology

### Task sourcing and expertise

Tasks come from Financial Modeling World Cup (FMWC), ModelOff, and Wall Street Prep (WSP). They include valuation, three-statement models, working-capital analysis, FP&A, debt/equity schedules, wealth management, and business/data analytics. Difficulty is assigned from four 1–6 subscales—scope, general modeling, finance knowledge, and Excel implementation—with weights 1/3, 1/3, 1/6, and 1/6, then rounded (Appendix B, pp. 16–19). Task types are assigned by Gemini 2.5 Pro in two passes and manually checked on only ten randomly selected tasks (Appendix B.7, pp. 22–23).

These are authentic competition and training artifacts, but authenticity is heterogeneous. FMWC and ModelOff cases were designed under competition constraints and often culminate in multiple-choice answers. WSP exercises are training cases and, by the paper’s own account, often test one specific operation rather than construction of an entire model (Appendix F, pp. 38–39). ModelOff reference workbooks are competitor submissions rather than organizer-provided ground truth. Thus “used in finance education/competition” is credible; “representative of ordinary production finance work” is not demonstrated by a sampling frame, workplace observation, or downstream use study.

The expert effort is substantial: two MBAs and three finance professionals reportedly spent more than 700 hours iterating rubric descriptions, constructing perturbations, and annotating judge examples (Section 5, p. 7). However, the paper does not give a contribution ledger by person, qualifications beyond role labels, task-author versus rubric-author versus rater assignments, independent double-labeling design, disagreement/adjudication procedure, compensation, or annotation time by activity. Competition authors and benchmark experts are also different authority sources; the paper does not reconstruct requirement provenance from original task author to benchmark criterion.

### Agent and harness conditions

The evaluation spans:

- an in-house API/MCP Excel CLI agent using OpenPyXL and LibreOffice;
- Excel Online add-in agents driven through Playwright;
- web-chat agents that upload files and download generated workbooks;
- proprietary ChatGPT Agent/Pro conditions.

The API framework gives models up to 15 iterations and 19 MCP tools for file, worksheet, cell, inspection, formatting, and formula-validation operations. It recalculates through LibreOffice after formula and cell writes (Appendix C.4, pp. 28–29). GUI and web systems expose different tools, hidden internal scaffolds, contexts, account tiers, and execution environments. The paper appropriately treats harness quality as a likely explanation but cannot isolate it causally.

Runs have a 120-minute task cap and a 25 MB attachment limit. One task is excluded by the size limit. Pipeline failures can be retried up to ten times and agent failures up to three times; this raises successful artifact collection above 99% (Appendix D.3, p. 36). That policy is operationally understandable but changes the estimand: reported quality is largely conditional on eventually obtaining an artifact, while first-attempt reliability, retry burden, and the distribution of discarded failures are not part of the score. Safety rejections are not retried in the same way. The paper reports roughly $7.4K to run all API agents and $1.7K for one judge round, but does not provide task/model-level cost, GUI subscription allocation, retry cost, expert cost, or confidence intervals.

### Workbook representation and judge

The rubric has three categories:

- **Accuracy:** final calculations, starting values, task completion, sign consistency;
- **Formula:** logic readability, edge handling, hardcoding, range hygiene, absolute references;
- **Format:** sheet structure, readability, color standards, number notation, alignment, style consistency, borders/shading, and output presentation.

The paper describes category weights of 50% Accuracy, 35% Formula, and 15% Format. Its Figure 2 assigns 35% of Accuracy to final calculations and 15% to sign consistency. The inspected release instead assigns 40% and 10% respectively (`judge/prompts/rubrics/rubric_6_weights.json`). This is not cosmetic: the released composite does not exactly instantiate the paper’s displayed score.

The standard judge loads both formula and `data_only` workbook views. It serializes each nonempty cell as coordinate, formatted display value, formula, and selected style properties, then adds merged-cell and freeze-pane summaries (`judge/utils/excel_utils.py`, lines 701–923). For files over a two-million-character budget, an agentic judge selectively reads sheets, ranges, formulas, and formatting (Appendix E.2; released agentic path). The standard and agentic judges therefore have different observation policies, and their reported performance differs: agentic 0.90 accuracy/0.89 balanced accuracy/0.87 F1 on 221 labels versus non-agentic 0.94/0.83/0.79 on 187 labels.

The released scorer is binary at criterion level in practice. With `rubric_max_mistakes: 1`, one recorded mistake reduces the entire criterion to zero; additional mistakes do not reduce it further. Missing criteria are conservatively scored zero, duplicate judgments retain the worst mistake count, and a failed decision with no mistake list receives the maximum penalty (`judge/main_scripts/judge.py`, lines 180–332). This makes scores easy to aggregate but collapses severity, extent, repair cost, and affected decision. A single minor number-formatting defect and pervasive number-formatting failure have the same criterion score.

No deterministic formula-dependency, accounting-identity, workbook-corruption, external-link, circularity, or metamorphic checker is part of the main scoring model described. The LLM sees the reference and candidate serializations and judges their relationship. This permits legitimate structural alternatives in principle, as the paper says, but also anchors judgments to one witness. Appendix D explicitly says differently positioned correct calculations are penalized because the judge compares fixed positions to the golden solution (p. 34), which conflicts with the stronger claim that any rubric-satisfying alternate structure should pass.

### Expert validation

The 408 annotations correspond to criterion decisions over selected workbooks from Claude Web, Claude Excel, and ChatGPT Excel across the task IDs shown in Tables 3 and 4. The paper reports classification metrics over labels, not acceptance decisions over complete workbooks. It does not report confidence intervals, prevalence, per-criterion sensitivity/specificity, rater-by-item matrices, number of independent raters per label, agreement among humans, held-out judge selection, workbook/task clustering, or a leave-task-family-out test.

The two judge modes are evaluated on disjoint annotation subsets (221 and 187 labels), so their metrics are not a clean paired comparison. The attempt sample covers only three agent interfaces and a small set of task IDs; it does not validate the judge on the API agents, all task families, many legitimate alternate models, corrupted files, adversarial artifacts, or threshold-near professional decisions. Synthetic perturbation results are shown as caught/not-caught marks for selected tasks and criteria rather than a complete perturbation inventory with rates and uncertainty.

## Evidence and results interpretation

The most credible substantive result is qualitative: current agents often compute outside Excel and paste correct values, fail to preserve dependencies, leave blank outputs, create monolithic formulas, or produce inconsistent presentation. These are genuine professional defects that exact-value benchmarks systematically miss. The paper’s examples of an off-by-one aggregation and a 1,000-row hardcoded simulation demonstrate why formula provenance and model structure matter.

The leaderboard is descriptive of configured systems, not models in isolation. Claude Web, Claude Excel, the in-house Opus agent, and other systems differ in interface, hidden tools, workbook-edit method, context handling, formula recalculation, retries, and model endpoint. The paper recognizes this, yet statements that one model family is strongest remain easy to overread. A matched intervention on the same model, prompt, task set, tool affordances, and retry policy is needed for causal harness conclusions.

The difficulty trend is plausible but under-identified. Difficulty labels are expert-weighted composites rounded to five realized levels; there are only seven level-5 tasks. Task source, task type, workbook size, formula count, file size, and agent/tool compatibility co-vary with difficulty. Scores are nested within tasks and likely within source families, but the paper shows means and standard errors without a hierarchical model, repeated trials, or task-clustered inference. The trend demonstrates that the selected configured systems score lower on selected harder cases, not that one scalar difficulty variable causes failure.

The 0.92 judge accuracy is useful engineering evidence, not evidence that the judge replaces expert review. Balanced accuracy of 0.88 and F1 of 0.85 already imply consequential minority-class errors; criterion labels are dependent within workbook; and errors concentrate in nuanced formatting and structural criteria. No professional release threshold or asymmetric loss function is tested. A false pass on final calculations or task completion is not equivalent to a false fail on one border.

## Two released task traces

### Task 13 — Bread and Butter: integrated three-statement acquisition model

The task requires a ten-year, three-way integrated model with debt, depreciation tranches, working capital, distributions, IRR, and scenario questions. The starting workbook has three sheets, 448 nonempty cells, and 80 formulas. The released reference has five sheets, 834 nonempty cells, and 541 formulas, including a dedicated Q&A sheet with formula-linked answers. This is a meaningful end-to-end construction delta rather than a one-cell edit.

The reference also contains three external-link records and many Capital IQ-related defined names, while the starting workbook has no external links. Structural inspection does not prove those links are live dependencies or defects, but it demonstrates why a “gold solution” cannot be treated as automatically rubric-perfect: reference workbooks may preserve legacy add-ins, names, links, and authoring residue. A valid grader must classify external links as required, benign residue, broken dependency, forbidden dependency, or insufficiently inspected—not silently inherit their legitimacy from the witness.

Most importantly, the stated construct is dynamic flow from assumptions through all statements. The released summary shows formulas and `fullCalcOnLoad`, but no benchmark trial mutates revenue growth, debt rate, capex timing, or distribution threshold and checks balance, cash flow, and IRR after recalculation. Static formula presence is only indirect evidence of the central behavior.

### Task 21 — The Hard Sell: board dashboard

The instruction asks for a printable Letter/A4 dashboard with annual financial statements, debt profile, traffic profile, CEO/CFO-relevant information, supplied branding, and judged visual aesthetics. The starting workbook already contains nine model sheets with 21,629 nonempty cells and 20,400 formulas. The reference adds one Dashboard sheet; the resulting workbook has 21,763 nonempty cells, 20,412 formulas, and two charts. The actual task delta is therefore a visual communication layer over a largely complete model, not construction of the full 20,000-formula workbook.

This task is decisive evidence of an evaluator-view mismatch. The released standard judge serializes cells, formulas, number formats, fonts, fills, borders, merged ranges, and freeze panes. It does not render workbook pages or pass chart/image objects or print layout to the judge. The instruction’s core predicates—chart selection, visual hierarchy, logo/color fidelity, A4/Letter fit, clutter, board readability, and aesthetics—cannot be fully observed from the provided candidate view. The judge may infer some formatting from cells but cannot validly certify the dashboard as presented. In the language of the existing `skill-bench` artifact-admissibility contract, these checks require a rendered worksheet/print view and native chart/state view; without them the correct outcome is `insufficient_evidence`, not a confident Format score.

Trace files and structural measurements are preserved under `data/sources/releases/2605.22664v4-mbabench/task-traces/` and `task-trace-summary.json`.

## Unique insight

MBABench reveals a distinction between **static artifact fidelity** and **counterfactual artifact integrity**.

A professional spreadsheet is not merely a file whose current cells look right. It is a small executable decision system. Its core contract is:

`authoritative input mutation → recalculation semantics → dependency propagation → invariant checks → updated outputs/charts → preserved presentation and provenance`

The paper’s Formula rubric points toward this contract but the evaluation usually infers it from formula text and a reference workbook. Directly exercising the contract would be stronger and often cheaper than asking a judge to speculate. Examples include changing a revenue assumption and checking downstream statements, moving a model start date and checking timeline headers, adding a row and checking dynamic ranges/charts, setting EBITDA to zero and checking error behavior, breaking an external source and checking explicit failure, or changing a debt assumption and checking that interest, cash, and balance sheet remain coherent.

A second insight is that end-to-end task scale must be measured as the **required delta from initial state**, not only the size of the final reference artifact. Task 21’s reference contains more than 20,000 formulas, but almost all are already in the starting workbook; the authored work is a dashboard sheet with 12 formulas and two charts. Final artifact size can dramatically overstate agent-created complexity and confound task difficulty. `skill-bench` should record initial-state complexity, required mutation surface, preserved-state obligations, and final-state complexity separately.

A third insight is that reference artifacts are **fallible witnesses**, not normative specifications. The task-13 reference’s external links and legacy defined names illustrate this directly. Reference quirks must be reviewed against requirement authority and declared invariances; otherwise an LLM judge can reward imitation or penalize legitimate cleanup.

## Transferable design patterns

### 1. Separate authoritative workbook views

Preserve at least four evidence views:

1. native package/state: workbook XML, sheets, names, links, charts, images, print settings, calculation properties;
2. executable view: formulas, dependency graph, recalculated values, errors, and convergence behavior in a pinned engine;
3. rendered view: worksheet and print/PDF renderings under pinned fonts, page setup, zoom, and renderer;
4. provenance/trace view: what the agent read, changed, recalculated, validated, and exported.

Each criterion should declare which views are necessary and which are merely suggestive.

### 2. Add counterfactual/metamorphic checks

Expert authors should identify a small set of meaningful mutations and invariants. Recalculate in a pinned Excel-compatible engine, compare affected and unaffected regions, and verify accounting, decision, and presentation consequences. Mutation tests are direct evidence of editability, hardcoding avoidance, absolute-reference correctness, dynamic-range behavior, and edge handling.

### 3. Measure task delta, not just final size

Record initial and final sheets/cells/formulas/charts, semantic diff, required preserved regions, permitted restructuring, and newly constructed dependency depth. A large inherited model plus one dashboard is a different capability from building the large model.

### 4. Treat reference solutions as reviewed witnesses

Record who created each witness, whether it is organizer-authoritative or competitor-provided, known external links/add-ins, calculation engine/version, residual errors, alternative valid structures, and criterion exceptions. Gold should not mean infallible.

### 5. Preserve severity and gating

Keep criterion verdict, mistake count, affected range, materiality, downstream consequence, repair effort, and decision impact. Gate invalid/corrupt/incomplete artifacts and safety-critical calculation failures instead of allowing weighted compensation. Do not equate one cosmetic defect with pervasive logic failure.

### 6. Validate judges on decisions and alternatives

Use held-out workbooks across task families, generator families, output sizes, corrupted files, visually strong/structurally wrong artifacts, structurally different but valid models, and threshold-near cases. Report rater design, human disagreement, criterion confusion matrices, calibration/abstention, task-clustered intervals, and asymmetric-loss sensitivity.

### 7. Report configured systems and retry estimands

Pin model endpoint, prompt, interface/add-in, file-edit mode, tool schema, spreadsheet engine, calculation settings, account tier, timeout, retry policy, and network access. Report first-attempt completion, eventual completion, quality conditional on artifact, and total retry/cost burden separately.

## Comparison with SciVisAgentBench and GDPval

Compared with [SciVisAgentBench](2026-07-10-scivisagentbench-multimodal-artifact-evaluation.md), MBABench has a sharper professional-artifact rubric for native spreadsheet structure, but a narrower evaluator evidence view. SciVisAgentBench explicitly varies artifact representations and evaluator families—rendered images, executable code, structured state, coordinates, segmentations, and topology metrics—although it then weakens those distinctions through aggregation. MBABench serializes most criteria through one cell/formula/style view plus an LLM. The dashboard trace shows why SciVisAgentBench's evaluator-admissibility lesson applies directly: native cells, executable dependencies, and rendered charts answer different questions and should not be treated as interchangeable witnesses.

Compared with [GDPval](2026-07-10-gdpval-occupational-task-validity.md), MBABench offers a more inspectable spreadsheet-specific rubric and released judge implementation, while GDPval has broader occupational framing, expert-authored tasks, and pairwise professional artifact evaluation. Neither source establishes an expert ceiling or representative population of work: GDPval's equal-quota occupational assembly is not economic weighting, and MBABench's competition/training corpus is not a finance-work sampling frame. Both use one human artifact as a witness rather than a complete specification, but MBABench additionally exposes formula and native-workbook structure; GDPval's pairwise preference better accommodates holistic alternatives while providing weaker absolute threshold semantics. The combined implication for `skill-bench` is to preserve inspectable native checks, plural artifact views, and expert disagreement without promoting reference similarity or pairwise preference into professional readiness.

## Limitations and validity threats

1. **No finance-work sampling frame.** Competition and training cases provide authenticity but not representative coverage of professional finance.
2. **Task sources have different constructs.** Some WSP exercises are explicitly atomic/linear; FMWC includes competition-time shortcuts and multiple-choice endpoints; ModelOff references are competitor submissions.
3. **Expert provenance is coarse.** The 700+ hours are impressive but roles, qualifications, assignment, independence, disagreement, adjudication, and compensation are under-specified.
4. **Type validation is minimal.** Gemini-derived task types are manually checked on only ten tasks.
5. **Difficulty is subjective and confounded.** Rounded author ratings co-vary with source, size, type, and tool compatibility; only seven tasks reach level 5 and none reaches level 6.
6. **Final size overstates required work.** The dashboard trace inherits 20,400 formulas and adds only 12, so final formula count is not construction complexity.
7. **Reference artifacts are not certified specifications.** ModelOff references are competitor work; task 13 retains external-link records and legacy names.
8. **Static evidence undermeasures editability.** No systematic assumption mutation, recalculation, invariant, or dynamic-chart trial is reported.
9. **Rendered presentation is absent.** The released judge does not observe workbook/chart/print rendering, yet scores visual dashboard criteria.
10. **Chart and image semantics are omitted.** Cell/style serialization cannot establish chart encodings, logo use, visual hierarchy, or page fit.
11. **Recalculation is not a single controlled treatment.** The CLI framework recalculates frequently with LibreOffice, while the judge’s local recalculation flag is optional and default-off at the function/CLI level.
12. **Excel/LibreOffice behavior may differ.** Circular references, iterative calculation, modern functions, cached values, external links, and chart rendering are engine-dependent.
13. **Circularity is a known harness limitation.** The paper reports 1,044 `#VALUE!` errors on a circular-reference case in a GUI/LibreOffice path, making some scores environment evidence rather than agent capability evidence.
14. **Alternative-validity claims conflict with implementation description.** The paper says rubric-satisfying alternatives should pass, but Appendix D says fixed-position reference differences are penalized.
15. **One witness anchors the judge.** Reference structure can bias judgments toward imitation and against legitimate alternate layouts or modeling conventions.
16. **Criterion scoring is severity-blind.** With maximum mistakes set to one, any single mistake zeros the criterion and further mistakes add no penalty.
17. **Aggregation is subjective and drifted.** Paper and released weights differ for final calculations and sign consistency; no stakeholder utility study validates either weighting.
18. **Mandatory defects can compensate.** Accuracy, formula, and format points combine into one score without a published professional-acceptance gate.
19. **Judge labels are dependent.** Seventeen labels from one workbook share artifact and rater context; headline metrics do not account for clustering.
20. **Judge validation is narrow.** Selected tasks, three GUI agents, no reported independent-rater reliability, no intervals, and no held-out task-family/generalization test.
21. **Agentic/non-agentic metrics are not paired.** Their different label subsets prevent clean comparison of observation policy.
22. **Synthetic validation is incompletely quantified.** Tables show selected caught/missed marks rather than a released complete perturbation population and error rates.
23. **Retry policy conditions away operational failure.** Up to ten pipeline and three agent retries can turn instability into eventual artifacts without charging reliability scores.
24. **Missing/invalid policy is incomplete.** Safety refusals and infrastructure failures receive different treatment; discarded attempts and denominators are not released.
25. **Configured-system comparisons are confounded.** Model, endpoint, GUI, hidden scaffold, tool affordances, calculation engine, context, and account tier vary together.
26. **Uncertainty is weak.** No repeated-task trials, paired tests, hierarchical/task-clustered intervals, provider drift analysis, or order/seed record is reported.
27. **Cost accounting is aggregate.** Approximate $7.4K agent and $1.7K judge totals omit task/model/retry/expert distributions and maintenance burden.
28. **Professional quality is not externally validated.** No independent finance team accepts, edits, uses, or makes a decision from the artifacts.
29. **Release does not reproduce tables.** Raw attempts, 408 expert labels, perturbations, grader outputs, exact result matrix, and table-reproduction scripts were not found.
30. **Release timing is post-v4.** The inspected code/data landed roughly 16 hours after v4 and cannot prove exact paper-time behavior.
31. **Public solutions create contamination.** The released ModelOff tasks include starting and reference files; they remain useful for regression/inspection but weaken future capability claims.
32. **Dataset redistribution authority is unclear in the inspected metadata.** The code repository is MIT-licensed, but the Hugging Face dataset metadata inspected here does not state an explicit dataset license.

## Reproducibility and operational realism

Reproducibility is **moderate for inspecting tasks, agent harnesses, and the current judge; weak for reproducing the paper’s results**. The complete immutable 40-page paper is local. The official post-v4 GitHub archive is pinned and contains three agent suites, prompts, rubric/weights, workbook extraction, standard and agentic judges, orchestration, and local setup documentation. The official ModelOff revision exposes 38 tasks; its entire 113-file tree is pinned, and two task triples from distinct workflow families are locally preserved and structurally inspected.

The release does not contain the raw 408 expert labels, rater assignments, synthetic perturbation suite, complete attempts, reported score matrix, discarded/retried run records, paper-table analysis, or immutable model responses. The released judge uses a mutable commercial model (`google/gemini-3-flash-preview`) and OpenRouter, while GUI agents require commercial accounts and changing proprietary products. Reproducing the headline ranking would require substantial spend, provider access, Microsoft/Excel environments, GUI automation, LibreOffice, task corpora beyond the mirrored ModelOff subset, and paper-time endpoint behavior.

Operational realism is mixed but materially stronger than atomic spreadsheet QA. Real `.xlsx` files, authentic instructions, inherited templates, multi-sheet dependencies, commercial add-ins, web interfaces, file transfer, time limits, formulas, styles, and large contexts expose genuine system failures. Conversely, competition cases, retries, reference-anchored static judgment, unrendered formatting, no downstream stakeholder use, and no systematic counterfactual edits omit central parts of workplace handoff and maintenance.

## Concrete changes for skill-bench

1. **Use the existing artifact-admissibility envelope rather than add a new schema.** For spreadsheet-like pilots, require native package, executable/recalculated, rendered/print, and trace views; make chart/aesthetic criteria abstain when render evidence is absent.
2. **Extend existing task projection records with initial-to-final semantic delta evidence.** Record inherited complexity, required mutation surface, preserved zones, permitted restructuring, and final complexity. This refines current projection/workspace contracts rather than creating spreadsheet-specific machinery.
3. **Add spreadsheet-style metamorphic cases to existing planted evaluator tests.** Mutate an assumption, model start date, edge-case denominator, and appended row; verify downstream values, unaffected regions, identities, charts/ranges, and explicit errors under a pinned engine.
4. **Treat reference artifacts as witnesses with health records.** Scan external links, defined names, calculation settings, cached/formula discrepancies, errors, circularity, charts, macros, and print settings; record exceptions and alternative valid structures.
5. **Keep criterion observations plural and severity-aware.** Preserve current-value correctness, recalculation behavior, dependency provenance, native integrity, rendered communication, and human readiness separately before any weighted metric.
6. **Use existing metric/validity machinery to block score promotion.** A criterion-label agreement study cannot license “professional quality,” expert replacement, or deployment readiness; require a stakeholder threshold/loss study and held-out clustered validation.
7. **Report retry and environment validity separately.** First-attempt failure, eventual artifact production, artifact quality, environment invalidity, and cost should be separate outputs.
8. **Add no new queue task.** The concrete obligations map to the completed evaluator-admissibility slice and existing task-projection, workspace, task-health, metric-monitoring, validity, and cross-record evidence-chain contracts; a new spreadsheet subsystem would duplicate them.

## Action items for repository

- [x] Read the complete immutable arXiv v4 PDF/text.
- [x] Archive and inspect the complete official code release at commit `c56319bea67fa5bfea8ed8010e93a88e1b8877e5`, preserving its post-v4 timing boundary.
- [x] Pin the official 38-task ModelOff dataset at revision `867fb5395b8e3fc28606dc681ba5ea284340ddd2`.
- [x] Trace the Bread and Butter three-statement model and Hard Sell dashboard from instructions and starting workbook to reference workbook.
- [x] Audit rubric weights, score semantics, workbook extraction/evidence views, recalculation, agentic overflow, retries, costs, expert validation, and release completeness.
- [x] Distinguish paper claims, post-v4 release observations, and `skill-bench` adaptations.
- [x] Map findings to existing contracts and add no duplicate build task.
