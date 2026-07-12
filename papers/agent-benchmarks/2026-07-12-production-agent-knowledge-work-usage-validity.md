# Production agent telemetry measures product-conditioned attempts, not completed professional work

**Source type:** Deep review of the complete immutable arXiv v2 primary source  
**Paper:** Jeremy Yang, Kate Zyskowski, Noah Yonack, and Jerry Ma, *How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope* (arXiv:2606.07489v2, 11 June 2026)  
**Immutable source:** https://arxiv.org/abs/2606.07489v2  
**Local PDF:** `data/papers/pdfs/2606.07489v2-how-agents-reshape-knowledge-work.pdf` (SHA-256 `de9641564e7a464c878d7ac4fcc447affd877b79cf8c4a834023d48c75148b04`, 55 pages)  
**Local text:** `data/papers/text/2606.07489v2-how-agents-reshape-knowledge-work.txt` (SHA-256 `99662cd82975043149a9162381f3014aaf185c09fb48e2f3f610f972d3c1d345`)

> **Evidence boundary.** This review covers the full 55-page paper, including appendices. The study analyzes proprietary Perplexity telemetry; no query-level data, matching code, classifier prompts, labels, tool-time audit, output artifacts, or outcome data are released. Two authors are Perplexity employees. Aggregate paper results are therefore author-reported production observations and model-derived estimates, not independently reproduced measurements. The arXiv metadata contains no withdrawal notice.

## Review judgment

This paper is unusually relevant to `skill-bench` because it observes what early users choose to delegate to a general agent rather than asking experts or benchmark authors what work matters. Its strongest finding is descriptive and product-specific: among selected dual-product users, execution-tool-gated Computer queries are longer-running and are classified as more artifact-producing, compositional, cross-domain work than Search queries. Follow-ups shift modestly from drill-downs toward extension, revision, and verification. Those patterns support representing task bundles, handoffs, review, and downstream extension—not merely isolated final answers.

The headline productivity and quality claims outrun the design. The 269-minute Search+Human counterfactual is not observed: it is constructed by multiplying Computer's selected tool calls by fixed analyst-assigned minutes, while Computer receives a fixed ten-minute oversight charge. “Completion” is assumed rather than verified. “Quality” is inferred from the next user turn only in surviving multi-turn sessions, not from artifact inspection, professional acceptance, downstream use, or harms. The matched sample conditions on Computer invoking an execution tool and on the same user submitting a near-duplicate to both products; product choice, order, intent, failure, and output are not randomized. Scope comparisons use different query mapping procedures across products and extensive unreleased LLM coding. The evidence cannot establish causal productivity, completed-task quality, worker benefit, occupational representativeness, or professional readiness.

## One-sentence contribution

The study offers valuable demand-side evidence that a production agent interface is associated with more compositional, artifact-oriented task attempts and review/extension handoffs, but its telemetry and modeled counterfactuals do not show that those attempts produced correct, valuable, or professionally usable completed work.

## Research question and contribution

The paper asks how moving from a conversational answer engine (Perplexity Search) to an autonomous orchestration product (Perplexity Computer) changes autonomy, estimated efficiency, and attempted work scope (pp. 2–5). It contributes:

1. a stylized task-selection model in which agents have higher fixed delegation/review cost but lower marginal execution cost per step (pp. 7–10, 42–47);
2. adoption and use-case summaries over the first three post-launch months;
3. 10,000 within-user session pairs whose initial queries have embedding cosine similarity above .99;
4. runtime, pause, stop, connector, follow-up, and next-turn dissatisfaction comparisons;
5. tool-based and LLM-based estimates of a Search+Human counterfactual, plus 25 user interviews;
6. within-user comparisons of inferred occupational crossing, cognitive level, knowledge breadth, and O*NET activity composition.

The paper's unique value is not a validated productivity estimate. It is an observational map of **which work users route to an agent-shaped product and what interaction follows delivery**.

## Methodology and system

### Products are compound treatments

