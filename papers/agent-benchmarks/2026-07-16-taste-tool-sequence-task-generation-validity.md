# TASTE broadens syntactic tool-sequence coverage, but its generator–validator loop does not establish workflow or benchmark validity

**Paper:** Tomer Keren, Nitay Calderon, Asaf Yehudai, Yotam Perlitz, Michal Shmueli-Scheuer, and Roi Reichart, *A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks*, arXiv:2605.28556v2 (2 June 2026), <https://arxiv.org/abs/2605.28556v2>.

**Official repository:** <https://github.com/tomerkeren42/TASTE-task-synthesis-from-tool-sequence-evolution>.

**Date read:** 2026-07-16.

**Review status:** Deep review of the complete immutable v2 paper and static release audit of exact paper-linked commit `d53da23956d63e2e6d9f6f5ba77fc5d0eca6b173`. The commit predates v2 by 1 day 20:29:33. It is close release evidence, not assumed to be the exact manuscript instrument.

## Evidence and provenance

- Immutable PDF: `data/papers/pdfs/2605.28556v2-taste.pdf` (41 pages; 1,390,277 bytes; SHA-256 `bf946a66f45167981aba435b8e5334e9e7cb73c7e31c8b54ba9e470b2e3b625b`).
- Complete layout-preserving text: `data/papers/text/2605.28556v2-taste.txt` (188,482 bytes; SHA-256 `5928525e850e3f236ca21cd6b8b744396a087773b915abb6fd8c9c6432442931`). The entire extraction was read, including methods, results, implementation details, verbatim prompts, examples, and checklist.
- Release provenance: `data/sources/releases/2605.28556v2-taste/provenance.json`.
- Restricted local archive: `data/sources/releases/2605.28556v2-taste/tomerkeren42-TASTE-d53da23.zip` (1,811,470 bytes; 99 files; SHA-256 `b73bc416c9d092c8ed238fd941a666b96b3d98ae42a19571bdb79e83ae6b33d7`). Its custom review/reproduction-only license prohibits redistribution and derivatives. The archive is locally excluded from Git and is **not** committed or reproduced in this review.
- Static audit covered all 99 paths and inspected the README/license, three domain packs, initial/final n-gram checkpoints, five medoid artifacts, seven task sets, prompts, sampler/clustering code, task generation/repair, domain validators, verifier integration, and evolution/fallback code. Small local scripts recomputed artifact counts, medoid-to-task sequence matches, retry/evolution flags, and base/evolved correspondence. No paid API calls or full benchmark reruns were made.

## One-sentence contribution

TASTE makes reverse generation from tool-name sequences into a concrete, inspectable benchmark-construction pipeline, but its released evidence establishes syntactic action dispersion and generator-conditioned package executability rather than semantic workflow coverage, saturation, professional validity, or readiness.

## Bottom line

TASTE contributes a useful **candidate-generation and panel-selection mechanism**: represent an environment by tool-name sequences; learn local positive and negative n-gram statistics from LLM plausibility labels; sample a larger candidate pool; choose medoids under a typed edit distance; then compile each sequence into a scenario, state, gold calls, and adversarial variant. This is a credible way to expose procedural regions that scenario-first authors may overlook. The released artifacts substantiate that the method produced longer, more varied tool-name sequences and executable synthetic tasks in three tightly specified customer-support simulators.

The paper's stronger conclusions outrun that evidence. Tool-name n-grams are syntax, not semantic workflow units. Their diversity grows almost mechanically with sequence length, and the hand-set distance treats name prefixes and READ/WRITE labels as semantics without external validation. The same model family labels sequence plausibility, authors tasks and databases, repairs failures, and proves solvability with corrupted gold hints. Failed sequences and tasks are replaced until a passing package exists. This supports **generator-conditioned package executability**, not an unbiased validity rate, complete alternative-path coverage, occupational realism, or robust task-solving ability.

The empirical difficulty result is also not a saturation test. The generated suite changes sequence length, write density, number of intents, user cooperation, decoy state, and user-simulator behavior simultaneously. Scores fall, but there is no matched difficulty-controlled panel, item-response linking, human baseline, independent capability criterion, or intervention showing that original high scores were caused by saturation rather than distribution shift. The paper reports point estimates without uncertainty, while agent and user randomness, task clustering, generator lineage, and selective retries create dependence.

