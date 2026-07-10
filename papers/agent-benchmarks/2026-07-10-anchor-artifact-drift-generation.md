# Paper Review: Anchor — Single-Specification Generation and Residual Artifact Drift

- **Paper:** https://arxiv.org/abs/2605.26321v1
- **Authors:** Maksim Ivanov, Abhijay Rana
- **Date read:** 2026-07-10
- **Venue / source:** RLEval 2026 paper; immutable arXiv preprint
- **Version read:** v1, 25 May 2026
- **Local PDF:** `data/papers/pdfs/2605.26321v1-anchor-artifact-drift.pdf` (12 pages; SHA-256 `e6a8953db1b1d37d0b865a16fb864f7cb4f58283d303fa7af3eda9a5cc801ee0`)
- **Local text:** `data/papers/text/2605.26321v1-anchor-artifact-drift.txt` (SHA-256 `f5a421ede1e8bcb50210fb9c0be8a43ffc7c3c7ae5eef08d5a4521cc422b5d11`)
- **Official release inspected:** https://github.com/agentic-labs/erp-bench at commit `ceba3880af555129b5278e056a0c20f2fb5a0ba9`, tree `364dc9c9c02e8c378f472c689ab736eeb2195e82` (commit dated 26 May 2026, one day after arXiv v1; close release evidence, not assumed byte-identical to a manuscript-time implementation)
- **Release archive:** `data/sources/releases/2605.26321v1-anchor/agentic-labs-erp-bench-ceba388.zip` (SHA-256 `3231829e8fa586921909f86fffebd46b320c021a624f44290b4553c4aaa71464`)
- **Release provenance:** `data/sources/releases/2605.26321v1-anchor/provenance.json`
- **Tags:** benchmark-generation, artifact-drift, constraint-programming, solver-oracles, terminal-state-verification, difficulty-control, ERP

## One-sentence contribution

Anchor formalizes a useful compiler architecture—sample one parametric workflow model, solve it, and project the solved state into instruction, environment, reference plan, and verifier—but the paper demonstrates **shared lineage and end-to-end witness consistency**, not semantic equivalence or verifier completeness: a manually authored CP-SAT model can omit professional rules, independent Jinja/Python projections can mistranslate it, oracle/no-op checks cover only two points in a vast state space, and the released containers expose mutable dependencies and public oracle/verifier artifacts.

## Why this matters for skill-bench

The paper targets a central benchmark-authoring failure. A task can look individually plausible while its prompt requests one outcome, its source pack permits another, its reference artifact instantiates a third, and its grader accepts a fourth. Anchor’s strongest general mechanism is to replace four independently authored artifacts with one versioned intermediate representation and deterministic projections (Figure 2 and Section 2, pp. 2–3). This directly advances charter objectives B and C: provenance should connect expert claims to an executable task model, and artifact/check bundles should be generated or validated against the same typed requirements.

The important boundary is equally transferable: **single-source generation reduces divergence among projections but does not make the source true or the compiler correct**. Anchor itself states that the constraint model may omit business logic, a renderer may mistranslate it, and the live ERP may introduce unintended defaults (Section 2, p. 3; Limitations, p. 4). Skill-bench should therefore treat a canonical task specification as a hypothesis-bearing intermediate representation with independent projection tests—not as a privileged ground truth that automatically licenses professional validity.

ERP-Bench is a methodological case, not a reason to narrow skill-bench to ERP. Procurement/manufacturing is useful because its structured records, deadlines, capacities, and measurable objectives make artifact drift unusually inspectable. The reusable hypothesis is cross-domain: can one typed requirement graph compile public instructions, initial state, valid witnesses, and checks while preserving fair disclosure and accepting legitimate alternative work products?

## Research question and claim boundary

The paper asks whether enterprise benchmark tasks can be generated at scale without the instruction/environment/oracle/verifier inconsistencies common in separately authored tasks, while retaining realistic system interaction, open-ended action paths, certified optima, and controllable difficulty.

The evidence supports the following bounded conclusions:

