# Paper Review: Synthetic Organizational Search Recovers Planted Descriptions, Not Tacit Expertise

- **Paper:** Gianlucca Zuin, Saulo Mastelini, Túlio Loures, and Adriano Veloso, *Leveraging Large Language Models for Tacit Knowledge Discovery in Organizational Contexts*, https://arxiv.org/abs/2507.03811v1
- **Date read:** 2026-07-17
- **Venue / source:** immutable 8-page arXiv v1 / IEEE-formatted manuscript
- **Tags:** expertise-elicitation, organizational-networks, multi-agent-simulation, planted-knowledge, question-policy, self-critique, release-audit
- **Local PDF:** `data/papers/pdfs/2507.03811v1-tacit-knowledge-discovery-organizational-contexts.pdf` (8 pages; SHA-256 `2e76af7209d793a3539836f624f4be675f8a1b9e4ec54ebab8e6b10f93431bcd`)
- **Local text:** `data/papers/text/2507.03811v1-tacit-knowledge-discovery-organizational-contexts.txt` (SHA-256 `079c6bef71f9ecc1d4ea61c22ed10d7e71d4971951ee952ff103f937bd2199fc`)
- **Official release inspected:** Figshare item 28785524 v1, DOI https://doi.org/10.6084/m9.figshare.28785524.v1; 17 files and supplied MD5s preserved in `data/sources/releases/2507.03811v1-tacit-knowledge-discovery/provenance.json`. The 51,847,034-byte archive `files/53777156-conversation_logs.zip` contains 864 complete run triplets (`artifacts.bin`, `descriptions.json`, `simulation.log`).

## Verdict

The paper contributes an unusually inspectable synthetic testbed for an important subproblem: an LLM interviewer begins with a table name and column names, searches through LLM-simulated employees holding fragments of an author-generated description, and decides whom to question and when to stop. Its 864-run factorial release is useful for studying **routing and recovery under planted information fragmentation**.

It does not test tacit knowledge, human expertise, real organizational transport, or expert participation. The “knowledge” consists of GPT-4o-mini-generated database documentation atoms copied into GPT-4o-mini employee backstories; the same model family asks questions, responds as employees, summarizes, routes, and self-scores. Full-column recall only checks whether every planted column name appears, not whether meanings, relations, uncertainty, or professional consequences are correct. The strongest headline—94.9% full-knowledge recall—therefore licenses a narrow synthetic string-coverage claim.

Release inspection further changes the interpretation. The published implementation starts with a random employee, not explicitly at the bottom of the hierarchy; its added informal graph edges influence dissemination but are omitted from the employee referral dictionary; multiple random choices escape the saved seed; and no released metric/analysis code reproduces METEOR, G-Eval, correlations, tests, or UMAP. A direct archive replay found 824/864 final reports containing all planted column names under an exact boundary-aware match, not the paper's 820/864, leaving the headline denominator unresolved.

For `skill-bench`, retain the networked-search decomposition and complete event logs. Reject the upgrade from planted-atom recovery to elicitation validity. The reusable benchmark unit is a **claim-routing episode** linking source authority, holder access, referral visibility, question exposure, adoption, and final claim evidence—not a scalar self-critic score or a final prose description.

## One-sentence contribution

The paper and release provide a 288-cell × three-repetition GPT-4o-mini simulation of question-guided recovery from fragmented generated table descriptions, but establish synthetic planted-information routing and identifier coverage rather than tacit expertise, organizational validity, or calibrated elicitation.

## Why this matters for skill-bench

This is targeted expansion under charter objectives A, B, and F. The general hypothesis is not that organizations should become the benchmark's domain. It is that consequential knowledge can be fragmented across people and channels, so benchmark authoring may need to evaluate whether an elicitor finds the right source, asks a discriminating question, preserves scope and authority, reconciles partial statements, and knows when evidence is sufficient.

The paper is distinct from existing evidence:

