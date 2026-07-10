# Paper Review: ClawArena — Evolving Information, Hidden Truth, and Workspace Grounding

- **Paper:** https://arxiv.org/abs/2604.04202v2
- **Authors:** Haonian Ji, Kaiwen Xiong, Siwei Han, Peng Xia, Shi Qiu, Yiyang Zhou, Jiaqi Liu, Jinlong Li, Bingzhou Li, Zeyu Zheng, Cihang Xie, Huaxiu Yao
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint
- **Version read:** immutable v2, 16 May 2026
- **Local PDF:** `data/papers/pdfs/2604.04202v2-clawarena-evolving-information.pdf` (28 pages; SHA-256 `c9b8289807b92bc9193f7857710b1b11b1af7af8fff88fb43aadcbcd36a2ac89`)
- **Local text:** `data/papers/text/2604.04202v2-clawarena-evolving-information.txt` (SHA-256 `a908c21e1cd28eab6a2aa14d619477a56684c773a425d2f26fcd8db2273a5319`)
- **Official release inspected:** https://github.com/aiming-lab/ClawArena/releases/tag/v1.0.0, commit `922f3142a3e5538f9004db7833063b74cb63d76f` (8,286 tracked files; tagged 19 May 2026, three days after v2, so not assumed identical to the paper-time implementation)
- **Later official commit inspected for timing only:** `630efd8a0d1dc8189718226c7da158cbe4c2fe64` (1 July 2026; 20,574 tracked files; not paper-time evidence)
- **Release provenance:** `data/sources/releases/2604.04202v2-clawarena/provenance.json`
- **Tags:** evolving-information, contradiction, temporal-validity, personalization, workspace-state, executable-graders, configured-systems

## One-sentence contribution

ClawArena contributes a rare persistent, ordered benchmark in which evidence arrives through sessions and mutable workspace files, with a six-layer hidden-truth construction method, staged updates, exact-set questions, executable artifact checks, and multi-framework baselines; its strongest transferable contribution is the **evidence-emission and reversal map**, while its claims about implicit personalization, reliability, framework effects, source authority, and skill-overlay improvement are weakened by explicit preference disclosure, answer-bearing feedback, prompt-level corrective hints, authored rather than validated truth, one run per configuration, order-sensitive scoring, soft keyword graders, and a public release containing truth specifications and keys.

## Why this matters for skill-bench

The paper directly addresses a charter-level construct that static source packs miss: professional evidence is not merely contradictory; it has **time, authority, scope, and state-transition semantics**. A direct message can be sincere but non-authoritative for a policy threshold; a calendar can establish that a meeting occurred but not what was decided; a later audit may supersede an earlier estimate without making the earlier estimate irrational at the time; and a file mutation can change the world the agent must act on rather than merely add context. ClawArena’s Layer 0 narrative, evidence-emission map, reversal matrix, staged update packages, and executable workspace checks are unusually concrete machinery for representing these distinctions (Section 3.3–3.4, pp. 4–6; Appendix F, pp. 20–23).

The benchmark also exposes why those distinctions cannot be reduced to one hidden answer. Its “complete hidden ground truth” is authored omniscience: writers decide which character is defensive, which legal review is superficial, and which source dominates. That makes deterministic scoring possible, but it does not establish that a domain expert, policy, or real adjudication would license those conclusions. For `skill-bench`, hidden truth should be decomposed into objective state, source claims, authority rules, valid intervals, observable evidence, permissible inferences, and unresolved judgment—not stored as one privileged narrative.

This is a narrow methodological case, not a reason to make the benchmark about personal assistants. It tests a general hypothesis across HR, healthcare, finance, security, education, retail, and research-integrity scenarios: whether agents can preserve and revise evidence-grounded state while producing inspectable artifacts.

## Research question and claim boundary

The paper asks whether persistent agents can:

1. resolve conflicts among heterogeneous sources;
2. revise beliefs after staged evidence changes;
3. infer and retain user preferences without reminders;
4. ground conclusions in workspace state as well as answer questions;
5. perform consistently across an ordered sequence; and
6. exhibit separable model, framework, and skill-overlay effects.

