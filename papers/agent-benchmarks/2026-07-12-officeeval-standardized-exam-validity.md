# OfficeEval: a standardized practical exam is an external rubric anchor, not a professional-readiness threshold

**Source type:** Deep review of the complete immutable arXiv v1 paper; no official benchmark release identified  
**Paper:** Tengchao Lv et al. (Microsoft Research), *Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?*  
**Immutable source:** https://arxiv.org/abs/2606.10956v1 (9 June 2026)  
**Local PDF:** `data/papers/pdfs/2606.10956v1-mind-the-gap-office-proficiency-exam.pdf` (21 pages; SHA-256 `4dc59a862be7fd8759ea385df8ee6ef9a1f294a31d60da1721f66c45c3d89ba1`)  
**Local full text:** `data/papers/text/2606.10956v1-mind-the-gap-office-proficiency-exam.txt` (SHA-256 `61a70607f9e6b02843ae9fa0708838d3563bde0021d46b12951136bacc153e58`)  
**Date read:** 2026-07-12  
**Release boundary:** The paper says the copyrighted NCRE task statements, inputs, scoring configurations, and scripts are not redistributed (§3.1, p. 4). No official task/code/data release is identified. A third-party community reproduction discovered during acquisition is not paper-release evidence and was not used.

## Review judgment

OfficeEval's durable contribution is an unusually dense, externally authored **artifact-property instrument**: 200 practical tasks from China's National Computer Rank Examination (NCRE), native Word/Excel/PowerPoint inputs and outputs, and 7,118 weighted deterministic criteria. Unlike synthetic office suites whose authors invent both tasks and checks, the requirements and point allocations predate this study. That external lineage gives the score a credible meaning: percentage of points earned on this selected practical-operation task set.

The paper nevertheless repeatedly approaches a validity leap it does not earn. The 60-point value is the passing threshold for the **full NCRE exam**, while OfficeEval omits multiple-choice and other components and then macro-averages 200 extracted tasks. It is explicitly only a “reference threshold” for the subset, not a validated subset pass score. The 95.5% comparator is an average over informally collected community solutions, not a sampled, timed, authenticated human baseline. And the evaluated coding agents do not use the same interface or feedback stream as human examinees. OfficeEval therefore supports exam-task artifact proficiency claims for configured code-generation systems—not professional Office-work quality, human parity, general agent capability, or deployment readiness.

## One-sentence contribution

OfficeEval converts externally authored certification tasks into dense deterministic native-artifact measurements, but its transformed test assembly, unavailable instrument, informal community comparator, and unequal human/agent interfaces bound conclusions to selected exam-task rubric performance.

## Research question and contribution

The paper asks how well frontier LLMs and coding agents automate complex Office documents when judged by a standardized human practical exam rather than synthetic tasks or subjective judges (pp. 1–3). It contributes:

1. 200 NCRE Level 1/2 practical-operation tasks across Word, Excel, and PowerPoint;
2. 7,118 weighted XML-configured checks, 20–70 per task, scored against native Office Open XML artifacts;
3. seven single-turn multimodal code-generation configurations and two stronger coding-agent configurations;
4. three-run single-turn results, per-application/level/skill analyses, an English translation study, and a diagnostic failure taxonomy;
5. a useful distinction between executable code and correct Office semantics.

The methodological advance is not merely “real tasks.” It is **external requirement and weight lineage**: exam authorities and preparation materials define the operations and point allocations before model evaluation. This reduces benchmark-author criterion tailoring. It does not automatically validate the authors' new sampling, aggregation, system interface, or interpretation.

## Methodology and system

### Exam source, selection, and transformation

NCRE is a nationally administered credentialing system; the paper reports more than 110 million candidates historically (p. 1). Level 1 includes foundational formatting, formulas, and presentation operations; Level 2 includes mail merge, pivot tables, chart customization, and complex animation (p. 3). OfficeEval extracts only Word, Excel, and PowerPoint practical components, which account for 60% of Level 1 and 80% of Level 2. It excludes multiple-choice computer fundamentals and Level-1 OS/internet tasks (p. 3).