- **Data Therapist** studies six real experts but confounds expert identity with elicitation interface and does not validate downstream truth. This paper removes human variation by planting a complete synthetic reference, gaining recoverability measurement while losing expert validity.
- **SimInstruct** shows that simulated-interlocutor traits alter expert output. Here both interlocutor and elicitor are simulated, making model realization and shared priors even larger parts of the treatment.
- **Laboratory workflow twins** preserve role-gated claims and conditional workflow structure from four reported real sessions but lack claim-level public evidence. This paper provides complete traces and planted authority but no real claims or contributors.
- **Industrial expertise codification** reports a selected package effect from two real experts and five co-designed artifacts. This paper tests search over fragmentation but never projects recovered text into tasks, procedures, artifacts, or consequences.
- The pending **consented micro-pilot** remains the relevant validation boundary. A synthetic simulator cannot unblock `build-elicitation-session-contract`, establish consent feasibility, or substitute for a qualified contributor's read-back and downstream fidelity review.

Useful completion is this release-grounded claim ceiling and a set of reusable validation implications. No source-specific schema or organizational pilot is warranted.

## Contribution and research question

The manuscript asks whether an LLM agent can navigate a synthetic company and reconstruct documentation for an unknown database table from partial employee knowledge (Abstract; Sections I and III, pp. 1–4). It contributes:

1. a prompt-chained interviewer with separate question, summary, self-critique, routing, and greeting roles;
2. a synthetic company with a directed hierarchy plus an undirected relationship graph;
3. column-level information diffusion using an SI-inspired process with decreasing transmission probability;
4. a factorial study across hierarchy depth, employee count, transmission parameters, informal-edge count, and table width;
5. 864 released run bundles with generated reference state, graphs, final descriptions, and detailed logs; and
6. reference-free self-scores compared with lexical and model-based reference scores.

The evidence supports bounded statements that GPT-4o-mini often reconstructed all planted column names, contacted multiple simulated employees, and sometimes did so without talking to the original source node. It does not establish discovery of tacit cognition, factual table truth, professional usefulness, human-like organizational behavior, optimal search, calibrated stopping, cost scalability, or transfer to real employee interviews.

## Methodology and system

### Unit of knowledge and authority

For each run, GPT-4o-mini generates one hypothetical table in one of 18 sector topics with either 5 or 20 columns. Each column receives a name, meaning, type, examples, and claimed relations; 80% are prompted as useful for machine learning and 20% as ingestion/timestamp fields (`utils.py`, lines 27–37; `llm_role.py`, lines 133–158). This generated table description is the run's `full_knowledge` reference.

Each column is then treated as one independent “disease” or fact (`company_maker.py`, lines 35–125). With one patient zero, the initial source possesses every column atom. Transmission occurs on the undirected relationship graph for ten steps with probability `alpha * decay**step`; the released experiment fixes `forgetting_chance=0`, despite the paper's discussion of loss/waning infectivity (`edd.py`, lines 72–107). Thus employees retain transmitted columns permanently; only future transmissibility wanes. Calling this “knowledge loss” in Section III-B (p. 4) is inaccurate for the released 864-run design.

Authority is entirely author-planted. An employee is “knowledgeable” because its generated system backstory contains a column description. There is no distinction among firsthand experience, hearsay, formal role authority, source evidence, confidence, valid time, contradiction, or permission to disclose. The patient-zero label identifies the simulation source, not a validated domain specialist.

### Formal and informal networks

The hierarchy generator creates an approximately balanced tree with parent–child and sibling relationships. It then adds `n_employees * connections` random undirected edges to the NetworkX relationship graph (`company_maker.py`, lines 144–229). Knowledge spreads over that complete graph.

However, the random informal edges are not added to `relationships_dict`, which is the structure used to tell employee agents whom they know and to generate referrals (`simulation.py`, lines 118–148). An audit of all 864 pickles found a mean of 222.8 graph edges per run absent from the referral dictionary (range 0–971; zero exactly in the 288 `connections=0` runs). Informal connectivity therefore changes who receives knowledge and graph-distance statistics, but not the explicit informal contacts through which simulated employees can route the interviewer. This weakens the paper's interpretation of informal networks as both dissemination and discoverable navigation channels.

