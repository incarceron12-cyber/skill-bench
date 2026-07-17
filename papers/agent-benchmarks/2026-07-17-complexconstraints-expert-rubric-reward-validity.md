# Paper Review: ComplexConstraints — Expert Rubrics as Measurement and RL Reward

- **Paper:** https://arxiv.org/abs/2606.09118v3
- **Authors:** Sushant Mehta, Liudas Panavas, Suhaas Garre, Edwin Chen
- **Date read:** 2026-07-17
- **Venue / source:** arXiv preprint; accepted to the GEM workshop at ACL 2026
- **Version read:** immutable v3, updated 4 July 2026
- **Local PDF:** `data/papers/pdfs/2606.09118v3-complexconstraints-and-beyond-expert-rubrics-for-rlvr.pdf` (11 PDF pages; SHA-256 `cc10bf23f29b145de1b510c2209f2e793d6ec5dfa78953f700556b10c82636bf`)
- **Local text:** `data/papers/text/2606.09118v3-complexconstraints-and-beyond-expert-rubrics-for-rlvr.txt` (SHA-256 `faa00965c62c90575463de935c8d9126b25ca2ef9b4ec3fdb18a52af87f9f226`)
- **Official dataset inspected:** https://huggingface.co/datasets/surgeai/ComplexConstraints/tree/e9625c6f635f42b72cb85a04c2be64746f945126 (CC-BY-4.0, revision `e9625c6f635f42b72cb85a04c2be64746f945126`)
- **Release provenance:** `data/sources/releases/2606.09118v3-complexconstraints/provenance.json`
- **Evidence status:** deep review of the full immutable paper and complete public benchmark surface; release-audited, but training, judge-calibration, CoreCraft, checkpoint, and run artifacts are unavailable
- **Tags:** expert-rubrics, RLVR, intervention-instrument coupling, instruction-following, judge-calibration, reward-validity, transfer

## One-sentence contribution

ComplexConstraints argues that expert-written, adversarially judge-calibrated criteria can serve both as a fine-grained instruction-following instrument and an RL reward, and reports large same-family and external pre/post gains from two single-seed training cases; its public 75-task release makes the benchmark criteria inspectable, but the missing training corpus, calibration labels, grader, checkpoints, run ledger, and CoreCraft implementation prevent reproduction and leave expert authority, judge reliability, reward causality, and professional validity unestablished.

## Why this matters for skill-bench

This source directly tests charter principle 6, **intervention/instrument separation**. The same family of criteria defines what counts as success, supplies the optimizer's reward, and—on the held-out ComplexConstraints split—measures the reported improvement. That loop can be productive: criterion-level feedback provides far denser credit assignment than whole-task pass/fail. It is also epistemically dangerous: improvement can mean learning the intended capability, the criterion-writing style, the judge's decision boundary, or a compensatory score topology.

The paper's strongest evidence is therefore not “rubrics transfer expertise.” It is a bounded demonstration that one rubric-conditioned training package was followed by higher scores on its own criterion family and on four independently named evaluation families. External gains weaken a pure memorization explanation. They do not identify which rubric-design choice caused the gain, validate the source criteria as professional ground truth, establish artifact or environment consequences, or show reliable benefit over repeated seeds and configurations.

For `skill-bench`, the reusable design lesson is to preserve a typed chain:

`authority-bearing requirement → criterion projection → observer evidence view → reward transform → optimizer exposure → frozen same-instrument measurement → untouched transport measurement → artifact/state consequence → permissible capability or readiness claim`.

A score increase licenses only the links actually observed.

## Research question and claim boundary

The paper asks whether expert-curated criteria designed for semantic and pragmatic instruction following can be both (1) a more expressive measurement instrument than narrow programmatic constraints and (2) a useful RLVR reward in fixed single-turn tasks and stateful enterprise-agent environments.

The evidence supports these bounded claims:

1. The public release contains 75 unique single-turn prompts and 1,559 non-empty criteria.
2. The paper describes a three-stage expert authoring/review pipeline and a local positive/negative judge-calibration procedure.
3. In one reported Qwen3-4B training run, mean held-out per-criterion pass rate increased from 57.9% to 73.4% on a 10% split of the unreleased 1,000-task companion corpus (Table 3, p. 6).
4. The same trained checkpoint reportedly improved on AdvancedIF and MultiChallenge under their external protocols (Table 4, pp. 6–7).
5. In a second single-epoch GLM 4.6/CoreCraft case, held-out CoreCraft and three external tool/agent benchmark scores reportedly increased (Table 5, p. 7).