The exact release improves inspectability but does not reproduce the paper's result surface. It contains checkpoints, medoids, and final task JSON, but no raw evaluation trajectories, reward records, per-configuration result tables, cost ledger, generation progress, evolution strategies, or administered-suite manifest. The release's paper-example sequence can be traced by equality from airline medoid 1 to `generated_1`, but its user identity and evolved instructions differ materially from Figure 6. Many final tasks no longer match a released medoid, and the final JSON drops the replacement/cluster lineage required to explain why.

The defensible claim is therefore narrow: **TASTE is an inspectable hypothesis for expanding tool-sequence syntax and compiling selected sequences into final-state-checkable synthetic tasks.** It does not establish semantic workflow coverage, benchmark validity, saturation, general agent capability, professional realism, or deployment readiness.

## Research question and claim ladder

The paper asks whether reversing task construction—from sampled tool sequences to scenarios—can automatically produce valid, broader-coverage, harder conversational-agent benchmarks (pp. 1–9).

## Why this matters for skill-bench

This review advances charter objectives A, B, and C by testing a reusable generation mechanism rather than endorsing its customer-support domains. It clarifies whether sequence-first synthesis can expand a cross-domain knowledge-work benchmark without laundering tool-string novelty, selective executability, or lower scores into workflow coverage and validity. Useful completion is a claim-bounded account of what to retain, repair, and validate using existing lifecycle machinery, with no accidental narrowing to conversational service agents.

Those words need separate claim levels:

1. **Syntactic action coverage:** more distinct tool names, n-grams, lengths, and edit-distance patterns occur.
2. **Package consistency:** one scenario, initial state, gold call list, and final-state grader execute together.
3. **Semantic workflow coverage:** selected tasks represent materially distinct intents, decisions, dependencies, and accepted procedures.
4. **Difficulty:** configured systems have lower or more discriminating response probabilities on a fixed construct.
5. **Saturation:** an older instrument no longer discriminates the target ability population, while a linked replacement does.
6. **Professional validity/readiness:** tasks and consequences represent consequential work accepted by qualified practitioners and operate under relevant conditions.

The paper directly supports level 1 and selected evidence at level 2. It reports lower scores relevant to level 4 but does not identify a common latent construct. It does not establish levels 3, 5, or 6.

## Methodology and system

### Stage 1: signed local sequence model

The adaptive contrastive trigram sampler keeps positive and negative count tables. It initializes them from original task sequences, samples candidate lengths from a clipped skew-normal distribution, asks Gemini-3-Flash whether each sequence is plausible, and updates positive counts for accepted n-grams and selected negative counts ending at model-identified problematic indices (pp. 4–5, 16–17, 21, 26–27). The final model uses `n=3`, smoothing `0.1`, negative weight `1`, 3,000 attempts, and a decaying temperature.

This is computationally simple and makes negative evidence operational. But its label is neither execution validity nor expert workflow validity. The validator asks whether *some* realistic interaction “could” produce the sequence and explicitly says to err toward accepting uncommon cases. It permits missing identification for assumed-external sub-tasks and concatenated multi-intent sequences. A binary response therefore mixes:

- local ordering plausibility;
- existence of some imaginable state;
- policy compatibility;
- scenario constructibility; and
- the judge's tolerance for artificial combinations.

No independent labels, repeated judge calls, judge agreement, held-out domains, or calibration against executable sequence feasibility are reported for this stage. Negative windows are selected using the same model's problematic indices, so the signed model learns that judge's decomposition, not independently observed invalidity.

### Stage 2: clustering and medoid selection

TASTE samples 2,000 unique candidates and chooses `K=50/114/114` medoids. Its weighted Levenshtein substitution costs are `0.33` for same type and group, `0.66` for same type/different group, and `1` across types; insertions/deletions cost `1` (pp. 5, 17–18). Tool groups are usually the prefix before the first underscore.