The manuscript says the hierarchy is explicitly known to the interviewer and the informal network is inferred (Section III-B, p. 4). The implementation instead gives the routing model all employee names, while each employee backstory exposes only local `relationships_dict` contacts and occasional table-level hints. There is no global hierarchy object, role map, or explicit graph supplied to the questioner.

### Interviewer, employee, and stopping policy

All roles call `gpt-4o-mini` at temperature 0.7 (`llm_agent.py`, lines 5–27). The loop is:

1. generate a greeting;
2. ask an open-ended question from the current description, recent local transcript, and self-critique;
3. have a simulated employee answer from an LLM-expanded backstory;
4. rebuild the entire table description from only the last three local interaction records;
5. self-score completeness from 0–10;
6. ask another model role whether to continue, switch, or end; and
7. stop at score 9, exhausted candidate users, an `end` action, or the maximum loop depth.

Employee backstories contain exact planted descriptions for their columns, local contacts, probabilistic hints about which neighbor knows the table, a generated job role/personality, and repeated instructions not to invent. After more than five interactions, the employee is explicitly instructed not to answer and to refer elsewhere (`orquestration.py`, lines 113–142). This is a strong routing scaffold, not emergent organizational behavior.

The paper says the agent begins with a random employee from the bottom of the hierarchy (Section IV, p. 5). The release calls `rng.choice(all_users)` (`simulation.py`, lines 151–162). Across the 857 runs where the first greeting was machine-parseable, only 311 (36.3%) began at the maximum observed hierarchy depth. This is a direct paper–implementation mismatch.

The intended saved seed also does not fully identify the treatment:

- `company_maker.py` uses global `random.sample` for added informal edges rather than the seeded `rng`;
- `simulation.py` uses global `random.random` for neighbor-knowledge hints;
- `edd.py` uses global `random.choice` for sector topic generation;
- names and table descriptions are stochastic API outputs; and
- `_extract_table_description` calls `start_conversation(table_name, table_columns, seed)` positionally, passing the seed as `chat_history_limit` while the actual `seed` parameter remains `None` (`simulation.py`, lines 8–33; `orquestration.py`, lines 54–63).

The saved integer therefore helps identify some graph construction but cannot replay the start employee, informal graph, referral hints, generated content, or model outputs.

### Factorial design and run completeness

The released runner defines:

- maximum hierarchy depth: 2, 5, 10, 20;
- employees: 20, 75, 200;
- `alpha`: 0.1, 0.5;
- `decay`: 0.5, 0.8;
- informal connection multiplier: 0, 2.5, 5;
- table columns: 5, 20; and
- three repetitions.

This yields 288 cells and 864 runs. Independent archive inspection confirmed exactly three runs in every cell, 864 valid description JSON files, 864 logs, 864 pickles, and no missing run triplets. The logs contain 29,400 employee answers and 29,400 interviewer questions (mean 34.0 each per run; range 1–156) plus 307,023 INFO/DEBUG event records. That grounds the paper's “over 300,000 interactions” only if internal logging/model-role events—not employee conversations alone—are counted.

No baseline interviewer, random-routing policy, no-self-critic arm, oracle routing policy, different model family, human interviewer, or real employee condition is included. Parameter variation describes one configured package; it does not identify which model role or prompt causes recovery.

## Measures and evidence

### Full-knowledge recall

A run is reported as full recall if its final report mentions every original column, regardless of whether meaning, type, example, relation, or uncertainty is preserved (Section V, p. 6). The paper reports 820/864 = 94.9%; the remaining 44 reports mention about 77% of columns.

A direct boundary-aware, case-sensitive exact-name replay against released `full_knowledge` and final JSON found 824/864 = 95.37%, with mean recall 0.780 among the 40 failures. The release contains no metric code, so differences in normalization, parsing, or report/reference inventory cannot be resolved. This audit does not supersede the authors' metric; it establishes that the headline is not exactly reproducible from disclosed code and artifacts.