The evidence supports narrower conclusions. The authors built 12 synthetic multi-turn scenarios with 337 ordered rounds, 45 update-bearing rounds, and two rule-graded output modes. The release operationalizes cumulative file/session updates and contains a substantial set of inspectable scenario specs, prompts, checkers, framework adapters, and two example result reports. Configured systems differ greatly on this instrument, and the case studies plausibly show that set selection and literal artifact construction fail differently.

The study does **not** establish representative professional coverage, expert-valid hidden truth, genuinely implicit preference learning, stochastic reliability, causal model-versus-framework importance, general skill transfer, safe sandboxing, or professional artifact usefulness. It also does not isolate retrieval failure, state-update failure, judgment failure, and output-format failure in the reported scores.

## Methodology and system

### Six-layer scenario construction

Each scenario has a hidden Layer 0 narrative bible containing an objective timeline, role-specific truth gaps, contradiction map, biases, traps, and answer provenance. Agent-visible Layers 1–4 contain workspace files, session histories, evaluation rounds, and dynamic update packages; Layer 5 supplies generation/noise controls (Section 3.3, p. 5). Appendix F publishes seven authoring templates: execution guide, narrative bible, evidence-emission map, workspace spec, session spec, evaluation/reversal spec, and update spec (pp. 20–23).

The paper distinguishes four evidence relations: factual conflict, authority conflict, genuine agreement, and temporal/process conflict. It also distinguishes integration from conflict reasoning, and stages subjective session updates separately from objective workspace mutations (Section 3.3, p. 5). Seeds are hand-authored, generalized into a meta-specification, batch-generated under claimed empirical distribution constraints, and filtered through structural, semantic, and control checks. The authors report catching 37 specification errors and retaining 12 refined scenarios (Section 3.4, pp. 5–6).

This is useful design machinery, but the validation is internal. The paper provides no author counts, domain qualifications, independent adjudicators, agreement, expert/novice trials, rejection totals, or evidence that the synthetic legal, clinical, finance, HR, and security judgments match professional practice. “Over 200 published empirical distributions” constrain message timing, contact frequency, and noise—not the validity of substantive domain decisions. Realistic communication volume cannot validate an authored labor-law conclusion.

The release makes the construction logic unusually auditable. In the wrongful-termination example, Layer 0 explicitly declares the objective truth, role motives, source ranking, reversal triggers, and intended shallow failures. That transparency is valuable for authoring. It also shows that “ground truth” includes contestable mind-reading—for example, legal counsel is declared to be managing reputational risk—and therefore mixes objective event state with author interpretation.

### Ordered updates and evidence availability

All rounds in a scenario share one persistent agent session and workspace. Before a round, the runner applies its listed updates; later rounds therefore inherit earlier file/session changes. The release implements `new`, `append`, `insert`, and `delete` actions and records target paths and channels. This is materially richer than a static long-context prompt.

However, the released round records contain only `update_ids`; they do not carry claim-level validity intervals, source authority, supersession semantics, or expected belief transitions. The paper’s 14-category taxonomy is also not encoded in the released `questions.json`: computational inspection found zero of 337 rounds with a taxonomy/category/dimension field. The taxonomy can diagnose only through an external mapping that is not preserved in the primary evaluation records.

The paper says set-selection questions present 7–9 candidates (Section 3.1, p. 3; Section 3.5, p. 6), but Appendix Table 9 reports mean 6.38, minimum 5, maximum 10 over the 95 released questions (p. 19). The release matches the appendix, not the stated 7–9 range. This is minor operationally but evidence that headline task-shape claims need executable validation.

### Question formats, feedback, and artifact grading

The 337 released rounds exactly match the paper’s 95 multi-choice and 242 executable-check split. Multi-choice requires exact set match; IoU, precision, recall, and F1 are recorded but do not score. Executable checks run fixed shell commands against the mutable workspace and score the exit code, with optional stdout matching (Section 3.5, p. 6; Appendix D, p. 17).

