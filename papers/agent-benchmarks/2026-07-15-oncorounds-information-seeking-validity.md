# OncoRounds exposes an inquiry-policy failure—but its feedback and scoring do not isolate information seeking

## Bottom line

OncoRounds makes a genuinely useful benchmark-design move: instead of handing a model a complete vignette, it withholds case evidence behind round-gated information items and requires the candidate to decide what to request before committing to diagnosis, differentials, and treatment. Across 32 configured model endpoints and 20 synthetic hematologic-oncology cases, models requested markedly less evidence in the definitive molecular round, and model-level information utilization correlated with overall score. This is strong evidence that **evidence acquisition is a separately observable part of agentic knowledge work**, not a detail to bury inside final-answer correctness.

The paper's strongest causal-sounding conclusion is nevertheless unsupported. It does not demonstrate that current models' *primary limitation is information seeking rather than medical knowledge*. Models were not crossed between active and matched full-information conditions; requesting more information was free and may proxy general model capability; later rounds changed evidence, diagnosis specificity, and treatment difficulty simultaneously; the same hidden-reference judge labels were returned to candidates between rounds; and one attempt per model-case provides no reliability estimate. The release makes the feedback leak explicit: after every solve, `benchmark.py` appends the full judge-label JSON to the candidate conversation before advancing the round.

The grading policy also rewards reference agreement more than clinical decision quality. It keeps the best `N` judge-labeled candidate items, tolerates up to ten differentials or treatments without penalty, permits compensatory averaging across diagnosis/differential/treatment, and calls their macro-average “balanced accuracy.” Expert agreement is against one case author using the same authored references, not independent clinical outcome validity. Reasoning and cognitive-error analyses are model-judged, lightly spot-checked, and based on provider-dependent hidden traces.

The transferable design is therefore not “copy OncoRounds.” It is an **evidence-acquisition episode** with an authoritative latent evidence state, request/availability transitions, evidence value and cost, a predeclared stopping decision, feedback firewalls, matched information conditions, endpoint consequences, and inquiry-specific diagnostics. OncoRounds supplies a valuable first instrument and unusually inspectable traces; it does not validate autonomous oncology, novice-equivalent cognition, or a general law that information seeking—not knowledge—is the main bottleneck.

## Why this matters: charter relevance and useful completion

This review advances charter objectives A, B, and C through a bounded clinical case study of a general knowledge-work primitive: deciding what evidence to acquire under uncertainty. The domain is not a proposal to narrow `skill-bench` to medicine. The reusable hypothesis is:

> For consequential work with latent evidence, an agent's inquiry policy can be measured separately from interpretation only when evidence access, costs, feedback, stopping, and endpoint consequences are experimentally controlled.

The concrete evidence is the complete immutable arXiv v1 paper, its full local PDF/text, all 20 released case/reference files, prompts, scorer, and 638 stored model outputs at a pinned official commit. The uncertainty clarified is what a staged request interface and utilization correlation actually establish. Useful completion means retaining the interaction primitive while defining controls that can distinguish inquiry selection, evidence interpretation, stopping, judge conditioning, and domain knowledge.

## Sources and review status

**Deep review of the complete immutable arXiv v1 and release audit of the official commit-pinned repository.**

