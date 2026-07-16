# Networked Intelligence: routed shared context is a consequential coordination hypothesis, not an isolated network effect

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 21-page arXiv v1 paper, including the Supplementary Note, Supplementary Methods, dataset description, all figures/tables, and the standalone-agent prompt, and checked the layout extraction against the preserved arXiv HTML/PDF evidence.

- **Paper:** Sutanay Choudhury et al., *Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science*, arXiv:2607.13220v1, https://arxiv.org/abs/2607.13220v1
- **Version read:** immutable v1, submitted 14 July 2026; metadata has no withdrawal/retraction notice
- **Date read:** 2026-07-16
- **Local PDF:** `data/papers/pdfs/2607.13220v1-networked-intelligence.pdf` (21 pages; SHA-256 `a7bdf1e2e5458484e410eefe4ec4576cfbefeaedd6806ecfa164a4d3e1802e05`)
- **Local text:** `data/papers/text/2607.13220v1-networked-intelligence.txt` (SHA-256 `71f37db5996479ace1419ff119778ff1e998dcdf674d00021db1a00897e2b27c`)
- **Immutable arXiv HTML:** `data/papers/source/2607.13220v1.html` (SHA-256 `794add32063facde8ccb78f9d43f27ce49e7c8871aa0f4618df818704ebf2cf7`)
- **Acquisition/release provenance:** `data/sources/releases/2607.13220v1-networked-intelligence/provenance.json`

No author-owned implementation, graph, campaign data, notebook, prompt set, routing record, trace, artifact matrix, experiment plan, result ledger, or analysis release was located at acquisition. The supplement says “see released harness” after omitting baseline output-schema fields, but provides no locator. This is a freshness-bounded search result, not proof that no release exists or will appear.

## One-sentence contribution

The paper proposes an active shared-context graph that captures typed scientific entries, preserves derivation links, and routes selected claims among three expert–agent workspaces, then reports one week-long multi-omics campaign and a 26-item post-hoc coverage comparison; it makes cross-expert routing a valuable measurable unit of knowledge work, but does not isolate routing from multiple humans, repeated sessions, proactive analyses, unequal compute, or treatment-specific information, and reports a proposed experiment rather than a realized downstream experimental result.

## Why this matters

This source advances charter objectives A–C through a general question rather than a biology scope commitment: **when does context produced in one workstream become usable evidence that changes another qualified actor's consequential decision?** Static memory, typed handoff, and participation records do not fully capture recipient selection, unsolicited delivery, attention, and cross-expert transformation. The source therefore identifies a useful coordination primitive for realistic distributed knowledge work.

The evidence ceiling is equally important. A graph edge, a routed message, and a narratively coherent downstream proposal are three different observations. None alone establishes that the recipient saw the claim, adopted it, changed a decision because of it, chose a better action, or caused a beneficial outcome. Useful transfer into `skill-bench` is an end-to-end routing-event record and a matched counterfactual—not a new scientific knowledge-graph subsystem or a generic “team intelligence” score.

## Research question and defensible claim boundary

The paper asks whether an active context graph can move a locally produced observation or hypothesis to the team member whose next decision it can inform, while retaining provenance and maintaining an evolving shared mechanistic model. It presents Mycelium as three coupled layers:

1. an active context graph with a closed eight-type node vocabulary;
2. a Claude Chat/MCP participant runtime connected to server-side analysis;
3. logging, proactive execution, state routing (“pollination”), and graph-write grounding protocols.

Its first empirical setting has three domain experts working asynchronously for one week. User-L analyzes 4,495 proteins across 62 samples; User-E contributes regulatory/iron-biology reasoning; User-J contributes phenotype interpretation and experimental design. The broader source pack contains four described modalities but five tabled tracks: proteomics, UniProt annotation, a metabolic graph, HPLC phenotypes, media optimization, and a transcription-factor library (the table treats annotation/reference resources alongside measured modalities). Every client and server operation uses Claude Opus 4.8.

The strongest defensible claim is narrow:

> In one author-run multi-omics campaign, Mycelium stored and surfaced cross-thread claims, and the authors reconstruct two routing episodes that they interpret as contributing to a shared mechanistic account and a later experiment proposal. Under a separate one-realization-per-condition content audit, the human–AI Mycelium campaign explicitly surfaced more of 26 author-extracted artifacts than either of two standalone Claude Opus 4.8 runs over the supplied data.

The paper does **not** establish a causal routing effect, tacit-knowledge transfer, irreducible network advantage, independent corroboration, scientific truth, improved experimental outcome, four-to-six-month time savings, calibrated routing utility, production reliability, privacy-preserving federation, cross-domain validity, or readiness.