The evidence does **not** establish the correctness or completeness of the criteria; calibrated human–judge reliability; independent effects of expert authorship, atomicity, intent restatement, density, difficulty targeting, or adversarial calibration; repeated-seed reward learnability; a causal advantage over another reward; transfer of domain expertise; professional artifact quality; safe stateful execution; deployment readiness; or economic value.

## Version and release audit

The arXiv API records v1 on 8 June, v2 on 22 June, and v3 on 4 July 2026 under the same title, **ComplexConstraints and Beyond: Expert Rubrics for RLVR**. Temporary full-PDF comparisons found that v1 and v2 were 10-page PDFs while v3 is 11 pages. The core ComplexConstraints, CoreCraft, +15.5 pp, single-seed, and external-agent claims already appear in earlier versions. V3 materially expands reporting: it adds the MultiChallenge results, explicitly states the 90:10 split, and adds a Data Availability section and public dataset link. Thus v3 improves disclosure rather than representing the exact evidence surface available at initial submission.

The ACL-facing “Complex-IF” naming seen in discovery metadata should be treated as title/catalog drift; the immutable arXiv versions inspected here all use ComplexConstraints. More important is release drift in substance: the pinned Hugging Face revision predates v3 and contains only a README and one benchmark CSV. Its card still has placeholder repository/citation fields, says year 2025, and names `ComplexConstraints_Benchmark_Set.csv`, while the actual sibling is `ComplexConstraints_benchmark_set.csv` (`README.md`, lines 14–18, 37–61). These defects do not invalidate the CSV, but they show that the release is a benchmark surface, not a synchronized reproduction package.

Absent from the pinned release are the stated disjoint 1,000-prompt training set; expert identities, qualifications, assignment, disagreements, and adjudications; explicit/implicit and objective/subjective criterion labels; reference responses; criterion calibration pairs and verdicts; judge prompt/code/version; CoreCraft environment and reward implementation; checkpoints; model and harness configurations; task-level outputs; training curves; external-evaluation records; and analysis code (`provenance.json`, release boundary).

## Methodology and system reconstruction

### Expert authoring and authority

The public and training sets are described as scratch-authored by a “workforce of domain experts.” Each prompt follows draft authoring plus a reference response, rubric authoring against that reference, independent second-expert review, and senior adjudication on disagreement; a frontier-model pilot tunes difficulty (Section 4, pp. 4–5).

This is a plausible task-design workflow, but “expert” is not operationalized. The paper reports no contributor count, qualifications, domain-to-person assignment, recruitment, training, compensation, task time, rejected items, revision counts, disagreement rate, adjudication examples, or conflict controls. Reading several model responses before restating user intent (Section 3.2, p. 3) also makes rubric authoring outcome-conditioned: it can clarify pragmatic intent, but it can tune requirements to the sampled systems' failures. The evidence supports reviewed **rubric-authoring authority**, not demonstrated professional authority for scheduling, employment law, medical filtering, donor analysis, education, or the other task settings.

### Public task and criterion structure

The paper says ComplexConstraints contains a disjoint 75-task public benchmark and 1,000-task training set, each with 10–40 criteria per prompt (median 19). It describes criteria as labeled explicit/implicit and objective/subjective and tasks as involving multi-step, conditional, planning, or unstated constraints (Section 4, pp. 4–5). The training mix is reported as business writing 39%, scheduling 22%, data categorization 11%, personal plans 10%, numeric processing 7%, creative writing 6%, and extraction 4%.

The public CSV exposes a thinner contract: task ID, prompt, one `use_case`, one `instruction_type`, one `prompt_style`, and 40 positional criterion columns. It has no stable criterion IDs, source or authority locators, criterion labels, polarity, required/bonus/penalty role, applicability predicate, dependency relation, evidence-view requirement, example type, weight, gate, or version hash.

A complete static audit of all 75 rows and 1,559 criteria found:

- seven use-case labels, dominated by Logistics/Scheduling/Event Planning (34/75) and Data Processing/Formatting/Math (22/75); Professional/Workplace Communication has 10, Education 6, and Health, Technical Design, and Creative Writing only one each;
- one task-level instruction label per task: Negative 22, Multistep 20, Conditional 19, Implicit 14—even though individual tasks visibly combine these properties;
- criterion counts of 10–40, median 19, matching the paper and card;
- median criterion length 22 words, mean 30.0, maximum 553;
- 285 criteria with a simple example marker, 547 containing “and,” 369 containing “or,” 98 containing an obvious conditional marker, 363 containing a negative marker, and 809 containing a number, currency sign, percentage, or quoted string;
- no exact duplicate criterion text.

