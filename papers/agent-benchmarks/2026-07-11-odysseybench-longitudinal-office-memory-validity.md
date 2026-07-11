# OdysseyBench: dialogue-conditioned office execution mixes memory, planning, and narrow state predicates

**Source type:** Deep review of the complete immutable arXiv v1 paper and a pinned official post-paper repository snapshot  
**Paper:** Weixuan Wang et al., *OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows* (arXiv:2508.09124v1, 12 August 2025)  
**Immutable paper:** https://arxiv.org/abs/2508.09124v1  
**Local PDF:** `data/papers/pdfs/2508.09124v1-odysseybench-evaluating-llm-agents-on-long-horizon.pdf` (SHA-256 `03e58608779097c9a46a2d02c734169ddfcbf7cf1afe41a5c007fa559f07a6d5`, 21 pages)  
**Full extraction read:** `data/papers/text/2508.09124v1-odysseybench-evaluating-llm-agents-on-long-horizon.txt` (SHA-256 `ec70c55a080c1ae71e759d16475cd3ddeee66d56c0734098388582573c419bef`)  
**Official release:** https://github.com/microsoft/OdysseyBench  
**Pinned archive:** `data/sources/releases/2508.09124v1-odysseybench/microsoft-OdysseyBench-3389881.tar.gz` (commit `3389881fa9e1dbc6e13c5b0706da8007e88d09d4`, SHA-256 `6b9dfd7617543025fd49980c8ecec304bfdd3402bb132ffe4b38589d2a5edeca`)  
**Release provenance:** `data/sources/releases/2508.09124v1-odysseybench/provenance.json`

> **Timing boundary.** The archived commit is dated 10 March 2026, seven months after arXiv v1. It is inspectable current-release evidence, not manuscript-time byte identity. The paper names no commit; the release contains no paper-result trajectories and requires a fresh OfficeBench checkout to import testbeds.

## Review judgment

OdysseyBench's strongest contribution is a useful experimental separation: the agent receives only a high-level intent while task-critical facts are distributed through a synthetic interaction history, then must convert selected facts into consequential office state. That couples evidence selection to action more directly than retrospective memory QA.

But the benchmark does not isolate “long-term memory” or “long-horizon workflow” as a causal capability. The histories are generated backward from the hidden task and rubric; prior assistant turns simulate acknowledgments rather than executed experience; all history is supplied at evaluation time; and the final score conjoins mostly narrow OfficeBench-style predicates. A failure may originate in retrieval, recognition, synthesis, planning, tool use, file mutation, or grader mismatch. Conversely, passing selected keywords/cells/file-existence checks does not establish a complete, usable, safe professional outcome. OdysseyBench supports a bounded claim about dialogue-conditioned predicate completion in a synthetic API-mediated office sandbox—not occupational realism, persistent memory, or deployment readiness.

## One-sentence contribution

OdysseyBench turns hidden task details into dialogue-distributed evidence that must drive office-state changes, but its generated histories and narrow final-state checks measure a configured evidence-to-action pipeline rather than memory or professional workflow competence alone.

## Why this matters

The source tests a general benchmark-design problem central to skill-bench: whether requirements scattered through prior interactions are not merely recalled but correctly transformed into consequential artifact and workspace state. Its design and release defects clarify the instrumentation needed to separate evidence retrieval from action validity.

## Research question and contribution

The paper asks whether agents can extract task-critical information from multi-day interaction histories and execute multi-application office tasks, and whether retrieval/storage representation affects success (pp. 1–3, 6, 9–11). It contributes:

1. **OdysseyBench+**: 300 OfficeBench tasks transformed into histories and high-level intents by a generator/verifier loop;
2. **OdysseyBench-Neo**: 302 newly generated task, criterion, ground-truth-memory, query, and dialogue packages grounded by agents exploring the office environment;
3. **HomerAgents**: two automated generation pipelines;
4. long-context and RAG baselines over raw or summarized histories;
5. final-filesystem evaluation across Word, Excel, PDF, email, and calendar stores.

The unique methodological move is not merely longer prompts. It is **requirement withholding with a disclosed retrieval basis**: the public query intentionally omits details, while generated dialogue carries those details and final state tests whether the agent used them. This resembles realistic delayed requirement accumulation, but only if every hidden check is actually entailed by accessible history and if the history's source authority is legitimate.

## Methodology and system reconstruction

### OdysseyBench+: task-preserving dialogue expansion

HomerAgents+ takes an OfficeBench atomic description, asks GPT-4.1 to produce a high-level intent and at least five days/100 turns of dialogue, and iterates against a GPT-4.1 verifier up to five times (paper §3.1.1 and Algorithm 1, pp. 4–5; Appendix A/B.1, pp. 16–17). The generator must split every atomic requirement exactly once across user turns and preserve filenames, numbers, applications, and times while adding “as much casual chitchat as possible.” Prior assistant turns say “will do” or “noted” but must not execute the work.

