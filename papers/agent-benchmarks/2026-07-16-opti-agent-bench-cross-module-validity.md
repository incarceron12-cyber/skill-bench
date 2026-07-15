# Opti-Agent-Bench: cross-module checking is the right object, but the released evidence does not validate optimization R&D capability

**Paper:** Yongchang Fu, Xinjie Huang, Chengjun Dai, Chengzhe Feng, Junshao Zhang, and Hong Zhu, *Opti-Agent-Bench: Benchmarking End-to-End Optimization R&D Agents on Real-World Business Problems*, arXiv:2607.10768v1 (12 July 2026), <https://arxiv.org/abs/2607.10768v1>.

**Official repository:** <https://github.com/huiliyi-XJ/Opti-Agent-Bench>.

**Date read:** 2026-07-16.

**Review status:** Deep review of the complete immutable v1 paper and release audit of exact official commit `6e030101b488226c3b05cb5347b90c0155ca1cf0`. The commit is 2 days 20:33:48 after v1 and is not treated as the paper-time implementation.

## Evidence and provenance

- Local immutable PDF: `data/papers/pdfs/2607.10768v1-opti-agent-bench.pdf` (57 pages; 2,305,779 bytes; SHA-256 `3ba4c7ff121f261c56c7ea26ad16883db2176a273620ad1eb88523b1d984c311`).
- Complete layout-preserving local text: `data/papers/text/2607.10768v1-opti-agent-bench.txt` (166,576 bytes; SHA-256 `6710142475df60a0510eaede3c39d4c1b306e5386396eafca512fae86af0566c`). The extraction was read through the main methods/results, references, system prompt, complete representative rubric, ten task examples, ORAC score tables, and final page.
- Archived official release: `data/sources/releases/2607.10768v1-opti-agent-bench/huiliyi-XJ-Opti-Agent-Bench-6e03010.zip` (680,825 bytes; 229 files; SHA-256 `5e45ce5706bc5093230fc305485a859eb3ba627ded80f9830f51bbf7d343d262`).
- Release provenance: `data/sources/releases/2607.10768v1-opti-agent-bench/provenance.json`.
- The repository archive passed ZIP integrity checking. This audit inspected all file paths and read the registry, release policy/status, ORAC map, pipeline stages/prompts, gateway, paper-result tables, representative problems, rubrics, solvers, checkers, and generated truth artifacts. Static scripts recomputed registry/rubric/evaluator coverage, released score aggregates, and exact duplicate groups.

## Bottom line

Opti-Agent-Bench identifies a genuinely important benchmark object: the chain from a business requirement through formal model, code, execution, and report, with checks not only on each artifact but on whether adjacent artifacts agree. That is more diagnostic than a final objective value and directly relevant to realistic knowledge work.

The paper and release do not validate the stronger construct. The tasks are author-created optimization exercises written in business vocabulary, not observed or source-traced business engagements. The “anti-template” target is often an author-preferred method: the representative SDP rubric caps an exactly correct enumeration solver because it does not demonstrate SDP, while several task descriptions or hints substantially disclose the intended mathematical family. ORAC task-quality scores are criterion applications to the same authored descriptions, not independent evidence of business authenticity, expert authority, trap prevalence, alternative completeness, or professional consequence.

The empirical result is not auditable as reported. The paper says Claude leads at about 2.9, followed by Qwen3-Max at about 2.0 and DeepSeek at about 1.9, with Qwen3.5-Plus and Kimi near or below 1.0 (pp. 24–26). Recomputing the later release's 55 human/rubric rows over eleven tasks gives the opposite ordering: Qwen3-Max `3.172`, Kimi `3.106`, Qwen3.5-Plus `2.895`, pooled Claude labels `2.727`, and DeepSeek `1.986`. The release explicitly says these rows came from private draft evaluation Markdown; it includes no raw outputs, judge calls, checker observations, retries, invalid-run ledger, or script that regenerates Figure 5. The public “four-stage harness” is also not the paper's RD-Agent-style iterative system: it makes one formulation call, one implementation call, executes once in an unsandboxed host subprocess, makes one report call, and applies only shallow file/status gateway checks. It contains no released Claude Opus 4.6 evaluator or full rubric engine.

The defensible contribution is therefore a **cross-artifact semantic-consistency design and a partially inspectable post-paper task package**, not validated optimization expertise, authentic business work, industrial reliability, model capability ranking, production fitness, or readiness.

