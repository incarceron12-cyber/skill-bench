# OccuBench: a language simulator broadens authored task coverage, not occupational validity

## Source and review status

**Deep review, release-audited.** I read the complete immutable 23-page arXiv v2 paper and inspected the complete official GitHub code/data snapshot and complete Hugging Face dataset at pinned revisions.

- Paper: Xiaomeng Hu et al., *OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation*, arXiv:2604.10866v2, <https://arxiv.org/abs/2604.10866v2>
- Local PDF: `data/papers/pdfs/2604.10866v2-occubench.pdf` (SHA-256 `8e915dff60276bf9880f1784246b964bb34408826b81351bc5a1d0e68bed245c`)
- Local text: `data/papers/text/2604.10866v2-occubench.txt` (SHA-256 `e374d3324c5bd80eb79216d0b1e015b710ab8a3727e1eb368627014090822ecf`)
- Official repository: <https://github.com/GregxmHu/OccuBench>, pinned commit `d47bffb524b51d69748bf6801e803de04ed40820`
- Local archive: `data/sources/releases/2604.10866v2-occubench/GregxmHu-OccuBench-d47bffb.zip` (SHA-256 `6f7efd963e8701748f584585a3877c1ae60a376d291aae431db49fdcfe221ed3`)
- Official dataset: <https://huggingface.co/datasets/gregH/OccuBench>, pinned revision `6c697ddecf38df07fc84391c5ad56610e3d6c9fe`
- Complete local dataset: `data/sources/releases/2604.10866v2-occubench/huggingface/`
- Provenance and timing boundaries: `data/sources/releases/2604.10866v2-occubench/provenance.json`
- Date read: 2026-07-15

The code and dataset revisions are dated 2026-04-14: after arXiv v1 and before immutable v2 on 2026-04-16. They are strong release evidence, but not proof of byte identity with every paper run.

## One-sentence contribution

OccuBench makes an LLM a stateful tool-response generator and uses it to package 382 interactive instances under 100 occupationally labeled scenarios, then adds prompt-driven explicit and implicit faults; this is a useful scalable **synthetic transition-system stress test**, but job-role labels, model-authored state, outcome-conditioned selection, and model-judged trajectories do not establish real occupational tasks, domain-valid dynamics, professional safety, or deployment robustness.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through narrow expansion into a benchmark mechanism absent from the reviewed landscape: replacing unavailable professional systems with a language model that generates every tool observation. The reusable question is not whether `skill-bench` should adopt one simulator or occupation. It is:

> What evidence is required before a generated action schema, latent state, transition, observation, fault, and verifier can stand in for a consequential professional environment?

The concrete evidence is the full paper plus all 382 released task/config pairs and the executable harness. Useful completion separates five claims that the paper often compresses: authored occupational resemblance, simulator-contract conformance, task solvability under one simulator, configured-agent performance, and validity for real professional action.

## Research question and defensible claim boundary

The paper asks whether Language Environment Simulators (LESs) can make the “untestable majority” of professional domains evaluable, and reports task completion and fault resilience for 15 models across ten categories and 65 domains (pp. 1–7).

The released evidence supports a narrower question:

> Under a named agent model, a named LLM simulator, a model-majority verifier, and one set of model-authored task/configuration packages, how often does the generated trajectory satisfy the released natural-language verification plan, and how does that rate change when fault instructions are appended to the simulator prompt?

It does not establish fitness for a profession, representative occupational capability, factual domain correctness, safe performance, real-environment robustness, deployment readiness, or that category differences are occupational specializations. The paper's statement that mapping each scenario to a job role “ensur[es] that evaluation results directly reflect an agent’s fitness for professional work” (p. 2) skips the entire source, authority, transition-fidelity, consequence, and sampling argument.

## Methodology and system

### 1. LES as an implicit stochastic transition system