Search retrieves and synthesizes cited answers. Computer searches, browses, codes, creates files, calls external services, delegates to subagents, and runs asynchronously (pp. 2–3). The comparison therefore changes autonomy, tool access, context integration, latency, interface expectations, price/subscription access, underlying orchestration, and likely model/scaffold configuration together. No versions, model identities, prompts, tool inventories over time, release changes, outages, pricing, or user-visible product defaults are frozen. “Agent access” is not an isolated treatment.

The conceptual model assumes task value weakly rises with step count, partial completion has zero value, agents have higher fixed cost, and lower marginal per-step cost (pp. 7–10). These assumptions organize intuition, but value and completion are unobserved. Query characters proxy fixed delegation cost; Computer tool-call count proxies task steps; analyst-assigned tool times create much of the marginal-cost result (pp. 24–26). Thus the empirical measures do not independently test the model's central value and completion primitives.

### Eight samples and different inference populations

The three-month window is 27 February–27 May 2026 (pp. 11–12). The analyses do not share one representative population:

- adoption uses the full query universe plus 100,000 randomly sampled Computer queries;
- complementarity starts with 100,000 adopters, retains 61,913 with pre-adoption Search, and exact-matches 61,786 non-adopters on tier, primary topic, and coarse Search-intensity quartile;
- autonomy/efficiency samples 100,000 dual-product users, requires Computer to invoke a “do” tool, greedily matches within user, retains similarity >.99, then samples 10,000 pairs; multiple pairs per user are allowed;
- follow-up analysis further conditions on both matched sessions having at least two turns (1,000 pairs; 15,507 follow-ups);
- horizontal scope samples exactly 1,000 dual-product users from each of eight inferred clusters and all their queries;
- vertical scope samples one do-gated Computer and one Search initial query from each of 5,000 dual-product users;
- interviews recruit 25 active users with at least five historical queries (six enterprise, nineteen consumer).

These are useful purposive samples, not the population of workers, occupations, Computer users, or knowledge-work tasks.

### Near-identical queries are not a natural experiment

The matched-pair design embeds all qualifying Computer initial queries and up to the 100 most recent Search initial queries per sampled user, greedily chooses one-to-one nearest neighbors, and retains cosine similarity >.99 (pp. 12, 15). It controls initial text and user more tightly than an unmatched product comparison. It does not randomize:

- which product was chosen first or why the task was repeated;
- whether the first attempt failed, informed, or caused the second;
- time, model/product version, available files, connectors, or external state;
- urgency, expected output, willingness to wait, and desired execution;
- post-query interaction, output artifact, or success criterion.

Conditioning the Computer side on observed “do” use selects sessions where the system executed. There is no analogous eligibility gate for Search and no attrition table from candidates to matched pairs. Similar text does not imply equivalent context, treatment propensity, or intended deliverable. Calling the pairs “natural experiments” is unjustified without an as-if-random assignment mechanism.

### Autonomy and follow-ups

Computer runtime is wall clock from user submission to last model response, summed over turns and capped at three hours; Search uses server latency (pp. 15–18). Mean session execution is 26 minutes versus 33 seconds; medians are nine minutes versus fourteen seconds. Parallel work makes wall time an underestimate of machine work, while retries and waits may inflate it. Runtime is a system-behavior measure—not useful work, autonomy quality, or human time saved.

Computer has more turns (5.3 versus 2.8), more pauses (38% versus .8% of sessions), and more connector use. User stop rates are similar (3.7% versus 3.4%), but a stop event is not a clean abandonment measure: asynchronous users can leave, ignore, accept, or continue elsewhere without issuing stop.

An unreleased LLM assigns 15,507 follow-ups to ten categories. Aggregate task advancement is effectively identical (52.7% Computer, 52.9% Search); reported shifts are small: extension +1.7 percentage points, drill-down −1.4, revision+verification +1.0, and short directives −1.7 (pp. 18–20). No prompt, model, human validation, agreement, uncertainty, or query/user clustering is reported. The direction is suggestive, but “higher-order work” is stronger than the taxonomy establishes.

### Dissatisfaction is not execution quality