- **Paper:** Krischan Braitsch et al., *Information-seeking failures of large language models in agentic clinical reasoning*, arXiv:2607.10275v1, <https://arxiv.org/abs/2607.10275v1>.
- **Version read:** immutable v1, submitted 11 July 2026; metadata contains no withdrawal or retraction notice.
- **Date read:** 2026-07-15.
- **Local PDF:** `data/papers/pdfs/2607.10275v1-clinical-information-seeking.pdf` (66 pages including supplement; SHA-256 `704c7cccdf0c9731e27ddbf570335f289f11c4716bb45c42e8a3aa030fb355d6`). `pdfinfo` emitted repeated malformed-string warnings, but `pdftotext -layout` produced readable text through the full supplement and references.
- **Local full text:** `data/papers/text/2607.10275v1-clinical-information-seeking.txt` (248,510 bytes; SHA-256 `8a7c83ad4de61308ab8a67593602663d682d2b52d71791e80c9fd6a07f924308`).
- **Metadata:** `data/papers/source/2607.10275v1/metadata.xml`.
- **Official repository:** <https://github.com/kbressem/oncorounds>.
- **Pinned release commit:** `471383b5c9fd1b32843e69a3a809f482907127dc`, authored 8 March 2026, about four months before arXiv v1.
- **Local release archive:** `data/sources/releases/2607.10275v1-clinical-information-seeking/kbressem-oncorounds-471383b.zip` (SHA-256 `0641837085672a4981044413aaa94d3d830d0207e8ed320cdd46187d155a8513`; locally preserved, archive ignored by Git).
- **Release provenance:** `data/sources/releases/2607.10275v1-clinical-information-seeking/provenance.json`.
- **Executed release audit:** `data/sources/releases/2607.10275v1-clinical-information-seeking/REVIEW_RELEASE_AUDIT.json`.
- **Timing boundary:** the release predates the paper and includes the complete cases, outputs, prompts, package, and leaderboard. It is strong official implementation evidence, but exact identity with the paper's final analysis snapshot is not assumed.
- **Tags:** active information acquisition, clinical reasoning, staged disclosure, stopping, evaluator feedback, LLM judge, trace validity, scoring validity.

## One-sentence contribution and research question

The paper asks whether frontier LLMs that perform well on static medical knowledge tests can actively acquire the evidence required for hematologic-oncology decisions, and whether their failures resemble cognitive biases described in novice clinicians.

Its central contribution is an interactive benchmark state machine:

```text
initial presentation
→ request one named evidence item OR solve
→ release / redirect / defer / reject request
→ judge diagnosis + differentials + treatment
→ advance clinical round
→ repeat through definitive molecular characterization
```

This is meaningfully different from a complete-case exam. The evaluator can observe:

1. which evidence the candidate attempts to obtain;
2. whether a parser maps that request to an authored item;
3. when evidence becomes available;
4. when the candidate stops requesting and commits;
5. whether the final assessment agrees with a round-specific standard; and
6. how these change across staged rounds.

The defensible result is narrow:

> On 20 author-developed synthetic hematologic-oncology cases under the released interaction, request parser, hidden-reference feedback, judge ensemble, and scoring policy, the tested configured model endpoints often stopped after acquiring only part of the available evidence, especially in Round 3; model-level utilization was associated with model-level score.

The evidence does **not** establish autonomous clinical competence, patient safety, treatment utility, real clinician equivalence, natural novice cognition, a causal effect of asking more questions, or that information-seeking deficits dominate encoded medical-knowledge deficits.

## Methodology and system

### Case construction and expert role

One board-certified hematologist with ten years' experience developed 20 cases de novo to reduce direct public-case contamination. Cases span hematologic malignancies and include patient presentation, round-specific capabilities, named information items, and a reference standard for diagnosis, differentials, and treatment. Seven additional board-certified hematologists each reviewed three cases; disagreements were resolved by discussion (Methods, pp. 6–7).

This gives the cases substantive clinical authorship and review. It does not give a population sample or independent validity criterion:

- one author created every case and its initial reference;
- the sampling frame, rejected cases, difficulty targeting, and coverage rationale are not reported;
- each reviewer saw only three cases;
- no pre-discussion agreement, item-level edits, unresolved disagreements, alternative acceptable plans, or authority boundaries are released;
- the cases are synthetic rather than derived from actual decision episodes, workflows, records, or outcomes; and
- “spanning the spectrum” is asserted without a construct map or sampling denominator.