## One-sentence contribution

Opti-Agent-Bench proposes a requirement → model → code → execution → report evaluation chain with task-specific anti-template checks and adjacent-artifact consistency, but its co-authored task/method/rubric projections, uncalibrated evaluator, manuscript/release inconsistencies, and absent raw run evidence limit it to a useful instrument hypothesis rather than a validated measure of optimization R&D capability.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through narrow expansion into one consequential knowledge-work structure: translating messy requirements into mutually consistent formal and executable artifacts. Optimization is a methodological case, not a scope boundary.

The central uncertainty is:

> When does agreement across a requirement summary, mathematical model, code, execution, and report establish faithful expertise transfer rather than internal consistency with one author-preferred interpretation?

Useful completion is a claim-bounded retain/repair/test account that reuses `skill-bench`'s existing provenance, dependency, artifact-view, grader-evidence, validity, task-health, metric, and execution-isolation contracts. No optimization-specific schema is warranted.

## Research question and claim ladder

The paper asks how reliably agents perform the complete optimization R&D pipeline when given business-language tasks rather than pre-structured mathematical formulations (pp. 1–3, 7–13, 19–26).

The relevant claim ladder is:

1. **Package conformance:** required files exist, code parses/runs, and a result object has an accepted status.
2. **Artifact-local correctness:** each requirement extraction, formulation, implementation, execution result, and report claim satisfies a valid observer.
3. **Cross-artifact fidelity:** later artifacts preserve the semantics of earlier authorized requirements and actual execution.
4. **Method competence:** the system identifies and applies an appropriate optimization method, including legitimate alternatives.
5. **Professional work quality:** qualified practitioners accept the artifact package for its declared business use.
6. **Operational effect/readiness:** the package works under real data, stakeholder interaction, changing requirements, constraints, risks, and production operations.

The public gateway directly observes level 1. Selected released checkers and private human/rubric scores appear to observe pieces of levels 2–3. The evidence does not establish levels 4–6 across a defined task population.

## Methodology and system

### Task construction and unstable denominators

The manuscript contains incompatible suite descriptions:

- Contribution 1 says **nine** industrial-scale scenarios (p. 3).
- Section 6 says **twelve** benchmark tasks (p. 13).
- Section 6.2 says each displayed problem type has **4–5 distinct problem instances** in different business scenarios (p. 14), but does not define the resulting inventory or sampling unit.
- Appendix Table 2 lists twelve task names (p. 49).
- The post-v1 registry contains twelve core entries: eleven public tasks and one request-only holdout, plus 22 extras.
- The released paper table has 55 rows: five models on eleven tasks, comprising nine core tasks and two extras. It has no rows for the cable task emphasized in the main text, the robust-production core task, or the hidden task.

These are not harmless labels. “Task,” “problem type,” “business scenario,” “instance,” and “scale” are different units. Without an administered-suite manifest, the paper's average cannot be mapped to a stable population or release form.

The release itself is candidly pre-1.0. `docs/RELEASE_STATUS.md` leaves the optional smoke test and tag unchecked; `docs/RELEASE_CHECKLIST.md` leaves task-paper alignment, final problem versions, sanitation, one-task execution, gateway example, table mapping, contamination, and archival release unchecked. Its own readiness table rates several tasks Low or Medium. The commit is valuable audit evidence precisely because it exposes this unfinished boundary.

### Business semantics and expertise authority

The authors argue that replacing terms such as “setup cost” with “changeover downtime” forces genuine semantic grounding (pp. 7–10). Vocabulary can remove direct template labels, but it does not establish business authenticity. The paper reports no source organizations, observed work products, stakeholder interviews, qualified task-author roster, role-to-task mapping, incident provenance, authoring/review independence, disagreement, adjudication, rejected tasks, professional acceptance, or downstream use.

Several appendixed scenarios are generic constructions rather than requirements evidenced from practice. The portfolio example introduces CFO concern, regulatory limits, tail correlation, and a target return, then its own ORAC assessment gives it `1.00/1.00` for authenticity and trap quality while noting that the target return is missing (pp. 38–40, 52). The “future information” task is explicitly called a frontier conceptual exploration (p. 47). The release's grocery data are synthetically generated, including latent true utilities and answer-shaping risky fields. Such fixtures can support controlled semantic tests; “industrial,” “authentic,” and “real-world business problems” require a separate lineage and acceptance argument.

