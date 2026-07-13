# BigFinanceBench: a narrated derivation rubric is not yet an audited workflow

**Source.** Alex Wang et al., *BigFinanceBench: A Workflow-Grounded Benchmark for Financial-Research Agents*, arXiv:2606.03829v1 (2 June 2026), <https://arxiv.org/abs/2606.03829v1>.

**Full text read.** Immutable 25-page v1 PDF: `data/papers/pdfs/2606.03829v1-bigfinancebench.pdf` (SHA-256 `4be3cd6e9d1b72c2554c01c2e7655e1d89cca7e3d3ca534900b97c04e6ec5195`). Complete local extraction: `data/papers/text/2606.03829v1-bigfinancebench.txt` (SHA-256 `43de90d2daf543edb82540be75f0f5e9d803acb8d7e59d03a9026fae9e31f4a8`). Date read: 2026-07-14.

**Release evidence inspected.** Official GitHub commit `244fb7a4d57e0f6f5ac1d82c50f55c355f49a4bb` (tree `b735b94360b4570223bd3103ce5d077bc6f0332a`) and Hugging Face revision `c286cd57cff686e47b73d2d75c88236c69bc8e08`, both dated about 22 hours after v1. Local archive paths, hashes, complete inventories, and timing limits are in `data/sources/releases/2606.03829v1-bigfinancebench/provenance.json`. The GitHub archive contains 44 entries, a 50-item public subset, harness, analysis code, and tests. The Hugging Face archive contains the same subset plus 1,500 deduplicated traces and 3,000 deduplicated two-judge grades. The 878 held-back items and full-benchmark run outputs are unavailable.

## Bottom line

BigFinanceBench makes a valuable construct correction: a financial answer should expose entity, source, period, definition, assumptions, adjustments, formulas, and conclusion rather than receive credit only for the final number. Its 928 expert-authored questions, three repeated trials, visible tool trajectories, weighted binary criteria, and dual judges are materially stronger than isolated finance QA.

But its headline rubric score does not establish that a system executed an auditable analyst workflow. The grader sees exact reference values and gives credit whenever the **trace or final response contains positive textual evidence** for each criterion. The released item contract has no source locator, passage, authority, freshness, evidence-entailment, dependency, or alternative-derivation field. Tool outputs are heavily truncated before grading, and assistant assertions are admissible evidence. The instrument therefore measures agreement of a visible narrated trajectory with one reviewed decomposition, not independently verified provenance from source through calculation to conclusion.

The strongest transferable lesson is a sharper evidence chain:

`source identity/state → cited passage → extracted value/definition → transformation with dependency links → conclusion → criterion observation → licensed claim`

Credit at one link must not imply the next. A value mentioned in a trace is not evidence that it came from the right source; the right final number is not evidence that the derivation was valid; and a point-weighted decomposition is not causal localization unless dependency and observer validity are tested.

## Why this matters: charter relevance and research question

This is narrow expansion serving charter objectives A and B: finance is a methodological case for converting professional derivations into inspectable evaluation primitives, not a scope boundary for `skill-bench`.

The paper asks whether financial-research agents can be evaluated on practitioner-inspired, open-ended, multi-source question shapes at the derivation-level resolution used in expert review (pp. 1–2). The auditable question is narrower: on 928 deliberately difficult, publicly sourced, time-anchored numerical questions, how much of one expert-reviewed checklist do ten configured systems appear to satisfy under one ReAct harness and two model judges?

## One-sentence contribution

BigFinanceBench turns a final financial number into a weighted inventory of intermediate analyst claims, but it does not yet prove that those claims form an alternative-complete, source-entailing, dependency-aware, professionally validated workflow.

## Methodology and system

### Task sourcing, expertise, and admission

The corpus contains 928 items written from September 2025 through March 2026 by 52 paid finance professionals, predominantly current/former investment bankers and private-equity investors, with smaller equity-research and adjacent buy-side representation. Twelve separate reviewers audited items; the busiest reviewer handled over one quarter of the corpus (paper §3.1 and Appendix B, pp. 4, 12–14).