The paper defines an LES as `(s[t+1], o[t+1]) = fθ(s[t], a[t]; c)`, where configuration `c` contains a system prompt, tool schema, initial state, and state description (pp. 4–5). State is not updated by executable code. The simulator receives the full prior action/observation conversation and emits the next JSON observation; latent state exists only in model context.

That design cheaply supports arbitrary schemas and semantically rich responses. It also removes an independent state authority. There is no serialized post-state, transition function, invariant checker, event log, state hash, rollback, or deterministic replay. A plausible observation can disagree with the hidden intended state while remaining valid JSON. The paper's own cross-simulator cases expose state fabrication, entity omission, and rule invention (pp. 11–13), but these are hand-selected symptoms rather than a measured conformance rate.

The released `occubench/lwm.py` confirms this boundary. Each tool call replays the complete textual history to an OpenAI-compatible chat endpoint. Parsing checks only that a JSON value can be extracted; after ten parse failures, the last invalid response may still be returned. Neither temperature nor seed is pinned. API calls retry up to 50 times, simulator calls can multiply that by ten parse retries, and retries are not represented as trial invalidity or cost.

### 2. Multi-agent synthesis and outcome-conditioned assembly

The paper says each scenario is split into 16 non-overlapping subtopics and grounded in a “professional reference document” covering terminology, workflows, state, edge cases, and constraints. Gemini-3-Flash-Preview then generates environment configurations, instructions, tools, solution plans, and verification rubrics. Instances are executed repeatedly with and without the plan; a majority verifier and repair module are used; 100%-autonomously-solved, 0%-solved, and invalid-schema items are removed (pp. 5–7).

None of the reference documents, 16-subtopic assignments, candidate pool, rejection/repair ledger, synthesis prompts, model outputs, reference plans, autonomous solve matrix, majority judgments, or difficulty-calibration runs is released. The public task table has exactly six fields and no solution plan. “Guaranteed solvability” therefore means that selected items reportedly admitted a passing model trajectory under the synthesis simulator and verifier—not that a validated professional solution exists, all task obligations are satisfiable, or a real environment supports the same path.

Selection explicitly uses model outcomes twice: trivial/unsolved items are removed, and for each task the level with the lowest autonomous success rate is selected “to maximize discriminative power” (p. 6). That produces a useful challenge set but invalidates naive difficulty prevalence and inflates dependence on the synthesis model, agent panel, plan, and verifier. Difficulty labels are construction/selection labels, not calibrated human effort or occupational complexity.

### 3. Released suite composition

The pinned files parse as 382 unique task IDs, 382 unique environment IDs, and 100 scenario metadata rows. The stated difficulty counts reproduce exactly: 108 level 1, 129 level 2, and 145 level 3. Tool counts range from 2 to 10 with median 5 and mean 5.47, consistent with the paper's rounded 5.5.

However, only **98** scenario names appear in the 382 evaluation instances. `Autonomous Driving Scenario Planning` and `Crop Disease Diagnosis` occur in the 100-row scenario pool but have no released evaluation instance. Thus “100 scenarios” describes the metadata frame, while the administered/released evaluation table covers 98 scenario labels. Instance allocation is also highly uneven: scenarios contribute one to nine instances, and category totals range from 16 Science instances to 63 Business instances. The paper reports category percentages without documenting whether its aggregation is instance-weighted, scenario-weighted, or otherwise balanced.

The scenario frame itself is model/author-curated. A row contains only category, domain, and scenario name. There are no occupational-source identifiers, job-task records, observed frequency, practitioner contributors, credentials, employer/workflow evidence, accepted omissions, authority statements, consequence model, independent expert review, or transformation lineage. “Emergency Department Triage” names a setting; it does not validate clinical actions.

### 4. Agent execution and configured-system identity

The released agent loop supplies the task, tools, and a generic “professional AI assistant” prompt, permits up to 200 tool calls, and inserts the host's current wall-clock date. It does not pin temperature, seed, provider snapshot, request parameters beyond token limit, retry policy at the agent layer, or a cost/time budget. Parallel tool calls are processed serially by the harness even if generated together.

