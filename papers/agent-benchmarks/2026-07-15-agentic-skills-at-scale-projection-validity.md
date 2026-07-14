# Agentic Skills at Scale: a skill-derived task and skill-derived judge measure shared-projection compliance, not independent utility

## Bottom line

*A Framework for Evaluating Agentic Skills at Scale* contributes a useful author-facing pipeline: turn an arbitrary Skill into task proposals, inputs, dependency requirements, two rubric families, paired no-skill/with-skill runs, and criterion-level diagnostics. Its released 1,110-task package is large and inspectable. All task-completion and instruction-following rubrics sum to 100 points, every task has a prompt and both rubric files, and the paired intervention is administered across 19 named model–harness configurations. This is meaningful infrastructure for asking whether a supplied procedure changes behavior.

The experiment does **not independently establish Skill utility**. In autonomous mode the Skill is simultaneously the source of the usage scenario, task requirements, instruction rubric, and often the facts or exact procedure needed to satisfy the task. The same pipeline then validates this co-designed package, and one uncalibrated LLM judge sees the generated rubrics, solution, and solver logs. A positive with-skill delta—especially on instruction following—is expected under this shared projection and the paper explicitly acknowledges that constructional advantage. It shows that a model can consume a surfaced, task-matched document and better reproduce its projected preferences. It does not show that the source Skill is professionally correct, that the generated task represents real demand, that the goal rubric is independent of the Skill, or that the learned procedure transfers to independently authored work.

Release inspection materially lowers the claim ceiling. The paper says “approximately 500” skills and 1,000 tasks; the pinned companion release contains 608 declared top-level Skills and 1,110 tasks in 511 groups. It contains task packages but no raw trajectories, judge outputs, invalid-run ledger, configuration manifests, domain-cluster assignments, task-generation prompts, validation decisions, or aggregate result tables. The reported approximately 38,000 valid trajectories cannot be reconstructed from the release. Because the complete nominal frame is 1,110 × 19 × 2 = 42,180 cells, roughly one in ten cells is absent under the paper’s rounded accounting, yet missingness by model, harness, task, and arm is unreported.

The unique transferable insight is a **projection-independence matrix**. Skill evaluation needs separate identities and authority for: source procedure, demand evidence, task author, goal oracle, instruction rubric, grader, equivalent-form author, and release decision. “No literal rubric leakage” is only one cell in that matrix. Skill-bench should distinguish (1) shared-projection compliance, (2) independently grounded task efficacy, (3) equivalent-form procedure transfer, and (4) portfolio utility. This paper provides substantial evidence for the first and a scalable generator for authoring/calibration; it does not validate the latter three.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, C, D, and E through comparative expansion, release validation, and consolidation into existing benchmark contracts. Public coding Skills are a methodological case, not a proposal to narrow `skill-bench` to software engineering or Skill evaluation.

The general hypothesis is that procedural knowledge can be transformed into realistic tasks and diagnostic checks at scale. The uncertainty is whether success after that transformation measures useful expertise transfer or agreement among artifacts projected from the same source. Useful completion therefore requires:

1. reconstructing the source→task→rubric→trial method from the full paper;
2. auditing the immutable public release rather than relying on headline counts;
3. tracing diverse examples end to end;
4. comparing the claim with SkillsBench, LH-Bench, and SLBench; and
5. mapping repairs into existing selection, task-health, validity, projection, trace, and repeated-task machinery without creating a duplicate subsystem.

## Sources and reading record

### Immutable primary paper read in full

- Maksim Shaposhnikov, Nicolas Fortuin, Simon Stipcich, Maria I. Gorinova, Amy Heineike, and Rob Willoughby, *A Framework for Evaluating Agentic Skills at Scale*.
- Immutable arXiv v1: <https://arxiv.org/abs/2606.17819v1>; PDF: <https://arxiv.org/pdf/2606.17819v1>.
- Local PDF: `data/papers/pdfs/2606.17819v1-agentic-skills-at-scale.pdf` (10 pages; SHA-256 `b453c44a3bd4ff243f2577a1c877c8d450d9699c06d6a3fb17b74477cd0757a7`).
- Complete layout extraction: `data/papers/text/2606.17819v1-agentic-skills-at-scale.txt` (SHA-256 `598255ed63c0e23fbf156ca6053a83f1f31cb10025629069183d27ff3a273d88`).
- Version read: v1, submitted 16 June 2026; read 15 July 2026. The full paper was read through the final references. No withdrawal notice was present in the inspected metadata.