Each candidate had to fail the authors' in-house agent and at least one of Claude, ChatGPT, or Gemini before admission. Reviewers were instructed to retain depth—niche expertise, multi-step method, or judgment—and reject “stacked simplicity.” This creates a useful hard-case stress set, but also **outcome-conditioned selection**. It is not a frequency-weighted census of analyst work, as the paper acknowledges, and score prevalence cannot be transported to ordinary finance workloads. The exact tested model snapshots, attempts, prompts, outcomes, rejected inventory, and author-specific selection rates are not released, so the admission treatment cannot be audited for provider, author, or topic bias.

“Objective” meant expert consensus on the final figure, a fixed time point, binary verifiability, explicit units/rounding, and query disclosure of non-obvious assumptions. Authors used a “95 of 100 experts” heuristic to exclude methodology-specific intermediate steps. This is thoughtful guidance, not measured consensus: no 100-expert sample, independent alternative-solution search, expert/novice contrast, item-level qualification mapping, agreement statistic, or unresolved-disagreement ledger is reported. One author and one reviewer iterated until agreement, while only twelve reviewers covered 928 items. The paper's 748/928 substantive-review-log count shows active editing, but the logs are held back and do not establish alternative-path completeness or professional acceptance.

The corpus is concentrated in public-company, mostly US-listed, English-language research. TMT and diversified questions are overrepresented. It excludes proprietary databases, private markets, client clarification, live collaboration, and downstream decision use (Appendix A, pp. 12–13). Thus the evidence supports a deliberately varied public-equity stress inventory, not finance representativeness or deployment validation.

### Reference answers and rubric construction

Every item contains a query, short reference answer, and weighted checklist. The full corpus reportedly has 15,656 criteria and 36,241 points; 70% of reference answers are at most 20 characters and 63.2% of points receive a regex-derived Calculation label (Appendix F/H, pp. 16–17, 25).

The five rubric rules are Binary, Precise, Atomic, Self-contained, and Weighted. Criteria specify exact values/periods, generally receive 1–10 points, and the final answer receives a meaningful share (pp. 4, 13–14). The 95-of-100 heuristic is intended to avoid one-path artifacts.

Several tensions remain:

1. **Self-contained criteria can destroy dependency semantics.** Splitting each input, formula, and output permits partial credit, but treating them independently can count one upstream fact several times and award a downstream result without its prerequisites.
2. **Exact values make a latent answer key.** Criteria such as “Identifies $X” or “Calculates $Y” define expected outputs but usually do not bind them to source passage, calculation object, or provenance.
3. **Binary atomicity is asserted, not audited.** In the public 793-line subset, a simple lexical audit finds 45 criteria containing “and,” 17 containing “or,” and five containing “plus.” These are only flags, not proof of bundling, but no released split-review or dependence graph resolves them.
4. **Weights are uncalibrated utilities.** No stakeholder loss, expert acceptance threshold, information value, or empirical criterion-importance study justifies the additive 1–10 scale.
5. **Alternative derivations remain untested.** The paper says criteria are path-independent, but releases no contrast set of legitimate alternative methods and no false-rejection audit.

The public release reveals a concrete paper/data mismatch. The paper says criteria carry weights from 1 to 10 (pp. 4, 13). The dataset documentation changes this to 1–20, and the 50-item subset contains two 15-point lines and one 20-point line, all in `bf-a9408e6a52`. It also contains two duplicated exact criterion texts. These defects do not invalidate the corpus, but they show that expert review does not replace executable schema and health checks.

### Source and temporal controls

Questions are time-anchored and agents use public sources through `web_search`, `edgar_search`, `fetch_url`, and `python_exec` (paper §4.1, p. 6). Time anchoring reduces ambiguity, and EDGAR-specific search is a sensible common affordance.