1. the authors implemented a substantial CP-SAT-backed generator and released 300 Odoo task packages across 29 workflow patterns;
2. the closest official release contains deterministic rendering code, seeded scenario data, reference plans, and terminal-state verifiers with a common generated lineage;
3. primary optimization objectives are required to reach CP-SAT `OPTIMAL` status before acceptance, while feasibility-only tasks require a feasible witness;
4. all 300 released tasks have a no-op score of zero and an oracle replay score of 100 according to the paper;
5. generated tiers are descriptively associated with lower success and larger action burden in the evaluated model/harness sample; and
6. terminal-state constraint and objective scoring permits multiple action trajectories and does not require exact equality to the released reference plan.

The study does **not** establish that the specification completely represents professional practice, every natural-language clause is semantically equivalent to the formal model, every environment behavior is modeled, the verifier is sound and complete over reachable states, the tier label is an isolated or calibrated difficulty treatment, the released benchmark can be reproduced from immutable dependencies, or success implies deployment-ready procurement/manufacturing competence.

## Methodology and system

### Expert workflow to solved specification

Ten freelance ERP practitioners with at least five years of production experience contributed roughly 40 person-hours across 29 workflow patterns; an engineer then encoded the patterns as parametric CP-SAT programs (Appendix D.1, p. 7). The formal model includes integer purchase, activation, assembly, and stock-allocation variables; demand, MOQ/capacity, BOM, workcenter, deadline, screening, invoicing, and repair constraints; and one of five objective modes (Appendix C–E, pp. 6–9).

This is materially better documented than anonymous “expert-authored” claims, but still thin as expertise-transfer evidence. The paper gives no practitioner role distribution, recruitment method, compensation, contribution-by-pattern lineage, elicitation protocol, disagreements, corrections, approval scope, or independent confirmation that the engineer’s formalization retained expert intent. Forty hours over 29 patterns is about a compact design review, not validation of every generated instance or every verifier predicate. The two later spot-check experts are not clearly separated from the ten contributors.

The formalization also selects only work naturally visible in terminal system state. Negotiation, tacit managerial judgment, persuasive communication, exceptions outside the ERP, and consequences beyond the system of record are excluded (Limitations, p. 4). This is a legitimate construct boundary, but “enterprise knowledge work” is broader than the constraint-programmable slice measured here.

### Sampling and solver semantics

Difficulty recipes jointly alter demand scale, stock and vendor-capacity ratios, deadlines, BOM depth, workcenters, intake screening, invoicing, repair state, and objective type. A seeded NumPy sampler draws concrete values; cheap arithmetic filters and CP-SAT rejection remove infeasible samples. The paper reports 300 accepted tasks after 732 rejected parameter sets and 3,195 solver calls (Appendix D.2–D.4, pp. 7–8).

For optimized tasks, the release’s `erp_bench/procurement/solver.py` requires `OPTIMAL` status for the primary objective, fixes that objective value, optionally certifies a spend secondary, then runs a deterministic single-worker fixed-search tie-break. The tie-break accepts `OPTIMAL` or `FEASIBLE` and uses `stop_after_first_solution`; it selects a stable witness but is not itself a proof that the resulting full assignment is lexicographically optimal. This does not undermine the certified primary objective, but it narrows “known optimal solution” to “a feasible canonical witness attaining the certified objective (and certified secondary where applicable).” For the 24 `constraint_only` tasks, no unique or optimal plan exists by design.

The generator’s 732 rejections also change the sampled population. Hard examples that remain unresolved after retries are resampled, so released difficulty is difficulty conditional on solver tractability and authored feasibility filters. This is sensible operationally but must be recorded as selection history; it is not an unconditioned sample from the declared recipe.

### Compilation into four artifacts

The release makes the projection pipeline inspectable. `ProcurementCategory.render` builds one template context from the scenario, plan, and blueprint. `HarborRenderer` then writes:

- `instruction.md` from `scenario.instruction` and `background_and_policy`;
- `environment/scenario_data.json` plus generated Odoo setup code;
- `solution/optimal_plan.json` plus replay code; and
- `tests/checks.py` with scenario-specific constants and rule invocations.

This is genuinely shared generation lineage, but “single source” should not be read literally as one declarative object from which all semantics are mechanically derived. The release contains a large solver, separate sampler/config models, an instruction template, a setup template, a roughly 100–130 KB generated checker per task, and replay logic. These are multiple translation programs whose consistency depends on human-maintained code. The architecture localizes drift to the specification or a translation layer; it does not eliminate translation-layer drift.

