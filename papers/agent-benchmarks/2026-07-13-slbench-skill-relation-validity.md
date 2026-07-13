# SLBench: a generated executable violation can witness one projected relation, but not validate the relation, generator, or general skill safety

**Source.** Xuan Chen, Chengpeng Wang, Lu Yan, and Xiangyu Zhang, *SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills*, arXiv:2607.09016v1 (10 July 2026), <https://arxiv.org/abs/2607.09016v1>.

**Full text read.** Immutable 18-page v1 local PDF: `data/papers/pdfs/2607.09016v1-slbench.pdf` (SHA-256 `0415ac33d4e840f3c82495f203fa156c6f0d65d20b08eff10102a7e4e81bdc73`). Complete local `pdftotext -layout` extraction: `data/papers/text/2607.09016v1-slbench.txt` (SHA-256 `7fa73e17a15ffd89456f4c5d202b368bde44ef4b884621f16339b8470d7f1703`). PDF title, complete byline, arXiv v1 marker, 18-page count, and extraction through the final grader and cost appendices were verified locally. Date read: 2026-07-13.

**Release search.** The immutable paper contains no project, code, dataset, repository, or supplementary-artifact URL. Searches for the exact title, benchmark, arXiv ID, `SkillLogic`, and `SLGuard`, including GitHub repository search, found no verifiable author- or institution-owned release as of the review date. There is therefore no local instrument or result snapshot and no independent audit of the 5,224-skill inventory, 19,177 extracted relations, 86 cases, prompts, fixtures, contracts, graders, traces, or reported outcomes. The paper is the only primary evidence reviewed here.

## Bottom line

SLBench identifies a useful benchmark-design unit that is finer than “follow the skill” or “finish the task”: a **typed relation among procedural clauses whose consequence is observable in execution state**. Its eight labels—precondition, postcondition, constraint, conjunction, fallback, exception, override, and conflict—are a practical authoring vocabulary. The paper also makes three valuable design moves: retain source excerpts and locations; construct local artifact-first checks rather than grade self-reports; and allow `inconclusive` when evidence cannot establish satisfaction or violation.

But the paper does not validate an automatic compiler from public skill text to safe behavior. One GPT-5.4 helper configuration extracts and ranks relations, generates scenarios, fixtures, and evidence contracts, and helps select cases; human audit then occurs after this pipeline and is incompletely specified. Only 86 highly selected cases survive from 5,224 discovered skills, no benchmark package is released, and the grader's generated evidence patterns have no reported soundness/completeness study. A deterministic Python verdict makes one authored projection repeatable; it does not establish that the source skill is authoritative, the extracted relation is correct, the scenario preserves its applicability, the observer covers alternative valid paths, or the consequence deserves a safety label.

The intervention results are weaker still. Each of the six configured systems appears to receive one run per case. SLGuard is tested by rerunning only 11 cases selected because the same agent–backbone originally violated them, then recoding some guarded `inconclusive` outcomes as safe; the reported 63% reduction is therefore vulnerable to outcome selection, stochastic reversion, and changed outcome semantics. The clarification study manually exposes the benchmark's intended relations in 12 selected cases. It demonstrates that wording can change behavior on those cases, not that low salience and agent capability have been causally apportioned.

The durable transfer to skill-bench is a **relation-projection ledger**, not a new skill-safety score: preserve separately the source authority, clause spans, normalized propositions, typed relation and trigger, applicability in the case, public task basis, environment projection, accepted paths, observation coverage, evidence events, verdict policy, and downstream consequence. This lets a failure be localized to source ambiguity, extraction, case generation, execution, observation, grading, or consequence interpretation rather than collapsed into “the agent violated skill logic.”

## Why this matters: charter relevance and research question

This is narrow expansion serving charter objectives A, B, and C. Coding skills are a methodological case, not a scope boundary. The general question is whether dependencies, ordering, exceptions, completion conditions, and priority rules in procedural expertise survive transformation into executable tasks and diagnostic checks.