The artifact channel is valuable: it can verify JSON shape, files, scripts, dates, exact values, and workspace state that a prose judge might miss. But release inspection substantially narrows the “workspace grounding” claim:

- There are 327 scenario checker scripts; 324 inspect file existence, 258 use substring/regex-style checks, 111 parse JSON, only one uses Python AST parsing, and none implements a domain-expert semantic adjudicator.
- Many report graders reward filenames, headings, required tokens, and presence of dates or names. These are useful conformance checks, not evidence that a legal, clinical, finance, or security artifact is professionally sound.
- The checker runner invokes `subprocess.run(..., shell=True)` on the host with the workspace merely as `cwd`. Agent-authored scripts are executed by some checks. A timeout is not a filesystem, process, credential, or network sandbox. The paper’s “sandboxed shell command” wording (Appendix D, p. 17) is therefore not demonstrated by the closest release.
- Preference checks in a separate `pref` field do not affect score; they only generate corrective feedback. Twenty-one rounds instead embed `check_preferences.py` directly in the main eval command. Thus preference scoring semantics vary by round and are not represented as a separate score family.

There are concrete fair-basis defects. In wrongful-termination round q3, the prompt says the `c_type` field is optional (“看你要不要加”), while the released failure feedback says the checker requires `c_type`. The hidden check therefore imposes a literal obligation the public instruction explicitly makes optional. The same scenario’s Layer 0 defines Chinese-style names such as `2026年03月_主题.md`, while release questions/checkers require an ISO `YYYY-MM-DD_` prefix. These are not expert traps; they are instrument contradictions.

### Personalization is mostly disclosed, not inferred

The paper describes four stages ending in silent exams with no preference reminders (Section 3.3, p. 5). The release does contain 24 rounds with typed preference checks. Yet every initial workspace includes a startup instruction to read `USER.md`, and the inspected HR scenario’s `USER.md` explicitly states all five preferences: hierarchical bullets, Chinese-convention naming, executive summary first, qualitative/quantitative balance, and warm professional tone. Round q4 directly asks the agent to retrieve those profile preferences. Later tasks often say to follow the team convention and feedback supplies exact correction rules.

This measures profile retrieval and compliance under intermittent prompting, not inference of latent preferences solely from corrections or interaction patterns. “Silent” means the current prompt omits a reminder while an explicit profile remains available. A valid personalization claim needs arms that independently vary explicit profile access, demonstration/correction history, and silent retention.

### Feedback changes the evaluated system

Every one of the 337 released rounds has non-empty correctness feedback. The runner injects detailed feedback from round *t* before round *t+1*. For missed multi-choice options it names the missing option and explanation; for executable failures it often lists exact required paths, fields, dates, and values. The benchmark is therefore an online assisted trajectory, not a sequence of independent capability probes.

That can be legitimate if the construct is correction uptake. But the reported TCR and CRS do not separate initial ability, exposed answer information, repair learning, and transfer to genuinely new evidence. Later rounds often ask for artifacts containing facts already disclosed by earlier grading feedback. Task order is fixed, no no-feedback arm is reported, and no equivalent-form transfer set tests whether the lesson generalizes rather than leaks the scenario key.

### Configured systems and experimental design

The paper evaluates 18 models and four base harnesses, with MetaClaw treated as a fifth skill-driven overlay. Cross-model comparisons use OpenClaw except that Anthropic models use Claude Code and are correctly labeled non-comparable. Cross-framework comparisons hold the model fixed within GPT-5.1, GPT-5.5, and Kimi-K2.5 blocks (Section 4.1–4.3, pp. 6–9).

Each configuration appears to be run once over the full ordered benchmark. The paper reports no repeated trajectories, seeds, confidence intervals, paired uncertainty, hypothesis tests, provider-time controls, or failure/missing-run policy. A range of observed point estimates cannot identify whether “model capability dominates framework design”: the compared model set and framework set differ in composition and support, ranges are sample-extreme statistics, and model/framework interactions are visibly large. The paper itself notes that Claude Code is worst for GPT-5.x but best for Kimi-K2.5 (p. 9), undermining a simple main-effect ranking.

