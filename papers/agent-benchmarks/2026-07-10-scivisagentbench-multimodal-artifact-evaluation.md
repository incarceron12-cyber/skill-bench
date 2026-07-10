# Paper Review: SciVisAgentBench — Multimodal Artifact Evaluation and Expert Validation

- **Paper:** https://arxiv.org/abs/2603.29139v2
- **Authors:** Kuangshi Ai et al.
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint (IEEE TVCG manuscript format)
- **Version read:** immutable v2, 26 June 2026
- **Local PDF:** `data/papers/pdfs/2603.29139v2-scivisagentbench-a-benchmark-for-evaluating-scient.pdf` (16 pages; SHA-256 `242bf444a54221bc87133b3a9369143339a3380ef38e257090b91ede02f4efc2`)
- **Local text:** `data/papers/text/2603.29139v2-scivisagentbench-a-benchmark-for-evaluating-scient.txt` (SHA-256 `a5d6ffd485d5436d764ecf145318bbb5b58d9590c61071a0e8fa05c7ec20cfae`)
- **Official code inspected:** https://github.com/KuangshiAi/SciVisAgentBench/tree/b9435d13e9ff979226b1754e6c467efeb026978a (158 tracked files; fetched commit dated 4 June 2026, before v2 but not proven to be the paper-time implementation)
- **Official dataset metadata inspected:** https://huggingface.co/datasets/SciVisAgentBench/SciVisAgentBench-tasks/tree/d2975dd424f619d706e8ae86dd47d1843e0f52c7 (730-path manifest; large blobs not downloaded)
- **Release provenance:** `data/sources/releases/2603.29139v2-scivisagentbench/provenance.json`
- **Tags:** scientific-visualization, multimodal-artifacts, expert-judgment, llm-judge, deterministic-graders, configured-systems, validity

## One-sentence contribution

SciVisAgentBench contributes 108 expert-authored scientific-visualization cases, a four-dimensional coverage taxonomy, heterogeneous executable and multimodal graders, three-run configured-system baselines, and a 12-expert judge-alignment study; its strongest transferable idea is to make the artifact’s **representation and evaluator admissibility conditions** explicit, while its broad task-validity, scalable-judge, diagnostic, and professional-work claims outrun a selected single-reference task set, a sparse post-hoc-filtered human study, incompletely specified aggregation, and a release that does not preserve the reported human labels or experimental records.

## Why this matters for skill-bench

This is one of the clearest primary examples of why “artifact quality” is not one measurement channel. A scientific result may be observed as a rendered image, executable script, saved application state, coordinate set, segmentation, persistence diagram, text answer, or resource trace. SciVisAgentBench responds with MLLM rubric judgments, PSNR/SSIM/LPIPS, execution checks, exact-answer rules, and topology-specific distances and matchings (Sections 5.2–5.5, pp. 5–6). That pluralism directly advances charter objectives B and C.

The important boundary is equally clear: those graders are not interchangeable witnesses. Pixel similarity is admissible only under controlled camera, lighting, and background; a script is useful only after execution; a screenshot cannot establish hidden application state; and a topology distance does not judge visual communication. The paper recognizes many of these restrictions but aggregates their outputs into leaderboard scores without publishing a complete measurement model. For `skill-bench`, the lesson is not “add a vision judge.” It is: **bind each criterion to the artifact representation, transformation, evidence view, invariances, and failure states that make its grader meaningful.**

The paper also tests a core project tension. It obtains reproducibility by constraining every included visualization to one explicit outcome and excluding multiple valid outputs (Section 5.1, pp. 4–5). This improves grading but removes the open-ended design choice and exploratory sensemaking that motivate consequential visualization work. It is therefore evidence about a tractable artifact-evaluation slice, not evidence that a single-reference instrument captures professional scientific analysis.

## Research question and claim boundary

The paper asks:

