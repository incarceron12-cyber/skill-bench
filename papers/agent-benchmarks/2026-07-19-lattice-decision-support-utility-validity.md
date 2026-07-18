# Paper Review: LATTICE and the response-quality → decision-utility gap

- **Paper:** <https://arxiv.org/abs/2604.26235v1>
- **Title:** *LATTICE: Evaluating Decision Support Utility of Crypto Agents*
- **Authors:** Aaron Chan, Tengfei Li, Tianyi Xiao, Angela Chen, Junyi Du, and Xiang Ren
- **Date read:** 2026-07-19
- **Version read:** immutable arXiv v1, submitted 29 April 2026
- **Local PDF:** `data/papers/pdfs/2604.26235v1-lattice.pdf` (15 pages; SHA-256 `1cc7228e7cc19a0d52e130ac61042e8c3101be2061ffc82f5a766cf1c09dff88`)
- **Local text:** `data/papers/text/2604.26235v1-lattice.txt` (SHA-256 `19635a4c302ff9b4f87a2af719de6f4d92916a16af8cab30de959282c9c99e45`)
- **TeX source:** `data/papers/source/2604.26235v1-source.tar` (15 members; SHA-256 `8abce8b0a4b4e0b84a1291182b0df287fc8eef6e62d39d71c5958793bcf36bdf`)
- **Official release:** `data/sources/releases/2604.26235v1-lattice/SaharaLabsAI-lattice-benchmark-d03cdca.zip` (official commit `d03cdcad44a38bf8c38006b83adc128756c1dffa`, eight days before v1; SHA-256 `619b6fa15d00f93cec2c375c788dd03126974f4fa339ac6c2303f93af9ad6eb3`)
- **Release provenance:** `data/sources/releases/2604.26235v1-lattice/provenance.json`
- **Tags:** decision-support, response-quality, LLM-judge, preference, consequence-validity, configured-products, missingness, rater-effects

## One-sentence contribution

LATTICE supplies an unusually inspectable, balanced response-quality instrument for deployed crypto copilots—six rubric dimensions, sixteen task types, five query forms, 1,200 queries, six complete response sets, and per-item GPT-5.2 judgments—but its label “decision support utility” outruns its evidence: the study observes textual rubric properties and a separate crowd preference panel, not user uptake, decision quality, calibrated loss, financial benefit, burden, or harm, while the release reveals untested query generation, joint rather than isolated judging, no judge calibration or repeats, and no product/version/live-context identity.

## Why this matters for skill-bench

Consequential knowledge work often ends in a memo, recommendation, plan, or dashboard that a person may use. It is tempting to call a well-structured, cautious, actionable artifact “useful” and then treat its rubric score as evidence of better decisions. LATTICE makes that slippage visible because it explicitly targets the human-in-the-loop boundary but measures only the response side of it.

The transferable evidence chain is:

```text
response property
→ evaluator observation under a frozen evidence view
→ user perception or preference
→ actual exposure and uptake
→ changed belief or action
→ decision quality under known information
→ outcome, benefit, burden, or harm
```

LATTICE provides evidence mainly for the first arrow and a separate, non-linked preference signal for the second. It does not observe the remaining stages. This advances charter objectives A, B, and E without making crypto a project scope: the reusable issue is how any artifact-quality benchmark licenses—or fails to license—claims about human utility and consequences.

## Research question and claim boundary

The paper asks whether production crypto copilots differ in properties intended to help users understand, evaluate, and act: intent fidelity, mechanism clarity, uncertainty handling, actionability, evidence coverage, and response structure. It deliberately avoids external truth, live-data verification, tool traces, and realized outcomes, and scores only query, task/category labels, and final response (Sections 1 and 3, pp. 1–8). It then asks whether a separate crowd pairwise preference study is broadly consistent with the rubric ranking (Section 4.6, pp. 12–13).

### Supported by the paper and release