These lexical counts are diagnostics, not semantic labels. They nevertheless falsify any inference that “1,559 criteria” means 1,559 uniformly atomic, independent bits. CIF-047 criterion 5 is a 553-word exclusion list of hundreds of patient IDs. CIF-023 criterion 1 embeds an ordered 20-plus-event answer key. CIF-033 criteria reproduce an entire excursion menu. CIF-013 criteria 17 and 20 substantially overlap the same camera specification. CIF-041 distributes a transformed 40-book answer across many criteria. Such criteria can make judging easier, but they vary radically in information content, combine multiple predicates, reveal answer structure, and induce dependence.

The public suite is therefore a dense **criterion inventory**, not evidence of criterion atomicity, equal information, fair hidden obligations, or a validated scale. Its two largest categories comprise 56/75 tasks; “realistic professional use cases” denotes authored scenario framing, not occupational sampling or ecological validation.

### Maximum viable atomicity and intent restatement

The paper rejects literal one-fact atomicity in favor of the “smallest meaningful unit” (Section 3.1, pp. 3–4). This is a sound warning: splitting a coupled professional consequence can reward individually correct but jointly incoherent pieces. The term is not operationalized, however. No splitting rule, dependence graph, human reliability study, or comparison of granularities is reported. The release shows both reasonable narrow checks and extremely large answer-bearing blocks.

Authors also inspect model responses and restate the user's “what” and “why” before writing criteria (Section 3.2, p. 3). This may recover pragmatic intent. It may equally add an analyst's preferred interpretation. No contributor read-back, user confirmation, public-basis audit, or alternative-valid-interpretation record distinguishes inferred intent from an undisclosed obligation. `skill-bench` should preserve intent hypotheses but not silently promote them to hidden scored requirements.

### Judge calibration and evidence view

For every criterion, the author reportedly hand-grades a reference response, checks agreement with an LLM verifier, revises ambiguous wording, edits the response so the correct verdict flips, and confirms the verifier flips (Section 3.3, p. 4). Factual answer keys are embedded in criteria to turn judge recall into verification. This positive/negative contrast pattern is valuable and directly transferable.

It is not a reliability study. One author-created positive and one adversarially edited negative can test local sensitivity, but does not estimate specificity over legitimate alternatives, repeated-call stability, criterion-family error, severe false acceptance, or transport to new responses. The paper reports no human duplication, adjudication, confusion matrix, prevalence, uncertainty, calibration-set separation, judge prompt, or retained evidence/rationale. GPT-5-mini produces per-criterion judgments during both ComplexConstraints and CoreCraft training (Section 5.3, pp. 5–6), but the paper does not clearly establish that it is the verifier used in every authoring-calibration step or fully specify the judge configuration.

Embedding answer keys reduces unsupported judge recall while increasing criterion answer-bearing and the risk that a reward model learns evaluator anchors. A local verdict flip shows observer responsiveness, not criterion authority or construct preservation.

### Reward topology

The general reward partitions required, bonus-only, and penalty-only criteria and averages each group separately, with coefficients α and β for bonus and penalty terms (Equation 1, p. 6). ComplexConstraints sets α = β = 0, so its reward is simply the fraction of required criteria judged satisfied. The public release does not expose these roles, and the paper does not report experiments with asymmetric shaping.

Dense partial credit is the paper's central mechanism: 28/30 receives more reward than 15/30. But uniform criterion averaging assumes that each criterion contributes a comparable increment and ignores dependencies, prerequisites, vetoes, contradictions, applicability, and information size. Splitting one requirement into multiple correlated criteria increases its reward leverage. Conversely, a severe failure can be compensated by many presentational successes. The all-criteria task-pass statistic is noncompensatory, but it is not the training reward and is a different estimand from mean per-criterion pass rate (Table 3 note, p. 6).

Most importantly, the reward observer and held-out ComplexConstraints measurement appear to share the same criterion family and model-judge paradigm. The reported +15.5 pp is therefore a **same-instrument gain**, not independent evidence that artifacts became professionally better.

### Fixed-task RLVR configuration

The instruction-following experiment trains Qwen3-4B (Thinking) on a 90:10 split of the unreleased 1,000 tasks: approximately 900 training tasks and 100 held-out tasks. The reward is fraction of required criteria satisfied. The paper states that external benchmarks were not used for training, hyperparameter tuning, checkpoint selection, or reward design (Section 5.3, p. 6).