This preserves an answer basis, but creates an authoring confound: the history is a rubric-shaped encoding of the original task, not an independently observed work history. Dialogue length and days are generator constraints, not empirically validated temporal dependency. The release audit confirms all 300 Plus task/history pairs and the 93/95/112 one/two/three-app split. Histories average 27.85 sessions and 317.85 turns in the current release; their fragmentation originates in transformed OfficeBench conversations, not repeated environment interaction.

### OdysseyBench-Neo: joint task/history/grader synthesis

HomerAgents-Neo uses GPT-4.1 agents in four phases: planning, environment exploration, generation of task description/intent/subtasks/evaluation criteria, and five-day dialogue generation (Algorithm 2 and §3.1.2, pp. 4–6). The hidden `ground_truth_memory` is deliberately expanded into chat. The prompts require criteria drawn from a fixed evaluator library, precise filenames/cells/calendar values, and enough dialogue evidence to reconstruct the hidden task while withholding intermediate solutions (Appendix B.2, pp. 18–21).

The 302 released Neo records preserve task descriptions, criteria, query sentences, ground-truth memories, and dialogues. Current histories average 5.04 sessions and 368.64 turns. This is highly inspectable lineage, but task, evidence, and grader are co-generated. The same generation logic chooses what matters, how it is said, and what will count. No independent domain expert or workflow sample establishes that those requirements are professionally salient.

### Validation and human study

Automated validation first excludes unsupported criterion types, then retains tasks o3 can complete both from the full task description and from intent plus subtask information (§3.2.3, p. 8). Five GPT-4.1 judges vote on completeness and non-leakage; reported joint pass rates are 72.67% for Plus and 83.77% for Neo (Table 2, p. 8). Three native-English annotators post-edit and remove incoherent tasks. The paper does not report pre/post-edit counts, agreement, adjudication, task-level judgments, annotator training, or independence from the authors.

Two human annotators complete a “randomly sampled subset” of Neo tasks with 91.43% success (Table 3, p. 9). The paper omits subset size, assignment, repeated attempts, timing, compensation, application familiarity, uncertainty, and whether annotators saw the same retrieval interface. This is weak solvability evidence, not a human-level comparison or professional-validity study.

### Agent and environment contract

The agent receives a query plus either the full dialogue history or RAG-selected context, then issues typed actions against a Dockerized textual office environment. The complete testbed is saved and checked post hoc (§3.2.1, pp. 6–7). Current `configs/base_config.yaml` specifies 50 steps, and the environment records action/observation history and copies final `/testbed` state.

Release inspection shows broad shell command execution inside the container, mutable external model APIs, copied private configuration, and no demonstrated network-denial policy. The repository has no tracked testbeds: its README instructs users to clone current OfficeBench and copy them in. Therefore task JSON is pinned by the archive but source-state identity is not self-contained. No result trajectories reproduce Tables 4–7.

## Evaluation and release audit

The paper reports exact, fuzzy, and execution-based checks, with task success only when all criteria pass (§3.2.1, p. 7). The current release contains 1,278 predicate invocations across 602 tasks:

| Split | Tasks | Checks | One-check tasks | Dominant checks |
|---|---:|---:|---:|---|
| Plus | 300 | 598 | 153 | containment 286; file existence 226; cell value 33 |
| Neo | 302 | 680 | 106 | containment 314; file existence 234; cell value 107 |

The evaluator lowercases and substring-matches all requested keywords, treats path existence as success, checks selected spreadsheet cells, and supports exact workbook value comparison on the active sheet. These views can establish selected predicates but usually miss artifact coherence, formulas, formatting, preservation of unrelated state, provenance, recipient correctness, safe side effects, and handoff usability. The released Plus record `tasks/3-99/subtasks_plus/0.json` illustrates both undermeasurement and an authoring defect: it asks for `revenues.docx` but checks existence of misspelled `revenuse.docx`, and checks only existence of both outputs.

The current release also contradicts the paper's claim that unsupported criteria were filtered out. Four Neo tasks invoke function names absent from `utils/evaluate.py` and from `evaluation/task_evaluator.py` imports: `evaluate_excel_sheet_exist`, `evaluate_doc_contain`, six instances of `evaluate_keyword_exist`, and `evaluate_file_contains_keywords`. The evaluator catches the resulting exception and returns failure. This is fail-closed but confounds agent failure with instrument defect. It also shows why successful oracle execution is not enough: mutable release changes require fresh criterion-dispatch conformance.

## Evidence and results