### Anti-template design is both a strength and a treatment confound

A fair anti-template item embeds a publicly grounded consequence that a naive but plausible method violates. Opti-Agent-Bench gets part of this right: the cable problem discloses online arrivals, deadlines, a three-plus-temporary-four reel buffer, strict substitution priority, and lexically business-shaped data. Its public checker separately notes that it cannot fully verify same-model-first behavior or workshop dynamics. This makes observer incompleteness visible.

But many “traps” are method targets rather than requirement consequences. The representative team-partition rubric awards 2.0/5 to SDP implementation alone and caps CE.1 at 2.6 for pure enumeration even if it reproduces the exact optimum 189 (pp. 34–37). That is legitimate only if the public construct is “demonstrate SDP relaxation,” not “produce the best business partition.” The task/rubric therefore mixes:

- requirement satisfaction;
- method-family recognition;
- method implementation;
- objective quality;
- artifact/report quality; and
- honesty about method limitations.

The released score comments confirm this: exact solvers are penalized for missing an intended method, while rubric-aware exposition can earn substantial credit despite weak execution. Anti-template success is consequently not pure evidence of business understanding. It can be agreement with an author-selected pedagogical method.

The paper also weakens its own anti-cue claim. Its detailed portfolio task explicitly asks for a minimax primal, dual log-sum-exp structure, biased-gradient discussion, and an efficient method (pp. 16–18). The SDP appendix labels mathematical modeling hints and explains robust SDP/CVaR reformulations. Release prompts require the agent to classify the problem as LP/MILP/QP/SOCP/MDP/stochastic optimization. These may be appropriate output requirements, but they make “no optimization jargon” and “independent identification” task-specific rather than suite-wide properties.

### Four artifacts in the paper, three generated calls in the release

The paper's evaluated outputs are problem understanding, formal model, executable implementation, and report, with C12, C23, and C34 adjacent consistency (pp. 10–13). Its agent architecture is a different three-stage runtime: parallel Data Exploration and Evaluation agents, an iterative best-of-k development loop under a time budget, then a report agent (pp. 18–19 and 49).

The public pipeline instead performs:

1. one formulation call that combines problem understanding and mathematical model into `model.md`;
2. one implementation call producing `solution.py`;
3. one direct host subprocess execution producing `result.json`; and
4. one report call producing `report.md`.

There is no Data Exploration agent, Evaluation agent, idea pool, iteration, best-of-k selection, repair loop, time-budgeted exploration, or independent Module 1 artifact. “Four-stage harness” is accurate for the release, but it is not an implementation of the paper's reported experimental architecture. Partial-module evaluation is also not packaged as a controlled intervention with exact upstream artifact identities.

### Execution and gateway evidence

The release calls its execution environment isolated, but `execution.py` creates a temporary directory and invokes `[sys.executable, "solution.py"]` with inherited process environment. It applies no container, namespace, filesystem restriction, network restriction, resource limit beyond wall timeout, dependency lock, or secret scrubbing. Generated code can access host filesystem/network/environment to the extent allowed by the parent process. Standard output and error are truncated to their last 5,000 characters; the temporary workspace is then deleted.

The gateway checks only:

- `model.md` and `report.md` exist and exceed 50 bytes;
- `solution.py` parses as Python;
- `result.json` has `status` and `objective_value`; and
- status is `optimal` or `feasible`.

It does not execute task checkers, compare objective values, validate decision variables, inspect model-code equivalence, verify report claims, apply task rubrics, run perturbations, or prevent a submission from self-declaring `optimal`. The ORAC map accurately admits that only gateway checks are currently automated and that CE.1/CE.2/ME.2 automation is future work.

### Rubrics and evaluator-agent validity

The manuscript says approximately 60% of checkpoints are automatic and 40% LLM-judged, with Claude Opus 4.6 applying binary-verifiable criteria consistently and reproducibly (pp. 10, 20–21). It reports no evaluator prompt, model snapshot, temperature, repeat policy, human comparison, agreement, calibration set, false-pass/false-fail study, alternative-solution contrast set, evidence-view truncation policy, invalid-output policy, or adjudication.