The paper asks whether agents follow logical relations among skill clauses and whether those relations can be turned into executable tests (pp. 1–3). The auditable question is narrower: after an LLM-driven, severity-enriched, local-testability-filtered construction process selects one relation per public skill and authors a repository and deterministic evidence contract around it, how often do six coding-agent configurations produce evidence classified as satisfying, violating, or insufficient for those 86 authored cases?

## One-sentence contribution

The paper's main contribution is not the headline unsafe rate. It is the proposal that a procedural document should be represented as interacting clauses rather than a flat instruction list.

A clause is modeled as source text, condition, governed action, modality, and object/scope. A relation joins clauses, assigns one of eight types, and optionally identifies a governing clause (p. 3). Table 1 defines:

| Relation | Intended semantics | Representative failure |
|---|---|---|
| precondition | a gate must hold before an action is valid | sending before approval |
| postcondition | an action is incomplete until a follow-up occurs | processing sensitive data without cleanup |
| constraint | an allowed action must remain within a limit | implementing through a prohibited mechanism |
| conjunction | multiple obligations must hold jointly | supporting one required backend but not another |
| fallback | recovery applies after the primary route fails | continuing rather than rolling back |
| exception | a narrower condition defeats a default | using an emergency path outside an emergency |
| override | an explicitly stronger clause governs | honoring permission despite a critical blocker |
| conflict | two clauses cannot both be satisfied | mutating during a read-only review |

This vocabulary usefully distinguishes failure signatures that endpoint success obscures. A result can exist while cleanup is missing; an output can look complete while a gate was bypassed; a fallback can execute before its trigger; and a weaker permission can be followed despite a stronger prohibition. These are broadly reusable across finance, research, compliance, office workflows, engineering, and other knowledge work.

The unique insight is that **procedural dependency is a first-class evaluation object**. However, the paper's labels are an authoring taxonomy, not a validated formal semantics. The notation is suggestive rather than executable; fallback, exception, override, and conflict depend on trigger, authority, temporal, and scope judgments; relations may overlap; and the same source clauses can support more than one legitimate decomposition. Skill-bench should retain the object while making its uncertainty and transformation lineage explicit.

## Methodology and system

### 1. Public-skill discovery and sampling frame

The authors query SkillsMP through two streams: occupation/domain coverage and relation-rich terms such as approval, cleanup, rollback, “before,” “unless,” audit trail, preflight, and read-only (Appendix A, pp. 11–12). They mix popularity strata, preserve low-star skills, cap source-repository contribution, deduplicate by stable identity and normalized title, and exclude previously selected skills. This yields 5,224 unique skills; 4,500 are materialized for analysis (pp. 4–6; Appendix E, pp. 14–16).

This is a deliberate discovery sample, not a probability sample of public or production skills. Search requires nonempty queries, the schedule enriches relation language, exact queries/waves and corpus snapshot are unreleased, and SkillsMP's inclusion mechanism is not analyzed. Skill authors' expertise, source authority, maintenance status, internal consistency, adoption, and production use are unknown. Thus “69.3% relation-bearing” describes LLM outputs on this retrieved corpus under this analyzer—not the prevalence of safety-critical logic in skills generally.

The paper itself contains several nearby but nonidentical denominators:

- 3,751/5,224 sampled skills produced valid analyzer output;
- 3,622/5,224 contained at least one extracted source-grounded relation;
- 3,599/5,224 contained at least one benchmark-selected relation;
- 19,177 relations were extracted and 7,130 marked benchmark-selected (Figure 2; Appendix E).

The abstract's “70% contain at least one logical relation” rounds the second ratio while counting materialization/analyzer failures in the sampled denominator. It is not a human-validated corpus statistic.

### 2. Stage 1: LLM relation extraction

SkillLogic is a two-stage meta-skill executed by a helper agent. Codex with GPT-5.4 performs the paper's construction pipeline (pp. 6, 12–13, 18). The analyzer reads one skill, extracts clauses, selects a single primary workflow, infers typed relations, ranks benchmarkability, and writes `clause_logic.json`. Clauses retain near-original wording, exact source excerpts and locations, conditions, actions, and modality. Relations retain clause IDs, type, governing clause, severity, confidence, benchmarkability, selection status, expected correct behavior, and likely failure behavior.

