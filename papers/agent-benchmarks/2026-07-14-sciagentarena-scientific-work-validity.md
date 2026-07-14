# SciAgentArena: executable scientific workflow coverage is not autonomous discovery validity

## Bottom line

SciAgentArena is valuable because it refuses to treat “science” as one question-answering construct. It assembles executable analysis, method selection, optimization, discovery-style, and premise-validation work across drug discovery, single-cell omics, spatial omics, EHR analysis, genetics, and three cross-domain probes. Its strongest design is the paired **step-wise versus pipeline** treatment for omics workflows: the same local operations become harder when outputs must survive a dependency chain. The drug-discovery release added after arXiv v1 is also unusually inspectable, with task JSONs, data, output contracts, runners, and deterministic oracles.

The paper’s evidence supports a narrower claim than its framing. It shows heterogeneous configured systems solving a purposive biomedical computational suite, with better performance on familiar local procedures than on longer, validity-sensitive, or optimization tasks. It does **not** establish performance in a sampled population of “real-world scientific research scenarios,” scientific novelty, self-directed exploration, professional validity, discovery impact, autonomy, reliability across the full suite, or readiness. “Approximately 200 tasks” mixes incomparable units: 78/79 drug prompts, omics workflow stages and validity questions, five EHR task *types* backed by 505 patient cases, genetics task groups backed by 187 MR pairs and multiple traits, and three cross-domain probes.

The release audit materially lowers reproducibility claims. The closest public GitHub snapshot at paper time contains notebooks and partial evaluators but not the later 79-task drug suite; its EHR and most cross-domain surfaces are tiny notes or one script. The official Hugging Face revision is auto-gated: metadata and README are public, but representative immutable-revision task/data downloads returned HTTP 401 anonymously. A post-v1 GitHub commit adds 79 drug tasks—one more than Methods’ 78, with 18 rather than 17 preprocessing tasks. No released run ledger, exact administered-suite manifest, outputs, per-run invalids, environment images, paper-table reproduction package, or complete cross-domain evaluator set was found.

The transferable lesson is a **dependency-aware scientific work graph**: preserve source authority, input state, stage contract, produced artifact, admissible alternatives, checks, downstream consumers, and root/surface failure attribution. Step checkpoints are valuable, but checkpoint pass rates alone cannot tell whether a later failure is a new reasoning error, inherited upstream corruption, evaluator fallback, environment breakage, or an invalid trial.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and D through expansion and consolidation. Scientific computation is one knowledge-work family, not a new scope boundary for `skill-bench`. The concrete evidence is the full immutable v1 paper plus a pinned paper-time repository, pinned review-time repository, and official dataset manifest/access audit. The uncertainty clarified is whether broad domain coverage, executable workflows, checkpoints, and biomedical data license claims about realistic science, novelty, autonomy, or reliability. Useful completion is a bounded retain/repair/test analysis that reuses the repository’s existing expertise, bundle, dependency, grader, harness, reliability, and validity contracts rather than creating a science-specific schema.

## Sources and reading record

### Immutable primary paper read in full

- Tianyu Liu et al., *Benchmarking AI Agents for Addressing Scientific Challenges Across Scales*.
- Immutable record: <https://arxiv.org/abs/2606.12736v1>.
- Immutable PDF: <https://arxiv.org/pdf/2606.12736v1>.
- Local PDF: `data/papers/pdfs/2606.12736v1-sciagentarena.pdf` (60 pages; SHA-256 `8e4460337aae7be889f6b3ea7807701da465301999b8d78e500b4781e63af02e`).
- Local layout-preserving text: `data/papers/text/2606.12736v1-sciagentarena.txt` (339,513 bytes; SHA-256 `94d7ca95477d8c7af661f8bbacb63510d3809a16c3ba40963d7eede89f88f356`).
- Local arXiv source archive: `data/papers/source/2606.12736v1-source.tar.gz` (SHA-256 `91d97ab4fe062fe072b07257beaae3a19cc8d96d6d6404d98ed4c6ea61439a1a`).
- Date read: 2026-07-14. The complete extraction was read through Methods, domain-specific task/evaluation/data sections, code/data availability, references, supplementary comparisons, and final stability figures.
- ArXiv API metadata records v1 published and last updated 2026-06-10 22:55:30Z in `cs.AI` with secondary `cs.LG`; the abstract has no withdrawal or retraction notice.

