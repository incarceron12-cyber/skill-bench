# ReasFlow: artifact production is not validated autonomous scientific discovery

- **Paper:** <https://arxiv.org/abs/2607.14178v1>
- **Authors:** Yutong He et al.
- **Date read:** 2026-07-17
- **Source:** complete immutable arXiv v1, submitted 15 July 2026
- **Local PDF:** `data/papers/pdfs/2607.14178v1-reasflow.pdf` (245 pages; SHA-256 `de63f432d09b9e7d130256e0385302a554baeaba20894c525d0d7fdc94d2dd01`)
- **Local text:** `data/papers/text/2607.14178v1-reasflow.txt` (SHA-256 `77f54d2b0322d2467532fca6a49cff480fb131625d69a52a3c4dc2f8fceaea5a`)
- **Archived official surfaces and five generated manuscripts:** `data/sources/releases/2607.14178v1-reasflow/` with retrieval metadata and hashes in `manifest.json`
- **Tags:** scientific-discovery, procedural-knowledge, knowledge-cards, natural-language-proofs, multi-agent-workflow, llm-judge, artifact-validity, release-audit

## One-sentence contribution

ReasFlow presents an ambitious file-producing multi-agent pipeline for literature review, algorithm design, natural-language proof, experiment execution, and paper assembly, but its evidence establishes configured artifact generation and model-judge preference—not correct autonomous discovery, faithful tacit-heuristic transfer, publishable science, or reduced expert burden.

## Bottom line

ReasFlow's strongest contribution is architectural. It gives each stage explicit artifacts, specialist agents, retrieval tools, review/refinement loops, and a shared workspace. Its knowledge cards are unusually procedural: they encode applicability conditions, structural prerequisites, execution steps, dependency checks, and expected result forms rather than merely summarizing facts. Its five case studies also expose the complete unpolished manuscripts, making failure inspection more possible than a results-only report.

The evidence does not validate the paper's strongest claims. Knowledge-card generation and retrieval prompts are optimized until a model-generated proof using cards is judged at least as good as another model-generated proof using source papers. Neither the implicit technique, card, applicability boundary, proof, nor comparator receives independent expert or formal validation. This is **source-conditioned self-distillation**, not demonstrated capture of tacit expert knowledge. The natural-language verifier is another LLM and the paper itself says successful reports can contain errors and require human evaluation (Section 4.3, p. 13). No theorem is formally checked, no expert correctness study is reported, and no proof-error detection benchmark isolates verifier sensitivity or false acceptance.

The five manuscripts prove that the configured system can produce long technical artifacts. They do not prove scientific validity. Three cases use direct human-to-specialist prompting, all permit iterative user feedback, and the paper provides only illustrative interaction figures rather than complete intervention logs. The two MetaAgent cases include human approval/continuation checkpoints. The claim that post-generation edits were merely presentational is unaudited. The released MC-ADSGD manuscript contains three literal placeholder references—“To be completed” and instructions to replace/fill them—an independently inspectable counterexample to submission readiness and to any implication that internal review guarantees citation integrity.

The public-evidence boundary is also material. At audit time, the paper-linked `https://github.com/ReasLab/ReasFlow.git` returned “Repository not found,” and the ReasLab organization API listed four public repositories but no ReasFlow implementation. Official documentation and five hosted PDFs were available, but not the paper-run code, prompts, card database, retrieval records, proof-verifier logs, experiments, baseline outputs, judge responses, costs, or human-edit diffs. Reproduction of the reported results is therefore blocked.

## Why this matters for skill-bench

This review advances charter objectives A, B, C, and E. Applied mathematics is a bounded stress case for a general question: when can source material and human guidance be transformed into reusable procedural expertise, then into actions and consequential artifacts, without losing authority, scope, or validity?

ReasFlow motivates a useful chain:

`source passage/paper or expert intervention → candidate procedural card → applicability and authority review → retrieval opportunity → delivered card → inspected/adopted step → proof/code/experiment transition → independent check → repaired artifact → external acceptance or consequence`

The paper observes only selected parts of this chain. It stores candidate cards, retrieves them, generates artifacts, and applies internal model judges. It does not establish that the cards recover source-author intent, that “implicit” content is expert-endorsed, that retrieval occurs at the decisive step, that the agent actually uses a card correctly, that verification detects consequential faults, or that generated work survives independent professional review.

