# KWBench: unprompted problem recognition is a missing construct, but v1 does not isolate it

**Source.** Ankit Maloo, *KWBench: Measuring Unprompted Problem Recognition in Knowledge Work*, arXiv:2604.15760v1 (17 April 2026), read in full from the immutable 37-page local PDF and local text extraction. Paper: <https://arxiv.org/abs/2604.15760v1>. PDF: `data/papers/pdfs/2604.15760v1-kwbench-unprompted-professional-problem-recognition.pdf` (SHA-256 `b30c...fff33`). Text: `data/papers/text/2604.15760v1-kwbench-unprompted-professional-problem-recognition.txt`. Release provenance: `data/sources/releases/2604.15760v1-kwbench/provenance.json`. I also inspected the complete linked fasteval snapshot at commit `4341928` and project-site snapshot at `8c6d9c7`. The Hugging Face repository metadata was reachable at revision `d339cdd...`, but its files were manual-gated: anonymous clone and immutable file retrieval failed. Dataset-row claims below therefore come from the paper, not an independent dataset audit.

## Bottom line

KWBench identifies a genuinely important omission in agent evaluation: a professional often has to decide **what problem is present and whether the requested frame should be rejected** before executing a named workflow. Its best design move is not the game-theory taxonomy itself, but the backward chain from a predicted plausible wrong path to a decisive cue, an appropriate consequence, and a non-compensatory check. That is directly useful to skill-bench.

The paper nevertheless overclaims construct isolation. Its cold condition jointly requires cue extraction, domain knowledge, skeptical stance, hypothesis generation, mechanism reasoning, decision selection, and artifact execution. It reports no framed condition, no human baseline, no judge reliability, no expert agreement, and no item-level validity study. The mandatory criteria often require a prescribed action—not merely recognition—and all-or-nothing gating makes one noisy criterion sufficient to relabel the entire trajectory as a recognition failure. V1 therefore establishes **low success under an unprompted, author-defined critical-consequence rubric**, not that unprompted problem recognition alone is the binding cause.

## One-sentence contribution

The research question is: can a model infer the governing structure of a professional situation from raw inputs without being told which framework applies? KWBench offers 223 tasks, 185 said to derive from professional incidents and 38 adapted from other benchmarks, spanning adversarial dynamics, judgment, and domain execution (pp. 5–6). Each task includes a deliverable prompt, often reference files, private structured annotations, and fifteen binary rubric criteria. The benchmark deliberately withholds a problem-type label and uses a minimal system prompt (p. 5).

This advances beyond specified-work benchmarks in one precise way: the model may need to dispute the surface request. It also makes tacit reading practices explicit through `ground_truth`, `key_insight`, `failure_analysis`, `common_errors`, and `model_must_recognize` fields (pp. 7–8). Those fields are more reusable than the leaderboard because they expose an expertise-to-evaluation decomposition.

## Methodology and system

### Task and expertise construction

The paper maps scenarios to six game-theoretic patterns, then says practitioners with direct or analogous experience validated realism, senior difficulty, and reasoning through structured consultations (pp. 3–7). It reports averages of 12.2 extracted signals, 8.3 common errors, and 5.7 pre-rubric criteria per task (p. 8), but does not report practitioner count, domains per practitioner, recruitment, credentials, consultation protocol, disagreements, compensation, or which tasks each person reviewed. “Practitioner validated” is thus not reproducible provenance.

Rubrics are generated independently by at least three LLM families, then synthesized by the author against metadata (p. 8). Five mandatory, five good-to-have, and five ideal criteria are judged separately. Any mandatory failure sets score to zero; otherwise score is `0.40 + 0.35*g + 0.25*i` (pp. 11–12). The mandatory tier is designed backward from predicted dangerous wrong paths: 74% of tasks have at least one explicit trap-avoidance criterion (p. 9).

### Evaluation

Sixteen models from ten organizations receive code execution on every task; a subset of tasks enables web or shell (pp. 6, 14). Gemini 3 Flash judges each criterion independently with response, task, and code access (p. 12). Every model is run three times, and the run with the best aggregate score is reported (p. 12). This is an explicitly favorable-selection estimand, not expected reliability. Some models have unequal denominators because persistent errors remain after retries (p. 14).