Medoids are more inspectable than latent embeddings and preserve actual candidate sequences. Yet the distance embeds unvalidated ontology assumptions. `search_direct_flight` and `search_onestop_flight` are “close” because of a shared prefix; two writes with distinct permissions or consequences remain closer than a read/write pair. Tool names omit arguments, actors, state preconditions, evidence authority, valid time, branch conditions, decision thresholds, and artifact effects. Two identical name sequences can implement different work; two different sequences can be equivalent procedures.

`K` is inherited from the old suite size rather than chosen from coverage saturation, cluster stability, intended construct strata, or marginal information value. There is no repeated clustering, seed sensitivity, stability score, held-out coverage audit, or evidence that one medoid per cluster optimizes discrimination or professional representativeness.

### Stage 3: compilation, repair, witness, and adversarial evolution

Two LLM calls author a verbose scenario/gold argument list and database. Deterministic checks test arguments, entity existence, schema, and whether the canonical calls run. An LLM checks policy coherence. A Gemini verifier then receives shuffled gold calls with 30% of each call's arguments removed and must obtain final-state reward 1 (pp. 5–6, 18–20). Failures trigger patching, regeneration, and eventually cluster replacement.

Evolution uses three further calls: select adversarial patterns for writes, add decoy records, and rewrite the user behavior. A verifier checks the evolved variant; repeated failure leads to a lite rewrite and then the base task (pp. 6, 18–20, 31–33).

This architecture wisely distinguishes base executability from interaction adversity and retains a fallback so the panel is complete. However:

- the verifier sees answer-bearing privileged evidence;
- one successful stochastic run is used as a witness;
- the witness does not enumerate legitimate alternatives or prove grader completeness;
- exact final state ignores communication, efficiency, unsafe attempted actions, unauthorized reads, intermediate side effects, and recovery quality (the paper itself acknowledges this on p. 3);
- regeneration/replacement conditions the final panel on what this generator and verifier can jointly realize;
- evolved validation skips some earlier rule checks “by construction,” despite adding state and rewriting instructions;
- adversarial patterns are manually curated but have no incident provenance, expert prevalence, fair-basis study, or false-trap audit; and
- the same gold arguments remain fixed, so evolution can privilege canonical recovery even when a changed conversation could make another response legitimate.

## Evidence and results

### Performance drops do not identify saturation

Across eleven agent/user pairs, reported pass¹ drops range from 5% to 80%; Gemini-3-Flash falls from approximately `0.82–0.94` on τ²-Bench Verified to `0.28–0.61` under one user configuration (pp. 6–8). Evolution lowers selected Airline/Retail success rates by 16–55%, and longer/write-heavier buckets score lower (pp. 8, 15).

These are descriptive treatment differences, not a saturation diagnosis:

- task identity is not held fixed across suites;
- average gold length changes sharply (Airline `2.84→11.36`, Retail `4.82→10.66`, Telecom `4.53→6.50`; p. 14);
- evolved user behavior and decoy density also change;
- user-model effects are large and part of the configured treatment;
- Claude is absent from several cells and pass³ is reported only for Airline;
- no repeated seeds or confidence intervals are reported; the checklist explicitly answers “No” for statistical significance (p. 37);
- no common-item linking or IRT analysis tests whether both suites measure the same ability scale; and
- a harder generated distribution can lower every score while being less representative or less discriminating.

“Saturation” should require a response matrix showing ceiling compression, lost rank/information under the intended population, and recovery on linked items—not merely lower performance on a substantially different distribution.

### Coverage is length-sensitive syntax, not a denominator over work

The paper reports weighted edit distance increases up to 124%, average n-gram TTR increases up to 111%, and normalized tool-frequency entropy increases (pp. 7, 14–16). These calculations substantiate greater diversity in released gold tool-name strings.

Their construct interpretation is weak:

- longer sequences generate many more high-order n-gram positions and make near-unique 5/6-grams likely;
- TTR has known sample-length and token-count sensitivity, but no matched-length comparison or rarefaction is supplied;
- “available tool-combination space” has no denominator restricted to policy-feasible, useful, or professionally relevant workflows;
- coverage weights each selected task equally despite shared clusters/generator lineage;
- Telecom compares write-only gold lists even though successful trajectories include reads and user tools;
- GoldSim selects the shortest successful run pooled across agents/users/trials and substitutes gold when none succeeds (pp. 14–15), combining observed behavior with authored witnesses; and
- unique combinations need not correspond to unique intents, decisions, consequences, or failure signatures.