More importantly, full-column recall is an extremely weak success criterion. The interviewer receives all column names at task start. Mentioning each name can occur with unknown descriptions, guesses, copied fragments, or incorrect relations. It measures retained identifier coverage, not knowledge recovery fidelity.

### METEOR and G-Eval

The paper averages METEOR over column descriptions and reports 0.174. It also applies G-Eval per column for “coherence” and “faithfulness,” reporting means 2.653 and 4.368 on a 1–5 scale (Section V, pp. 6–7). The exact segmentation rules, prompts, model snapshot, decoding, invalid-output handling, number of judge calls, retries, and analysis code are absent from the release. No human annotation validates either dimension.

The high faithfulness / low coherence / very low lexical overlap combination is plausible for paraphrased generated descriptions, but it does not prove semantic equivalence. Both the reference and candidate are generated by the same model family, and likely model priors can fill or recognize sector-generic content. The judge may reward plausible shared semantics even when no employee transmitted them.

### Self-critic

The interviewer self-scores after every turn without seeing the reference. A post-hoc contextual variant sees the original reference. The paper reports final self-score 7.432 and contextual self-score 6.747. Spearman correlations are:

- self-score versus contextual self-score: 0.729;
- self-score versus G-Eval faithfulness: 0.498;
- contextual self-score versus G-Eval faithfulness: 0.665;
- self-score versus METEOR: 0.264; and
- self-score versus G-Eval coherence: 0.347 (Table II, p. 7).

The abstract's “strongly correlating with external literature critic scores” overstates the direct result. The strongest external association is obtained after giving the self-critic the reference; the deployed reference-free score has only moderate correlation with faithfulness and weak correlation with lexical/coherence measures. Shared model family, prompt style, and candidate text also violate evaluator independence. Correlation is not calibration: no threshold-specific precision/recall, stopping regret, premature-stop audit, reliability, or held-out model validation is reported.

Archive logs exactly reproduce the reported final self-score mean of 7.4317. Only 384 runs ended at score 9; the remainder ended from route exhaustion or another stop boundary, including scores 3–8. Thus score 9 is not the universal endpoint, and the observed stopping policy is a mixture of confidence, candidate exhaustion, loop limits, and model `end` decisions.

### Patient-zero independence

The paper averages `% p0` near 0.30 in Table I and reports a −0.06 correlation between patient-zero contact and G-Eval faithfulness; a UMAP visualization is used to argue high-quality recovery need not reach the source (pp. 7–8). Parsing the original-source name from 844 logs with simple quoted-name formatting and checking employee-response records found 245 contacts (29.0%), consistent with the table.

This supports a narrow structural claim: final descriptions can contain all planted identifiers even without a direct dialogue with the initial source because exact atoms were deliberately diffused to other nodes. It does not show that intermediaries preserve provenance, that independent fragments jointly entail the reference, or that a real organization can reconstruct expertise without specialist review. The treatment constructs redundancy before evaluation.

UMAP is descriptive and unnecessary for the main claim. The projection pools factorial configuration summaries, has no disclosed seed/hyperparameters or uncertainty, and cannot identify causal independence from patient-zero contact. Contact is endogenous to graph structure, diffusion, model routing, and stopping.

### Statistical analysis and negative evidence

The paper says pairwise t-tests at `p ≤ .05` were applied over three repetitions (Section IV, p. 5), but reports no test table, effect estimates, confidence intervals, exact contrasts, multiplicity correction, assumptions, or unit definition. Marginal averages in Table I pool many configurations and generated topics. Three stochastic API runs per cell cannot support strong reliability claims, especially when the saved seed is incomplete.

The paper has no explicit negative-case taxonomy. The 40/44 recall failures are summarized only by average identifier coverage; there is no audit of wrong meanings, hallucinated examples, contradictory relations, premature stopping, referral loops, employee leakage, or source attribution. Costs, token usage, wall time, rate-limit failures, retries, and invalid model outputs are not recorded, despite the release requiring tens or hundreds of calls per run.