### Official dataset inspected

- Paper-linked Hugging Face dataset: <https://huggingface.co/datasets/tesslio/task-evals-for-skills>.
- Immutable revision: `5db85e25253204f78497c6e2832a96ed51ed912e`, reported modified 5 June 2026—eleven days before arXiv v1.
- Revision URL: <https://huggingface.co/datasets/tesslio/task-evals-for-skills/tree/5db85e25253204f78497c6e2832a96ed51ed912e>.
- Provenance: `data/sources/releases/2606.17819v1-agentic-skills-at-scale/provenance.json`.
- Complete archive: `data/sources/releases/2606.17819v1-agentic-skills-at-scale/tasks.zip` (SHA-256 `c881a0bad7ad9b613a033cc672e65eef9cba6cc3eacacce7545202cbb7552168`; 65,931,931 bytes; 27,916 archive entries and 18,508 files).
- Metadata: `data/sources/releases/2606.17819v1-agentic-skills-at-scale/metadata.csv` (SHA-256 `a486437dbb6033f265dcb684ada385ba28e7e5e977587b40fdf1f2ccc33cd84f`).
- Machine-readable review audit: `data/sources/releases/2606.17819v1-agentic-skills-at-scale/audit.json`.

The complete archive was opened and all 1,110 task directories, both rubric families, declared top-level Skill packages, score sums, reference fields, input inventories, task groups, and Skill hashes were statically audited. Three deliberately different cases were traced from task through bundled Skill content and both rubric sets: a Prompt Guard security module, a React Native Navigation implementation plan, and a multi-Skill spreadsheet/board briefing. Static inspection establishes release content and internal structure, not execution correctness or judge validity.

## One-sentence contribution

The paper provides a scalable author-facing compiler from public Skill packages to paired, LLM-judged task evaluations and shows that explicitly surfaced Skills alter projected instruction compliance across 19 configured systems, but its autonomous study co-derives demand, tasks, and measurement from the intervention and therefore measures shared-projection adherence more directly than independent task or deployment utility.

## Research question and licensed claim

The paper asks how a Skill author can determine whether an arbitrary newly authored Skill improves agent behavior. It separates four practical questions: whether the agent follows encoded instructions, whether the Skill adds unavailable information, whether goal completion improves rather than only surface behavior changes, and whether a cheaper model with a Skill can match a larger one (pp. 1–2).

The auditable question is narrower:

> After an autonomous agent pipeline infers usage scenarios from a Skill, constructs executable-looking tasks and two rubric families from the same Skill, discards packages that fail its checks, explicitly tells each solver which relevant Skill is installed, excludes infrastructure/runtime-invalid trajectories, and asks Sonnet 4.6 to grade the surviving outputs and logs, how do criterion scores differ between Skill absent and Skill present?

The paper and release support these bounded claims:

1. A single pipeline produced a large, structurally complete release of 1,110 Skill-derived task packages.
2. On the paper’s unreleased valid-trajectory set, all 19 named configurations score higher overall with the relevant Skill surfaced, with reported gains of 5.5–22.1 points.
3. Most aggregate gain is in criteria projected from Skill instructions; goal-completion scores are high in both arms and often saturate.
4. Realized adherence varies substantially across the named model–harness configurations.
5. Criterion-level differences can help a Skill author identify which disclosed conventions changed behavior.

It does **not** establish:

- utility over an independently sampled work distribution;
- correctness, authority, safety, or professional legitimacy of the public Skills;
- independent goal improvement when task demand and goal criteria were projected from the Skill;
- transfer to independently authored equivalent tasks, altered environments, or different graders;
- model-only differences independent of harness, endpoint, context, and provider;
- stable per-domain or per-Skill effects under repeated trials;
- production reliability, cost-optimal deployment, capability substitution, or readiness.

## Methodology and system

### 1. Skill collection and selection

The authors source popular Skills from a public aggregation platform, emphasizing roughly 100 well-known organizations. They download full Skill folders from original GitHub repositories, deduplicate by file content, remove malformed packages, state that only MIT and Apache 2.0 Skills are retained, and apply Snyk security checks (Section 3, p. 4). This is purposive provider/popularity sampling, not a probability sample of public Skills, installed Skills, production use, professions, or consequential tasks.

