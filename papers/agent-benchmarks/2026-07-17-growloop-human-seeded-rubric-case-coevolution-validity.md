# GrowLoop: evolving a rubric and its cases can preserve discrimination while silently changing the construct

## Source and review status

**Deep review of the complete immutable primary source and appendices, plus a timing-bounded audit of the complete official repository tree.**

- **Paper:** Yihang Lin, Yunze Gao, Zeyang Lin, Dongbo Li, Kun Peng, and Yue Liu, *GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human*, arXiv:2605.28882v2 (10 June 2026), <https://arxiv.org/abs/2605.28882v2>
- **Local PDF:** `data/papers/pdfs/2605.28882v2-growloop-human-seeded-rubric-case-co-evolution.pdf` (37 pages; 5,450,004 bytes; SHA-256 `10c7a00e4fd5291de374afcd2d1ef8155725493ca732a88a455ced022f61dd16`)
- **Full local text:** `data/papers/text/2605.28882v2-growloop-human-seeded-rubric-case-co-evolution.txt` (140,412 characters; SHA-256 `c8c8bdbc5a5711ef8277a7c9de2c6e1f9138d20c3aaeafaf59bcdba5afa7ad5f`)
- **Metadata:** `data/papers/source/2605.28882v2-metadata.xml`
- **Official release:** `data/sources/releases/2605.28882v2-growloop/AMAPVOICE-GrowLoop-62e170d.zip`, pinned commit `62e170d2f70bcae7442c83f392de7965ea9c6510` (23 June 2026), SHA-256 `b1780867c987933d21e2dee5343988cb6283e9df33d0af04b34059e22032ec2c`
- **Release provenance:** `data/sources/releases/2605.28882v2-growloop/provenance.json`
- **Timing boundary:** the acquired commit is nearly thirteen days after v2. Its complete, non-truncated 15-blob tree contains English/Chinese READMEs, ten images, and a PDF byte-identical to immutable v2—not a paper-time code or data release.
- **Tags:** rubric-evolution, case-generation, tacit-knowledge, disagreement, LLM-as-judge, adaptive-benchmark, construct-drift, release-inspectability

## One-sentence contribution and assessment

GrowLoop offers a valuable lifecycle abstraction—a versioned rubric–case pair in which unanimous human seed labels train editable criteria, generated cases stress those criteria, and novel failures can request new human seeds—but the paper validates rubric fitting and model-order-conditioned case selection, not the advertised outer co-evolution: three undisclosed annotators, consensus-selected supervision, no operational test of divergence-zone plausibility, no independent criterion-authority or construct-continuity audit, adaptive reuse of one judge and model pool, absent uncertainty/cost records, one illustrative rubric update, and no released code/data/full rubrics limit the evidence to a private configured conversation-evaluation prototype.

## Why this matters for skill-bench

This review advances charter objectives A, B, D, and E through a cross-domain benchmark-lifecycle question rather than a commitment to conversation evaluation:

```text
human observations and disagreement structure
→ seed admission and authority
→ model-proposed criterion transformation
→ versioned rubric and score semantics
→ rubric-conditioned case generation
→ adaptive case admission against a model pool
→ detected coverage gap
→ human-authorized rubric revision
→ bridge evidence across versions
→ bounded benchmark claim
```

The paper's unique insight is that criteria and probes are coupled: a rubric determines which failures can be named, while cases determine which rubric gaps become visible. That is important for `skill-bench`. The danger is equally important: if cases are selected to recover an expected ranking and rubrics are then revised from those cases, discrimination can improve while the construct, population, and score meaning drift. A living benchmark therefore needs **semantic versioning and bridge evidence**, not merely monotonically improving gates.

## Research question and claim boundary

The paper asks how an evaluation system for tacit, subjective, and changing judgments can (1) distinguish agreement from legitimate disagreement, (2) turn sparse human judgments into explicit criteria, and (3) update both criteria and cases as models and expectations change (Sections 1 and 3, pp. 1–11).

The full source supports narrow claims that:

1. the authors define a concrete three-stage rubric pipeline—cold-start extraction, natural-language rubric optimization, and a safety-first cascade—from 50 cases/200 unanimously labeled model responses (Section 3.3 and Section 4.1, pp. 5–8 and 12);
2. two judges using the resulting private rubric match the same three-expert unanimous seed labels at reported cascaded rates of 86.0% and 83.6% (Table 4, p. 14);
3. on 364 unanimous responses within a generated 178-case sample, GrowLoop leads nine reported comparators over 355 derived pairs: tie-aware accuracy 0.78, pair accuracy 0.87, and mean per-case Spearman 0.78 (Table 5, pp. 14–15);
4. the authors produce a 500-case synthetic set that passes their five adaptive admission gates against one four-model pool, including mean Kendall tau 0.713, minimum adjacent-tier Cliff's delta 0.33, and best-tier mean 69.5 (Section 4.3, pp. 16–17);
5. reported inner-loop trajectories move rubric agreement and case-set gates past authored thresholds, and one component ablation associates the full generation stack with higher final ranking/diversity metrics (Section 4.4 and Appendix F.2, pp. 17–18 and 33–34); and
6. the paper specifies a useful prospective state model `(R_t, C_t, L_t)` and add/refine/restructure trigger taxonomy (Section 3.5, pp. 10–11).

The evidence does **not** establish that the learned criteria are the experts' tacit knowledge, that the panel is authoritative or representative, that divergence judgments are plausible to affected experts/users, that case quality exceeds human authoring, that the expected model tiers are a valid capability ground truth, that rubric updates preserve the construct or score scale, that an outer rubric→case→new-human-seed→revised-rubric cycle works, that the system adapts to temporal drift, or that it transfers across domains, modalities, products, populations, cultures, judges, model pools, or decisions. It does not support professional validity, causal adaptation benefit, operational cost-effectiveness, safety, reward-model use, production fitness, or readiness.

## Methodology and system reconstruction

### Human seeds, panel, and annotation units

The supervision unit is a **model response within a conversation case**. A fixed panel of three unnamed “domain experts” independently assigns `0=fatal`, `1=poor`, or `2=good`. Unanimity defines the consensus zone; every other label pattern defines divergence. The 50 training cases are deliberately selected so all four responses per case are unanimous, yielding 200 consensus-selected responses. Safety optimization uses all 200; quality optimization uses the 133 non-fatal responses. A generated 178-case sample supplies 712 further ratings, of which 364 (51.1%) are unanimous (Section 4.1, p. 12).

The source does not report:

- who qualifies as a domain expert, recruitment or exclusion, tenure, demographics, cultural/language background, conflicts, compensation, consent, or attrition;
- whether all three panelists authored cases, rubrics, external priors, or disagreement analyses;
- calibration, examples shown, annotation interface, response order/randomization, model identity masking, rationale capture, adjudication, repeats, or label-change history;
- panel-level marginal distributions, pairwise agreement, chance-adjusted reliability, severity, or case/rater interactions; or
- why unanimity of three is the correct boundary between criterion-bearing consensus and legitimate divergence.

This matters because unanimity is not criterion authority. Selecting only cases where three raters agree conditions the learned rubric on an easy or culturally aligned subset. Conversely, every non-unanimous response is treated as legitimate disagreement without showing that some disagreements are annotation mistakes, evidence omissions, unstable raters, hidden safety expertise, or ambiguous instructions. The design collapses several states—uncertain, conflicting frameworks, insufficient evidence, inattentive error, and genuine plural values—into “divergence.”

### Consensus–divergence evaluation is asymmetric

Consensus cases have an executable target: exact match to a unanimous categorical label. Divergence cases do not. The paper says an AI judgment need only be “reasonable” or “within the range of reasonable human opinions” (Sections 3.2 and 4.2.1, pp. 5 and 13–14), but defines no acceptance instrument, evaluator panel, threshold, prospective sample, uncertainty, or failure rate.