The benchmark is also extremely imbalanced in context burden. Appendix E reports that `hil_s1` contributes 91.7% of all authored tokens, while the other 11 scenarios share 8.3% (pp. 19–20). Scenario-macro averaging prevents that case from dominating the score, but compute, context-pressure, and framework effects are dominated by it. This should be treated as a distinct stress stratum, not as ordinary variation around one population.

### Skill-overlay ablation

Four matched baseline/MetaClaw pairs add a skills overlay over OpenClaw. Reported CRS gains are 0.33–1.19 points, with TCR changes from 0 to 0.59 points (Table 5, p. 9). The release includes 36 generic skills and a config with template retrieval and `auto_evolve: true`. The inspected source-evaluation skill is an 18-line generic CRAAP checklist; it is not a domain procedure derived from ClawArena experts.

No repetition, uncertainty, fixed retrieval log, injected-skill trace, skill-version hash, no-op-length control, independently authored rubric, or held-out task transfer is reported. The improvement can be one or a few changed binary rounds, prompt/context effects, online feedback uptake, or service variation. “Reliably improves” is unsupported. At most, the point estimates show no aggregate TCR decrease in these four one-run package comparisons.

## Evidence and results interpretation

The paper’s descriptive tables show substantial configured-system variation. The strongest OpenClaw model has TCR 78.34 and CRS 68.28; the lowest reported OpenClaw model has TCR 54.10 and CRS 38.82 (Table 3, pp. 7–8). Under fixed models, framework ranges are also large and highly model-dependent (Table 4, p. 8). MC and EC can diverge, supporting the useful claim that exact set reasoning and literal artifact construction expose different surface failures.

The release includes complete example reports for GPT-5.5/OpenClaw and Gemma-4-31B/OpenClaw. The GPT-5.5 example records 75,936,741 tokens and 16,403,957 ms over 337 rounds, but no immutable environment lock or raw model-provider snapshot establishes exact reproduction. The paper does not report dollar cost, repeated-run variance, grader false-pass/false-fail rates, expert quality, or human review burden.

The error analysis is case-study evidence, not a coded failure study. Ten selected option-level examples motivate six patterns, but selection criteria, independent coding, denominator counts, and inter-rater agreement are absent (Section 4.5 and Appendix G, pp. 9, 24–28). “Belief revision difficulty is governed by update design rather than update volume” is inferred from clustered anecdotes, not a controlled manipulation or regression with uncertainty.

## Unique insight

ClawArena’s deepest transferable idea is not its CRS or leaderboard. It is an **evidence-state transition contract**:

`world/event state → source-specific claim emission → authority/scope/valid-time rules → agent-visible evidence state → expected belief delta → consequential artifact/check`

This is better than treating contradiction as a pair of incompatible strings. It distinguishes:

- **static contradiction:** two contemporaneous claims disagree;
- **temporal supersession:** a later valid claim retires an earlier state;
- **conditional applicability:** both claims can be true under different populations, policies, or intervals;
- **authority conflict:** one source can establish occurrence but not approval or legal sufficiency;
- **non-conflict synthesis:** consistent facts jointly imply a consequence no source states;
- **workspace-state error:** the agent’s artifact fails to reflect the current file state;
- **retrieval failure:** relevant evidence existed but was not accessed;
- **belief-update failure:** evidence was accessed but the stale conclusion persisted; and
- **preference-state failure:** an applicable convention was available but not used.

The paper contains pieces of this chain, but its hidden narrative collapses them into one “objective truth,” and its released traces do not record access, adoption, belief state, or claim-level transitions. `skill-bench` should preserve the chain explicitly so a final wrong report is not automatically labeled a reasoning failure.

A second insight is negative: **ordered correctness streaks are not reliability unless order itself is a validated stochastic unit**. CRS assigns half its weight to streak geometry. The paper’s own worked example gives different CRS values to two permutations with the same 60% TCR: alternating `[1,0,1,0,1]` scores 0.300, while `[1,1,1,0,0]` scores 0.488 (Appendix D, pp. 17–18). Because rounds are deliberately grouped by scenario phase, update timing, feedback, and difficulty, CRS rewards the authored ordering and outcome clustering. It is not repeatability, calibration, or robustness to perturbation.

