# Paper and Release Review: $OneMillion-Bench — Wage-Cost Coverage Is Not Economic Value Delivered

## Source and review status

**Deep review and release audit.** I read the complete immutable arXiv v1 paper and all 400 rows of the pinned official dataset, and inspected the complete inventories and core grading/execution code in the nearest pre-v1 and acquisition-time official GitHub archives.

- **Paper:** Qianyu Yang et al., *$OneMillion-Bench: How Far are Language Agents from Human Experts?*, arXiv:2603.07980v1 (9 March 2026), https://arxiv.org/abs/2603.07980v1
- **Local PDF:** `data/papers/pdfs/2603.07980v1-onemillion-bench.pdf` (39 pages; SHA-256 `97b53e25372ea883d5b2b94b39bea73f706caab126eddefdff8188131b1bfbee`)
- **Local text:** `data/papers/text/2603.07980v1-onemillion-bench.txt` (SHA-256 `0f0db408998ddac8c25341366fe8f6d68904b503d8712130e885a076eccb9db1`)
- **Official code:** https://github.com/humanlaya/OneMillion-Bench
- **Paper-time code:** commit `335372069513e5c41e333d6a64f16b7ca0eb0d87`, 31 minutes before v1 submission; local archive `data/sources/releases/2603.07980v1-onemillion-bench/humanlaya-OneMillion-Bench-3353720.zip`
- **Later code:** commit `b82d627db853eda4584572cc261336e19f5c0286` (21 April 2026); local archive `data/sources/releases/2603.07980v1-onemillion-bench/humanlaya-OneMillion-Bench-b82d627.zip`
- **Official dataset:** https://huggingface.co/datasets/humanlaya-data-lab/OneMillion-Bench, pinned at revision `5cf9d5005e2e1f20b4481ed50846161697e82a73`; all five JSON files are local under `data/sources/releases/2603.07980v1-onemillion-bench/dataset/`
- **Provenance and exact hashes:** `data/sources/releases/2603.07980v1-onemillion-bench/provenance.json`
- **Timing boundary:** the dataset was created after v1 submission and the pinned revision is dated 11 March. The later code adds support for its five array-valued JSON files. Both are official release evidence, not proof of the exact corpus and implementation that produced v1 results.

## One-sentence contribution

$OneMillion-Bench releases 400 bilingual, detailed rubric-scored research questions across five selected domains and reports 35 model/search/deep-research systems, but its dollar column re-labels human wage-cost attached to threshold-passing benchmark items as agent “economic value,” without observing a delivered artifact, acceptance, substitution, workflow use, revenue, savings, benefit, or loss.

## Why this matters for `skill-bench`

This review advances charter objectives A, B, D, and E. The benchmark is directly mission-aligned in its ambition: expert-authored, authority-sensitive work; conflicting evidence; localized rules; negative consequences; configured search treatments; cost reporting; and a score-to-economic-claim bridge. It also supplies the clearest reviewed example of why **task cost, score, and realized value must be different records**.

The concrete evidence is the full paper, 400 current task records, 6,758 rubric criteria, and both official code snapshots. This is comparative expansion feeding consolidation, not a proposal to narrow `skill-bench` to law, finance, industry, healthcare, or science. Useful completion is a bounded claim: performance under a text-response/rubric-judge instrument over a purposive five-domain portfolio—not human-expert equivalence, professional readiness, or dollar value delivered.

## Research question and claim ladder

A defensible question is:

> How do configured language systems, with and without web-search scaffolds, satisfy expert-authored textual criteria on 400 selected bilingual professional and scientific research questions?

The paper instead often climbs this chain (abstract and pp. 1–3, 12–15):

```text
selected professional scenario
→ expert-authored question/reference/rubrics
→ text response
→ model-judge criterion hits
→ weighted Expert Score
→ 0.70 task pass
→ senior time × wage assigned to passing items
→ economic value/output/profit margin
→ autonomous professional labor and practical readiness
```

Only the middle instrument is substantially instantiated. A threshold-passing response has not been used or accepted in a workflow. Human completion cost is not customer willingness to pay, avoided cost, revenue, surplus, benefit, or loss-adjusted value. The paper's “economic value” and “profit margin” language therefore promotes a benchmark observation across several unevidenced links.