The correct label for these metrics is **tool-sequence syntactic dispersion**. Semantic coverage requires typed requirements, states, decisions, accepted paths, consequences, and expertise authority.

### Verifier evidence is narrow and partially circular

The verifier is evaluated by treating unchanged τ²-Bench tasks as valid and substantial Verified edits as invalid: 50 Airline items (8 invalid) and 86 Retail items (9 invalid). Reported precision is `1.00/0.97` and recall `0.75/0.83` (p. 8). This is useful but not decisive:

- “changed by Verified” is a proxy, not an independently blinded solvability label;
- Telecom is absent;
- denominators contain very few invalids;
- confidence intervals and item-level predictions are absent;
- the verifier receives corrupted gold hints unlike evaluated agents;
- the same model authors and verifies tasks; and
- high precision under this proxy does not establish correctness of novel generated tasks.

Authors manually inspected only the 15 tasks on which every evaluated pair failed and judged all valid (p. 8). That is outcome-conditioned review, not a random full-suite audit, and no rubric, qualifications, independent labels, disagreements, or records are released.

## Exact release audit

### What is present

The 99-file snapshot contains:

- three source domain packs (`50/114/114` task files, policies, tool specs, wiring);
- initial and final signed n-gram checkpoints;
- full medoid/member artifacts;
- task generation and evolution prompts/code;
- deterministic domain validators; and
- seven final/base task-set JSON files.

This is enough to inspect much of the pipeline and final task packages. It is more useful than a paper-only generation claim.

### What is missing

The release lacks the artifacts needed to replay the paper's empirical claims:

- raw agent/user trajectories and final-state observations;
- per-task/per-model rewards and pass¹/pass³ tables;
- the script/input manifest that produces Tables 1–2 and Figures 2–5;
- rendered prompts, model responses, token/cost records, and API timestamps;
- stage-1 item-level plausibility labels;
- stage-3 generation `progress.jsonl`, `generation_meta.json`, evolution `metadata.json`, and `strategies.jsonl` described by the README;
- task-to-original-cluster/replacement lineage in final task JSON; and
- an administered-suite identity selecting which of three Airline evolved sets is τᶜ-Bench.

The released code also has no global seed argument for the primary training/clustering/evolution commands. Stage-3 reclustering hard-codes `random.Random(42)`, but initial pool generation and LLM calls remain stochastic. Exact reproduction requires more than paper hyperparameters.

### Checkpoint and task audit findings

The checkpoints expose selection history but also correspondence gaps:

- Airline `post_seed.json` reports 51 total seed sequences (`32` valid, `12` invalid, `7` skipped) although the domain task file has 50 records; no item ledger explains the extra denominator.
- The final Airline checkpoint is a resumed run and records only the resumed segment's `607` accepted, `61` rejected, and `332` duplicate outcomes, while its accepted set has `1,621` sequences. Retail's final artifact records only its last 100-attempt window (`45/5/50`) with an accepted set of `1,390`. These snapshots cannot directly regenerate the paper's 86.7% ablation estimate.
- Airline medoid validation replaced 17 of 50 initial medoids; Retail and Telecom medoid files report one-attempt acceptance for all 114. Final tasks add another replacement layer.
- Exact sequence matching connects only `47/50` Airline and `106/114` Retail final/base tasks to the released medoids. Telecom final tasks match `89/114` of the derived write-only medoids. Final task JSON retains retry counts but not replacement source or cluster ID, so unmatched cases cannot be traced from released artifacts alone.
- Evolution fallback is substantial and heterogeneous: the Gemini-3-Flash sets contain 5 Airline and 2 Telecom unevolved fallbacks; 1 Retail and 50 Telecom tasks are marked lite evolution. Thus “evolved suite” is a mixture of full, lite, and base treatments.
- Release fields are inconsistent across domains: Airline tasks carry `difficulty: easy` and an “easy” profile even when `evolved=true`; Retail/Telecom omit those fields. This limits machine-readable treatment interpretation.

