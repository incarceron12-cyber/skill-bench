# Web, tool-use, and computer-use benchmark evolution

## Scope and evidence status

This is a full-primary-source comparative review, not an abstract survey. I downloaded and read immutable arXiv versions of GAIA, WebArena, τ-bench, OSWorld, AndroidWorld, ToolBench, API-Bank, and BrowseComp. PDFs and extracted text are preserved under `data/papers/{pdfs,text}/`; exact identities and hashes are recorded in `data/papers/web-tool-computer-evolution-provenance.json`. Existing full local reviews of AgentRewardBench and Agent Reliability Profile supply bounded successor evidence about grader observability and repeated reliability.

This advances charter objectives A, B, and D. The concrete artifact is an evolution matrix plus retain/repair/test decisions. It clarifies what interactive benchmarks add beyond static answer tests, and which realism, scoring, reliability, contamination, and maintenance claims remain unsupported. This is expansion followed by consolidation; web/API/GUI tasks are methodological cases, not a narrowing of `skill-bench` to computer use.

## Research question

What did influential web, API, and computer-use benchmarks make measurable, what weaknesses did newer designs attempt to repair, and what evidence shows that the repairs worked?

The central progression is not simply “harder tasks.” It is an expansion of the observable system:

`answer → action sequence → executable state delta → policy/user interaction → repeated outcome distribution`.

Each step repairs an earlier blind spot but introduces another: mutable environments, simulator validity, incomplete state checks, interaction confounds, and operational cost.

## Comparative evolution matrix

