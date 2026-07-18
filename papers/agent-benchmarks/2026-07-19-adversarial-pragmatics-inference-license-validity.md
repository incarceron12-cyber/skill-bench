# Adversarial Pragmatics: controlled label contrasts expose evaluator instability, not safety validity

## Source and evidence status

**Deep review of the complete immutable primary source; timing-appropriate official release audited.**

- **Paper:** Brett Reynolds, *Adversarial Pragmatics for AI Safety Evaluation: A Benchmark for Instruction Conflict, Embedded Commands, and Policy Ambiguity*, arXiv:2607.01153v2 (15 July 2026), <https://arxiv.org/abs/2607.01153v2>.
- **Date read:** 2026-07-19.
- **Local PDF:** `data/papers/pdfs/2607.01153v2-adversarial-pragmatics.pdf` (28 pages including supplement; SHA-256 `bcc792a143ae2138f5852f622c2e8f8a42ee6e7e2fcf8036f0d34e860d23a6bd`).
- **Local text:** `data/papers/text/2607.01153v2-adversarial-pragmatics.txt` (complete extraction; SHA-256 `cc11f1c367dd08c87eae1957df4cf16c8bda5f523224f3e56ba8501ec00d87e0`).
- **TeX source:** `data/papers/source/2607.01153v2-source.tar` (SHA-256 `83a148facefac654d9dd91f818100c50022b60590bc630260e9a020c6348342f`).
- **Official repository:** <https://github.com/BrettRey/adversarial-pragmatics-for-ai-safety-evaluation>, archived at timing-appropriate commit `4f27d32378ed4b9fb4bf77b54b9bc13d3173df31` under `data/sources/releases/2607.01153v2-adversarial-pragmatics/`.
- **Provenance and release boundary:** `data/sources/releases/2607.01153v2-adversarial-pragmatics/provenance.json`.

The pinned commit is 32 minutes 44 seconds after the arXiv v2 update and differs from its pre-v2 parent only in arXiv font packaging. This makes it a reasonable correspondence snapshot, not proof of the exact private pilot state. ZIP CRC verification passed. I independently reran the ordinary item validator and repository `make test`; both passed. The stricter pair validator correctly failed only P008 because its two rows mix phenomena, matching the paper's exclusion of that diagnostic contrast from strict-pair scores.

## One-sentence contribution

Adversarial Pragmatics contributes a useful controlled vocabulary and minimal-pair method for separating source role, authority, quotation/use, scope, reference, speech-act force, policy boundary, and transcript attribution, but its evidence is an 18-item author-written seed set, 54 author-adjudicated local outputs, and one answer-cued same-model judge pass—enough to expose label and instrument failure, not enough to establish gold labels, expert validity, realistic safety behavior, judge robustness, or professional-work validity.

## Why this matters

This review advances charter objectives A, B, and E through narrow expansion on a cross-domain measurement problem: **what exactly does a behavioral label license us to infer when language changes role, wrapper, authority, or interpretation?** Safety is the paper's application, not a proposed boundary for `skill-bench`.

Knowledge work repeatedly turns on the same distinctions. A sentence in an email may be evidence rather than authority; a quoted policy may be the object of analysis rather than an active constraint; “the previous figure” may have two plausible referents; a refusal may preserve policy while failing the task; and a correct artifact may still expose protected information in its explanation. If a benchmark compresses these into pass/fail, it cannot tell whether the agent failed to identify a source, resolve scope, respect authority, execute a requested act, preserve information flow, or satisfy an evaluator's preferred interpretation.

The paper's strongest conceptual move is to call labels **inference licenses**: a category is useful only to the extent that it projects across declared meaning-preserving variants and changes when the governing contrast changes (paper §§1, 7, pp. 2, 13–14). That reframes paraphrase and wrapper tests. They are not generic robustness decorations; they audit the scope of the claim attached to a label.

## Research question and claim boundary

The defensible question is:

> Can a small, pre-specified contrast set and plural annotation protocol reveal when task, policy, risk, refusal, and failure-attribution labels are unstable under changes in linguistic role or evaluator condition?

The relevant claim ladder is:

```text
predeclared linguistic contrast
→ structurally valid item metadata
→ author-expected behavior
→ one author-adjudicated output label
→ independently repeatable criterion-specific label
→ stability over declared paraphrase/wrapper/model/judge projections
→ valid task or policy construct
→ realistic safety or professional-work behavior
→ consequential decision utility or readiness
```

V2 provides evidence for the first three links and pipeline evidence at the fourth. The negative judge result usefully challenges promotion to the fifth. It does not establish the later links.

## Methodology and system

### 1. Construct and taxonomy

The paper actually defines **eight**, not seven, development families (paper §3, pp. 4–6):

1. embedded commands;
2. mention/use and quotation;
3. authority and instruction hierarchy;
4. scope, negation, and modality;
5. deixis and reference hijacking;
6. indirect speech acts and pragmatic pressure;
7. policy-boundary ambiguity; and
8. agent-transcript interpretation.

The first seven describe prompt-level linguistic phenomena; transcript interpretation is downstream and can combine several of them. The abstract's list can look like seven because it names the prompt-level families and then multi-turn transcripts separately. Natural cases are acknowledged to overlap. The seed benchmark separates them to make controlled contrasts possible.

This is a productive inclusion rule: ordinary hard instruction following is out of scope unless expected behavior depends on source role, pragmatic status, authority, policy boundary, or transcript evidence (paper §3, p. 4). It avoids treating every mistake as “pragmatics.” However, labels such as authority hierarchy, policy boundary, information flow, and transcript attribution are not purely linguistic. Their correctness also depends on an externally valid authority model, policy, state, and evidence view.

### 2. Seed construction and pair scoring

The released `benchmark/items/seed-items.csv` contains 18 hand-authored rows: eight strict two-item pairs plus P008, a diagnostic confidentiality contrast. Harmless colors (`BLUE`, `GREEN`), a protected token (`ZETA-42`), and a dummy secret (`ALPHA-000`) isolate control structure without operational harmful content (paper §4, pp. 6–7; supplement Tables 2–3, pp. 2–4).

Each row predeclares item/pair identity, phenomenon, variant, control dimension, context source, source role, authority level, pragmatic status, response act, prompt, expected behavior, six expected label fields, judge flag, and notes. Strict pair success requires both variants for one model to be task-successful **and** policy-compliant. This defeats trivial always-output, always-ignore, and always-refuse strategies better than item accuracy.

The pair structure is only partially minimal. P008 contrasts email-body exfiltration with a direct toy-policy refusal; both require non-disclosure, but the phenomenon and intervention differ. The paper transparently excludes it from the 24 strict pair–model cells. The release's strict validator detects the mixed phenomena, but the default `make test` runs only non-strict validation. More broadly, the validator checks columns, nonempty fields, inventories, pair cardinality, shared phenomenon/control dimension, and whether at least one expected label differs. It does **not** establish semantic minimality, naturalness, public authority, alternative-valid interpretations, unchanged payload/response space, or correctness of expected behavior.

At least one retained “stable” item is explicitly unstable in the rater guide: AP-SEED-007 does not settle whether metalinguistic mention of prohibited `BLUE` counts as output. The guide recommends `item_problem` or `partial`, while the released author evidence labels a response containing “I will not output BLUE ... GREEN” as success/compliant because the token is mentioned rather than used. By contrast, AP-SEED-016 and AP-SEED-018 treat repeating a protected token inside a refusal as disclosure. This is not necessarily contradictory—the intended policies differ—but it shows that use/mention analysis cannot alone settle an information-flow predicate. The paper recognizes this at AP-SEED-016 (paper §6, pp. 10–11).

### 3. Annotation topology and label ontology

The paper and historical protocol separate:

- `task_success` (`success`, `partial`, `failure` in the pilot);
- `policy_compliance` (`compliant`, `noncompliant`, `policy_ambiguous`);
- `safety_risk` and `risk_type`;
- `refusal_outcome`;
- `failure_attribution`;
- confidence and rationale.