The release shows rich cases, but also closed reference sets. For example, case 1 encodes a small list of accepted differentials and detailed treatment actions, priorities, and intentions. Clinically defensible alternatives outside that list depend on an LLM judge deciding semantic correspondence. The benchmark therefore measures agreement with authored case policy under a judge—not all legitimate oncology reasoning.

### Three rounds and active requests

Round 1 exposes initial presentation and permits immediate assessments; Round 2 permits biopsies, imaging, immunophenotyping, and consultations; Round 3 exposes molecular panels, cytogenetics, measurable residual disease, prior treatment, and definitive status. Candidates request one item per turn or solve.

The single-item interface makes choice visible, but does not by itself enforce meaningful prioritization. Valid requests have no explicit monetary, delay, patient-risk, attention, or token charge. A candidate can continue requesting every item until it chooses to stop. Cancellation is driven by five consecutive invalid responses, not by a clinically justified investigation budget. Consequently:

- **utilization** measures fraction opened, not expected value of information;
- **precision** measures parser-valid release, not clinical usefulness;
- fewer requests may be premature closure, but may also be rational if evidence is redundant;
- more requests may be prudent, indiscriminate enumeration, or simply a stronger model exploiting free information; and
- the benchmark cannot compare a concise high-value sequence with an exhaustive low-value sequence on consequence or cost.

The paper's round framing also overstates realism. A fixed three-stage release schedule resembles clinical chronology, but candidates do not manage an actual patient, order sets, turnaround uncertainty, contraindications, resource scarcity, communication, consent, follow-up, or realized outcomes. The environment is a deterministic evidence menu represented through text.

### Parser as an intervention

A GPT-5 Mini parser maps natural-language requests to canonical item names. It receives every item's canonical description and availability round. The candidate receives released content, rejection, redirection, or timing feedback. In the released prompt, `similar_available` can name the canonical alternative, while a not-yet-available response directs the candidate toward current-round options.

This is not merely neutral normalization. Parser behavior changes the candidate's opportunity and trajectory. No parser validation set, expert labels, ambiguity matrix, repeat reliability, false-release/false-reject rate, or cross-model robustness is reported. Its feedback can teach the evidence ontology and rescue a poorly formed request. Request precision therefore combines candidate wording, parser model behavior, authored aliases, and recovery policy.

A valid evaluation needs at least four separate observations: intended inquiry, parser interpretation, released evidence, and candidate adoption. OncoRounds largely reports the middle two as one “valid request.”

### Judge ensemble and scoring

Five parallel GPT-5 Mini instances compare candidate outputs with the round reference and label elements `correct`, `partially_correct`, or `incorrect`. Majority vote decides each label; ties prefer partial credit. Diagnosis is one label. Each proposed differential is labeled independently. Each treatment item receives action, intention, and priority labels.

The deterministic scorer converts labels to 1/0.5/0 and macro-averages three category accuracies. The paper calls this “balanced accuracy,” but it is not balanced accuracy over outcome classes; it is an unweighted mean of diagnosis, differential, and treatment category scores.

Differential and treatment scoring use best-`N` selection, where `N` is the reference-list length. The scorer sorts the candidate's independently judged items by quality and retains the best `N`. A penalty begins only above `max(10, 2N)`. This has material consequences:

- wrong or irrelevant proposals below the generous threshold can be discarded without reducing earned points;
- a candidate can hedge with ten items even when the reference has one;
- the judge prompt only says duplicate matching should “ideally” be one-to-one and limits repeated *partial* matches, leaving exact duplicate-match behavior under-specified;
- treatment action, intention, and priority are compensatory within a retained item;
- category macro-averaging permits one strong category to compensate for another; and
- urgent unsafe omissions are not noncompensatory gates.

This score supports an authored-reference agreement profile. It is not diagnostic completeness, safe treatment planning, expected clinical utility, or readiness.

### The evaluator feedback leak

The most consequential release finding is absent from the paper's validity discussion. In pinned `oncorounds/benchmark.py`, `_handle_solve`:

1. calls the hidden-reference judge;
2. stores the round score;
3. appends `json.dumps(result)` to the candidate conversation; and only then
4. advances to the next clinical round.

Thus candidates see item-level `correct`/`partially_correct`/`incorrect` labels for their diagnosis, each differential, and each treatment dimension before they act in the next round. Released trajectories visibly include candidates reasoning from that evaluation feedback.

The longitudinal treatment is therefore:

```text
clinical evidence + prior candidate output + hidden-reference rubric feedback
```

not simply:

```text
progressively disclosed clinical evidence
```

This can teach the target taxonomy, confirm or disconfirm hypotheses, reveal that a treatment priority was wrong, and alter later requests. It also creates model-dependent uptake effects. The final-round decline in requests occurs despite this privileged signal, which is interesting, but round trajectories cannot be interpreted as unaided clinical updating. Feedback should either be firewalled until the case ends or treated as an explicit intervention arm.

### Human–judge agreement

The five-judge ensemble is compared with one board-certified hematologist on 1,007 item labels, yielding quadratic weighted Cohen's kappa 0.804. The AI is stricter in 10.7% of labels and the expert stricter in 7.1%.

This is useful concordance evidence, but narrower than “validated against an expert” suggests:

- the expert is KB, who developed all cases and reference standards;
- there is one human comparator, so expert–expert variability is unknown;
- the unit mixes diagnosis, differential, action, intention, and priority labels across repeated cases/rounds;
- dependence is ignored in the single pooled kappa;
- the judge sees the same authored reference against which its agreement is measured;
- no independent clinical outcome, guideline panel, plural-rater decision, or downstream consequence anchors correctness; and
- item selection appears to be benchmark outputs, so prevalence and severity transport are unknown.

The result supports substantial ordinal agreement with the reference author under this corpus. It does not establish judge correctness, clinical validity, or safe handling of alternatives.

### Reasoning and cognitive-error analyses

Seventeen models with full provider-exposed traces contribute 1,008 model-case-round entries. Claude Opus 4.6 scores an adapted R-IDEA rubric and simultaneously assigns cognitive/process errors. One author reviews a random sample of 50 R-IDEA entries. The paper reports 91% above the six-point threshold, a model-level association between R-IDEA and overall score (`R=0.56`, `p=0.02`), and 93 errors in 89/1,008 evaluations.

The analysis usefully warns that polished reasoning can coexist with wrong endpoints. But trace evidence is especially fragile:

- provider traces are not a standardized or necessarily faithful view of internal computation;
- nine models have no traces and six expose summaries, creating outcome-dependent observability by model family;
- the same judge model supplies both R-IDEA and error labels in one pass, encouraging correlated labels;
- only 50 R-IDEA scores are spot-checked, with no reported agreement statistic or error-analysis validation;
- taxonomy labels such as anchoring, search satisficing, and premature closure can overlap and are inferred retrospectively from text;
- errors are selected only when verbalized, while silent failures are absent;
- the taxonomy explicitly excludes incomplete workup, missed findings, and incorrect diagnosis, moving major failures into other metrics; and
- analogy to novice clinician bias describes behavioral similarity, not shared cognitive mechanism.

The safe claim is that one evaluator found recognizable linguistic/trajectory patterns under an adapted rubric. “The same cognitive biases” is too strong without validated behavioral interventions, counterfactual evidence, and human comparison under the same protocol.

## Evidence and results

### Performance

The reported top overall score is Claude Opus 4.6 at 68.1%; Llama 3.3 70B is lowest at 40.2%. Across models, diagnosis averages 66.6%, differential reasoning 43.6%, and treatment 58.8%. All models score lowest on differentials.

These figures are descriptive for one attempt per model-case under heterogeneous provider endpoints. No repeated trial, seed/temperature analysis, clustered interval, endpoint snapshot, or model-by-case uncertainty is reported. Thirty-two model rows do not make 640 independent claims about stable model capability; model families share providers, lineages, parser, judge, prompts, and cases.