| Family | Construct and unit | Environment / scoring | Strength to retain | Limitation and failure signature | Newer repair and evidence | Operational realism / reproducibility | Relevance |
|---|---|---|---|---|---|---|---|
| **GAIA** (2023) | 466 tool-using, multimodal, web/file questions with short answers and three difficulty levels | Live web, files, browser/code/plugins; exact short-answer evaluation; 300 answers held back | Human-solvable generalist tasks; tool and modality composition; private answers | Final answer cannot distinguish retrieval, evidence quality, tool execution, or lucky/internal-knowledge success; live-web repeats are not identical; task-level professional consequence is absent | BrowseComp increases search depth; Agent Reliability Profile adds repeats and perturbations. These demonstrate difficulty/variance, not causal browsing quality | Easy output grading but mutable web and opaque configured-system differences; public questions become exposure material | **Tier B:** useful generalist anchor, weak artifact/workflow evidence |
| **WebArena** (2023/24) | 812 natural-language tasks over realistic websites; long-horizon navigation and transactions | Self-hosted Reddit, shopping, GitLab, CMS plus map/manual sites; programmatic URL/content/state evaluators; best baseline 14.41% vs 78.24% human | Executable, resettable websites; functional outcome rather than action imitation; multiple valid paths | Evaluators observe selected end-state predicates, not all side effects or intent; authored replicas and seeded data are not the public web; one successful state does not prove safe process | BrowserGym/AgentLab standardizes adapters and trajectories; AgentRewardBench adds expert success/side-effect/repetition labels. Its release shows evidence-view and adjudication weaknesses rather than a completed reliability repair | Public and self-hostable, but multi-site images, reset, account state, browser versions, and app maintenance are costly | **Tier A question / B evidence:** strong state architecture, bounded validity |
| **ToolBench** (2023) | Eight real software-tool task families for goal→API-call generation | Tool-specific APIs; task success; curated demonstrations and retrieval/system-prompt interventions | Executable tool feedback and concrete error analysis; intervention cost reported as about one developer-day per tool | Tiny, convenience-selected tool set; tool-specific curation and evaluator coupling; success can reward memorized format; no user interaction, policy, side-effect, or repeated reliability evidence | API-Bank expands capability decomposition and domains; τ-bench adds policy, user, database state, and repeated trials | Reproduction depends on API/service versions and bespoke wrappers; the evidence supports adaptation to eight tools, not generic enterprise tool mastery | **Tier B:** historical anchor for executable tool calls |
| **API-Bank** (2023) | 314 manually annotated evaluation dialogues/753 calls over 73 implemented APIs; call, retrieve+call, plan+retrieve+call | Reset databases; hard-coded external results; execution-equivalence call scoring plus ROUGE-L response score | Separates retrieval, planning, invocation; freezes external results; records annotation cost and rejection | The gold call chain is privileged despite alternative paths; ROUGE does not establish user outcome; synthetic implementations and eight evaluation domains limit realism; API-search behavior is scaffold-specific | τ-bench replaces call-chain agreement with final database state and adds policy/user interaction | Runnable and stable by freezing data, but stability is purchased by simulator simplification; 98 person-days for 73 APIs shows maintenance burden | **Tier B:** useful decomposition, not professional workflow validity |
| **τ-bench** (2024) | Multi-turn retail/airline tasks with simulated user, tools, and domain policy | Stateful synthetic databases/APIs; final-state goal checks; `pass^k` over repeated runs; GPT-4o <50%, retail pass^8 <25% in v1 | User negotiation, policy adherence, state deltas, repeated reliability | LLM user simulator is part of treatment and may deviate from intent; final goal state can omit conversational quality, prohibited attempts, or collateral effects; annotated policy/task defects matter materially | Later external audit used by Agent Reliability Profile removed 24/50 airline tasks; repeated profiles show mean success is not reliability. This is evidence that task health and repeatability are real repairs, while simulator validity remains open | Modular and more reproducible than live services, but synthetic users/databases and task corrections constrain deployment claims | **Tier A:** direct architecture for policy/state/reliability, not real-customer readiness |
| **OSWorld** (2024) | 369 open-ended tasks across real desktop/web apps, files, and multiple applications | Ubuntu/Windows/macOS VMs; task-specific setup and execution-based evaluators; humans 72.36%, best baseline 12.24% | Real applications, alternative action paths, cross-app state, explicit initializers/evaluators | Broad task success hides environment faults, partial progress, unsafe side effects, and cause; app/OS drift can invalidate tasks; one witness/evaluator need not be complete | AndroidWorld parameterizes tasks with initializer/check/teardown logic; OSWorld 2.0 is a reported successor but was not deeply reviewed here, so improvement claims remain open | High ecological substrate but expensive VM, licensed-app, network, version, and reset maintenance; exact reproduction is fragile | **Tier A question / B operational evidence:** important computer-use substrate, limited knowledge-work claim |
| **AndroidWorld** (2024/25) | 116 programmatic task templates across 20 Android apps, dynamically instantiated with parameters/paraphrases | Emulator/device state; per-task initialization, success check, teardown; best baseline 30.6%; robustness variants | Task families rather than one fixed wording/state; lifecycle hooks; outcome evaluation accepts multiple paths | Parameter generation is not occupational/task-distribution sampling; checks cover declared state, not all harms; emulator/app versions and randomization can confound comparisons | Demonstrates that nominally equivalent task variations materially change agent performance, directly repairing fixed-instance overconfidence; does not validate semantic equivalence of every variation | Stronger repeatable lifecycle than desktop/live web, but real-app versions, emulator images, permissions, and external services remain dependencies | **Tier A:** reusable parameterized state-check pattern |
| **BrowseComp** (2025) | 1,266 adversarially hard, inverted fact-finding questions with short answers | Live web; LLM semantic-equivalence judge; canary; Deep Research 51.5%; human trainers solved 29.2% of attempted set under up to two hours | Persistent, strategic search; cheap answer verification; compute-scaling and repeated-pass analysis | Inverted construction guarantees a witness, not uniqueness; 21 zero-pass items were removed after answer-guided review; model was trained on BrowseComp-style tasks; answer grading ignores source authority, citations, path, cost, and contamination; canary detects only some exposure | Repairs GAIA saturation by adversarial search depth and private-ish handling. Evidence supports difficulty and compute response, not unbiased browsing generalization or trustworthy research | Simple to run but live-web/index/time/provider dependence is uncontrolled; public question exposure and search-time leakage grow over time | **Tier B:** sharp retrieval stress test, poor professional-research validity |

## Unique cross-family insight: realism migrates the oracle

Interactive benchmarks do not eliminate syntheticity; they **move it**. Static QA places syntheticity in question/reference construction. API benchmarks place it in tool implementations and gold call/state semantics. Web replicas place it in seeded sites and evaluators. Desktop benchmarks use real applications but still author initial states and custom success scripts. User-interaction benchmarks add a simulator whose behavior partly determines the result.

Therefore “real environment” is not a binary property. A benchmark needs a projection ledger:

1. which substrate is native versus simulated;
2. which initial state is authored;
3. which actions are exposed and permitted;
4. which state predicates are observed;
5. which consequences are omitted;
6. which user/stakeholder behavior is simulated;
7. which environment changes across repeats;
8. which claims survive those projections.

The papers collectively demonstrate that execution-based checks are better than action-sequence imitation for admitting alternative paths. They do **not** show that a passing selected state predicate establishes safe, complete, professionally acceptable work.

## Methodology and evidence appraisal

### Evidence that design repairs worked