For `skill-bench`, the key claim boundary is therefore:

1. **candidate procedural representation** — a model expresses a potentially useful heuristic;
2. **source-faithful card** — cited evidence supports the card and its scope;
3. **expert-approved operationalization** — an authorized contributor approves its meaning and use;
4. **delivered guidance** — the card is visible at a relevant decision opportunity;
5. **adopted guidance** — the trajectory/artifact shows the card changed a step;
6. **locally correct consequence** — plural checks support the resulting derivation or action;
7. **transferable skill** — held-out tasks, contexts, and solvers benefit without harmful misuse;
8. **professional utility** — independent users accept the result under measured burden and consequence.

ReasFlow provides evidence mainly for levels 1 and 4, configured examples relevant to level 5, and model-mediated observations relevant to level 6. It does not establish levels 2–3 or 7–8.

## Research question and claim boundary

The paper asks whether a knowledge-augmented multi-agent system can automate reasoning-centric applied-mathematics research by combining specialist agents, procedural knowledge cards, natural-language proof verification, executable experiments, and manuscript assembly (Sections 1–4, pp. 1–18).

### What the evidence supports

- A concrete staged system design with Survey, Algorithm, Prover, Experiment, Introduction, Writing, and Meta agents sharing file and terminal tools (Section 3.1, pp. 7–8).
- A procedural card format containing scope cues, prerequisites, execution logic, dependency checks, and expected outcomes (Figure 4, pp. 10–11).
- Automatic prompt-refinement algorithms for card extraction and retrieval, defined relative to proof outputs from source papers or designated cards (Algorithms 1–2, pp. 8–9).
- Five full unpolished technical manuscripts bundled into immutable arXiv v1 and separately available from the official ReasLab host (Appendix C).
- One configured full-paper comparison where ReasFlow/GPT-5.4 receives 77.9 from three model reviewers versus 57.3 for the strongest reported baseline (Table 1, pp. 22–23).
- Section-level configured comparisons for survey, algorithm execution, proof reports, experiment reports, introductions, and paper assembly (Section 5.3, pp. 23–27; Appendix B).
- A relatively strong writing-only experiment: eleven systems receive the same upstream asset bundle, prompt, and template; programmatic compile/template checks complement model review (Section 5.3.6 and Appendix B.7).

### What the evidence does not support

- Correctness, novelty, or publishability of any generated algorithm, theorem, proof, experimental claim, or paper.
- Faithful capture of tacit expert knowledge or source-author intent in knowledge cards.
- Causal benefit of cards, retrieval, specialist decomposition, verification, or MetaAgent orchestration; there is no component ablation with matched resources and held-out tasks.
- Equivalence to direct expert guidance; the comparator and outcome are model-generated/model-judged.
- Reduced human intervention or expert burden; complete prompts, feedback, edits, time, and review labor are not reported.
- Autonomous end-to-end discovery across all five cases; three use direct specialist interaction and all allow refinement.
- Formal proof assurance; the verifier performs natural-language LLM review, not proof checking.
- Reproducibility of paper results or operational readiness of the public system.
- Generalization beyond selected optimization-related applied-mathematics topics and the configured model/tool stack.

## Methodology and system reconstruction

### Stage and artifact architecture

The MetaAgent begins after user approval of a research plan. It invokes a SurveyAgent to create survey and Related Work artifacts, an AlgorithmAgent to produce pseudocode/code/tests, a ProverAgent to construct theorem reports, an ExperimentAgent to execute numerical work, an IntroductionAgent to summarize prior artifacts, and a WritingAgent to assemble a paper (Section 3.1, pp. 7–8). Each specialist can read/write files and run commands; sub-agents have isolated context.

This decomposition is valuable because it externalizes handoffs. But it does not by itself establish semantic edge validity. A polished theorem can rest on a wrong algorithm; an experiment can test an implementation that diverges from pseudocode; a writer can faithfully reproduce a false upstream claim. The paper has many local review loops but no released cross-artifact identity ledger binding claim, equation, code path, run, figure, and manuscript statement.

### Knowledge cards and prompt optimization

Cards encode targeted patterns rather than broad summaries. The variance-reduction example names the problem pattern, assumptions, execution steps, dependency checks, and expected `σ²/N` form (Figure 4). This is directly relevant to procedural benchmark design.