### Reconstructed sequence → task → evolution → grader chain

A partial chain can be reconstructed for the paper's Airline example:

1. Original Airline tasks feed aggregate positive/negative trigram counts; no per-candidate ancestry links a particular seed to a sampled sequence.
2. Released Airline cluster `1` has the representative sequence `get_user_details → get_reservation_details → search_onestop_flight → update_reservation_flights → list_all_airports → get_reservation_details → get_user_details → update_reservation_baggages → search_direct_flight → send_certificate`; it was accepted on the first medoid-validation attempt and represents a 45-member cluster.
3. Exact sequence equality links it to final task `generated_1`, with zero recorded solver retries and `validation_success=true`.
4. That task is marked `evolved=true`, adds misleading membership/payment/compensation claims and decoy state, and preserves the ten canonical calls/arguments.
5. The evaluator applies τ²-Bench final-state equality after a simulated interaction; the release contains no trial trajectory or grader observation for this item.

This is valuable partial lineage, but not the paper's exact Figure 6 artifact. Figure 6 names “Liam Cohen” and prints a shorter evolved script; the release uses “Liam Miller” and adds further insurance and conditional-compensation branches. The release therefore substantiates a nearby task version, not exact paper/release identity.

## Unique insight for skill-bench: coverage needs three ledgers, not one diversity score

TASTE's most useful provocation is correct: scenario-first authoring can repeatedly sample familiar workflows without noticing procedural gaps. The repair is not to equate tool-string novelty with benchmark coverage. `skill-bench` should separate:

1. **Candidate-generation ledger**
   - source task/version and authority;
   - generator configuration and random/API identity;
   - candidate sequence/state/requirements;
   - plausibility labels and evidence views;
   - duplicates, rejects, repairs, replacements, and attrition reason.
2. **Semantic coverage ledger**
   - intent and decision boundary;
   - required evidence/state transitions;
   - accepted procedure equivalence class;
   - artifact/consequence and failure signature;
   - domain/expertise authority;
   - declared population denominator and uncovered strata.
3. **Panel health and claim ledger**
   - why each item was admitted;
   - item information/difficulty with uncertainty;
   - construct and treatment comparability to anchors;
   - task/grader defects and revisions;
   - contamination/saturation evidence;
   - permissible capability/use claims.

Tool n-grams can propose candidates for ledger 1 and provide one feature for ledger 2. They cannot replace ledgers 2–3.

## Comparison with nearby skill-bench evidence

- **Anchor** starts from an expert-informed formal constraint program and compiles instruction, environment, oracle, and verifier. It offers stronger shared semantic lineage and solver witnesses, but still does not prove projection equivalence or verifier completeness. TASTE explores a broader syntactic action space but has a weaker authoritative semantic spine.
- **SLBench** starts from typed relations among source skill clauses and projects them into executable evidence contracts. Its relation ledger better preserves preconditions, exceptions, and consequences, but generator/grader co-design and selected-case attrition remain. TASTE should borrow typed relation coverage rather than treating adjacent tool names as the unit of logic.
- **SOP-Bench** exposes a procedure/data/tool/oracle package but often scores endpoint recovery rather than procedural fidelity. TASTE has the same endpoint limitation: final-state equivalence admits many paths but observes neither mandatory procedure nor unsafe/collateral behavior.
- **τ²-Bench** supplies the simulator and final-state semantics; TASTE changes task construction, not the fundamental evaluator. It therefore cannot claim to repair trajectory-observability limits inherited from the base harness.
- **Task-health/lifecycle contracts** already in this repository are the correct implementation home for origin, candidate/rejection history, role transitions, defects, saturation evidence, versioned replacements, and retirement. No new TASTE-specific schema is justified.

## Limitations, reproducibility, and operational realism

**Reproducibility strengths:** immutable paper version; verbatim prompts; exact hyperparameters; readable code; complete domain specifications; signed-model checkpoints; medoid/member artifacts; base tasks for two domains; exact close-timing commit; explicit restrictive license.