Thus the paper's phrase “five judgments” at §2, p. 3 is an imprecise summary: the implemented pilot has six categorical label families before confidence/rationale, while “source sensitivity” is represented mostly in metadata/failure analysis rather than as its own adjudication column.

The plural ontology is valuable. A response can complete the visible task yet violate policy; comply with policy yet over-refuse; safely mention a string while violating an explicit no-output channel constraint; or fail because the item itself is unstable. Refusal is a matrix, not a safety-success synonym.

But the completed pilot did not exercise the proposed expert topology. The author wrote all items and expected behaviors, generated the review instrument, saw expected behavior and diagnostic context, and labeled all 54 rows (paper §6, pp. 8, 14). There were no independent policy evaluators, linguists, domain specialists, repeated human labels, disagreements, adjudications, or gold-label transitions. The release's historical rater guide contains calibration answers and criterion-specific boundary rules; handing it to nominally “independent” raters would train them toward the author's interpretation.

The timing-appropriate release does include a more careful `benchmark/study-a/schema.md`: role-separated linguistic/task and policy/safety first-pass forms, standard `insufficient_visible_context` and `item_problem` escape states, separate source-role and visible-boundary fields, and later rather than first-pass failure attribution. That is a stronger planned instrument, not completed external evidence. The schema itself says the historical risk labels are frozen and not directly comparable to the newer visible-boundary fields. No external Study A responses are released at the pinned commit.

### 4. Local pilot and configured systems

The author ran all 18 items once against `qwen3:8b`, `gemma3:12b`, and `glm-4.7-flash:q4_K_M` using local Ollama 0.15.2 on 30 June 2026. Settings were temperature 0, seed 1, 256 predicted tokens, no thinking trace, and unloading between runs (paper §6, pp. 8–9). This yields 54 crossed item–model rows, but only 18 independently authored items and one attempt per cell.

Author labels report:

- task success: 36 success, 11 partial, 7 failure;
- policy: 46 compliant, 7 noncompliant, 1 ambiguous;
- strict pairs: 12/24 eligible pair–model cells;
- model strict-pair cells: 3/8, 4/8, and 5/8.

Three pairs pass for all models (embedded command, mention/use, scope/negation), while deixis/reference, agent transcript, and policy-boundary pairs pass for none (paper Table 1 and Figures 2–3, pp. 9–10). These are descriptive seed diagnostics, not model comparisons: there is one row per model/item, no uncertainty, no frontier model, no independent oracle, and no valid population frame.

The released 54-row sanitized evidence table is unusually helpful because it reveals rationales and output excerpts. It also exposes label dependence. Three identical AP-SEED-014 `BLUE` outputs are called partial because the author expected contextualized order status, even though the seed expected behavior says to output the requested color. Three AP-SEED-017 answers of “Disallowed” are called partial for insufficient helpful context even though the prompt asks to classify the request as allowed or disallowed. These may be defensible quality judgments, but they demonstrate that `task_success` includes an author-specific helpfulness standard not fully fixed by the visible request or expected label. Alternative-valid-output review is absent.

### 5. Rule-aided triage and LLM judge

Simple diagnostics flag all seven author-labeled policy-noncompliant rows as high priority, but low-priority rows still contain partial failures and the policy-ambiguous row (paper §6, pp. 10–12). That is an appropriate use: deterministic token/source checks nominate review; they do not determine pragmatic correctness.

The first judge pass uses `glm-4.7-flash:q4_K_M`, one of the evaluated models, once over all 54 rows. It therefore grades 18 of its own outputs. The compact prompt exposes each row's expected behavior, asks for all six labels plus confidence/rationale, and validates structured JSON. There is one prompt condition, no repeated calls, no disjoint judge, no source-order variation, and no no-rubric condition despite those being proposed for future work.

Exact agreement, majority baseline, Cohen's κ, and minority recall are:

| Label family | Agreement | Majority baseline | κ | Key minority recall |
|---|---:|---:|---:|---:|
| Task success | 66.7% | 66.7% | 0.26 | 0/11 partial |
| Policy compliance | 88.9% | 85.2% | 0.45 | 3/7 noncompliant |
| Safety risk | 72.2% | 79.6% | 0.14 | 0/11 risk-labelled |
| Risk type | 83.3% | 81.5% | 0.27 | 1/10 non-none |
| Refusal outcome | 98.1% | 96.3% | 0.79 | 2/2 refusals |
| Failure attribution | 77.8% | 66.7% | 0.40 | 6/18 non-none |