The paper calls the resulting corpus “representative” and “high-quality,” but reports no sampling frame, inclusion denominator, organization distribution, popularity threshold, repository snapshot, commit identity, maintenance check, source-author qualifications, independent correctness audit, security-check outputs, false-positive/negative study, or rejected-item ledger. “Trusted company” is a source heuristic, not evidence that each procedure is accurate, current, or professionally authorized.

The release preserves copied Skill bytes and repository-level URLs but not upstream commit/blob hashes. None of the 608 declared top-level Skill documents contains a 40-character commit hash. This prevents exact reconstruction of source identity and later drift. It also prevents distinguishing a repository’s license at acquisition from a Skill’s own metadata.

Release license evidence conflicts with the paper’s simple MIT/Apache description. Among the 608 declared top-level Skill documents, only 63 say `MIT` and 42 say `Apache-2.0` in frontmatter; 485 omit a license field, five say `Proprietary. LICENSE.txt has complete terms`, one says GPLv2-or-later, four say ISC, and the remainder use indirect labels. Missing frontmatter does not prove an upstream repository was ineligible, but the explicitly proprietary/GPL/ISC entries require reconciliation with the stated filter and dataset-level Apache 2.0 label. The dataset card partly acknowledges this by telling users to respect upstream licenses. The release should not be treated as demonstrating a clean uniform redistribution license.

### 2. Dependency engineering and construct attrition

An environment-engineering agent classifies requirements such as CLI access, network, credentials, runtimes, existing repositories, MCP servers, databases, browsers, services, and input files (Table 1, pp. 2–4). In autonomous construction, Skills requiring existing repositories, MCP, multi-turn interaction, pre-populated external state, local services, databases, or particular Git states are discarded. Authentication-dependent Skills may remain because the authors judge that a valid solution can often be written without a live key.

This is pragmatic, but it changes the target construct. The retained corpus is enriched for procedures that can be projected into self-contained file production and weakly live environments. The paper’s own Table 3 says 19.3% require an existing repository, 16.2% MCP, 7.0% multi-turn interaction, and smaller shares require stateful services, databases, browsers, and Git state; the exclusion and category accounting are not reconciled at task level. The released package contains no executable environment manifest, image digest, dependency lock, network policy, credentials contract, or solver launcher. It contains prompts, optional inputs, copied Skills, and LLM rubrics.

Static release inspection found 707 tasks with at least one input file and 403 with none. Prompts themselves mention credentials in 73 tasks, API keys in 49, browsers in 69, databases in 91, and network access in 23 (simple case-insensitive string presence, not semantic classification). Such mentions do not prove invalidity, but they show that “fully verifiable environment” cannot be inferred from directory structure. Execution evidence is needed.

### 3. Autonomous task and rubric projection

In fully autonomous mode, the pipeline lacks observed user requests and therefore infers usage scenarios from the Skill itself using a quorum of agents (Section 2, p. 2). A task generator creates up to three scenarios per Skill or Skill combination, resolves or synthesizes inputs, and writes:

- a natural-language task;
- optional input artifacts;
- a task-completion rubric; and
- an instruction-following rubric.

A quality-assurance agent checks input presence, environment satisfiability, task ambiguity, executability, and literal leakage of exact steps or rubric details. Failed tasks are discarded. The paper gives no generator/validator prompts, model identities, quorum rule, rejection counts by stage, human review rate for this 500-Skill run, independent audit sample, mutation tests, or false-accept/false-reject estimates. The paper recommends hybrid human review but describes the large study as fully autonomous.

This architecture has a crucial circularity:

`Skill content → inferred demand → task requirement → projected rubric → validation by sibling agents → solver intervention → judge score`.

Task-completion criteria cite the generated task while instruction criteria cite the Skill, but that bookkeeping does not make the goal independent. The task was itself derived from the Skill. A Skill can inject both the problem shape and the preferred solution into the benchmark without any literal rubric text appearing in the public prompt.

The release quantifies the scale of this projection. It contains 10,689 task-completion criteria (mean 9.63 per task) and 13,476 instruction-following criteria (mean 12.14), all summing to exactly 100 in each family for every task. Only 4,474/10,689 task references and 2,253/13,476 Skill references are normalized substrings of their cited source text. Paraphrase can be legitimate, but most references are not exact locators and have no file/section/line spans. Forty-eight goal criteria and 12 instruction criteria omit their expected reference field. Thus the release provides rationale strings, not a fully auditable claim-to-source crosswalk.