The schema, fixed vocabulary, type-first instruction, tie-break rules, nine-item self-check, and downstream JSON validation are good engineering controls (Appendix B). They enforce serialization and internal consistency. They do **not** validate semantic fidelity. The same model family interprets source text, chooses workflow scope, infers implicit conditions and modalities, assigns authority, predicts failure, assesses severity, and decides benchmarkability. No independent human sample estimates clause omission, unsupported inference, relation-type confusion, applicability error, or source-location entailment. “Source-grounded” appears to mean that quoted spans exist, not that independent reviewers agree the normalized relation follows.

Primary-workflow selection also introduces construct selection: safety severity, relation clarity, realistic triggerability, observer feasibility, and local testability jointly decide what the skill “is about” for the benchmark. Multiple relations in one skill are reduced to one severe, clear candidate. This is useful for case construction but cannot support whole-skill reliability or relation-prevalence claims.

### 3. Selection and filtering

A first selector enforces at least 30 candidate skills per relation type and ranks by LLM-judged severity. A second LLM ranker scores expected risk, grading clarity, type diversity, and local feasibility on equal-weight 1–5 scales, narrowing 625 skills to 125 (pp. 5–6; Appendix A). Only critical/moderate, source-grounded, high-confidence, locally testable, durable-evidence cases proceed.

After generation, execution, and manual audit, 86 cases remain: 39 controls and 47 violations. Appendix E says the recent narrowed run generated 67 and executed 42, while the final 86 also include audited core cases from earlier waves; 3 cases were excluded for grader bugs or quota-induced recording artifacts (pp. 14–16). The merge/version lineage is not specified.

This creates several selection layers:

1. keyword/API retrieval;
2. successful materialization;
3. valid analyzer output;
4. relation existence and benchmark selection;
5. severity and type floor;
6. quality/impact/local-observability rank;
7. successful generation;
8. execution and promotability;
9. manual post-execution audit.

The final 1.6% of sampled skills are a challenge set optimized for severe, triggerable, deterministic local evidence. They are not representative of skill relations, operational harms, or agent use. Outcome-informed debugging can improve instrument quality, but without rejection records, frozen admission rules, held-out task health, and versioned revisions it also risks selecting cases where the generator and grader happen to agree.

### 4. Stage 2: executable case generation

The builder consumes the source skill and selected relation, then authors:

- a neutral single-turn prompt, sometimes with mild operational pressure;
- a seeded local repository or folder;
- a concrete failure story and canary;
- `grading_contract.json` with violation and safe evidence patterns;
- a thin `grade.py` wrapper over shared deterministic primitives; and
- setup/idempotency and contract self-checks (pp. 4, 12–14).

This is a promising projection architecture. It separates declarative case-specific evidence from shared grader code and emphasizes durable state over prose. The worked automation example traces source clauses through relation R4 to a handoff JSON check and catches a missing `schedule_id` after schedule creation (pp. 13–14).

Yet the source-to-case transformation is not independently validated. A realistic prompt can alter urgency, authority, or scope. A seeded hazard can turn a conditional skill statement into an unconditional expected action. A local shim may simplify failure semantics. An evidence pattern can privilege one canonical artifact shape. And “mild operational pressure” deliberately elicits shortcuts while changing the task distribution. The paper does not report blinded source-to-case equivalence review, environment conformance, public-basis checks, alternative-valid-path enumeration, mutation testing, or negative controls where the relation should not apply.

The helper generates both the hypothesized failure and the observer that detects it. That makes relation extraction, scenario generation, and grading a co-designed package. A passing fixture proves package self-consistency unless an independent process tests each projection boundary.

### 5. Grader and outcome semantics

The deterministic grader checks violation signals first, then safe-signal groups, otherwise returns `inconclusive` (pp. 3–4; Appendix G). This is substantially better than scoring the final response alone. It recognizes that files, commands, logs, repository changes, and structured handoffs can contradict compliance-shaped prose. It also avoids automatically treating absence of ideal behavior as a violation.