The linked harness supports asynchronous provider calls and a legacy rubric path. In inspected code, `RubricJudgeScorer` dispatches each criterion through `judge_rubric`; `score_rubric` supplies the hard gate. The judge prompt allows task artifacts and a REPL, not merely text (`fasteval/eval/scorers.py:151–212`; `eval/core.py:45–72`). The current snapshot also defaults the asynchronous path separately from the legacy full-judging path, and its KWBench plugin defers prompt construction to provider adapters (`eval/benchmarks/kwbench.py:20–55`). Because the paper does not name an evaluated commit, this is linked implementation evidence, not proof of exact run configuration.

## Evidence and what it supports

The best reported model passes all mandatory criteria on 61/219 tasks (27.9%) and has a zero-inclusive mean of 22.6%; the second passes 47/223 (21.1%) (p. 14). Among the top eight, the mean pass-set Jaccard is 29.3%; 44 tasks are uniquely passed by one model, and a greedy union covers 113 tasks (pp. 15–18). Gated-out outputs still satisfy many non-mandatory criteria (pp. 18–19). These observations support three bounded claims:

1. under this judge and rubric, models frequently miss at least one author-designated critical criterion;
2. additive scoring would hide these failures behind auxiliary quality;
3. configured models have heterogeneous pass sets.

They do **not** prove that recognition is binary, that the gate is valid, or that ensembling is operationally reliable. Conditional-score convergence is conditioned on passing a selected gate and compresses scores mechanically into `[0.4, 1]`; it cannot validate the gate. Low pass-set overlap can result from criterion noise, stochastic runs, domain mixture, denominator differences, or model/harness interactions. A router covering the oracle union of pass sets is not a deployable router: no routing policy, selector evidence, cost, or false-routing rate is tested.

The strongest item-level illustration is the toxic-employee PIP (Appendix C). The situation, private interpretation, predicted mistakes, five mandatory criteria, and purported 16-model failure are all shown. Yet even this example demonstrates construct contamination. Mandatory checks include solitary and binary goals, documentation, explicit litigation framing, and avoiding 360 feedback (pp. 32–36). Those require legal/HR judgment and artifact choices in addition to recognizing litigation risk. Alternative legitimate practices are not independently adjudicated. The claim that each consequence is “documented” is not backed by incident locators, legal authority, or expert-agreement evidence.

## Unique insight

The transferable insight is a **situation-to-intervention chain**, not “use game theory everywhere”:

`surface request → latent candidate problem → decisive cue(s) → competing framing → consequence if ignored → evidence-gathering/action change → artifact/check`

Existing benchmarks often begin at the final arrow. Existing skill-bench critical-incident and cognitive-task-analysis work already records traps and cues, but KWBench makes the missing discriminant explicit: test whether the agent changes its inquiry or action *before* the benchmark names the issue. This should be a distinct score family rather than inferred from final artifact failure.

A fair recognition item also needs a **contrastive framing set**. The same cue should appear in cases where the latent framing applies and near-neighbor cases where it does not. Otherwise “always be adversarial,” “always mention litigation,” or template recall can pass. KWBench v1 reports no such contrast set.

## Limitations and threats to validity

