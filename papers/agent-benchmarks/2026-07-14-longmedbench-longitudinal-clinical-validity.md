# Paper Review: LongMedBench — Longitudinal Clinical-Decision Validity

- **Paper:** https://arxiv.org/abs/2607.09322v1
- **Authors:** Yanzhen Chen, Zihan Xu, Xiaocheng Zhang, Zhiting Fan, Weiqi Zhai, Hongxia Xu, Zuozhu Liu
- **Date read:** 2026-07-14
- **Venue / source:** arXiv preprint
- **Version read:** immutable v1, 10 July 2026
- **Local PDF:** `data/papers/pdfs/2607.09322v1-longmedbench.pdf` (10 pages; SHA-256 `2fd5ebeb574607c4b53642d1cb6acaa73e5ed21d2d1651cf981c209b9be46ff8`)
- **Local text:** `data/papers/text/2607.09322v1-longmedbench.txt` (SHA-256 `155d93c1a26921abb89048221513f165ad818053b70b5450a2d168a49eebff58`)
- **Author-owned repository inspected:** https://github.com/Yanzhen-CN/LongMedBench/tree/05c956b97070fe7839f6051dbf18225cbde5f86b (commit `05c956b97070fe7839f6051dbf18225cbde5f86b`; tree `b799b63082ea2ba08058311259e91f56c5ed5bb3`)
- **Release provenance:** `data/sources/releases/2607.09322v1-longmedbench/provenance.json`
- **Tags:** longitudinal-evaluation, EHR, temporal-reasoning, retrospective-oracle, decision-validity, patient-clustering, release-audit

## One-sentence contribution

LongMedBench transforms high-utilization MIMIC-IV inpatient histories into fact retrieval, chronology reconstruction, and recorded-next-event prediction tasks, but its own no-history result and released generator show that the nominal “decision” suite measures agreement with retrospective care traces more directly than necessity or quality of long-horizon clinical reasoning.

## Why this matters for skill-bench

LongMedBench tests a generally important benchmark-design hypothesis: a long record does not create a long-horizon construct merely by being present. Historical evidence must be both **available before the decision** and **necessary for a defensible consequence**. The benchmark is a useful negative case because its baseline without historical memory scores `0.45`, while event-memory, note-memory, RAG, and Mem0 conditions remain approximately `0.40–0.44` on the reported decision aggregate (Table 5, p. 8). The paper interprets this primarily as an agent-memory limitation. An equally important instrument interpretation is that the selected questions and retrospective labels may not require long-range evidence.

This advances charter objectives A and B without making medicine the project scope. The reusable question is cross-domain: when a task claims longitudinal knowledge work, can an intervention on prior state change the justified action while holding immediate context fixed? If not, the task may be a long-input task, a retrospective sequence-completion task, or a local-state task—not evidence of longitudinal decision competence.

## Research question and claim boundary

The paper asks whether contemporary long-context LLMs and memory systems can retrieve, temporally organize, and use multi-visit EHR histories for later clinical decisions. It contributes three task families over note, event, and current-visit contextual memory (Sections 2.1–2.2, pp. 3–5):

1. fact-based QA with explicit or relative temporal references;
2. event-, visit-, and joint-fragment sorting;
3. next-action, action-argument, and six-hour discharge prediction.

The evidence supports narrower claims than the title and abstract imply:

- the authors created code for projecting MIMIC-IV v3.1 records into temporally bounded text contexts;
- the paper reports large performance differences between timestamp-visible event sorting and timestamp-hidden visit sorting;
- the reported memory treatments change factual retrieval much more than the decision aggregate;
- the pre-v1 repository makes the construction and decision-scoring logic partially inspectable.

It does **not** establish interactive long-horizon clinical decision-making, clinical appropriateness, patient benefit, safe care, clinician-equivalent reasoning, general medical competence, professional validity, production fitness, or deployment readiness. No agent action changes a patient trajectory. The “environment” replays an archived record, and decision labels are subsequent recorded events or discharge timing rather than independently adjudicated appropriate actions.

## Methodology and system reconstruction

### Cohort and event projection