A static audit in this review inspected all 300 task directories. It confirmed the paper’s exact tier counts (50 easy, 166 medium, 84 hard), 29 patterns, and objective counts (183 spend, 34 vendor consolidation, 31 capacity preservation, 28 repair, 24 feasibility-only). Every accepted reference allocation fulfilled its stated demand; all 183 spend-task objective values matched the reference `expected_new_spend` to cents; every task preserved the generated instruction in `scenario_data.json`; and all 300 task manifests enabled internet access. These checks support structural coherence, not semantic equivalence or live Odoo execution.

### End-to-end trace: procurement-only instance

For `tasks/2000_easy_01_buy_only_baseline`:

1. **Instruction.** The public brief names four Sound Privacy Panels orders totaling 32 units, deadlines of 6–8 days, 27 on-hand units, no manufacturing route, margin and budget constraints, confirmed SO/PO requirements, delivery dates, and SO→PO origin traceability.
2. **Environment projection.** `scenario_data.json` contains the customers, products, 54 vendors, stock levels, policies, and the same generated instruction; `setup_scenario.py` loads it into Odoo.
3. **Oracle projection.** `optimal_plan.json` allocates 21 stock units and purchases 11 units from one six-day offer for $3,065.92, fulfilling all four demands and preserving the required margin. Because this is `constraint_only`, the objective value is zero; the plan is a feasible canonical witness, not a uniquely optimal purchase plan.
4. **Verifier projection.** The generated checker identifies relevant Odoo records, reprices purchase lines from authoritative offer tiers rather than trusting agent-written prices, checks demand/deadline/budget/margin/order state and origin links, and gives fixed optimality credit for the feasibility-only objective.

This trace illustrates the central benefit: customer atoms, stock, offers, witness allocation, and check constants share generated identifiers. It also illustrates residual risk. The sentence “use stock where it helps,” the meaning of “necessary” records, tolerances, fallback record matching, adjacency protection, and acceptable lineage representations live in renderer/checker code, not in a proved instruction-to-model equivalence relation. A second feasible plan may be professionally legitimate yet fail if its representation falls outside checker assumptions.

### End-to-end trace: manufacturing instance

For `tasks/2075_medium_09_single_bom_lowest_cost`:

1. **Instruction.** Eight Automatic Case Erector orders total 152 units; 69 finished units are on hand; shortfalls may be purchased or manufactured; the task requires minimum new spend, a 29.8% margin floor, workcenter limits, component procurement, dated SO/PO/MO records, and SO→MO→PO or SO→PO lineage.
2. **Environment projection.** The scenario seeds 58 customers, 75 vendors, 57 products, 11 BOMs, two workcenters, stock, tiered supplier offers, and internal-note capacity data.
3. **Oracle projection.** The certified spend objective is $79,890.56. The witness allocates stock to later orders, manufactures 83 units in three due-date buckets, and buys component quantities across multiple tiered offers, with explicit MO and PO lineage references.
4. **Verifier projection.** `tests/checks.py` embeds `EXPECTED_OBJECTIVE_VALUE = 79890.56`, reconstructs realized spend from authoritative supplier tiers, checks component and manufacturing feasibility, workcenter schedules, demand deadlines, order states, and origin-token flow, then applies the feasibility gate before optimality and traceability scores.

The verifier does not compare the terminal state to the exact oracle assignment, which is desirable: alternative action sequences and alternative feasible terminal plans can receive credit. But acceptance remains bounded by the checker’s hand-coded abstraction of Odoo. The paper reports no mutation testing against near-valid alternative plans, no exhaustive state-space proof, and no adversarial grader audit beyond naturally occurring rollouts.

## Verifier, reward, and validity evidence

The reward separates constraints (25%), optimality (60%), and traceability (15%). Any failed explicit constraint suppresses optimality/traceability credit, and two hard-zero gates prevent no-op rewards on screened and repair tasks (Appendix E, pp. 8–9). Optimality is recomputed from terminal records and decays exponentially above the certified objective; agent-written PO prices are checked and repriced from authoritative offer tiers. These are strong anti-shortcut design choices.

Five end-to-end checks are reported (Appendix I, pp. 11–12):

- no-op scores zero on 300/300 tasks;
- oracle replay scores 100 on 300/300;
- an LLM cross-artifact judge was run over all tasks in 12 development iterations;
- a canary found no feasible rollout strictly better than the solver objective among 16,159 completed trials; and
- two experts independently attempted 15 stratified tasks, averaging 90.48 reward and 55 minutes, with three explicit-constraint failures in 30 attempts.