The suite contains 88 Level-1 and 112 Level-2 task packages: 66 Word, 65 Excel, and 69 PowerPoint. Each task has an input artifact and supporting files, 5–15 instruction groups (often with reference images), and an XML scoring configuration (pp. 3–5). The appendix reproduces one complete example per application. Those examples demonstrate real artifact specificity: the Word item has 71 checks spanning exact fonts, gradients, pagination, formulas, table geometry, borders, and document properties; the Excel item has 20 checks for formulas, conditional formatting, chart properties, sorting/filtering, and sheet identity; the PowerPoint item has 21 checks for themes, layouts, SmartArt, animation, transitions, tables, and notes (pp. 16–18).

The paper does not explain the sampling frame within available NCRE materials: source years, exam forms, publishers, duplicate forms, inclusion/exclusion counts, selection seed, task overlap, exposure, or whether task availability, scorer compatibility, community-solution availability, or model outcomes affected admission. “200 NCRE tasks” is externally grounded content, but not a probability sample of NCRE, Office work, or professional workflows.

English variants translate all instructions, document content, criteria, and font/style mappings (p. 3). This is a substantive instrument transformation, not language substitution alone: named fonts and Office constants can change task affordances. The paper acknowledges this and does not treat English results as a native English certification (p. 13).

### Artifact and grader contract

The evaluator parses ISO/IEC 29500 Office Open XML through Open XML SDK 2.5 and invokes Office COM for some render/format checks. It requires a compatible x86 .NET/Windows/Microsoft Office/font/locale environment (pp. 4, 20–21). Each XML criterion identifies a type, target, expected value, operator, and point allocation. A command-line evaluator returns total score and criterion-level pass/fail JSON. Per-task points sum to 100, enabling partial credit (pp. 4–5).

This is stronger than file-existence or keyword grading: the criterion examples inspect authoritative native state such as formulas, sheet names, page setup, chart properties, SmartArt, transitions, and metadata. But “deterministic” is conditional. The authors state repeatability only for a fixed compatible Windows, Office, font, and locale environment (p. 4), yet do not report the Windows build, Office build/channel, fonts, locale, COM configuration, evaluator binary hash, XML hashes, or scoring-script version. Some visual claims are reduced to named internal properties; no rendered-image comparison, human visual-quality audit, or alternative-rendering invariance study is described.

The 7,118 criteria are not 7,118 independent signals, despite the paper's wording on p. 5. Criteria share tasks, objects, operations, generators, and cascading prerequisites. For example, failure to create a slide or table can induce many correlated failures. Criterion counts also differ sharply by category—Text & Format is 38.6%, Data & Formulas only 2.4%—and by task. Task-macro SR protects tasks from criterion-count weighting, while skill-level criterion pass rates answer a different, micro-weighted question. Neither weighting is shown to match NCRE candidate decisions, workplace frequency, consequence, or stakeholder utility.

### Configured-system treatments

The single-turn condition receives preprocessed instructions, up-to-1000px screenshots, input paths, and a library-specific prompt requiring `python-docx`, `openpyxl`, or `python-pptx`. It emits code once with no execution feedback or tools (pp. 6, 20). This is a fixed **library-constrained code-generation** test, not the human exam interface.

Claude Code/Claude Opus 4.7 and Codex/GPT-5.5 instead receive the raw RTF exam and files in an isolated temporary directory. They can inspect, write, execute, and debug with unrestricted tool access, use COM as well as Python libraries, have no turn cap, and receive one hour per task (pp. 6, 8, 20). Their environments exclude scoring rubrics, but “unrestricted” access and isolation are asserted rather than specified through network, host-filesystem, process, secret, or Office-state canaries.

The paper correctly warns that this is not a feedback ablation: model endpoint, scaffold, preprocessing, screenshots, libraries, COM availability, repair budget, turn count, and observation policy differ together (pp. 6, 8, 13). It is a comparison of configured packages.

