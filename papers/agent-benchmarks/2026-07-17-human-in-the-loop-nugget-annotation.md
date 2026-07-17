# Human-first nugget annotation: accountable criterion origin does not by itself validate the instrument

## Source and review status

**Deep review of the complete immutable primary source plus a code/data audit of the paper-linked mutable prototype.**

- **Paper:** Laura Dietz, *Human-in-the-Loop Nugget Annotation for Accountable LLM-as-a-Judge Evaluations*, arXiv:2606.29033v2 (7 July 2026), <https://arxiv.org/abs/2606.29033v2>
- **Date read:** 2026-07-17
- **Local PDF:** `data/papers/pdfs/2606.29033v2-human-in-the-loop-nugget-annotation.pdf` (12 pages; 1,898,262 bytes; SHA-256 `f4897a695a27e10197573c542d19ce69096aca5c1e713754cb05968c421efaa3`)
- **Local text:** `data/papers/text/2606.29033v2-human-in-the-loop-nugget-annotation.txt` (52,672 bytes; SHA-256 `17ef28d19ba0b9775457ef0005fe571acf04d10a7ea8ae94acd61cc7f9dd6ab0`)
- **Paper-linked prototype:** <https://trec-auto-judge.cs.unh.edu/annotate/nugget-hil-demo.html>; captured as `data/sources/releases/2606.29033v2-human-nugget-annotation/nugget-hil-demo.html` (15,904,942 bytes; SHA-256 `675a00d3d9e0ca1e2c9b0909919371bb70abbc806385b0d93681f44c48d3a1d3`)
- **Provenance:** `data/sources/releases/2606.29033v2-human-nugget-annotation/provenance.json`; the mutable demo reported `Last-Modified: Thu, 02 Jul 2026 17:33:46 GMT` and was retrieved 17 July 2026.
- **Additional-artifact boundary:** targeted exact-title/arXiv searches, GitHub repository search, and inspection of Laura Dietz's public repository inventory on 17 July found no title- or arXiv-linked code/data release beyond the web demo. This is evidence about those searches, not proof that no private or unindexed implementation exists.
- **Tags:** human-in-the-loop, nugget-judging, criterion-authority, anchoring, outcome-conditioned-authoring, grader-validity, expert-participation

## One-sentence contribution

The paper contributes a clear human-first authoring workflow in which an expert records spans or notes before an LLM canonicalizes them into nuggets, then previews model matches and inspects score impact; this is a useful accountability interface pattern, but the paper reports no user study, rater experiment, judge validation, cost measurement, held-out-bank test, or professional decision criterion, while the released demo exposes candidate-output anchoring, outcome-conditioned criterion tuning, incomplete lineage export, and unvalidated matching behavior that prevent claims of reduced bias, reliable coverage, scalable judging, or expert-valid evaluation.

## Why this matters for skill-bench

This source directly advances charter objectives B and F: it proposes a feasible division of labor for turning human attention into reusable criterion objects without asking an expert either to rubber-stamp a machine proposal or to assign one opaque score to a long artifact. The general hypothesis is domain-neutral:

```text
human notices consequential content
→ human-authored span/note/category
→ model-assisted canonical form
→ model-applied criterion observations
→ human inspection
→ reusable evaluation instrument
```

The key distinction for `skill-bench` is between **criterion initiative** and **instrument validity**. Requiring a human action before machine formalization gives an auditable origin and can reduce one specific form of machine-proposal anchoring. It does not show that the human is qualified, that the displayed outputs cover the construct, that the nugget preserves the human's intent, that different experts agree, that model matches are accurate, that weights correspond to consequence, or that the resulting score supports a professional decision.

The prototype also reveals a deeper tension: AI is downstream of the first human note, but not downstream of the criterion's final form or admission. “Check Impact” shows machine grades, quotes, coverage, and candidate-system consequences before commitment; quality control invites experts to adjust nuggets and weights until rankings fit their informed impression (paper Sections 3.3–3.4, pp. 3–4; Appendix A.2–A.3, pp. 9–12). This replaces **proposal anchoring** with a potentially useful but different treatment: **outcome-conditioned instrument authoring**. That treatment must be logged and validated rather than described as anchoring-free.

## Research question and claim boundary

The paper asks how humans can remain intellectually accountable for what matters while LLMs handle canonical phrasing and high-volume matching. It contrasts three approaches: human verification of AI proposals, unsupported manual labels, and human specification of criteria followed by AI application (Section 1, pp. 1–2). It proposes Must Have, Should Have, and Avoid nuggets, a creation/canonicalization/impact workflow, and aggregate quality control (Sections 2–4, pp. 1–5; Appendix A, pp. 6–12).