## Methodology and system

### 1. Portfolio and denominators

The paper allocates exactly 80 questions to each of Finance, Law, Healthcare, Natural Science, and Industry, split evenly into 40 “Global” and 40 Mainland-China cases (pp. 1–7). It variously reports 37 second-level subdomains and 86 third-level categories (p. 5), while Figure 3 and Appendix B report 92 third-level categories (pp. 5, 20–22). The current release contains 68 distinct second-level labels and 161 distinct third-level strings because Chinese and English labels are retained separately; it has 280 unique `case_id`s. Healthcare, Industry, and Natural Science contain 40 bilingual pairs each, while Finance and Law contain 80 language-distinct cases each.

This is an equal-cell purposive assembly, not a sample of professional work, industries, occupations, decisions, economic exposure, or task frequency. The authors call the five domains “representative” while immediately noting many high-value fields are uncovered (p. 13). No eligible-work universe, selection funnel, inclusion probability, task-frequency distribution, consequence sampling, occupation mapping, employer/user demand, or domain-weight rationale is reported.

The current dataset confirms real topical breadth, but labels are not coverage validity. Equal domain weighting produces a policy-defined five-cell mean. It does not estimate the distribution of economically valuable work.

### 2. Experts, authoring, review, and task selection

One specialist drafts a task, reference answer, and rubrics; several frontier agents test it; a second same-subdomain specialist reviews it; and a third specialist audits unresolved or risky cases (pp. 4–5). Low-difficulty cases solved by all tested agents are removed; universally low-scoring cases receive upper-bound review. The paper says curation involved more than 2,000 expert hours and names 15 major contributors who agreed to attribution (pp. 1, 20).

Important authority evidence is absent:

- recruitment source, eligibility, credentials, tenure, current practice, jurisdiction, and conflicts;
- author/reviewer/task assignments and counts;
- contributor hours by authoring, review, adjudication, and time estimation;
- compensation, consent, ownership, withdrawal, and permitted transformations;
- independent initial judgments, disagreements, adjudication outcomes, revision counts, rejection rates, or defect yield;
- whether the experts estimating senior completion time are the task authors or independent professionals.

The process is also outcome-conditioned. Tasks must defeat several contemporary systems and easy items are removed. This can create useful frontier challenge items, but it changes the estimand from professional-work performance to performance on selected model-resistant work. The tested agents, exact retention threshold, number of attempts, failed candidates, and task-selection history are not released.

### 3. Task and source realization

The paper describes semi-open tasks with multiple valid approaches, reference answers, authoritative citations, conflicting evidence, local standards, and process-sensitive correctness (pp. 4–7). The five long appendix examples are detailed and often genuinely diagnostic: financial source authority, legal doctrine, clinical guidance, scientific evidence, and causal ML diagnosis.

But the released unit is a **text question plus answer-bearing criteria**, not an executable professional task package. All 400 `system_prompt` fields are empty. The release includes no reference answers, source files, source/citation manifest, evidence snapshots, expected artifact schema, environment, professional recipient, downstream operation, or acceptance record. Only six of 6,758 criteria contain a URL or DOI-like string, although 279 mention citation/source/reference/official concepts. The judge sees the question, response, and criterion text—not the alleged authoritative sources.

This creates two validity problems:

1. **Source verification is mostly unobservable.** A criterion can check whether expected facts or a link appear, but the judge cannot establish source existence, authority, entailment, valid time, completeness, or agent access.
2. **Public criteria leak answer content.** Detailed exact facts, conclusions, formulas, and forbidden errors are useful for audit and grader calibration, but once public they are no longer secure capability items.

The “time-invariant” construction claim (p. 4) conflicts with both the paper's December-2025/February-2026 case example and the current release: 125 rows are weakly time-sensitive and 26 strongly time-sensitive. Search-provider index, retrieval date, source version, cutoff enforcement, and unavailable-source policy are not fixed.

### 4. Rubrics, scoring, and pass threshold