## Methodology and system

### Active context graph and runtime

The graph's eight node types are `dataset`, `observation`, `interpretation`, `hypothesis`, `finding`, `open_question`, `recommendation`, and `experiment_proposal`. Edges are said to include `generated_by`, `derived_from`, `supports`, and `contradicts`; every new claim is described as linked to data, user, agent, or tool execution. Server-side analysis preferentially uses library functions, otherwise generates Python, performs error recovery, validates data structures, and emits executable notebooks.

This is a promising representation, but the semantics outrun the evidence. Referential grounding proves that a parent identifier exists, not that an observation is correct, an interpretation follows, a “finding” is established, a contradiction is adjudicated, or a proposal is authorized. The paper does not expose entry/edge schemas, write validators, identity/version rules, immutable graph events, notebook hashes, relation constraints, confidence/status semantics, access policy, or examples sufficient to audit the claimed exact lineage. “Physically auditable” and “fully reproducible” are therefore architecture claims, not demonstrated study properties.

The ontology also collapses important states. A human observation and auto-captured result share one type; an interpretation and hypothesis have no visible authority, uncertainty, valid time, applicability, disagreement, supersession, or approval state; and “finding” presupposes an establishment process the contract does not show. The paper itself says all contributors currently receive equal epistemic weight. Attribution is necessary, but equal attribution is not qualified authority or evidential weight.

### Routing and proactivity

Mycelium is said to score candidate cross-thread links against localized belief states, route claims whose epistemic utility is high, preserve disagreements, and run proactive analyses between sessions. The Supplementary Note defines routing value as the change in a receiver's maximum expected action utility after adding claim `v`, with a critical edge when the change exceeds threshold `τ`.

No implementation or empirical measurement of that quantity is reported. The source does not identify the utility function, action set, outcome distribution, threshold, scoring model/prompt, candidate pool, delivery cadence, false-positive/false-negative policy, permission filter, or user controls. Figure 7 only describes a “smaller sustained fraction” of active work; it gives no graph node/edge counts, routing opportunities, attempted deliveries, accepted/rejected links, proactive jobs, human turns, model calls, tokens, wall time, failures, or review burden. The paper therefore demonstrates narrated routing instances, not calibrated sparse conditional computation.

Proactivity and routing are also inseparable in the evaluation. New system-authored analyses can expand content independently of cross-user delivery. Persistent graph state, multiple participant sessions, qualified human expertise, routing, proactive search, generated notebooks, and a shared evolving goal all enter one Mycelium package.

### Campaign evidence chain

The first narrated route carries User-E's regulatory anomaly to User-L, where it is said to recontextualize the absence of corresponding top proteomic signals. The second carries User-J's HPLC phenotype constraint to User-L, shifting the synthesis from protein ranking toward intervention mechanisms. The paper then attributes a converged retention/re-assimilation model and several proposed interventions—`mqo-2`, `kguT`, `PP_2256`, sulfonate supplementation, and `PP_1794` characterization—to the combined threads. User-J authors the experiment plan.

This is a coherent process account but an incomplete causal chain. The paper does not release the source entries, exact routed payloads, timestamps, recipient-visible views, prior beliefs, acknowledgement, adoption language, graph diffs, decision versions, alternative explanations, rejected proposals, or counterfactual no-route continuations. The figures are author reconstructions, not independent event evidence. Existing HPLC/proteomics measurements are inputs to the campaign; the paper reports no execution or result from the newly proposed interventions. Thus “altered experimental action” means **changed experiment planning/proposal**, not an authorized experiment run or observed biological consequence.

### Standalone comparison and artifact instrument

Two standalone Claude Opus 4.8 baselines receive the frozen problem, data/resources, code environment, and an artifact contract. Baseline B adds a clause to integrate “as a multidisciplinary team would”; C removes it. Both use `xhigh` reasoning and adaptive thinking and run once to natural termination. Mycelium uses the default `high` setting but consists of three humans, their repeated interfaces, autonomous investigations, and one week of asynchronous work.

The comparison therefore does not isolate architecture. The treatments differ in participant count, human expertise, interaction count, temporal opportunity, local context, prompting, proactive jobs, total inference, stopping, artifact format, and likely review/selection. “Identical data” does not mean identical information: the paper's irreducibility argument depends on expert priors, tacit knowledge, and action authority that are not supplied to the standalone agents. Conversely, the actual baseline is given the campaign files, so the paper does not show that non-mergeable contexts constrained this study.

