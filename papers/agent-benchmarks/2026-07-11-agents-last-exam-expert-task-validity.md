# Paper and Release Review: Agents' Last Exam — Executable Breadth Is Not Occupational Readiness

- **Paper:** https://arxiv.org/abs/2606.05405v1
- **Date read:** 2026-07-11
- **Primary evidence:** immutable arXiv v1, 39 pages
- **Local PDF:** `data/papers/pdfs/2606.05405v1-agents-last-exam.pdf` (SHA-256 `db0bc77073c8906ec1b3612d72714a6f4b08bb8294a0589660186e2b887864a5`)
- **Local text:** `data/papers/text/2606.05405v1-agents-last-exam.txt` (SHA-256 `daf9138040682e16a6484a6af924b17d3a97c340cd5e32ace5e8de5e35709bed`)
- **Official release:** https://github.com/rdi-berkeley/agents-last-exam at commit `186691830cd6906a405cb997b39bc5f5ca82e2a4`; archive `data/sources/releases/2606.05405v1-agents-last-exam/rdi-berkeley-agents-last-exam-1866918.zip` (SHA-256 `e247c79e50f44012b016b1342a987d39d8a0a58e33ba4bfa20054727c1c9b098`); provenance `data/sources/releases/2606.05405v1-agents-last-exam/provenance.json`
- **Timing boundary:** the inspected commit is dated 2026-07-09, after arXiv v1 (2026-06-03) and v2 (2026-06-11). It is official release evidence, not the exact v1 implementation.
- **Tags:** occupational-frame, expert-authoring, executable-artifacts, deterministic-graders, long-horizon-agents, living-benchmark

## One-sentence contribution

Agents' Last Exam (ALE) assembles 1,490 claimed task instances across 55 software-mediated subdomains, converts expert project submissions into VM tasks with artifact-based graders, and evaluates many model–harness packages; its strongest contribution is a broad executable-task production system, while its “last exam,” occupational readiness, domain-knowledge diagnosis, and GDP-impact interpretations exceed the evidence supplied by selected tasks, predominantly single runs, authored references, and unvalidated grader completeness.

## Why this matters for skill-bench

This review advances charter objectives A, B, C, and F. ALE is unusually close to the charter's ambition: heterogeneous professional artifacts, GUI and CLI work, real software, expert sourcing, private/public operation, configured-agent comparisons, and inspectable graders. The concrete artifact is a full-paper plus pinned-release audit, including end-to-end inspection of finance, radiology, and manufacturing tasks.

The central uncertainty is whether **broad executable coverage can support broad professional claims**. ALE demonstrates machinery for implementing many artifact workflows. It does not show that its convenience collection estimates an occupation's work distribution, that deterministic similarity checks are sufficient for professional acceptance, or that passing one isolated workflow establishes readiness for a profession. This is expansion for reusable machinery, not a proposal to make U.S. occupational taxonomy or ALE's 55 subdomains the scope of `skill-bench`.

## Research question and claim ladder

ALE asks whether generalist computer-use agents can execute long-horizon, economically valuable professional workflows with verifiable outcomes. The paper's interpretation implicitly climbs this ladder:

```text
SOC/O*NET occupational frame
→ digitally executable workflow subdomains
→ expert-contributed past projects
→ engineered isolated task instances
→ reference/rubric score
→ task-workflow competence
→ professional readiness
→ GDP-relevant impact
```

The release substantially instantiates the middle three links. Every upward inference needs additional evidence. In particular, a full score establishes success under one task implementation and grader—not occupational representativeness, acceptance under alternate legitimate methods, safe deployment, or economic substitution.

## Methodology and system

### 1. Taxonomy and collection frame

ALE screens 1,016 O*NET 30.2 occupation entries using a fixed GPT-4o-mini prompt, consolidates them to 117 SOC base codes, groups work into 51 SOC-anchored workflow subdomains, and adds four frontier subdomains plus seven extensions. This yields 55 subdomains in 13 clusters (Appendix B.1, pp. 16–18). Figure 2 reports 1,490 instances and nonzero coverage in all 55.

This is a useful **coverage coordinate system**, not a sampling design. The paper does not publish the 1,016 screening labels, prompt-level validation sample, expert disagreement, inclusion probabilities, task-frequency weights, or denominators from retained occupational tasks to collected workflows. “All 55 covered” means at least one implemented or pending instance per authored bucket; it does not mean proportional coverage of occupations, activities, consequences, or labor value. The LLM-assisted mapping of 16 prior benchmarks into ALE's own taxonomy is similarly not validated by independent coders (pp. 4, 16–18).