Appendix G.2 supplies two author-selected narratives. In Case A, AI chooses one of the three observed labels and the authors call its rationale defensible. In Case B, all three humans assign passing/good labels while AI assigns fatal; the authors say the AI discovered a medical role-boundary issue the humans overlooked (pp. 35–36). No annotator, clinician, safety expert, user, or independent panel is reported to have reviewed or accepted that reinterpretation. Thus the second example is evidence that the rubric can **disagree** with the panel, not that it uncovers a valid latent criterion. It also exposes a logical problem: human unanimity is ground truth when optimizing the rubric, but may be overridden by the model when a qualitative example favors the system.

A disagreement-aware benchmark needs at least three separate outputs:

1. observed rater distribution and framework/rationale;
2. independent admissibility of a candidate judgment under named authorities; and
3. the decision policy for aggregation, abstention, escalation, or plural reporting.

GrowLoop measures the first weakly and illustrates the second; it does not validate the second or specify the third.

### Cold-start criterion generation mixes human evidence with model priors

A model first ingests rubric designs from prior benchmarks, then analyzes the 50 seeds, identifies one-vote-veto patterns, clusters candidate dimensions, and creates 15–25 weighted dimensions plus fatal gates (Section 3.3.1, p. 6). The final instrument has six safety standards and 18 quality dimensions grouped into four cognitive categories. Only three safety standards and five quality dimensions are shown; the remainder, weights, dependencies, calibration notes, and checkpoints are withheld as production IP (Appendix B, pp. 27–29).

This is not a pure externalization channel. The resulting text is jointly caused by:

- selected human labels;
- which model responses happened to be in the seed;
- existing benchmark structures;
- the generator model's pretrained concepts and preferences;
- agent prompts and clustering/merging choices; and
- later optimization against one judge's errors.

No human-authored criterion baseline, blind expert reconstruction, criterion-by-criterion source locator, contributor acceptance, alternative generator, or seed perturbation test separates these channels. The authors' strongest example—changing D01 from topical relevance to user-requested content—may be useful. But Appendix G.4 shows a highly specific calibration rule derived from a rejection sequence, then a single “held-out” lexically altered sequence constructed to share that structure (pp. 36–37). There is no sampling frame or evidence that this test was authored before the update. It demonstrates plausible local rule transfer, not extraction of tacit knowledge or broad generalization.

### Heuristic Learning optimizes one observer against selected labels

For each rubric version, Gemini 3.1 Pro Preview at temperature zero scores all seed responses with chain-of-thought; disagreements are diagnosed; dimensions, anchors, and calibration rules are revised; and rubric text is compressed. The safety and quality stopping thresholds are 90% and 85%. Proposed edits allegedly target systemic patterns, remove the triggering case for a leave-one-out check, fit a length cap, and for quality pass through Analyzer/Critic/Integrator roles (Algorithm 1 and Section 3.3.2, pp. 7–8).

Important operational details are missing: prompts, model snapshots/endpoints, random seeds, character caps, exact revision actions, candidate counts, acceptance tests, stored chain-of-thought or evidence, rubric versions/diffs, tie handling, failure/retry policy, judge variance, and whether multiple edits are evaluated on the same 200 labels. Repeatedly adapting to one small seed set makes the final 86% training agreement post-selection evidence. A leave-one-out check against “other disagreements of the same type” does not create an independent validation set; the type itself is diagnosed after observing the errors.

The second judge offers limited transport evidence. Claude Opus 4.6 scores the same consensus-selected training responses with the same private rubric and reaches 83.6%, but there is no repeat study, judge-by-criterion confusion matrix, blinded human audit, or held-out natural-conversation criterion test. Similar aggregate agreement does not establish stable criterion semantics across judges.

### Generated cases and rubric-conditioned source pool

Each synthetic case begins from a 14-field Conversation Situation Package spanning scene, topic, relationship, social expectation, persona, intent, emotion, ambiguity, turn structure, difficulty, failure trigger, target dimensions, challenge type, and failure mode (Section 3.4 and Appendix D, pp. 8–10 and 32–33). Inputs include:

- the private rubric and prior-round coverage deficits;
- 50 seed conversations as style/rhythm/persona references;
- 1,767 production user–AI transcripts containing 12,799 user messages;
- expert-curated scenarios, seven challenge dimensions, five failure modes, and a ten-trap taxonomy; and
- a four-tier target model pool.