No optimizer, learning rate, batch size, rollout count, token budget, epoch count, base-checkpoint hash, system prompt, sampling configuration, judge prompt, invalid/missing-reward policy, checkpoint-selection trace, held-out item identities, or training curve is provided. The authors explicitly disclose one seed and no seed-to-seed variance (Section 5.4, pp. 6–7). This is enough to describe an observed configured pre/post contrast, not to estimate a stable training effect or data efficiency.

### CoreCraft stateful configuration

For agentic training, the paper imports a CoreCraft case from Mehta et al. (2026): GLM 4.6, GRPO with decoupled clipping, 16 rollouts per prompt against stateful Docker enterprise simulations, GPT-5-mini criterion judgments, and one epoch (Sections 5.2–5.5, pp. 5–7). The paper provides no CoreCraft task inventory, criterion set, state schema, action or state observer, reward-to-environment binding, reset evidence, container image, tool surface, trajectory, checkpoint, or run ledger.

An LLM criterion judgment over a trajectory can reward narrated compliance without proving a state change unless authoritative state and action observations are joined. The authors say they qualitatively monitored verbal satisfaction and verbosity exploits and inspected a held-out pre/post subsample, finding no systematic quality degradation (Section 5.3, p. 6). The sample size, selection, reviewers, coding protocol, evidence view, and results are absent. A distinct judge model does not prevent reward hacking; it only removes one shared-model pathway.

### External evaluations

Qwen3-4B is evaluated on AdvancedIF and MultiChallenge using those benchmarks' official judges/protocols; MultiChallenge uses four runs per task. The CoreCraft-trained GLM 4.6 is evaluated on BFCL Parallel, τ²-Bench Retail, and Toolathlon under their official protocols (Section 5.3, p. 6).

Independent task authors and different graders make these results more probative than the held-out same-family result. Yet the paper does not preserve endpoint versions, exact task splits, harnesses, prompts, budgets, environment versions, retries, missing runs, raw outputs, task-level paired differences, uncertainty, or checkpoint identity. “The model never saw [them] during training” is an author statement about the explicit training pipeline, not a contamination audit. The CoreCraft results are cited to another same-organization paper rather than reproduced from released evidence here.

## Evidence and results interpretation

### ComplexConstraints same-family result

Mean held-out criterion pass rises from 57.9% to 73.4% (+15.5 pp); an untrained Qwen3-235B-A22B-Instruct reference scores 73.9% (Table 3, p. 6). “Within 0.5 pp of a roughly 60× larger model” is numerically true for this one metric, but not parameter-efficiency equivalence: architecture, training history, inference compute, cost, uncertainty, and task-level reliability are not matched.

The public leaderboard's best all-criteria task pass is 40.4% (Table 1, p. 5). This is not comparable to the 73.4% mean criterion score. Dense conjunction mechanically lowers task pass as criterion count rises; low task pass alone does not prove frontier-level construct difficulty.

### External instruction-following transport

AdvancedIF overall rises 28.2%→36.6% (+8.4 pp), while MultiChallenge overall rises 41.1%→51.2% (+10.1 pp). The largest reported slice is MultiChallenge Instruction Retention, +22.1 pp (Table 4, pp. 6–7). These changes are consistent with transport of some constraint-following behavior across task formats. With one pre/post checkpoint pair, no uncertainty, and multiple reported dimensions, they do not establish a general mechanism or its reliability. The paper itself says controlled investigation of transfer remains future work (p. 7).

### CoreCraft and external agent transport

GLM 4.6 rises 25.4%→36.8% on held-out CoreCraft, 91.0%→95.5% on BFCL Parallel, 68.7%→76.1% on τ²-Bench Retail, and 18.8%→25.6% Toolathlon Pass@1 (Table 5, p. 7). Toolathlon Pass3 reportedly rises 9.3%→17.6%, but the paper defines it as all-three success rather than a conventional pass@k estimator. These are promising configured-checkpoint observations. Without raw repeated trials or clustered uncertainty, they do not establish operational reliability, and without authoritative state evidence they do not show that rubric reward improved all consequential workflow effects.

### Claimed construct validity

Section 6 claims content, predictive, and discriminant validity (p. 8). The evidence is thinner:

- broader semantic criteria show **intended content coverage**, not content-validity agreement with a defined professional construct;
- external pre/post gains show **transport association**, not predictive validity against a future external criterion or consequence;
- a wide leaderboard spread shows **discrimination among current configured systems**, not that the differences reflect the intended construct rather than judge, criterion density, prompt length, or system access.

The paper's comparison to synthetic rubrics and RIFL uses results from different studies, models, data, and pipelines; the authors appropriately call one comparison suggestive rather than controlled (Section 5.6, pp. 7–8). It cannot identify expert authorship as the active ingredient.

## Unique insight

The paper's deepest contribution is exposing a three-way tension:

1. **Criteria must be expressive enough to represent pragmatic work.**
2. **Criteria must be legible enough for an automated observer to apply consistently.**
3. **Criteria used as rewards must be robust enough that optimization does not exploit the observer.**

Adversarial calibration tries to satisfy all three by rewriting criteria until one judge flips on a paired example. But that procedure can improve judge legibility by narrowing the criterion around answer-bearing cues. RL then optimizes against that narrowed decision surface. Thus “trainable rubric” is not automatically “valid rubric”: reward learnability and construct validity can move in opposite directions.

The appropriate claim ladder is:

- **rubric authority:** qualified people approved the requirement in scope;
- **judge reliability:** a frozen observer applies it reproducibly over representative alternatives;
- **reward learnability:** optimization changes the observed reward over repeated runs;
- **same-instrument gain:** a frozen held-out form from the same criterion process improves;
- **external transport:** untouched independent instruments improve under comparable evaluation;
- **artifact/state consequence:** authoritative outputs or states improve without collateral harm;
- **expertise transfer:** the improvement reflects expert procedures or judgment rather than evaluator cues;
- **professional validity/readiness:** performance predicts acceptable consequential work at an explicit threshold and resource envelope.

ComplexConstraints provides evidence at the same-instrument and preliminary external-transport rungs. It does not collapse the ladder.

## Limitations and validity threats

1. **Expert authority is unspecified.** Contributor qualifications, counts, scopes, and assignment are absent.
2. **Outcome-conditioned authoring is uncontrolled.** Authors inspect frontier responses and tune difficulty, potentially selecting model-specific failures.
3. **No task-population frame exists.** Authored “realistic” scenarios do not establish prevalence or occupational representativeness.
4. **The public suite is concentrated.** Logistics and data-processing labels account for 56/75 tasks; three use cases have one item each.
5. **Task labels flatten composition.** Each task gets one of Negative/Multistep/Conditional/Implicit despite mixed properties.
6. **Criterion metadata promised in prose is missing in release.** Explicit/implicit and objective/subjective labels are unavailable.
7. **Atomicity is asserted, not measured.** Criteria range from short checks to 553-word answer-bearing lists and overlapping specifications.
8. **Dependencies and applicability are absent.** Uniform averaging can double-count, compensate vetoes, and score inactive requirements.
9. **Intent restatement lacks user confirmation.** Analyst inference can become a hidden obligation.
10. **Judge calibration is local and unreported.** No retained pairs, repeated judgments, human agreement, confusion, uncertainty, or alternative-valid-answer study exists.
11. **Judge identity is incompletely bound.** GPT-5-mini is named for training judgments, but prompts, versions, parameters, and calibration identity are not preserved.
12. **Reward and measurement are coupled.** The held-out gain uses the same criterion family and likely observer paradigm used for optimization.
13. **No reward ablation isolates the mechanism.** Expert versus synthetic, calibrated versus uncalibrated, dense versus binary, intent-aware versus literal, and dependence-aware versus uniform rewards are not compared.
14. **The fixed-task training package is unreleased and underspecified.** Data, hyperparameters, checkpoints, and raw outputs are missing.
15. **Both headline training cases are single-seed.** No training variance or repeated configured-run uncertainty is available.
16. **External transport lacks paired item evidence and uncertainty.** Versions, budgets, missingness, task-level effects, and multiple-comparison accounting are absent.
17. **No contamination audit is provided.** “Never used for training” is narrower than pretraining or search-time non-exposure.
18. **CoreCraft consequence observability is unavailable.** Trajectory rubric scores cannot substitute for authoritative state/action checks.
19. **Reward-hacking inspection is qualitative and unreported.** Sampling and coding are absent, and a distinct judge model is not a robustness proof.
20. **Scale comparisons are not resource-matched.** Similar rubric scores do not establish compute, cost, or general-capability equivalence.
21. **Task-pass and criterion-pass are easy to conflate.** They have different aggregation and conjunction semantics.
22. **Construct-validity labels outrun the design.** Content intent, external score transport, and discrimination are not full content, predictive, or discriminant validity arguments.
23. **Release synchronization is incomplete.** V3 adds disclosure while the pinned dataset card retains placeholders and filename/year mismatches.
24. **Professional realism is mostly prompt framing.** Single-turn text output omits stakeholder clarification, source custody, native artifacts, review/repair, and organizational consequences.