### Metrics, repetition, and comparison

Score Rate (SR) is the unweighted macro-average of 200 task scores; application, level, and skill slices are descriptive (p. 7). Main single-turn results average three temperature-1 runs. Overall run SDs are 0.4–2.1 percentage points; the top-two difference has a paired task test `p=0.82` and bootstrap CI `[-3.5, 4.4]` pp (p. 7). The paper does not explain whether the bootstrap resamples tasks, runs, or both, nor account for task families/forms or repeated outputs nested within tasks. Coding-agent Table 4 does not state replication and appears to report one run per agent/task; the text's “all numbers” three-run statement is scoped to single-turn Table 3.

Exec% is the fraction of tasks whose generated code runs without error. It is useful but incomplete: a running script may omit operations, corrupt state, or produce no valid artifact, and output creation versus scorer validity are not separately reported. The paper's rough conditional-SR calculation `SR / Exec%` assumes crashed tasks receive zero and treats execution as a simple gate rather than a potentially partial artifact state (p. 7).

## Evidence and results

### Performance

The strongest single-turn configurations score 36.6% (Claude Opus 4.7) and 36.2% (GPT-5.5); Exec% is 61.5 and 56.8 respectively. Other configurations range down to 2.8% SR (Table 3, p. 7). The strongest coding agent, Codex/GPT-5.5, scores 68.8% with 99% execution; Claude Code/Claude Opus 4.7 scores 53.0% with 98% execution. Mean turns are 50.0 (range 8–133) and 23.1 (3–90) respectively (Table 4, p. 8).

These results credibly establish that the evaluated configured systems leave many official rubric points unsatisfied and that richer agent packages often score higher. They do not identify iterative feedback as the cause, compare equal budgets, or establish that 68.8 means “passed NCRE.” The paper itself correctly labels the coding-agent contrast as bundled (pp. 8, 13).

PowerPoint is weakest in the single-turn setting and improves most with coding-agent access; the authors plausibly connect this to animations, themes, and constants unavailable or awkward in `python-pptx` but exposed through COM (pp. 7–8). This is evidence of a model–tool–artifact interaction, not a pure model skill hierarchy. Excel's relative strength similarly reflects interface alignment with formulas and tabular primitives.

### Community solutions and the 60-point reference

Informally collected community solutions average 95.5%, with 89/200 perfect scores. The authors manually inspect the lowest-scoring examples and say deductions correspond to genuine omissions or errors (pp. 4, 21). This is a valuable **positive-witness and scorer sanity check**: high-scoring artifacts exist and selected low-score diagnoses look plausible.

It is not a human baseline. The authors report no number of contributors, provenance per solution, timing, exam conditions, selection process, independence, use of answer keys, retries, software versions, or distribution of candidate ability. Collection from study communities likely selects prepared, shared, or corrected artifacts. Manual inspection is restricted to unspecified low-scoring cases, with no blinded sampling, dual review, or false-pass analysis.

The 60 threshold is still weaker. NCRE awards certification at 60/100 on the full exam, whose composition and component weights differ from OfficeEval's macro-average over practical tasks (p. 3). A candidate may trade practical and multiple-choice points; OfficeEval cannot. Calling 60 an “externally defined” subset threshold risks criterion substitution. It is an interpretive reference line, not a validated decision rule.

### Error analysis

For Claude Opus single-turn run 1 and the Codex agent, failed criteria are assigned to execution failure, missing/misunderstood operation, implementation knowledge, cascading failure, or library limitation (pp. 9–10). Single-turn classification uses execution status and generated-code keyword matching; Codex classification relies mainly on scorer errors and final outputs. The paper explicitly calls this diagnostic rather than definitive and warns that it may over-count implementation knowledge and under-count library limitations.