An unspecified model scores dissatisfaction from the next user turn as zero/low/mid/high. Among multi-turn responses, medium+high is 1.3% for Computer and 2.9% for Search; any dissatisfaction is 10.8% versus 16.6% (pp. 19–20). This measure excludes terminal turns by construction and cannot distinguish satisfaction from silent abandonment, unnoticed error, acceptance, task completion, or continuation outside Perplexity. Computer and Search also induce different response times and artifacts, changing whether and how dissatisfaction is expressed. No artifact, external state, consequence, or professional reviewer is observed. The result supports a narrow claim about model-coded next-turn behavior among multi-turn sessions—not “execution quality” or output quality.

### Efficiency is a constructed counterfactual

For Search+Human, “search” tools receive zero manual minutes and Computer's “do” calls receive fixed per-call estimates: for example write=15, edit=10, bash=5, browser click=.5, browser task=10 minutes (pp. 21–22). Repeated calls are summed. Computer+Human receives ten minutes of oversight plus observed Computer runtime and model cost. Domain-level BLS mean wages price human time (pp. 22–25).

This construction reports 269 versus 36 minutes and 94% lower cost. But it assumes:

- the human would reproduce Computer's path and number of calls;
- every call is necessary, sequential, nonduplicative, and successful;
- fixed minutes do not depend on task complexity, call content, expertise, setup, or batching;
- Search's answer already performs all research and final composition at zero human time;
- Computer oversight is exactly ten minutes regardless of stakes, errors, artifact complexity, or downstream verification;
- both workflows achieve the same completed output and quality.

The independent LLM estimate sees query text only and is another model judgment, not measured labor. Interviews are selected retrospective self-reports and report dramatic 5×–300× gains; they cannot validate the same estimand. Sensitivity sweeps stress the assigned constants but not path equivalence, noncompletion, quality adjustment, output correction, parallel human work, selection, or omitted downstream labor. The study estimates **modeled equivalent execution effort conditional on Computer's observed tool path**, not actual completion time or productivity.

### Scope coding is extensive but asymmetrical

Horizontal scope infers a user's occupation from the modal topic of Search queries, maps Search sessions deterministically through topic domains, and maps Computer queries by an LLM into eight clusters plus Other (pp. 27–30). Search both defines the user's occupation and supplies the baseline, creating a mechanical home-cluster advantage for Search. Query interests need not equal employment, role, competence, or task authority. Physical occupations are excluded, and the balanced 1,000-per-cluster sample is not prevalence-weighted. The reported 59% versus 50% cross-cluster share is descriptive of this circular proxy.

Vertical scope uses unreleased LLM classification for Bloom level, routine/abstract, minimal O*NET knowledge domains, and hierarchical GWA/IWA/DWA/task-statement mappings (pp. 30–37). Computer queries are do-gated; Search queries are not execution-eligible matched tasks. Artifact requests naturally attract Create labels and more task statements, so the comparison partly measures interface-conditioned query formulation and taxonomy verbosity. The paper reports no annotator validation, agreement, classifier version, prompt, abstention rate, confusion analysis, multiplicity adjustment, paired uncertainty, or sensitivity to alternative mappings.

“New tasks unlocked” means an O*NET label occurs in sampled Computer queries and zero or at most k times in sampled Search queries (pp. 31, 34–37). It is sample novelty, not a task that was infeasible before agent access. Rare labels, classifier noise, unequal product usage, and do-gating all increase apparent novelty. At k=0, the strongest result—23% of classifiable Computer queries touching a Computer-only task statement—falls to 5% at detailed-work-activity level and nearly zero at coarser levels. This supports fine-grained label-set differences, not economic frontier expansion.

## Evidence and results: what survives

The following are supported as bounded author-reported descriptions of selected production telemetry:

1. Computer sessions in the execution-gated matched sample run far longer and invoke more action/connectors than Search.
2. The two products produce different interaction shapes: Computer has more turns and pauses, while model-coded follow-ups modestly shift toward extension/review.
3. Users route different requests to the products: do-gated Computer queries are more often classified as artifact creation, abstract/Create work, multi-domain, and multi-activity.
4. Users repeat near-identical initial requests across both products often enough to form 10,000 selected pairs, a promising basis for future randomized or order-aware studies.
5. Product telemetry can reveal demand, delegation, and handoff patterns that benchmark author intuition alone will miss.

The data as presented do not establish that Computer completes tasks, produces higher-quality outputs, saves 87% of actual time or 94% of actual cost, expands users' real competence, lowers coordination costs, or creates greater realized value.