The format itself has small release inconsistencies: most rubrics use a `checklist` field, two use `items`, some omit `context` and `type`, and one adds `total_max_score`. All parse and sum correctly, but a reusable evaluator needs a versioned schema and validator rather than inference over adjacent shapes.

### 4. Three end-to-end release traces

#### Prompt Guard: useful procedure, unvalidated security semantics

`tessl-single-firecrawl_ai-research-skills_prompt-guard_1` asks for a Python input filter using a pretrained classifier, full-message handling, and different trusted/untrusted thresholds. The bundled Skill supplies the exact Meta model ID, imports, label index, thresholds 0.5/0.7, 512-token window, 256-token overlap, and maximum-over-window aggregation. The 16 instruction criteria then award points for those exact choices.

This is an excellent test of whether the solver copied and instantiated this Skill. It is weak security-validity evidence. No adversarial messages, model weights, executable tests, threshold calibration set, long-message counterexample, multilingual sample, or false-positive/false-negative oracle is included. A solution can receive high rubric credit for containing the projected literals without demonstrating that `check_user_input` works. The Skill itself asserts performance and hardware figures but the benchmark does not validate them. The underlying model may require mutable network access, package installation, and license acceptance. Goal completion is therefore largely code-shape attestation; instruction following is canonical-implementation matching.

#### React Native Navigation: the Skill contains the requested plan

`tessl-single-wix_react-native-navigation_rnn-codebase_2` asks for an implementation plan for `dismissAllModals()` across JS, iOS, and Android. No repository is supplied. The bundled Skill contains a “Where to Find Things” table and testing section naming the exact files and commands. The ten instruction criteria require those names: `Commands.ts`, `NativeCommandsSender.ts`, `RNNCommandsHandler.mm`, `NavigationTurboModule.kt`, `RNNModalManager.mm`, `ModalStack.java`, three exact test commands, and the `lib/` gotcha.

This cleanly measures retrieval and reproduction from the supplied Skill. It does not test whether those files exist at the relevant upstream revision, whether the proposed change is complete, whether bridge declarations differ by architecture, or whether the plan would compile. The task-completion rubric awards 100 points for valid JSON, three named layers, at least one file per layer, and two test commands. The instruction rubric supplies the substantive answer. Calling the resulting delta “goal utility” would conflate answer-bearing context with independent implementation knowledge.

#### Spreadsheet plus board briefing: style conformance exceeds professional evidence

`tessl-multi-anthropics-claude-agent-sdk-demos_0` combines a spreadsheet Skill and executive-briefing Skill to request a three-year Series B model and board memo. The prompt supplies assumptions and required sheets. The instruction rubric then requires exact formatting and document conventions projected from the Skills: blue hardcodes, black formulas, parenthesized negatives, dashes for zero, one-decimal percentages, `BOTTOM LINE` first, exact section order, owner/timeline fields, and explicit confidence labels.

This case is closer to artifact-centered knowledge work and reveals the framework’s promise. Yet no deterministic workbook parser, formula replay, accounting reconciliation, human board-readiness review, alternative-model policy, or source-provenance check is released. Sonnet 4.6 must infer all of these from artifacts and logs. Criterion compliance may improve while the financial model remains economically incoherent or the recommendations unjustified. The bundled `xlsx` Skill also declares a proprietary license, directly complicating the paper’s permissive-license claim.

Across all three cases, the generated package asks a valid narrow question—did the agent instantiate the package’s preferred procedure?—but does not independently establish that the preference is correct, useful, or complete.

### 5. Paired conditions and configured systems

Each task is attempted once per named configuration in two conditions:

- **without Skill:** task plus nominally valid environment;
- **with Skill:** same task/environment, Skill installed, and explicit notice that the relevant Skill is available.

Explicit relevance notice is a legitimate treatment when the estimand is utility conditional on perfect routing. It excludes discovery and applicability recognition from the measured system. It also gives the with-Skill arm both extra content and an evaluator-relevance cue. The paper correctly says real deployments require a separate Skill-selection study (p. 8).