However, the source layer is not frozen. The full master reportedly records anticipated source documents, optional links/screenshots, notes, and review logs (Appendix B, p. 12), but the released `DatasetItem` has only `id`, `query`, `reference_answer`, and `rubric`; all 50 public items omit `sources` and `annotator_notes`. Only 10/793 public criteria match a broad citation/source/filing lexical heuristic. The harness retrieves mutable SEC, investor-relations, search-provider, and web content without preserving canonical passage locators, content hashes, retrieval snapshots, or expected authority. Time-anchored answers can therefore coexist with source drift, removed pages, changed search rankings, or later restatements.

This is the central gap between **workflow narration** and **auditable derivation**. The grader can reward a stated number without establishing source existence, period, definition, authority, entailment, or whether the number was copied from an answer-bearing snippet. `skill-bench` should retain the time boundary but require immutable source/evidence identity or a declared live-evidence policy with access logs and adjudication.

### Configured systems, tools, and execution

Ten systems are run for three trials per question in a shared 50-step ReAct scaffold with public web/EDGAR retrieval, URL fetching, Python calculation, and a terminal final-answer tool (pp. 6, 14). The traces preserve prompts, tool specifications, provider request IDs when surfaced, token usage, costs, stop states, timestamps, and resolved model names when providers return them. This is good configured-system evidence.

Comparability is still bounded. Models use different providers, floating/preview endpoint labels, hidden provider behavior, tokenization, and defaults; `thinking=off` means no explicit thinking setting rather than a matched cognitive budget. Search results and fetched pages are live. The README correctly admits `python_exec` is not a security sandbox: it is an unsandboxed host subprocess with a five-second timeout. `fetch_url` blocks private-address targets, but the harness as a whole has no released outer-envelope filesystem/network canary. Common tools reduce one treatment difference; they do not make the configured systems or evidence exposure identical.

The public traces show operational failures worth retaining separately: after last-write deduplication, 1,079/1,500 terminate through `final_answer`, 281 through `no_tool_call`, and 140 at `max_steps`. These are different failure modes, not one capability score.

### Judge implementation and evidence view

Gemini 3.1 Pro Preview and Claude Opus 4.7 independently receive the question, reference answer, unweighted rubric text, final answer, and a formatted visible trace. The judge does not see criterion weights, reducing salience bias. It returns one boolean and explanation per line plus final-answer correctness; client code applies weights afterward (`big_finance_harness/grader.py`, lines 44–318 in the pinned archive).

The decisive observer limitation is in “positive evidence.” The prompt accepts evidence from the trace **and final answer**, including assistant text. It does not require a matching authoritative tool result, cited passage, executable calculation, or source-to-claim link. Nor does it encode `insufficient_evidence`, applicability, contradiction, or acceptable alternative. Missing judge entries silently become failed criteria.

The trace view is lossy by construction. Each tool result is capped at 4,000 characters, each tool argument at 1,500, and traces over 150,000 formatted characters retain only head and tail (`grader.py`, lines 54–117). A local replay over the 1,500 released deduplicated traces found:

- 1,374 traces contain at least one tool result that the judge truncates;
- 58 exceed the global 150,000-character cap and lose their middle; and
- the largest capped-format trace was 356,063 characters before global truncation.

The paper says judges see the “visible agent trajectory,” but they do not see an evidence-complete trajectory. Truncation may be operationally necessary; it must be recorded as an observer treatment and should force abstention for criteria whose supporting or contradicting passage was omitted.

### Metrics, repetition, and uncertainty

The paper's primary score averages the two judges within `(question, trial)`, trials within question, then macro-averages questions. This is a reasonable task-macro estimand. It reports three trials and 95% bootstrap intervals “over questions” (pp. 1, 6, 14).

The released `headline_table.py` does something materially different for uncertainty: it bootstraps individual `(question, trial)` records, treating three trials from one question as independent sampling units (lines 1–14, 28–42, 121–147). Balanced three-trial data leave the point mean unchanged, but this bootstrap does not preserve question clustering and can understate uncertainty for a new-question estimand. It also generates per-judge tables rather than the exact two-judge headline aggregation. The paper-time full outputs and analysis files are unavailable, so the published intervals cannot be reproduced or reconciled from the release.