### Official release audited

- Project page: <https://sciagentarena.github.io/>.
- Official repository: <https://github.com/HelloWorldLTY/SciAgentArena>.
- Closest paper-time commit: `91d7fcf2452cbcfc996ada95fd6f166741fc8253` (2026-06-10 02:57:11Z, about 20 hours before v1 publication).
- Review-time commit: `ce27b8cdaad4dc5d5ff35a20e0b97cb35cad9f57` (2026-06-22 02:33:19Z, 11 days after v1; explicitly adds `evaluations/dd`).
- Official dataset: <https://huggingface.co/datasets/iLOVE2D/SciAgentArena>, immutable revision `52490e33c18d96d0217b82f5c6e7fd78f542a81f` (last modified 2026-06-11 01:00:05Z).
- Release provenance: `data/sources/releases/2606.12736v1-sciagentarena/provenance.json`.
- Archived code: `data/sources/releases/2606.12736v1-sciagentarena/HelloWorldLTY-SciAgentArena-91d7fcf.zip` and `HelloWorldLTY-SciAgentArena-ce27b8c.zip`.
- Dataset/API manifest: `data/sources/releases/2606.12736v1-sciagentarena/huggingface-api.json`; public dataset card: `hf-sample/README.md`.

The release status is **paper-time code and current code audited; gated dataset manifest audited, gated bytes not read**. The 120-file Hugging Face manifest is public and identifies 99 drug-discovery, nine single-cell, five spatial, three cross-domain, one EHR, one genetics, and two root metadata files. Because the repository is `gated: "auto"`, attempts to download representative immutable-revision question files from every main domain returned HTTP 401 without authentication. This review does not infer their contents from filenames and does not call them inspected.

## One-sentence contribution

SciAgentArena contributes a broad, heterogeneous executable biomedical benchmark whose strongest evidence is the local-to-pipeline and answer-to-validity gradient, but its mixed task units, partially observed releases, heterogeneous configured systems, weak expert/task lineage, and incomplete run accounting support only a bounded computational-suite result—not autonomous scientific discovery or professional research validity.

## Research question and claim boundary

The paper asks how capable and reliable current agents are on realistic scientific tasks, and what benchmark design enables fair comparison. It organizes work into Data Analysis, Optimization, Discovery, and Validity and evaluates 18 generalist/specialist systems across five named domains plus cross-domain tasks.

The evidence supports these bounded conclusions:

1. the authors constructed a large purposive collection of biomedical computational prompts, workflow stages, patient cases, and analysis instances;
2. some configured systems execute familiar local workflows and deterministic chemical operations reliably;
3. linking familiar stages into one pipeline creates substantial additional failure exposure;
4. method-selection outputs often converge on widely documented defaults;
5. premise-validation tasks expose over-compliance that ordinary executable-workflow scoring misses;
6. selected repeated drug-validity and omics pipeline evaluations show nonzero run/environment variation; and
7. the released drug suite demonstrates a workable separation among execution, chemical validity, correctness, and strategic success.

It does **not** establish prevalence over scientific work, cross-domain general intelligence, novelty of hypotheses, self-directed research, scientific impact, professional acceptance, causal benefit to scientists, safety, reliability of the full configured system population, or production readiness. It also cannot establish that specialist-versus-generalist differences come from agent architecture because backbone, tools, environment, budget, and compatibility vary jointly.

## Methodology and system

### Assembly: breadth is real, but the unit of “task” is not stable

The paper’s approximate-200 headline can be reconstructed only by treating unlike units as peers:

| Family | Headline unit | Paper count |
|---|---|---:|
| Drug discovery | individually described task prompts | 78 (Methods), later public suite 79 |
| Single-cell omics | 12 workflow/method tasks + 15 validity questions | 27 |
| Spatial omics | 11 workflow/method tasks + 15 validity questions | 26 |
| EHR | four named task types plus a fifth causal-analysis task | 5 task types, 505 cases reported for T1–T4 |
| Genetics | 14 single-ancestry PRS + 15 MR + 18 multi-ancestry PRS + 10 validity | 57 task/subtask groups |
| Cross-domain | eQTL, target identification, synthetic lethality | 3 |