The authors extract a global set of 26 “scientific artifacts” and score each execution from 0 (absent) to 4 (actionable with data-backed rationale). Recomputing Table 3 verifies Table 2 exactly:

| Condition | Surfaced | Score ≥2 | Score ≥3 | Score =4 | Sum / 26 | Mean among surfaced |
|---|---:|---:|---:|---:|---:|---:|
| Mycelium | 25 | 22 | 17 | 4 | 68 / 26 = 2.62 | 68 / 25 = 2.72 |
| Standalone B | 17 | 14 | 9 | 2 | 42 / 26 = 1.62 | 42 / 17 = 2.47 |
| Standalone C | 18 | 15 | 11 | 3 | 47 / 26 = 1.81 | 47 / 18 = 2.61 |

These arithmetic summaries are reproducible from the paper; their validity is not. The artifact universe is extracted from the evaluated traces rather than prospectively frozen from an independent source, so Mycelium's longer, multi-actor trace has more opportunity to nominate content into the denominator. The paper gives no extraction protocol, independent authorship, blinded raters, duplicate ratings, codebook beyond endpoint labels, item-level rationale, adjudication, alternative-valid handling, or uncertainty. One realization per condition precludes stochastic reliability or inference; “significantly broader” is unsupported statistically. Similar conditional specificity does not prove that standalone limitations were “purely” exploration breadth, because selection into the surfaced subset differs by condition.

## Evidence and result interpretation

### What v1 supports

- A concrete system design for typed shared context, cross-thread routing, persistent hypotheses, and server-side notebook-producing analysis.
- One week-long, three-expert author deployment with at least two narrated cross-thread routing episodes.
- A later experiment proposal that combines contributions attributed to three expert threads.
- Internally consistent descriptive counts for a 26-item explicit-content audit.
- The useful admission that breadth and specificity should be separate and that the matrix audits explicit coverage rather than latent capability.
- The useful admission that equal epistemic weighting and cross-domain translation loss remain unsolved.

### What v1 does not support

- **No identified routing effect:** there is no no-routing/shared-store/manual-forwarding/full-broadcast comparison, delayed delivery, route ablation, or replay from frozen recipient state.
- **No receipt/adoption evidence:** delivery, attention, interpretation, uptake, and downstream decision change are reconstructed rather than independently observed.
- **No experimental consequence:** the newly derived interventions are proposed, not reported as executed with outcomes.
- **No scientific validation:** independent biologists do not adjudicate the mechanistic model, proposed interventions, or 26 artifacts.
- **No tacit-transfer evidence:** exclusive expert knowledge is asserted generally, but the routed payloads in this campaign are not classified as tacit, elicited, previously unavailable, or inaccessible to the baseline.
- **No irreducibility proof:** the formal note defines regimes but neither establishes conditionally independent error profiles nor shows non-mergeable contexts in the empirical case.
- **No time-saving evidence:** a one-week sprint is not compared with a matched four-to-six-month process, and development, setup, analysis, review, and failed work costs are absent.
- **No operational reliability:** no repeated campaign, routing precision/recall, stale/incorrect route test, burden study, outage/invalid denominator, or cost ledger is reported.

The formal “irreducibility” claim is especially weak. Independent corroboration only reduces error under assumptions about estimator errors and combination; the paper does not measure those errors, independence, truth, or decision loss. A single model can also be sampled, ensembled, independently scaffolded, or paired with external evidence; shared weights do not mathematically imply one identical error trajectory. Non-mergeable contexts can make a monolithic full-information baseline impossible, but a routing network does not automatically gain lawful access or preserve privacy. It succeeds only if an authorized summary can cross the boundary with sufficient fidelity—precisely the untested translation and permission problem the paper leaves for future work.

## Unique insight: routing is an intervention between provenance and consequence

The paper's most transferable insight is that **recipient selection and delivery are first-class transformations**, not incidental features of memory. A claim can be well-provenanced yet useless because it never reaches a qualified decision-maker; it can be routed yet harmful because it is stale, mistranslated, unauthorized, or overweighted; and it can precede a decision change without causing it.

For `skill-bench`, preserve this chain:

```text
source evidence and participant authority/permission
→ captured proposition with exact locator and epistemic status
→ graph relation, transformation, version, validity, and disagreement
→ routing opportunity and candidate-recipient rationale
→ policy/permission decision and delivered evidence view
→ recipient receipt, attention, interpretation, and adoption/rejection
→ changed analysis, belief, or decision record
→ authorized attempted action
→ realized state/result and collateral consequence
→ bounded claim about route utility
```