The paper reports final-answer Cohen's κ of 0.952–0.973, but final-answer agreement does not validate criterion-level workflow grading. On the public release, a local paired audit found criterion-level κ from 0.722 to 0.884 across models, with raw agreement 0.862–0.944. Mean Opus-minus-Gemini rubric score differences range from −0.47 to +8.44 percentage points by evaluated model; GPT-5.5 differs by +5.87 points and Gemini 3.1 Pro by +8.44 points. This reproduces the paper's warning that rubric disagreement is larger and model-asymmetric (Appendix I, p. 18), while showing why final-answer κ is not the relevant validation statistic for the headline derivation construct.

No human labels validate judge criterion decisions. The paper mentions manual sample checks but gives no sample size, selection, rater evidence view, label matrix, errors, agreement, or adjudication. Both judges also appear in the evaluated lineup, creating self/family interaction possibilities. Averaging two judges is a panel policy, not ground truth.

## Evidence and reported results

The full-benchmark Table 3 reports rubric scores from 22.3% to 58.8% and final-answer accuracy from 6.6% to 44.3%. Every system earns more rubric than final-answer credit; across ten model aggregates, rubric and answer scores correlate at `r = 0.94`, with one rank inversion (pp. 6–8, 14). This supports the bounded claim that the fixed rubric exposes credited intermediate statements hidden by final-answer accuracy.

It does not establish that the extra 15.95 percentage points are valid workflow progress. Some may be genuine retrieval, definition, or calculation; some may be unsupported narrated values, duplicated dependent checkpoints, answer-key alignment, or judge over-credit. A criterion-level human/source audit and alternative-derivation contrasts are required to estimate that mixture.

The clean-setup analysis conditions on perfect Retrieval and Definition credit, then compares Calculation (pp. 8, 15). The authors correctly call it descriptive. Additional limitations are important:

- stage labels are assigned by the first rubric verb through regex, not by observed causal workflow state;
- “retrieval” can be credited from a mentioned value without verified retrieval;
- conditioning on perfect judge-awarded setup selects different task/trial subsets by model and can induce selection bias;
- GPT-5.4 Mini is excluded because its selected pool is small and a lower-tail outlier; and
- the fixed-effects model has no clustered uncertainty or sensitivity to judge/stage misclassification.

The result therefore supports “conditional rubric Calculation scores compress in this selected judged pool,” not “arithmetic is solved once setup is correct” or a causal localization of remaining model deficits.

Workflow specialization and routing are also descriptive. Workflow/skill labels come from GPT-5.5 three-sample voting with deterministic label-order shuffles; 5.4% of questions have three-way workflow ties and 6.0% have three-way skill ties (Appendix G, pp. 15–16). The public metadata contains a tenth `Other / Misc Lookup` workflow despite the paper's stated nine-category taxonomy. The coarse router is evaluated on the same 928 outcomes used to estimate group performance, without held-out routing validation, so its +4.5-point rubric gain is an in-sample upper estimate rather than deployed routing evidence.

## Release audit

### What is inspectable

The pinned post-v1 GitHub release provides a well-structured, typed harness; exact dependency pins; public dataset; tests; resumption logic; analysis scripts; and explicit warnings about floating snapshots and `python_exec`. The Hugging Face revision preserves all 50 × 3 × 10 nominal public-subset trajectories and both judge outputs. After last-write deduplication, every `(model, question, trial)` and `(model, question, trial, judge)` key is present.

The public subset exactly contains 50 unique items, 793 criteria, and 1,931 points. Recomputed two-judge, trial-then-question macro scores preserve the full rubric ranking except GPT-5.5 and Opus swap: Kendall's τ is 0.956, matching the paper. Yet the subset was explicitly stratified on **difficulty defined by median score across the same ten evaluated models**. Using model outcomes both to select the public form and to demonstrate ranking preservation is outcome-conditioned form construction; τ is useful release engineering evidence, not independent external validation.

### Row-count anomalies resolved

Two trace files contain 151 rows:

- `opus47`, `bf-a838bf1b8e`, trial 1: an OAuth/network error followed by a successful retry ending at `max_steps`;
- `sonnet46`, `bf-d1228a30ce`, trial 0: the same class of OAuth/network error followed by a successful retry ending at `no_tool_call`.