The full source supports narrow claims that:

1. the author specifies an implementable human-first workflow and a concrete prototype;
2. the interface can preserve selected spans, free-text notes, category choices, canonicalized questions, automated 0–5 matches, quotes, coverage diagnostics, adjustable weights, enable/disable state, and ranking views during a browser session;
3. the captured demo embeds two queries with 59 reports each, one ten-nugget bank, and 590 populated nugget–report grades; and
4. the export code can emit a JSONL nugget bank with question, ID, query, importance, creator metadata, and some human source fields.

The evidence does **not** establish that:

- human-first capture reduces anchoring, fatigue, omission, variance, or criteria drift relative to alternatives;
- displayed-output sampling yields complete or representative criteria;
- canonicalization preserves criterion semantics, atomicity, polarity, scope, or threshold;
- Must/Should/Avoid assignments or category weights represent expert consensus or decision loss;
- nugget matching is accurate, repeatable, calibrated, or superior to holistic judgment;
- score/ranking agreement with the author's informal impression is criterion validity;
- the workflow lowers total expert time or evaluation cost;
- one expert's bank represents a profession, stakeholder population, or legitimate plural views; or
- exported banks support professional capability, deployment, safety, scalability, expert substitution, or readiness claims.

The abstract's language about “reliably,” “real quality signal,” “consistency,” and playing to each party's strengths is therefore a design rationale, not a result of this paper's empirical method.

## Methodology and system

### Paper method: design argument and walkthrough, not evaluation study

The paper is a 12-page prototype report. It grounds the design in prior work on anchoring, criteria drift, judge biases, and nugget evaluation, then explains interface behavior through screenshots and three authored walkthroughs. There are no participants, recruitment criteria, expert qualifications, annotation tasks, comparison arms, random assignment, repeat sessions, agreement statistics, usability outcomes, timing, cost, error analysis, preregistration, or inferential results.

This matters when interpreting the three phases. The interface calls them Creation, QC, and Observe; the conclusion describes creation, calibration, and analysis. During creation, the human reads a query and one or more candidate reports, selects spans and/or writes notes, assigns a category, and may ask an LLM to formalize the nugget. “Check Impact” applies that wording across reports and exposes grades and quotes. QC changes inclusion and category weights while showing rankings; Observe summarizes universal, hard, and discriminative nuggets and cross-query system behavior (Sections 3.1–3.4, pp. 2–4; Appendix A, pp. 6–12).

The workflow is coherent, but no measured comparison shows that it is less cognitively demanding than black-box labeling or less biasing than verify-and-correct. The paper cites adjacent evidence for those risks; it does not test whether this intervention repairs them.

### Human-first curation changes, but does not remove, anchoring

The strongest control is temporal: a human must select text or write a note before requesting canonicalization (Section 3.2, p. 3; Appendix A.1, pp. 6–8). That prevents the exact sequence “machine proposes criterion, human accepts/rejects.” It does not create independent opinion formation in the broader sense:

- the human is explicitly grounded in outputs from evaluated systems, so candidate content can define what becomes salient;
- the paper recommends anonymized systems and random response order (Section 3.1, p. 2), but the captured implementation contains no response shuffling/randomization code and initializes the first sorted run;
- the interface does not export an order/exposure log, sampling probabilities, unseen-system holdout, or whether a nugget was spontaneous versus prompted by a displayed output;
- after the initial note, the human sees a model-generated canonicalization, model-generated grades and quotes, coverage prevalence, and rank changes before final commitment.

The correct claim is therefore: **the interface enforces human initiative before one model transformation**. Reduced total anchoring remains an empirical hypothesis. A valid study would randomize output exposure and assistance timing, preserve pre-assistance intent, and measure semantic edits, criterion coverage, repeat stability, and held-out decision behavior.

### Criterion formation, scope, polarity, and completeness

A nugget is represented as an open-ended question and categorized Must Have, Should Have, or Avoid. The prototype supports edit, duplicate, delete, and free-text/spans, but it has no explicit split/merge operation, dependency relation, applicability condition, source-authority predicate, evidence threshold, alternative valid path, contradiction link, unresolved disagreement state, or completeness claim.