These checks are useful but have narrower meanings than “artifact drift mitigated by construction.” No-op and oracle are two witnesses: they detect an already-solved initial state and rejection of the intended plan, but cannot estimate false acceptance or false rejection elsewhere. The reward-hacking canary detects only states both marked feasible and better than the certified objective; it misses exploitable states that tie/worsen the objective, manipulate traceability, alter adjacent data outside checked predicates, or receive partial reward illegitimately. Zero naturally produced triggers is not an adversarial soundness proof.

The LLM judge is a development tool, not independent validation: prompt/model/version, outputs, error rates, reviewer overrides, and the final audit record are not released or reported. Its 12 iterative passes are outcome-dependent generator development, so the final 300-task corpus is a post-debug instrument, not a held-out test of the judge.

The expert study is more revealing than the perfect oracle result. Experts failed explicit constraints in 10% of attempts and averaged below full credit, but the paper does not adjudicate whether those are expert errors, instruction ambiguity, UI failures, or verifier false negatives. There is no agreement measure, alternate-solution audit, expert acceptance threshold, or novice/control group. The study therefore supports rough human executability and time realism, not semantic completeness or professional validity.

## Evaluation evidence and difficulty claim

Five models were run through coding, browser, and computer-use interfaces, nominally with five trials per task/configuration and one-hour/400-turn budgets. Two open-weight computer-use configurations were stopped after hundreds of zero-score trials, yielding 16,159 completed of 18,000 scheduled trials (Sections 3–4 and Appendix F–H, pp. 3–4, 9–11).

The descriptive result is clear: aggregate pass@5 decreases from easy to hard in every harness (70.5%→22.3% coding, 46.5%→7.7% browser, 56.0%→9.5% computer use), and scale/structure variables correlate with lower pass@1 and more turns among successful trials. Constraint-clean trials are more common than perfect-optimal trials (26.1% versus 17.4% overall), suggesting that exact rule adherence and optimization remain separable.

The stronger “controlled difficulty” interpretation is not identified. Tiers jointly manipulate task size, rule count, source density, action count, manufacturing availability, objective type, repair state, and interface burden. They are bundled strata, not a one-dimensional intervention. Easy/medium/hard also have unequal task and pattern composition, and tasks share generator patterns, so item outcomes are clustered. Wilson intervals do not address pattern clustering, five repeated attempts per item, model/harness dependence, or selection through infeasibility rejection. Parameter correlations are numerous, correlated with one another, and reported without uncertainty or multiplicity control. Correlations on resolved trials additionally condition on success and can induce selection bias.

The harness comparison is descriptive rather than causal. Coding agents can batch JSON-2 API operations, browser calls allow seven accessibility actions, and computer use allows sixteen pixel/keyboard actions; models are not identical in the vision arm. The 16–56 point GUI gap and 3.1–14.3× cost difference describe configured systems with deliberately different affordances, not intrinsic interface penalties or human-relative ERP capability.

Finally, “pass5” (all five attempts pass) is a useful strict repeat statistic, but the paper’s statement that low pass5 implies agents are not ready for unattended deployment requires a deployment population, incident costs, correlated run conditions, and a readiness threshold. The benchmark’s own validity evidence does not provide those.

## Unique insight

Anchor’s deepest transferable insight is a **benchmark compiler with typed projection obligations**:

`expert evidence → versioned workflow IR → sampled solved instance → public requirement projection + environment projection + witness projection + verifier projection → cross-projection tests`

This is stronger than storing four files with a shared task ID. It enables defect localization: if a prompt clause lacks a requirement atom, the instruction projector is at fault; if the atom is absent from the model, expertise formalization is at fault; if a valid state fails, verifier admissibility is at fault; if an oracle cannot execute, environment/witness compilation is at fault.

The crucial extension for skill-bench is to preserve **bidirectional coverage**, not merely shared ancestry:

- every public requirement atom maps to environment affordances, at least one valid witness consequence, and one or more checks;
- every scored/private predicate maps back to a fair public basis and evidence authority;
- every environment variable relevant to score is disclosed or intentionally discoverable;
- alternative valid representations are admitted through declared invariances;
- unsupported expert assumptions and renderer-generated conventions remain typed hypotheses; and
- each projection carries compiler/version hashes plus end-to-end witness, negative-contrast, metamorphic, and adversarial tests.

