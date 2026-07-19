# Adaptive task elicitation: hard-example discovery is not yet model profiling

**Paper:** Davis Brown, Prithvi Balehannina, Helen Jin, Shreya Havaldar, Hamed Hassani, and Eric Wong. *Adaptively profiling models with task elicitation.* EMNLP 2025; arXiv:2503.01986v3.

**Primary source:** [arXiv abstract](https://arxiv.org/abs/2503.01986v3) · [immutable v3 PDF](https://arxiv.org/pdf/2503.01986v3) · local PDF: [`data/papers/pdfs/2503.01986v3-adaptive-task-elicitation.pdf`](../../data/papers/pdfs/2503.01986v3-adaptive-task-elicitation.pdf) · layout-preserving full text: [`data/papers/text/2503.01986v3-adaptive-task-elicitation.txt`](../../data/papers/text/2503.01986v3-adaptive-task-elicitation.txt)

**Release evidence:** [`data/sources/releases/2503.01986v3-adaptive-evals/provenance.json`](../../data/sources/releases/2503.01986v3-adaptive-evals/provenance.json) records the first public official repository snapshot, commit `9731dab376193474e98189c12cd834e5d31035e4`, and six immutable Hugging Face dataset revisions. The repository snapshot is official but postdates arXiv v3 and publication; it is not evidence that these were the exact paper-run bytes.

**Review scope:** Full-paper deep review plus static audit of the pinned official repository and all six released Parquet tables. No paid model calls were made and the paper's headline scores were not reproduced.

## Relevance and decision

**Tier A question, Tier B evidence.** The paper asks a question central to `skill-bench`: can an evaluator use a system's prior successes, failures, and reasoning traces to generate model-specific probes rather than administer only a fixed form? Its strongest contribution is a practical adaptive loop and a useful warning that benchmark averages can hide localized weaknesses. But its evidence does not establish a calibrated capability profile. It primarily establishes that a coupled generator–target–judge configuration can find additional examples on which the target fails, under selected domains and acceptance rules.

The key validity repair is:

`initial response record → generator-conditioned candidate → validity/novelty admission → target response → repeated/independent response evidence → candidate failure family → stable model-specific contrast → bounded capability profile`

No edge inherits the next. In particular, a generated hard item is not automatically a valid item; target failure is not automatically a stable weakness; a natural-language cluster label is not automatically a task construct; and target-relative success does not by itself show model specificity.

**Charter decision filter.** This review advances objectives A–C by deepening benchmark-generation research, converting it into durable validity rules, and identifying one bounded validation experiment. The concrete evidence is the immutable full paper, official pinned release, source-code audit, released-table census, and this review. It clarifies when adaptive generation supports hard-example discovery versus model profiling. This is **expansion with consolidation consequences**, not a commitment to legal, truthfulness, politeness, or safety benchmarking. Useful completion means preserving the positive adaptive mechanism while specifying the missing crossed controls, independent item validation, repeated target measurement, provenance, and claim ceiling needed before `skill-bench` uses it.

## One-sentence contribution

The paper proposes **task elicitation**: use a profiling model to inspect an evaluated model's answers and chain-of-thought traces on an initial benchmark, generate new questions intended to expose the inferred weakness, filter those questions, evaluate the target on them, and summarize accepted failures as natural-language “tasks” or behavioral descriptions (pp. 1–4). The intended gain is not merely a lower score. It is a more diagnostic, model-specific profile than one obtained from static benchmark sampling.

The paper applies variants of the loop to six settings:

- legal reasoning from four MAUD/LegalBench classification tasks;
- TruthfulQA multiple choice;
- cultural politeness classification in ten languages;
- cyberharassment generation;
- HarmBench jailbreaking;
- probabilistic-forecast consistency.

This breadth is useful because it shows that “adaptive evaluation” is not one intervention. The legal, truthfulness, and politeness paths generate candidate questions from prior correct/incorrect examples; the safety paths optimize harmfulness or jailbreak outcomes; forecasting iteratively searches for conjunction/conditional-probability inconsistencies. Inputs, outputs, validators, target outcomes, and construct claims therefore differ substantially. The family supports a common search pattern, not a single interchangeable metric.

The distinctive contribution is **response-conditioned evaluation construction**. Existing dynamic-generation work can search for difficult or diverse items in a domain; this method conditions generation on one target's observed response record and asks whether that information produces better probes than random/static or nonadaptive generation. This is directly relevant to finding localized failure signatures in knowledge work, where a fixed form may miss combinations of hidden requirements, contradictions, source conditions, and artifact conventions.

## Methodology and system

### 1. Initial evidence and adaptive context

For legal reasoning and TruthfulQA, the evaluator first runs the target on an existing dataset and retains the question, correctness, and optionally chain-of-thought. The profiler receives sampled correct and incorrect examples and is instructed to infer specific failure modes and generate a distinct, difficult question (paper pp. 2–4; release `solvers/solver_adaptive_legal_refactor.py`, lines 106–190 and 261–285; `solvers/solver_adaptive_truthfulqa_refactor.py`, lines 197–316).

The official legal runner defaults to one positive and two negative examples and performs 30 epochs per configured pairing (`runners/legal.py`, lines 29–50 and 133–163). The TruthfulQA runner uses the same one/two context default but five epochs (`runners/truthfulqa.py`, lines 29–46 and 126–159). The paper studies further variants: randomizing labels, randomizing example selection, embedding retrieval, supplying target reasoning, generator reasoning, iterative regeneration, and generator identity.

### 2. Candidate generation and admission

Generated multiple-choice candidates must parse into the expected JSON/sample representation. Optional self-check and LLM-judge stages assess answerability/correctness. A novelty check compares a candidate to context questions, using either `difflib.SequenceMatcher` or sentence-transformer cosine similarity. The default threshold in the refactored solvers is 0.6 (`utils_elicitation/novelty.py`, lines 13–52; legal solver lines 193–218; TruthfulQA solver lines 149–171).

The target is then evaluated on the candidate. The retry loop can seek a candidate that is valid, novel, and—when configured to use the target as an in-loop checker—answered incorrectly. The core release implementation is important: if no target-failing candidate is found, `generate_question_with_retries` retains the **last valid novel candidate** as a fallback, even when the target answered it correctly (`solvers/adaptive_utils.py`, lines 368–511). Thus the released generated tables appropriately contain both correct and incorrect target outcomes; “adaptive question” does not mean “elicited failure.”

The paper's human-quality check samples 100 questions and compares GPT-4o judging to five human annotations per question, reporting 96.2% agreement and Krippendorff's alpha 0.76 (p. 8). This is useful item-admission evidence, but the manuscript does not supply the 100 item IDs, annotator records, item-level labels, adjudications, or uncertainty around agreement.

### 3. Outcomes and profile synthesis

The central item-level outcome is whether the generated question is valid/novel and the target fails it. The paper's “adaptive wins” statistic counts generated questions that pass novelty and are answered incorrectly, and compares adaptive with static/nonadaptive generation (pp. 5–7). For safety-generation settings, continuous harm or jailbreak scores replace multiple-choice error. For forecasting, the search target is inconsistency among forecast triples rather than benchmark correctness.

For the natural-language profile, the system generates behavior descriptions from failures, deduplicates them, embeds or clusters them, and chooses a concise set intended to explain the response corpus via perplexity reduction (pp. 3–4 and Appendix A). This is a second model-generated instrument layered on top of generated items. The paper presents qualitative task descriptions, but does not validate profile-label stability, coverage, causal fidelity, or usefulness to an independent decision maker.

## Transfer and comparators

The paper compares adaptive generation against several controls, including static questions, rewording, random generation, randomized correct/incorrect labels or sampling, and variants without target reasoning. It also generates against one model and tests resulting questions on others (pp. 5–8). Transfer is often asymmetric: questions elicited from stronger models can expose weaker models, while questions elicited from weaker models do not reliably expose stronger ones. The authors explicitly note that transfer is “neither uniform nor monotonic” (p. 8).

That asymmetry is compatible with at least three mechanisms:

1. model-specific diagnosis;
2. generic difficulty calibration to the source model's strength;
3. generator-specific style or answer-key artifacts that affect model families differently.

The study does not fully identify among them because it lacks a balanced crossed design over target history, generator identity, candidate batch, receiving model, and blinded independent validity adjudication.

## Evidence and findings

### What the experiments support

1. **Adaptive context can improve hard-example yield.** Across the paper's domains, adaptive variants frequently produce more target failures or stronger adversarial outcomes than fixed/reworded/random baselines (pp. 5–7). This is credible evidence that prior response records can be useful search context.

2. **The treatment is not reducible to topical prompt generation.** Randomizing the correct/incorrect assignment or removing parts of the response context often weakens performance, and supplying target reasoning can help in some settings (pp. 5–7, Appendix C). This suggests that the profiler uses response-contingent information, although it does not prove semantic uptake of the inferred failure mechanism.

3. **Profiler strength matters.** Stronger profiling models generally achieve higher elicitation rates, but no profiler dominates every target/domain pair (pp. 7–8). The observed result belongs to a profiler–target–prompt–validator configuration, not to “adaptive elicitation” abstractly.

4. **Generated probes can transfer, but transfer does not equal specificity.** Strong-to-weak transfer is common and weak-to-strong transfer is limited (p. 8). That is useful practical evidence for curating hard suites. It weakens a pure target-specific interpretation unless crossed controls show an additional same-target advantage after conditioning on generic difficulty.

5. **Scale did not visibly collapse diversity in one setting.** Appendix D reports a cultural-politeness scaling run where “adaptive wins” increased smoothly with the number of generated examples and the authors found no evidence of diversity collapse (p. 20). This is a narrow observed-setting result, not a general saturation analysis: the novelty metric and candidate distribution define what collapse could be seen.

6. **Cost is substantial.** The paper estimates roughly one million input tokens and 10,000–100,000 output tokens for 50 successfully generated questions, with generation cost driven by repeated retries and long contexts (Limitations, p. 9). This is operationally relevant because the denominator is successful candidates, not all attempts, validated stable weaknesses, or useful profile claims.

### Static audit of the official released tables

The six pinned Hugging Face snapshots contain 24,343 rows in total. The three multiple-choice generation tables expose why denominators must stay typed:

| Released table | Rows | Target marked incorrect (`score=I`) | `is_incorrect=true` | Exact duplicate question strings |
|---|---:|---:|---:|---:|
| Legal | 10,444 | 2,660 (25.5%) | 1,998 (19.1%) | 175 (1.7%) |
| TruthfulQA | 1,350 | 484 (35.9%) | 301 (22.3%) | 35 (2.6%) |
| Politeness | 9,800 | 4,850 (49.5%) | 2,566 (26.2%) | 1 (<0.1%) |

`score` and `is_incorrect` are not interchangeable. The latter appears to incorporate later filtering/judging, but the dataset cards do not provide a complete machine-checkable derivation for every row. A benchmark must preserve attempted, parse-valid, judge-valid, novel, target-incorrect, repeated-incorrect, admitted, and profile-used counts separately.

The safety tables are also heterogeneous. The 500-row cyberbullying release contains 381 rows (76.2%) with score 0, null iteration, and null `reasoning_and_question`; its `question` field consequently has 380 repeated null-string representations. The 857-row HarmBench table has complete question/reasoning fields and no exact duplicate question strings. The 1,392-row forecasting release has 256 repeated question titles (18.4%), partly expected because each forecast structure contributes multiple probability questions. Raw “duplicate counts” therefore require task-specific semantics rather than one global quality rule.

These counts are independent static observations over the pinned release, not reproductions of paper figures. They demonstrate that the release is valuable enough to audit, while also showing that one aggregate elicitation or novelty rate would erase meaningful lifecycle states.

## Unique insight for `skill-bench`

The paper's deepest reusable insight is not “generate harder questions.” It is that **a failed work product can become evidence for choosing the next discriminating probe**. For knowledge-work benchmarks, that could mean generating or selecting a follow-up scenario after observing a missed contradiction, unsupported source choice, incorrect decision threshold, provenance break, or artifact-convention violation.

However, `skill-bench` should not let the same model-generated hypothesis author the follow-up, answer key, validity judgment, and profile label without crossed evidence. Adaptive generation creates a powerful outcome-conditioned instrument. It can increase diagnostic resolution, but it can also amplify:

- answer-key errors that happen to defeat the target;
- target formatting/parsing quirks;
- generator stereotypes about a model;
- prompt leakage from exposed reasoning traces;
- generic difficulty rather than a target-specific weakness;
- repeated variants of one surface form;
- selection on stochastic single-sample failures;
- profile labels that redescribe selected examples without predicting untouched behavior.

The appropriate object is an **adaptive probe lineage**, not merely a generated task:

`source construct and authority → initial item/form → target attempt and observer → candidate failure hypothesis → generation inputs and generator → candidate bytes/answer source → independent validity/admissibility → novelty relation → target repetition → crossed-target contrast → frozen failure-family label → untouched confirmatory probe → licensed profile claim`.

This complements rather than duplicates nearby work:

- **TASTE** begins from tool sequences and tests coverage through generated tasks; adaptive elicitation begins from target responses and tests conditional hard-example search. Both need semantic diversity and attrition ledgers.
- **GrowLoop** co-evolves cases and rubrics from human seeds; adaptive elicitation co-evolves questions from model outcomes. Both risk outcome-conditioned construct drift and need frozen bridges plus untouched confirmation.
- **ANCHOR** and **Auto-Benchmark Audit** emphasize artifact/task defects; adaptive search makes those defects especially dangerous because a bad key that defeats the target is preferentially retained.
- **Agentic CLEAR** dynamically summarizes trace issues; adaptive elicitation dynamically summarizes generated failures. Both require label stability, evidence-span links, invalid-case handling, and prospective usefulness tests before a generated taxonomy becomes a diagnostic claim.

## Limitations and validity threats

### 1. “Profiling” outruns the demonstrated construct

The paper measures the yield of valid/novel target failures and presents plausible natural-language summaries. It does not estimate a target's capability distribution over a defined task population, sensitivity/specificity of profile claims, calibration, test–retest stability, or decision utility. Because generation deliberately conditions on prior failures, the resulting distribution is not a prevalence sample. The warranted claim is targeted failure discovery under a configured search policy.

### 2. Model specificity is not isolated from generic difficulty

Strong-to-weak transfer and profiler-strength effects are expected under generic hard-item generation. The paper's randomization ablations show that response context matters, but not that it yields target-specific probes beyond difficulty matching. A decisive design would swap target histories while holding generator, domain, budget, and receiving-model panel fixed, then test source-target interaction on independently validated candidates.

### 3. Stochastic target failure is selected, not stabilized

Candidates are often admitted after one target response. Selecting on an incorrect stochastic draw inflates apparent weakness yield. Re-evaluation on the same target and untouched variants is needed to distinguish stable failure signatures from response variance. Paper-level sample counts do not substitute for item-cluster uncertainty because many questions share generators, contexts, tasks, and templates.

### 4. Validity and correctness rely heavily on model judges

The reported human agreement is encouraging but narrow and incompletely released. Human annotators appear to assess generated-question quality, not the full construct/profile inference. No independent legal experts are reported for generated MAUD questions, despite subtle contract interpretation and invented option/key risks. The release's judged tables retain substantial gaps between raw target error and `is_incorrect`, showing that adjudication materially changes the eligible set.

### 5. Novelty is an observer, not a construct guarantee

Character similarity and embedding cosine can reject paraphrases or admit semantically redundant questions. The batch reducer also preferentially retains incorrect items when similar correct/incorrect candidates collide (`utils_elicitation/novelty.py`, lines 130–170), which is defensible for adversarial discovery but makes the final set outcome-conditioned. Diversity over embeddings does not establish coverage over hidden requirements, contradiction types, source rules, or consequences.

### 6. Exposed chain-of-thought complicates interpretation

The profiler may exploit target reasoning traces, but those traces are model-generated text, not privileged internal state or a faithful causal explanation. Their usefulness can reflect lexical cues, self-diagnosed uncertainty, answer leakage, or prompt interaction. The paper's reasoning ablations should be read as treatment effects of exposing these texts, not evidence that the system recovers the model's causal failure mechanism.

### 7. Cross-domain aggregation is inappropriate

Legal answer correctness, truthfulness multiple choice, cultural politeness classification, generated harassment, jailbreak success, and probabilistic consistency are different constructs with different harm directions and validators. The breadth supports mechanism portability, not one universal profiling score or professional-readiness inference.

### 8. Human and operational baselines are incomplete

The paper does not compare the profiler with qualified humans given equal source evidence and budget, nor report expert time, correction burden, false alarms, or profile usefulness. Token estimates omit full validation and maintenance costs. There is no evidence that a domain expert, benchmark author, auditor, or model developer makes a better decision from the generated profiles.

### 9. Release timing and executable reproducibility are bounded

The official repository is commendably broad—86 Python files, tests, scripts, and six pinned datasets—but the first public commit is post-paper. The release check verifies structure/importability, not the paper tables. `scripts/run_paper_repro.sh` covers only TruthfulQA, legal, and politeness, invokes current provider endpoints, requires paid credentials, and does not reconstruct all six domains or published figures. The checked runner interfaces also show drift: the generic reproduction script is a convenient rerun entry point, not an immutable paper-result reconstruction.

### 10. Source-level defects constrain result reconstruction

The static release audit found code paths that deserve caution:

- the core retry loop falls back to the last valid novel candidate after exhausting attempts, so acceptance must not be inferred from candidate presence;
- `adaptive_truthfulqa_scorer` returns `CORRECT` when no generated sample exists (lines 24–34), a fail-open default that can inflate accuracy if exercised;
- the base runner's transfer mixin is an unimplemented `pass` (`runners/base.py`, lines 214–223);
- one PRESS scorer is explicitly a placeholder with “evaluation pending” (`scorers/scorers_truthfulqa.py`, lines 165–200);
- release and paper model identifiers include mutable `latest` aliases and live provider endpoints.

These do not prove that published rows are wrong. They show that the post-paper release is not a closed reconstruction package and that missing/error states need explicit fail-closed semantics.

## Reproducibility and operational realism

**What is inspectable:** immutable paper PDF/text/source; official repository commit; six dataset revisions; prompts, solver variants, scoring code, novelty filters, runners, release checks, and a rerun script; row-level generated questions, targets, model identities, judge choices, and some reasoning/log provenance.

**What is not closed:** exact paper-run commit; immutable model endpoint snapshots; complete raw request/response traces and retry ledgers; all prompt/config/environment hashes per row; human-validation packet; item-level novelty matrix and selection provenance; code that rebuilds every paper table/figure; full usage/cost ledger; deterministic reproduction without paid mutable services.

The operational realism is mixed. The method confronts a genuine evaluation problem—static suites miss localized failures—and pays the real cost of iterative generation and validation. Yet the evaluated units remain mostly generated multiple-choice or short classification/generation prompts. There is no professional workflow state, source pack, artifact lifecycle, recipient consequence, or expert decision. Legal topicality does not make an invented multiple-choice item professional legal work.

## Concrete repository actions

### Retain

1. **Response-conditioned follow-up selection.** Use observed failure signatures to select or propose discriminating follow-ups after an initial broad form.
2. **Typed ablations.** Compare response-aware generation with shuffled outcomes, no-reasoning, random/static, and cross-target controls.
3. **Attempt and attrition accounting.** Preserve every proposal, parse failure, validity rejection, novelty rejection, target outcome, judge disposition, and final admission.
4. **Cross-model transfer matrices.** They can distinguish generic hard suites from source-model-local probes when analyzed as interactions rather than raw transfer rates.
5. **Separate generation and profile synthesis.** Keep item evidence and natural-language failure labels linked but separately validated.

### Repair

1. **Freeze authority before adaptation.** Independently author the construct, source rules, admissible answer/equivalence policy, and critical failure families before the profiler sees target outcomes.
2. **Use plural independent validity observers.** Generated answer keys and legal/professional claims need source-grounded deterministic checks or qualified adjudication independent of generator and target.
3. **Require repeated target evidence.** A stable failure family needs repeated responses and untouched semantically matched probes, not one selected miss.
4. **Test target specificity directly.** Cross target-history source, generator, candidate batch, receiving target, and judge; estimate interaction after generic item difficulty.
5. **Validate profile labels prospectively.** A frozen label should predict untouched failures better than generic difficulty/topic labels and help a blinded user choose an effective intervention or follow-up.
6. **Fail closed.** Missing samples, judge failures, parse errors, and exhausted retries are typed invalid/missing outcomes, never correct responses or implicit accepted items.
7. **Separate denominators and claims.** Report proposed, parse-valid, source-valid, novel, target-tested, target-failed, repeat-failed, independently admitted, profile-linked, confirmatory-passed, and decision-used counts.

### Do not infer

The paper does not establish domain expertise capture, comprehensive model capability profiles, failure prevalence, causal model mechanisms, professional validity, human equivalence, productivity, safety assurance, deployment readiness, or cross-domain benchmark validity.

## Falsifiable next action

Run one bounded **crossed adaptive-probe specificity** experiment over two existing, structurally different `skill-bench` knowledge-work shapes. Freeze authoritative task rules and planted failure families first. Collect initial attempts from at least two configured systems, then generate matched candidate batches under true-history, swapped-history, shuffled-outcome, and history-blind conditions with equal budgets. Independently validate candidates without exposing target identity or outcome. Re-evaluate each admitted candidate repeatedly on both systems and on untouched matched variants.

Primary evidence should be a source-history × receiving-system interaction among independently valid, repeated-stable failures. Secondary outcomes should include proposal attrition, validity false-admission, semantic family coverage, novelty observer disagreement, profile-label stability, token/time/correction burden, and whether a frozen label predicts untouched failure. A same-target advantage that disappears after item difficulty or on untouched variants falsifies the model-specific profiling claim while retaining generic hard-item value.

## Bottom line

Adaptive task elicitation is a strong search heuristic and a useful benchmark-maintenance primitive. The paper gives broad empirical evidence that prior response records can improve the yield of hard, sometimes transferable probes. Its official release makes many generated artifacts and implementation choices inspectable. But the demonstrated object is a selected, configured hard-example distribution—not a calibrated capability profile. `skill-bench` should adopt response-conditioned probing only inside an authority-preserving, fail-closed, crossed and repeated validation design, with profile claims frozen and tested on untouched evidence.