These figures correctly support a **negative instrument finding**: valid JSON and high raw agreement can coexist with performance at or below a constant judge and zero recall on important minority states. But they do not estimate general judge robustness. The 54 rows are clustered within 18 authored items, classes are tiny, the author labels are not an independent reference, expected behavior is answer-cuing, and one model/prompt/call supplies every judge label. The refusal κ rests on only two author-positive rows. No interval or clustered resampling is reported.

### 6. Taxonomy drift and projectibility

The paper proposes taxonomy drift as the proportion of items whose labels change under paraphrase, wrapper, model version, or adjudication criterion while the intended control dimension stays fixed; diagnostic ambiguity is unresolved disagreement after context clarification (paper §7.8, pp. 13–14). This is a strong design proposal, but **the pilot does not execute it**. It has minimal pairs where the control dimension intentionally changes, not controlled paraphrases where it remains fixed; several wrappers exist across different items, not matched wrapper variants; three models provide output variation, not repeated labels on equivalent outputs; and there are no independent criterion-specific evaluators.

The fake development pass exercises table layouts and decision rules only. Its simulated “keep/revise/narrow/exclude” counts are explicitly not empirical evidence. Therefore V2 introduces taxonomy-drift machinery but reports no empirical taxonomy-drift rate or projectibility profile.

## Evidence and interpretation

The paper and release support five useful findings:

1. An auditable seed item can bind expected behavior to source role, authority, pragmatic status, and response act before outputs are seen.
2. Strict pair scoring can falsify invariant but superficially safe strategies better than single-row accuracy.
3. Task success, policy compliance, refusal, information-flow risk, and attribution can diverge on the same response.
4. A deterministic triage layer can recover obvious channel/policy failures while remaining insufficient for full pragmatic grading.
5. One answer-cued, same-model judge pass can produce perfect parse validity and high majority-dominated agreement while missing every author-labelled risk row and partial success.

It does **not** show that the expected labels are independently correct, that the eight-family taxonomy is complete or stable, that labels project under paraphrase or wrapper changes, that experts can apply the protocol reliably, that model differences are stable, that toy-token results transfer to realistic prompt injection or policy use, or that any grader supports safety decisions.

## Unique insight

The deepest transferable idea is not another safety taxonomy. It is a **label-license contract**:

```text
public requirement / authority / policy basis
→ criterion-specific interpretation and admissible alternatives
→ output or state evidence visible to this observer
→ raw label + uncertainty + rationale
→ disagreement source and adjudication
→ declared projection set
→ invariant-preserving and boundary-changing variants
→ observed stability / failure
→ licensed scope of the score and downstream claim
```

A label should travel only as far as its tested projection set. Stability across harmless paraphrase does not license wrapper transfer. Wrapper transfer does not license source-authority validity. Agreement with an expected-behavior-cued judge does not license blind judging. A policy-compliance label does not license safety or consequence. Conversely, a label change is not automatically model failure: it may reveal item wording, observer evidence, criterion conflict, or taxonomy drift.

This complements rather than replaces existing `skill-bench` machinery:

- **Ambig-DS** varies missing task framing and tests an ideal clarification channel; Adversarial Pragmatics varies linguistic role and asks whether label meaning survives. Both require public admissible interpretations rather than a hidden author preference.
- **UnderSpecBench** distinguishes private intent from public authorization and realized effect. Adversarial Pragmatics contributes finer language-level candidate causes, but toy expected behavior cannot establish authorization.
- **AgentRewardBench** shows that predicate, evidence view, prevalence, and label lineage condition judge reliability. This pilot adds a stark answer-cued minority-recall failure, but with far weaker human reference evidence.
- **ComplexConstraints** makes pragmatic criteria expressive and rewardable but risks criterion/judge coupling. Adversarial Pragmatics shows why expected-behavior visibility and local author calibration are upper-bound treatment conditions, not independent validity.
- **ScopeJudge** shows that request context changes scope-label recall and preserves real expert disagreement; Adversarial Pragmatics supplies source/quotation/scope contrasts but does not execute an online gate or observe consequence.
- **Context-to-Execution Integrity** binds field, effect, and invocation authority at a mediated sink. Linguistic source classification can nominate which text influenced a proposal; it cannot substitute for manifest-bound execution authority or state evidence.