The release makes nine core `answer_rubric.md` files available but omits them for core tasks 04 and 11; the hidden task is withheld. Each of twelve evaluation README files promises `rubric.md` and `auto_eval.py`, but those filenames do not exist. Only tasks 01 and 07 include any evaluation Python, both named `eval_generalization.py`. No Claude evaluator or rubric-scoring engine exists in the archive.

The rubric text is useful design material: it names evidence sources, automatic/LLM/hybrid methods, points, expected failures, and code-report checks. Yet “binary-verifiable” is inaccurate for criteria such as appropriate complexity, credible results, business implementability, honest boundaries, clarity, and parsimony. Severity weights, metric caps, total weights (`0.35/0.40/0.25`), and success threshold `3.0` are authored policies without stakeholder loss calibration or empirical decision validation.

### Reference solvers, hidden truth, and leakage

The public release favors inspectability over clean public evaluation. It exposes most problem statements, rubrics, reference answers/solvers, optimal values, checkers, generation scripts, and grocery hidden truth. This enables audit and local development, but a search-enabled participant can retrieve target methods and checks. The README acknowledges future-training contamination and keeps one task request-only; that is a useful start, not rollout-level exposure control.

The release also withholds the cable optimizer and hidden cinema task while publishing score tables from private evaluations. Consequently, public reproduction and contamination resistance pull in opposite directions without a versioned private-form protocol, access ledger, bridge study, or evaluator firewall.

References play several roles that must remain typed:

1. construction inspiration;
2. canonical method witness;
3. optimal/near-optimal numeric witness;
4. feasibility checker logic;
5. rubric answer anchor; and
6. participant-accessible public artifact.

A solver witness proves that one implementation attains one result under one environment. It does not prove natural-language equivalence, unique method, checker completeness, professional acceptability, or resistance to direct answer retrieval.

## Evidence and reported results

### The paper's descriptive result

Figure 5 and the prose report Claude at about `2.9`, Qwen3-Max around `2.0`, DeepSeek-V3.2 around `1.9`, and Qwen3.5-Plus/Kimi near or below `1.0` (pp. 24–26, 51). The authors infer that low ME.1 reflects effective anti-template discrimination, relatively high ME.3/RE.3 shows models implement and report their own formulations more faithfully than they formulate correctly, and score profiles localize failures.

Those interpretations are plausible hypotheses. They are not supported by an inspectable trial ledger. There are no model snapshots/provider dates, task-run assignments, prompts as rendered, time budgets, seeds, repetitions, retries, invalids, execution environments, raw artifacts, evaluator records, checker records, token/cost logs, or uncertainty intervals. Five models × an unclear task inventory appears to be one observation per cell.

### The release's result surface contradicts the manuscript

The post-v1 archive includes 55 rows over eleven tasks, exactly five rows per task. Model labels vary for Claude (`claude`, `claude-rd`, `claude-4.6`, `claude-sonnet-4.6`) but form one row per task when pooled. Recomputed task-macro totals are:

| Canonicalized model | Tasks | Mean released Total |
|---|---:|---:|
| Qwen3-Max | 11 | 3.172 |
| Kimi-K2.5 | 11 | 3.106 |
| Qwen3.5-Plus | 11 | 2.895 |
| Claude labels pooled | 11 | 2.727 |
| DeepSeek-V3.2 | 11 | 1.986 |

This does not reproduce the paper ordering or levels. It also conflicts with Appendix Table 7: that table reports SDP team-partition totals `4.21, 4.10, 3.75, 2.98, 1.69`, while released rows for the same named task are `2.04, 1.91, 2.89, 1.09, 0.44` for Qwen3-Max, DeepSeek, Claude, Qwen3.5-Plus, and Kimi respectively. The README calls the released data “human/rubric evaluation scores from the draft experiments,” not gateway scores, and gives no version mapping.

The release therefore supports only: **a later private-review-derived table exists and exposes detailed failure comments**. It cannot validate Figure 5, ranks, absolute scores, anti-template effects, or model-profile conclusions. The discrepancy should be resolved by versioned result manifests, not averaged away.

### Statistical and causal limits

Even if the score table were reconciled:

- no repeated trials estimate model stochasticity or evaluator variance;
- tasks share authors, problem families, solvers, rubrics, prompts, and possibly generated templates;
- four core score rows have task-specific CE.3 missing, and 15/55 released rows omit CE.3;
- aggregate totals rely on compensatory, uncalibrated weights;
- task admission is purposive and no candidate/rejection inventory is supplied;
- anti-template traps and critical rubric checks are co-designed;
- no matched structured-language versus business-language intervention isolates formulation distance;
- no naive-template versus legitimate-alternative contrast estimates trap specificity;
- no human expert baseline anchors score meaning; and
- no uncertainty supports rank or threshold claims.

Low scores show difficulty under one authored instrument. They do not “validate” that the instrument discriminates genuine reasoning from pattern matching, because no independent construct label or controlled intervention identifies that distinction.

## Unique insight: cross-artifact consistency needs an authoritative semantic spine

Opti-Agent-Bench's deepest reusable insight is that professional artifacts should not be graded as independent documents. A plausible model, runnable script, good objective, and polished report can contradict one another. The benchmark should preserve a typed semantic spine:

```text
source/mandate + valid-time state
→ authorized requirement claim
→ public task obligation
→ formal element
→ implementation element
→ execution observation
→ report claim
→ recipient decision/use
→ bounded benchmark claim
```

Each edge needs its own relation and evidence:

- `entails` — a source or expert statement supports the requirement;
- `formalizes` — a model element implements the requirement's semantics;
- `implements` — code realizes the formal element;
- `observed_by` — execution evidence is sufficient for the property;
- `reports` — prose accurately states the observed implementation/result;
- `accepted_as_alternative_to` — a legitimate different method satisfies the same requirement;
- `contradicts` or `omits` — a downstream artifact diverges;
- `depends_on` — downstream failures may propagate from one upstream defect; and
- `licenses` — the evidence supports only a bounded interpretation.

This is stronger than pairwise “semantic diff.” Pairwise internal agreement can be wrong all the way down: a mistaken requirement interpretation may be formalized, implemented, executed, and reported perfectly. Conversely, a model and code may differ syntactically while being semantically equivalent. The root observer must therefore bind every artifact to an independently warranted requirement and admit alternative realizations.

A cross-module score is diagnostic only when it distinguishes:

1. upstream requirement error;
2. formalization omission/distortion;
3. model-code divergence;
4. execution/environment failure;
5. report-implementation divergence;
6. observer insufficiency or grader error; and
7. propagated downstream symptoms.

Without that lineage, “consistency” rewards self-consistency and double-counts one defect across adjacent checks.

## Comparison with adjacent reviewed evidence

- **DORA** also compiles a real-looking problem into a typed analytical witness. DORA shows that one gold path and endpoint do not establish authorized action or consequence. Opti-Agent-Bench adds formal-model and report links, but has weaker source/event reality and similarly lacks alternative and consequence validation.
- **SciAgentArena** demonstrates dependency-aware scientific stages and executable artifacts. Its step-wise/pipeline contrast provides stronger evidence that composition adds failure exposure. Opti-Agent-Bench names the artifact edges more explicitly but supplies no matched modular/full-pipeline experiment or propagated-failure estimand.
- **ResearchClawBench** types a target paper as construction reference while its grader mostly sees final reports. Opti-Agent-Bench aims to inspect code and execution as well, a better observer design in principle, but the released evaluator does not implement that aim and its public references create the same role/leakage ambiguity.
- **SOP-Bench** exposes procedure → data → tools → endpoint projection drift. Opti-Agent-Bench's requirement → model → code → report chain is the optimization analogue. Both can be internally consistent because tasks, preferred methods, references, and rubrics are co-generated; neither establishes professional fidelity from package coherence alone.
- **BigFinanceBench** decomposes derivations but can reward unsupported narrated evidence. Opti-Agent-Bench correctly asks for model-code-report cross-checks; however, without source-bound requirements and released evidence-complete grader views, it still cannot distinguish proof-carrying derivation from polished agreement with an answer rubric.
- Existing `skill-bench` artifact/evidence-chain machinery already has the needed homes: source and expert provenance, dependency edges, artifact views/admissibility, trace observations, root/surface attribution, task health, metric specifications, validity arguments, and execution-isolation records. This source refines how those objects should be joined; it does not demonstrate a missing optimization-specific contract.

## Reproducibility and operational realism

### What is inspectable

The later official snapshot is substantial for a young release: eleven public core problem packages, one holdout placeholder, 22 extras, data, many reference programs, task-specific rubrics, a simple OpenAI-compatible harness, aggregate score tables, two licenses, and explicit release/contamination notes. The registry enables exact inventorying. The cable checker honestly states two properties it cannot establish. These are strengths worth preserving.