No link inherits the next. The decisive causal unit is a **frozen recipient-state delivery intervention**: hold source claim, recipient, prior workspace, task, budget, and observer fixed; vary no delivery, targeted delivery, broad delivery, delayed/stale delivery, corrupted translation, or manual forwarding; then measure receipt, adoption, decision delta, artifact/state consequence, burden, and error. A graph path documents a possible lineage. It does not show that the route was necessary, sufficient, correctly timed, or beneficial.

This extends—not replaces—existing repository machinery. Laboratory workflow twins supplies claim-level authority and transformation cautions; Shared Selective Persistent Memory separates retained objects, access, presentation, adoption, and execution; HAS-Bench separates participant availability, exercise, uptake, effect, and burden; AgentCoop separates transport from receiver use; LongMemEval-V2 separates evidence delivery from held-out action benefit. Mycelium contributes **candidate-recipient selection and unsolicited cross-workstream delivery** between those established links.

## Limitations and validity threats

1. One campaign, one institution, one biological problem, three participating authors, and one week provide no population or cross-domain inference.
2. Participant selection, credentials specific to each claim, prior project familiarity, independence, compensation, consent, and conflicts are not reported.
3. All human and server-side interfaces use Claude Opus 4.8, coupling capture, analysis, routing, synthesis, and baseline behavior to one model family.
4. The Mycelium treatment bundles three humans, repeated sessions, expert priors, shared persistence, routing, proactivity, tools, and more total work.
5. Standalone conditions receive one continuous run each; there are no repeats, missing/invalid-run records, or uncertainty estimates.
6. Total model calls, tokens, tool executions, wall time, human time, review time, and cost are not matched or reported.
7. The baseline artifact contract and single-run deliverable differ from the team's evolving graph/workflow, weakening measurement equivalence.
8. “Identical data” does not equal identical expert information, priors, authority, interaction opportunities, or compute.
9. The empirical campaign does not instantiate the claimed non-mergeable-context regime because the baseline receives the supplied datasets/resources.
10. No no-routing, passive shared graph, manual-forwarding, full-broadcast, delayed-routing, or route-ablation condition isolates targeting.
11. Routing utility `Δ`, threshold `τ`, candidate generation, belief-state representation, and scoring implementation are neither released nor measured.
12. No routing denominator supports precision, recall, timing, overload, or missed-critical-link claims.
13. Figure 7 gives no quantitative proactive/responsive split, while proactive investigation is confounded with routing.
14. Exact source entries, deliveries, timestamps, recipient views, acknowledgements, adoption events, and decision diffs are unavailable.
15. Referential grounding is not claim truth, causal validity, authority, applicability, consensus, or experimental confirmation.
16. The eight-type vocabulary lacks demonstrated uncertainty, valid time, supersession, access scope, consent, approval, and claim-specific expertise.
17. Equal epistemic weighting ignores differing authority and reliability; attribution does not solve weighting.
18. Preserving contradiction nodes does not show that disagreement is surfaced, understood, resolved, or safely retained.
19. The 26-item artifact universe appears extracted after viewing the evaluated executions, creating outcome-conditioned construct coverage.
20. Artifact extraction, scoring rubric, rater identities, blinding, duplicate labels, agreement, adjudication, and item rationales are absent.
21. Scores are ordinal but averaged; no evidence validates equal step distance, compensability, category weighting, or the `≥2/≥3` thresholds.
22. One observation per condition makes “significantly broader” and pure-exploration attribution unsupported.
23. Conditional specificity compares different selected artifact subsets and cannot establish equivalent local reasoning quality.
24. The mechanistic synthesis and proposed experiments have no independent expert review, accepted alternatives, or prospective registration.
25. Newly proposed experiments are not executed; existing campaign measurements cannot serve as downstream validation of later recommendations.
26. The four-to-six-month compression claim has no matched historical cohort, process definition, time ledger, or outcome equivalence.
27. Conditional independence of expert/model errors is asserted, not measured; shared weights do not prove identical errors across contexts or runs.
28. Non-mergeable information establishes an access constraint, not guaranteed network success, lawful transfer, privacy, or semantic fidelity.
29. No permission model, purpose limitation, field/entry visibility, redaction, revocation, audit access, or cross-project privacy test is shown.
30. No author-owned code/data/harness release was located, and the baseline prompt omits fields while pointing to an unlocated “released harness.”
31. Mutable proprietary model/service identities, absent environment locks, and unreleased notebooks prevent reproduction.
32. No recipient burden, interruption, over-routing, stale route, malicious entry, false corroboration, or recovery experiment supports safe operation.

## Reproducibility and operational realism