Using Methods’ drug count gives 196; using the later release’s 79 gives 197. That is reasonably “approximately 200,” but it is not approximately 200 exchangeable items. EHR T2 alone includes 455 cases, while one causal task is a multi-artifact project scored on eight dimensions. MR’s 15 task groups operate over 187 trait pairs. Cross-domain eQTL averages over 100 genes. Any aggregate that treats top-level rows equally has arbitrary weighting; any aggregate that treats underlying cases equally makes EHR dominate. The paper appropriately emphasizes domain panels more than one grand score, but broad “no agent dominates” and “across scales” claims still depend on these design weights.

The task taxonomy also shifts. Results call four categories Data Analysis, Optimization, Discovery, and Validity. Drug discovery uses five role-like categories. Omics divides preprocessing, method selection, design, and validity. Genetics mixes staged pipelines and conceptual questions. EHR includes action sequences, medication-set imitation, and causal analysis. This diversity is a strength for stress testing and a weakness for interpreting one latent capability.

### Expert authority and task provenance

The paper says tasks and criteria are designed by domain experts and that all experts hold PhDs or PhD-level knowledge. Author contributions identify leads and contributors by domain. This is useful role attribution, but “thereby ensuring validity” is circular. Degrees do not establish that a task represents consequential work, that a private reference is correct, or that a grader accepts legitimate alternatives.

Missing evidence includes candidate-task inventories, work-source sampling, contributor-by-task identity, source-to-requirement lineage, elicitation protocol, rejected tasks, independent review, disagreements, adjudication, participant compensation, approval scope, update authority, and practitioner or affected-party validation. Many task sources are canonical tutorials, public datasets, prior benchmarks, and author-constructed failure cases. Those can create strong controlled tests without establishing prevalence or professional representativeness.

This differs from the laboratory-workflow elicitation evidence already reviewed in `skill-bench`: role labels and a workflow graph do not by themselves establish claim authority, masking relations, or operational validity. SciAgentArena’s PhD assertion supplies less task-level lineage than a role-gated claim ledger would. It also differs from AARRI’s research-judgment lifecycle: outputs here are mostly benchmark submissions with fixed endpoints, not observed research decisions whose adoption and downstream consequences are measured.

### Runtime and configured systems

The runtime framework gives each agent a dedicated Conda/Mamba environment, runs frontier LLMs as general agents, stores code/data/structured outputs, and limits runs to at most 24 hours. The paper says specialist agents use recommended backbones when frontier models are unsupported or too costly, and all systems operate at “maximum capacity.”

This maximizes ecological performance for each package but prevents clean attribution. A row denotes a bundle:

`backbone snapshot + provider + system prompt + wrapper + tools + package versions + data access + compute + time/call budget + retry/debug policy + evaluator adapter`.

Those bundles differ by task compatibility. Hatched cells mark incompatible agent-task combinations rather than failures. Consequently, broad averages condition on which tasks a system can attempt, while comparisons can conflate capability with compatibility and missingness. Supplementary File 1 is referenced for backbones, but the public paper-time repository does not preserve an exact run manifest binding every figure cell to immutable model/provider, prompt, environment, package, dataset, seed, and output hashes.

The framework also says evaluator environments install “the most advanced version” of packages proposed by agents. This improves rescue/executability at evaluation time but makes environment identity endogenous to the submission and time. It can turn package-version selection, evaluator repair, and infrastructure drift into unrecorded treatment variation.

### Step-wise versus pipeline execution

The most useful experimental structure is in single-cell and spatial workflows. Step-wise mode tests local operations separately; pipeline mode requires later stages to consume earlier outputs. The observed drop in pipeline mode supports a dependency/horizon hypothesis better than a static final score would.