The host date is an uncontrolled environment intervention. Several released tool examples use 2023 dates, while valuation and expiry tasks can be date-sensitive. A run in 2026 or later may receive a contemporary date in the agent system prompt while the generated environment emits an old simulated date. The paper's model-family, generation, and reasoning-effort comparisons also lack repetitions, confidence intervals, task/scenario clustering, run dates, token/cost accounting, and a full run inventory. Small category differences and explanations about model training data (pp. 14–15) are post hoc hypotheses, not identified specialization mechanisms.

### 5. Verification

Every released task has a natural-language verification plan. The verifier receives the initial state, state description, instruction, plan, and textual trajectory; three concurrent calls to one verifier model each return binary correctness and prose feedback, and majority vote decides pass/fail. By default the verifier model is the simulator model.

This is not an automated state oracle in the usual sense. It is repeated model judgment over model-generated observations. The verifier cannot inspect authoritative post-state because none exists. Individual votes are discarded except for the first feedback from the majority class; no vote IDs, probabilities, evidence locators, disagreement, invalid response status, or adjudication is retained. Parsing errors become false, conflating grader failure with substantive task failure.

No human or expert annotation study, agreement estimate, false-accept/false-reject audit, adversarial trajectory test, alternative-valid-path study, criterion-dependence analysis, or cross-verifier sensitivity is reported. A three-vote majority may reduce sampling noise; it does not validate the rubric or establish professional correctness.

### 6. Fault injection

E1, E2, and E3 are implemented by appending natural-language rules to the simulator system prompt. The prompt asks the model to choose faults randomly, space them naturally, persist them for a requested duration, and avoid targeting critical actions. There is no sampled fault schedule, seeded randomizer, fault event ID, before/after observation pair, affected field, injected-vs-spontaneous distinction, realized duration check, or replayable fault transform.

Consequently nominally matched agents need not receive matched faults. A simulator can choose different calls, fields, values, or timing depending on the agent trajectory. E2's “stale/cached data” permits “plausible but slightly outdated or incorrect values” without defining an allowed perturbation, while “non-critical fields” is left to the simulator. E3 is not a fixed mixture when the default count is two; “roughly half” is a prompt instruction.

The paper reports lower mean completion under E2 than E1 and a 14.1-point E0→E2 decrease (pp. 8–9). This is meaningful evidence that agents have more trouble satisfying the verifier when the same simulator is prompted to emit silent degradation. It is not evidence about prevalence, severity, or handling of real database/API faults. Because the fault prompt changes simulator behavior rather than applying a controlled transform to a canonical response, the contrast mixes agent resilience with fault realization, simulator compliance, and verifier sensitivity.

The robustness metric `min(CR_E1, CR_E2, CR_E3) / CR_E0` is also unstable for low baselines and compresses three qualitatively different conditions into the noisiest observed ratio. No uncertainty accompanies it.

## End-to-end release reconstruction: Oakwood Gardens

The paper's Property Valuation fault case corresponds to released task `11`, environment `env_153c260a856a`:

1. **Occupational label:** the scenario table labels it `Business & Enterprise / Real Estate / Property Valuation Assessment`. No occupational source or practitioner is attached.
2. **Task projection:** the instruction asks for 12-month NOI and DSCR for `OAK-88`, including MCI surcharge expiry, fixed $142,000 expenses, $17,500 monthly debt service, and a 1.20 threshold.
3. **Tool interface:** three generated tools expose current date, unit-level records, and property metadata.
4. **Intended state:** the config contains three five-unit groups. Group A rents at $2,800; B at $2,100; C at $1,450 plus a $550 surcharge expiring after four months. The state contains $210,000 annual debt service and $142,000 fixed expenses.
5. **Simulator projection:** the entire state, state descriptions, tool definitions, and examples are embedded in the simulator prompt. Each observation is generated afresh from that prompt and conversation; no executable database query occurs.
6. **Fault projection:** under E2, another prompt tells the same model to truncate lists, omit fields, or return stale values. The paper's case says it returned 2 of 15 units for two calls, but neither that trajectory nor its sampled fault schedule is in the release.
7. **Expected witness:** the verification plan fixes revenue at `$168,000 + $126,000 + $87,000 + $11,000 = $392,000`, NOI at `$250,000`, annual debt service at `$210,000`, DSCR near `1.19`, and `Fail`.
8. **Observed score path:** a model verifier reads the textual tool observations and response and votes pass/fail. It has the exact expected intermediates. There is no deterministic arithmetic grader, final state, or released paper-run vote record.