Three grade files contain 151 rows because the errored and retried traces were both graded: Opus's Opus-judge file has a zero-point error grade then a 47-point retry grade; Sonnet's Gemini and Opus files each have a zero-point error grade then a 72-point correct retry grade. The released analysis code intentionally keeps the last write for duplicate grade keys, and trace indexing also keeps the last row, so its headline path selects the retries. Raw JSONL consumers that count rows or keep first occurrence can produce different results. A stronger contract would mark supersession explicitly and exclude invalid traces before grading rather than rely on file order.

One additional serialization issue matters for tooling: Python text `splitlines()` treats a Unicode line-separator character inside at least one very large JSON string as a record break, while byte-level newline parsing succeeds. JSONL consumers should split on byte `\n`, validate each record, and preserve parse-error counts.

### Reproduction boundary

The release cannot reproduce the paper's headline experiment because the 878 held-back tasks, their rubric/source/review records, 27,840 full traces, 55,680 judge records, run manifest, costs, classifications, and paper analysis outputs are absent. The README says the harness reproduces the paper, but only the current scaffold and public 50-item results are inspectable. The post-v1 timing boundary also prevents assuming byte identity with paper-time code.

A local test collection attempt against the archive failed before execution because the repository environment lacked declared optional/runtime packages (`litellm`, `pytest-httpx`, and `pymupdf`). The pinned `pyproject.toml` and 47 advertised tests make recreation feasible, but no lockfile or container image is provided; full execution additionally requires paid/mutable model and search providers. This is not a test failure in the release itself, only a limit on this audit's execution evidence.

## Unique insight: derivation credit needs proof-carrying dependencies

BigFinanceBench reveals that **decomposing a solution is not the same as observing a workflow**. A checklist can make expert attention inspectable while remaining detached from the evidence and operations that supposedly produced each checkpoint.

For `skill-bench`, each derivation node should be proof-carrying:

1. **Claim:** normalized value, definition, period, unit, and scope.
2. **Evidence:** source identity/version, authority, passage locator, retrieval event, and entailment state.
3. **Operation:** formula/transformation identity, typed inputs, code or calculation trace, rounding policy, and output.
4. **Dependencies:** prerequisite, descendant, alternative, exclusion, and shared-evidence relations.
5. **Observer:** which artifact/trace/source views the grader actually received, including truncation or missingness.
6. **Verdict:** supported, contradicted, insufficient evidence, acceptable alternative, invalid observation, or failed.
7. **Claim ceiling:** exact checkpoint, coherent derivation, task success, professional acceptability, or readiness—never inherited automatically.

This design permits partial progress without laundering narration into provenance. It also separates **root localization** from **surface decomposition**. If one wrong source value causes five failed calculations, the benchmark should record one upstream retrieval/definition defect and five downstream consequences, not report six independent capability failures. Conversely, a correct downstream number reached through an invalid source or coincidental cancellation should not erase the root defect.

## Comparison with adjacent reviewed evidence

- **ResearchRubrics** shows that expensive expert decomposition makes criteria inspectable but can hide dependence, implicit obligations, answer anchors, and insufficient judge views. BigFinanceBench improves workflow trace access and separate item review, yet its exact-value criteria and source-free released contract sharpen the same answer-key and evidence-view problem.
- **MBABench** evaluates native spreadsheet values, formulas, and formatting, exposing why a correct current value can hide a broken dependency graph. BigFinanceBench has richer retrieval traces but no native derivation artifact or counterfactual recalculation. Together they motivate proof-carrying calculation graphs plus executable perturbations.
- **AARRI** demonstrates that check decomposition can misclassify substantively legitimate action when lexical/executable observers are incomplete. BigFinanceBench similarly needs accepted alternative derivations and observer insufficiency, not only binary line credit.
- **Consulting cognitive traps** separates source existence, entailment, authority, scope, and freshness. BigFinanceBench's public-source design should implement these as separate evidence predicates rather than infer all of them from a number appearing in a trace.
- **Existing artifact/evidence-view contracts** already provide homes for authoritative representations, observer admissibility, criterion dependencies, trace locators, invalid/insufficient states, task health, metrics, and validity claims. A finance-specific schema would duplicate them.