The paper starts from MIMIC-IV v3.1 and retains patients with at least 15 admissions and complete admission/discharge records. It keeps abnormal laboratory results and parses structured admissions, prescriptions, procedures, microbiology, radiology notes, and discharge notes into patient event streams (Section 2.1, pp. 3–4). The methodology reports **355 patients, 6,999 visits, 19.72 visits per patient**, and 44.91 events per visit; the abstract, Introduction, and Conclusion instead say **335 patients** (pp. 1–3, 9). The visit count divided by the reported mean is consistent with approximately 355, not 335.

This is a highly selected utilization cohort, not a sample of typical longitudinal care. Requiring at least 15 inpatient admissions and complete discharge-note coverage emphasizes repeatedly hospitalized patients and institutions/documentation patterns represented in MIMIC. Removing normal laboratory values also changes the available evidence: absence from the projected stream can mean normal, unretained, unavailable, or unmeasured unless those states remain typed.

The event representation is `{action, timestamp, arguments, observation}`. Three memory views are constructed (pp. 4–5):

- **note memory:** prior visit summaries;
- **event memory:** flattened prior events with visit boundaries discarded;
- **contextual memory:** the current visit rewritten as assistant action / environment feedback turns, retaining events before a reasoning timestamp.

The public repository confirms that current-visit contexts are synthetic replays. `tasks/agentic_decision/build_context.py` emits an assistant action before each recorded observation and can use an LLM to infer imaging parameters and clinical “reason” text. The resulting reasoning text is generated after the underlying event is known, so it is not an observed clinician trace. Even if no future event is exposed, generated rationales can encode hindsight-derived cues and must be treated as a transformation, not clinical-process evidence.

### Fact retrieval

A target event is sampled and queried either with its timestamp/ID or by relative position. The event-memory window is varied around the target visit, including full history (Section 2.2, p. 4). Answers are graded by LLM/keyword matching according to Figure 2; the manuscript does not specify the judge model, prompt, adjudication, reliability, or invalid-output policy.

Table 2 reports only qwen-turbo long-context windows and Mem0, despite a `Model` column. Full-history performance falls sharply relative to short windows, while Mem0 is strong on some explicit targets and poor on imaging and relative tasks (pp. 6–7). This is useful configured-package evidence but not a clean memory-capacity estimate: window size also changes prompt length, truncation pressure, and distractor distribution, and Mem0 changes retrieval/query behavior.

### Temporal reasoning

The three temporal tasks use archived order as the oracle (pp. 5, 7):

- **Visit Cloze:** remove several events but retain timestamps and ask the model to place them;
- **Visit Sorting:** remove timestamps from five summaries and ask for their original order;
- **Joint Sorting:** split five admissions into ten admission/discharge fragments, pair them, and order them.

Kendall's `τ` is reported over 6,776 cloze, 765 visit-sorting, and 2,878 joint-sorting items. Explicit timestamp placement reaches `0.969`; the best reported visit-sorting and joint-sorting means are `0.424` and `0.330` (Table 3, p. 7). Standard deviations are item-level dispersion, not uncertainty for model comparisons.

The lower timestamp-hidden scores do not uniquely identify implicit clinical temporal reasoning. Multiple admissions can be clinically exchangeable from summary text, while generated/parsed summaries may omit the cue that makes one chronology identifiable. Original order is a valid archive fact but not proof of a uniquely inferable ordering. No clinician annotation establishes uniqueness, partial-order equivalence, or which errors matter for a later decision.

### “Long-horizon decision” construction

The manuscript describes three formats (pp. 5–6): next action (`T3-N`), action argument (`T3-A`), and discharge within six hours (`T3-D`). The release makes their oracle semantics much clearer:

- `sample_decision_points` chooses two predecessor indices per visit for which the **next recorded event** maps to a supported action;
- `T3-N` labels that next event's coarse action class as the correct option;
- `T3-A` treats same-action events in the next 24 hours as targets with exponential time-decay credit;
- `T3-D` labels whether the recorded discharge timestamp lies within six hours, and deliberately samples timestamps close to discharge toward a configured 70% Yes ratio.

Thus “most appropriate next step” means “the next encoded action in this record,” not “an independently validated appropriate action under the visible evidence.” A clinician could choose a safe alternative, ask for information, defer action, or make a better decision than the historical trace and be scored wrong. Conversely, predicting documentation and workflow regularities can score well without supplying a clinical warrant.