This package is internally legible and supports an authored calculation-and-evidence-retrieval task. It does not show that the rent-control/MCI representation is legally or professionally correct, that a real appraisal database behaves this way, that the task is representative, or that the paper's displayed trajectories can be replayed. The unique methodological lesson is that an LES package contains **three coupled models of the world**—state/transition, observation/fault, and verifier—and shared authorship can make them agree even when all three are wrong about professional reality.

## Evidence and claim limits

### Supported

1. A compact, inspectable release can package hundreds of semantically diverse generated tool interfaces and initial states without implementing 65 domain backends.
2. All 382 released task-to-environment links resolve, schemas parse, tool counts match the reported range, and the published difficulty distribution is reproducible from the release.
3. Under the paper's configured simulator and model verifier, reported completion varies substantially across agent configurations, categories, fault prompts, reasoning settings, and simulator models.
4. Cross-simulator score and observation differences demonstrate that simulator identity is a material instrument component.
5. Prompt-driven silent degradation creates a useful stress condition for detection, re-query, and verification behavior.

### Partially supported

- **Solvability:** selected instances reportedly admitted a passing generated trajectory under one simulator/verifier, but plans and calibration runs are absent and professional feasibility is unvalidated.
- **Difficulty:** levels and lowest-success selection provide an authored discrimination ordering, not human or occupational difficulty calibration.
- **Ranking stability:** Gemini/Qwen simulator rankings agree on 24 of 28 model pairs, but this is one unrepeated eight-agent panel with no pair-margin uncertainty or simulator-conformance criterion.
- **Fault resilience:** rate changes support simulator-prompt-condition sensitivity, not real-environment reliability or production robustness.

### Not supported

- direct fitness for any occupation or professional role;
- occupationally representative coverage or task prevalence;
- correctness of clinical, legal, financial, industrial, or safety procedures;
- a real-world incident probability or robustness estimate;
- safe autonomous action, professional acceptance, economic value, or deployment readiness;
- causal explanations for industry profiles or training-data effects;
- exact independent reproduction of the paper tables from released raw trajectories/results.

## Unique insight: simulator validity is a coupled-contract problem

An LES is not one component. It is a chain:

```text
occupational source / authority
→ task and public requirements
→ initial-state authority
→ executable or generated transition semantics
→ observation projection
→ fault transform and exposure
→ agent action
→ realized post-state / consequence
→ grader evidence view and verdict
→ licensed claim
```

OccuBench releases the middle authoring package but supplies little evidence for the first or last links. More importantly, its state transition, observation, fault, and verifier are not independent: model-authored prompts define the world; a model produces the evidence; a model judges that evidence against model-authored expected behavior. Agreement inside that loop is **closed-loop conformance**, not external validity.

For `skill-bench`, simulator replacement must therefore be validated per boundary:

- **semantic authority:** who or what licenses the state variables, rules, thresholds, and consequences;
- **transition conformance:** whether actions produce invariant-preserving post-states, including invalid and alternate paths;
- **observation conformance:** whether each tool reveals exactly the declared view and no hidden/private state;
- **fault conformance:** whether a pinned transform realizes a predeclared fault without changing unrelated semantics;
- **grader independence:** whether scoring observes authoritative state/evidence rather than the simulator's fluent self-report;
- **transport evidence:** whether passing/failing behavior predicts anything in a real or higher-fidelity environment.