However, the paper does not define a dependency-aware estimand. A failed early normalization can cause every later check to fail; a later error may be independent; a fallback evaluator may make an unusable submission scoreable. For batch correction, Methods says that if an agent fails to produce a usable algorithm, principal components are computed for evaluation. That protects metric execution but can score evaluator fallback rather than submitted work unless fallback outcomes are segregated.

The released notebooks show why stronger packaging is needed. Single-cell and spatial checks mutate shared `AnnData` state and contain reference code, output cells, broad `except: pass` paths, and dataset-specific thresholds. Genetics notebooks contain author-local paths such as `/home/yj348/...` and inspect expected files, package choices, commands, and gold references. These are substantive checking artifacts, but paper-time reproducibility depends on local files, execution order, manually edited configuration, and hidden references.

A step checkpoint should therefore record four separate facts: stage-local conformance, input eligibility, causal dependence on upstream outputs, and whether any fallback/repair was applied. “Passed task 8” cannot otherwise tell whether the agent created a valid stage, inherited a valid state, or was rescued by the evaluator.

### Domain-specific scoring

**Drug discovery.** The paper specifies executable scripts or notebooks, fixed output contracts, task-specific reference checks, 30-minute/100-oracle optimization budgets, and claim-validation checks that reward identifying flaws rather than forcing numeric answers. The post-v1 suite operationalizes 79 tasks across four runners/output modes. This is the most inspectable part of the release. It also exposes a paper/release mismatch: Methods says 78 total and C1=17; the registry and JSON files have 79 total and C1=18. Public ground truth, task JSON, scorers, and examples create contamination/reward-hacking exposure unless scored forms remain private.

**Single-cell and spatial omics.** Pipeline checks use pass@1; optimization uses scIB, clustering metrics, marker/SVG overlap, trajectory preservation, and perturbation prediction metrics. Ground truths are often tutorial-derived, label-derived, or silver standards. These are reproducible proxies for selected artifact properties, not proof that one method is scientifically best. Label-based cluster agreement can penalize plausible novel structure, and SVG overlap explicitly lacks gold truth. Method convergence to Leiden/Harmony/scVI/Wilcoxon/Moran’s I therefore need not demonstrate deficient creativity: prompts, package availability, reference metrics, and conservative risk under pass@1 can rationally favor robust defaults.

**EHR.** T1–T3 use action-level F1 under bidirectional substring matching; T4 fuzzy-matches medication names at SequenceMatcher ≥0.82. This ignores or weakly observes action order, arguments, dose, timing, patient state, and duplicate actions even though the prose describes action *sequences*. Substring matches can reward semantically wrong actions containing the expected token. Actual inpatient prescriptions in MIMIC-IV are historical events, not necessarily appropriate treatment recommendations. T5 is stronger: it requires `answer.json`, `cohort.csv`, code, temporal hard gating, point-estimate recomputation, and robustness reporting. But two free-text dimensions use GPT-4o-mini with no item-level judge validation reported.

**Genetics.** PRS/MR tasks inspect multi-stage files and analytical checks, which is closer to artifact-based procedural evaluation. Yet Methods says the MR benchmark covers 13 methods while passing requires successful implementation and interpretation of at least one. That pass rule measures partial workflow recovery, not completion of the declared 13-method comparison. Hardcoded cluster paths and unbundled large/controlled genotype resources further constrain independent reproduction.

**Cross-domain.** eQTL is scored against GTEx-derived calls over 100 genes; target identification and synthetic lethality use 20 subsampled Medea items each. These are transfer probes, not end-to-end cross-domain discovery. Their released paper-time implementation surface is one eQTL evaluator plus tiny target/SL notes, with data bytes gated.

## Evidence and results

### Strongest descriptive evidence

The clearest empirical pattern is a local-to-dependent gradient:

- familiar, explicitly specified chemical calculations and table operations are often solved;
- omics step-wise workflows outperform pipeline execution;
- method selection often converges on established libraries and defaults;
- open design/optimization tasks yield more runtime and implementation failures; and
- premise-validation tasks catch systems that would otherwise receive credit for executable but scientifically inappropriate work.

This supports keeping task completion and validity judgment separate. It also supports collecting artifacts and intermediate states rather than only final prose.