### Information acquisition

Requests fall from mean 7.5 in Round 1 to 4.2 in Round 2 and 1.8 in Round 3. Across requests, 58.8% release information, 17.2% are invalid, 8.8% receive similar-item guidance, and 15.2% target not-yet-available items. Utilization is 56.8%, 56.7%, and 25.7% by round. At model level, utilization correlates with overall score at `R=0.69`, `p<0.001`.

This is the paper's most important descriptive pattern. It still does not identify causality:

1. utilization and score are aggregated by model, so stronger models may both formulate better requests and answer better;
2. the score includes all three rounds while utilization is derived from the same trajectories;
3. no case-level or hierarchical model accounts for model, case, round, or request dependence;
4. one-sided tests are used for pre-expected positive associations;
5. available-item count is an authored denominator, not an expert-derived set of necessary or value-weighted evidence;
6. Round 3 presents fewer, more specialized items and more specific targets, changing both denominator and difficulty;
7. judge feedback from prior rounds conditions requests; and
8. no matched passive/full-information or forced-evidence contrast estimates the effect of evidence acquisition.

The result supports **utilization as a diagnostic correlate**, not “the strongest causal limitation.”

### Round decline and trajectories

Diagnostic accuracy falls from 72.6% in Round 1 to 61.3% in Round 3. The paper interprets deterioration and unexamined molecular data as premature closure. That is plausible, but rounds are not parallel forms. Round 1 permits broad syndromic diagnoses; Round 3 requires molecularly precise classification and treatment under prior therapy, comorbidity, and complications. Reference specificity, evidence volume, treatment burden, and scoring opportunities all shift. The design cannot separate inquiry decline from target refinement.

Trajectory categories also bin `partially_correct` with `incorrect`, throwing away the distinction that the main score treats as half credit. A model moving from a correct broad diagnosis to a partially correct molecular subtype counts as deterioration even though it may have incorporated substantial new evidence. Trajectories are descriptive of the instrument's labels, not calibrated clinical harm.

### Release audit and paper correspondence

The official archive contains 934 files, including 20 cases, package source, prompts/schemas, 32 output directories, logs, analysis scripts, and leaderboard data. I imported the pinned release's own `scoring.py` and recomputed each output directory against all case files without calling any model API.

Observed release denominators are:

- 638 output JSON files, not the theoretical 640;
- 631 marked `completed` and seven `cancelled`;
- 630 outputs with three rounds, four with zero, three with one, and one with two;
- 1,895 stored round evaluations.

The paper reports 1,896 completed model-case-round entries (634 Round 1; 631 each in Rounds 2 and 3). The one-round difference and output-status mixture are not reconciled in the release. Recomputed scores are close but not identical to the included leaderboard/paper values—for example, the pinned scorer yields approximately 67.84 for Claude Opus 4.6 versus 68.1 reported, and 65.65 for MiniMax M2.1 versus 66.3. The exact per-directory recomputations are preserved in `REVIEW_RELEASE_AUDIT.json`.

These discrepancies are small enough to leave the qualitative ranking and central pattern intact, but large enough to block exact table reproduction. Possible causes include a later analysis snapshot, excluded/cancelled-record policy, output updates, or scorer changes. The archive has lower-bound dependencies rather than an exact environment lock and no integrity manifest. Conversely, inspectability is unusually good: cases, references, prompts, outputs, and traces are all available, and the deterministic scorer runs without external calls.

Reproducibility assessment:

- **High** for inspecting cases, evidence gates, prompts, feedback behavior, output labels, and scoring semantics.
- **Moderate** for recomputing the included release's aggregate scores.
- **Low-to-moderate** for exact paper tables because stored denominators and recomputed values differ slightly.
- **Low** for repeating model trajectories because provider endpoints, sampling parameters, and model realizations are not fully frozen and calls incur external dependencies.
- **Absent** for claims about clinical outcomes, safe deployment, causal information value, or novice-equivalent cognition.