For task `q`, the paper sums criterion scores, divides by the sum of positive weights, clips to `[0,1]`, and calls the result Expert Score. A task passes at `Expert Score ≥ 0.70`; task scores are averaged within domain and domain means are averaged overall (pp. 3, 8–10). Negative criteria penalize unsafe, unprofessional, hallucinated, or instruction-violating behavior (pp. 5–6).

This is transparent arithmetic, but not calibrated measurement:

- the 0.70 threshold has no expert acceptability study, downstream consequence study, sensitivity/specificity analysis, or loss basis;
- binary criterion hits ignore degree, applicability, uncertainty, and insufficient evidence;
- correlated criteria can multiply one underlying fact or style preference;
- criterion weights have no reported elicitation, normalization, agreement, or utility calibration;
- rubric-type means mix heterogeneous criteria and task denominators;
- domain equality is an aggregation policy, not an economic or construct weight.

The release audit finds 6,758 criteria: 5,099 positive and 1,659 negative, with 11–37 per task (mean 16.895). Positive-weight denominators range from 47 to 146; 393 of 400 are not 100. Weights range from -20 to +12, contradicting the paper's stated -20 to +10 range (p. 6). Fourteen rows have non-contiguous criterion numbering. Label vocabulary also drifts (`Instructions Following`/`Instruction Following`, `Analytical Reasoning`/`Viewpoint Analysis`, Chinese labels, and `Others`). These defects need not change every score, but they show that a released rubric corpus requires semantic and structural validation beyond expert branding.

### 5. Judge and observer view

The released grading prompt asks one model to decide all criteria as binary yes/no based only on direct text in the response. The parser accepts several yes spellings; missing/unparseable criteria become `NA`, while later aggregation code skips `NA` in some summaries. The paper reports a six-judge/five-agent sensitivity figure and says rankings remain stable even though absolute scores differ by roughly eight points for a top system (pp. 11–12).

This does not establish judge reliability. V1 reports no human criterion labels, expert-judge comparison, criterion-level agreement, chance correction, confusion matrix, calibration, domain/language slices, repeated judge calls, evidence-view audit, or uncertainty. The exact plotted values and analysis records are not released. “Moderately consistent” and “stable” are not accompanied by a rank statistic or interval.

The paper itself acknowledges that rubrics are less objective than exact-answer checks and rely on judge capability (p. 13). More fundamentally, the observer view cannot inspect the cited source, artifact structure, calculation lineage, hidden assumptions, or consequential state. It measures answer-text agreement with answer-bearing criteria.

### 6. Configured systems, search, repeats, and uncertainty

V1 reports 17 base models, their 17 search-enabled variants, and three deep-research systems—described as 35 models despite totaling 37 listed configurations (pp. 8, 38–39). Provider, thinking effort, temperature zero, and maximum output tokens are listed in Appendix Table 6. Search-scaffold comparisons include official providers, OpenRouter, and no search (pp. 10–11).

The paper's domain tables contain useful evidence that search is a treatment rather than an unconditional capability gain: several systems improve sharply while others regress, and effects vary by domain. But “base + search” is not one controlled intervention across providers. Search API, index, tool schema, prompting, orchestration, query limits, result/page exposure, date, retries, context policy, and provider-native behavior differ.

Main leaderboard cells appear to be one response per task. No task-level repeats, confidence intervals, model-family/task/domain clustering, paired search-effect uncertainty, invalid-run counts, timeout policy, missingness sensitivity, or multiplicity adjustment is reported. The only large repeat experiment samples up to 128 outputs on the 40 Global Finance questions and reports pass@k and pass^k curves (p. 12); the release config supports this, but outputs and analysis are absent. `pass@k` and `pass^k` answer different selection/reliability questions and do not validate single-attempt deployment reliability.

### 7. Economic value and cost transformation

The paper estimates each task's nominal human labor cost as the mean time from two to three senior experts multiplied by a regional hourly wage. U.S. sources include OEWS and selected industry sources; China uses tier-1-city wage guidance. Annual figures are divided by 2,080 hours; wage-only sources receive a 1.3 benefits multiplier (pp. 2–3). Table 1 totals approximately USD 1.008 million for the 200 Global cases and CNY 0.922 million for the 200 China cases.