This is especially important outside fact-rich report evaluation. “Does the response mention X?” can represent a desired fact, a forbidden error, a style preference, a hard safety gate, or a context-dependent professional consequence. Converting all of these into question-shaped nuggets plus category weights can erase the distinction. An Avoid nugget's 0–5 grade means *presence*, and a negative weight later turns presence into penalty; this is inspectable, but it is not equivalent to validating the severity or applicability of the prohibition.

Bank completeness is not identified by candidate outputs. If every displayed system omits a professionally mandatory requirement, no span will cue it and coverage diagnostics cannot reveal it. If one verbose system includes irrelevant detail, that detail can become a candidate nugget. The paper's advice to make nuggets discriminate among strong systems compounds this selection problem: universal requirements may be professionally essential despite low leaderboard discrimination, while candidate-specific trivia may be highly discriminative. Criterion coverage, task discrimination, and decision importance are separate properties.

### Canonicalization is a semantic transformation

The demo uses OpenRouter model string `gpt-oss-120b` at temperature 0.3. Its system prompt asks for “brief, atomic questions” targeting query-essential information, relevance, correctness, and completeness. It receives query context, selected spans, free text, and human category, and returns question text, type, and explanation (`nugget-hil-demo.html`, lines 5170–5357).

The human can edit the output, which is a valuable review affordance. But the implementation does not preserve the exact canonicalization prompt, model response, explanation, before/after text, semantic-diff decision, rejection, or model-service version in the exported bank. The export records only a broad model string and `canonicalized_from_spans` strategy for new human nuggets. An edited existing nugget records updater/time in browser state but export reconstruction drops revision history. Thus every final nugget may have a human action in its ancestry while the released artifact cannot reconstruct how machine wording changed scope.

The “LLM cannot introduce criteria” claim is too categorical. The model is instructed to infer query-essential information and can add specificity, assumptions, or normative framing not contained in the selected span/note. Human editability creates authority only if acceptance is explicit, qualified, scope-bound, and preserved with the transformation lineage.

### Impact preview and QC are measurement interventions

“Check Impact” grades one draft nugget across all 59 displayed reports, sorts matches, and shows quotes before the author commits. This is useful semantic debugging: experts can discover overbroad or overspecific wording. It is also adaptive reuse of evaluation outputs. The resulting criterion is selected and tuned on the same candidate pool whose ranking is displayed.

QC makes the circularity explicit: experts adjust category weights, disable criteria, isolate one criterion, and ask whether the ranking agrees with their informed system judgment (Section 3.4, p. 4). This can repair an obvious malformed criterion. It can also encode a preferred ranking, amplify favorite-system content, remove inconvenient counterevidence, or overfit the bank to the current pool. The paper offers no untouched systems, frozen bridge cases, prospective decision rule, edit log, multiplicity correction, or independent reviewer. “Leaderboard agrees with expert impression” is a calibration target chosen after viewing outputs, not independent validation.

For `skill-bench`, preview data must be labeled **authoring/adaptation data**. Bank claims require untouched confirmation artifacts and systems, with pre/post criterion versions and every admission/removal/weight change preserved.

### Matching and score behavior in the captured prototype

The matching prompt assigns 0–5 based on relevance, completeness, and accuracy. For Avoid nuggets, 0 means absent and 5 clearly present. Reports are truncated to the first 8,000 characters for grading; quote extraction occurs only after grades of at least 4 and separately checks that a normalized quote occurs in the full passage (`nugget-hil-demo.html`, lines 5449–5619).

This implementation creates material failure modes:

- first-8,000-character truncation can produce order-dependent false omissions;
- a 0–5 score combines presence, completeness, relevance, and factual accuracy without external source access;
- invalid numeric grades are silently converted to 0, conflating parser failure with substantive absence;
- API/JSON failures return null, but no retry, stable failure disposition, or export ledger is defined;
- 32 concurrent calls at temperature 0.3 have no repeated-run reliability study;
- model confidence is self-reported and uncalibrated;
- quotes are absent for grades below 4, so many partial/negative decisions lack direct evidence; and
- category weighting and aggregate thresholds have no decision-loss calibration.

The embedded demo data are an implementation witness, not validation data. They contain two topics and 118 reports total, but only the avocado topic has a bank: ten preloaded nuggets with `importance: null` and `quality: null`, plus complete 590-cell grades. The grade distribution is 279 zero, 81 one, 106 two, 92 three, 23 four, and 9 five; 28 cells contain quotes. No human labels, repeated judge calls, criterion-author records, adjudications, matching confusion matrix, or acceptance decisions are embedded. One bank for one query cannot support reliability or scalability.