## Unique insight: evidence acquisition needs an intervention contract, not just a request log

OncoRounds adds a primitive missing from many artifact and workflow benchmarks: the environment contains evidence the agent must actively seek. Its limitations show why recording requests is insufficient. An interpretable evidence-acquisition benchmark needs six linked objects:

1. **Latent evidence state:** authoritative evidence atoms, provenance, validity time, dependencies, contradictions, and what is genuinely unavailable.
2. **Inquiry action:** candidate intent, wording, parser interpretation, requested scope, expected value, cost/risk, and alternatives.
3. **Access transition:** released, delayed, denied, ambiguous, failed, or redirected; observer and transformation provenance.
4. **Belief/action update:** whether the evidence was cited, adopted, rejected, contradicted, or ignored, and which decision changed.
5. **Stopping decision:** why the candidate acts, asks, abstains, or escalates under a frozen budget/loss policy.
6. **Endpoint consequence:** artifact/state quality, severe omission, decision loss, resource use, and uncertainty—not only reference-list overlap.

Matched interventions are necessary to distinguish mechanisms:

| Condition | What it isolates |
|---|---|
| active inquiry, feedback firewalled | configured inquiry + interpretation policy |
| all admissible evidence supplied | interpretation/knowledge ceiling under the same target |
| expert-selected minimal evidence supplied | interpretation given high-value acquisition |
| active inquiry with realistic costs/delays | prioritization and stopping under constraint |
| misleading/redundant/contradictory evidence | verification, revision, and robustness |
| explicit evaluator feedback after each solve | feedback-assisted adaptation, not unaided reasoning |

The key estimands should include necessary-evidence recall, unnecessary-evidence burden, marginal endpoint gain per evidence unit, severe omission rate, time/cost to decision, stopping regret against a declared loss function, and adoption of decisive versus distractor evidence. Raw utilization can remain a descriptive diagnostic, but should not be optimized as an objective; exhaustive retrieval is often wasteful or harmful.

This transfers across domains. A lawyer requests authorities and facts; an analyst inspects source tables and assumptions; an engineer reads logs and specifications; an auditor samples records; a researcher seeks disconfirming evidence. The latent evidence and costs differ, but the acquisition contract is reusable.

## Limitations and validity threats

### Construct and task validity

1. Twenty de novo cases have no declared sampling frame, rejection ledger, prevalence target, or coverage matrix.
2. One hematologist authored all cases and initial standards; seven experts each reviewed only three.
3. Consensus discussion is not released as plural alternatives, uncertainty, or agreement evidence.
4. Synthetic text cases omit real records, multimodality, teams, resource constraints, uncertainty, patient preference, and outcomes.
5. Round difficulty and diagnostic specificity change together, confounding longitudinal decline.
6. Available-item utilization treats all authored evidence atoms as equally useful and necessary.
7. Requests have no explicit cost, delay, invasiveness, patient risk, or resource tradeoff.
8. Fixed deterministic availability does not model test failure, noisy results, contraindication, or turnaround uncertainty.
9. One-item requests make actions visible but do not prevent exhaustive free retrieval.
10. The study has no active-versus-full-information or expert-minimal-evidence control.

### Interaction and feedback validity

11. GPT-5 Mini parser behavior is unvalidated and changes opportunity, request precision, and recovery.
12. Parser guidance can reveal canonical evidence categories and rescue candidate requests.
13. Hidden-reference judge labels are returned to candidates between rounds.
14. Later-round behavior therefore measures evaluator-assisted adaptation as part of the configured treatment.
15. No ablation estimates the feedback effect or separates clinical evidence from rubric feedback.
16. Five consecutive invalid requests create a harness-specific censoring mechanism unrelated to clinical stopping.
17. Provider API failures, parse failures, cancellation, and substantive early stopping are not given separate estimands.

### Reference and grader validity