## Limitations and validity threats

1. **Synthetic breadth is not ecological validity.** Twelve generated scenarios do not establish prevalence or consequence in any profession.
2. **Ground truth mixes events and interpretation.** Motives, credibility, and legal sufficiency are author-declared without expert adjudication.
3. **Domain expertise is not documented.** Author qualifications, domain reviewers, agreement, labor, and expert/novice baselines are absent.
4. **Empirical distributions validate surface statistics only.** Message timing and noise do not validate professional decisions.
5. **The 14-category taxonomy is not in released round records.** Diagnostic mappings cannot be audited from results alone.
6. **Task-shape claims conflict.** The text says 7–9 options; Appendix Table 9 and release span 5–10.
7. **Preference information is explicit.** `USER.md` lists the preferences the paper describes as implicitly learned.
8. **Preference semantics vary.** Separate preference checks do not score, while 21 checks are embedded in main pass/fail commands.
9. **Detailed feedback leaks task information forward.** All rounds can alter later performance through answer-bearing feedback.
10. **No no-feedback or reset arm exists.** Initial capability, learning, correction uptake, and transfer are confounded.
11. **Prompts often name sources and correct distractors.** Some tasks test instruction following more than source discovery or authority judgment.
12. **Private checks sometimes add or contradict obligations.** The optional `c_type` and naming-convention examples violate public-basis fairness.
13. **Most executable graders are syntactic.** Keyword/date/header presence does not establish professional artifact quality.
14. **No checker calibration is reported.** False passes, false failures, legitimate alternatives, and adversarial artifacts are unmeasured.
15. **The shell checker is not demonstrated as sandboxed.** Host subprocess execution with a workspace cwd is an operational and safety gap.
16. **One run cannot establish reliability.** There are no replicate trajectories or uncertainty estimates.
17. **CRS is permutation-sensitive.** It measures authored streak geometry, not repeatability across equivalent trials.
18. **CRS equal weights are unvalidated.** TCR and SC×FD are averaged without stakeholder loss or decision evidence.
19. **Model/framework range comparisons are not causal.** Support differences, sample composition, and interactions dominate the observed extrema.
20. **Anthropic model rows use a different harness.** The paper labels this, but the headline “18 models” still spans incomparable treatments.
21. **Context burden is extremely skewed.** One scenario accounts for 91.7% of input tokens.
22. **Update volume is not experimentally manipulated.** The update-design conclusion is anecdotal and endogenous to scenario content.
23. **Error analysis is selected and uncoded.** No sampling rule, denominators, or coding reliability support prevalence claims.
24. **Skill gains are tiny single-run differences.** No uncertainty, retrieval trace, no-op control, or held-out transfer supports “reliably.”
25. **Public release leaks instrument internals.** Narrative bibles, answer keys, checkers, feedback, and task descriptions expose hidden truth and exact values.
26. **Top-level metadata itself leaks answers.** `tests.json` descriptions include values such as the 40-vs-60-day PIP and 20-day shortfall.
27. **Release timing is not paper identity.** v1.0.0 postdates v2 by three days; the larger inspected commit postdates it by six weeks.
28. **Professional consequence is absent.** No stakeholder uses an output, and no downstream harm, decision quality, or expert acceptance is measured.

## Reproducibility and operational realism

Reproducibility is strong for inspecting the instrument’s structure and weak for reproducing its headline study. The immutable paper, full extracted text, official v1.0.0 archive, later pinned archive, hashes, complete question corpus, 327 checker scripts, scenario authoring specs, adapters, scoring code, tests, and example reports are locally provenance-recorded. This review read the complete paper; inspected the core runner, scoring, update, question, preference, and checker code; computationally audited all released question records and checker scripts; and traced one full HR scenario from Layer 0 through updates, prompts, checks, preferences, and report output.