1. Can a taxonomy support broad, extensible coverage of scientific-visualization agent tasks?
2. Can outcome-centric evaluation compare code-generating, tool-using, GUI-like, multimodal, and multi-agent systems despite different trajectories?
3. Can deterministic artifact checks and MLLM rubric judgments produce reliable scores?
4. How closely do three MLLM judges align with a sample of SciVis experts, and how stable are they under prompt/presentation changes?
5. What capability, reliability, and efficiency patterns appear across specialized agents and general coding agents?

The evidence supports narrower conclusions: the authors assembled an inspectable 108-case instrument spanning four tool suites plus object identification; configured systems exhibit large performance and token-use differences over three trials; some artifact predicates admit useful deterministic checks; and on one selected set of Claude-Sonnet-4.5 outputs, pooled MLLM ratings correlate positively with a filtered human reference.

It does **not** establish representative coverage of scientific visualization, the “if and only if” task-validity condition asserted in Section 6.1, equivalence of human and model judgment, validity on open-ended or multiple-solution artifacts, causal superiority of coding-agent architecture, professional usefulness to scientists, stable leaderboard comparison across incompatible tool suites, or a diagnostic account of workflow failures. The current benchmark explicitly leaves process evaluation to future work (Section 5.1, p. 5).

## Methodology

### Taxonomy and case authoring

The taxonomy crosses application domain, data type, complexity, and 15 visualization operations. Eight domain labels, five data-type labels, and task/workflow complexity labels are listed in Appendix A (pp. 12–13). Cases were iteratively collected, reviewed, and annotated with visualization researchers and domain experts; candidates were selected for workflow relevance, clear objectives, human feasibility, and taxonomy alignment (Sections 4 and 5.2, pp. 3–5).

The released YAMLs account for the reported 108 cases: 48 ParaView, 27 object-identification, 11 bioimage, 13 molecular, and 9 topology cases. This is an expert-driven convenience corpus, not a sampling frame. The paper does not report contributor counts by suite, expert qualifications, independent author/reviewer assignments, rejection counts, disagreements, authoring time, or a novice/expert contrast. Taxonomy frequency is partly determined by available collaborators, data, and toolchains; labeling a case with an operation establishes intended coverage, not that success specifically measures that operation.

All included cases are narrowed to one explicit visualization result. Experts specify methods, cameras, colormaps, and sometimes lighting; visualization researchers execute and review tasks for branching outcomes, refining or excluding those with materially different valid solutions (Section 5.1, pp. 4–5). This is a defensible reliability intervention, but it changes the construct from choosing an effective analysis/design to reproducing a constrained reference. The benchmark’s “workflow” label describes a sequence of operations, not necessarily an open-ended professional workflow.

### Artifacts and heterogeneous evaluation

Each task has a natural-language instruction, input dataset, mandatory reference artifact, and expert-authored criteria. Depending on the tool, references may include images, scripts, software state, coordinates, segmentations, or text. The MLLM receives task information, a reference visualization, an agent visualization, rubrics, and a 0–10 scale. The paper says rubric order is shuffled to reduce order bias (Section 5.3, p. 5).

Deterministic channels include:

- PSNR, SSIM, and LPIPS over front, side, and diagonal views when rendering is controlled;
- generated-file presence and code execution;
- exact rules for explicit-answer tasks;
- case-specific software-state checks;
- optimal matching for critical points;
- Wasserstein and partial fused Gromov-Wasserstein distances for topology;
- Hungarian matching and Dice scores for segmentations (Section 5.4, pp. 5–6).

The paper rejects CodeBERT script similarity after observing similar values for functionally correct and incorrect programs—a useful example of retiring a convenient but construct-invalid metric (p. 5). However, it does not report the sample, effect, threshold, or decision rule behind that retirement.

Image metrics are averaged only over completed cases and then multiplied by completion rate; LPIPS is transformed analogously (Section 5.4, p. 5). This is transparent but not a neutral missing-data correction: it imposes a particular utility function equating incomplete coverage with degraded visual fidelity. The release computes this formula, but neither paper nor code supplies uncertainty or validates that the scaled metric preserves decisions.