The paper’s error examples are useful failure signatures: reused rather than harmonized labels; asymmetric spatial graphs; nonexistent package functions; mixed-unit analysis without recognizing the red flag; and proceeding on biologically or technically unsupported requests. These are concrete benchmark authoring targets: hidden assumptions, package/API reality, unit/provenance checks, modality limits, and premise rejection.

### Reliability and denominator limits

Repetition is not uniform. Drug safety uses three runs per agent, drug claim validation reports three “independent environments,” and omics pipeline stability figures use three replicates. The rest of the suite does not have a clearly reported common repeat policy. “Independent environments” is not operationally defined: package, random seed, model call, wrapper, machine, and evaluator changes may all contribute.

The paper does not release a run ledger with scheduled, started, valid, timed out, environment-failed, parser-failed, incompatible, and substantively failed counts. Hatched incompatibilities are visible, but denominator and aggregation policies across figures are not fully reconstructable. Error bars in claim validation are described as average per-task standard errors across only three evaluations, which is a fragile uncertainty summary and does not model task or agent dependence. Omics stability plots similarly do not establish reliability under an identified deployment distribution.

Thus the evidence supports “selected configured systems varied over selected repeats,” not a stable reliability profile. Reliable scientific work would require repeated outcomes grouped by task family and environment, severity-weighted failures, correlated incident modeling, recovery behavior, and decision thresholds.

### Novelty, exploration, and autonomy claims

The paper infers limited novelty from convergence on standard methods and low performance on optimization/design tasks. That is suggestive, not a novelty evaluation. No hypothesis corpus, prior-art search, expert novelty rating, blinded usefulness assessment, prospective experiment, or downstream scientific uptake is reported. Beating a reference predictive metric on one perturbation benchmark shows task performance, not a novel scientific contribution.

“Self-directed exploration” is even less directly observed. Agents receive benchmark prompts, data, tools, output contracts, and explicit metrics. There is no self-generated research question, adaptive evidence acquisition under a hidden objective, choice to stop/escalate, or longitudinal program state. Search over a bounded molecular oracle is autonomous optimization under a fixed target, not autonomous science.

Similarly, recommendations to improve autonomy or scientific reasoning are hypotheses derived from observed errors. They are not tested interventions. The benchmark can diagnose configured failures; it does not identify which architecture change causes repair.

## Release audit: inspectability, drift, and operational realism

### Paper-time snapshot

The closest public commit before v1 contains 95 ZIP entries (5.0 MB uncompressed). Its evaluative surface consists of:

- one single-cell and one spatial notebook;
- two genetics checking notebooks;
- one eQTL comparison script;
- `target_sl.md` files of 64 and 95 bytes for cross-domain/EHR;
- agent setup material; and
- a generic Node/Python front end.

The front-end catalog does not instantiate the paper suite one-to-one. It describes generic 11-stage single-cell, 11-stage spatial, five EHR, two cross-domain, five drug, eleven genetics, and three perturbation tasks and points at local `./data/...` paths. The root README says “50+” tasks and automated scoring, but the repository does not bundle a self-contained paper-result reproduction package.

### Post-v1 drug suite

The June 22 commit adds a much stronger drug evaluation package: 79 task definitions, a registry, CLI, batch/notebook/design runners, task-specific scorers, ground-truth files, examples, environment docs, and a uniform result schema. Static audit found C1=18, C2=26, C3=10, C4=6, and C5=19. This later release is useful implementation evidence but cannot retroactively prove the exact manuscript-time instrument or runs.

The suite’s offline/no-network contract, oracle budgets, fresh notebook kernels, hidden scorer-side answer pool, and explicit output variables are good patterns. Remaining operational concerns include public private answers, no immutable package lock across every tool, optional PyTDC/network resources, generated-agent provider defaults, and no preserved paper outputs or CI run proving all 79 tasks under one frozen environment.

### Dataset access

The official Hugging Face revision was uploaded about two hours after arXiv publication and is publicly discoverable but auto-gated. Anonymous immutable downloads of representative question/data files returned HTTP 401. The manifest is dominated by drug-discovery files; EHR and genetics each appear as one workbook, while single-cell/spatial include question and large data archives. Because bytes were inaccessible, this review cannot verify paper counts, solutions, labels, source licenses, patient/trait membership, data transformations, or correspondence between the dataset and paper figures.