## Limitations and validity threats

1. **Outcome-conditioned task admission.** Every item had to defeat an in-house and another frontier system, selecting a hard tail whose construction depends on unreleased tests.
2. **No work-population sampling frame.** The suite is purposive, public-equity-heavy, US/English-heavy, and explicitly not workload-frequency weighted.
3. **Expert authority is coarse.** Qualifications are not linked to items/claims, twelve reviewers are concentrated, and no independent agreement or unresolved disagreement is reported.
4. **Consensus is heuristic.** “95 of 100 experts” is author guidance, not measured agreement or alternative-method validation.
5. **Review evidence is private.** Source lists, screenshots, author notes, review logs, edits, rejected items, and alternate calculations are held back.
6. **Public source provenance is absent.** Released items omit source locators, snapshots, hashes, authority, passages, and anticipated-source fields.
7. **Temporal drift remains.** Questions are anchored, but live web/search/IR/SEC observations and retrieval rankings are not frozen or versioned.
8. **Narration can receive workflow credit.** Assistant text and final answers count as positive evidence without mandatory source or calculation proof.
9. **Judge evidence is truncated.** Most public traces lose at least one tool-result suffix; 58 lose their middle globally.
10. **No insufficiency state.** Missing evidence, omitted judge entries, observer truncation, and substantive failure can all collapse to false.
11. **Reference/criterion answer anchoring.** Judges see the exact reference and exact expected intermediate values, encouraging agreement with one authored witness.
12. **Atomicity and independence are unvalidated.** No criterion split audit, dependency graph, effective-information analysis, or alternate-derivation contrast set is released.
13. **Additive points are uncalibrated.** Criterion weights lack stakeholder utility, severity, repair-cost, gate, or professional-acceptance evidence.
14. **Paper/release weight conflict.** The paper specifies 1–10; the public release contains weights up to 20 and documentation acknowledges 1–20.
15. **Criterion duplication exists.** Two exact rubric texts repeat in the public subset despite self-contained expert review.
16. **Final-answer κ is not rubric validity.** Criterion-level public agreement is materially lower and model-asymmetric; no human criterion validation is reported.
17. **Evaluated systems serve as judges.** Self/family effects are possible, and averaging is an unvalidated panel policy.
18. **Trial uncertainty is misclustered in released code.** The bootstrap resamples question-trial records rather than questions, contrary to the manuscript's stated unit.
19. **Clean-setup conditioning is endogenous.** Setup is a judge-derived selected state, stage labels are lexical, and one model is excluded post hoc.
20. **Stage labels do not prove causal process.** First-verb regex categories describe criterion wording, not where an observed failure originated.
21. **Workflow labels are model-derived.** Three-way ties, first-sample tie-breaks, no human validation, and a nine-versus-ten category discrepancy bound specialization claims.
22. **Routing gains are in-sample.** Group outcomes and best model choices use the same benchmark; no held-out router trial is reported.
23. **Public subset validation is outcome-conditioned.** Difficulty uses the ten systems' scores, then ranking preservation is measured on those systems.
24. **Retry lineage is implicit.** Error and retry rows coexist and are both graded; last-write deduplication, not an explicit supersession record, determines the result.
25. **Full results are unverifiable.** Held-back tasks, traces, grades, classifications, manifests, and paper tables are not publicly inspectable.
26. **Configured-system identity remains mutable.** Preview/floating provider endpoints and live search prevent exact replay despite useful trace metadata.
27. **Execution isolation is incomplete.** `python_exec` is explicitly not a sandbox, and no outer-envelope canary is released.
28. **Professional validity is untested.** No analyst receives, audits, repairs, accepts, reuses, or makes a decision from agent work under matched workplace conditions.
29. **No deployment, representativeness, or general-capability inference.** The authors appropriately warn against deployment interpretation; the same boundary applies to broader finance competence.