The inspected code reveals additional score semantics absent from the paper’s main methods. A vision task can sum 10 points per rubric goal, 5 for output generation, and 10 for thresholded token/time efficiency (`evaluation_manager.py`; `sciviz_evaluator.py`). Consequently, efficiency’s implicit weight changes with the number of rubric goals. Multiple rubrics are simply summed; dependencies and gate failures are not represented. The code’s output-generation check initially assumes success and is revised by downstream evaluator failures. This is an implementation observation from the 4 June commit, not proof of the exact v2 scoring run.

### Configured-system baselines

The study evaluates ChatVis and ParaView-MCP for ParaView, GMX-VMD-MCP for molecular work, BioImage-Agent for bioimages, TopoPilot for topology, and ParaView-MCP for object identification. General-purpose Claude Code and Codex receive preinstalled visualization engines but no API references, skills, or online documentation access (Section 7.1, pp. 7–8). No specialized agent spans all suites, so comparisons are suite-local; the general coding agents provide the only broad reference.

Each setting is run three times. Table 4 reports mean and standard deviation for overall score and completion, plus `pass@k` (at least one valid output) and `pass^k` (valid output in all k trials), pp. 8–9. These “pass” measures are output-validity/completion measures, not success on the intended scientific criterion. Calling them pass metrics risks conflating artifact production with correctness.

The results show coding agents leading many suites but at much higher token use, while BioImage-Agent is stronger in its supported suite (Tables 4–6, pp. 8–9). Because agent architecture, tool interface, model, prompt, environment, available documentation, and suite all vary, these are configured-system descriptions—not causal architecture effects. Three repetitions give a rough stability view but no task-clustered intervals, paired tests, order/seed records, or provider-drift controls.

Appendix E reports a small skill follow-up on the 11-case bioimage suite. A napari skill distilled from the MCP agent improves Claude Code’s mean score and often reduces tokens (p. 16). The authors state the skill was developed without benchmark-task exposure. Still, this is a nonrandomized, same-environment package comparison with three repetitions, different task/evaluator model combinations, and no independent-rubric arm; it supports package efficacy on this suite, not transferable domain expertise.

### Human–MLLM alignment and robustness

The authors select 24 cases stratified over taxonomy dimensions; 21 vision-scored cases enter the alignment study, while three topology cases are excluded. All evaluated artifacts come from one generator configuration, Claude-Sonnet-4.5. Twelve SciVis experts see the same task description, reference image, candidate image, rubrics, and scale as the model judge. The study has IRB approval and informed consent (Section 6.2, p. 7).

The reporting unit is unclear. The text says 12 experts yield 65 ratings across 21 cases, while Table 1 defines each `n` as a “full evaluation of all cases” and reports human `n=12`. Twelve complete 21-case evaluations would imply at least 252 case-level judgments before multiple rubric criteria, not 65. The paper does not provide assignment design, missingness, rater-by-case matrix, raw labels, or analysis code.

Human reliability is Krippendorff’s α=0.669 and ICC(2,1)=0.673. A leave-one-out procedure identifies two deviating experts; both are removed, raising α to 0.719 and ICC to 0.723, and the filtered ten-expert mean becomes the human reference. No preregistered exclusion criterion, expertise/context analysis, sensitivity table, or adjudication is provided. Disagreement may encode legitimate subdomain judgment, as the authors themselves note, so post-hoc removal can manufacture a more homogeneous construct.

Three MLLMs run five times each. Cross-model reliability is α=0.817 and ICC=0.819. Correlations against filtered human averages range from Pearson 0.764–0.808 and Spearman 0.789–0.830; MAE is 1.469–1.691 on the 0–10 scale (Tables 1–2, p. 7). There are no intervals, clustered analyses, held-out model selection, or correction for selecting Claude-Opus-4.6 after comparing the same 21 cases. Correlation does not test calibration or decision agreement and is inflated by between-item difficulty/quality variation. A judge can rank obviously good and bad outputs similarly while disagreeing at consequential thresholds.

Prompt/presentation robustness varies wording, scale description, image order, and reference-image visibility over five repeats. The proposed stability score is one minus the mean score standard deviation divided by the 11-point range; all models exceed 0.92 (Table 3, p. 7). This average scale-normalized variability is easy to make high and does not test correctness, bias, criterion-specific flips, or robustness near release thresholds. Perturbation-level outcomes and prompts are not released in the inspected snapshot.