Table 4 reports single aggregate pass rates for ten model configurations. On Plus, o3 scores 56.19% overall and GPT-4o 33.67%; on Neo they score 61.26% and 51.99% (p. 9). All models fall from one- to three-app strata, especially on Plus. App count, however, bundles task family, number of required values, action path, output artifacts, representation changes, and generated-history structure. It is not an identified coordination effect.

The RAG experiment uses GPT-4o and `text-embedding-3-large` (§4, p. 9). For Plus, full context scores 33.67%; the best reported chunk-summary condition scores 33.33%. For Neo, full context scores 51.99%, session-summary top-5 53.64%, and chunk-summary top-25 56.29% (Tables 5–6, pp. 9–10). These are configured-pipeline contrasts. Summaries are model-generated representations with different token counts; retrieval top-k, segmentation, representation, and context budget all vary. No repeated runs, paired uncertainty, retrieval recall against ground-truth-memory spans, summary faithfulness audit, or fixed-token matched ablation is reported. The paper's causal language that summaries “capture task essence” and “streamline reasoning” is stronger than the evidence.

The manual failure analysis names missed files, missed actions, incorrect tools, and inaccurate planning, then plots failed outcomes by file type (pp. 11–12). It gives no sample size, coding protocol, rater agreement, mutually exclusive labels, or earliest-cause procedure. A missed file may itself follow retrieval failure; a wrong tool may follow a mistaken plan; a grader defect may masquerade as failure. The categories are useful surface symptoms, not causal diagnoses.

Costs are not reported. Table 7 reports mean execution steps by condition, but not failed/invalid handling, latency, model tokens, generation cost, environment setup, retries, or grader cost. “Long-horizon” therefore refers mainly to dialogue length and multi-step execution, not measured calendar persistence or operating burden.

## Unique insight

OdysseyBench exposes a useful **evidence-to-consequence bridge** absent from pure memory QA: historical text is valuable only when selected facts correctly change an artifact or operational store. Yet this bridge has separable links:

1. evidence was available in an admissible source;
2. the agent accessed the relevant span;
3. it recognized the span as authoritative and applicable;
4. it reconciled all required details;
5. it formed a valid plan;
6. it executed the correct state transition;
7. it verified the artifact/state;
8. the grader observed enough state to support the claimed consequence.

A binary pass collapses this chain. The transferable repair is not a benchmark labeled “memory,” but **requirement-lineage instrumentation**: each hidden consequence should link to public-basis spans, access/adoption evidence, intended state delta, realized state, and an admissible grader view. Then matched interventions can vary evidence access, representation, or action support without changing the task and rubric.

## Limitations and validity threats

1. **No persistent-memory treatment.** Histories are supplied at evaluation; agents do not accumulate them over time, experience intervening outcomes, or demonstrate retention, forgetting, updating, or recovery.
2. **Backward-generated history.** Dialogue is expanded from hidden task requirements. It tests recovery of planted facts, not naturally emerging commitments, contradictions, corrections, or authority changes.
3. **Task/evidence/grader co-design.** Neo jointly generates all three, permitting criterion-shaped evidence and evaluator-cue regularities.
4. **Workflow realism unsupported.** Prior assistant “work” is explicitly simulated and not executed (p. 6). Five days/100 turns are prompt constraints; no observed occupational workflow or expert validation supports realism.
5. **Construct mixture.** Retrieval, recognition, reasoning, planning, tool use, artifact creation, and grading all determine pass rate. App count and history length do not isolate any one.
6. **Narrow consequence views.** Containment, existence, and selected-cell checks can pass incomplete or professionally unusable artifacts and usually ignore collateral changes.
7. **Instrument defects.** At least one Plus filename mismatch and four Neo records with unavailable evaluator functions are present in the pinned release.
8. **Outcome-conditioned selection.** o3 success is an admission gate, coupling task survival to one configured system and excluding valid hard cases that it cannot solve.
9. **Thin human evidence.** Unknown sample size and assignment, two annotators, no agreement/uncertainty, no expert or recipient study.
10. **No reliability analysis.** Apparently one attempt per model/task; no seeds, repeated stochastic runs, confidence intervals, or lineage-clustered uncertainty.
11. **Representation confounds.** RAG studies jointly vary summarization, segmentation, retrieval volume, and token budget; they do not isolate semantic compression.
12. **Mutable/incomplete release.** Post-paper commit, externally imported testbeds, mutable models/dependencies, no paper outputs, and no exact run manifest.
13. **Safety undermeasured.** Email/calendar/shell actions are consequential; authorization, secret handling, recipient boundaries, confirmation, and rollback are not scored.
14. **Public contamination.** Tasks, hidden descriptions, memories, dialogues, and graders are public; no held-out/private refresh protocol is described.

## Reproducibility and operational realism