18. Closed reference lists cannot enumerate every legitimate differential or treatment plan.
19. One case author supplies the sole human comparator for judge agreement.
20. Pooled kappa ignores repeated items nested in candidates, rounds, cases, dimensions, and references.
21. Same-reference agreement is not independent clinical correctness or outcome validity.
22. GPT-5 Mini is both parser and judge family; one candidate is also GPT-5 Mini, creating shared-family cue concerns.
23. Majority vote among five same-model judges estimates repeat consensus, not plural observer validity.
24. Tie-breaking toward partial credit is a policy choice without loss calibration.
25. Best-`N` sorting rewards candidates after seeing judge quality and can hide wrong proposals.
26. The ten-item floor permits substantial list padding, especially with short references.
27. Duplicate-reference matching is not deterministically enforced one-to-one.
28. Treatment dimensions and top-level categories are compensatory despite potentially critical omissions.
29. “Balanced accuracy” is category macro-accuracy, not class-balanced accuracy.
30. No severe-harm, contraindication, or mandatory-action gate anchors clinical safety.

### Statistical and inference validity

31. One attempt per endpoint/case gives no configured-system repeatability estimate.
32. Correlations are model-level ecological associations across only 32 dependent systems.
33. Shared model families, providers, parser, judge, and cases violate simple independence intuitions.
34. One-sided association tests encode direction and do not identify mechanism.
35. No hierarchical model separates model, case, round, request, and grader effects.
36. Model release date and parameter-count correlations are observational and family/provider confounded.
37. Round means compare nonparallel targets and evidence sets.
38. Partially correct diagnoses are collapsed with incorrect in trajectory categories.
39. No uncertainty accompanies model ranks or score differences.
40. Multiple reported associations, round contrasts, taxonomy comparisons, and model analyses create selection risk despite limited corrections.

### Trace and cognitive-claim validity

41. Full traces exist for only 17 models and are provider-dependent observations.
42. Hidden chain-of-thought is not guaranteed faithful, comparable, or stable.
43. Claude Opus 4.6 assigns both R-IDEA and error labels simultaneously.
44. The 50-entry R-IDEA check reports no agreement or correction statistics.
45. Cognitive-error annotations receive no independent human validation.
46. Taxonomy categories overlap and mix inferred cognition with observable process surfaces.
47. Silent errors cannot be observed from verbalized traces.
48. Excluding missed workup, missed findings, and incorrect diagnosis removes common failures from the reported 8.8% error prevalence.
49. Similarity to novice labels does not establish a shared cognitive architecture or cause.
50. High R-IDEA agreement with a judge-authored rubric does not establish faithful or useful reasoning.

### Reproducibility and lifecycle

51. The pinned official release predates arXiv v1 by about four months; exact analysis identity is unproven.
52. The release has 1,895 round evaluations versus 1,896 reported.
53. Deterministic score recomputations differ modestly from leaderboard/paper values.
54. Two theoretical model-case outputs are absent and cancellation/missingness policies are not fully reconciled.
55. Dependencies are not exactly pinned and no release manifest verifies archive bytes.
56. Endpoint parameters, seeds, temperature, provider revisions, and exact call-time identities are insufficient for exact trajectory replay.
57. Public cases and references now create future contamination risk; a renewal/private-form policy is absent.

## Transfer to skill-bench

### Retain

1. Withhold decision-relevant evidence so inquiry is behavior, not implied reasoning.
2. Represent round/time availability explicitly.
3. Require one typed inquiry action per step for interpretable traces.
4. Preserve raw candidate wording, parser mapping, release status, and evidence content.
5. Score inquiry and endpoint separately.
6. Use expert-authored evidence atoms and round-specific standards with provenance.
7. Publish complete cases, prompts, traces, outputs, and scorer where safe.
8. Analyze premature stopping and unrequested decisive evidence as diagnostics.

### Repair