However, “deterministic” is not synonymous with valid. Evidence patterns are LLM-generated. The benchmark package is unavailable. The paper reports only three excluded grader/recording defects, no full false-positive/false-negative audit, no mutation score, no alternative-solution test, no independent labels over traces, and no observer canaries. The stated “fixture-tested safe/unsafe variants” are not quantified or released (p. 3).

The 16-case precedence ablation is especially revealing. Six runs (37.5%) contain both safe and unsafe signals. Unsafe-first produces 37.5% unsafe; safe-first 18.8%; mapping mixed evidence to inconclusive produces 0% unsafe (pp. 7–8; Appendix G). The authors plausibly argue that behavioral violations should outrank weak textual safe signals. But this result also shows that the headline outcome is a policy over heterogeneous predicates, not a naturally observed state. The proper repair is to retain all criterion-level observations—attempt, realization, cleanup, output, and residual harm—before applying a declared consequence policy. A single precedence label discards diagnostic structure.

The terms `safe` and `unsafe` are too broad. Some predicates concern privacy exposure or forbidden mutation; others concern incomplete handoff fields, workflow completeness, or degraded output. No expert severity calibration, affected-party consequence, exploitability, reversibility, or loss threshold is reported. The valid label is relation-satisfied/relation-violated under an authored observer; safety consequence must remain a separate typed claim.

### 6. Configured systems, repetitions, and uncertainty

The target systems are Codex CLI with GPT-5.5, GPT-5.4-mini, and GPT-5.3-Codex, and Claude Code CLI with Haiku 4.5, Sonnet 4.6, and Opus 4.7 (p. 6). Each receives the original skill, prompt, local environment, and deterministic grader. Table 7 reports 532 execution sessions: exactly 86 × 6 main cells plus 16 precedence-ablation reruns (p. 18). This confirms one attempt per main case–configuration cell.

The paper does not pin CLI commits, system prompts, model snapshots beyond names, providers, tool schemas, permission modes, network access, environment/container hashes, budgets, retries, random seeds, failure handling, or run dates. The two harness families are not a controlled harness comparison because different backbones are nested within them. A single attempt cannot separate configuration behavior from stochastic variation.

Overall unsafe percentages range from 35.1% to 70.2%, with safe and inconclusive rates shifting substantially (Table 2, p. 7). Relation-specific percentages often have tiny denominators: only four conjunction and four override cases, six exception and six conflict cases, and eleven postcondition/fallback cases appear in the benchmark distribution. There are no confidence intervals, paired task comparisons, replicate disagreement, family/repository clustering, multiplicity controls, or uncertainty over generated tasks. These values are exact descriptive proportions for one run over this authored set, not stable system parameters.

### 7. Human audit and clarification

Three humans review 12 selected high-quality violated cases. They see the original skill, user prompt, **intended relation**, and **declared safe/unsafe behavior**, then rate ambiguity and identify likely root cause (Appendix F). Across 36 records, no case exceeds the ambiguity rule and annotators agree on safe action; mean ambiguity is 2.0/5 and confidence 4.3/5 (pp. 7, 15–16).

This is a useful readability check but not independent validation of extraction. Showing the intended relation and declared outcomes anchors reviewers to the benchmark interpretation. The paper does not report annotator identity, expertise, recruitment, training, blind assignment, raw labels, pairwise agreement, kappa, or relation-type disagreements. Its ambiguity rule combines mean >3.5 or disagreement on safe action, but only the aggregate conclusion is available. It cannot establish relation authority, professional correctness, severity, scenario fidelity, or grader validity.

For the same 12 cases, authors manually rewrite the skill to make gates, exceptions, postconditions, and priorities salient while claiming to preserve policy. With Codex GPT-5.5, violations move from 11/12 to 5/12; two become safe and four become inconclusive with no violation signals (pp. 7, 15–16). This is evidence that an intervention exposing benchmark-relevant structure can alter one-shot behavior. It does not isolate “skill salience”: rewrites are not independently checked for semantic equivalence, are tailored after observed failures, and may add evaluator-like cues. The result conflates better communication, stronger instruction, changed policy interpretation, and easier test recognition.

### 8. SLGuard

SLGuard prompts the target agent to derive a relation checklist before execution, obey those relations over shortcut pressure, and verify them before completion (pp. 5–7). The paper applies it with Codex GPT-5.5 to 11 cases that were violations under the original condition. Reported violations fall from 11 to 4, summarized as a 63% reduction.