Within this coding scheme, execution accounts for 51.8% of weighted single-turn loss; implementation knowledge is 61.7% of non-crash weighted loss. For Codex, execution is 7.9% of weighted loss and implementation knowledge is 97.4% of non-crash loss. Dominant subtypes include OOXML paths, enumeration constants, color/theme encoding, units, SmartArt, and chart styles (Tables 5–6, pp. 9–10).

This is useful hypothesis generation, but not a validated root-cause distribution. Labels are inferred without a reported codebook, sample audit, independent raters, agreement, adjudication, trace-based earliest-cause analysis, or counterfactual repairs. “Implementation knowledge” can absorb instruction ambiguity, translation mismatch, tool limitation, renderer/environment mismatch, cascade, or grader overspecification. The weighted-loss denominator also differs from task SR and contains dependent failed criteria.

The directly observed regression result is stronger: Codex scores below its single-turn counterpart on 23/200 tasks (11.5%), suggesting repair can damage working artifacts (p. 11). Yet because the systems differ in many dimensions and no intermediate checkpoint scoring is reported, this does not isolate iterative repair as the cause.

### Translation study

Five single-turn models are reevaluated in English; Claude Opus is only two runs. Overall changes range from -1.9 pp to +8.8 pp, while PowerPoint improves 10–17 pp for nearly all models (Table 7, pp. 12–13). This supports language/mapping sensitivity, especially where English-origin Office constants align with translated labels. It does not isolate language comprehension because content, fonts, names, style mappings, and potentially screenshot appearance change together; no item-level paired interval is reported.

## Unique insight

OfficeEval reveals that **external task lineage and external decision validity are separate properties**.

An externally authored exam can reduce benchmark-author tailoring and supply legitimate requirement/weight provenance. But once researchers select components, transform language, change interfaces, repeat tasks, macro-average forms, and import a threshold from the full exam, they create a new instrument. The original certification's validity argument does not automatically transfer. A reusable lineage should therefore be:

`source exam purpose and population → licensed source forms → selection/transformation record → preserved/changed constructs → configured administration → score mapping → separately validated interpretation and decision threshold`.

A second insight is that dense deterministic artifact grading changes diagnosis only if criterion dependence is preserved. A 71-check Word task is not 71 independent capabilities. It is a dependency graph: object creation enables style checks; layout choices affect downstream renders; one formula range can drive charts. Reporting atomic checks without prerequisite/cascade structure can exaggerate evidence density and misclassify one root error as many implementation deficits.

A third insight is that native-property correctness and human affordance are different constructs. Humans choose gallery labels with continuous rendered feedback; code agents manipulate internal constants without equivalent visual confirmation (p. 11). Low performance may therefore indicate a mismatch between task's human affordance and administration interface as much as missing Office semantics. Skill transfer should be tested across matched GUI, API, and procedural-skill conditions rather than treating hidden constants as intrinsic professional knowledge.

## Comparison with adjacent reviewed benchmarks

### OfficeBench and OdysseyBench

[OfficeBench](2026-07-11-officebench-cross-application-office-validity.md) and [OdysseyBench](2026-07-11-odysseybench-longitudinal-office-memory-validity.md) provide cross-store office transitions but often grade file existence, keywords, or selected cells. OfficeEval substantially improves **native artifact-property coverage** and externally authored requirement lineage. Conversely, it omits cross-application communication/calendar state, requirement accumulation, collateral-state checks, and workflow-stage evidence. None supports professional readiness: OfficeEval is stronger on artifact microstate, while OfficeBench/OdysseyBench are broader on state transitions.

### MBABench

[MBABench](2026-07-11-mbabench-spreadsheet-artifact-validity.md) targets larger, editable finance workbooks, formula provenance, formatting, and judgment. OfficeEval has more deterministic and externally weighted checks but mainly exact exam operations; MBABench asks more about maintainability and professional presentation but relies on a fallible reference and incompletely observed LLM judgment. Both under-test rendered quality and counterfactual behavior. OfficeEval's “correct current property” does not establish that a workbook remains valid after authoritative input changes.

### GDPval and Workflow-GYM