A simulator can be useful before it clears all six gates, but its claim must remain “performance in this synthetic instrument.”

## Limitations and validity threats

1. No occupational sampling frame, task-frequency weights, work observations, practitioner authors, or independent experts are reported.
2. Job-role and domain labels provide face resemblance, not occupational validity.
3. Professional reference documents and 16-subtopic structures are unreleased and have no provenance or authority audit.
4. The synthesis candidate pool, repair/rejection flow, prompts, plans, and calibration outcomes are absent.
5. Selection removes 0%/100% items and chooses lowest-success levels, conditioning suite assembly on model/verifier outcomes.
6. Difficulty labels lack human-time, error, consequence, or psychometric calibration.
7. Only 98 of 100 scenario metadata names appear in released evaluation instances.
8. Scenario and category instance allocations are unequal, while aggregation policy and clustered uncertainty are unspecified.
9. State is maintained implicitly in model context rather than an authoritative serialized transition system.
10. No transition invariants, final-state records, state hashes, reset equivalence, or deterministic replay exist.
11. Simulator temperature, seed, snapshot, API date, and stochastic repeats are absent.
12. Agent prompt inserts mutable host date into date-sensitive generated worlds.
13. Provider/model/harness identities and reasoning controls are insufficient for exact configured-system replay.
14. Reported main cells appear single-run and lack intervals, task/scenario clustering, and multiple-comparison treatment.
15. Model-majority verification has no human/expert calibration, released votes, evidence locators, or adversarial validation.
16. The default verifier shares the simulator model, coupling environment and judgment errors.
17. Verifier errors become false; evaluation-task exceptions can be logged and omitted rather than assigned an explicit invalid status.
18. Faults are prompt requests, not seeded transforms; realized type, location, duration, and severity are not auditable.
19. Different agents can receive different nominal faults because exposure depends on generated trajectories.
20. Implicit fault categories do not define field criticality, plausible value ranges, source freshness, or oracle truth.
21. Cross-simulator “quality” is inferred from completion and selected cases, not measured against an authoritative transition corpus.
22. Pairwise rank agreement over 28 pairs ignores score margins, ties, task clustering, and repeated-simulator variance.
23. No human baseline, professional acceptance threshold, downstream user, consequence study, or correction workflow exists.
24. Dangerous domains are textual simulations; this avoids physical harm but cannot establish safety in those domains.
25. Raw trajectories, result matrices, model-judge votes, costs, invalids, and paper-time run manifests are unreleased.

## Reproducibility and operational realism

**Instrument inspection is high; headline-result reproduction is low.** The complete release contains 382 task packages, 382 simulator configurations, the agent loop, simulator wrapper, fault prompts, and verifier. Another researcher can inspect the exact released prompts and run a new benchmark against compatible endpoints.

They cannot recreate the paper tables exactly because model snapshots/endpoints, seeds, temperatures, dates, raw trajectories, run inventories, retries, verifier votes, reasoning settings, result matrices, and synthesis/calibration evidence are absent. Proprietary future-dated model names and a mutable host date further weaken replay.

Operational realism is deliberately thin. Multi-step tools, partial observations, mutable state, ordering constraints, and silent degradation resemble professional systems at an abstract level. But no real data, software behavior, institutional permissions, practitioners, recipients, liabilities, or downstream consequences are present. As the paper concedes (pp. 15–16), LES evaluates a generated decision process rather than exact real data. Even that process is only as valid as the authored transition and verifier contracts.

## Comparison with adjacent reviewed evidence