This is a **human input-cost annotation**, with several limitations:

- raw per-expert estimates, roles, instructions, disagreement, revisions, and uncertainty are absent;
- reported averages of roughly 22–31 hours per task imply many thousands of hypothetical completion hours, distinct from the reported 2,000+ curation hours;
- regional wage sources, role mappings, seniority adjustments, exchange-rate choices, and every task-level valuation row are not released;
- wage plus benefits is employer cost, not output value, willingness to pay, marginal product, avoided loss, or expert market billing rate;
- completion time does not account for quality variation, review, collaboration, tooling, liability, or downstream consequence.

The result tables' “Economic Value” is not defined by an explicit equation linking task score to dollars. It cannot be Expert Score times total cost: for example, Claude Opus 4.6 has 55.0% Global Expert Score but USD 439.2k, not approximately 55% of USD 1.008m. The values are consistent with attaching full task cost to threshold-passing items, but exact reconstruction is impossible because task-level values and pass records are absent. Either way, no money or accepted work changed hands.

Section 5.1 then interprets benchmark dollars against API inference cost as economic output, unmet demand, and “extremely high profit margins” (p. 12). This is the paper's largest validity failure. It compares a tiny generation bill with the full nominal labor cost of threshold-passing questions while omitting expert review, correction, integration, rejected output, error loss, tool/infrastructure overhead at task level, user acquisition, organizational process, and liability. No observed workflow or economic transaction supports the margin.

## Limitations

1. **Sampling:** five equal domains, model-resistant item filtering, and no eligible-work frame support a purposive challenge portfolio—not prevalence, occupation, industry, or economic estimates.
2. **Expert authority:** qualifications, assignments, independent judgments, disagreement, adjudication, labor, compensation, and approval records are absent.
3. **Task realization:** current public items are text prompts and answer-bearing criteria without source packs, reference answers, native artifacts, environment state, recipients, or downstream operations.
4. **Measurement:** one binary model judge applies dependent, uncalibrated criteria through an unvalidated 0.70 threshold; human criterion labels and uncertainty are absent.
5. **Configured-system inference:** provider-specific search and deep-research bundles are heterogeneous; main results lack repeated task trials, paired uncertainty, invalid-run accounting, and immutable search identity.
6. **Economic inference:** human time×wage is an estimated input cost. No acceptance, correction, use, substitution, resource change, benefit, revenue, or loss is observed.
7. **Reproduction and lifecycle:** the later official dataset and array-capable runner postdate v1, while paper outputs, judgments, value rows, result tables, and exact run configurations are not released; public criteria are contaminated for future capability use.

## Release inspection and reproducibility

### Dataset audit

The pinned official release contains exactly 400 unique IDs and 400 unique question strings, evenly divided across five domains and two language labels. It preserves the current questions, taxonomy, time-sensitivity labels, and 6,758 criteria under Apache 2.0. This is substantial inspectability for content and grader auditing.

It does **not** include reference answers, source packs, provenance, expert records, task time/wage/value rows, candidate selection history, model outputs, judge outputs, costs, or paper result tables. Consequently the paper's task validity, source correctness, expert-score results, judge sensitivity, and dollar values cannot be independently reconstructed.

### Code timing and operability

The nearest pre-v1 commit contains the grading prompt/parser and runner, but scans `*SQL_Item_*.json` and expects one JSON object per file. The official dataset is five JSON arrays. The 21-April commit changes the loader to expand array elements and scans general `*.json`, making the current release usable. Grading prompt, parser, and default configuration are byte-identical between the two audited commits, but the later orchestrator is not paper-time evidence.

The code records responses, rubric judgments, token usage, API cost, retries, and reports; repeated sampling/judging is configurable. This is useful operational machinery. Exact v1 replay remains blocked by absent outputs/config snapshots/result tables, mutable proprietary endpoints and search indexes, unknown judge identity/assignment for headline tables, and the paper-time code/data interface mismatch.

### Operational realism