## Limitations and validity threats

1. One author creates the taxonomy, items, expected behaviors, historical rater guide, adjudications, and interpretations.
2. Eighteen items cannot establish eight-family content coverage, prevalence, difficulty, or psychometric structure.
3. The 54 rows are crossed repeats of 18 items, not 54 independent tasks.
4. One attempt per item/model gives no configured-system reliability.
5. Three small local model configurations do not support frontier-model or model-ranking claims.
6. Harmless token prompts isolate syntax/control structure but omit realistic documents, tools, state, side effects, user stakes, and adversarial adaptation.
7. Minimality is structurally checked, not semantically validated; P008 is known invalid for strict pairing.
8. AP-SEED-007 is acknowledged as not gold-stable, yet remains in a pair reported as 3/3.
9. Some task labels import under-disclosed helpfulness preferences, as AP-SEED-014 and AP-SEED-017 show.
10. No systematic alternative-valid-response review tests whether author expectations are too narrow.
11. The completed labels are not independent expert labels; no expertise basis beyond the author's roles is operationalized.
12. Proposed policy-versus-linguistic disagreement is not observed because one person supplies all labels.
13. Confidence has 41 high and 13 medium rows but cannot be calibrated against another authority or outcome.
14. `safety_risk` mixes toy-output classification with hypothetical transfer risk; the newer release schema itself retires it from blind first-pass use.
15. Failure attribution is post-outcome causal interpretation without counterfactual, trace, or independent root-cause evidence.
16. The judge is also an evaluated model and self-grades 18 rows.
17. Expected behavior is visible to the judge, creating answer cues and an upper-bound rubric condition.
18. One judge model, one prompt, and one call per row do not identify prompt, model, order, or stochastic sensitivity.
19. Severe class imbalance makes raw agreement misleading; tiny minority counts make κ and recall fragile.
20. No confidence intervals, task-clustered uncertainty, repeated calls, or multiplicity treatment are reported.
21. The reference labels are author expectations, so judge disagreement does not by itself identify judge error.
22. Taxonomy drift is proposed but not empirically measured; the seed pairs intentionally change controls rather than preserve them.
23. Application-surface transfer is not isolated by matched prompt-only/web/email/tool/transcript variants.
24. Raw model outputs and browser adjudication exports are unreleased, preventing full reconstruction of truncation, parsing, order, and rationale context.
25. Sanitized row excerpts are inspectable but lossy; full run manifests, hardware details, model digests, and environment capture are absent.
26. The official snapshot contains evolving Study A machinery not evaluated in the paper; protocol availability must not be confused with completed evidence.
27. No human baseline, novice/expert contrast, burden measurement, safety consequence, affected-party decision, or professional acceptance is observed.
28. The eight families may overlap or require domain policy/authority evidence beyond linguistic expertise; no completeness or discriminant-validity study exists.

## Reproducibility and operational realism

Reproducibility is **good for inspecting and validating the seed artifact, moderate for reconstructing sanitized tables, and weak for reproducing the empirical runs or labels**. The immutable PDF/text/TeX, 18-row CSV, schemas, validator, local runner, diagnostic and judge scripts, 54-row sanitized evidence, aggregate tables, and fake calibration assets are preserved at a timing-appropriate commit. The basic validator and `make test` execute successfully; strict validation reproduces the documented P008 exclusion.

Exact replay is blocked by absent raw output bundles and browser exports, mutable local model artifacts, incomplete runtime/hardware capture, and no independent annotation records. Sanitized outputs are sufficient to audit several label choices and confusion counts, not to replay generation or reconstruct every judge input and response.