A second insight is negative: **solver certification proves a property of the formal model, not the live professional task**. The logical chain has separate warrants:

`CP-SAT optimum` does not imply `ERP-executable optimum`;  
`ERP-executable witness` does not imply `instruction-equivalent witness`;  
`verifier acceptance` does not imply `professional correctness`; and  
`generated tier association` does not imply calibrated difficulty.

Each arrow needs independent evidence.

## Limitations and validity threats

1. **Expertise transfer is under-specified.** Ten practitioners and 40 hours are reported, but contribution lineage, disagreement, approval, and per-pattern coverage are absent.
2. **The formal source can be wrong.** Omitted business rules propagate consistently into all artifacts rather than producing detectable disagreement.
3. **“Single source” still has multiple hand-maintained translators.** Solver, sampler, prompt, setup, replay, and checker code can drift.
4. **Natural-language equivalence is not proved.** An undocumented LLM judge and small expert study are the principal semantic checks.
5. **No-op/oracle tests cover only two states.** They do not establish verifier soundness or completeness.
6. **The reward-hacking canary is narrow.** Better-than-oracle feasible states do not cover tie/worse objective exploits, partial-credit exploits, or unchecked side effects.
7. **Alternative valid solutions are not calibrated.** No contrast set or mutation study estimates false rejection across legitimate representations.
8. **The canonical tie-break is not a certified lexicographic optimum.** Fixed search accepts the first feasible tied witness; primary/secondary objectives remain certified.
9. **Feasibility-only tasks have no meaningful unique optimum.** Their released plan is a witness, despite broad “known optimal solutions” wording.
10. **Rejection sampling changes the instrument population.** Solver-hard or infeasible samples are discarded/resampled.
11. **Difficulty is a bundled recipe.** Scale, rule density, objective, workflow structure, and action burden change together.
12. **Difficulty evidence is clustered and observational.** Pattern dependence, repeated attempts, parameter collinearity, and multiple correlations are not modeled.
13. **Resolved-trial turn correlations condition on success.** This can distort action-burden associations.
14. **Incomplete runs complicate aggregation.** Two computer-use arms were stopped early after zero scores; missingness is treatment-related.
15. **Harness comparisons include different affordances and model support.** They are configured-system descriptions, not isolated interface effects.
16. **Terminal-state scoring omits process safety.** Harmful transient actions, unauthorized access, and inefficient repair paths may disappear from the final state.
17. **The system of record is treated as truth.** Off-system outcomes, tacit judgment, negotiation, and downstream consequences are outside construct coverage.
18. **Generated prompts are unusually explicit.** Fair grading improves, but ecological realism and hidden-requirement elicitation decrease.
19. **Public release exposes private internals.** Exact objective constants, check code, scenario seeds, and optimal plans are distributed with each task; operational access controls and contamination policy are required.
20. **Coding containers include readable scenario data.** `/setup/scenario_data.json` is copied into the task image; this may let file-capable agents bypass ERP discovery unless the intended construct explicitly permits it and access is measured.
21. **Internet is enabled for every released task.** The paper does not discuss external retrieval, exfiltration, service drift, or network isolation.
22. **Environment dependencies are mutable.** `FROM odoo:19`, `uv:latest`, live apt repositories, and PostgreSQL installation lack immutable image/package digests.
23. **No ordinary release test suite was found outside generated task verifiers.** Regeneration/oracle/no-op commands are documented, but CI evidence and paper-table reproduction are not preserved in the pinned snapshot.
24. **The LLM consistency audit is not reproducible.** Prompt, model, judgments, overrides, and final report are absent.
25. **Expert execution is not adjudicated.** Three constraint failures could be human errors, prompt defects, UI defects, or grader errors.
26. **Professional and deployment validity are unmeasured.** No organization uses the artifacts or supplies decision-loss thresholds.
27. **Paper-time code identity is not exact.** The inspected commit postdates arXiv v1 by one day.
28. **Public naming already drifts.** The release README calls the paper “Preventing Artifact Drift,” while v1 is titled “Mitigating Artifact Drift”; minor, but illustrative of metadata projection drift.

## Reproducibility and operational realism