**Reproducibility weaknesses:** proprietary mutable API models; vendor-default reasoning settings; no global seeds; incomplete stage ledgers; no raw trials/results; no paper-figure scripts; ambiguous administered Airline task set; post-generation replacements not linked; paper/release example drift; restricted redistribution; external τ²-Bench dependency not pinned in the provenance manifest.

**Operational-realism ceiling:** all three domains are synthetic customer-support transition systems. Policies, tool schemas, tasks, users, decoys, and final consequences are authored inside the simulator. There are no observed work records, qualified practitioner authors/reviewers, real service outcomes, escalation costs, privacy/security obligations, or deployment traces. The method may transport to other formal environments, but that is untested. Its bounded domain application must not narrow `skill-bench` to customer service or tool-call sequences.

## Transferable design implications for skill-bench

### Retain

1. Reverse-generation as an **expansion strategy**, especially when current tasks cluster around familiar paths.
2. Explicit negative candidate evidence rather than retaining only successful generations.
3. Representative-panel selection with inspectable medoids rather than opaque embedding centers.
4. Base-versus-evolved variants and graduated fallback, provided treatment status remains explicit.
5. Executable witnesses plus deterministic structural checks before expensive agent trials.

### Repair

1. Replace tool-name-only distance with a typed semantic signature: actor, authority, pre/postcondition, evidence dependency, state mutation, consequence, and accepted alternatives.
2. Preserve immutable candidate → label → cluster → selected medoid → task → repair/replacement → evolution → grader lineage.
3. Separate LLM plausibility, deterministic executability, independent task validity, alternative-path completeness, and expert/ecological validity.
4. Record every retry and rejected candidate; report release coverage conditional on attrition.
5. Make full/lite/base evolution a stratified treatment, not one suite label.
6. Use matched anchor items or equivalent forms to distinguish increased difficulty from construct drift and saturation.
7. Report task-clustered uncertainty and repeated configured-system trials; keep user-simulator identity as a treatment component.
8. Preserve trajectory and collateral-state checks alongside final state, especially for forbidden attempts and unnecessary access.

### Validation experiments

1. **Length-matched semantic coverage study:** compare scenario-first, TASTE name-sequence, and typed-relation generation at fixed length/write ratio; have blinded experts label distinct intent/decision/consequence strata and valid alternatives.
2. **Generator–verifier independence ablation:** cross models and human reviewers across sequence label, task authoring, and solvability verification; estimate false passes/fails on a random sample, not only universally failed items.
3. **Saturation bridge:** administer shared anchor/equivalent-form items with repetitions and fit a response model; test whether the new panel adds information where the old panel is compressed without changing the intended construct.
4. **Mutation and alternative-path audit:** mutate state, instructions, forbidden side effects, and legitimate procedure variants; require graders to fail invalid packages and admit equivalent valid ones.
5. **Attrition sensitivity:** compare released scores and coverage with all candidate/retry histories versus passing-only items; quantify which semantic strata the generator/verifier systematically removes.

## Concrete repository actions and queue decision

No new build or consolidation task was added. The evidence maps to already implemented task-health, benchmark-bundle, validity-argument, metric-monitoring, trace/root-cause, expertise-transfer, and lifecycle machinery. A TASTE-specific contract would duplicate those objects. The next useful work is empirical use of those contracts in a generation experiment, not another schema.

## Final assessment

TASTE is strongest as a warning and a proposal: author-written scenarios can hide action-space blind spots, and reverse generation can systematically search for candidates. Its release gives enough code and artifacts to make that proposal technically concrete.

Its central metric and inference should not be promoted unchanged. More tool-name n-grams mean more **syntactic dispersion**, not necessarily more knowledge work. One hint-assisted successful run means one configured witness found the authored endpoint, not that the task, grader, alternatives, or professional construct are valid. Lower scores on much longer, more adversarial, differently simulated tasks mean the new package is harder for those configured systems; they do not prove the old benchmark was saturated or that the new benchmark measures robust task-solving ability.

For `skill-bench`, reverse generation belongs upstream as a candidate-expansion instrument. Expertise authority, semantic coverage, accepted-path validity, grader observability, item health, and claim licensing must remain independent downstream gates.