### Export and operational provenance

The JSONL export is narrower than the live interface. For each topic it emits the request identity, bank, question IDs/text, category, creator metadata, and some source spans/notes. It does **not** preserve:

- all nugget grades, reasoning, confidence, or supporting quotes;
- enabled/disabled state, solo tests, category weights, ranking sensitivity, or QC decisions;
- candidate-system exposure/order and whether names were masked;
- canonicalization prompt/response/explanation, exact endpoint, temperature, retries, or revision diffs;
- matcher prompt/version/configuration and invalid-call history;
- disagreement, adjudication, split/merge, dependency, applicability, or bank-completeness review;
- held-out confirmation, bridge items, licensed score interpretation, or retirement/version history.

Preloaded nuggets lacking creator metadata are exported with `is_human: false`, `llm_model: preloaded`; user nuggets are marked `is_human: true` even when model-canonicalized. That binary origin flag is too coarse for accountable transformation lineage. In addition, deletion retains cached grades keyed by text hash, so recreating identical text can recover earlier judgments without an explicit version/eligibility event.

## Evidence interpretation

### What is genuinely useful

1. **Human initiative should precede machine formalization** when criterion authority is meant to remain human.
2. **Spans and free text are better provenance anchors than a bare final criterion.** They expose what prompted the expert's attention.
3. **Impact preview can reveal semantic operating behavior before release.** This is valuable if treated as adaptation evidence rather than confirmation.
4. **Criterion-level grades and quotes are more auditable than one holistic score.** They localize disagreements and omissions.
5. **Must/Should/Avoid separates positive coverage from forbidden content.** The categories are a useful starting vocabulary, though not sufficient semantics.
6. **QC should expose sensitivity to criterion inclusion and weights.** Hiding this dependence behind one scalar would be worse.

### What the paper does not show

- no causal reduction in anchoring, criteria drift, fatigue, or omission;
- no expert-time, throughput, cost, usability, or cognitive-load benefit;
- no inter- or intra-rater reliability;
- no criterion-authority, completeness, atomicity, or professional-validity study;
- no semantic-preservation test for canonicalization;
- no human validation or repeat stability for nugget matching;
- no held-out ranking/decision validity; and
- no evidence that the workflow scales beyond one mutable demonstration.

## Unique insight

> **Human-first authoring creates accountable initiative, but the full instrument remains jointly authored by the expert, displayed candidate outputs, the canonicalizer, the matcher, and the QC objective. Accountability must therefore follow the entire criterion lifecycle, not stop at the first human click.**

The lifecycle has four distinct treatments:

```text
candidate-output exposure
→ pre-assistance human intent
→ model canonicalization and human acceptance/edit
→ model impact preview and outcome-conditioned admission/weighting
→ fixed-bank application to untouched outputs
→ bounded score/decision claim
```

The paper protects the second arrow better than common verify-and-correct workflows. It leaves the other arrows largely unmeasured. This explains why “every criterion traces to a human action” is necessary but insufficient: ancestry does not establish semantic fidelity, coverage, independence, judge accuracy, or decision validity.

A second insight is that **preview before commitment has two opposing causal roles**. It can reveal wording defects and reduce accidental criterion drift, but it can also cause deliberate drift toward candidate-pool discrimination or a preferred ranking. The correct response is not to remove preview; it is to separate adaptation from validation, preserve every preview/edit, and test the frozen bank on untouched systems and artifacts.

## Comparison with existing project evidence

- **ResearchRubrics** makes large human-written criterion inventories inspectable but shows that fine-grained does not imply atomic, authoritative, independent, or fair. Nugget-HIL improves pre-canonicalization intent provenance, but supplies far less author/reviewer, disagreement, weight, and judge-validation evidence.
- **Expert disagreement review** shows that one human's criterion choice cannot silently become “expert ground truth.” Nugget-HIL has no plural annotation or disposition for context splits, framework-conditioned criteria, unresolved conflict, or stakeholder policy.
- **Many-Facet rater effects** separates agreement, severity, fit, and decision validity. Nugget-HIL estimates none of them; self-reported matcher confidence and a leaderboard impression cannot substitute for a connected rater design.
- **Rubric modification** shows that criterion text, examples, call topology, and aggregation are measurement interventions. Here canonicalization, impact preview, inclusion, category weights, truncation, and matcher prompt all alter the instrument and require separate identities.
- **Generated/adaptive-rubric reviews** show that model-generated criteria are candidate transformations and that score correlation/discrimination can hide omitted gates or construct drift. Nugget-HIL starts from human attention, a stronger authority anchor, but its candidate-conditioned preview and QC can still optimize discrimination while changing the construct.
- **GrowLoop** makes the criterion–case co-evolution hazard explicit. Nugget-HIL's current candidate reports function as both elicitation cases and bank-tuning data; without frozen bridges and untouched systems, better separation among those reports is selection history, not validation.