1. The released dataset is exactly balanced: 16 tasks × 5 categories × 15 queries = 1,200 unique query strings; every task has 75 rows and every category 240.
2. Six released response files each contain 1,200 non-empty responses matched to all 1,200 queries. The score file contains 1,200 query records, six scored products per record, no recorded errors, and internally consistent weighted totals.
3. The release reproduces the paper’s aggregate means exactly to displayed precision: Elsa 58.48, Gina 63.69, June 68.00, Minara 69.83, Sorin 75.31, and Surf 68.24. Recomputed dimension, task, and category means reproduce Tables 5–6 and Figure 3 after rounding.
4. The six dimensions expose substantial profile differences. For example, released means reproduce Surf’s high evidence coverage (6.86) and refusal (8.43), Minara’s uncertainty handling (6.90), and Sorin’s response structure (8.78).
5. The paper reports a separate 80-query, seven-product human panel with 18,481 pairwise judgments, 8.3% ties, and approximately eleven judgments per query/product-pair; Sorin ranks first, but the mid-tier differs from the rubric ordering (Section 4.6, pp. 12–13).

### Not established

The study does **not** establish that a response is factually correct, current, source-grounded, safe to execute, professionally acceptable, adopted by a user, decision-improving, economically beneficial, burden-reducing, harm-reducing, or preferable under a declared stakeholder loss function. It does not establish that the dimensions are distinct latent constructs, that category weights represent any user population, that GPT-5.2 is calibrated to experts or users, that one score per response is reliable, that released responses identify stable production systems, or that the crowd panel validates LATTICE at item or dimension level. No decision-improvement, financial-benefit, safety, professional-validity, production-fitness, or readiness claim is licensed.

## Methodology and released system

### Construct and task design

The paper defines six nominally complementary dimensions (Table 1, pp. 5–6):

| ID | Dimension | Observable target |
|---|---|---|
| D1 | Intent Fidelity | goal, constraints, missing information, no silent reframing |
| D2 | Mechanism Clarity | mechanisms and causal relationships |
| D3 | Uncertainty Handling | scenarios, ranges, conditional reasoning, re-evaluation triggers |
| D4 | Actionability | next steps, checks, guardrails, abort or falsification conditions |
| D5 | Evidence Coverage | relevant evidence angles and acknowledged gaps |
| D6 | Response Structure | organization, consistency, conclusion-reason alignment |

T1–T15 cover interpretation, event impact, claim validation, sentiment, market regime, execution feasibility, derivatives, flows, supply, failure modes, stress, opportunity cost, allocation, execution planning, and feedback adaptation. T16 is a separate safe-refusal task scored only on “Boundary Recognition and Clean Refusal” (Table 2 and Section 3.5, pp. 6–8). Five query forms—basic, comparative, constrained, decision, and ambiguous—cross every task (Table 3, p. 7).

Three unnamed domain experts reportedly iterated on dimensions, taxonomy, categories, generator prompts, and rubrics (Section 3.5, p. 8). The release adds an important authority detail absent from the paper’s high-level account: `rubric/DeFi Agent Evaluation Tasks and Protocol.md` says the task set is grounded in **Sorin’s product capability taxonomy** and intentionally uneven across six Sorin capability domains (internal lines 23–39). Sorin is also one of the evaluated products and the reported winner. That does not prove favoritism, but it creates a task-authority/system-evaluation dependency that should have been disclosed and independently reviewed.

The experts’ identities, roles, recruitment, conflicts, exact changes, disagreements, approval scope, and evidence are absent. “Substantial input” therefore supports domain-informed authorship, not representative user requirements or independent construct validity.

### Query generation and admission

The paper says GPT-5.2 generated the 1,200 queries and reports 15 per task-category cell (Section 4.1, p. 9). The release exposes a more complex lineage:

```text
80 seed queries
→ prompt expansion to 240
→ Codex generation of another 960
→ exact-overlap check against the 240
→ concatenation and ID normalization to 1,200
```