Realism is strongest in textual content: long prompts, local rules, competing evidence, professional role framing, primary-source expectations, calculations, and harmful-error penalties. It is weakest in workflow realization: no files, editable artifacts, environment state, stakeholder interaction, clarification, permissions, institutional review, execution, downstream recipient, correction loop, or realized consequence. The benchmark tests **professional-style research responses**, not autonomous professional labor.

## Evidence and claim boundaries

### Strongly supported

1. The authors assembled and released a balanced 400-question bilingual portfolio across five selected domains with unusually detailed positive and negative criteria.
2. The paper evaluates a broad set of configured base/search/deep-research systems and reports substantial heterogeneity across system, search condition, domain, language subset, and rubric type.
3. Search access can help or harm under this instrument, motivating configured-system and evidence-integration diagnosis rather than “search enabled” as a scalar upgrade.
4. The public code makes the criterion-judge prompt, binary scoring, parser, retries, cost tracking, and repeat controls inspectable.

### Partially supported

- **Professional content:** detailed scenarios and domain-authored criteria provide content relevance, but expert qualifications, transformation lineage, agreement, independent validity, and downstream acceptance are absent.
- **Source-sensitive reasoning:** prompts/criteria require authoritative citations and conflict resolution, but source packs and judge source access are absent.
- **Judge robustness:** the six-judge figure suggests ranking may be less sensitive than absolute levels for five selected systems, but no exact corpus, human labels, statistic, or criterion-level reliability is available.
- **Challenge:** low pass rates show difficulty for selected configurations on outcome-filtered tasks, not representative professional failure rates.

### Not supported by v1

- human-expert parity or distance to an expert performance distribution;
- occupational, industry, or economy-wide representativeness;
- professional acceptance, safety, production fitness, or readiness;
- that the 0.70 threshold is a minimum professional standard;
- that public criterion compliance establishes source authority, entailment, or correct evidence use;
- causal search/scaffold effects across heterogeneous provider implementations;
- reliable single-attempt or repeated deployment performance;
- dollar value, revenue, savings, profit, productivity, economic readiness, or autonomous-labor substitution;
- exact paper-result reproduction from the current release.

## Unique insight: keep five value objects separate

The benchmark makes visible a distinction that `skill-bench` should enforce:

```text
human task effort/cost
≠ benchmark criterion score
≠ thresholded acceptable-output probability
≠ observed workflow resource saving
≠ realized stakeholder/economic value
```

A task can be expensive for a human and still have little marginal value, or be cheap but highly consequential. A response can earn partial rubric credit while being unusable due to one gate. A threshold-passing benchmark response can require more review than it saves. A time saving can create no benefit—or negative value—if error loss, liability, distributional effects, or displaced responsibilities dominate.

The correct bridge is prospective and loss-aware:

```text
versioned task cost estimate
→ configured-system output distribution
→ independent professional accept/reject/correct decision
→ review and correction resources
→ realized downstream use and state
→ benefit/cost/loss by stakeholder
→ bounded economic decision claim
```

No scalar multiplication should skip these links. This sharpens GDPval's “speed/cost scenario” warning and AlphaEval's “score × replacement cost” warning: $OneMillion-Bench goes further by presenting nominal wage-cost captured by passing items as output and profit margin.

A second insight is that **answer-bearing rubrics can increase diagnostic resolution while decreasing capability security**. The public release is excellent for auditing criterion dependence and judge behavior. It should be treated as calibration/regression material, not a private frontier-capability instrument.

## Comparison with adjacent professional benchmarks