The 19 rows are configured systems, not base-model estimates. Anthropic models use Claude Code, OpenAI models use Codex, several other models use Claude Code as a custom backend, and Gemini/Nemotron/Qwen use OpenHands. Model family, harness, native Skill support, prompt construction, tool behavior, provider endpoint, context window, and serving stack vary jointly. The paper reports no harness commits, Skill mounting paths, exact system prompts, environment/container hashes, network policy, budgets, timeout duration, retries, random seeds, run dates, or attempt-selection rules.

There appears to be one attempt per task × condition × configuration cell: the nominal frame exactly explains approximately 42,000 attempts, and no repetitions are described. Stochastic reliability, paired run covariance, and task-level uncertainty are therefore unknown.

### 6. Grading, aggregation, missingness, and cost

Sonnet 4.6 in Claude Code serves as the only judge for every trajectory. It sees both rubric sets, the proposed solution, and all solver logs. The paper reports manual spot-check agreement but no sample size, sampling rule, labels, annotators, blinding, agreement statistic, false-decision analysis, criterion-specific calibration, judge repeats, alternate judges, or adjudication policy. A strong judge can still share model-family preferences with the generator, reward visible effort in logs, miss artifact defects, and overfit exact canonical paths.

Each natural-language criterion is graded 1–10 and weighted to a 100-point family score. Table 4’s overall score is numerically the 50/50 average of instruction following and goal completion, although the text describes a use-case-dependent weighted average without justifying this equal mixture. A 50/50 scalar treats procedural convention and task completion as compensatory and equal by construction. It obscures whether a Skill improves the artifact, merely changes its form, or harms goal completion while raising adherence.

A trajectory is called valid when it passes, fails, or times out without infrastructure or runtime errors. Approximately 38,000 valid trajectories are reported from a nominal 42,180-cell release frame. Invalid runs are excluded from scoring, but the paper does not report counts, reasons, arm imbalance, configuration imbalance, retries, or whether invalidity depends on Skill size and loading. Excluding runtime errors may remove genuine configured-system operational failures; excluding infrastructure errors may be correct for capability estimation. Without typed reasons and a frozen policy, the estimand is indeterminate.

No confidence intervals, standard errors, task-cluster bootstrap, paired task-effect distribution, negative-effect frequency, or multiplicity control accompany Table 4 or domain analyses. Tasks are clustered within 511 groups, Skills, repositories, organizations, and generator templates; multi-Skill cases share packages; the same judge scores every cell. Treating thousands of trajectories as independent would be invalid, but the paper reports no uncertainty at any level.

Cost, runtime, and token reporting is useful but insufficient for deployment substitution. Table 4 reports condition means and shows cost can increase with Skill context. However, missing/invalid attempts, provider-specific pricing, setup costs, Skill authoring/maintenance cost, routing errors, latency tails, and quality thresholds are absent. A cheaper Skill-augmented model matching a larger model’s shared-projection score is not evidence of equivalent production value.

## Evidence and results interpretation

The central descriptive result is clear: all 19 configurations increase overall score with the relevant Skill, by 5.5–22.1 points. Instruction-following scores rise substantially; goal-completion scores are already high and generally move closer to saturation. The authors explicitly state that the overall gain is “expected by construction” because the with-Skill condition has access to the source that generated the preferred criteria (Section 5.1, p. 6). This candor is important.

The paper overinterprets the same evidence in several places:

- Small models being close to large models on the shared 50/50 score does not establish substitutability on independent work.
- A small delta does not imply a Skill “can be removed”; it may reflect failed discovery, context crowding, an invalid task, an insensitive judge, already learned behavior, or a useful procedure whose consequence is not represented.
- A large delta does not identify which part of the Skill is “doing the work” without component ablations; it identifies criteria whose score changed when the entire package and relevance cue were added.
- Domain uplift differences do not establish that workflow Skills are intrinsically better. Domain labels come from an unspecified clustering procedure, tasks and rubric observability differ, and no uncertainty or sample counts accompany Table 5.
- Attributing Nemotron/Kimi behavior to model size or training data is speculative without controlled model/harness comparisons and exposure traces.

The strongest evidence is therefore not general utility but **treatment responsiveness under a projected instrument**. That is valuable for Skill debugging and model–document compatibility. It should be named accurately.

## Unique insight: Skill evaluation needs a projection-independence matrix

The paper’s pipeline and release expose eight roles that are often collapsed:

1. **source procedure authority:** who wrote the Skill, for what version, context, and consequence;
2. **demand evidence:** observed user request/log/incident versus generator-inferred use;
3. **task projection:** how demand and procedure become prompt, inputs, environment, and difficulty;
4. **goal authority:** who determines useful completion independent of the procedure’s preferred path;
5. **instruction instrument:** which procedural consequences are measured and why;
6. **grader authority:** what evidence the judge can observe and how its decisions were calibrated;
7. **transfer author:** who constructs equivalent or changed-context forms without seeing treatment outcomes; and
8. **portfolio authority:** what real work distribution and decision loss justify aggregation.

For each evaluation, record whether each pair shares source text, model, human author, organization, outcome visibility, examples, or calibration data. This yields four progressively stronger estimands:

| Estimand | Required evidence | What it can support |
|---|---|---|
| Shared-projection compliance | Skill-derived task/rubric; matched no/with arm | Whether the configured solver follows a surfaced package on its own projected criteria |
| Independently grounded efficacy | External demand plus independent goal oracle; Skill only as intervention | Whether the package improves completion on a fixed task class |
| Equivalent-form transfer | Different task/environment/verifier authors and held-out variants | Whether the procedure generalizes beyond one projection |
| Portfolio utility | Prespecified work distribution, routing, null/harm cases, cost/loss policy | Whether deploying the package is useful for a declared population and decision |

Literal leakage checks are necessary but insufficient. A task can avoid verbatim criterion text while selecting exactly the case, output shape, implementation route, and facts that the Skill teaches. Conversely, overlap is not always invalid: when the construct is adherence to an organization’s declared convention, explicit public guidance is the legitimate basis. The matrix makes the claim conditional rather than treating all overlap as contamination.

## Comparison with adjacent benchmark families

### SkillsBench

SkillsBench uses 87 human-contributed containerized tasks, deterministic verifiers, three repeated runs per cell, and matched no-Skill/curated-Skill conditions across 18 configurations. Its main weakness is outcome-enriched task admission and task–Skill–verifier co-design. This paper scales far beyond 87 tasks and supports arbitrary author-facing generation, but replaces deterministic verification and contributor review with autonomous projection plus one LLM judge, provides no repeats, and offers less execution provenance. SkillsBench better measures package efficacy on its curated inventory; this paper better demonstrates generation throughput and criterion-level adherence diagnostics. Neither independently establishes portfolio utility.

### LH-Bench

LH-Bench’s expert-authored procedures are cross-walked to trace-visible workflow boundaries, artifact contracts, and human preferences. It provides some evidence that observable expert boundaries improve judge agreement, but its Skill intervention ablation is tiny and the same procedure can cue the measuring instrument. This paper supplies the large paired intervention matrix LH-Bench lacks, but has no demonstrated domain experts, independent artifact-quality tier, preference threshold, or judge reliability study. Combining their strengths means large matched trials with separately versioned public procedure, independent consequence checks, artifact evidence, and expert-calibrated thresholds—not using one projected 50/50 score.

### SLBench

SLBench projects typed relations among Skill clauses into executable local cases and preserves an `inconclusive` outcome, but releases no inspectable instrument and uses a highly selected 86-case set. This paper releases 1,110 task packages and broader weighted rubrics, but its graders are natural-language LLM checks rather than artifact-first relation witnesses and it has no explicit insufficient-evidence state. SLBench’s relation-projection chain is diagnostically sharper; this paper’s release and scale are stronger. Both rely on co-designed source→case→observer transformations without independent semantic validation.

## Limitations and validity threats