`data/query/README.md` documents that the 80 are contained in the 240, while the 960 are exact-exclusive. Independent inspection confirmed 1,200 case-folded unique strings, 80/80 seed overlap with the 240, zero exact overlap between the 240 and 960, and 15 records in every one of the 80 cells.

However, provenance is not equivalently complete. `pipeline/prompt/prompt_80_to_240_en.txt` asks for Simplified Chinese output even though most released rows are English; the 960-query Codex stage has no prompt, model/configuration record, transcript, rejection log, or reproduction script; and only exact overlap is asserted. There is no item-level admission rubric, human approval, realism review, live-dependence check, near-duplicate test, task/category relabel audit, or source showing that sampled queries represent user traffic. Balanced coverage is a design property, not population representativeness.

### Response collection and configured-system identity

The paper evaluates Elsa, Gina, June, Minara, Sorin, and Surf as black-box deployed products and argues that this captures model, orchestration, tool use, and UI/UX jointly (Sections 1 and 4.1, pp. 2 and 9). The release provides all final responses and query IDs, which is stronger than many product comparisons.

But each response record contains only `id`, `query`, and `response`. Neither paper nor release binds:

- collection timestamp or market-time window;
- product URL, app surface, account tier, geography, authentication, or UI state;
- product/version/model/orchestrator/tool/data-feed identity;
- conversation history, system prompt, tool calls, citations, retrieved evidence, or execution state;
- timeout, retry, missing-response, moderation, or manual-copy policy;
- response sampling count, decoding variability, or post-processing;
- screenshot or receipt proving the response came from the named product.

Thus the release preserves six complete text corpora, not six reproducibly configured production systems. UI/UX is invoked as part of the construct, but the judge never sees UI, latency, citations as interactive objects, controls, previews, or execution affordances—only flattened response text.

### Judge, evidence view, and call topology

The paper describes each copilot as independently scored by a fixed GPT-5.2 judge using query, task/category metadata, and response, once per query-product pair (Sections 3.5 and 4.1, pp. 8–9). The release pins the instructions and strict JSON schema and records token usage. It does **not** pin a model snapshot, seed, temperature/reasoning settings, API response IDs, timestamps, raw API output, request hashes, or service revision.

More importantly, the implementation does not isolate products one response at a time. `scoring/batch.py` builds all valid product answers into one `[Agent Answers]` block and makes **one judge call per query**; the strict schema requests an array of all product results (internal lines 73–118 and 157–206). The instruction says to score independently and avoid comparisons, but every response remains visible in the same context. This creates possible contrast, anchoring, ordering, verbosity, and shared-call effects. It also couples failures: one failed API call errors all products for that query, and no randomization or leave-one-product-out test estimates context sensitivity.

The paper’s “per-agent absolute scoring rather than pairwise comparison” is true of the requested judgment form, but not of evidence isolation. The configured grader is:

```text
GPT-5.2 label
+ shared six-product context in fixed file-discovery order
+ one structured-output call per query
+ rubric floor guidance
+ task/category metadata
+ no truth/source/tool evidence
```

That exact topology—not merely “GPT-5.2 judge”—is the instrument.

### Rubric behavior, polarity, and applicability

T1–T15 always receive all six dimensions. Before any score below six, the judge is told to identify a directly observable key defect; otherwise it should prefer 6–7 (`judge_instructions_en.txt`, lines 29–32). The released 40,500 standard-dimension labels show the expected concentration: scores 6, 7, and 8 account for most labels; D6 has only 3.5% at 5 or below, while D4 has 25.5%. This floor is not inherently wrong, but it is a severity intervention requiring calibration.

Applicability is not typed. A basic mechanism query can be penalized on D3 for lacking scenarios and re-evaluation triggers and on D4 for lacking a reproducible action checklist, even when the user asked only for an explanation. Conversely, a lengthy answer can gain D3–D5 points by enumerating generic branches, guardrails, and evidence types. The judge has no `not_applicable` outcome and no task-specific criterion map beyond T16. This confounds response quality with compliance to a preferred comprehensive-advisory style.