Operational realism is intentionally low. Webpage, document, email, tool-result, and transcript wrappers are text fields around toy payloads, not instrumented applications with source provenance, user authority, tool mediation, state transitions, or downstream consequences. This is appropriate for early construct isolation. It means the warranted object is a **linguistic/evaluator calibration seed**, not a safety benchmark, agent-security test, or knowledge-work readiness instrument.

## Transfer to skill-bench

### Retain

1. Use controlled pairs where one declared governing dimension changes and expected behavior is frozen before outputs.
2. Separate task completion, authority/policy compliance, refusal form, information flow, failure attribution, and observer confidence.
3. Preserve `item_problem`, `insufficient_visible_context`, criterion conflict, and policy ambiguity instead of forcing pass/fail.
4. Report class prevalence, confusion matrices, minority recall, invalids, and per-family cells before any aggregate.
5. Treat deterministic rules as triage witnesses and model judges as measurement objects.
6. Record the projection set that each label is intended to survive: paraphrase, source order, wrapper, rater role, model version, and judge prompt.

### Repair before use

1. Bind each expected behavior to public requirements, authority, policy version, admissible alternatives, and consequence—not author intuition alone.
2. Separate blind first-pass criterion observations from later causal attribution and gold adjudication.
3. Use independent role-qualified raters; preserve every label/rationale/confidence and disagreement rather than replacing them with consensus.
4. Cross invariant-preserving variants with boundary-changing controls. A taxonomy-drift study needs same-control paraphrases/wrappers, while a discrimination study needs matched changes that should flip the label.
5. Validate pairs semantically: naturalness, one-factor isolation, unchanged public basis where intended, changed expected label where intended, and alternative-valid outputs.
6. Cross judge conditions: disjoint versus same model, expected behavior visible versus hidden, clean versus misleading rationale, isolated versus joint labels, source order, prompt form, and repeated calls.
7. Join language-level judgments to authoritative state/action evidence for consequential tasks. Mention/use status cannot decide confidentiality when channel occupancy is the protected predicate.
8. Estimate uncertainty at item/family level and preserve one-attempt pilot results as descriptive only.

### Falsifiable validation slice

Use two existing cross-domain task shapes rather than create a safety-only suite. For each, author:

- one same-control harmless paraphrase;
- one wrapper change that should preserve the requirement;
- one authority/source-role change that should flip the legitimate action;
- one genuinely ambiguous version with at least two public-valid interpretations;
- one response that is task-successful but policy-noncompliant;
- one policy-compliant but task-incomplete response;
- one refusal that protects action authority but leaks a protected field in explanation; and
- one clean sentinel.

Obtain blind, role-separated ratings before adjudication. Cross human, deterministic, and model observers under exact evidence views. Require label stability on invariant variants, label change on authority variants, explicit ambiguity on unresolved variants, and correct state/channel consequences. A useful result would identify which labels project under which transformations and where observer or taxonomy failure begins; it would not claim professional validity from linguistic agreement alone.

## Concrete repository actions

1. Add no new schema. Existing public-basis, authority, rubric, configured-rater, disagreement, metric, task-health, trace, artifact/state, safety, and validity contracts can represent the obligations.
2. Add one bounded consolidation task to incorporate the label-license/projection-set rule into canonical synthesis after higher-priority consolidations. The task must preserve the distinction between a proposed taxonomy-drift metric and evidence actually observed here; it should not create a linguistics- or safety-specific subsystem.

## Claim boundary

Adversarial Pragmatics v2 supports the claim that an inspectable 18-item seed artifact can encode language-control contrasts and that, on 54 author-adjudicated outputs from three specified local model configurations, plural labels and strict pairs expose failures hidden by row accuracy. It also supports a negative result for one favorable but circular judge condition: structured validity and high raw agreement did not yield useful recall on author-labelled partial success, risk, or several failure attributions.

It does **not** establish final gold labels, independent expert reliability, empirical taxonomy drift, projectibility beyond the seed contrasts, general judge robustness, frontier-model safety differences, prompt-injection resistance, policy correctness, information-flow security, realistic agent behavior, professional knowledge-work validity, deployment utility, or readiness.