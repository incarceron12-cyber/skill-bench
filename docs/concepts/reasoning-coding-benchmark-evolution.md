# Reasoning and coding benchmark evolution: what to retain, repair, and not claim

**Status:** comparative deep research based on four full primary papers and inspection of two current official releases. This is an evolution-chain review, not a claim that question answering or programming defines knowledge work.

## Decision filter

- **Charter objectives:** A (frontier), B (expertise-to-evaluation), and D/E (comparative consolidation and human learning).
- **Evidence/artifact:** four immutable/versioned local PDFs and text extractions; pinned official MMLU-Pro and LiveCodeBench release snapshots; this cross-family comparison.
- **Uncertainty clarified:** why simple benchmarks became standard, which successor repairs are evidenced, and which claims remain invalid despite harder or fresher items.
- **Mode:** expansion plus consolidation.
- **Useful completion:** explicit retain/repair/test rules that transfer to realistic knowledge-work instruments without treating benchmark popularity, hardness, or test execution as validity.

## Sources actually read and release boundary

| Source | Local evidence | Role |
|---|---|---|
| Hendrycks et al., *Measuring Massive Multitask Language Understanding*, arXiv:2009.03300v3 | `data/papers/pdfs/2009.03300v3-mmlu.pdf` (SHA-256 `d3a7b0f...48fc1`); `data/papers/text/2009.03300v3-mmlu.txt` | established reasoning/knowledge anchor |
| Wang et al., *MMLU-Pro*, arXiv:2406.01574v4 | `data/papers/pdfs/2406.01574v4-mmlu-pro.pdf` (`f9d1a3...fcc57`); text sibling | reasoning successor |
| Chen et al., *Evaluating Large Language Models Trained on Code*, arXiv:2107.03374v2 | `data/papers/pdfs/2107.03374v2-humaneval.pdf` (`ebae72...c4855`); text sibling | executable coding anchor |
| Jain et al., *LiveCodeBench*, arXiv:2403.07974 (fetched 2026-07-11; latest unversioned PDF) | `data/papers/pdfs/2403.07974-livecodebench.pdf` (`a9bd3f...b427`); text sibling | rotating coding successor |
| Official MMLU-Pro release | `data/sources/releases/benchmark-evolution/MMLU-Pro/`, commit `f418b116db00b065c2aea046518d8fcf74d39872` | post-paper/current implementation, not assumed to be v4 paper-time code |
| Official LiveCodeBench release | `data/sources/releases/benchmark-evolution/LiveCodeBench/`, commit `28fef95ea8c9f7a547c8329f2cd3d32b92c1fa24` | post-paper/current implementation, not assumed to be paper-time code |

The release snapshots include model adapters, prompts, and evaluation code (both), plus scenario machinery and errata (LiveCodeBench). MMLU-Pro's bulky archived model-output directory was inspected but omitted from the preserved snapshot; the review does not depend on those outputs. The current commits postdate the papers and are implementation evidence only where explicitly noted.

## Chain 1 — broad multiple-choice knowledge to harder reasoning

### MMLU: the adoption bargain

MMLU assembled 15,908 multiple-choice questions from 57 subjects spanning elementary through professional levels and evaluated zero/few-shot accuracy (paper §§1–3). Its contribution was not ecological realism. It made **breadth cheap, standardized, and decomposable by subject** while retaining one common interface and exact scoring. The paper also reported calibration and lopsided subject performance rather than only a macro average.

That design explains its influence more credibly than “valid measure of general intelligence”: it is easy to run across model families and easy to communicate. The MMLU-Pro paper itself calls MMLU a “de facto standard” and documents near-clustering of 2024 frontier results around 86–87% (p. 2), which is adoption evidence through routine model comparison, not evidence that the construct is valid for professional work.

**Original evidence limits:** MMLU’s subject labels are a convenience sample, not an inference population of occupations or work activities. Four-choice final answers obscure retrieval, reasoning, confidence, source use, and consequence. “Professional” means exam-source level, not demonstrated professional performance. The original human comparisons use heterogeneous convenience groups and do not turn a test score into readiness.

### MMLU-Pro: evidenced repair and residual confound