- **Outcome checks over demonstrations:** WebArena, OSWorld, and AndroidWorld explicitly execute tasks and inspect state, admitting multiple paths. This is a genuine measurement repair over action matching.
- **Frozen versus live external information:** API-Bank hard-codes external results, improving repeatability while reducing ecological validity. GAIA/BrowseComp retain live-web realism but cannot guarantee equivalent repeats.
- **Parameterized task families:** AndroidWorld shows significant performance changes under task variation, empirical evidence that one fixed wording/state is insufficient. It does not establish that generated variants are perfectly construct-equivalent.
- **Reliability beyond mean success:** τ-bench's `pass^k` and the later Agent Reliability Profile expose severe repeatability gaps. Five or eight proprietary-model calls still provide weak tail estimates and do not neutralize shared environmental/provider dependence.
- **Observer-view expansion:** AgentRewardBench adds expert labels for success, side effects, and repetition across WebArena-family trajectories. Its released labels have incomplete adjudication provenance and unequal evidence views, showing that adding humans does not automatically produce ground truth.
- **Harder browsing:** BrowseComp demonstrates much greater search depth and smooth compute scaling, but its model-selection/training relationship, live web, answer-only grading, and post-hoc item deletion prevent a clean claim that it measures general research quality.

### Adoption and influence

These families are treated as anchors because later primary papers explicitly use, compare against, or extend them: BrowseComp cites GAIA as a predecessor; AgentRewardBench samples WebArena/VisualWebArena/WorkArena; Agent Reliability Profile evaluates GAIA and τ-bench; AndroidWorld and OSWorld situate themselves against WebArena-style interactive evaluation. This is evidence of methodological influence, not validity. Citation counts, leaderboard presence, and model coverage were not used as substitutes for construct evidence.

## Limitations of this review

1. Eight immutable papers were read, but official repositories were not pinned and audited in this run; implementation claims are limited to paper descriptions and existing release-audited local reviews.
2. BrowserGym and OSWorld 2.0 are successor systems named in the task, but no immutable full source was acquired here; they remain comparison gaps rather than claimed improvements.
3. ToolBench refers here to arXiv:2305.16504's eight-tool benchmark, not the separate ToolLLM/ToolBench corpus at arXiv:2307.16789. Conflating them would corrupt the evolution chain.
4. Reported human baselines use different populations, instructions, time budgets, and environments and are not comparable across rows.
5. Paper-reported scores establish behavior under historical configured systems, not current difficulty or reproducibility.
6. No new leaderboard, citation, or cost inventory was constructed; adoption and maintenance claims remain bounded.

## Retain, repair, test

### Retain

1. Executable outcome/state checks that admit alternative legitimate paths.
2. Explicit initializers, teardown/reset, and task-specific evaluator identities.
3. Separate tool retrieval, invocation, policy, interaction, and outcome constructs.
4. Parameterized/equivalent forms and repeated trials.
5. Persistent multi-site/multi-app state when the work construct requires it.
6. Public calibration environments plus protected/refreshed capability forms.

### Repair

1. Record native/simulated substrate and omitted consequences instead of calling an environment simply “realistic.”
2. Separate attempted prohibited action, realized state delta, collateral side effect, communication quality, and final goal state.
3. Bind every check to an admissible observer view; emit `insufficient_evidence` when the view cannot establish it.
4. Preserve clean-start evidence, pre/post snapshots, reset result, environment health, and run-attributable deltas.
5. Treat user simulators, browser adapters, API search, prompts, and recovery policy as configured-system components.
6. Use task-clustered repeated estimates and report invalid runs, environment failures, retries, and cost.
7. Distinguish legitimate source retrieval from benchmark-answer exposure and record exposure→access→visibility→adoption→effect.
8. Keep answer, state, artifact, policy, safety, efficiency, and professional acceptance scores separate.

### Test in `skill-bench`

1. **Oracle completeness:** for each executable checker, construct one canonical pass, one legitimate alternative, one shortcut pass with omitted consequence, and one correct-looking artifact with wrong native state.
2. **Environment equivalence:** replay a task after reset and under pinned semantically equivalent variants; compare state hashes and failure labels before interpreting system variance.
3. **User-simulator validity:** run matched scripted, model-simulated, and human-reviewed interactions; estimate whether user behavior changes task outcome independently of the agent.
4. **Side-effect observability:** plant prohibited attempts, harmless failed attempts, realized collateral damage, and repaired damage; ensure these do not collapse into final success.
5. **Live-source role transition:** maintain immutable source snapshots for capability claims and separate live-web exploratory runs whose content/index/time are recorded.
6. **Handoff consequence:** extend beyond final GUI/API state by checking whether the resulting artifact/state is usable by a declared recipient's next operation.

## Concrete next actions

No new schema task is warranted: benchmark-bundle, execution-isolation, task-health, artifact-view, validity, metric, trace, and retrieval-leakage contracts already house these requirements. The highest-value remaining evidence work is a pinned full-source/release audit of BrowserGym and OSWorld 2.0 to test whether successor claims deliver stronger adapter conformance, environment health, diagnostics, and lifecycle maintenance rather than only higher scores.