### 2. Expert recruitment, task transformation, and authority

ALE reports 250+ experts in the abstract, 300+ practitioners in related-work language, and an extensive contributor list. Advisory committees recruit practitioners, who upload projects they previously completed over days or weeks. AI assistance helps specify description, inputs, software, deliverable, and evaluation. Tasks then pass first review, engineer implementation/dry-run, and committee QC for reference correctness, evaluation bounds, context sufficiency, and reproducibility (pp. 4–5, 18–20).

The staged handoff is promising, but the study does not report eligibility rules, years of experience, author/reviewer counts by domain, compensation, hours, consent or ownership terms, conflicts, independent ratings, disagreement, defect yield by gate, reviewer reliability, or how many accepted tasks were materially altered by engineers. Authority can be lost at the **expert specification → engineer environment → grader** transformation. “Expert-authored” therefore cannot be inherited by every executable detail without a lineage and reapproval record.

Figure 5 is also easy to overread: 960 external variants include 128 strong accepts, 369 accepts, 157 borderline accepts, 158 minor revisions, and 148 major revisions; 530 are internally commissioned. Of 1,490 instances, 150 are public, 1,017 private, and 323 unverified. Thus 323 (21.7%) were pending QC in the reported total, and commissioned builds are not equivalent evidence to practitioners uploading prior shipped projects.

### 3. Execution and evaluation architecture

Each task's `main.py` exposes `load()`, `start()`, and `evaluate()`. A VM stages `input/`, `software/`, writable `output/`, and hidden `reference/`; host-side or VM-side graders return [0,1]. Artifact modes include exact/hash, structured numeric/tabular, geometric, visual, behavioral state, semantic rubric, and executable tests. Gate-and-score, weighted rubrics, checklists, and file-pair averaging compose criteria (pp. 5–7, 26–31).

This separation is valuable and closely matches `skill-bench`'s task/environment/grader objects. Yet v1's claim that the same spec can move across cloud VMs or local containers “without modification” is an interface aspiration, not demonstrated equivalence (p. 26). Licensed applications, Windows images, GPU stacks, live sources, fonts, and proprietary harnesses remain mutable. The later release supports multiple providers, but task data, images, licenses, credentials, and service access are operator prerequisites.

The paper says 93.2% of open workflows are code-graded and 6.8% use LLM judges, based on static scanning (p. 30). Determinism is not soundness: a reproducible function may reward an incomplete proxy. Nor are all LLM probes sharply objective; released examples such as “correct enough to pass,” “coherent,” and “acceptable enough” remain threshold-free subjective judgments (pp. 29–30).

### 4. Evaluation design and evidence

The public evaluation uses Near-Term, Full-Spectrum, and Last-Exam sets, with a five-hour cap and many model–harness configurations. Table 1 reports task-macro pass and mean score, cost, time, and tokens. Only a subset has three runs; most cells are single attempts (pp. 7–9). Scores are therefore noisy configured-system observations, not stable capability estimates. There are no task-clustered confidence intervals, repeated-run distributions, paired seeds, or missing-run sensitivity analyses.

Difficulty is outcome-informed: Near-Term contains workflows frontier agents can partly complete; Last-Exam contains the hardest, mostly zero-pass workflows (pp. 8–9). This is useful operational routing, but it makes tiers task-health roles, not intrinsic difficulty constructs. Versioned systems can change membership, and selection on observed outcomes biases subsequent comparisons unless the admission snapshot and intended estimand are frozen.

The public/full representativeness check runs one configured system and correlates 12 visible cluster-level pass rates (transport omitted) between subsets (`r=.89`), while acknowledging the private pool is easier (p. 33). A high correlation of coarse domain rankings does not establish equivalent task mixtures, score distributions, grader modes, software demands, or model rankings. It cannot support the phrase “faithfully reflects” the full pool generally.

### 5. Failure diagnosis

For failed Claude Code + Opus 4.7 runs, Codex generates cards from logs and artifacts but is explicitly prohibited from reading the full transcript; GPT-4o then assigns one root cause at temperature zero. The paper attributes 31% to understanding, 47% to approach, and 22% to execution, excluding timeout/resources (pp. 34–35).

This is not validated root-cause evidence. The taxonomy has no human ground truth, inter-rater agreement, ambiguous/multiple-cause option, causal intervention, or root-versus-surface protocol. “Would a domain expert have avoided this?” collapses task disclosure, retrieval, reasoning, tool affordance, and grader defects into “domain knowledge.” Omitting the full transcript reduces evidence precisely where an earlier causal failure may appear. The result is useful hypothesis generation, not support for the claim that domain knowledge is the dominant bottleneck.