## Unique insight

The deepest transferable insight is that **networked elicitation has at least six separable reachability stages**:

`authoritative claim exists → holder can access it → holder is reachable through a disclosed/referral channel → elicitor asks a claim-discriminating question → response is adopted without distortion → final artifact preserves evidence and scope`

This simulator directly observes only a subset. It plants access, constructs dissemination, logs routing/questions/responses, and checks final identifier presence. It does not establish claim authority, response truth, semantic preservation, professional scope, or downstream utility. A high final recall can coexist with failures at every stronger stage.

A second insight comes from the release defect: **information-flow topology and navigation topology are different interventions**. Adding hidden edges made facts spread farther but did not add those edges to employees' referral maps. Benchmark designs must separately version:

- who actually possesses a claim;
- who knows that another person possesses it;
- who is authorized and willing to disclose it;
- what the elicitor can observe about roles and channels; and
- which routing edges it exercises.

Collapsing these into “organizational connectivity” makes mechanism claims uninterpretable.

Third, **stopping is an evidence decision, not a prose-quality judgment**. The self-critic scores apparent documentation completeness from the same generated report it helped create. It neither tracks unresolved claims nor asks whether evidence has independent authority. A benchmark elicitor should stop only against a claim inventory with typed statuses—confirmed, contradicted, unobserved, inferred, out of scope, or escalated—and should be penalized separately for unnecessary burden and unsupported closure.

Finally, complete trace availability does not create ecological validity, but it creates falsifiability. The Figshare archive allowed direct discovery of start-policy, referral-graph, seed, endpoint, and recall discrepancies that the prose alone hides. This is precisely the evidence standard `skill-bench` should preserve for its own synthetic validation fixtures.

## Limitations and validity threats