## Unique insight

> **Production usage is evidence about attempted delegation and workflow shape; benchmark validity requires a separate chain from attempt to accepted consequence.**

For each telemetry-derived candidate task family, `skill-bench` should preserve distinct records for:

1. **attempt:** initial request, product eligibility, user/task sampling frame, and selection mechanism;
2. **execution:** configured system, actions, machine/human active and elapsed time, pauses, retries, failures, and cost;
3. **delivery:** artifacts and external state actually returned;
4. **inspection:** what evidence the user, grader, or expert saw, with correction and dissatisfaction signals;
5. **acceptance:** explicit acceptance, abandonment, rework, or unresolved status;
6. **downstream use:** whether the artifact was used, extended, handed off, or caused a state change;
7. **consequence:** quality, safety, value, and loss under an appropriate criterion;
8. **counterfactual:** observed or modeled comparator, assumptions, uncertainty, and population.

The paper observes pieces of attempt, execution, and next-turn interaction. It largely imputes the counterfactual and does not observe delivery quality, acceptance, downstream use, or consequence. A benchmark should not collapse those stages into “completion” or “productivity.”

## Limitations and validity threats

1. **Compound product treatment:** autonomy, tools, context, interface, model/scaffold, latency, access, and expectations vary jointly.
2. **Endogenous routing and repetition:** users choose the product and may repeat because of prior success/failure; order is unreported.
3. **Post-treatment selection:** Computer matches require observed execution-tool use.
4. **Restricted matched support:** only near-duplicate dual-product sessions enter autonomy/efficiency; no overlap diagnostics or candidate attrition are reported.
5. **No completion outcome:** session presence, runtime, or a final response does not prove task completion.
6. **No artifact-quality measure:** next-turn dissatisfaction cannot validate correctness, professional convention, downstream usability, or harm.
7. **Survivor/observation bias:** dissatisfaction requires another turn; silent acceptance, abandonment, and unnoticed errors are indistinguishable.
8. **Constructed time and cost:** fixed per-tool minutes and fixed oversight dominate estimates; path and outcome equivalence are assumed.
9. **Non-independent triangulation:** tool estimates use Computer traces, LLM estimates use the same queries, and interviews select active users; agreement does not remove shared selection or desirability bias.
10. **Circular occupation proxy:** Search topics define occupation and are then compared against Search/Computer crossing.
11. **Asymmetric classifiers:** Search and Computer occupation destinations use different mappings.
12. **Unvalidated model coding:** taxonomy prompts, models, labels, agreement, and error rates are unreleased across use case, follow-up, dissatisfaction, occupation, cognition, expertise, and activity measures.
13. **Taxonomy-to-construct leap:** Bloom/Create and O*NET label counts do not directly measure difficulty, expertise, quality, or coordination burden.
14. **Sample novelty called unlocking:** zero Search occurrences can reflect rarity, finite sampling, coding error, or product framing.
15. **Dependence and uncertainty gaps:** multiple pairs per user and many labels per query require clustered/multilevel uncertainty; most headline comparisons report no intervals.
16. **Early-adopter boundary:** three months of paying/power-user behavior cannot represent workers or stable mature usage.
17. **Ecosystem blind spot:** activity, rework, collaboration, and outcomes outside Perplexity are unobserved.
18. **Proprietary non-reproducibility:** raw queries, outputs, traces, code, prompts, mappings, and sampled IDs are unavailable.
19. **Theory-evidence mismatch:** task value, completion, budget, and surplus are unobserved; stronger welfare propositions are not tested.
20. **Conflict and reporting incentives:** vendor-employed coauthors and product framing increase the importance of release, preregistration, external audit, and conservative claims, none of which are provided.

## Reproducibility and operational realism

**Primary-source inspectability: moderate.** The paper clearly enumerates samples, basic matching, fixed tool-time mappings, wage mappings, taxonomies, aggregate results, sensitivity sweeps, and limitations. Full appendices make the claimed method more inspectable than a product post.