## Pinned release inspection

The post-paper archive contains 1,503 entries, 1,034 files, runner/provider code, 15 agent adapters, tests/docs, and 157 non-demo `main.py` workflows across 14 release directories. Excluding seven demo workflows gives 150 public workflows, agreeing with the README's approximate public count. The domain directory counts are highly uneven (health 26; computing 23; business 21; engineering 20; social sciences 1).

The later selected split files do **not** reproduce v1's exact evaluation set. They list 67 Near-Term, 55 Full-Spectrum, and 38 Last-Exam entries, versus v1's 59/55/36. The union is 152 unique workflows because two Near-Term/Full-Spectrum and six Full-Spectrum/Last-Exam entries overlap. This is legitimate living-benchmark evolution, but it proves that score-bearing suite identity must include immutable membership and role; a tier name is not a version.

### Trace 1: equity research workbook (business/finance)

`tasks/business_finance/equity_research_summary/main.py` instructs the agent to combine fixed FY2023 values with live Yahoo Finance fields in one `.xlsx`, requiring formulas and presentation conventions. `evaluate()` reads the workbook and a hidden manifest, then calls `score_workbook_bytes`.

**Conformance:** output path, fixed/live source distinction, formulas, and formatting are publicly disclosed; the hidden manifest can test fair consequences of those requirements. The editable workbook is an appropriate authoritative artifact rather than a screenshot.

**Validity limits:** live Yahoo fields make task state time- and provider-dependent unless an as-of timestamp, retrieval snapshot, tolerance, and outage policy are pinned. A manifest can verify selected cells and style but cannot by itself establish that the equity summary is decision-useful, sourced to authoritative disclosures, or professionally acceptable. This task resembles GDPval's artifact production but gains executable grading at the cost of narrowing the target to manifest-observable qualities.

### Trace 2: chest-X-ray adjudication (health/medicine)

`tasks/health_medicine/microdicom_nih_cxr_reader_adjudication/main.py` instructs review of nine DICOM cases, two readers' boxes, notes, and three TSV outputs. The grader checks reader choice/IoU, selected log fields, and exact impressions, then equally averages three binary components.

**Conformance:** schemas, allowed labels, and required files are explicit. Image evidence plus candidate annotations creates a genuine adjudication operation rather than pure QA.

**Validity limits:** the task fixes every case to `Atelectasis` and `positive_for_atelectasis` in the public prompt, making one-third of the score largely transcription/compliance. The log scorer checks `case_id`, `selected_reader`, and `disagreement_type` but not the free-text `resolution_basis`; professional reasoning quality is therefore requested but not measured. Equal weighting lets exact boilerplate impressions count as much as nine image-level box adjudications. Hidden agreement with one authored reference is not clinical ground truth, patient-safety validation, or radiologist readiness.

### Trace 3: PowerMill toolpath generation (engineering/manufacturing)

`tasks/engineering/gcode/main.py` exposes collision/gouge gates and geometric thresholds, then evaluates 18 variants with common code. The normal path uploads scripts, checks collisions, simulates the saved PowerMill project, and compares 10,000 sampled surface points to a hidden STL.

**Conformance:** safety gate, target geometry, tools, save path, and exact score formula are public. This is a strong example of artifact-plus-executable-state grading.

**Validity and gaming limits:** if `output/agent_sim.stl` already exists, the released evaluator enters “test mode” and skips both collision checking and simulation, then scores that STL directly against the reference. Unless the environment proves the output directory begins clean and agents cannot create that path before evaluation, the gate is bypassable by submitting an STL rather than a safe PowerMill project. More generally, one-way candidate-to-reference surface distance may not penalize all missing/extraneous geometry symmetrically; a canonical STL is a witness, not proof of verifier completeness. No released metamorphic/adversarial test establishes necessity and sufficiency across legitimate alternate toolpaths.

## Evidence and claim boundaries

**Strongly supported:**

1. ALE operationalizes a large, heterogeneous pipeline from professional-work proposals to executable artifact tasks.
2. The public post-paper release is substantial and inspectable: approximately 150 non-demo workflows, provider abstractions, harness adapters, and task-specific graders.
3. Under the reported configurations, public tasks are difficult and performance varies materially by task, model, harness, cost, and time.
4. Shared lifecycle interfaces and mixed artifact modes are reusable benchmark machinery.