The validation mechanism is weaker than the representation. For card generation, the system first creates a baseline proof from reference papers; it repeatedly extracts cards, generates a proof with those cards, and updates the extraction prompt until comparator `Ω` says the card-based proof is at least as good (Algorithm 1). Retrieval prompt refinement similarly uses a designated “ground-truth” card set and its generated proof as targets (Algorithm 2).

This creates a closed epistemic loop:

`papers → model-extracted cards → model-generated proof → model comparison against model-generated reference-conditioned proof → prompt update`

A paper is a source, not an oracle for the implicit heuristic; a generated reference-conditioned proof is not ground truth; and model preference is not proof correctness. Optimizing against this loop can improve stylistic resemblance, expected technique mention, or judge approval while preserving a shared mathematical error. No card-level source spans, extraction confidence, contradictory sources, expert approval, scope tests, or held-out misuse cases are reported.

### Natural-language proof generation and verification

The ProverAgent downloads references, optionally generates custom cards, constructs a proof plan, proves one statement at a time, and invokes a LemmaVerifierAgent. The verifier sees context, prior lemmas, and references; checks soundness, missing justification, notation, assumptions, and tightness; and returns every detected issue for revision under a claimed zero-tolerance policy (Section 4.3, pp. 13–15).

This is sensible workflow engineering, but “zero tolerance” describes the decision rule conditional on detected faults. It says nothing about sensitivity. A checker can fail every issue it sees while missing important issues. The study reports no planted-error suite, expert-labeled proof steps, false-accept/false-reject matrix, repeated verifier reliability, evidence citations, or comparison against formal checking. The authors appropriately concede that generated reports may contain errors and require human evaluation (p. 13), then later over-promote model-review scores into rigorous-theory claims.

### Algorithm and experiment loops

The AlgorithmAgent implements designs, runs simple tests, plots training dynamics, and checks JSON/visual output against expected behavior. The ExperimentAgent chooses datasets, baselines, and hyperparameters from retrieved conventions; executes scripts and tuning; then applies a plot-analysis loop (Sections 4.2 and 4.4).

“Meets expected criteria” risks confirmation bias when the same pipeline authors the claim, experiment, stopping criterion, and interpretation. The paper does not release run manifests or distinguish prespecified tests from post-result adaptation. Its experiment evaluation asks model judges whether artifacts appear sound and flags “hallucination suspicion” when result files are missing or trivial (Section 5.3.4). File existence and plausible plots are useful admissibility checks, not evidence that code implements the intended method, comparisons are fair, statistics are valid, or claims follow.

### Human role in the five cases

Cases 1–3 receive a concise research idea and key references through direct interaction with specialists. Figure 12 explicitly says each specialist is not limited to one trial and refinements are allowed based on user feedback. Cases 4–5 route through MetaAgent, with plan and continuation checkpoints where comments may be supplied (Figure 13). The paper reports that later changes were only minor presentation edits, but supplies no complete dialogue, intervention count, before/after diff, decision provenance, contributor identity by case, or independent classification of technical versus presentational changes.

The five cases therefore demonstrate two configured co-production modes, not five clean autonomous runs. They are also not independent samples from a defined research-problem population: topics, seed ideas, references, participating experts, and inclusion criteria are selected by the authors, and multiple cases involve overlapping authors and optimization themes.

### Evaluation design

The full-paper comparison uses one target idea/reference bundle, one autonomous trial per system, heterogeneous interfaces and model backbones, and three LLM reviewers applying a nine-dimension rubric (Section 5.2). ReasFlow scores highest, but there is no human panel, rater calibration against correctness, repeated generation, confidence interval, blinded identity statement, cost/resource parity, or released output set.

Section-level studies vary substantially:

- Survey evaluation uses three tasks, four backbones, and three model judges; the paper reports wins in 28/36 cells, but the “verified” 339-paper library and judgment records are unreleased.
- Algorithm evaluation uses 35 MLR/OR tasks and a one-hour budget. Table 3 reports 100% and 94% for ReasFlow configurations, while the surrounding prose says 98% and gives baseline ranges inconsistent with the table, indicating reporting drift.
- Proof evaluation uses one target algorithm and model-only reviewers. ReasFlow/GPT-5.4 averages 90.7, but one reviewer gives all three ReasFlow backbones 100 while scoring many strong baselines much lower (Table 4), a warning about judge/configuration interaction rather than independent correctness.
- Experiment evaluation averages only successfully completed tasks (`n`) and scores model-authored outputs with two model judges. Success conditioning can make quality comparisons non-equivalent when failure rates differ.
- Introduction evaluation has five repetitions and three judges but compares a structured iterative agent against one-shot GPT-4o; it identifies package uplift, not the contribution of extraction, evaluation, refinement, or model capability separately.
- Writing evaluation is the cleanest package comparison because inputs and template are byte-identical and compile/template facts are programmatic. It still measures assembly of supplied assets, not discovery or truth of those assets.

### Generated-manuscript audit

All five official hosted PDFs were fetched and converted to text. They range from 25 to 50 pages and contain theorem/proof and experiment sections. This is real artifact evidence.

The audit also found a decisive failure in `MC-ADSGD.txt`: references [1], [3], and [16] include literal “To be completed” and “Placeholder” instructions. The PDF visibly presents those placeholders in its references. This is not a subtle theorem dispute; it is an unambiguous submittability and citation-integrity defect that the described survey, writing, completeness, reference-verification, and visual-review loops should detect. Its survival shows why internal checks must be empirically calibrated at predicate level rather than described by intent.

The other manuscripts were inspected for structure and experiment/proof content, not independently re-proved or rerun. Their existence and later arXiv counterparts (`2604.24012`, `2604.25467`, `2604.23980`, `2606.07496`, `2604.23754`) are provenance signals, not peer-review outcomes or proof of technical correctness. The ReasFlow paper itself labels the bundled versions “unpolished” and says later arXiv versions received human-expert polishing (Appendix C, p. 71 onward).

## Unique insight and evidence interpretation

The paper's unique design insight is that procedural scientific knowledge should be represented as **conditional operations**, not free-floating advice. “Use independence” is inadequate; a useful record says which random objects must be independent, what cross terms vanish, where the averaging factor enters, what must not be bounded prematurely, and what result shape should follow. That representation transfers directly to hidden requirements, decision thresholds, failure signatures, and rubric checks in `skill-bench`.

The unique validity lesson is the opposite of the paper's promotion: **procedural compression creates an epistemic fork**. A card may be:

- explicitly supported by a source;
- a plausible interpretation of implicit source reasoning;
- an expert-provided heuristic;
- a model-generated synthesis across sources;
- or a benchmark-optimized instruction selected because another model prefers its downstream output.

These states cannot share one “knowledge” label. ReasFlow's cards are primarily model-inferred and judge-selected. Calling their content “tacit knowledge” or “direct expert guidance” erases authorship and authority. A card can be useful while its provenance claim remains weak.

The artifact audit adds a second insight: a long, technically fluent manuscript can fail a cheap deterministic predicate that a broad LLM rubric overlooks. Scientific-work evaluation should therefore be conjunctive at critical boundaries: valid references, executable code/run provenance, assumption/theorem consistency, source-supported claims, and required artifact integrity should gate any holistic quality score. A 77.9 reviewer score cannot compensate for an unresolved placeholder, just as fluent proof prose cannot compensate for one invalid inequality.

## Comparison with related reviewed systems

- **AARRI** separates research judgment, action, abstention, escalation, and artifact consequence. ReasFlow treats forward progress toward a paper as the default; it does not evaluate whether stopping, narrowing a claim, or escalating to an expert was the correct research action.
- **SciAgentArena** measures executable scientific stages and dependency-aware pipelines under bounded tasks. ReasFlow exposes richer applied-math artifacts but has weaker released execution evidence and no step-wise versus full-pipeline causal contrast.
- **AstaBench** treats heterogeneous scientific assistance as a portfolio rather than one latent scale. ReasFlow's mixed section metrics and one full-paper score should likewise remain configured endpoints, not a general scientific-discovery ability.
- **PaperBench/paper-replication** separates dense partial progress from successful replication and binds rubrics to artifact evidence. ReasFlow's long manuscripts need the same noncompensatory completion gates and run lineage.
- **AFTER/ACE** separates candidate procedural memory, transfer edges, update semantics, and solver/context effects. ReasFlow does not test cards on held-out source families, tasks, solvers, or contexts and does not report harmful retrieval.
- **ResearchRubrics and LLM-generated-rubric meta-evaluation** distinguish useful generated criteria from criterion authority. ReasFlow's reviewer ensemble reduces single-model dependence but does not confer expert or mathematical authority.
- **HANSEL/Pista/HiLSVA oversight reviews** separate inspectability and opportunity to intervene from exercised, effective, burden-aware oversight. ReasFlow says files are inspectable but does not measure what humans inspect, correct, accept, or miss.