### What is not reproducible

The archive cannot regenerate the paper experiments or full evaluation:

- it postdates immutable v1;
- the paper's RD-Agent-style iterative architecture is absent;
- the Evaluator Agent and full rubric engine are absent;
- raw model artifacts, traces, execution logs, grader calls, and checker outputs are withheld;
- paper/release task and score identities disagree;
- no environment image, lockfile, run manifest, repeat policy, or usage/cost ledger is supplied;
- the release's own one-task smoke test remains unchecked; and
- multiple evaluation READMEs reference nonexistent `rubric.md` and `auto_eval.py` paths.

The release has no repository test suite discoverable by standard test filenames. Some reference files contain tests or verifiers, but there is no one-command conformance/reproduction suite. Exact duplicate audits also found repeated verifier/generator files and two sets of three byte-identical `solve.py` files across differently named nonsmooth extras, which warrants semantic provenance rather than assuming domain-specific implementations from directory names.

### Operational realism

The problems use business nouns, CSV/JSON data, optimization libraries, executable code, and reports. That is more operational than mathematical QA. Yet there is no stakeholder dialogue, access control, production data lineage, live system integration, human approval, changing requirement, solver procurement/licensing constraint, monitoring, deployment, maintained handoff, or realized decision consequence. “Industrial scale” is also weakly supported: the paper acknowledges being below some million-variable MIPLIB instances, while the public suite mixes small examples, synthetic data, and incomplete references.

The host subprocess is not a safe production-like environment. It neither prevents reference/file access nor records all effects. A successful gateway status is package conformance, not a valid optimization result.

## Limitations and validity threats

### Construct and content validity

1. Business vocabulary is treated as evidence of authentic business semantics without source or stakeholder lineage.
2. No expert roster, task-level qualification, independent review, disagreement, or approval scope is reported.
3. Task, scenario, instance, scale, and problem-type counts conflict.
4. The administered experimental suite is not versioned or released.
5. Tasks are purposive and method-diverse but not sampled from optimization R&D work.
6. Anti-template checks are co-designed with tasks and references.
7. Some traps encode preferred methods rather than requirement consequences.
8. Hints and requested output taxonomies reveal mathematical families on some tasks.
9. No legitimate-alternative inventory tests whether different correct formulations are accepted.
10. No practitioner baseline or artifact acceptance study anchors professional quality.

### Measurement and grader validity

11. Claude Opus 4.6 judge consistency/objectivity is asserted without calibration or human comparison.
12. “Binary-verifiable” rubrics include subjective parsimony, clarity, credibility, appropriateness, and honesty judgments.
13. Critical caps and aggregate weights are uncalibrated to stakeholder loss or decision thresholds.
14. Pairwise consistency can reward an end-to-end coherent mistake.
15. Adjacent checks can count one propagated upstream defect multiple times.
16. Checker completeness and false acceptance/rejection are not adversarially tested.
17. Public gateway accepts self-declared feasible/optimal status and does not invoke task checkers.
18. The release omits the full rubric evaluator and two public-core rubrics.
19. Reference methods, answers, solvers, checks, and hidden truth create public-form leakage.
20. Missing/not-implemented CE.3 handling is not tied to a frozen aggregation policy per form.

### Comparison, reliability, and causal validity

21. Paper and release score rankings materially conflict.
22. Appendix team-partition scores materially conflict with the release rows for the same named task.
23. Model snapshots, budgets, retries, invalids, prompts, and dates are absent.
24. No repeat trials or evaluator repeats support reliability.
25. No task-clustered uncertainty or inferential analysis is reported.
26. Claude labels change across tasks and may represent different configured systems.
27. No matched intervention isolates business language, trap presence, iteration, or cross-module grading.
28. Low ME.1 does not independently identify template anchoring.
29. Score profiles are descriptive categories, not validated causal localization.
30. A `3.0` success threshold has no empirical acceptance or loss basis.

### Release, execution, and operational validity