1. **Purposive corpus sampling.** Popular Skills from selected organizations are not a representative frame of public, installed, production, or professional procedures.
2. **Source authority is assumed.** Repository/provider reputation does not establish procedure correctness, currency, adoption, expertise, or consequence legitimacy.
3. **Upstream identity is not immutable.** Repository URLs and copied bytes are preserved, but source commit/blob hashes are absent.
4. **License evidence is inconsistent.** Explicit proprietary, GPL, and ISC Skill metadata appear despite the paper’s MIT/Apache-only claim; most Skill documents omit license frontmatter.
5. **Security filtering is unaudited.** No Snyk outputs, policy version, rejection ledger, false-decision study, or residual malicious-content audit is released.
6. **Environment filtering narrows the construct.** Stateful, interactive, database, service, MCP, and repository-dependent work is excluded or simplified.
7. **“Fully verifiable environments” are not released as such.** There are no images, manifests, locks, launcher policies, or deterministic oracles for the 1,110 tasks.
8. **Demand is inferred from the intervention.** In autonomous mode the Skill substitutes for observed user intent, making task relevance self-confirming.
9. **Task, instruction, and often goal are co-projected.** The Skill influences both treatment and measurement even without verbatim leakage.
10. **Generator and QA independence is unspecified.** Agent identities, prompts, quorum, rejection counts, review rates, and model-family overlap are absent.
11. **Most references are paraphrases, not locators.** Only 2,253/13,476 instruction references are normalized Skill substrings, and no line/section locations are supplied.
12. **Task groups induce dependence.** The 1,110 tasks belong to 511 groups, with up to four variants sharing a Skill or collection.
13. **Multi-Skill treatment is composite.** There are 259 multi-Skill tasks with two to five declared packages; effects cannot be assigned to one Skill without factorial or component ablation.
14. **Nested Skill content exceeds top-level identity.** Nineteen additional nested `SKILL.md` names occur inside declared packages and are not represented as top-level metadata components.
15. **Explicit relevance cue changes the intervention.** Results estimate utility conditional on surfaced relevance, not automatic routing or ordinary installed-Skill use.
16. **Configured systems are bundled.** Model, harness, native support, provider, endpoint, context, and tools vary together.
17. **No repeated trials.** One apparent attempt per cell cannot characterize stochastic reliability or paired effect uncertainty.
18. **Invalid-run missingness is opaque.** Roughly 38,000 valid trajectories are reported from 42,180 nominal cells, with no typed arm/configuration/task ledger.
19. **Single uncalibrated judge.** No raw labels, agreement sample, alternate judge, repeated grading, artifact mutation, or criterion-level error study is released.
20. **Judge evidence view may be insufficient or biasing.** The judge sees solutions and all logs, but no declared distinction among intended action, realized artifact, execution evidence, and self-report.
21. **Natural-language checks are not executable verification.** Many criteria assert exact files, behavior, formulas, or security properties without released tests.
22. **Goal completion is not independent.** The generated task itself embeds Skill-derived scenarios and requirements.
23. **Equal aggregation is unvalidated.** Instruction and completion are combined 50/50 despite distinct constructs and consequences.
24. **No uncertainty analysis.** There are no task-clustered intervals, paired effect distributions, negative-effect rates, domain sample counts, or multiplicity controls.
25. **Domain clustering is under-specified.** Embeddings/model, cluster selection, assignment reliability, and task counts behind Table 5 are absent.
26. **Mechanism claims are speculative.** Training-data gaps, model size, and Skill utilization are inferred without exposure or component evidence.
27. **Cost substitution is not decision-valid.** Mean scenario cost excludes routing, failures, authoring, maintenance, latency tails, and independently calibrated quality thresholds.
28. **Release/result mismatch.** The task release is inspectable, but raw trajectories, scores, invalids, configuration manifests, and result tables are absent.
29. **Paper/release counts differ.** “Approximately 500/1,000” in the paper corresponds to 608/1,110 in the pinned release; exact table denominators are not bound to a manifest.
30. **Professional validity is absent.** No expert sampling, human completion baseline, artifact acceptance study, threshold calibration, or field outcome supports professional or deployment claims.

## Reproducibility and operational realism

Instrument inspectability is moderate to strong. The full immutable paper, pinned dataset revision, 1,110 prompts, optional inputs, copied Skill folders, and 2,220 rubric files are available. The release’s task grouping, declared Skill/repository identities, score sums, and criterion text can be independently inspected. A researcher can replay a selected task with a new solver and implement a compatible LLM judge.

Exact paper reproduction is poor. Missing components include source repository commits, collection/filter logs, generator and QA prompts/configurations, task rejection history, environment images, harness/model snapshots, trial manifests, raw solver outputs/logs, judge prompts beyond the high-level description, judge decisions, invalid-run reasons, domain assignments, and aggregate result snapshots. Proprietary historical model endpoints and provider behavior add time dependence. The paper’s results cannot be recomputed from the released artifact.

Operational realism is mixed. Inputs include notebooks, PDFs, code, spreadsheets, documents, and multi-artifact requests; costs and runtimes are reported; and the framework explicitly considers environment dependencies. Yet autonomous filtering favors self-contained artifacts, many checks grade code/document shape rather than running consequences, live services and stakeholder interaction are largely excluded, and no human acceptance threshold exists. The benchmark is best treated as a **large generated procedural-compliance instrument**, not a validated sample of consequential work.