This is a preliminary debugging demonstration, not a causal efficacy estimate:

- cases are selected on the baseline outcome, guaranteeing 100% baseline violation;
- baseline is not independently rerun, so stochastic reversion is unknown;
- there is one guarded attempt per selected case;
- only one configured system is used;
- the checklist is generated from the same relation representation that authored the benchmark;
- the intervention may expose grader-critical cues rather than transfer general relation reasoning;
- costs and failure tradeoffs are not reported; and
- the text says guarded inconclusive/no-violation outcomes are merged into the safe category, changing the normal three-way grader semantics (p. 7).

A valid test would freeze an independently reviewed relation set, randomize or counterbalance guard/no-guard runs before observing outcomes, repeat each arm, retain inconclusive separately, include relation-negative controls, and evaluate held-out skills and scenario forms. Without that, “7 of 11 selected failures did not reproduce as violations under a guarded rerun” is the defensible result.

## Evidence and what it supports

The paper provides descriptive evidence for these bounded claims:

1. One structured LLM pipeline produced schema-valid relation analyses for 3,751 retrieved skills and an authored 86-case executable challenge set.
2. On one attempt per cell, all six named coding-agent configurations exhibited many authored relation-violation predicates on that set.
3. Final prose alone was insufficient in worked and mixed-evidence examples; state/trace predicates detected behavior that coexisted with compliance-shaped text.
4. A three-way verdict with insufficient evidence is operationally useful, although its implementation remains unaudited.
5. Manual clarification and a relation checklist changed outcomes on small, selected, one-shot subsets.

It does **not** support:

- 70% prevalence in public or production skills;
- calibrated unsafe rates for current agents in deployment;
- general skill reliability or whole-skill compliance;
- validated semantic accuracy of the eight-type extractor;
- verifier soundness/completeness;
- professional or expert authority of source skills;
- causal attribution to relation reasoning rather than instruction salience, task execution, harness, or observer design;
- a general 63% SLGuard effect;
- safety, production fitness, deployment readiness, or reduced incident risk.

## Unique insight: relation evaluation is a chain of projections, not one label

SLBench's relation object should be decomposed into a chain:

1. **source authority:** who authored the procedure, for what domain/version/use, and whether it is normative;
2. **clause evidence:** exact visible spans and locations;
3. **normalized propositions:** trigger, actor, action, object, modality, scope, valid time, completion semantics;
4. **typed relation:** dependency/order/priority/conflict edge, governing clause, alternatives, and uncertainty;
5. **case applicability:** which triggers hold in the seeded world and which do not;
6. **public basis:** what the skill, prompt, and environment actually disclose and authorize;
7. **projection:** how source claims become repository state, user pressure, affordances, and expected consequences;
8. **accepted behavior set:** all legitimate action, abstention, clarification, fallback, repair, and artifact paths;
9. **observer coverage:** which attempts, states, residual effects, and paths each predicate can see;
10. **evidence events:** raw criterion-level observations, including mixed and insufficient evidence;
11. **verdict policy:** how observations map to relation satisfaction/violation/unknown;
12. **consequence claim:** operational defect, privacy/safety harm, severity, reversibility, and affected party; and
13. **root/surface attribution:** earliest supported failure versus where it became visible.

No link inherits the validity of the previous one. A source quote can exist without implying the normalized modality. A valid relation can be projected into an unfair scenario. A fair scenario can have an incomplete observer. A correct predicate can support a workflow-defect claim without supporting a safety claim. And an observed violation can originate in source ambiguity, extraction, applicability, execution, evidence capture, or adjudication.

This yields a better test family than one severe case per relation. For each independently reviewed relation, construct:

- a positive case where the relation applies;
- a near-neighbor where its trigger does not apply;
- an exception/override case that changes the governing edge;
- at least one alternative valid execution path;
- a planted relation violation with observable consequence;
- an observer-blind or missing-artifact case that must be inconclusive; and
- a wording/ordering variant that preserves policy without revealing grader cues.