The action-argument option distractors are LLM-generated using the history **and ground truth** (`tasks/agentic_decision/generate_questions.py`). That can make the instrument easier or harder through model-specific lexical contrast and creates generator–grader dependence. The released scorer uses case-insensitive substring containment, sums credit for every predicted option, clips at one, and does not penalize extra wrong options. A model can therefore inflate multi-option scores by selecting many choices. Provider exceptions are recorded but omitted from score arrays, so aggregate denominators silently become valid-response complete cases (`tasks/agentic_decision/eval_utils.py`; `agents/llm_agent/agentic_decision/eval.py`).

### Configured systems and aggregation

The paper names qwen-turbo, deepseek-v3.2, deepseek-v3.2-thinking, and gpt-5-mini, plus naive context, RAG using `text-embedding-3-small`, and Mem0 (Section 3.1, p. 6). It says default configurations are used. Provider snapshot, endpoint, run date, prompt hash, retries, budgets, seeds, patient set, invalid calls, and attempt counts are not reported. Table 4 lists gpt-5-mini at 400K context even though the surrounding text says all models are limited to 128K (p. 8).

The release defaults decision evaluation to `CLIP_PAITENT=True` and IDs 1–50 excluding 8, apparently 49 patient files, while the paper never states this denominator. It also defaults construction to demo mode for five patients, and no frozen paper configuration is supplied. Scores are micro-averaged over successful question calls within patient runs and then logged; no patient-clustered estimator or paired memory-treatment analysis is released.

## Evidence and results interpretation

### Retrieval results support task-specific access effects

The full-history qwen-turbo factual average falls from `0.88` at a three-visit window to `0.42` in explicit questions and from `0.80` to `0.34` in relative questions. Mem0 reaches `0.99` on explicit Lab-T and `0.98` on medication but `0.07` on imaging and a `0.33` relative average (Table 2, pp. 6–7). These observations support heterogeneous retrieval-package behavior under the authors' projected records. They do not show that Mem0 preserves clinically sufficient history, because retrieval success is measured against generated fact questions rather than future action consequences.

### Temporal results mix timestamp use, identifiability, and archive reconstruction

Deepseek-v3.2-thinking rises from `0.316` to `0.969` relative to non-thinking on timestamp-visible cloze, while all systems perform much worse with timestamps removed (Table 3, p. 7). The paper reasonably concludes that explicit timestamps help. Its stronger language about “realistic multi-visit” implicit reasoning is not identified because task ambiguity and summary projection fidelity are unmeasured. A chronology task should permit partial orders or clinician-adjudicated equivalence when the visible record cannot uniquely order visits.

### The decision ablation threatens the construct, not only the systems

Across Table 5, the no-history baseline is `0.45`. Injecting two or five event/note visits yields `0.43–0.44`; RAG-event yields `0.40`, Mem0-event `0.44`, RAG-note `0.44`, and Mem0-note `0.41` (p. 8). No uncertainty accompanies these differences. The authors explicitly state that task design must amplify deeper reasoning requirements and decision interdependencies.

That admission should be elevated into the main validity conclusion: **the reported decision suite has not demonstrated history necessity**. If immediate context or class priors recover the retrospective label, near-zero memory gains cannot distinguish a weak agent from a weak longitudinal intervention. Before comparing memory architectures, tasks need prospective pairs where an earlier evidence atom changes the defensible action and where deleting, perturbing, or substituting that atom predictably changes performance.

## Official-release audit

The complete author-owned commit was inspected. Its HEAD predates arXiv v1 by 15 days, but the manuscript does not link a repository or identify a commit; it is therefore a plausible pre-v1 implementation snapshot, not proven exact experiment code.

### What is released

The 81-entry archive contains 52 Python files covering:

- MIMIC extraction and cohort construction;
- event, note, and current-context projection;
- factual, temporal, and decision question generation;
- long-context, RAG, and Mem0 evaluation paths;
- prompts, option generation, scoring, and result summarization;
- pinned Python package versions.

This is enough to inspect important oracle, visibility, sampling, and scoring choices.

### What is absent or broken