**Partially supported:**

- Authenticity: practitioner sourcing and committee review are meaningful content evidence, but transformation lineage and expert reliability are not reported.
- Verifiability: most graders are code-based, but completeness, alternative-path acceptance, and anti-gaming tests are not demonstrated suite-wide.
- Breadth: 55 subdomains provide frame breadth, not a probability sample of occupational work.
- Public/private comparability: one system's coarse cluster correlation is suggestive, not general representativeness.

**Not supported by v1:**

- Professional readiness from task pass.
- GDP relevance or economic transformation from benchmark saturation.
- “Domain knowledge” as the causal source of most failures.
- Deterministic cross-provider/environment reproducibility.
- Expert-level or safe performance in clinical, legal, financial, or manufacturing deployment.
- A stable living-leaderboard comparison without immutable suite membership, grader, environment, and policy versions.

## Unique insight

ALE reveals a crucial distinction between **workflow coverage** and **workflow closure**.

Coverage asks whether a taxonomy cell has a task. Closure asks whether the benchmark preserves and validates the whole chain:

```text
professional demand
→ public requirements and source authority
→ initialized environment
→ permissible solution paths
→ artifact and consequential state
→ necessary/sufficient checks
→ acceptance threshold
→ licensed inference population
```

ALE is unusually broad at the first concept and strong at producing the middle machinery. But a task is not professionally “closed” merely because `evaluate()` returns a deterministic number. The radiology case requests reasoning it does not score; the CAM task has a test-mode gate bypass absent a clean-output invariant; the equity task mixes fixed and live evidence without an explicit time-state contract. These are not reasons to reject executable grading—they show why grader code must itself be treated as a falsifiable instrument.

A second insight is that **living benchmarks require role-versioning, not just new task IDs**. In the later release, tier membership overlaps and counts differ from v1. A workflow may simultaneously serve breadth coverage, near-term regression, and frontier challenge, but each role has a different selection mechanism and permissible comparison. Store suite membership, admission evidence, exposure state, and role transitions as immutable events.

## Limitations of the study and this audit

1. Convenience collection within a principled occupational frame, not probability sampling.
2. Unequal task density across domains and no task-frequency or consequence weights.
3. 323 reported instances pending QC and 530 commissioned builds blur “expert past project” provenance.
4. No contributor eligibility, labor, compensation, consent, ownership, disagreement, or retention evidence.
5. Engineer transformations are not paired with explicit expert reapproval lineage.
6. Most model–task cells are single attempts; repeated subsets are unspecified.
7. No hierarchical uncertainty, paired stochastic analysis, or missing-run sensitivity.
8. Outcome-informed difficulty tiers.
9. Public/full comparison uses one system and coarse cluster correlation.
10. Grader determinism is conflated with validity; suite-wide adversarial verifier testing is absent.
11. LLM probes retain subjective “enough to pass” thresholds and mutable models.
12. Root-cause labels are model-generated, single-label, transcript-limited, and unvalidated.
13. Harness comparisons do not equalize all prompts, tools, compaction, retries, or proprietary behavior.
14. Five-hour censoring and partial-artifact scoring alter the estimand across harnesses.
15. Live data, licenses, proprietary software, images, and provider services limit reproducibility.
16. Release commit postdates v1; differences cannot be projected backward.
17. This audit statically inspected the full archive inventory and three tasks deeply but did not provision licensed VMs or execute all 150 workflows.

## Reproducibility and operational realism

ALE's public release is much more reproducible than a paper-only benchmark: grader code, task prompts, split files, runner abstractions, and environment guides are preserved at a commit. The task forms include editable workbooks, DICOM/image decisions, CAD/CAM projects, simulations, and multi-file packages. This is substantial artifact realism.

Full reproduction remains expensive and in places impossible without cloud images, proprietary applications/licenses, API credentials, live services, and unpublished private tasks. The paper does not release the exact result table, trajectories, task-review histories, failure cards, or exact manuscript-time tree. “Same spec across backends” therefore needs conformance evidence per task/backend combination. Operational realism is also bounded: isolated one-shot VMs omit colleagues, approvals, evolving organizational state, downstream consequence, and recovery after review.

## Comparison with adjacent benchmarks