MMLU-Pro narrows 57 subjects into 14 domains, expands to more than 12,000 questions, uses ten choices, shifts toward college-level reasoning questions, and conducts two rounds of review, including model-assisted error finding followed by targeted human verification (§§1, 3). Its direct evidence for repair is stronger than a difficulty assertion:

- accuracy falls 16–33 points relative to MMLU;
- across 24 prompt styles, reported score variation drops from roughly 4–5% to about 2%;
- chain-of-thought helps on MMLU-Pro while often hurting on MMLU;
- an audit of 120 GPT-4o errors attributes 39% to reasoning, 35% to domain expertise, and 12% to computation (paper pp. 1–2 and error-analysis section).

These results support **more headroom and lower tested prompt sensitivity**. They do not establish that ten distractors measure deeper reasoning rather than greater elimination burden, nor that chain-of-thought gain identifies the causal construct. The error taxonomy is small, model-specific, and judgment-dependent; no inter-rater reliability is reported. Filtering with strong models and retaining difficult items also makes the administered population partly outcome-conditioned. The current release stores prompts and many model outputs, improving auditability, but its evolving code/output inventory means instrument identity must be pinned.

### Where BBH, ARC, GSM8K, GPQA, and ARC-AGI fit

The papers position ARC, BBH, GSM8K-style mathematical reasoning, and exam suites as narrower predecessors/adjacent probes; MMLU-Pro imports more reasoning-heavy material rather than inheriting one clean lineage. GPQA and ARC-AGI go further toward expert-resistant questions or abstraction/skill-acquisition, but they change the construct and response process. **Hardness is not succession evidence.** A successor claim requires a matched test showing that the old failure (noise, prompt instability, saturation, contamination, or shortcutting) was reduced without silently replacing the population.

**Unique insight:** the chain is not “easy → hard.” It is **cheap common interface → saturation/shortcut concern → difficulty-conditioned item reconstruction**. This preserves comparison at the cost of changing domain mix and item-selection policy. Scores across the boundary are not a capability time series without anchors and bridge evidence.

## Chain 2 — standalone function synthesis to rotating multi-scenario coding

### HumanEval: executable equivalence as the decisive repair

HumanEval contains 164 hand-written Python function problems with unit tests (paper §2.1). The key methodological move is functional correctness: unlike reference-text similarity, tests admit many equivalent programs. The paper defines an unbiased pass@k estimator because naive averaging is biased when only a finite number of samples is generated (§2.1). It also documents sandboxing hazards and warns that untrusted generated code requires stronger isolation than the presented setup.

This is a durable strength: **turn requirements into executable consequences and preserve alternative valid implementations**. Yet the unit is a docstring-to-standalone-function interview exercise. Hidden tests are incomplete observers; pass@k mixes model ability with sampling budget and candidate selection; passing says little about maintainability, repository integration, security, or professional handoff. Hand-writing reduces direct copying but is not proof of training-set non-exposure. The paper’s own strongest results use up to 100 candidates, which is a resource-conditioned portfolio success probability, not one-shot reliability.

### LiveCodeBench: freshness and plural scenarios

LiveCodeBench continuously sources contest problems from LeetCode, AtCoder, and Codeforces and timestamps them. The paper’s initial release covers more than 500 problems from May 2023–May 2024 and evaluates code generation plus self-repair, code execution, and test-output prediction (§1). It uses model-cutoff-relative windows and reports performance drops after the stated cutoff for selected models as evidence consistent with older-problem exposure. The current official release operationalizes scenario-specific prompts, model adapters, pass@k, execution utilities, and score computation; it also carries an `ERRATA.md`, which is useful evidence that benchmark operation includes grader/data repair.

The repair is real but bounded:

- **freshness:** release dates make exact post-cutoff exposure less plausible and enable time slices;
- **coverage:** four scenarios expose model-ranking changes hidden by generation-only tests;
- **inspectability:** executable tests and released completions permit error and scorer audits.

“Contamination-free,” however, is too strong. Cutoff dates can be uncertain, contest solutions can propagate rapidly, benchmark use itself creates post-release exposure, and time windows change difficulty/source composition. The observed pre/post drop is endogenous: older and newer problem populations may differ. Rotation reduces one exposure route but introduces form drift and maintenance burden. Contest programming remains far from repository issue resolution, terminal operation, stakeholder requirements, code review, and deployment consequences.