**Computational reproducibility: very low.** No data, code, prompts, classifier outputs, product snapshots, model identities, matching diagnostics, artifacts, or result tables are released. Privacy constraints are legitimate, but reproducibility could still be improved with synthetic examples, prompt/version cards, aggregate attrition tables, blinded human audits, privacy-preserving label distributions, and externally executable estimators.

**Operational realism: high for routing, low for outcomes.** Real users, live products, connectors, asynchronous runs, follow-ups, and early deployment failures/pauses provide authentic workflow substrate. Yet the study does not observe whether artifacts entered a professional process, passed stakeholder review, required repair, caused harm, or delivered economic value. Production telemetry is not automatically production validity.

## Transfer to skill-bench

### Retain

- Use production demand evidence to sample candidate task families, artifact formats, and handoff patterns.
- Treat composite requests and cross-domain evidence integration as real usage phenomena worth testing.
- Represent delegation overhead, clarifications/approvals, review, verification, extension, and recurrent scheduling as first-class workflow states.
- Separate active human time, elapsed time, machine time, model/provider cost, external-service cost, and review/rework burden.
- Compare configured systems and product modes, not model names alone.
- Preserve query/session/task distinctions; one session is only a noisy task proxy.

### Repair

1. Attach a **demand-provenance record** to task families: telemetry source, dates, population, product eligibility, sampling, coding method, prevalence denominator, uncertainty, and generalization boundary.
2. Require task instances to specify delivery, acceptance, downstream-use, and consequence states separately from execution termination.
3. Record handoff edges (`delivery→review→repair→verification→extension`) and whether each is required, optional, observed, or inferred.
4. For time/cost comparisons, distinguish observed time from model-assigned equivalent time; require comparator path, equal-outcome basis, parallelism, rework, invalid runs, and uncertainty.
5. Construct matched benchmark variants that hold task/source/artifact/rubric fixed while changing only the agent/scaffold or guidance treatment; do not emulate the paper's compound Search-versus-Computer contrast as a causal ablation.
6. Calibrate task-composition labels against expert decomposition and observed artifacts. Keep Bloom/O*NET labels as descriptive metadata, not difficulty or validity scores.
7. Include lower-frequency, short conversational tasks as controls so the portfolio can test routing thresholds rather than selecting only action-tool-positive work.
8. Track user/professional authority: attempting legal, medical, financial, or cross-occupation work does not license the resulting artifact or prove expertise transfer.
9. Add explicit terminal states for silent abandonment, no follow-up, unnoticed error, user stop, provider failure, partial delivery, and accepted completion.
10. Bound benchmark claims to the tested setting and configured system. Demand prevalence can motivate coverage but cannot establish professional representativeness or readiness.

## Action items

No new queue task is warranted. The nonduplicate implications fit existing machinery:

- benchmark-bundle trial/artifact/trace records can distinguish attempt, execution, delivery, and terminal state;
- task-health and validity-argument contracts can prevent usage prevalence or dissatisfaction from licensing capability/readiness claims;
- metric-monitoring can type populations, denominators, missing terminal turns, clustered uncertainty, and modeled versus observed estimands;
- configured-system and execution-validity records can preserve the compound treatment;
- cost-aware usefulness should add downstream review/rework and equal-outcome assumptions when next revised;
- future pilot design should use the paper's observed review/extension pattern to test a bounded delivery→review→repair→verification handoff, without treating Perplexity telemetry as expert validation.

## Relevance to the charter

This review advances charter objectives A, B, D, and E through narrow expansion into production knowledge-work evidence. It does not narrow `skill-bench` to Perplexity, one occupation, or an agent product. Its reusable result is an inference boundary: production logs can inform **what people attempt and how workflows unfold**, while benchmark claims about capability, quality, productivity, and consequence require separate evidence.

## Claim boundary

The immutable v2 paper supports descriptive claims about selected Perplexity usage during its first three months and reports model-coded differences between Search and Computer samples. It reports large modeled time/cost reductions and lower model-coded next-turn dissatisfaction. Without randomized assignment, observed completion/quality, equal-outcome counterfactuals, released coding evidence, external workflow outcomes, or representative sampling, it does not establish causal productivity, artifact quality, user welfare, occupational scope expansion, genuine expertise transfer, professional validity, safety, economic value, or deployment readiness.