Instrument inspectability is strong. The immutable full paper, extracted text, 39.7 MB official archive, generator, lockfile, 300 task packages, templates, solver, setup code, reference plans, and checkers are locally provenance-recorded. This review read the complete paper, inspected the core build/render/solve paths, traced one procurement-only and one manufacturing instance across instruction/environment/oracle/verifier artifacts, and statically audited all 300 task directories for counts and selected invariants.

Exact reproduction is weak. The closest release is post-v1, raw 16,159 trial records and complete result-reproduction scripts are not evident in the pinned archive, proprietary models are mutable, provider defaults are used, first-party/OpenRouter service state is time-sensitive, and container builds pull mutable Odoo/uv/apt artifacts. Re-running generation may be deterministic at the Python seed level while producing a different executable ERP environment. A benchmark compiler needs hashes for the compiler, specification, solver/library, rendered artifacts, base image digest, package snapshot, and verifier runtime—not only a seed.

Operational realism is mixed. Fresh databases, persistent ERP records, real Odoo APIs/UI, tiered offers, capacities, deadlines, invoicing, traceability, adjacent records, and hour-scale tasks are substantially closer to consequential work than static QA. Conversely, the tasks expose every scoring-relevant rule, reduce work to terminal structured state, omit human coordination and off-system effects, allow internet, distribute private solutions/checkers publicly, and do not demonstrate that agent-visible filesystem boundaries prevent reading setup artifacts. These design choices support reproducible planning evaluation but not the full construct of autonomous enterprise work.

## Transfer to skill-bench: concrete changes

1. **Adopt a versioned task intermediate representation, not an omniscient task truth.** Link each requirement atom to expert/source evidence, authority, scope, validation status, and compiler version.
2. **Require four-way bidirectional coverage.** Public requirement ↔ source/environment affordance ↔ witness consequence ↔ check, with explicit unmapped-item failures.
3. **Preserve projection manifests.** Hash the IR, sampler/config, instruction renderer, source-pack/environment builder, witness generator, verifier generator, dependency lock, and each rendered artifact.
4. **Separate solver certificates from validity claims.** Record feasibility/primary/secondary/tie-break status independently; label feasibility-only plans as witnesses and keep professional correctness unsupported without expert evidence.
5. **Add negative and metamorphic projection tests.** For each task family, mutate one requirement, source value, environment affordance, witness action, and checker predicate; assert the expected projection changes and unchanged invariants.
6. **Calibrate verifier admissibility.** Plant near-valid alternatives, equivalent representations, irrelevant side effects, price/field tampering, no-op states, and adversarial partial-credit cases; estimate false pass/fail rather than relying on natural rollouts.
7. **Instrument agent evidence access.** If setup/source files duplicate ERP facts, declare whether direct file access is permitted and record reads; otherwise enforce tool-level canaries and fail closed.
8. **Keep public/private artifacts operationally separate.** Public release can include development fixtures, but scored runs need held-out parameters/check details, contamination records, and canaries proving oracle/verifier files are unreadable.
9. **Pin the executable environment.** Record image digests, package snapshots, database/ERP versions, network policy, clocks, solver versions, and readiness checks.
10. **Treat difficulty as a multidimensional design vector.** Report demand scale, evidence density, rule count, action burden, objective structure, ambiguity, and environment friction separately; validate tiers with held-out instances and pattern-clustered uncertainty.
11. **Add process/safety checks where consequential.** Terminal correctness should not erase unauthorized, destructive, or unsafe intermediate actions.
12. **Use existing contracts rather than add a duplicate schema.** These requirements refine `expertise-transfer`, benchmark-bundle artifact/check crosswalks and admissibility, task health, validity arguments, metric monitoring, and execution-isolation records.

## Action items for repository

- [x] Read the complete immutable arXiv v1 PDF/text and preserve exact local evidence paths and hashes.
- [x] Inspect the official pinned release with its post-paper timing boundary.
- [x] Trace procurement-only task `2000_easy_01_buy_only_baseline` across instruction, scenario, witness, and verifier.
- [x] Trace manufacturing task `2075_medium_09_single_bom_lowest_cost` across instruction, scenario, certified objective/witness, and verifier.
- [x] Audit all 300 released task directories for tier/pattern/objective counts and selected cross-artifact invariants.
- [x] Separate paper claims, release observations, and skill-bench adaptations.
- [x] Add no duplicate queue task; map the requirements into existing authoring, bundle, validity, task-health, metric, and execution contracts.