## Transfer to skill-bench

### Retain

1. Capture a human span/note/category before any model proposal.
2. Preserve criterion-level observations and direct evidence locators.
3. Permit model assistance only through typed operations such as canonicalize, match, quote, cluster, or duplicate detection.
4. Show downstream operating behavior before release, including universal, hard, and discriminative criteria.
5. Keep positive requirements, optional preferences, and prohibited content distinct.

### Repair

1. **Represent origin as a graph, not `is_human`.** Record exposure set/order, spontaneous/probed status, raw span/note, contributor authority/scope, canonicalizer input/output/configuration, human acceptance/edit, and every later revision.
2. **Separate authoring, adaptation, and confirmation pools.** Candidate outputs may elicit and debug nuggets; untouched outputs/systems must test frozen-bank behavior. Preserve rejected candidates and all edit history.
3. **Type criterion semantics.** Add public basis, polarity, gate/scored/diagnostic role, applicability, threshold, evidence authority, dependencies, legitimate alternatives, contradiction/context links, and licensed claim.
4. **Preserve plural judgments.** Allow independent nuggets, proposed merges/splits, context-specific variants, unresolved disagreement, framework/stakeholder identity, and explicit adjudication or policy aggregation.
5. **Validate canonicalization.** Use before/after semantic review, planted scope/polarity/threshold changes, independent contributor confirmation, and held-out behavior. An editable model output is not automatically faithful.
6. **Validate matching independently.** Sample criterion–artifact cells by grade, category, length, domain, and consequence; obtain blinded human labels with evidence views; report confusion, insufficiency, severe errors, repeat stability, rater effects, cost, and drift.
7. **Fail closed operationally.** Parser/API failure, truncation, missing source access, and unvalidated evidence must remain typed invalid/insufficient states, never silently become grade zero.
8. **Version the whole instrument.** Hash criterion bank, creator/transformation lineage, matcher prompt/model, evidence view, truncation/chunking, weight policy, enabled set, aggregation, and decision threshold.
9. **Measure burden rather than infer scalability.** Compare total expert minutes, model calls/tokens/cost, corrections, adjudication, and severe-error loss against manual and AI-first alternatives.

### Test before promotion

A minimum cross-domain experiment should use at least two materially different artifact families and factorially or sequentially compare:

- human-only criterion authoring;
- AI-proposal-first plus human verification;
- human-note-first plus canonicalization without impact preview; and
- human-note-first plus impact preview.

Randomize and log candidate-output order, anonymize systems, preserve pre-assistance notes, and include an external professional-requirement source not present in any candidate output. Measure criterion recall/precision against independently authorized obligations, semantic transformation errors, intra/inter-rater stability, time/cost, matcher confusion, held-out system decisions, and whether impact preview improves wording while overfitting candidate rankings. This would directly test the paper's central design claim without treating a prototype walkthrough as evidence.

## Limitations and validity threats