Exact evaluation requires mutable commercial models and APIs, several rapidly changing harnesses, large token budgets, credentials, and framework-specific state layouts. The paper does not provide container digests, exact dependency locks, request/response traces for all configurations, seeds, repeated runs, provider snapshots, or a paper-time commit. The release tests software behavior but does not reproduce all paper tables from immutable raw records.

Operational realism is mixed. Persistent sessions, hundreds of messages, mutable files, updates, heterogeneous channels, irrelevant noise, structured deliverables, and long cumulative interaction are closer to knowledge work than isolated QA. Conversely, synthetic omniscient truth, explicit preferences, answer-bearing feedback, heavily specified prompts, deterministic keyword checks, public keys, and no demonstrated outer sandbox make the environment less realistic as evidence of autonomous professional judgment.

## Transfer to skill-bench: concrete changes

1. **Add claim-level evidence-state transitions to existing source-pack and trace records.** For each claim atom, record source, authority predicate, scope, valid interval, observed time, evidence locator, confidence, contradiction/supersession links, and expected belief delta.
2. **Separate world updates from evidence updates.** A changed underlying file, a new report about an unchanged event, a correction, a retraction, and a policy-version change need distinct event types.
3. **Decompose hidden truth.** Preserve objective state, authored assumptions, expert judgment, policy rules, unresolved disputes, and permissible conclusions separately; never allow an author’s motive attribution to masquerade as fact.
4. **Add an update-to-check crosswalk.** Every reversal check should identify the prior answer, newly available evidence, changed predicate, still-valid predicates, and why revision is required. Equivalent unchanged checks should detect indiscriminate revision.
5. **Instrument evidence access and adoption.** Record which files/messages were available, accessed, quoted, and used before assigning retrieval, state-update, reasoning, or artifact-construction causes.
6. **Make feedback policy an explicit treatment.** Compare reset/no-feedback, outcome-only feedback, diagnostic feedback, and lesson/skill conditions on held-out equivalent forms. Do not pool them into one capability score.
7. **Test personalization with factorial disclosure.** Cross explicit profile access, demonstrations/corrections, retention delay, and silent query; score preference compliance separately from factual/artifact correctness.
8. **Reject order-sensitive CRS as a reliability measure.** Preserve TCR and ordered failure episodes descriptively, but estimate reliability from repeated equivalent trials, perturbations, calibration, and task-clustered uncertainty. Any sequence utility needs a stakeholder loss model.
9. **Run public-basis linting against prompts and private checks.** Detect optional fields enforced privately, conflicting naming conventions, exact values leaked in metadata, and grader requirements absent from the user-visible task.
10. **Use typed grader outcomes.** Distinguish `incorrect`, `invalid_artifact`, `insufficient_evidence`, `grader_error`, and `environment_invalid`; calibrate keyword graders with planted semantic failures and legitimate alternatives.
11. **Fail closed on executable safety.** Run agent and grader code in a pinned outer sandbox with filesystem, process, credential, and network canaries; never treat `cwd` plus timeout as isolation.
12. **Stratify context stress.** Treat the 91.7%-token outlier as a declared stress condition and report quality/cost by context regime rather than hiding it behind scenario-macro averages.
13. **Use existing contracts rather than create a duplicate subsystem.** These requirements refine the benchmark bundle, longitudinal evolution, validity argument, task health, metric monitoring, compounding lesson, execution-isolation, and artifact-admissibility work.

## Action items for repository

- [x] Read the complete immutable arXiv v2 PDF/text with section/page evidence.
- [x] Inspect the complete v1.0.0 archive at commit `922f3142a3e5538f9004db7833063b74cb63d76f` and preserve the post-paper timing boundary.
- [x] Inspect the later pinned commit only as later release evidence.
- [x] Audit all 337 question records and 327 checker scripts computationally; inspect core runner/scorer, feedback, update, preference, and shell-check execution paths.
- [x] Trace one released scenario from hidden truth through visible evidence, updates, prompts, private checks, and output report.
- [x] Separate paper claims, release observations, and `skill-bench` adaptations.
- [x] Add no duplicate queue task; map findings to existing contracts and the pending observation/leakage consolidation.