Four agents plan, generate, criticize, and revise a conversation, with up to three revision rounds. Failed aggregate gates trigger severity-weighted replacement; a new case is accepted only if no monitored metric regresses.

This is useful construction machinery, but “authentic production patterns” do not make synthetic cases authentic. The paper omits traffic dates, product surfaces, eligible users, languages, geography, privacy/de-identification, consent for benchmark generation, filtering, duplicates, transcript selection, retention, and distribution summaries. It also does not expose source-to-CSP or transcript-to-case lineage, memorization checks, generated-case review, invalid rates, or human recipient judgments. The 500 cases, CSPs, prompts, outputs, and criteria are unreleased.

The human-versus-generated comparison is especially weak. Table 11 assigns checkmarks for depth, covert traps, rhythm, and creativity, while reporting mean turns of 2.1 versus 6.3 (pp. 17 and 33–34). It supplies no matched human authoring protocol, author count, independent raters, confidence intervals, cost, or task utility. Greater length and taxonomy coverage are consequences of the generator specification, not evidence of better cases.

### Model-order-conditioned admission is not independent validity

The case loop assumes `Claude Opus 4.7 > Qwen3.5-Plus > Qwen3-235B-A22B > Qwen3-80B-A3B`. The paper calls this externally established from public benchmark results and treats it as ground truth (Section 4.1, p. 12). Yet model capability is multidimensional and configuration-specific; public aggregate ordering does not guarantee ordering for Chinese open-ended companionship, voice-style response, safety, or every synthetic case.

More importantly, the case set is repeatedly regenerated until its scores under the GrowLoop rubric and Gemini judge recover this expected ordering. The final Kendall tau, adjacent-tier gaps, Cliff's delta, and best-model difficulty band are therefore **admission objectives**, not untouched validation outcomes. The same case pool, judge, rubric, and four target models participate in adaptation and final reporting. A 1,000-resample bootstrap of the admitted 500 cases shows that this selected set retains its selected ordering under case resampling; it does not estimate performance on the pre-selection case population or a new model pool.

The gate metrics also have unresolved semantics:

- per-case Kendall tau with one output per model conflates model identity, generation stochasticity, and capability;
- Cliff's delta compares score distributions across adaptively selected cases without paired or hierarchical uncertainty;
- adjacent gaps and best-tier mean are tuned on the same rows;
- entropy rewards balance over authored categories, not construct coverage or population representativeness;
- “all dimensions” scores come from one rubric-conditioned judge; and
- thresholds are described as empirical floors, but calibration data and selection procedure are absent.

The final 500-case set therefore demonstrates that a private adaptive generator can construct a **model-pool-discriminating instrument by design**. It does not establish a stable capability scale, new-model ranking validity, criterion validity, or production realism.

### Rubric–case co-evolution: specified outer loop, unexecuted core transition

The strongest conceptual contribution is the explicit state `(R_t, C_t, L_t)`, where the log contains per-dimension scores, rankings, and disagreements (Section 3.5, pp. 10–11). Rubric-to-case updates target new, underrepresented, or saturated dimensions. Case-to-rubric updates are classified as:

- **refine:** adjust anchors when cross-judge consistency falls;
- **add:** request new human labels and add a dimension for a recurring uncovered failure; or
- **restructure:** request labels, add a dimension, rescope overlaps, and renormalize weights.

But the experiment does not execute the defining outer transition. Section 4.5 says it validates “one complete outer iteration,” then explains that fresh generated cases being sampled, human-annotated, reinjected, and used to retrigger Heuristic Learning is future/ongoing work (pp. 18–19). What is actually shown is initial rubric fitting followed by case regeneration; generated cases merely “expose dimensions that would motivate” the next rubric round. No new human seed, additive/restructuring trigger, revised `R_{t+1}`, bridge set, rollback, or cross-version score comparison is reported.

The claimed inner-loop convergence is also narrower than the prose suggests. Greedy non-regression on selected metrics can terminate, stall, cycle under ties, or optimize away coverage; it is not a general convergence guarantee for semantic text edits or generated case sets. Trigger terms such as “recurring,” “semantically account,” “partial overlap,” and “unambiguous” lack executable thresholds or human authority. Frozen anchors, rollback, multi-step stability, and `K>=3` iterations are explicitly future work (Section 3.5 and Appendix A.3, pp. 11 and 26–27).