## Limitations and validity threats

1. Five purposively chosen, related case studies do not define an inference population.
2. Three cases use direct specialist interaction; all allow refinement; two include MetaAgent checkpoints.
3. Human inputs, feedback, intervention timing, edits, and burden are not released or quantified.
4. “Minor presentational refinements” is author-asserted without blinded diff classification.
5. Card content is model-inferred from papers rather than elicited from or approved by source experts.
6. Card generation is optimized against model-generated proof comparators.
7. Retrieval refinement assumes a “ground-truth” card set without reporting its authority or annotation process.
8. The proof comparator `Ω`, prompt versions, training tasks, iterations, and failures are unreleased.
9. There is no card-level source-span provenance, contradiction record, confidence, scope approval, or expiry.
10. Retrieval, visibility, reading, adoption, and downstream effect are not separately logged in reported results.
11. No held-out transfer or negative-transfer experiment validates reusable procedural skill.
12. Natural-language verification has no formal soundness guarantee.
13. The verifier has no expert-labeled fault-detection calibration or false-accept estimate.
14. “Zero tolerance” is a threshold policy, not evidence of detection sensitivity.
15. Algorithm, experiment, verification, and interpretation can share expectations and confirmation bias.
16. Experiment artifacts are judged for plausibility, not independently rerun or implementation-matched.
17. Successfully completed experiment tasks form a post-outcome quality denominator.
18. Full-paper evaluation uses one target and one generation trial per system.
19. Baselines differ in model, interface, orchestration, and likely resources; treatment effects are not component effects.
20. Model reviewers are not calibrated against expert scientific correctness or acceptance decisions.
21. Reviewer calls, seeds, raw responses, disagreement, and uncertainty are not released.
22. Aggregate dimensions are compensatory and can hide critical scientific defects.
23. Proof evaluation uses one target theory and shows strong judge/configuration interaction.
24. Reported algorithm success prose and Table 3 are internally inconsistent.
25. No cost, tokens, wall-clock total, compute, API budget, or human-time ledger supports scalability claims.
26. The five standalone manuscripts have no accompanying immutable source/code/run bundle in the audited release.
27. MC-ADSGD retains three explicit placeholder references despite claimed review machinery.
28. Later arXiv posting is not peer review, independent correctness evidence, or publication acceptance.
29. The paper-linked GitHub repository was unavailable at audit time.
30. Official product documentation describes intended outputs, not paper-run reproducibility.
31. The hosted platform returned HTTP 403 to the automated access attempted; no operational conformance run was possible.
32. The public ReasLab organization contained no source repository for the reported system.
33. The built-in paper/card databases, exact snapshots, embeddings, and retrieval indices are unavailable.
34. No complete paper-run workspace, code, prompts, traces, verifier logs, or judge outputs are released.
35. Applied-mathematics optimization concentration blocks broad disciplinary transport claims.
36. Author overlap among system paper and case papers complicates independence of case selection, polishing, and assessment.

## Reproducibility and operational realism

Reproducibility is **strong for reading immutable v1 and inspecting the five generated PDFs, weak for reproducing any experiment, and blocked for the system itself**. The 245-page arXiv artifact includes the full main paper, extensive evaluation prompts/tables, and all five generated manuscripts. Official ReasLab pages describe a plan-driven workflow and claim LaTeX, BibTeX, code, tests, proof, experiment, and final-paper outputs. The five separate PDFs were reachable and hash-preserved.

The implementation boundary fails. On 2026-07-17, the exact linked GitHub clone returned “Repository not found.” The GitHub organization API exposed only `LeanSearch`, `lean4-infoview`, `reaslab-ide-issues`, and `async-lsp`; neither ReasFlow nor the alternate queried agent repository was public. Product documentation cannot substitute for the missing implementation or paper-run evidence. The five hosted files are mutable web resources, so the local hashes and retrieval timestamp are essential.