## Reproducibility and operational realism

**Reproducibility is strong for inspecting the current public instrument and weak for reproducing the headline experiment.** The immutable paper, pinned post-v1 code/data, exact public questions, rubric lines, traces, grades, typed harness, dependency pins, and analysis logic permit unusually detailed auditing. The public two-judge scores, rank fidelity, row anomalies, truncation exposure, weight anomalies, and criterion agreement can be recomputed locally.

The full 928-item experiment cannot be replayed or independently analyzed. It requires held-back data, commercial/mutable endpoints, live search APIs, provider credentials, changing public pages, and unreleased full outputs. No container image, lockfile, frozen source pack, or paper-time commit exists.

**Operational realism is mixed.** Multi-source public research, long retrieval loops, EDGAR, numerical calculation, visible failure modes, three trials, and practitioner-authored questions are materially closer to analyst research than page-conditioned QA. The benchmark omits proprietary tools, clarification, stakeholder interaction, native spreadsheet/memo artifacts, handoff, revision, compliance, source custody, decision consequence, and observed professional acceptance. Its strongest licensed construct is **rubric agreement on visible public-source research trajectories under one configured harness**, not analyst competence or deployable finance work.

## Transfer to skill-bench

1. **Require proof-carrying derivation nodes.** Bind every source/value/definition/formula/conclusion checkpoint to immutable evidence locators, typed operations, dependencies, and observer views.
2. **Separate mention, provenance, entailment, and causal use.** A trace statement can satisfy a mention predicate only; source authority, passage entailment, extraction, and downstream adoption require their own evidence.
3. **Preserve dependency-aware partial credit.** Report unique upstream defects, descendant consequences, and coincidental-correct outputs separately; do not sum dependent checks as independent failures.
4. **Add legitimate alternate derivations to criterion health.** Use reviewed contrast solutions and mutation cases to estimate false rejection and criterion path dependence.
5. **Fail closed on observer truncation.** Record exact judge-visible spans and hashes; return `insufficient_evidence` when required passages or operations are omitted.
6. **Keep expert review, but measure it.** Preserve item-level authority, independent derivations, disagreements, edits, reviewer concentration, alternative paths, time, and release disposition.
7. **Treat source packs as versioned task state.** Freeze public passages where licensing permits, or declare live retrieval windows, authority policies, content hashes, drift checks, and revalidation triggers.
8. **Use question-clustered inference.** Average repeated trials within question and bootstrap/hierarchically model questions; retain rollout variance and judge variance separately.
9. **Keep score claims bounded.** Criterion credit, coherent derivation, final answer, professional acceptance, and deployment readiness are distinct claims and thresholds.
10. **Use existing contracts.** Expertise-transfer, benchmark-bundle, artifact/evidence admissibility, task-health, metric, validity, trace/root-cause, and source-provenance machinery already cover these requirements. No finance-specific build task is needed.

## Concrete repository actions

No new queue task is added. The review supplies evidence for the existing criterion-dependence, source-provenance, observer-admissibility, trace, task-health, metric, and validity contracts. The most useful next implementation is not another schema: apply the proof-carrying derivation chain and one legitimate alternate-path contrast to a future pilot, then test whether a grader distinguishes unsupported narration, source-backed extraction, executable transformation, and coincidental correctness.

## Assessment

**Evidence tier:** Tier A for inspectable public-subset task/rubric/trace/grader methodology; Tier B for full-benchmark results because 878 items and headline outputs are held back.  
**Most reusable contribution:** criterion-level decomposition of source-to-definition-to-calculation-to-conclusion work with repeated visible trajectories.  
**Most serious flaw:** a criterion can receive “workflow” credit from narrated exact values without proof of source provenance, entailment, transformation, or dependency validity.  
**Claim skill-bench may safely make:** derivation-level rubrics add useful resolution beyond final-answer accuracy only when each checkpoint's source, operation, dependencies, grader evidence view, alternative paths, and claim ceiling remain explicit; otherwise the score measures agreement with a narrated reference decomposition rather than audited professional workflow.