“Full codes, tasks, and datasets can be accessed” is therefore true only after satisfying a gate and does not yield anonymous, automatically reproducible access. A benchmark may legitimately gate biomedical resources, but the gate, terms, identity, revision, acceptance process, and artifact hashes belong in the reproducibility statement.

### Operational realism

The suite contains genuine scientific file types, package APIs, long computations, heterogeneous outputs, patient/omics/genetics data, and multi-stage dependencies. That is more operational than static QA. But it remains a controlled computational substrate: no laboratory action, scientist handoff, institutional approval, live clinical use, experiment selection, evidence procurement cost, recipient adoption, or downstream research consequence is observed. Synthetic Synthea cases, MIMIC demo records, tutorials, fixed labels, benchmark oracles, and public datasets are legitimate fixtures—not a sampled population of research practice.

## Unique insight: checkpoints need dependency and failure lineage

SciAgentArena’s deepest reusable contribution is not “science at scale.” It is the contrast between scoring a stage locally and scoring the same stage inside a dependent artifact chain. The appropriate representation is:

`source/mandate → eligible input state → stage obligation → agent operation → native artifact/state delta → stage-local checks → downstream consumers → final claim/consequence`

Each edge needs evidence. For every stage, preserve:

1. **authority and source** — who says the operation is required and why;
2. **input eligibility** — schema, quality, modality, temporal, unit, and biological assumptions;
3. **dependency identity** — exact upstream artifact hashes and required invariants;
4. **operation contract** — permitted tools, outputs, alternatives, budget, and safety constraints;
5. **artifact evidence** — native output, logs, code, state diffs, and provenance;
6. **local observation** — executable, valid, correct, calibrated, and efficient as separate checks;
7. **fallback/repair** — evaluator or human intervention, with the unassisted result retained;
8. **downstream adoption** — which later stage actually consumed which output;
9. **failure lineage** — root cause, propagation path, surface symptom, severity, and recovery; and
10. **claim ceiling** — local procedural conformance, not professional/scientific impact unless separately validated.

This prevents three common errors. First, downstream failures should not be counted as independent reasoning failures when they are deterministic consequences of one upstream defect. Second, downstream passes should not erase upstream shortcuts or evaluator repair. Third, a pipeline score should not be interpreted as “long-horizon reasoning” unless evidence shows that later success causally depends on retained, correctly adopted earlier work rather than a fresh recomputation or hidden reference.

Compared with AARRI, this graph adds executable scientific state but still lacks stakeholder action, adoption, and research consequence. Compared with laboratory-workflow twins, it has stronger machine-verifiable artifacts but weaker role/claim authority and no evidence that graph coverage is substantively complete. Compared with AstaBench’s literature-oriented research suite as characterized by SciAgentArena, it expands into code/data workflows; that expansion does not itself validate novelty or end-to-end research impact.

## Limitations and validity threats

### Construct and content validity

1. “Scientific work” is a purposive biomedical computational slice, not a sampled scientific-work population.
2. Five domains are broad labels but concentrated in biomedicine/life science; “across scales” is a biological-level narrative, not validated construct coverage.
3. Task units mix prompts, stages, types, cases, genes, trait pairs, datasets, and artifacts.
4. PhD/PhD-level authorship is asserted as validity rather than supported by task-level authority, independent review, or acceptance evidence.
5. Tutorials, prior benchmarks, labels, and author-designed traps provide controlled tests but unknown prevalence in real work.
6. Discovery, optimization, validity, and data analysis are not consistently defined across domains.
7. Real-world scenario wording exceeds synthetic/curated fixture and no-workplace-use evidence.
8. Method convergence is not direct evidence of absent creativity or novelty.
9. Fixed benchmark objectives do not measure self-directed question formation or exploration.
10. No downstream experiment, scientist adoption, decision change, or research impact is observed.

### Measurement and grader validity