Operational realism is mixed. File-based handoffs, compilation, executable scripts, dataset download, tuning, multiple specialist contexts, and a long artifact horizon resemble real research work. But the evaluation omits the most consequential operational states: failed runs, environment identity, compute and API budgets, source/version locks, model alias drift, experiment preregistration, complete intervention histories, expert review time, reviewer disagreement, submission outcomes, and maintenance. The observed system is best described as a **research-artifact co-production package under selected author supervision**, not a validated autonomous scientist.

## Transferable design implications for skill-bench

### Retain

1. **Procedural-card structure.** Encode problem pattern, prerequisites, execution steps, dependency checks, forbidden shortcuts, expected outcome form, and source locators.
2. **Typed stage artifacts.** Preserve survey, method, proof, code, run, figure, introduction, and final assembly as separate linked artifacts.
3. **Local refinement loops.** Return detected issues to the producing stage rather than asking a final writer to conceal upstream gaps.
4. **One-statement proof units.** Small proof obligations reduce hidden propagation and improve attribution.
5. **Shared-input writing controls.** Byte-identical asset bundles and templates support a bounded assembly-package comparison.
6. **Plural evidence views.** Combine deterministic compilation/reference checks, artifact inspection, model observations, and domain review.

### Repair

1. **Type card authorship and authority.** Distinguish `source_explicit`, `model_inferred`, `expert_supplied`, `expert_approved`, and `benchmark_optimized`.
2. **Bind cards to evidence.** Require source spans, version hashes, transformation rationale, scope, contradictions, approver, and unresolved uncertainty.
3. **Instrument delivery and adoption.** Record retrieval opportunity, query, candidates, ranking, displayed content, read/use evidence, affected step, and counterfactual baseline.
4. **Calibrate every checker.** Maintain planted and natural fault suites with false-accept, false-reject, invalid, and abstention states.
5. **Gate critical predicates.** Unresolved references, missing run provenance, failed assumption checks, or unverified theorem dependencies cannot be averaged away.
6. **Preserve intervention lineage.** Store every human prompt/comment/edit and classify proposed versus accepted technical and presentational changes with reviewer disagreement.
7. **Separate package and component claims.** A multi-agent win supports the configured package only until matched ablations isolate cards, retrieval, verification, orchestration, or model effects.
8. **Report complete denominators and resources.** Include attempted, completed, invalid, selected, polished, judged, and accepted artifacts plus tokens, compute, time, and human burden.

### Test

1. **Card fidelity:** independent experts trace candidate cards to source evidence, classify inferred additions, and test applicability boundaries.
2. **Negative transfer:** inject plausible cards with violated prerequisites and measure misuse, abstention, detection, and downstream harm.
3. **Adoption causality:** compare no-card, full-source, correct-card, irrelevant-card, and corrupted-card conditions under matched model/tool budgets.
4. **Verifier calibration:** plant cyclic dependencies, missing assumptions, invalid inequalities, loose-but-valid bounds, notation collisions, and unsupported citations; require evidence-backed verdicts.
5. **Cross-artifact consistency:** bind algorithm equations to implementation lines, run manifests, figures, reported numbers, and manuscript claims.
6. **Human-oversight study:** measure inspection opportunities, exercised review, correct detections, missed faults, accepted repairs, time, and final independent quality.
7. **Transfer edges:** hold out paper families, research questions, domains, and solver models; freeze cards before testing.
8. **External acceptance:** use blinded domain reviewers and submission-like criteria, while keeping acceptance, novelty, theorem correctness, and utility as separate outcomes.

## Action items for repository

- [x] Read and hash the complete immutable arXiv v1 PDF/text.
- [x] Archive and inspect all five official unpolished manuscripts plus official documentation surfaces.
- [x] Recheck the exact paper-linked GitHub repository and timestamp the bounded public-organization absence.
- [x] Reconstruct the stage architecture, human interaction modes, card-refinement loop, proof verification, and model-judge evaluations.
- [x] Record the MC-ADSGD placeholder-reference failure as direct artifact evidence.
- [x] Separate candidate procedural representation, fidelity, authority, delivery, adoption, local consequence, transfer, and professional utility.
- [x] Add no new queue task: the evidence sharpens existing expertise-transfer, intervention, evidence-lineage, grader-calibration, artifact-admissibility, execution-validity, and cross-artifact consistency machinery rather than justifying a ReasFlow-specific subsystem.