Static conceptual reproducibility is moderate: v1 specifies the eight entry classes, examples of edge semantics, MCP/chat architecture, Python execution pattern, four protocol names, dataset dimensions, one abridged baseline prompt, and the complete 26×3 score matrix. Another team could build a system inspired by Mycelium.

Study reproducibility is absent. The graph schema/instances, routing implementation, prompts, chat sessions, notebooks, environment, exact datasets, artifact extraction/rating protocol, experiment proposal, run traces, and results are unavailable. The phrase “fully reproducible” applies at most to the intended notebook-producing mechanism, not to evidence exposed for this paper. The unlocated harness also prevents baseline replay.

Operational realism is mixed. Asynchronous experts, heterogeneous evidence, persistent hypotheses, negative results, cross-modal tension, proactive analysis, experiment planning, and review burden are genuine features of knowledge work. But the study omits the hardest production boundaries: permissions, stale claims, revocation, contradictory authorities, failed or noisy routing, attention limits, cross-language/domain translation, audit/recovery, and realized downstream action. It is a compelling deployed case narrative and architecture hypothesis, not a reliability or benefit study.

## Transfer to skill-bench

1. **Treat routed context as a versioned intervention.** Record candidate generation, recipient rationale, permission decision, timing, delivered evidence view, and route policy separately from source provenance and shared storage.
2. **Separate opportunity, delivery, receipt, adoption, decision change, action, and consequence.** A route edge is no more evidence of use than a shared file permission is.
3. **Bind authority to propositions and uses.** A contributor may be authoritative about a local observation but not its cross-domain interpretation or a recipient's action threshold. Preserve transformations, disagreement, valid time, and approval.
4. **Use frozen recipient-state counterfactuals.** Compare targeted route, no route, manual forwarding, broadcast, delayed/stale route, and corrupted translation while holding task, prior workspace, recipient, budget, and grader fixed.
5. **Measure both missed-link and overload loss.** Report routing opportunities, true/false deliveries, stale/duplicate routes, attention/inspection, interruption burden, decision loss, and downstream consequences; do not optimize recall alone.
6. **Keep graph validity distinct from scientific/task validity.** Parent existence and notebook replay support lineage/execution claims, not substantive correctness or professional acceptance.
7. **Require a prospective artifact universe or independent outcome.** Do not define “breadth” from the same traces being compared without a frozen external construct map and blinded, reliable scoring.
8. **Keep configured packages explicit.** A human–AI network versus one standalone run is a legitimate package comparison only when work, information, compute, stopping, and instrument differences are reported; it is not a routing ablation.
9. **Do not promote proposals to outcomes.** Preserve proposal, authorization, execution, measured result, replication, and decision consequence as separate records.
10. **Do not infer team intelligence, tacit transfer, irreducibility, scientific discovery, privacy, productivity, or readiness** from this one narrated campaign.

No new schema is warranted. Existing participation/authority, expertise-transfer, evidence-state, persistent-workspace, trace, handoff-usability, action/state, metric, task-health, and validity contracts can carry the chain. The nonduplicate requirement is a route-event view joining those records, not a Mycelium-specific subsystem.

## Concrete repository actions

No new queue task is added. The evidence-implied validation is already covered by existing participant realization, authority, evidence-delivery/adoption, handoff, and consequence machinery; opening another generic memory or collaboration build would duplicate active work.

1. At the next relevant consolidation, add **routing opportunity → permission/delivery → receipt/adoption → decision delta → action/result** to the participation/context synthesis, with Mycelium explicitly bounded to a case narrative plus one configured-package content audit.
2. When a consented distributed-work pilot exists, implement one frozen-recipient matched route-event slice inside existing contracts. Useful completion requires route-policy identity, exact source and delivered views, adoption/rejection evidence, downstream artifact/state checks, stale/corrupted controls, burden, and a no-route/manual-forwarding counterfactual—not merely a graph edge or higher endpoint score.

## Bottom line

Mycelium identifies a neglected and important unit of realistic knowledge work: a locally grounded claim reaching the qualified actor whose next decision it may change. Its active-context design usefully couples provenance, persistent hypotheses, recipient selection, and experiment planning. But v1 provides one author-run campaign, two reconstructed routing stories, one unexecuted downstream experiment proposal, and a post-hoc 26-item matrix comparing a week-long three-human–agent package with two single standalone runs. It neither isolates routing nor demonstrates tacit transfer, irreducibility, scientific correctness, realized experimental benefit, time savings, safe federation, or readiness. `skill-bench` should retain the route-event chain and test it with frozen recipient-state counterfactuals; it should not inherit the paper's stronger network-intelligence claims.