1. **Construct substitution:** GPT-generated table documentation is explicit planted text, not tacit experience, cue recognition, embodied skill, or difficult-to-articulate judgment.
2. **No humans or experts:** every employee, elicitor role, reference, and evaluator is model-generated; there is no participant authority, consent, disagreement, or read-back.
3. **Same-family dependence:** GPT-4o-mini generates references, employee backgrounds, responses, questions, summaries, routing, and self-scores, inviting shared-prior recovery and stylistic agreement.
4. **Identifier leakage by design:** all target column names are visible at task start, making full-column recall a coverage/retention check rather than discovery.
5. **Generated reference fallibility:** no domain expert validates names, meanings, types, examples, relations, usefulness labels, or sector realism.
6. **Column atomization:** table-level purpose, interactions, conditional rules, exceptions, temporal change, contradictions, and workflow consequences are not independently disseminated units.
7. **No provenance in output:** final descriptions do not link statements to employees, utterances, authority, corroboration, uncertainty, or competing claims.
8. **Single-source authority:** one planted description is treated as truth; multiple valid perspectives, local applicability, disagreement, and supersession are absent.
9. **Informal-edge implementation gap:** random informal graph edges affect spread and distance but are absent from employee referral dictionaries.
10. **Hierarchy-observability mismatch:** the paper says the hierarchy is known, while the interviewer implementation lacks the explicit hierarchy/role graph.
11. **Start-policy mismatch:** the paper says bottom-of-hierarchy; release code samples any employee, and only 36.3% of parseable starts were at maximum depth.
12. **Incomplete seed control:** global random calls, stochastic API generation, and a positional-argument bug prevent exact replay from saved seeds.
13. **Stopping-policy mixture:** score threshold, candidate exhaustion, `end` decision, and maximum depth all terminate runs; results do not isolate self-critic stopping quality.
14. **Forced referral treatment:** after five employee interactions, the simulator instructs the employee to stop answering and name someone else.
15. **Employee leakage risk:** backstory generation is another model transformation that can omit, alter, or embellish planted facts; no transformation fidelity audit is reported.
16. **No model/harness variation:** one model family, one prompt package, temperature 0.7, and hosted mutable behavior bound configured-system generality.
17. **No mechanism ablation:** self-critique, referrals, hierarchy, hidden hints, memory window, and model roles are not independently ablated.
18. **Weak headline metric:** column-name presence ignores incorrect meaning, hallucination, relation loss, unsupported examples, and professional actionability.
19. **Unreproducible metric pipeline:** METEOR/G-Eval prompts, segmentation, judge model/settings, invalid handling, and analysis scripts are absent.
20. **Recall discrepancy:** exact-name release replay yields 824 successes while the paper reports 820; no released metric code resolves it.
21. **Judge dependence:** self-critic, contextual critic, and G-Eval are not independent evidence views and have no human calibration.
22. **Correlation overclaim:** reference-free self-score correlations with external measures are weak to moderate; correlation does not establish calibrated stopping.
23. **Underreported inference:** pairwise t-tests are asserted without contrasts, estimates, intervals, multiplicity control, or outputs.
24. **Three repetitions:** API nondeterminism and clustered factorial data make three runs per cell inadequate for strong reliability or small-effect claims.
25. **Marginal aggregation:** Table I averages across other parameters and generated topics, obscuring interactions and changing task content.
26. **Endogenous patient-zero contact:** graph structure, diffusion, referrals, routing, and stopping jointly determine contact, so association with quality is not a causal ablation.
27. **No failure analysis:** omission cases, hallucinations, loops, invalid outputs, premature stops, and unsupported final claims are not categorized.
28. **No cost evidence:** calls, tokens, dollars, latency, retries, coordination burden, and cost per confirmed claim are unavailable.
29. **No real organizational behavior:** simulated roles, personalities, incentives, trust, confidentiality, power, workload, refusal, and political risk are prompted stereotypes rather than validated behavior.
30. **Unsupported implementation claim:** preliminary Kunumi deployment is mentioned without protocol, participants, outcomes, comparison, consent, or evidence and cannot validate the simulation.
31. **No downstream utility:** recovered text is not used to build a task, detect an error, improve a decision, or support an independently graded artifact.
32. **Cross-domain surface diversity only:** 18 sector labels change generated vocabulary but do not vary the elicitation construct, professional authority, or workflow consequence.

## Reproducibility and operational realism

Release inspectability is high relative to the paper's size. The immutable PDF, prompt supplement, runnable-looking Python modules, requirements, 864 final JSON files, 864 detailed logs, and 864 pickled graph/reference states preserve the complete realized corpus. All 17 Figshare files matched supplied sizes and MD5s, and every run triplet was present. The archive permits structural and textual reanalysis without new model calls.

Exact experimental reproduction is still weak. Dependencies are unpinned beyond a generated environment list; OpenAI snapshots and request IDs are absent; API dates, retry/error policy, usage, and costs are absent; several random choices bypass the saved seed; the conversation seed is mis-bound positionally; and analysis code for every paper metric beyond logged self-scores is missing. The duplicate byte-identical `edd.py` files and a second `edd_bc.py` with different 100/250-employee and 100-column settings also require care: the 864 archive corresponds to the 20/75/200 × 5/20 design in `edd.py`, not the broader commented/alternate runner.

Operational realism is low for expertise elicitation and moderate for a synthetic search stress test. Positive features include fragmented access, local referrals, repeated contacts, finite conversation depth, partial answers, hidden network structure, complete traces, and reports assembled from multiple sources. Missing are actual experts, organizational permissions, scheduling, nonresponse, confidentiality, strategic withholding, contradictory testimony, source documents, incident evidence, changing facts, contribution burden, review, correction, consent, and downstream consequences. The simulator should be described as an **offline planted-information navigation environment**, not an organizational digital twin or evidence that autonomous interviewing scales.

## Transfer to skill-bench

### Retain