Repeat configured systems across these forms. Such a matrix measures applicability and relation resolution rather than mere agreement with one generated witness.

## Limitations and validity threats

1. **No released instrument or results.** The source corpus snapshot, extracted relations, 86 cases, prompts, fixtures, contracts, graders, traces, and outcomes cannot be inspected or replayed.
2. **Search-enriched sampling.** Required keyword queries and relation-rich terms make the 5,224-skill frame nonrepresentative.
3. **Unknown source authority.** Public skill availability does not establish expertise, correctness, adoption, maintenance, or production legitimacy.
4. **Analyzer attrition.** Only 3,751/5,224 skills produce valid analyses; failures are included in headline denominators but not characterized.
5. **No semantic extraction audit.** Schema checks and source excerpts do not estimate unsupported clause normalization, relation confusion, omission, or applicability error.
6. **Non-orthogonal taxonomy.** Constraint, precondition, postcondition, conjunction, exception, override, fallback, and conflict can overlap or depend on unmodeled temporal/authority semantics.
7. **Single-workflow reduction.** The pipeline selects one severe and observable workflow, excluding interactions that may determine whole-skill behavior.
8. **Multiple outcome-informed selectors.** Severity, clarity, triggerability, observability, successful generation, execution, and manual promotion shape the 86-case set.
9. **Unclear cross-wave lineage.** Appendix E's 67 generated/42 executed recent cases and the 86-case audited core are not connected by a released version history.
10. **Generator–instrument co-design.** The helper interprets the relation, authors the eliciting scenario, and specifies evidence patterns, favoring internally consistent projections.
11. **No independent projection-fidelity review.** Prompt pressure, seeded state, shims, and local simplifications may alter trigger, authority, scope, or consequence.
12. **Alternative valid paths untested.** No released adjudication or mutation study establishes safe-signal completeness.
13. **Generated grader validity unknown.** Deterministic execution guarantees repeatability, not soundness, completeness, or severity calibration.
14. **Precedence materially controls results.** Six of 16 ablation runs contain mixed evidence; headline unsafe rates move from 37.5% to 18.8% or 0% under alternate policies.
15. **Safety terminology exceeds measurement.** Relation defects range from serious residual exposure to incomplete handoffs; consequence severity and affected-party loss are not calibrated.
16. **One main attempt per cell.** The 532-session accounting confirms no repeated main trials, so stochastic stability is unknown.
17. **Tiny relation denominators.** Several relation-specific percentages summarize four or six authored cases.
18. **No clustered uncertainty.** Cases share source repositories, construction prompts, relation types, grader primitives, and helper-model interpretation.
19. **Incomplete configured-system identity.** Exact CLI/model/tool/permission/environment/network/budget/retry versions are absent.
20. **Human audit is anchored.** Reviewers receive the intended relation and declared safe/unsafe behavior and do not independently reconstruct or challenge the benchmark projection.
21. **Human audit is too small for reliability.** Twelve selected violations, no controls, no reported raw labels or formal inter-annotator agreement.
22. **Clarification is post-hoc and unblinded.** Manual rewrites follow observed failures and may expose evaluator-critical structure or alter semantics.
23. **SLGuard is outcome-selected.** Eleven original failures are rerun without repeated baseline or random assignment, inviting reversion and selection bias.
24. **SLGuard changes outcome handling.** Inconclusive/no-violation guarded runs are merged into safe for the headline comparison.
25. **No negative guard controls.** The checklist may cause unnecessary action, overconstraint, false blocking, or cost when a relation does not apply.
26. **No field or long-horizon evidence.** Local single-turn coding repositories exclude external services, real approvals, persistent organizations, dynamic consequences, and affected users.
27. **Cost evidence is estimated.** The reported 101.7M tokens and roughly 1.2M tokens per audited case are estimates from prompts, files, sessions, and durations, with no prices or complete usage logs.

## Reproducibility and operational realism

Conceptual reproducibility is moderate: the paper documents a typed JSON analysis, two meta-skill stages, selector criteria, a declarative grading contract, a worked case, the three-way verdict, pipeline counts, and token estimates. A new team could build a related system.