31. The release commit postdates the paper and is explicitly unfinished.
32. Paper architecture and public harness are materially different.
33. Host subprocess execution is not filesystem/network/resource isolation.
34. Environment, dependencies, and solver versions are not frozen per trial.
35. Temporary execution state is deleted and stdout/stderr are truncated.
36. Raw results and evaluator evidence are private, preventing replay.
37. Release READMEs promise absent evaluation files.
38. Reused identical reference code across differently named tasks weakens task-specific implementation claims without lineage.
39. Code/data licenses are declared, but full legal texts are URL pointers rather than complete bundled licenses.
40. No production use, recipient adoption, business effect, safety, reliability, or readiness is observed.

## Transferable benchmark-design lessons

### Retain

1. **Artifact-chain unit of work.** Evaluate requirement extraction, formal model, implementation, execution, and report as linked artifacts.
2. **Adjacent consistency checks.** Preserve model-code and code-report divergence as explicit failure signatures.
3. **Requirement-specific traps.** Use plausible naive paths whose failure follows from disclosed requirements.
4. **Plural observations.** Keep feasibility, objective quality, method fidelity, code quality, robustness, report fidelity, and limitations separate.
5. **Reference roles.** Preserve witnesses, checkers, task references, and participant-visible sources as distinct objects.
6. **Honest checker limitations.** Record what an automatic observer cannot prove.
7. **Partial-module interventions.** Supplying frozen upstream artifacts can localize a transition if artifact identity and treatment are controlled.

### Repair

1. Bind each hidden or critical requirement to source/expert authority, valid time, public basis, and acceptance state.
2. Separate outcome obligations from required-method demonstrations; do not penalize a valid alternative method under an outcome claim.
3. Give each artifact element a stable semantic ID and reciprocal crosswalk across requirement, model, code, execution, and report.
4. Record observer views and abstain when code, logs, references, or source evidence are insufficient.
5. Preserve root defect, propagation edges, and surface symptoms instead of adding dependent failures as independent points.
6. Calibrate judge decisions on positive, negative, legitimate-alternative, coherent-wrong-chain, and polished-report/incorrect-code contrasts.
7. Freeze suite/task/instance/configuration identities and release scheduled/started/valid/invalid/retried denominators.
8. Run in an actually isolated, hash-pinned environment and retain artifacts, state effects, usage, and complete logs.
9. Keep public development forms separate from private/semi-private scored forms and record search/reference exposure.
10. Bridge every score to an explicit criterion, construct, or decision claim; never infer professional readiness from an aggregate.

### Test

A cross-domain validation slice should create matched artifact chains for at least two unrelated knowledge-work families, each with:

- one fully correct chain;
- one shared upstream misunderstanding propagated consistently through all artifacts;
- one correct model with code omission;
- one correct execution with stale/fabricated report claim;
- one legitimate alternative formulation/implementation;
- one observer-insufficient case; and
- one artifact that passes a shallow endpoint while violating an authorized requirement.

The instrument should demonstrate that source-bound local checks and cross-artifact edges identify the correct boundary, accept the legitimate alternative, abstain on insufficient evidence, and avoid double-counting propagated failures. This is already representable in existing `skill-bench` contracts; it should be implemented when a suitable diverse pilot needs it, not as a new optimization subsystem.

## Concrete repository actions

1. **No new queue task.** The evidence refines existing source/expert provenance, artifact/check crosswalk, dependency, artifact-view admissibility, trace/root-cause, task-health, metric, validity, and execution-isolation machinery. A new “cross-module” schema would duplicate those objects before a concrete pilot exposes a missing invariant.
2. When the next artifact-chain pilot is authored, add the matched coherent-wrong-chain and legitimate-alternative cases described above to its conformance plan.
3. During canonical consolidation, cite this review as evidence that internal cross-artifact consistency is necessary but cannot substitute for an authoritative semantic spine, alternative acceptance, observer calibration, or claim validity.
4. Do not use the paper's Figure 5 ranking or the later release's 55-row ranking as a stable model comparison until a versioned administered-suite manifest, raw trials, evaluator records, and reconciliation are available.

## Claim boundary

This review establishes that immutable v1 presents an important cross-artifact evaluation design and that a timing-bounded later official release contains a meaningful but unfinished task/harness package with material paper/release discrepancies. It does **not** establish that the tasks are authentic business work, that ORAC is a validated validity framework, that the evaluator is accurate or reliable, that any named model has the reported optimization capability, that anti-template scores isolate genuine reasoning, or that any system is professionally valid, industrially reliable, production-fit, safe, or ready.