- **GDPval:** GDPval has a clearer top-down occupational frame, experienced-professional recruitment, native artifacts, and repeated occupation-matched comparisons. Its time×wage scenarios are still not observed productivity. $OneMillion-Bench is easier to audit criterion-by-criterion but lacks artifact and human-judgment evidence and makes the stronger unsupported value-delivered leap.
- **Agents' Last Exam:** ALE adds executable environments, native artifacts/state, and task-specific graders but still lacks occupational sampling and verifier closure. $OneMillion-Bench adds bilingual/localized textual criteria and explicit human-cost labels, not workflow execution.
- **JobBench:** JobBench begins from worker delegation preference and artifact-rich packages, but preference is not benefit. $OneMillion-Bench begins from author-selected high-value scenarios; neither observes worker uptake, correction, or outcomes.
- **AlphaEval:** AlphaEval has stronger prospective company-demand provenance and recurring partner refinement, but private transformations and score×cost claims remain unauditable. $OneMillion-Bench releases its current questions/rubrics, while withholding the time/value/result bridge required for its economic claim.
- **ResearchRubrics:** ResearchRubrics reports a much larger expert authoring investment and a human/model judge protocol, though criterion dependence and source-observer limits remain. $OneMillion-Bench supplies negative criteria and equal domain cells but almost no expert or judge-validation detail.
- **Professional benchmark evolution matrix:** the benchmark belongs between broad static artifact/research packages and executable workflow suites. Its strongest repair is detailed localized criterion transparency; its unresolved links are work sampling, source observer access, artifact/state realization, criterion reliability, threshold validity, and score-to-consequence/economic inference.

## Transfer to `skill-bench`

### Retain

1. Use positive and negative criteria for requirements and professionally serious failure signatures, but keep safety gates separate from additive quality.
2. Preserve localized jurisdiction/standard and valid-time requirements as typed source-authority records.
3. Evaluate search as a configured treatment, with possible regressions and evidence-integration failures.
4. Report score distribution, threshold pass, cost, and rubric-family outcomes separately.
5. Release public audit/calibration tasks with rich criteria while maintaining distinct secure or refreshed capability forms.

### Repair

1. **Separate portfolio denominators:** eligible work frame, sampled content, realized assembly, and licensed inference population.
2. **Preserve expert lineage:** qualifications, role/task assignment, independent ratings, disagreements, revisions, labor, compensation, and approval scope.
3. **Bind source claims to evidence:** immutable source/version, authority, valid time, entailment, agent exposure/access, artifact citation, and judge observer view.
4. **Calibrate thresholds:** use professional acceptance decisions, false-accept/false-reject costs, alternative valid outputs, and downstream consequences; never call 0.70 a professional standard by stipulation.
5. **Model criterion dependence:** identify gates, shared causes, alternatives, applicability, and redundant evidence before aggregation.
6. **Estimate reliability hierarchically:** repeated outputs and judge calls, invalid/missing policies, paired search treatments, and task/family/domain clustering.
7. **Version configured systems:** provider, model alias, prompt, search API/index/date, query budget, page access, context policy, retries, judge, and parser.
8. **Forbid score-to-dollar shortcuts:** task time/wage is a cost descriptor; economic claims require observed acceptance, correction, use, consequences, and loss.

## Concrete next actions

1. **No new queue task.** Existing expertise-transfer, participation, source/evidence-state, benchmark-bundle, configured-system, artifact-admissibility, task-health, metric-monitoring, and validity-argument machinery already has homes for these requirements.
2. In the next economic-claim consolidation, add a machine-rejectable case where `sum(human_cost_of_passed_tasks)` is labeled `economic_value_delivered` without workflow acceptance/use evidence.
3. In the next real expert pilot, record raw task-time estimates separately from authoring/review labor and run a matched unaided versus agent-assisted workflow with review, correction, severe defects, downstream acceptance, and stakeholder loss.
4. Treat all 400 released rows as public audit/calibration items; do not use their answer-bearing criteria for secure capability claims.

## Action items

- [x] Read the complete immutable v1 paper.
- [x] Audit all 400 released task records and 6,758 criteria.
- [x] Pin and inspect the nearest pre-v1 and acquisition-time official code archives.
- [x] Preserve the code/data timing boundary and paper-time array-loader incompatibility.
- [x] Reconstruct portfolio, expert workflow, scoring, search treatment, judge view, repeats, cost model, and economic claim ladder.
- [x] Compare GDPval, ALE, JobBench, AlphaEval, ResearchRubrics, and the professional evolution matrix.
- [x] Map findings to existing contracts without creating a duplicate build task.
- [ ] Obtain observed professional acceptance, correction, downstream use, and loss evidence before licensing any economic-value claim.