## Evidence interpretation

### What is genuinely learned

1. **Rubric and case evolution must be modeled together.** A criterion vocabulary bounds which failures can be attributed, and probes determine which vocabulary gaps become observable.
2. **Consensus selection can create a clean optimization signal at a cost.** It reduces label ambiguity but changes the target population to a unanimous subset and cannot validate divergence handling.
3. **Editable rubric optimization can expose useful local rules.** The D01 example is an inspectable hypothesis about requested versus merely relevant content, even though its authority and generality remain unverified.
4. **Case admission can deliberately maintain headroom and pairwise separation.** This is operationally useful for panel construction, but the resulting metrics are selection criteria and require untouched transport tests.
5. **Structural rubric changes are qualitatively different from anchor edits.** Adding or rescoping dimensions changes applicability, weights, and score meaning, so it needs stronger review and bridge evidence.
6. **Human seeds do not remain the sole authority after model transformation.** Once models infer criteria, generate cases, diagnose novelty, and judge plausibility, every stage needs its own authorization and validation.

### What the headline numbers do not license

- `86.0%` is post-optimization agreement on 200 unanimity-selected seed responses, not held-out expert accuracy or tacit-knowledge fidelity.
- `0.78` tie-aware accuracy is calculated on consensus-derived pairs from generated cases, not the full 712-response set or natural traffic.
- two anecdotal divergence cases do not validate reasonable-plural-judgment coverage.
- a 500-case set tuned to recover four expected model tiers does not independently validate model capability ordering.
- 100% preservation over bootstrap resamples is stability of the admitted set, not generalization to new cases, models, judges, or time.
- one local rubric edit plus five case-regeneration rounds is not empirical rubric–case co-evolution.
- model-generated criteria matching selected labels are not demonstrated human tacit knowledge.
- private production use and a “living infrastructure” roadmap are not production utility, low cost, or readiness evidence.

## Unique insight for skill-bench

> **A self-evolving benchmark has two coupled adaptive instruments—criterion space and probe population—and must preserve authority, selection history, and score bridges for both. Otherwise “evolution” can be indistinguishable from target-conditioned construct drift.**

## Transferable design pattern

The reusable record is:

```text
benchmark/version identity
→ source population and human authority
→ raw observations, disagreement states, and seed-admission policy
→ criterion proposal sources and transformation lineage
→ criterion version, applicability, dependencies, weights, judge view, and approval
→ case proposal sources and generation configuration
→ candidate population, rejection reasons, adaptive gate history, and admitted assembly
→ untouched bridge cases/models/judges and cross-version invariance
→ detected drift/coverage gap with evidence and trigger authority
→ refine/add/restructure decision, human review, rollback, and retirement
→ version-specific score vector, uncertainty, cost, and licensed claim
```

Three controls follow.

### 1. Replace binary consensus/divergence with typed disagreement

Store rater identity/role and framework, confidence, evidence, applicability, and rationale. Distinguish `consensus`, `legitimate_framework_difference`, `uncertain`, `insufficient_evidence`, `instruction_ambiguity`, `possible_error`, and `requires_specialist`. A candidate model judgment in a divergence zone must be independently reviewed for admissibility; being inside the observed numeric range is neither necessary nor sufficient.

### 2. Separate evolution data from bridge data

Every version should have:

- **adaptation data** allowed to drive rubric/case changes;
- **frozen semantic anchors** spanning old and new coverage;
- **new-scope confirmation data** untouched during proposal;
- **retired or invalidated items** with reasons; and
- **external bridge systems/judges** not used by the admission loop.

Report both current-version discrimination and bridge stability. If a restructure changes dimension scope or weights, old and new totals should not be treated as one scale until equating evidence supports it.

### 3. Treat gate success as selection history, not validation

Preserve every candidate case, generated response, rejection, replacement, metric trajectory, model/judge configuration, and stopping decision. Estimate performance on an untouched candidate draw and new configured systems. Otherwise the benchmark can be optimized to reproduce a prior model order while hiding how many cases contradicted it.