11. Step checkpoint scores lack explicit upstream dependency and propagated-failure attribution.
12. Evaluator fallbacks can score repaired/default representations instead of submitted methods unless separated.
13. EHR substring F1 weakly observes sequence order, arguments, dose, timing, and patient-state consequences.
14. Historical medication lists are not necessarily professionally correct recommendations.
15. Silver standards and cell labels can penalize plausible alternative biological structure.
16. Genetics’ one-method MR pass criterion is weaker than the declared 13-method workflow.
17. Free-text GPT-4o-mini grading in EHR T5 lacks reported item-level human validity/reliability.
18. Public post-v1 drug task answers, scorers, and examples create contamination and direct optimization risks.
19. Alternative valid methods and representations are not systematically calibrated for false rejection.
20. No adversarial grader mutation study estimates false pass/fail rates.

### Statistical and comparison validity

21. Agent rows combine different backbones, tools, prompts, environments, budgets, and compatibility sets.
22. “Maximum capacity” is an unequal treatment policy, useful for package comparison but not architecture attribution.
23. Incompatible cells create treatment-related missingness and incomparable denominators.
24. Repeat policy is uneven across domains; most observations do not form a common reliability study.
25. Three repeats/environments provide fragile standard errors and do not identify sources of variation.
26. Task/case/trait/gene and workflow-stage clustering is not modeled consistently.
27. Aggregate weighting over radically different task units is under-defined.
28. No complete scheduled/started/valid/invalid/failed run ledger is released.
29. Cost and runtime are discussed but not preserved as a complete comparable per-trial resource table.
30. Error examples are selected diagnostics, not prevalence estimates.

### Reproducibility and lifecycle

31. Paper-time GitHub code is partial relative to the paper’s claimed full codes/tasks/datasets.
32. The full drug suite postdates v1 and has 79 tasks versus Methods’ 78.
33. Paper-time notebooks contain author-local paths, mutable execution state, broad exception handling, and hidden/local references.
34. The official dataset is auto-gated; anonymous representative downloads were denied.
35. Dataset bytes, exact paper membership, labels, transformations, and licenses could not be audited.
36. No model outputs, trajectories, judge calls, invalid records, paper figure tables, or complete analysis scripts were found.
37. “Most advanced package version” makes evaluator identity mutable and partly submission-dependent.
38. Model/provider snapshots, prompts, seeds, retries, package locks, compute images, and network states are not bound per figure cell.
39. The front-end catalog and paper taxonomy drift in counts and task descriptions.
40. Community extensibility is proposed without a released intake/authority/adjudication/lifecycle protocol.

### Safety and professional validity

41. Clinical task scores do not establish safe patient care; no clinician action or consequence is measured.
42. Chemical optimization/safety oracles do not establish synthesizability, experimental safety, or campaign value.
43. Genotype/biomedical data governance and gated-access terms are not integrated into the paper’s operational evaluation description.
44. No institutional approval, human handoff, escalation, affected-party burden, or rollback process is evaluated.
45. No professional or deployment threshold is defined.

## Reproducibility and operational realism assessment

- **Paper inspectability:** strong. The immutable 60-page v1 gives extensive domain-specific Methods and examples.
- **Paper-time implementation inspectability:** moderate-to-weak. Core notebooks and one evaluator exist, but the full claimed instrument and results do not.
- **Post-v1 drug implementation inspectability:** strong for static task/scorer review, with clear timing drift.
- **Dataset inspectability:** manifest-level only in this review because immutable data bytes are gated.
- **Result reproducibility:** weak. No complete run/config/output/table package was found.
- **Operational realism:** moderate for computational artifacts and workflow dependencies; weak for scientist collaboration, institutional context, real intervention, and consequence.
- **Evidence tier:** Tier B enabling evidence for heterogeneous executable-workflow and dependency-aware benchmark design; not evidence of professional validity, discovery impact, capability in a defined science population, safety, production fitness, or readiness.

## Transfer to skill-bench

### Retain