The archive contains no MIMIC-derived patient files, generated benchmark questions, frozen split/manifests, prompts/configuration used for the paper, raw predictions, invalid-run logs, aggregate result records, or scripts that regenerate the paper tables. Access restrictions can legitimately prevent derived EHR release, but they still leave the reported denominators and results unauditable.

Static compilation found one syntax error among 52 Python files: `agents/rag_agent/agentic_decision/eval.py` line 537 has an invalid nested f-string, so the released RAG decision evaluator cannot import unchanged. The README recommends `python build_sequence.py`, but that file is absent. `EHR_pipeline/embedding.py` is empty. Defaults do not identify paper execution: cohort construction starts in five-patient demo mode, while decision evaluation clips to 49 IDs. These defects make the “reproducible pipeline” claim aspirational rather than demonstrated end to end.

## Unique insight

LongMedBench exposes a crucial distinction among four things often collapsed into “long-horizon evaluation”:

1. **history volume:** many prior visits are present;
2. **history access:** the system can retrieve an earlier fact;
3. **history necessity:** that fact changes which action is justified now;
4. **consequence validity:** the action is judged against an authoritative outcome, not merely the historical next event.

The paper strongly instantiates the first, partially measures the second, and does not establish the third or fourth. This distinction generalizes to finance, operations, research, legal, and office work. A long source pack or persistent workspace is not longitudinal evidence unless prior state participates in a falsifiable decision boundary.

A useful cross-domain longitudinal task should bind:

`prior evidence atom + authority/valid time → later visible state → admissible action set and alternatives → counterfactual history intervention → realized or expert-adjudicated consequence`.

Retrospective next-event agreement is a **behavioral imitation label**. It can be useful for predicting workflow, but it must not inherit a normative “most appropriate” label without expert review, alternative-path policy, and evidence that the visible state was sufficient.

## Limitations and validity threats

1. **The cohort denominator conflicts:** 335 patients in the abstract/Introduction/Conclusion versus 355 in the processing section; 6,999/19.72 supports approximately 355.
2. **Long history is not shown necessary:** no-history matches or exceeds every reported memory condition on the decision aggregate.
3. **Decision labels are retrospective behavior:** the next recorded action and actual discharge time are not independent judgments of appropriateness.
4. **The environment is replay, not interaction:** agent choices do not alter tests, treatment, patient state, delay, cost, or harm.
5. **Alternative valid care paths are scored wrong:** no clinician-approved action set, contraindication policy, or adjudication procedure is reported.
6. **Current-context sufficiency is uncontrolled:** decision points are sampled from mappable next events rather than selected for long-range dependence.
7. **Transformation hindsight is possible:** generated assistant rationales and inferred imaging parameters are derived from completed EHR events.
8. **Normal results are removed:** absence conflates normal, unavailable, unmeasured, and filtered evidence.
9. **The selected cohort is atypical:** ≥15 admissions with complete discharge records limits population and setting claims.
10. **Temporal ground truth may be non-identifiable:** timestamp-hidden summaries are not clinician-checked for unique ordering or acceptable partial orders.
11. **Distractors are generated with ground truth visible:** option artifacts can encode the generator's contrast strategy and share lineage with the instrument.
12. **Weighted scoring is gameable:** substring matching, additive option credit, clipping, and no false-positive penalty reward over-selection.
13. **Discharge prevalence is authored:** a 70% Yes target and narrow pre-discharge sampling make T3-D a constructed timestamp classification distribution.
14. **Patient dependence is ignored:** many questions share each patient, visit, projection code, and source record; no patient-clustered uncertainty is reported.
15. **Invalid calls disappear from aggregates:** exceptions are retained as records but omitted from score arrays and denominators.
16. **Configured systems are under-specified:** default model configurations, mutable endpoints, prompts, budgets, retries, and run dates are absent.
17. **The context-limit description conflicts:** Table 4 gives gpt-5-mini 400K while text says all models are capped at 128K.
18. **No clinician validation or rater reliability is reported:** task wording, action appropriateness, temporal uniqueness, and consequence relevance remain author/code oracles.
19. **Release completeness is low:** no derived data, questions, exact run manifest, trajectories, or results permit independent table replay.
20. **Released code is not end-to-end runnable unchanged:** one RAG evaluator has a syntax error and the advertised build script is missing.
21. **Costs and operational burden are absent:** token usage support exists in code, but the paper reports no cost, latency, failure rate, or human-review burden.
22. **Safety claims are unsupported:** no harmful alternative, omission severity, escalation, uncertainty communication, or realized patient consequence is measured.