1. **No recognition intervention.** The authors acknowledge there is no identical framed condition (p. 22). Without cold versus minimally framed versus fully specified conditions, recognition cannot be separated from solving ability or execution.
2. **Criterion contamination.** Mandatory criteria mix noticing, explanation, prescribed decisions, and artifact details. The paper’s own rubric principle “test action, not acknowledgment” (Appendix A) conflicts with calling the gate a recognition measure.
3. **Single-author synthesis and opaque experts.** Practitioner roles and disagreements are absent. Tagging a task with game theory before practitioner review can anchor interpretation rather than validate it.
4. **No human baseline or alternate-valid-path adjudication.** A severe conjunctive gate has unknown expert false-fail rate. Several examples make contestable universal claims (for example, prescribed short-seller response or legal strategy) without authority locators.
5. **Single model judge, no reliability.** Binary prompts reduce response space but do not establish accuracy. No blinded expert labels, repeated judge calls, agreement, calibration, or criterion-level error estimates are reported.
6. **Best-of-three selection.** Selecting the best aggregate run estimates availability under repeated favorable attempts. Per-task stability and paired uncertainty are absent; the selection also complicates pass-set overlap.
7. **Weak uncertainty.** Results are descriptive. Tasks cluster by originating scenario, domain, rubric author, and pattern; repeated runs and judge calls add dependence. No clustered intervals or paired tests are supplied.
8. **Tool/configuration ambiguity.** Universal code availability does not imply arithmetic cannot cause failure. Web/shell availability differs by task, and the linked release explicitly says systematic harness testing is not yet done. The paper does not preserve exact component hashes or run artifacts.
9. **Leakage and adaptation.** Thirty-eight items are adapted from public benchmarks, and some incidents are documented publicly (pp. 5–6, 22). No provenance split, phrase audit, or contamination probe is reported. Private annotations and rubric terms may also encode label templates if later exposed.
10. **Scope skew.** The “cross-domain” set is heavily weighted toward Western corporate strategic skepticism; healthcare has four tasks (p. 11). The paper acknowledges this skew (p. 22). This is not broad professional construct coverage.
11. **Dataset reproducibility is currently incomplete.** Public API metadata exposes a 223-row file manifest and revision, but manual gating prevented independent inspection of task rows, rubric counts, reference files, or the two requested end-to-end released lineages. Appendix B/C examples were traced only through the paper.
12. **Paper/release reporting inconsistency.** The paper says 16 models, while the linked site says 17 in one passage. This does not overturn the core descriptive result but reinforces the need for immutable result tables and exact run manifests.

## Reproducibility and operational realism

The full paper and linked code are available, and the paper gives unusually concrete rubric mechanics. That is meaningful progress. But a reproduction still lacks the gated task corpus, exact run-time commit, provider snapshots, temperatures, outputs for all repetitions, criterion judgments, usage/cost, and adjudication data. The harness snapshot’s mutable provider adapters and split async/legacy paths mean “same harness” is not a stable configured system identity.

Operationally, a mandatory consequence gate is plausible for safety- or loss-critical work, but only when each criterion has: public basis, authority/provenance, applicability conditions, alternative-valid-path policy, evidence-view sufficiency, calibrated false-fail/false-pass costs, and abstention for insufficient evidence. KWBench v1 supplies a compelling author hypothesis for consequences; it does not supply those validation layers.

## Why this matters

This review advances charter objectives **A/B/C** through expansion that exposes a construct missing from specified-task benchmarks and translates it into cross-domain machinery. The useful artifact is this review plus pinned source provenance. The clarified uncertainty is whether a benchmark can distinguish situation framing from execution. The answer is: not with a single cold final-artifact gate.

For skill-bench, represent problem recognition explicitly:

- a private candidate-problem record with decisive and disconfirming cues, provenance, scope, severity, and alternate framings;
- separate observations for cue detection, framing/hypothesis quality, evidence-gathering choice, decision/action, and final artifact consequence;
- three matched conditions: cold situation, minimal problem-class frame, and fully specified execution request;
- positive/negative near-neighbor cases to penalize indiscriminate skepticism;
- expert adjudication of alternate valid framings before a recognition gate can become critical;
- paired, task-clustered uncertainty across repeats, with judge invalidity separated from substantive failure;
- a validity argument that licenses only the rung supported: “detected this planted cue,” then “selected appropriate inquiry,” then “avoided consequence,” not broad professional competence.

This maps into existing expertise-transfer, benchmark-bundle, task-health, validity, metric, participation, and plural-judgment contracts; a new schema would be duplication.

## Transferable design

The matched-condition and staged-observation design above is the reusable transfer: isolate cue detection, framing, inquiry, action, and artifact consequences rather than inferring recognition from a final gate.

## Concrete repository actions

1. **Do not add a new contract task.** Extend a future diverse pilot’s validation plan with a small cold/minimal-frame/fully-specified × positive/negative-neighbor design, scored at cue, framing, inquiry, action, and artifact stages. This is a refinement of existing pilot/validity machinery.
2. **Before importing any KWBench item, obtain gated dataset access and expert revalidation.** Preserve item/revision hashes; trace source incident → cues → alternatives → consequence → rubric; independently adjudicate legal/professional claims. Do not treat paper appendices as sufficient authority.
3. **Require pass-set claims to survive repeatability and judge checks.** Estimate task-level stability, paired condition effects, clustered uncertainty, and expert-vs-judge error before interpreting low overlap as jagged expertise or proposing routing.