## Reproducibility and operational realism

Reproducibility is **good for the public benchmark text and weak for every reported model result**. The immutable paper, complete benchmark CSV, exact revision, license, counts, and hashes are preserved locally. A third party can inspect the 75 prompts and write a new grader. They cannot reproduce the paper's leaderboard or training because the response corpus, rubric labels/roles, grader implementation, calibration evidence, training set, model configuration, checkpoints, and run records are absent.

Operational realism is similarly split. The prompts include dense schedules, employment-policy revisions, data transformations, workplace communication, and planning constraints that are richer than surface-format tests. Yet they remain single-turn text tasks with answer-bearing rubrics and no native spreadsheet/document state, source authority, interactive clarification, execution trace, consequential environment, recipient acceptance, or maintenance lifecycle. CoreCraft could supply stateful realism, but this paper and release do not expose enough implementation evidence to audit it.

## Transfer to skill-bench

### Retain

1. **Positive/negative criterion calibration.** For every model-graded check, preserve an author-approved satisfying witness and a minimally edited verdict-flip contrast.
2. **Dense diagnostic observations.** Keep criterion-level failures separate from whole-task gates so partial progress is inspectable.
3. **Independent transport tests.** Evaluate an intervention on untouched tasks, criterion authors, graders, and environments rather than only a same-family holdout.
4. **Explicit same-instrument versus external reporting.** Never combine them into one “transfer” number.

### Repair

1. **Bind criterion authority and semantics.** Stable criterion ID/hash, public basis, authority evidence, polarity, gate/scored/diagnostic role, applicability, dependencies, permitted alternatives, evidence view, answer-bearing examples, and licensed claim already have homes in the expertise-transfer and benchmark-bundle contracts.
2. **Separate observer calibration from reward validation.** Preserve repeated human/model labels, adjudication, per-class errors, severe-error slices, and held-out alternatives; then separately test whether optimizing the reward improves an independent consequence.
3. **Record reward topology as a configured component.** Hash criterion set, grouping, weights, invalid/missing-judge policy, aggregation, judge, prompt, and model. Any change creates a new intervention and instrument version.
4. **Require a reward-to-consequence bridge in stateful tasks.** Join criterion observations to authoritative action receipts, state deltas, collateral effects, and cleanup rather than accepting trajectory prose alone.
5. **Use clustered repeated designs.** Multiple seeds, task-level paired outcomes, repeated grader calls where stochastic, complete missing-run accounting, uncertainty, and resource envelopes are prerequisites for treatment-effect or reliability claims.
6. **Audit answer-bearing and dependence leverage.** Report effective requirement groups as well as raw criterion counts; a 553-word exclusion list and a single format check must not silently count as equivalent units.

### Test

A future procedural-skill or grader intervention should use at least four frozen measurement surfaces:

1. same tasks/same criteria with an independently calibrated observer;
2. equivalent tasks from the same domain with independently authored criteria;
3. a different domain with the same proposed latent procedure;
4. authoritative artifact/state consequences plus collateral-effect checks.

Cross these with intervention exposure, preserve task/criterion/grader/reward hashes, and predeclare the claim at each surface. A gain only on surface 1 is evaluator-package adaptation; surfaces 2–3 support bounded transport; surface 4 is required before professional-consequence claims.

## Action items for repository

- [x] Read the complete immutable v3 paper and verify section/page claims against the local PDF/text.
- [x] Audit the complete public 75-row/1,559-criterion release at pinned revision `e9625c6f635f42b72cb85a04c2be64746f945126`.
- [x] Inspect all public criteria computationally and purposively for atomicity, dependence, conditionality, answer-bearing content, and observability risks.
- [x] Audit v1→v3 title, page, reporting, and release-link changes while keeping v3 as the evidence version.
- [x] Separate rubric authority, judge reliability, reward learnability, same-instrument gain, external transport, artifact/state consequence, expertise transfer, professional validity, and readiness.
- [x] Add no queue task: the findings refine existing criterion, grader, configured-component, validity, task-health, metric, artifact/state, and longitudinal contracts; no genuinely unrepresented contract was found.