## Evidence and results interpretation

The benchmark supplies credible descriptive evidence that artifact representation and interface strongly shape observed performance. On ParaView, coding agents complete about 95–98% of runs while the specialized systems complete roughly 44–54%, yet consume orders of magnitude more input tokens (Tables 4 and 6, p. 8). On bioimages, the specialized agent leads the reported Opus-judged scores over both coding agents in some configurations. Topology uses deterministic rather than MLLM grading and produces a different comparison surface. There is no coherent evidence that one system is globally “best”; the suite/tool compatibility matrix precludes that claim.

The human study supports a bounded statement: on a selected 21-case set of one generator’s outputs, the tested MLLMs share substantial rank signal with a post-hoc-filtered expert mean. MAE near 1.5–1.7 points is not negligible on a ten-point criterion, and higher MLLM self-consistency than human consistency can indicate shared model bias rather than superior judgment. The paper’s conclusion that MLLMs “reliably approximate” experts is plausible for explicit visually grounded properties, but unsupported for higher-level scientific interpretation—the exact area the authors report as most disagreement-prone.

The release improves auditability but does not reproduce the paper. The official code snapshot contains 158 files, the 108-case YAML definitions, grader implementation, human-evaluation UI, and a newly added Docker staging path. It contains no reported human ratings, rater assignment, reliability/correlation analysis, perturbation results, baseline result matrix, environment lock beyond a broad container recipe, or tests establishing the paper tables. TopoPilot2 is explicitly not open-sourced. The official dataset revision exposes 730 paths, including 364 ground-truth files under `GS/` and 51 `visualization_goals.txt` rubric files; public exposure enables inspection but creates contamination risk.

The latest release’s staging script strips `GS/`, rubrics, prior results, scoring scripts, filename-pattern leaks, and byte-identical ground-truth duplicates, then audits the staged tree. That is a strong operational pattern. Yet the Docker launcher does not disable network access and forwards provider credentials; paper-time isolation is not established. The sanitization commit predates v2 but postdates the dataset revision and is not tied to the reported trials.

## Unique insight

SciVisAgentBench’s deepest contribution is an implicit **evaluator-admissibility envelope**:

`criterion → required artifact representation → controlled transformations/invariances → evaluator evidence view → valid score`

For example, PSNR is admissible only after standardized rendering from comparable camera views; a topology matcher needs structured point/region outputs; a vision judge needs both reference and candidate renderings but still cannot certify internal state; and execution success says nothing about whether the scientific result is correct. Once this envelope is violated, the correct output is `not_applicable` or `insufficient_evidence`, not zero and not a substitute grader score.

The paper partly follows this logic by restricting image metrics to ParaView and using topology-specific evaluators, but its aggregate score erases the envelope. This matters beyond visualization. A spreadsheet formula checker, rendered-chart judge, workbook-state inspector, source-provenance audit, and stakeholder reviewer similarly observe different predicates. `skill-bench` should not ask all graders to emit fungible points; it should preserve criterion-level observations, admissibility, dependencies, and bounded claims before any aggregation.

A second insight is that **reference narrowing is itself an intervention on the construct**. Constraining camera, color, and method can increase rater reliability while eliminating legitimate expert alternatives. Reliability and realism are not endpoints on one monotonic scale. The benchmark should record which freedoms were intentionally removed, why they were irrelevant to the target capability, and which resulting claims are excluded.

## Transferable design patterns

### 1. Type artifact views and transformations

For each criterion, record authoritative artifact type, observed view, rendering/export pipeline, software/version, camera/background/normalization, permitted invariances, and transformation hash. Never treat a screenshot as equivalent to application state or an executable source file.

### 2. Gate graders by admissibility

Declare when each grader is applicable. Image similarity requires controlled rendering; semantic visual criteria require sufficient resolution and views; state checks require authoritative structured state; scientific-insight criteria require domain evidence. Return explicit `not_applicable`, `invalid_artifact`, and `insufficient_evidence` states.