## Transfer to skill-bench

1. **Add projection independence to existing provenance, not a new schema.** For every task/check/intervention record the source author, generator, task author, goal-oracle author, instruction-rubric author, grader author, shared models/sources/examples, outcome visibility, and review state.
2. **Type the estimand before running.** Label a generated Skill-derived case `shared_projection_compliance`; do not upgrade it to task efficacy, transfer, portfolio utility, capability, or readiness without the corresponding independent evidence.
3. **Separate demand from procedure.** Prefer observed requests, incidents, expert critical cases, or independently authored task families. If the Skill is the only demand source, preserve that fact as a construct limitation.
4. **Keep goal and instruction evidence separate.** Do not combine them 50/50 by default. Require an independently grounded goal oracle and decision-loss argument before claiming utility.
5. **Use generated packages for calibration, then freeze independent confirmation.** Autonomous generation can cheaply expose missing inputs, brittle criteria, and routing assumptions. Confirmatory tasks should be authored or reviewed without treatment outcomes and should include null and harmful-Skill cases.
6. **Build equivalent-form families across projection boundaries.** Change scenario author, inputs, environment, accepted path, and verifier while preserving the procedure class. Measure whether the Skill helps across those forms rather than only variants generated alongside it.
7. **Require artifact-first falsification.** For code, spreadsheets, and security modules, add executable tests, mutation cases, alternative valid implementations, missing-evidence states, and human adjudication where deterministic checks cannot establish professional quality.
8. **Preserve typed invalids and full cell inventories.** Report infrastructure, dependency, provider, harness, timeout, malformed-output, missing-artifact, and judge-invalid outcomes separately. Freeze retry and replacement policy before seeing condition outcomes.
9. **Repeat and cluster correctly.** Repeat within task/configuration/arm, estimate paired task effects, bootstrap over task groups or independent Skills, and report negative/null effect rates—not only trajectory-weighted means.
10. **Evaluate routing as a separate intervention.** Compare not installed, installed-but-unsurfaced, auto-routed, explicitly surfaced, and exact-section-surfaced conditions. Preserve availability→discovery→read→application→verified-consequence traces.
11. **Bind release identity.** Pin upstream Skill commits/blobs, full package tree hashes including nested Skills, licenses, security-policy/report hashes, generator/validator identities, environment digests, and result manifests.
12. **Human-calibrate consequential artifacts.** A criterion-compliant board memo, security module, or implementation plan is not professionally acceptable by default. Use independent experts, threshold decisions, disagreement records, and consequence-specific validity arguments.

## Concrete repository actions

No new build or consolidation task is added. The repository already has independently versioned intervention/instrument components, task-projection manifests, source/authority lineage, task-health selection history, artifact-view admissibility, validity arguments, metric specifications, trace exposure chains, and a blocked repeated cross-pilot matrix. The evidence should refine those objects rather than create a parallel “Skill utility” contract.

When the repeated cross-pilot matrix is unblocked, include one generated shared-projection case and one independently authored equivalent form under the same Skill. Freeze all task/check artifacts before outcomes; run no-Skill, installed-unsurfaced, and explicitly surfaced arms; retain every invalid; and compare goal completion, instruction compliance, artifact quality, and cost separately. That bounded contrast directly tests the uncertainty this paper exposes.

## Assessment

- **Evidence tier:** full immutable primary paper plus complete pinned task-package release and repository-local static audit; no released raw trajectories, judge decisions, validity labels, or exact experiment manifests.
- **Most reusable contribution:** scalable author-facing conversion of a Skill into dependency analysis, paired task conditions, two rubric families, and criterion-level behavioral diagnostics.
- **Most serious flaw:** autonomous construction uses the Skill to infer demand, author the task, and derive measurement, so positive deltas—especially instruction-following deltas—primarily establish shared-projection compliance under one unvalidated judge.
- **Claim skill-bench may safely make:** generated Skill-derived evaluations are useful calibration instruments when labeled as such; independent utility requires external demand, independent goal evidence, equivalent forms across authoring boundaries, repeated paired trials, typed missingness, calibrated graders, and explicit portfolio/decision validity.