- **GDPval** obtains tasks and artifacts from experienced occupational contributors but lacks representative within-occupation sampling. OccuBench expands interactive domain labels much more cheaply, while removing GDPval's strongest authority evidence. Breadth of labels cannot substitute for practitioners or artifacts.
- **TheAgentCompany / WorkArena** implement service state and executable transitions. Their occupational and consequence claims remain bounded, but native state gives graders an authority that an LES transcript lacks. OccuBench repairs domain implementation cost, not state or occupational validity.
- **HAS-Bench** shows that model-backed social roles are configured simulator interventions, not human participation. OccuBench requires the same provenance distinction for professional environments: a clinical-tool label does not make a model response clinical evidence.
- **UnderSpecBench** uses fixed synthetic state and side-effect predicates but can keep a private oracle after public authorization changes. OccuBench adds broader generated dynamics while weakening oracle authority further; both need public-basis and alternate-action validation.
- **Synthetic Computers at Scale** generates rich work substrate inside a model-authored loop. OccuBench generates interactive dynamics inside a similar loop. In both, scale and internal coherence are generator-conformance evidence, not professional validity.

## Transfer to skill-bench

### Retain

1. **Configuration-first simulator packaging:** keep state, state descriptions, tools, examples, and environment behavior independently versioned.
2. **Cross-domain transition primitives:** use generated simulators to prototype rare or inaccessible workflows without making those domains permanent scope boundaries.
3. **Plural fault classes:** preserve explicit failure, silent incompleteness, stale values, and mixed conditions as distinct diagnostic treatments.
4. **Cross-simulator sensitivity:** treat simulator identity as part of configured-system identity and test transport across implementations.
5. **Trajectory-grounded checks:** require evidence collection and verification, not only the right final phrase.

### Repair

1. Require every professional rule, threshold, hidden consequence, and fault expectation to cite a trusted source, consented expert, executable reference system, or explicit `synthetic_hypothesis` status.
2. Separate authoritative state from the simulator's observation text. Prefer executable transitions; otherwise serialize proposed post-state and run invariant/conformance checks before exposing an observation.
3. Pre-sample and hash fault schedules and canonical clean responses. Apply typed transforms with field, truth basis, severity, duration, recovery, and unaffected-invariant records.
4. Give compared systems matched fault opportunities or report exposure-conditioned estimands; never infer resilience from different unlogged fault realizations.
5. Use deterministic or independently calibrated state checks where possible. Preserve model-judge votes, evidence locators, invalidity, disagreement, and adjudication separately.
6. Validate simulator transitions with positive/negative/edge/alternate-path cases and an external authority set; measure false transition acceptance, state drift, and observation leakage.
7. Report scenario-balanced and instance-weighted results separately with scenario/task clustering, repeated trials, invalid denominators, and simulator-by-agent interactions.
8. Keep claim rungs explicit: synthetic package conformance → performance under one simulator → transport to another simulator → matched higher-fidelity system → professional consequence. Evidence does not automatically propagate upward.

## Action items

1. **No new build task.** Existing benchmark-bundle, projection, artifact/state admissibility, execution-validity, task-health, metric-monitoring, validity-argument, authority, and repeated-trial machinery already hosts these requirements. Adding an LES-specific schema would duplicate the backlog.
2. In the next synthetic environment pilot, create one paired executable-versus-LES task with the same public interface and predeclared action set. Plant transition, observation, and fault defects independently; measure conformance and agent-score transport before using the LES as a cheaper substitute.
3. Add release-conformance mutations to existing validator/fixture work: unlogged fault realization, simulator-only post-state, changed unaffected field, stale value without valid-time basis, verifier/simulator shared blind spot, and a legitimate alternate action rejected by the authored plan.
4. Require suite reports to distinguish metadata-frame scenarios from administered scenarios; OccuBench's 100-row frame/98-scenario evaluation mismatch is a concrete regression case.

## Claim ceiling

OccuBench supports the claim that the authors released a broad, inspectable collection of 382 model-authored interactive task/simulator packages and reported meaningful configured-system sensitivity to agent, simulator, reasoning, and fault-prompt conditions. It does **not** establish occupational fitness, domain-expert knowledge, real professional task coverage, valid clinical/financial/industrial transitions, real-environment robustness, safety, economic value, or deployment readiness. Its strongest transferable result is methodological: a language simulator is a versioned stochastic measurement instrument whose state, transition, observation, fault, and grader contracts each require independent evidence.