### Where SWE-bench Verified and terminal suites fit

Repository and terminal benchmarks expand the unit from function to issue/environment episode and retain executable outcomes. Their added realism introduces new confounds: repository selection, issue solvability, dependency reconstruction, test incompleteness, harness permissions, patch equivalence, and environment validity. “Verified” can repair task defects through human screening, but it does not itself prove representativeness, complete tests, or professional readiness. The evolution is therefore **reference equivalence → executable function tests → time-indexed scenario plurality → repository/environment episodes**, with observer and environment risk increasing alongside realism.

**Unique insight:** executable scoring does not remove the oracle; it relocates it into tests, fixtures, sandbox versions, and allowed side effects. As the unit grows, a binary pass becomes less complete, not more authoritative.

## Cross-family conclusions

1. **Adoption rewards low-friction stable interfaces.** MMLU’s one-letter answers and HumanEval’s tests made comparison cheap. `skill-bench` should preserve a thin common trial/result interface even when tasks are heterogeneous.
2. **Successors repair different links.** MMLU-Pro evidences headroom and tested prompt stability; LiveCodeBench evidences timestamped renewal and scenario heterogeneity. Neither establishes professional validity.
3. **Difficulty and freshness are interventions.** Filtering for hard items and rotating recent tasks change the population. Report form/version/window separately; never splice scores into an unqualified trend.
4. **Exact and executable graders have opposite blind spots.** Exact choice scoring is reproducible but process-poor. Tests admit alternative implementations but only observe encoded consequences. Both need observer-coverage claims.
5. **Resource policy is part of the construct.** Few-shot/CoT prompts and pass@k sampling budgets can reverse comparisons. Model, prompt, sample budget, selector, harness, and feedback policy are trial identity.
6. **Breadth labels are not work sampling.** Subjects and contest platforms do not license occupation, workflow, handoff, or readiness claims.
7. **Public release changes role.** A benchmark can begin as capability evidence and become training/calibration material. Release time, model cutoff, form membership, and rerun time are separate clocks.

## Concrete transfer to skill-bench

### Retain

- a common, cheap administration/result envelope;
- deterministic checks where consequences are fully observable;
- alternative-valid-path semantics rather than witness imitation;
- subject/domain/scenario slices without pretending they are representative;
- full prompts, outputs, component hashes, resource budgets, and scorer code;
- explicit calibration and uncertainty rather than one macro score.

### Repair

- bind every check to the consequences and evidence views it can observe;
- separate task-bank frame, selected form, execution environment, and inference population;
- version difficulty filters, model-assisted filtering, grader fixes, and rolling windows;
- keep factual correctness, reasoning/process evidence, artifact quality, safety, and handoff usability separate;
- report one-shot reliability separately from best-of-k opportunity;
- require environment health and side-effect boundaries for repository/terminal tasks.

### Test

1. **Renewal bridge test:** retain frozen anchors plus candidate rotating forms; estimate item/form drift before claiming longitudinal improvement.
2. **Observer falsification:** plant artifacts that pass selected checks while violating an omitted professional consequence, and valid alternatives that differ from the witness.
3. **Resource-profile curve:** report quality/reliability against calls, tokens, time, and feedback rather than one unconstrained score.
4. **Cross-unit transfer:** test whether gains on question/function units predict source-rich artifact and handoff tasks; assume no transfer until observed.

## Reproducibility and operational realism

All four papers are locally preserved and searchable. Current official releases were inspected at exact commits, but their snapshots are later than the paper versions and include mutable model adapters/results. MMLU/MMLU-Pro are inexpensive to reproduce but depend on prompt/parser details and public data. HumanEval/LiveCodeBench require safe execution; the latter additionally requires a pinned data version and explicit time window. None supplies realistic organizational state, stakeholder interaction, source authority, or downstream handoff evidence. Their primary value to `skill-bench` is measurement machinery and lifecycle warning—not direct construct coverage.

## Next actions

No new queue task is warranted. Existing task-health, metric, validity, execution-isolation, artifact-view, and handoff work already represent the requirements. The immediate canonical change is to add these two evolution chains to the landscape/synthesis indexes and require rolling-form bridge evidence before longitudinal claims.