## Reproducibility, release, and operational realism

The paper gives useful pseudo-code, field names, metric formulas, threshold tables, rubric excerpts, and case studies. It does not provide sufficient evidence to reproduce any headline result.

The official repository audit is definitive for the pinned tree: 15 blobs totaling 13,769,654 bytes and 17 archive members, exactly reconciled against the GitHub tree. Present are two READMEs, ten images, `.gitignore`, and the byte-identical v2 PDF. Absent are implementation code, seeds, production transcripts, panel records, full rubrics, rubric versions/diffs, CSPs, generated cases, model responses, judge prompts/outputs, candidate/rejection logs, baseline outputs, statistical rows, bootstrap samples, ablation records, costs, and reproduction scripts. There are no tags, GitHub releases, repository license file, or additional author-owned artifact links in the paper. The README explicitly states that no code or data is released and restricts the PDF to research use.

Operational realism is mixed. Positive features include real transcript-derived inputs, multi-turn cases, explicit rubric editability, model-pool saturation checks, and a human re-entry concept for structural changes. Missing are privacy/consent and data-governance records, production traffic denominators, service/model snapshots, latency, tokens, dollars, human hours, annotation cost, failure/retry rates, invalid cases, ongoing trigger frequency, rollback incidents, live decisions, recipient outcomes, and longitudinal drift. Appendix A calls strong-LLM scoring the dominant deployment cost but supplies no measurement; the claim that cost grows sub-linearly is a design conjecture.

## Limitations and validity threats

1. Three annotators are called domain experts without recruitment, qualification, authority, demographic, compensation, consent, or attrition evidence.
2. The annotation instrument, ordering, masking, calibration, rationales, repeats, and adjudication are unreleased.
3. Unanimity of three is an authored zone boundary, not validated truth or legitimacy.
4. Training seeds are selected because all four responses are unanimous, changing the supervision population.
5. Divergence combines legitimate plural values with uncertainty, error, ambiguity, and missing expertise.
6. Divergence-zone plausibility has no operational metric or independent review sample.
7. The claimed “overlooked” medical issue contradicts all panel labels without clinician, panel, or affected-user adjudication.
8. Model-proposed criteria mix human labels with pretrained priors and benchmark structures.
9. Criterion-level source lineage, contributor acceptance, rejection history, and authority are absent.
10. Only excerpts of three of six safety standards and five of 18 quality dimensions are released.
11. Full weights, dependencies, calibration rules, and score implementation are private.
12. Repeated optimization and threshold selection reuse the same 200 seed labels.
13. Leave-one-out within diagnosed error types is not independent confirmation.
14. Rubric prompts, version diffs, candidate edits, length caps, and acceptance rows are absent.
15. Aggregate second-judge agreement on the training set does not establish criterion reliability or semantic equivalence.
16. The 178 held-out cases are generated under the learned rubric and shared seed/source machinery, not an independent natural population.
17. The 355 pairwise observations are nested within 364 responses and 132 cases, but no clustered uncertainty is reported.
18. Baseline prompt/version/configuration details and uncertainty are absent.
19. The D01 generalization example has no prospective registration or sampling frame and is structurally constructed to match the seed failure.
20. Production transcript eligibility, dates, users, languages, consent, privacy, filtering, duplication, and source-to-case lineage are unreported.
21. Generated cases have no independent human quality, realism, validity, or artifact-consequence review.
22. The human-authored comparison is an unsupported checkmark table without matched authorship, ratings, uncertainty, or cost.
23. Entropy over authored CSP categories measures balance under a taxonomy, not construct coverage or population representativeness.
24. Model tier order is imported from broad public results and treated as ground truth for a different configured construct.
25. Cases are adaptively regenerated until they recover the target model ordering, so final ranking metrics are post-selection.
26. One Gemini judge applies the rubric during both adaptive admission and final case-quality reporting.
27. One response per model/case does not separate stochastic response variation from model effects.
28. Cliff's delta and Kendall summaries omit hierarchical dependence and adaptive-selection uncertainty.
29. Bootstrap resampling occurs after admission and cannot validate the candidate population or new systems.
30. Gate thresholds are empirically asserted without released calibration records or sensitivity analyses.
31. “No metric regresses” is not a semantic, finite-time, or global convergence guarantee.
32. Trigger concepts such as recurring failure, semantic coverage, partial overlap, and unambiguous evidence are not executable.
33. The core generated-case→new-human-seed→revised-rubric transition is not empirically run.
34. Only one outer stage in one product domain is reported; temporal drift is not observed.
35. Frozen anchors, rollback, version equating, and long-horizon stability are future work.
36. Rescoping dimensions and renormalizing weights can change score meaning without a bridge study.
37. Case and rubric retirement policies are mentioned but not demonstrated.
38. No human/compute time, token, latency, dollar, storage, privacy-review, or maintenance ledger is reported.
39. No live workflow decision, user outcome, or stakeholder consequence validates operational usefulness.
40. No code, data, full instrument, result rows, or reproduction scripts are released.
41. The acquired official repository is post-v2 and has no tags/releases or declared code/data license.
42. Cross-domain, cross-modal, cross-cultural, cross-language, cross-product, and reward-model extensions are proposals only.