### 3. Preserve plural measurements before aggregation

Keep execution, artifact presence, visual semantics, structured-state correctness, efficiency, and professional judgment separate. Document dependencies and gates: a visually plausible output should not compensate for loading the wrong dataset, and efficiency should not rescue an invalid result.

### 4. Validate judge decisions, not only correlations

Use held-out artifacts spanning threshold neighborhoods, multiple generator families, planted failures, and legitimate alternatives. Report criterion-level confusion/calibration, clustered intervals, human disagreement, abstentions, and sensitivity to evidence views. Select and test the judge on disjoint cases.

### 5. Preserve expert disagreement and assignment lineage

Record each expert’s scope, case assignment, rating, uncertainty, rationale, and evidence. Analyze outliers but do not silently delete them; distinguish careless ratings from subdomain-specific standards and publish sensitivity with and without exclusions.

### 6. Treat environment/tool identity as part of the configured system

Pin model, harness, visualization engine, API/tool interface, package versions, prompt/skill, network policy, hardware/render backend, evaluator, and run seed. Compare architectures only through matched interventions or bounded suite-local claims.

### 7. Separate public release from evaluation exposure

Keep inspectable public examples and code, but operate fresh/private or semi-private cases with an audited launcher. Test filesystem, network, model-visibility, and reference-leak paths. Public ground truth makes reproducibility possible but weakens future capability evidence.

## Limitations and validity threats

1. **Expert-driven coverage is not representative coverage.** No sampling frame or domain prevalence supports ecological claims.
2. **Authoring provenance is under-specified.** Contributor qualifications, counts, review assignments, disagreements, rejections, and labor are absent.
3. **Taxonomy tags do not establish task validity.** A case-capability mapping is not evidence of the asserted “if and only if” relation.
4. **Single-reference narrowing removes professional choice.** Camera, colormap, and method constraints can turn design work into reference reproduction.
5. **No expert baseline or expert–novice contrast is reported.** Human feasibility is asserted rather than measured with time, errors, or artifact variation.
6. **Tool suites are not comparable populations.** Different agents, environments, tasks, and graders prevent global architecture attribution.
7. **Three runs are too few for reliable tails.** No task-clustered intervals, paired tests, seed/order details, or service-drift analysis are given.
8. **`pass@k` is misnamed.** It measures production of a valid output, not criterion-level task success.
9. **Aggregation is under-specified in the paper.** Goal counts change implicit efficiency weight; dependencies, gates, and missingness are not modeled.
10. **Scaled image metrics encode an unvalidated utility function.** Completion-rate multiplication is not merely normalization.
11. **The MLLM study uses one output generator.** Judge agreement may not transfer to other model families, error distributions, or adversarial artifacts.
12. **The 65-rating accounting is unclear.** It conflicts with the table’s description of 12 complete evaluations and blocks replication.
13. **Human labels are post-hoc filtered.** Two experts are removed without a preregistered rule or preserved substantive disagreement analysis.
14. **Correlation is not calibration.** Pooled item variation, sparse assignments, and absent intervals make the headline coefficients easy to overinterpret.
15. **Judge selection is not held out.** Claude-Opus-4.6 is chosen using the same cases used to report alignment.
16. **Robustness measures stability, not validity.** A consistently biased judge scores highly; perturbation-level results are absent.
17. **Criterion dependence is ignored.** “Overall match,” structure, coverage, and color rubrics overlap and are summed as if independent.
18. **Process diagnosis is not implemented.** Traces are reportedly recorded, but baseline conclusions rely on outcomes and anecdotal symptoms.
19. **Release evidence is incomplete.** Human labels, study analysis, perturbation data, exact result records, and one topology agent are unavailable.
20. **Public ground truth creates contamination risk.** Tasks, rubrics, scripts, states, and images are openly downloadable at a mutable repository.
21. **Isolation evidence is post hoc.** The strong sanitizer exists in the inspected commit, but network remains available and paper-run canaries are not preserved.
22. **Operational cost is incomplete.** Token counts are reported, but dollars, wall time distributions, evaluator cost, expert hours, and maintenance burden are not.
23. **Skill ablation is exploratory.** One 11-case suite, three runs, no independent rubric, and no task-clustered inference cannot establish general skill transfer.
24. **Professional consequence is unmeasured.** No scientist uses the outputs for a decision, and no downstream insight or error cost is observed.