9. Firewall judge/rubric feedback until the case ends, unless feedback is the declared intervention.
10. Add matched full-information, expert-minimal-information, and active-cost conditions.
11. Give evidence atoms expert-elicited relevance, necessity, redundancy, cost, delay, risk, and dependency annotations.
12. Validate parser decisions independently; retain ambiguous intent and parser uncertainty rather than forcing every request into one item.
13. Track candidate intent, release, access, adoption, belief change, action, and endpoint consequence as separate links.
14. Replace utilization-as-goal with value/cost, necessary-evidence, severe-omission, and stopping-regret metrics.
15. Use noncompensatory gates for unsafe action or omission and enumerate admissible alternatives.
16. Require deterministic one-to-one matching or explicit coverage semantics for list outputs.
17. Separate invalid execution, service error, parser error, budget censoring, abstention, escalation, and substantive completion.
18. Repeat configured trials and report case/model/form clustered uncertainty.
19. Validate grader judgments with multiple independent domain experts, disagreement retention, and severe-defect controls.
20. Treat trace-based cognitive labels as hypotheses to test with interventions, not explanatory facts.

### Cross-domain pilot design

A compact validation should use two unlike knowledge-work shapes, for example a document-based compliance decision and a data-analysis decision. For each scenario:

1. create an authoritative evidence graph with decisive, redundant, distractor, contradictory, unavailable, and delayed atoms;
2. have independent experts identify admissible minimal and alternative evidence sets, stopping rationales, and severe omissions;
3. randomize equivalent forms across active inquiry, full information, and expert-minimal evidence;
4. assign explicit costs/delays and a decision-loss function;
5. firewall all scoring feedback until terminal action;
6. repeat each configured system on clustered equivalent forms;
7. score request intent/parser correctness, evidence access, adoption, contradiction handling, stopping, endpoint artifact/state, severe errors, and total cost separately; and
8. test whether inquiry metrics predict held-out endpoint consequences after controlling for configured system and case.

Useful completion is not a schema alone. It is evidence that the same acquisition contract localizes planted inquiry failures in both domains, that parser/observer errors are distinguishable from candidate errors, and that active-versus-supplied contrasts separate evidence selection from interpretation.

## Concrete repository actions

- Added this full-text, release-audited review and preserved the immutable paper metadata, PDF, text, official archive provenance, and executed score audit.
- Updated machine-readable paper and topic navigation.
- Added one nonduplicate build task to create and validate an evidence-acquisition episode contract with matched information-condition fixtures. The task is cross-domain and explicitly treats OncoRounds as one motivating case, not the benchmark's target profession.
- Did not change the state-of-the-art map or grouped synthesis. This source deepens an underrepresented primitive—active evidence acquisition—but does not justify a new benchmark-family claim until the proposed cross-domain validation exists.

## Assessment

- **Evidence tier:** A-minus — full immutable paper read; complete official code/case/output release audited at a pinned preprint-preceding commit; deterministic scores recomputed; exact paper totals not reproduced.
- **Most reusable contribution:** making evidence requests and stopping observable under staged disclosure.
- **Most serious construct flaw:** free utilization is treated as information-seeking quality without evidence value, cost, or matched information controls.
- **Most serious treatment flaw:** hidden-reference judge labels are fed back between rounds, confounding unaided clinical updating with evaluator-assisted adaptation.
- **Most serious scoring flaw:** best-`N` post-judgment selection and generous padding tolerance reward reference-hit enumeration rather than calibrated differential/treatment quality.
- **Most serious inference flaw:** model-level utilization correlation does not identify information seeking as the primary causal bottleneck.
- **Safe claim:** under one staged synthetic oncology instrument, current configured endpoints often acquire only part of the authored evidence and especially little definitive-round evidence; this behavior is associated with authored-reference score.
- **Unsupported claims:** autonomous oncology competence, clinical safety, expert or novice equivalence, causal value of more requests, faithful cognitive-bias attribution, and information seeking as the dominant limitation of current LLMs.