1. **Plural work forms.** Keep analysis, optimization, validity judgment, and artifact production separate rather than collapsing knowledge work into QA.
2. **Step-wise/pipeline pairing.** Use matched local and dependent conditions to expose integration burden.
3. **Native outputs.** Score code, dataframes, figures, structured state, and files—not only prose.
4. **Validity tasks.** Include unsupported-premise cases paired with legitimate near-neighbors so useful skepticism is measured separately from completion.
5. **Execution/validity/correctness separation.** Preserve distinct gates and score families.
6. **Task-specific metrics behind common evidence contracts.** Domain metrics may differ while provenance, applicability, observer sufficiency, and claim limits remain shared.

### Repair

7. **Define the unit of work.** Distinguish suite, family, workflow, stage, case, replicate, and underlying sample; never advertise one count without a typed count manifest.
8. **Add dependency lineage.** Bind every stage to exact upstream artifact hashes and record causal use by downstream stages.
9. **Separate root and propagated failure.** Report stage-local defects, inherited invalid inputs, infrastructure errors, fallback use, and downstream symptoms.
10. **Keep evaluator repair out of unassisted scores.** A PCA fallback or package rescue should create a separate assisted condition.
11. **Calibrate alternatives.** Use expert-approved and metamorphic variants to test false rejection of valid methods, formats, and action sequences.
12. **Freeze configured-system identity.** Hash prompts, wrappers, tools, model/provider snapshots, environments, network policy, budgets, and adapters per trial.
13. **Make missingness explicit.** Incompatible, gated, timeout, environment-failed, parser-failed, and substantive failure must remain different states and denominators.
14. **Preserve complete run evidence.** Schedule, start, artifacts, logs, metrics, cost, invalid reason, retries, and final inclusion must be auditable.
15. **Bound the claim.** Executable benchmark success supports selected procedural/artifact conformance, not scientific novelty, professional competence, or research impact.

### Test

16. **Dependency necessity intervention.** Replace an upstream artifact with a plausible wrong or independently correct alternative and test whether downstream behavior/score changes appropriately.
17. **Stage reset ablation.** Compare local stage, cumulative pipeline, and pipeline-with-clean-upstream conditions to identify integration versus local capability.
18. **Fallback ablation.** Report original failure, evaluator-repaired score, and repair burden separately.
19. **Alternative-path calibration.** Blind domain reviewers to reference identity and estimate verifier acceptance of legitimate methods versus near-invalid contrasts.
20. **Reliability matrix.** Use the already pending repeated cross-pilot task-family reliability work rather than a science-only build: repeats should cross task family and environment perturbation with item-family clustering and invalid-run accounting.
21. **Impact bridge only if evidence exists.** If a future pilot claims research usefulness, measure expert adoption, changed decision/artifact, correction burden, and downstream outcome; do not infer these from benchmark metrics.

## Concrete repository actions

- **No new queue task added.** The dependency, artifact-view, invalid-run, configured-system, validity, and reliability machinery already exists; `build-repeated-cross-pilot-reliability-matrix` is pending and directly covers the strongest untested implication. Adding a SciAgentArena-specific build would duplicate it and narrow scope.
- During the next synthesis consolidation, index this review as Tier B under realistic knowledge work/workflows and reliability, with the claim ceiling above.
- Do not use the paper’s approximately-200 count as a sample size, the heatmaps as a universal agent ranking, method convergence as a novelty score, or three-repeat variation as a deployment reliability estimate.

## Assessment

- **Most reusable contribution:** matched local-stage versus dependent-pipeline evaluation with native scientific artifacts.
- **Most important empirical signal:** familiar local procedures can succeed while dependency chains and validity judgments remain fragile.
- **Most serious measurement flaw:** mixed task units and incomplete run/dependency accounting make broad capability and reliability interpretations under-identified.
- **Most serious reproducibility flaw:** the paper-time public code is partial, the fuller drug suite postdates v1 and changes counts, and official task/data bytes are gated without a released paper-run package.
- **Claim `skill-bench` may safely make:** scientific workflow benchmarks should preserve typed stage dependencies, native artifacts, premise-validity checks, configured-system identity, invalid/fallback states, and root-versus-propagated failure; these observations can support bounded procedural conformance claims, not professional validity, scientific novelty, autonomous discovery, research impact, safety, production fitness, or readiness.