[GDPval](2026-07-10-gdpval-occupational-task-validity.md) and [Workflow-GYM](2026-07-11-workflow-gym-professional-state-validity.md) pursue broader occupational/professional coverage and expert judgment or procedures. OfficeEval's national exam provenance is stronger than synthetic “professional” labels, but its construct is narrower: certification-style Office operations under explicit instructions. GDPval's one-shot occupational artifacts and Workflow-GYM's long GUI paths still do not establish population readiness; OfficeEval's externally calibrated content does not repair that inference gap.

## Limitations and validity threats

1. **Unknown task sampling.** No source-form inventory, selection flow, duplicates, years, inclusion criteria, seed, or outcome-independent admission record.
2. **Subset threshold substitution.** The full-exam 60-point certificate threshold is not validated for a 200-task practical-only macro-average.
3. **No formal human baseline.** Community artifacts are informal positive witnesses without authenticated, timed, sampled examinees.
4. **Interface inequivalence.** Humans use GUI galleries and continuous visual feedback; agents use constrained libraries or broad coding tools and COM.
5. **Agent contrast is bundled.** Model, scaffold, prompt, preprocessing, screenshots, feedback, budget, tools, and Office access all change.
6. **Agent replication unclear.** Three runs are documented for single-turn results; coding-agent repetition, seeds, and uncertainty are not reported.
7. **Criterion dependence ignored.** Thousands of checks share tasks, objects, prerequisites, operations, and cascades; they are not independent signals.
8. **Aggregation unvalidated.** Task-macro SR and criterion-micro skill rates answer different questions; neither maps to workplace frequency or consequence.
9. **Exact-property overspecification risk.** Named style/template/internal properties may reject visually or functionally equivalent artifacts unless invariances are declared.
10. **Rendered quality underobserved.** No systematic rendered-view comparison or human visual validation despite multimodal visual requirements.
11. **Counterfactual behavior absent.** Formula/dependency checks do not appear to mutate inputs and test recalculation, editability, or preserved invariants.
12. **Collateral damage undermeasured.** Criteria target requested operations; no general preservation contract for unrelated document state is described.
13. **Environment incompletely pinned.** Windows, Office build, fonts, locale, COM behavior, evaluator binary, task XML, and instrument hashes are unavailable.
14. **Unrestricted agent boundary unclear.** Network, host filesystem, secrets, installed documentation, Office state, and process permissions are not specified or canaried.
15. **Error taxonomy is heuristic.** No independent coding, agreement, adjudication, validated root-cause protocol, or repair intervention.
16. **Translation is multi-component treatment.** Language, document text, fonts, named styles, mappings, and API alignment change together.
17. **Contamination plausible.** Public NCRE preparation materials may occur in training or web-accessible sources; no exposure tracing or private-form design is reported.
18. **Copyright blocks audit and replication.** Tasks, inputs, criteria, evaluator, outputs, and result matrix are unavailable.
19. **Cost absent.** One-hour agent limits and up to 133 turns are reported, but tokens, monetary cost, wall time, retries, and evaluator/human labor are not.
20. **Professional validity unsupported.** Exam operation accuracy does not establish ambiguous requirement handling, organizational context, communication, compliance, maintenance, recipient use, or deployment safety.

## Reproducibility and operational realism

**Inspectability: low to moderate.** The immutable paper is unusually explicit about task counts, criterion taxonomy, prompts, package versions, metric, examples, and aggregate results. Three complete example instructions and criterion summaries make the intended construct concrete.

**Exact reproducibility: low.** Copyright prevents redistribution of the 200 task packages, source documents, XML scoring configurations, evaluator, community solutions, generated outputs, and criterion-level result matrix. The paper gives Python/Open XML SDK versions but not the complete Windows/Office/font/locale environment or immutable harness/model identities. Reproduction requires independently acquiring the same materials and recreating proprietary evaluation behavior.