1. Prototype/design report with no user study or controlled comparison.
2. No participant, expert-qualification, authority, recruitment, compensation, consent, or burden evidence.
3. No inter-rater disagreement, adjudication, or plural-stakeholder workflow.
4. No repeat annotation or criteria-drift measurement.
5. Humans inspect candidate outputs before defining criteria, creating content and omission anchoring.
6. Random order and anonymization are recommendations, not demonstrated implementation/evidence.
7. The captured demo lacks randomization code and exposure/order export.
8. Impact preview occurs before commitment and can anchor the final criterion to matcher behavior.
9. QC explicitly tunes inclusion and weights against observed rankings.
10. No untouched candidate systems, bridge set, or held-out confirmation.
11. Discrimination among current systems is conflated with construct coverage and importance.
12. Universal professionally mandatory criteria may be incorrectly treated as unhelpful.
13. Requirements absent from all displayed outputs cannot be discovered from output highlighting alone.
14. Model canonicalization can alter scope, polarity, assumptions, or thresholds.
15. No semantic-preservation labels or canonicalizer comparison.
16. Question-shaped nuggets omit explicit applicability, dependency, alternatives, evidence authority, and decision semantics.
17. Must/Should/Avoid categories and weights lack outcome/loss calibration.
18. No split/merge lineage or duplicate/dependency analysis.
19. The matching scale combines relevance, completeness, and accuracy.
20. The matcher lacks authoritative external source access for factual correctness.
21. First-8,000-character truncation creates order-dependent evidence loss.
22. Invalid grades become zero, conflating instrument failure and absence.
23. No retry/service ledger, repeated calls, calibration, or uncertainty.
24. Self-reported confidence is unvalidated.
25. Supporting quotes are requested only for grades at least four.
26. One bank, ten criteria, and 59 graded reports are demonstration data, not a validation sample.
27. The second embedded query has reports but no bank.
28. Embedded nuggets have null importance/quality and no creator authority.
29. Export omits grades, quotes, matcher identity, QC state, weight changes, and preview/edit history.
30. Binary `is_human` masks mixed human/model authorship.
31. Text-hash grade caching can reuse observations without explicit version eligibility.
32. No source population, task-coverage, professional acceptance, or consequential decision criterion.
33. No latency, token, dollar, human-time, failure-rate, or maintenance measurement.
34. Mutable web demo has no repository commit or immutable paper-time implementation identity.
35. Exact-title/arXiv/public-repository searches found no additional linked release, limiting independent replay and maintenance inspection.

## Reproducibility and operational realism

**Conceptual reproducibility is high:** the immutable paper explains the intended workflow, categories, screenshots, and walkthrough in enough detail to understand the interaction design.

**Prototype inspectability is moderate:** the self-contained captured HTML exposes embedded requests/reports/banks/grades, prompts, model string, temperature, queueing, matching, quote validation, QC controls, local state, and export code. It is unusually informative for a demo artifact.

**Empirical reproducibility is absent:** there is no experiment to replay. The demo is mutable, has no linked commit, dependency lock, tests, paper-time hash, source dataset manifest, author sessions, human labels, run logs, or analysis package. OpenRouter model string `gpt-oss-120b` is not an immutable endpoint realization.

**Operational realism is mixed:** long reports, source documents, criterion-level evidence, revision, and ranking sensitivity resemble real evaluation work. But the system is a single-browser prototype with local-state/export loss, no access governance, reviewer handoff, criterion approval lifecycle, source authority checks, invalid-state policy, judge calibration, service monitoring, frozen release, or consequential decision. It demonstrates an interaction pattern, not an accountable operating evaluation service.

## Concrete changes for skill-bench

1. **Do not add a duplicate schema task.** Existing expertise-transfer, participation/transformation lineage, criterion provenance/dependency/applicability, grader evidence-view, task-health, metric, and validity contracts are the correct homes. The blocked real-session elicitation task already requires spontaneous/probed/inferred status and should remain blocked until genuine contribution evidence exists.
2. **Add this workflow as a future experimental condition, not a default truth pipeline.** When a real expert pilot is authorized, preserve pre-assistance notes and compare with/without impact preview on untouched artifacts.
3. **Treat impact preview as adaptation exposure.** Any nugget or weight changed after seeing candidate grades/rankings must carry those exposures and cannot use the same rows as confirmatory evidence.
4. **Require full bank export before operational use.** Export must include immutable criterion/transformation history, exposure order, all grader observations/evidence, invalid states, QC changes, configuration hashes, confirmation split, and claim boundary.
5. **Add no queue item now.** The evidence sharpens existing contracts and a prerequisite-blocked real expert calibration; another schema or synthetic prototype would duplicate machinery without resolving the empirical uncertainty.

## Action items completed

- [x] Read and verified the complete immutable v2 PDF/text, including the appendix walkthrough.
- [x] Inspected the paper-linked demo's embedded data, prompts, grading, quote extraction, authoring/editing, QC, persistence, and export logic.
- [x] Audited the two-query/118-report demo, ten-nugget bank, and all 590 embedded report-grade cells.
- [x] Performed targeted exact-title, arXiv-ID, author-profile, and public-repository searches; documented the bounded absence of an additional linked release.
- [x] Compared nonduplicatively with ResearchRubrics, expert disagreement, Many-Facet rater effects, rubric modification, and generated/adaptive-rubric evidence.
- [x] Derived retain/repair/test implications while leaving criterion authority, bias reduction, completeness, judge validity, scalability, expert substitution, professional validity, and readiness unclaimed.
- [x] Added no duplicate queue task.