- A frozen claim inventory and per-holder access map for synthetic conformance tests.
- Separate formal hierarchy, informal relation, possession, referral-awareness, and observed-contact graphs.
- Complete event traces linking question, respondent, response, route decision, summary update, and stop reason.
- Factorial variation in fragmentation, network reachability, and source redundancy.
- Source-avoidance analysis: can independently held fragments support a conclusion without contacting one designated source?
- Negative cases where evidence is unreachable, contradictory, stale, unauthorized, or insufficient.

### Repair before reuse

1. **Type claim authority and evidence.** Each planted atom should record author/source, holder access basis, firsthand/hearsay status, confidence, scope, valid time, contradictions, and disclosure authority.
2. **Separate graph layers.** Version actual possession, referral belief, organizational relation, agent-observed topology, and exercised route independently; test that each configured edge affects only its declared layer.
3. **Use semantic claim checks.** Score proposition entailment, scope, contradiction, unsupported additions, and evidence locators—not only identifier mentions or same-family judge plausibility.
4. **Make stopping claim-based.** Require a declared required-claim set and final status for every claim. Report premature closure, unresolved critical claims, unsupported closure, excess contacts, and burden.
5. **Add matched policies.** Compare random, formal-only, referral-following, uncertainty-seeking, source-authority-aware, and oracle routing under the same generated organization.
6. **Break model dependence.** Generate references from frozen human-authored or independently reviewed packs; vary employee and elicitor models; use deterministic simulators for access/referral behavior where that is the construct.
7. **Plant adversarial but fair cases.** Include confident wrong intermediaries, two conditionally correct experts, stale versions, inaccessible source evidence, authority conflicts, and a high self-score despite one consequential missing claim.
8. **Preserve invalid and cost denominators.** Log every call, retry, malformed output, timeout, token/cost record, contact, question, and stop path.
9. **Validate transport with a real session only after consent.** Compare simulator-predicted routing/stopping failure signatures against one bounded, consented, non-sensitive expert incident; do not expose private organizational networks or infer real coworkers' knowledge without authorization.

### A bounded validation design

A reusable cross-domain conformance slice could freeze 12–20 claims from a synthetic source pack and distribute them across simulated contributors under four matched conditions:

- formal links only;
- hidden dissemination edges without referral awareness;
- referral-aware informal links; and
- one authority conflict plus one stale claim.

Run multiple routing policies with equal budgets. Measure separately: source reachability, discriminating-question rate, supported claim recall, unsupported claim rate, contradiction discovery, correct scope, provenance retention, premature stopping, contacts/calls/tokens, and final task/check utility. This would test the paper's genuine contribution—networked evidence acquisition—without claiming tacit expertise or organizational realism.

The existing benchmark bundle, evidence-chain, metric-monitoring, validity-argument, task-health, participation, and blocked elicitation-session machinery can represent these requirements. No new contract is justified.

## Concrete repository actions

1. **Index this review as release-audited expertise-elicitation evidence.** Its claim ceiling is synthetic planted-information routing and identifier recovery.
2. **Do not add a source-specific build task.** The implied records already have homes in existing contracts, and the consented micro-pilot remains the human-validity gate.
3. **Use the discovered graph-layer and stopping distinctions in the next expertise/evidence synthesis.** Specifically preserve possession, referral awareness, observed routing, semantic adoption, and authority as separate states.
4. **If a future synthetic elicitation fixture is built, require an exact replay test.** The runner must pin all random sources/model versions, expose metric code, reproduce reported denominators, and include failure cases before any mechanism claim.

## Bottom line

This is a valuable released simulator and an overclaimed tacit-knowledge study. It shows that one GPT-4o-mini prompt chain can often reassemble column identifiers and plausible descriptions from fragments embedded in other GPT-4o-mini agents across generated networks. It does not show that models can discover tacit expertise, replace domain specialists, navigate real organizations, or know when evidence is professionally sufficient. `skill-bench` should adopt the inspectable claim-routing episode and layered-network decomposition, while requiring real authority, semantic evidence, calibrated stopping, cost, and downstream fidelity before promoting synthetic recovery into expertise-to-evaluation evidence.