**Operational realism: bounded.** Native Office files, multimodal references, interdependent operations, partial credit, exact formatting, formulas, charts, animation, and one-hour repair loops expose real artifact engineering challenges. But exam tasks are explicit, individually bounded, and certification-oriented; there is no stakeholder, evolving context, organizational system, collaboration, policy, source conflict, or downstream use. The coding interface also differs sharply from human Office interaction.

## Relevance to skill-bench

OfficeEval is directly relevant as an external-instrument and native-artifact grading case: it tests whether provenance from a pre-existing exam survives task selection, interface changes, translation, aggregation, and score interpretation. Its reusable value is cross-domain—any benchmark adapted from certification, licensing, training, or competition materials needs the same transformation and threshold-transport controls.

## Transfer to skill-bench

### Retain

1. Externally authored requirements and point allocations as provenance-bearing inputs, not merely benchmark-author rubrics.
2. Native artifact parsing with criterion-level structured outputs and partial credit.
3. Positive witness artifacts for solvability and scorer-health checks, explicitly separated from human baselines.
4. Separate execution validity from semantic operation correctness.
5. Skill/category diagnostics, but with dependency and denominator disclosure.
6. Matched repeated runs for stochastic systems and task-level paired analysis.

### Repair

1. **Create a source-instrument transformation record.** Preserve original purpose, target population, full composition, source threshold, selected components/forms, translations, omitted constructs, licensing, exposure, and every changed administration affordance.
2. **Require threshold transport evidence.** Never import a full-exam pass mark into a subset or transformed assembly without a linking study; label it a reference line otherwise.
3. **Represent criteria as a dependency graph.** Mark prerequisites, cascades, shared objects, alternative-valid equivalence classes, gates, and root/surface relations before computing category rates.
4. **Use plural artifact views.** Pair native OOXML checks with pinned renders for appearance and with recalculation/metamorphic checks for editable artifacts; return `insufficient_evidence` when a view cannot support a criterion.
5. **Cross interfaces experimentally.** Hold task/model/budget as fixed as possible while varying GUI, API/library, COM, visual feedback, and procedural skill. Treat each full package as a configured system when crossing is impossible.
6. **Replace community score with typed witness evidence.** Record acquisition, authorship, timing, tool access, selection, corrections, and health; obtain a sampled timed human condition before human-comparison claims.
7. **Preserve invalidity and cost.** Report first-attempt execution, valid artifact production, eventual repair, semantic score conditional/unconditional on validity, regressions, time, turns, tokens, and cost.
8. **Bound public-form use.** Public exam forms and disclosed scoring examples should be calibration/regression items unless exposure controls justify capability use.

These requirements already have homes in the repository's expertise-transfer, task-projection, benchmark-bundle, artifact-view admissibility, configured-system, task-health, metric-monitoring, validity-argument, and contamination records. No new build task is warranted.

## Concrete repository actions

1. In the next benchmark-family consolidation, classify OfficeEval as a **standardized external-instrument/artifact-property case**, not as evidence of professional readiness; preserve the distinction between source-exam validity and transformed-suite validity.
2. Add the source-instrument transformation chain and threshold-transport warning to existing task-projection/validity guidance when those documents are next consolidated, rather than creating an office-specific schema.
3. Reuse OfficeEval's failure pattern in a future cross-domain conformance slice: plant dependent criteria where one missing object creates many surface failures, and require root-cause aggregation not to count them as independent capability deficits.
4. For editable Office-like artifacts, combine exact native-state checks with one rendered-view invariance case, one counterfactual input mutation, and one collateral-state preservation check.

## Claim boundary

OfficeEval v1 provides evidence that selected June 2026 single-turn code-generation configurations and two stronger coding-agent configurations failed many externally weighted native-artifact criteria on 200 selected NCRE practical Office tasks, and that the richer configured packages obtained higher scores while still leaving substantial criterion loss. It does **not** establish that any system passed or failed the full NCRE, that 60 is a valid subset pass threshold, that 95.5% is human performance, that iterative feedback caused the agent gains, or that the systems possess general Office, professional-work, human-level, economic, or deployment-ready capability.