- **GDPval:** broader occupational sampling rationale and human comparative grading, but one-shot artifact production and no executable environment. ALE adds stateful execution and code graders; neither establishes occupation-level validity. GDPval's witness/judge separation remains essential because ALE's reference is also only a witness.
- **LH-Bench:** makes expert procedures and rubric crosswalks explicit and supports skill ablation. ALE has more domains and software, but exposes less systematic evidence that expert procedure, public requirement, and grader criterion remain independent.
- **SaaS-Bench:** emphasizes stateful business workflows and consequential database state. ALE broadens artifact types and software but often grades final outputs without demonstrating all workflow-state consequences.
- **Workflow-GYM:** supplies controlled initial state and workflow execution machinery. ALE contributes authentic-tool breadth, while inheriting the same need to prove preconditions are not pre-satisfied and graders distinguish doing from merely ending in a plausible state.
- **Existing skill-bench taxonomy:** ALE validates configured-system identity, artifact-view admissibility, public-basis/private-consequence, task health, evidence-view, and execution-envelope boundaries. Its genuinely additive emphasis is role-versioned living-suite membership tied to occupational-frame denominators; this can be represented in existing task-health/metric/validity records rather than a new subsystem.

## Transfer to skill-bench

### Preserve

1. Use a declared cross-domain frame before solicitation, with explicit digital/non-digital exclusions.
2. Separate expert submission, engineer implementation, dry-run, and final domain review.
3. Standardize task lifecycle interfaces while permitting heterogeneous artifact modes.
4. Prefer inspectable structured artifacts and executable checks over holistic judges.
5. Preserve public calibration tasks and rotating private capability tasks as different operational roles.
6. Report pass, partial score, cost, wall time, tokens, timeout, and configured-system identity separately.

### Correct

1. **Four denominators:** record occupational frame, workflow-family universe, realized suite assembly, and licensed inference population; do not treat nonzero taxonomy cells as representativeness.
2. **Transformation authority:** require explicit expert disposition after engineer changes to instructions, assets, environment, reference, and grader.
3. **Verifier falsification:** for every consequential grader, add positive witnesses, legitimate alternatives, minimally wrong contrasts, adversarial shortcuts, metamorphic invariances, and necessity/sufficiency status.
4. **Clean-start contract:** cryptographically attest initialized input/output/reference visibility and reject a run as invalid—not agent failure—when preconditions are violated. The CAM `agent_sim.stl` bypass is a concrete planted test.
5. **Criterion coverage:** crosswalk every requested professional judgment to an observed view and check. Requested-but-unscored `resolution_basis` must be removed from the capability claim or evaluated.
6. **Role-versioned living suites:** immutable membership hash, tier/role, admission rationale, outcome-selection status, exposure state, replacement bridge, and retirement event.
7. **Repeated hierarchical measurement:** estimate stochasticity at trial/task/workflow/domain levels and preserve missing/timeout policies.
8. **Bounded diagnosis:** allow multiple causal hypotheses, require full evidence views, report confidence/disagreement, and validate labels via interventions before aggregating “domain knowledge” failures.
9. **Claim ladder:** task execution → workflow family → occupation → deployment/economic impact requires independent evidence at every step.

## Concrete next actions

1. **No new queue task.** Existing expertise-transfer, expert-participation, benchmark-bundle, artifact-admissibility, task-health, metric-monitoring, validity, execution-isolation, leakage, and longitudinal contracts can hold the requirements.
2. Add the ALE release's split drift as a test case when consolidating living-suite role transitions: immutable membership hashes must differ across v1 and the later commit, even when labels are unchanged.
3. Add the released CAM pre-existing-`agent_sim.stl` path as a verifier-adversary fixture in the next grader/task-health validation slice: it must invalidate the environment or fail the provenance gate, never bypass collision/simulation.
4. In the next cross-domain pilot audit, require a requested-criterion coverage report so unscored professional reasoning cannot silently support the capability interpretation.
5. Before any occupation/economic claim, predeclare a workflow sampling frame, frequency/consequence weights, generalization boundary, and validation against independent practitioners and downstream acceptance.

## Action items

- [x] Read the complete immutable arXiv v1 paper.
- [x] Inspect the complete pinned official post-paper archive inventory.
- [x] Reconcile paper and later-release public workflow/split counts with timing boundaries.
- [x] Trace finance, health, and manufacturing tasks from public instruction through environment paths and grader behavior.
- [x] Audit expert authority, occupational denominators, grader necessity/sufficiency, uncertainty, execution realism, leakage, and living-suite governance.
- [x] Compare ALE with GDPval, LH-Bench, SaaS-Bench, Workflow-GYM, and the canonical taxonomy.
- [x] Map findings to existing contracts without adding a duplicate task.
- [ ] Obtain independent expert and empirical evidence before licensing occupational-readiness or economic-impact claims.