## Concrete changes and next actions: retain / repair / test

### Retain

- Version rubric and case set jointly, with logs that link coverage gaps to case and criterion changes.
- Separate anchor refinement from additive and restructuring changes; require stronger authority for structural edits.
- Use explicit case specifications and coverage diagnostics before generation.
- Track saturation, discrimination, difficulty, and diversity as separate panel-operation metrics rather than one quality scalar.
- Preserve disagreement rather than forcing majority truth.

### Repair before adoption

- Bind every criterion to raw observations, proposal source, transformation, reviewer authority, applicability, and approval state.
- Replace unanimity zoning with typed disagreement and an independent admissibility protocol.
- Store full candidate/rejection histories for rubrics and cases; never report adaptive gate metrics as untouched validation.
- Freeze bridge cases, models, judges, source strata, and score anchors before an evolution cycle.
- Require contributor/user rights and privacy lineage for production-derived source pools.
- Report clustered uncertainty and human/compute/correction costs.

### High-value falsification test

Run a preregistered, cross-domain two-cycle evolution experiment on at least two materially different knowledge-work task families:

1. obtain authorized criterion-bearing observations from multiple experts and preserve typed disagreement;
2. split them by expert/source/task cluster into proposal, confirmation, and frozen bridge sets;
3. generate candidate criteria under four conditions: human-only synthesis, model synthesis from authorized seeds, model synthesis with shuffled/prevalence-matched labels, and model synthesis without seed labels;
4. generate a complete candidate-case ledger and adapt only on a declared model/judge pool;
5. have blinded independent experts assess criterion authority, candidate-case validity, legitimate disagreement coverage, and construct continuity;
6. execute at least two real add/restructure cycles with explicit rollback rules;
7. test old/new versions on frozen bridges plus new systems and judges not used in adaptation; and
8. report criterion retention/addition/rejection, scale drift, case attrition, expert disagreement, score/rank changes, uncertainty, and total human/compute cost.

GrowLoop's central claim survives only if authorized model-derived criteria outperform controls on untouched expert review and downstream task diagnosis **without** unacceptable bridge drift. If discrimination rises while criterion authority or bridge invariance falls, the process has optimized the benchmark rather than improved its validity.

## Bottom line

GrowLoop is more valuable as a warning and lifecycle blueprint than as validation of self-evolving evaluation. It correctly identifies that tacit criteria, disagreement, cases, and model progress cannot be maintained independently, and its `(R_t, C_t, L_t)` abstraction plus refine/add/restructure taxonomy should inform `skill-bench`. But the present evidence stops before the decisive experiment: no fresh generated failure is authorized by humans, converted into a revised rubric, and bridged across versions. The reported agreement and discrimination are produced inside a private, adaptively selected, model-judged loop. `skill-bench` should retain the coupled lifecycle while adding authority lineage, typed disagreement, frozen bridges, full adaptation histories, untouched transport tests, and cost/consequence evidence.