## Reproducibility and operational realism

Reproducibility is **moderate for understanding the intended construction logic and poor for reproducing the paper's experiments**. MIMIC-IV v3.1 is obtainable under credentialed access, and the pre-v1 repository exposes substantial projection/question/evaluation code with pinned Python dependencies. Exact paper reproduction still requires the frozen cohort manifest, derived question IDs and hashes, LLM-generated transformations/distractors, model endpoints and prompts, patient subset, seeds, retries, invalid calls, output rows, and table-generation code. The broken RAG evaluator and missing runner must also be repaired without silently changing the instrument.

Operational realism is bounded. The substrate contains real de-identified hospital documentation and genuine temporal irregularity. Yet the tasks are static multiple-choice/ordering probes over retrospective records, not clinical work with responsibility, consultation, authorization, uncertainty, resource constraints, side effects, changing patient state, or outcome follow-up. The release's generated action/reason traces simulate an interface; they do not preserve observed clinician cognition or workflow.

## Transfer to skill-bench

### 1. Require a longitudinal-necessity witness

For any task claiming history-dependent decision work, identify at least one prior evidence atom whose removal or controlled substitution changes the admissible action set while immediate context remains fixed. Report no-history, irrelevant-history, correct-history, stale-history, and contradictory-history controls. If they are equivalent, classify the task as long-input or local-state rather than longitudinal-decision evidence.

### 2. Separate historical behavior from normative action

Type the oracle as one of: recorded behavior, policy/rule, expert-adjudicated acceptable set, realized outcome, or counterfactual consequence. A recorded next event can be a target for workflow prediction but must not be named “most appropriate” without authority and alternative-path evidence.

### 3. Preserve time and information availability

Every evidence atom should carry source, event time, record time, availability time, valid interval, projection/transformation lineage, and visibility. Generated summaries or rationales must not inherit clinician authority. Normal, unavailable, unmeasured, filtered, delayed, and contradictory states must remain distinct.

### 4. Admit partial orders and plural procedures

Temporal graders should accept declared partial orders or equivalence classes when evidence does not determine a unique sequence. Decision graders should encode contraindicated, acceptable, preferred, ask/inspect, abstain, and escalate outcomes rather than one historical witness.

### 5. Analyze at the trajectory cluster

Freeze patient/workspace/entity splits before question generation. Report eligible, attempted, valid, invalid, and scored denominators by configured system; use paired trajectory-level effects and cluster-aware uncertainty. Prevent many easy questions from one trajectory from dominating the estimand.

### 6. Test consequence sensitivity, not only retrieval

A successful retrieval probe establishes access. A decision probe should show that adopting the retrieved evidence improves a downstream artifact, state, or expert-adjudicated decision and should localize failures among availability, retrieval, temporal interpretation, uptake, action, and consequence.

### 7. Keep strict claim ceilings

Even a valid synthetic counterfactual would support history-sensitive package performance under a frozen instrument. Clinical/professional validity, patient benefit, safety, production fitness, and readiness would still require qualified experts, represented settings, calibrated harms, workflow integration, and prospective or otherwise defensible outcome evidence.

## Action items for repository

- [x] Read the complete immutable v1 PDF/text and verify all tables and claims against the manuscript.
- [x] Pin and inspect the complete author-owned pre-v1 code snapshot with explicit manuscript-link and timing limits.
- [x] Record the 335/355 cohort contradiction, 49-patient release default, no-history result, retrospective oracle, scoring defects, invalid-call handling, and release failures.
- [x] Map findings to existing longitudinal, evidence-state, trace, artifact/state, validity, task-health, metric, participation, and safety machinery.
- [ ] Build one cross-domain longitudinal-decision necessity conformance slice with history interventions, typed oracle authority, alternative valid paths, clustered denominators, and explicit consequence claim ceilings; do not use clinical data or claim professional validity.