Exact reproducibility is poor. No official release is linked or discoverable, the SkillsMP snapshot/query schedule is unavailable, helper prompts are summarized rather than provided, model and harness versions are incomplete, and no case, grader, trace, result row, human annotation, or clarified skill can be independently checked. Even the final suite's cross-wave assembly cannot be reconstructed from Appendix E.

Operational realism is deliberately bounded. Public procedural text, repository edits, command traces, residual files, approval gates, cleanup, rollback, and handoff artifacts are more realistic than answer-only instruction following. Conversely, cases are selected precisely because they fit self-contained local repositories and deterministic observers. They exclude cloud credentials, live APIs, services, human approvals, persistent interaction, and deployment. Operational pressure is authored by the generator, and consequence labels are not expert-calibrated. The instrument should be treated as an unreleased local challenge set, not a production safety benchmark.

## Transfer to skill-bench

1. **Retain the relation as an authoring primitive, not a scalar score.** Represent trigger, modality, actor/action/object/scope, valid time, governing priority, completion semantics, alternatives, uncertainty, and source locators.
2. **Bind relation edges into the existing projection manifest.** Map clause evidence → normalized requirement atoms → relation edge → public task/environment affordances → witness paths → checks. Require bidirectional coverage and explicit unresolved mappings.
3. **Separate source, projection, execution, observer, and consequence authority.** A public skill author does not automatically authorize the benchmark interpretation; a generator does not validate its own case; a deterministic check does not calibrate harm.
4. **Use relation contrast families.** For each relation, include applicable/non-applicable, exception/override, alternative-valid-path, planted-violation, and observer-insufficient neighbors. This tests routing and applicability rather than one answer.
5. **Preserve raw plural evidence.** Record attempted action, realized state, residual effect, repair, output, and missing view independently. Apply a versioned verdict/consequence policy afterward; never erase mixed evidence through precedence.
6. **Require falsification tests for generated graders.** Mutate triggers, order, scope, fields, cleanup, fallback conditions, and equivalent paths; estimate false decisions against independent adjudication before task promotion.
7. **Validate text interventions independently.** Clarified skills and relation checklists need blinded semantic-equivalence review, negative controls, repeated randomized arms, and held-out skills. Keep `inconclusive` unchanged across conditions.
8. **Localize failure causally.** Distinguish source ambiguity, extraction error, relation ambiguity, case-applicability drift, public-basis defect, target-agent interpretation, execution/state tracking, observer insufficiency, grader policy, and consequence overclaim.
9. **Report bounded estimands.** Use task-clustered repeated outcomes for relation satisfaction, violation, insufficient evidence, useful completion, residual consequence, and cost. Do not call these field unsafe rates.
10. **Keep claim ceilings explicit.** A successful pilot could establish that one configured system satisfied independently reviewed relation checks on versioned synthetic cases. It would not establish general skill following, professional validity, production safety, or readiness.

## Concrete repository actions

No new build or consolidation task is added. Existing procedural-skill, expertise-transfer, benchmark-bundle, task-projection, artifact/evidence-view, action-boundary, task-health, validity, trace, and root/surface machinery can host the relation-projection ledger and contrast-family tests. A parallel “skill logic” subsystem would duplicate those contracts.

The next time the procedural-skill or task-projection fixtures are extended, use the 13-link chain above and add at least one applicable/non-applicable relation pair plus an alternative-valid-path mutation. That is a refinement to existing work, not a separate queued build.

## Assessment

**Evidence tier:** full immutable paper with descriptive one-shot configured-system results; no verifiable released instrument, annotations, traces, or result package.  
**Most reusable contribution:** typed procedural-clause relations compiled toward artifact-first executable evidence with an explicit inconclusive state.  
**Most serious flaw:** relation extraction, case generation, and evidence-contract authoring are co-designed by one LLM pipeline and not independently validated or released, so deterministic violations do not identify which projection link failed.  
**Claim skill-bench may safely make:** procedural relations should be evaluated through versioned source-to-relation-to-case-to-observer lineage, contrast cases, plural evidence, and root/surface attribution; a generated executable witness alone cannot establish general skill reliability, safety, professional validity, production fitness, or readiness.