Criterion boundaries are also porous. On the 6,750 T1–T15 response rows, pooled score correlations are high: D3–D4 = 0.91, D3–D5 = 0.83, D4–D5 = 0.80, and D2–D5 = 0.77. Correlation does not prove redundancy because product and task quality induce common variation, but no factor analysis, discriminant cases, criterion-mutation tests, or human dimension labels show that judges can separate the dimensions. “Scored independently” is an instruction, not evidence of measurement independence.

There is a deeper polarity conflict. D2’s top levels require correct mechanisms and D6 refers to internal consistency/**correctness**, yet the judge is forbidden to verify current factual accuracy or use external evidence. D5 rewards mentioning evidence angles but explicitly does not assess whether data are traceable or verifiable. A fabricated but coherent causal story, complete checklist, and invented evidence list can therefore score well. LATTICE measures text-observable *signals associated with careful advice*, not trustworthy advice itself.

### Aggregation, denominators, and uncertainty

For T1–T15, integer 0–10 dimensions are transformed by category-specific weights summing to 100. T16’s single score is multiplied by ten. Every query then contributes equally to each product mean. The release records 1,200/1,200 scored rows and zero errors for every product, and all per-item weighted totals recompute exactly.

This clean released panel should not obscure missing operating semantics:

- scoring code excludes errored product rows from that product’s denominator and computes each mean over successful rows; there is no common-complete-case or failure penalty policy;
- score output has no attempted-call count, retry history, invalid structured outputs, raw failures, or post-retry denominator ledger;
- one score per response supplies no judge-repeat or response-repeat variance;
- no confidence intervals, clustered uncertainty, task-family sampling model, or multiple-comparison policy accompany aggregate, dimension, task, or category differences;
- 1,200 generated prompts are treated as a census of the authored suite, not a sample from real use, so the apparent precision does not establish population generalization.

Category weighting has little effect on the balanced aggregate. Replacing the published category weights with equal D1–D6 weights while retaining the observed 6.25% T16 share changes product means by at most about 0.25 points and preserves the ranking. This is unsurprising because all five categories appear equally within every task and their average weight vector is close to uniform. The paper does not run stakeholder weight elicitation or rank-sensitivity analysis.

### Human preference study

The separate human panel includes **seven** products—the six rubric products plus Wayfinder—over 80 separate queries. Every product appears roughly 5,280 times, consistent with 80 queries × six opponents × about eleven judgments. Sorin ranks first; Surf and Gina move upward relative to LATTICE, and Minara moves downward (Table 7, p. 12). The paper reports reason shares among non-ties: usefulness 45.54%, reasoning 35.37%, accuracy 19.08%, caution 0%, and clarity 0% (Table 8, p. 13), plus product-specific “serious error when lost” rates (Table 9).

This is useful convergent evidence for **crowd preference**, but not criterion validation or utility:

- annotator recruitment, expertise, geography, incentives, training, exclusions, and conflicts are not reported;
- exact pair randomization, display order, repeated-measures structure, annotator IDs, agreement, uncertainty, and per-item labels are absent;
- the response collection and product version boundary is absent;
- preference queries differ from the 1,200 rubric queries, preventing item-level judge-human agreement or dimension calibration;
- no direct statistical relationship, correlation coefficient, confidence interval, or rank-uncertainty analysis links the two studies;
- reasons are single-choice post-preference labels, not independent construct scores;
- zero caution and clarity selections are unexplained and may reflect form, mapping, interface, or reporting behavior;
- “serious error” authority and criteria are not defined;
- the human data, protocol, and analysis code are absent from the official release despite the paper’s statement that all code and data used are open-sourced.

Most importantly, choosing a preferred response is not making a consequential decision with it. The study observes no exposure-to-action uptake, belief change, option selection, calibration, regret, return, avoided loss, time saved, burden, or harm.

## Evidence and result interpretation

### Reproduced release claims

Independent standard-library inspection of the timing-appropriate official archive established:

- 1,200 unique query strings, sequential IDs 0–1199, 75 rows per task, 240 per category, and 15 per task-category cell;
- six response files × 1,200 unique matched, non-empty responses;
- 1,200 score rows × six products, no recorded result errors, and 1,200 rows with usage records;
- 10,547,334 total recorded judge tokens across 1,200 **shared six-product calls** (7,819,995 input; 2,727,339 output);
- exact weighted-total recomputation and exact aggregate means;
- task means reproducing all displayed Table 6 entries after one-decimal rounding;
- dimension means reproducing Table 5 after two-decimal rounding;
- category means reproducing Figure 3 after rounding.

This is strong **paper–release correspondence for the published score table**. The code, prompt, queries, responses, rationales, totals, and token usage are unusually inspectable.

### What the score pattern actually supports

Sorin leads every D1–D6 mean and every T1–T15 task mean. Therefore no nonnegative global reweighting of the released **mean standard dimensions** can make another product beat Sorin: Sorin componentwise dominates on that representation. June and Surf beat Sorin only on T16 refusal. Among the middle tier, ranking does vary by dimension, but the paper does not map any observed user-priority distribution to those dimensions or test whether selecting on a profile improves a user outcome.

The safe interpretation is:

> Under one released GPT-5.2, six-response shared-context rubric instrument, Sorin’s preserved response corpus receives the highest standard-dimension and T1–T15 means; other products show different rubric profiles and refusal scores.

The stronger interpretation—different users would be better served by different copilots—is a plausible product-selection hypothesis, not a demonstrated result. “Better served” requires an uptake/outcome or at least preference-by-priority interaction study.

The aggregate also mixes 1,125 six-dimension rows with 75 one-dimensional refusal rows. T16 represents 6.25% of the suite by construction, not by observed user need or expected loss. A product’s overall rank therefore embeds an unvalidated policy choice about the relative value of clean refusal versus all other work.

## Unique insight

LATTICE’s most valuable lesson is a **claim-ladder boundary** rather than a crypto rubric:

```text
high rubric score on response properties
≠ trustworthy response
≠ preferred response
≠ used response
≠ improved decision
≠ beneficial consequence
```

Scalable text-only judging can be a legitimate instrument for presentation, explicit uncertainty, constraint handling, or checklist completeness. It becomes misleading when the construct name absorbs downstream causal stages the study did not observe. “Decision-support utility” should be decomposed into at least:

1. **response affordance quality**—what the artifact makes visible or actionable;
2. **epistemic adequacy**—correctness, provenance, authority, freshness, and calibrated uncertainty;
3. **interaction usability**—whether the user understands and can operate the interface;
4. **uptake**—whether advice changes belief or action;
5. **decision quality**—whether the selected action is defensible under available information and stakeholder preferences;
6. **consequence**—benefit, burden, cost, loss, or harm.

A benchmark may evaluate any subset, but its title, score names, validity argument, and downstream use must identify the highest observed rung. LATTICE’s strongest observed rung is response affordance quality plus non-linked crowd preference—not decision utility.

A second insight is that “absolute judging” and “independent judging” are not synonyms. A judge can return one absolute score per product while seeing every competitor in a shared prompt. Evidence-view topology, call grouping, order, and co-visible artifacts are part of rater identity and must be frozen and tested.

## Limitations and validity threats

1. The construct name includes human decisions, but no decision process or consequence is observed.
2. Factual correctness, recency, source support, and live state are explicitly excluded despite high-stakes and fast-changing subject matter.
3. D2 asks for correct mechanisms while the judge lacks an authoritative reference or verification channel.
4. D5 rewards evidence-angle coverage rather than evidence existence, entailment, authority, or freshness.
5. Three domain experts are unnamed and their selection, authority, contributions, disagreements, and approval scope are absent.
6. The task taxonomy is grounded in evaluated product Sorin’s capability taxonomy, creating an undisclosed authoring/evaluation dependency.
7. The 80 seed queries have no documented source or user-traffic basis.
8. The 80→240 prompt requests Simplified Chinese, but the released benchmark is mostly English; translation or regeneration lineage is absent.
9. The 240→960 Codex expansion has no prompt, configuration, transcript, rejection ledger, or reproduction script.
10. Exact uniqueness does not establish semantic diversity, realism, or absence of templated near-duplicates.
11. Balanced task/category coverage is authorial balance, not population representativeness.
12. Every standard row gets every dimension; there is no criterion applicability or `not_applicable` state.
13. The below-six instruction imposes an uncalibrated score floor and severity prior.
14. The rubric structurally rewards comprehensive branching, checklists, and missing-information language, potentially favoring verbosity and rubric-aware style.
15. D3–D5 are strongly correlated, but no discriminant validation tests whether judges separate them.
16. The same GPT-5.2 label is used for query generation and judging, permitting generator–judge style alignment.
17. GPT-5.2 snapshot, API/service revision, seed, decoding/reasoning configuration, and request IDs are absent.
18. Each response is judged once; no judge-repeat reliability or ensemble sensitivity is measured.
19. Contrary to the natural reading of independent scoring, all six responses are co-visible in one judge call.
20. Product order is fixed by discovered file order; no order randomization or leave-one-out sensitivity is reported.
21. One shared-call failure affects all products; raw attempts/retries/invalid outputs are absent.
22. Product responses have no collection timestamps or configured-system identities.
23. UI/UX is claimed as part of product quality but not observed by the text-only judge.
24. Tool traces, citations as interactive objects, preview/confirmation controls, and execution outcomes are absent.
25. Live factual drift is avoided in scoring but not in query meaning or product-response collection.
26. Missing/error rows would be excluded per product, allowing unequal denominators; no fail-closed common-denominator policy exists.
27. No uncertainty intervals or dependence-aware analysis accompany 1,200 authored-query means.
28. Task and category comparisons are numerous, but no multiplicity or minimum-important-difference policy is stated.
29. Integer dimensions and floor guidance make small reported mean differences hard to interpret without repeat variance.
30. Category weights are expert-authored but lack user-priority elicitation, loss calibration, or sensitivity analysis.
31. Equal weighting produces nearly the same aggregate ranking, so the claimed priority sensitivity is not demonstrated by category weights.
32. Sorin leads every standard dimension and T1–T15 task; alternative-user-fit claims are mainly a mid-tier or refusal hypothesis.
33. T16 receives 6.25% aggregate mass by suite design, not observed prevalence or consequence severity.
34. Human queries are separate from rubric queries, precluding item-level judge-human calibration.
35. Human annotator population, protocol, expertise, incentives, randomization, agreement, and uncertainty are absent.
36. Human preference includes Wayfinder, which is not part of the LATTICE score panel.
37. The unexplained zero caution and clarity reason counts threaten interpretation of the preference form.
38. “Serious error” lacks a released definition, authority model, and adjudication protocol.
39. Human data and analysis code are absent from the release despite the all-code-and-data statement.
40. Preference measures comparative appeal, not correctness, uptake, decision quality, or consequence.
41. The release has smoke tests only; no scoring unit tests, schema mutation tests, replay fixture, or paper-table test is shipped.
42. Rubric updates are presented as easy, but changing criteria, weights, prompt, judge, or call topology creates a new instrument and breaks score comparability unless bridged.
43. No contamination analysis addresses products potentially trained or tuned on Sorin’s public capability language or the released queries.
44. The study cannot support financial advice, safety, professional validity, production fitness, or deployment readiness.

## Reproducibility and operational realism

Paper preservation and score inspectability are strong. The immutable PDF/text/TeX and both official release snapshots are hash-pinned. The appropriate pre-v1 commit is only eight days before submission; acquisition HEAD is about 23 hours after v1 and changes only README citation text. The archive passes CRC checks and includes all 1,200 queries, all six 1,200-response files, all 7,200 score/rationale records, the rubric, judge prompt, scoring and aggregation code, generation assets, and usage. Core displayed score tables are reproducible from released JSON without paid calls.

Full experiment reproduction is not possible. Product responses cannot be recollected under the original configurations; the judge model snapshot and API receipts are absent; one-shot GPT-5.2 calls are stochastic and expensive; the Codex 960-query generation is not reproducible; and the complete human study is unreleased. The score JSON is therefore a strong immutable observation artifact but not a complete execution receipt.

Operational realism is mixed. Evaluating actual product outputs recognizes the configured-system nature of agents. However, stripping each system to one unverified text response removes the very operational features invoked—tools, data feeds, latency, UI, controls, citations, and execution. The design is realistic as a **black-box response-corpus comparison**, not as a replayable production evaluation or prospective human decision study.

## Transferable benchmark implications

1. **Name the highest observed rung.** A text-only rubric score should be called response-property or artifact-affordance evidence unless uptake, decisions, and consequences are separately observed.
2. **Use an explicit utility chain.** Bind response observation → user exposure → comprehension → uptake → action → outcome, with absent links marked unsupported rather than rhetorically bridged.
3. **Separate preference from utility.** Preserve rater population, evidence view, choice set, reason taxonomy, repeated-measures structure, agreement, and uncertainty. Preference is one stakeholder response, not benefit.
4. **Freeze judge topology.** Record co-visible artifacts, batch size, product order/randomization, model snapshot, instructions/schema hashes, API settings, request IDs, retries, and raw outputs. Test isolated versus joint judging.
5. **Type criterion applicability.** Permit `not_applicable`, and map each task/requirement to relevant dimensions before scoring. Do not penalize a direct explanatory answer for lacking an action plan unless the public task requires one.
6. **Keep epistemic adequacy distinct from presentation.** Correctness, provenance, authority, freshness, uncertainty calibration, structure, and actionability require separate evidence views and claim families.
7. **Treat rubric weights as policy.** Record whose preferences/losses they represent, how elicited, and rank/decision sensitivity. Do not call author-chosen balanced weights “user priorities.”
8. **Preserve configured-system identity even for products.** Capture time window, surface, account state, product revision, tool/data access, collection protocol, failures, and immutable receipts.
9. **Require authoring-independence disclosure.** If a task taxonomy comes from one evaluated system’s product ontology, record that dependency and use independent review, contrast tasks, or held-out authoring to test advantage.
10. **Bridge instrument updates.** New dimensions, prompts, judges, call topology, or weights create a new measurement version. Use anchor items and overlap panels before longitudinal comparison.

## Concrete repository actions

1. **Do not add a crypto-specific schema or another generic rater contract.** Existing configured-system, evidence-view, grader/rater, metric-monitoring, plural-judgment, task-health, release, and validity machinery can represent most requirements.
2. Add one consolidation task to integrate a **response-quality → preference → uptake → decision → consequence claim ladder** and the **joint-versus-isolated judge topology** into the canonical taxonomy and synthesis index, reusing existing contracts.
3. For future memo/recommendation pilots, keep artifact quality and downstream utility as separate estimands. A good memo score may license a bounded artifact claim; a decision-utility claim requires a prospective user or simulated-decision protocol with predeclared information, action, loss, and consequence records.
4. When model judging multiple candidate artifacts, run at least an isolated-versus-joint and order-randomization canary. Treat material score/rank movement as a rater-instrument effect, not agent capability.
5. If LATTICE is revisited, acquire any later release, pin timing, check whether human data/protocol and model snapshots were added, and run repeated isolated/joint judge calibration before upgrading claim status.