## Reproducibility and operational realism

Reproducibility is moderate for inspecting task and grader structure and weak for reproducing the reported study. The immutable 16-page PDF/text, complete official 158-file code archive, all case YAMLs, evaluator implementations, human UI, Docker recipe, sanitizer, and official dataset revision are identified and locally provenance-recorded. The code compiles under the local Python parser. The dataset path manifest verifies the public artifact layout, but the large scientific datasets and images were not downloaded or executed in this review.

Exact results require mutable commercial models, several visualization engines, specialized MCP agents, substantial data, rendering dependencies, and in one case unreleased TopoPilot2. The release does not contain the human-study data or analysis, baseline outputs/tables, exact prompts for all perturbations, endpoint snapshots, immutable images, seeds, hardware/render details, or a lock that demonstrates the v2 environment. The code commit predates v2 and must be treated as release evidence, not as proof of paper-time behavior.

Operational realism is mixed. Authentic scientific formats and tools, executable scripts, application state, multiview rendering, multi-step operations, and token/time costs are substantially more realistic than static QA. Conversely, the instrument excludes multiple valid designs, open exploration, iterative analyst steering, scientific discovery, report production, and downstream decisions. It measures constrained artifact realization in specialized software, not the full professional loop.

## Concrete changes for skill-bench

1. **Refine existing criterion/grader records with an admissibility envelope.** Add authoritative artifact type, observed representation, transformation/render hash, required controls, permitted invariances, evidence sufficiency, and `not_applicable`/`invalid` states. This belongs in the existing benchmark bundle and rubric model, not a new subsystem.
2. **Use the existing validity-argument contract to block claim upgrades.** Human–MLLM correlation on selected reference-matching images may support a narrow concordance claim; it cannot license expert replacement, open-ended artifact quality, scientific usefulness, or deployment readiness.
3. **Use task health to preserve reference-narrowing history.** Record rejected alternative paths, why constraints were added, expert/novice trials, and whether an item remains a capability probe or only a regression check.
4. **Use metric monitoring to make aggregation explicit.** Specify unit, eligible cases, grader applicability, missing/invalid policy, criterion dependencies, task clustering, uncertainty, thresholds, and error cost before combining quality, completion, and efficiency.
5. **Add multimodal planted cases to the existing pilot grader tests.** Include a visually plausible but structurally wrong artifact, a structurally correct alternate rendering, a missing view, an invalid export, and a correct artifact transformed by a different renderer. Confirm each grader abstains or fails for the right reason.
6. **Preserve expert assignment and exclusion provenance.** Never replace disagreement with a filtered mean without typed reason, sensitivity analysis, and authority scope.
7. **Extend launcher canaries to network and model visibility.** The file sanitizer pattern is useful, but a valid private evaluation also requires a network policy, provider/model exposure record, and proof that public ground truth was unavailable during the run.
8. **Do not add a queue task.** These requirements refine the existing bundle, validity, task-health, metric-monitoring, participation, and execution-isolation work; no nonduplicate contract gap was found.

## Action items for repository

- [x] Read the complete immutable arXiv v2 PDF/text and verify claims with section/page evidence.
- [x] Inspect and archive the complete official code snapshot at commit `b9435d13e9ff979226b1754e6c467efeb026978a`.
- [x] Inspect the official dataset revision and all 730 published paths; record that large blobs were not downloaded.
- [x] Audit case counts, grader channels, aggregation implementation, human-evaluation tooling, Docker staging, and leakage boundaries.
- [x] Separate paper claims, release observations, and `skill-bench` adaptations.
- [x] Add no duplicate build task; map findings to existing executable contracts and the active isolation/metric work.