**Inspectability: moderate-high for task lineage.** All 602 task/history records, generation prompts, environment adapters, memory code, and evaluator code are available in the pinned later snapshot. This permits static auditing and reveals criterion drift.

**Exact reproduction: low.** There is no manuscript commit, container digest, OfficeBench dependency revision, complete source testbed archive, provider snapshot, seed ledger, per-trial outputs, or result table. Current reproduction requires proprietary APIs and reconstructing source state from another moving repository.

**Operational realism: bounded.** Agents manipulate real office file formats and persistent stores through textual APIs, but requirements and histories are synthetic, prior work is not executed, broad shell access exceeds normal office boundaries, and professional handoff/authorization is absent. This is a dialogue-conditioned office-state sandbox, not evidence of longitudinal workplace performance.

## Comparison with adjacent reviewed benchmarks

### Versus OfficeBench

OfficeBench supplies the underlying typed office stores and many Plus task/check definitions, but exposes self-contained atomic instructions. OdysseyBench's genuine addition is to hide details in dialogue and require evidence selection before the same kind of state transition. It does **not** repair OfficeBench's narrow grader views, app-count confounding, mutable environment, or missing professional provenance; it inherits them and adds generated-history validity as another layer (`papers/agent-benchmarks/2026-07-11-officebench-cross-application-office-validity.md`).

### Versus LongMemEval-V2

LongMemEval-V2 isolates bounded evidence gathering before a fixed reader, making retrieval/representation failures more inspectable, but does not test downstream action. OdysseyBench tests action consequence but collapses evidence selection and execution into one pass bit. Together they motivate two linked estimands: (a) grounded evidence delivery and (b) held-out state/action benefit. Neither alone establishes persistent learning or experienced-colleague competence (`papers/agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md`).

## Transferable benchmark relevance to skill-bench

### Retain

- High-level public intent plus fair, traceable requirement evidence distributed across prior interactions.
- Cross-representation evidence-to-state tasks, not final-answer QA alone.
- Full final-state capture and deterministic predicates where evidence views are sufficient.
- Separate raw, retrieved, and transformed context identities and budgets.
- Ground-truth-memory records as authoring lineage—not as proof of realism.

### Repair

1. Link every hidden check to exact public-basis spans, source authority, valid time, and applicability; reject checks supported only by hidden task descriptions.
2. Add evidence-access and adoption events before action, then required/permitted/forbidden state deltas, preservation invariants, verification, and handoff checks.
3. Use matched evidence interventions on the same task: full admissible evidence, retrieval interface, faithful summary, planted omission/distortion, and no-evidence control.
4. Score retrieval, reconciliation, plan validity, state transition, artifact quality, collateral effects, verification, and cost separately before aggregation.
5. Run evaluator-dispatch and oracle-witness conformance on every released task version; classify unavailable graders and typoed paths as instrument invalidity, not agent failure.
6. Replace app-count claims with typed transition burden and matched task ladders.
7. Validate generated histories against observed workflows or consented experts, including authority, corrections, contradictions, and evolving requirements.
8. Use repeated trials and cluster uncertainty by source task, generated lineage, workflow family, and environment state.
9. Pin source-state archives, container/tool/model/harness identities, network policy, resets, traces, retries, and all costs.
10. Keep claims bounded to evidence-to-action behavior until expert/recipient studies establish artifact and workflow validity.

These requirements already have homes in the benchmark-bundle, expertise-transfer, artifact-view, trace, persistent-workspace, execution-validity, task-health, metric-monitoring, longitudinal, and validity-argument contracts. The existing experience-memory transfer conformance proposal from the LongMemEval-V2 review is the right nonduplicate implementation path; OdysseyBench adds the need for hidden-requirement lineage and instrument-defect cases. No new queue task is warranted.

## Concrete changes

1. **Consolidation:** compare OdysseyBench with OfficeBench and LongMemEval-V2 in the workspace/memory synthesis as complementary evidence-view and action-consequence instruments; do not classify OdysseyBench as proof of persistent memory.
2. **Validation:** extend the already proposed experience-memory transfer conformance slice with a hidden requirement supported by one admissible history span, one distractor, one correction/supersession, one summary omission, one collateral mutation, and one unavailable grader. Require separate retrieval and state-consequence outcomes.
3. **Release gate:** add static criterion-dispatch, file-locator, and oracle-witness checks to task-health admission before trials; instrument-invalid tasks must not enter capability denominators.

## Claim boundary

OdysseyBench v1 provides evidence that selected 2025 model-agent configurations often failed conjunctions of task-specific predicates when required details were distributed through synthetic dialogues, and that particular summarized-retrieval configurations sometimes outscored raw-history baselines. It does **not** establish persistent long-term memory, a causal benefit from semantic compression, realistic occupational workflow coverage, professional artifact quality, safe autonomous office operation, human parity, or deployment readiness.
