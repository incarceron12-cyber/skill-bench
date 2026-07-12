# HAS-Bench: configurable simulated participation is not identified human-participation evidence

## Source and review status

**Deep review of the complete immutable primary source.** I read the full 52-page arXiv v1 paper and checked claims against the preserved PDF. I found no official HAS-Bench artifact URL in the paper; its only repository link is LiteLLM. The paper says persona traces and raw outcomes are in a “released artifact” (p. 48), but that artifact could not be verified, so all implementation and result claims below remain paper-reported rather than release-audited.

- Paper: Yaozu Wu et al., *HAS-Bench: Evaluating LLM-Based Human-Agent Systems under Configurable Human Participation*, arXiv:2607.04329v1, https://arxiv.org/abs/2607.04329v1
- Immutable PDF: `data/papers/pdfs/2607.04329v1-has-bench.pdf` (52 pages; SHA-256 `d2c2cc688d99d7be262926eb1cbe0fc5f4fff622092eb4eaac0d572820df02bb`)
- Full text: `data/papers/text/2607.04329v1-has-bench.txt` (SHA-256 `57d27bc2c82de521b11d1a7edddc55077a696b9dc05efffb3737a7b76dc8e5fb`)
- Version read: v1, submitted 5 July 2026
- Date read: 2026-07-13
- Tags: human-agent systems, simulated users, authority, configured-system identity, intervention, process metrics

## One-sentence contribution

HAS-Bench supplies a useful graph and trace vocabulary for role-, permission-, information-, and authority-bearing participants plus clarification/feedback/control channels, but its main experiment compares autonomous agents with **LLM-simulated assistance under changed prompts, tools, information access, authorization, and interaction budgets**; it therefore measures configured synthetic collaboration treatments, not actual human participation, human burden, or causal uplift from a separable participation factor.

## Why this matters

This review advances charter objectives A, B, C, and E by separating the social role assigned to a participant from the participant's actual realization, and by turning human assistance into an auditable treatment rather than an untyped benchmark convenience. The reusable benchmark question is cross-domain: which information, authority, intervention, and burden changes produced an outcome, and what evidence licenses calling those changes human participation?

## Research question and claim boundary

The paper asks how to evaluate systems in which humans are active collaborators rather than passive task providers (pp. 1–3). It represents a scenario as task, participant graph, shared state, participant-specific observation/action spaces, transition function, human-participation policy, and evaluator (pp. 5–6). This is a strong conceptual correction to benchmarks that hide user behavior in a generic environment.

The evidence supports narrower claims:

1. the authors specify an inspectable vocabulary for participant nodes, typed edges, clarification/feedback/control events, agency policies, user personas, and trace-derived metrics;
2. they report constructing 397 adaptations from 301 retained tasks in τ²-Bench and MultiAgentBench across six domains (pp. 6–7, 21–27);
3. under one rollout per task, GPT-4.1-simulated users generally improve selected configured agent outcomes relative to an A1 condition, with substantial domain/model heterogeneity (pp. 8–13);
4. a 79-scenario human review finds high agreement about authored scenario quality, not behavioral parity between simulators and humans (pp. 35–37, 50–51).

It does **not** establish effects of real human participation, human–simulator equivalence, professional collaboration validity, causal value of “agency” as one factor, scalable expert substitution, human time/cognitive burden, calibrated safety, or cross-domain deployment readiness. The paper itself correctly states that its human study validates scenario artifacts rather than simulator–human behavioral parity (p. 50), but the abstract, RQ framing, metric names, and conclusions repeatedly call GPT-4.1 simulator events “human participation.”

## Methodology and system

### Scenario population and adaptation

The authors start with 2,749 tasks from τ²-Bench and MultiAgentBench, bucket/rank them for interaction richness and evaluability, and retain 301 base tasks. Selection is strongly outcome- and interaction-conditioned: tasks lacking reliable evaluation signals are removed, while tool diversity, role diversity, hidden information, and checkability increase rank (pp. 6, 21–23). Four LLM judges independently score six adaptation patterns for fit, evaluator feasibility, and injection risk. The prompt includes sensible public/private-field rules and forbids a process event from being the sole success criterion (pp. 23–26).

Adaptation then creates human roles, private information, permissions, relationships, and evaluation criteria. Automatic checks, LLM structural review, LLM worthiness review, and sampled human verification follow (pp. 27–37). The final 397 tasks exceed the 301 base pool because one source task can yield multiple pattern-specific adaptations, but the paper does not provide a full flow table from proposed adaptations through rejection, revision, duplication, and final inclusion. Nor does it report panel agreement for pattern assignment, model identities for the four construction judges, author review, or whether scenario outcomes were examined during revision.

The six patterns—information asymmetry, latent constraint, safety-critical authorization, multi-stakeholder specification, iterative verification, and dynamic goal revision—are useful primary labels but explicitly non-exclusive (pp. 20–22). Assigning one primary pattern supports stratification while losing compound-treatment structure.

### Graph, authority, and channels

A typed directed graph places agent and purported human nodes under participant-specific visibility, tools, responsibilities, permissions, and action spaces. Edges route communication, delegation, supervision, handoff, and intervention (pp. 4–6). Clarification acts on missing information before commitment; feedback evaluates an existing output; control determines whether, how, or by whom an action executes (pp. 5, 17–18). Classification by operational effect rather than surface utterance is the paper's best methodological idea.

However, the paper gives a YAML sketch rather than a verified released implementation. Relationship labels appear as free strings, and the appendix describes lifecycle and routing behavior without source evidence that permissions are enforced rather than prompted. More importantly, “human” nodes in all main outcome experiments are GPT-4.1-backed responder policies (p. 8). The graph semantics should therefore distinguish participant ontology (`real_human`, `simulated_persona`, `model_agent`, `scripted_policy`) from assigned social role. Calling a model-backed user a first-class human node launders behavioral provenance.

### Agency levels are treatment bundles

A1 disables channel tools and hides user nodes and C/F/C guidance. A3 registers all virtual tools, reveals available users, adds the full collaboration protocol, routes medium/high-risk control, and supplies simulator responses. A4 adds proactive input, changes the collaboration instruction, encourages engagement, and uses stricter/lower control thresholds (pp. 19–20).

Thus A1→A3 simultaneously changes:

- prompt and protocol;
- visible participants;
- available tools/actions;
- access to hidden task information and acceptance criteria;
- authorization and execution authority;
- number of model calls and effective inference budget;
- opportunity to receive answer-bearing critiques;
- failure and waiting paths.

A3→A4 changes unsolicited information timing, agent instructions, engagement policy, and control thresholds. These are legitimate configured-system comparisons, but they do not isolate “amount of human agency.” The paper's own A4 instantiation is one fixed proactive message at a fixed turn on Coding and Research, far narrower than its A4 definition of a human-led process (pp. 10–11, 19–20).

### Models, controls, and repetitions

Five agent backbones are evaluated with GPT-4.1 as default user simulator and judge. Temperature is zero, with one rollout per task (p. 8). A1 and A3 use the same base task but not the same information/action interface. Service and bargaining tasks are structurally ill-defined without user interaction, yet they remain in the main A1–A3 table; the authors exclude those domains only from the cleaner agency sweep (pp. 8–10). Consequently some “rescue” reflects restoring information deliberately withheld from an invalid or disadvantaged baseline rather than recovery of a task a comparably informed autonomous agent failed.

The 60-task simulator study varies user-simulator backbone and preserves positive A3–A1 point differences, but simulator choice changes Pass@1 by up to 13.3 points for GPT-4.1 agents (pp. 49–50). This demonstrates simulator sensitivity, not robustness to humans. GPT-4.1 is also agent, default simulator, and judge in central cells, creating family-dependent interaction and evaluation channels.

### Outcomes and process observers

Outcome metrics include single-run Pass@1, equal-weight average Task Score dimensions, Delivery Rate, registry-based protected-action Safety Rate, and HAS Rescue Rate conditional on A1 failure (pp. 7, 37–39). Process metrics include judged clarification quality, feedback uptake, control-request justification, action safety, initiative entropy, Human Intervention Rate, turns, tool calls, steps, and tokens (pp. 39–47).

Several distinctions are valuable:

- event coverage is reported separately because CQS/FUR/CRJ are undefined when no event occurs;
- final-state Safety Rate is separated from trace-level ASR;
- HIR is explicitly descriptive rather than beneficial;
- recovery denominators are distinguished from safety denominators;
- A4 harm is counted, not hidden.

But the observers remain under-validated. Task Score's natural-language judge sees transcripts and outputs, not necessarily authoritative environment state or executable artifacts. FUR labels behavioral adoption within five steps, not whether feedback was correct or improved the outcome. CQS rewards asking against `user_known_info`, potentially measuring criterion-aware elicitation. CRJ's generic normative rubric may conflict with domain policy. ASR defaults to safe absent clear evidence and uses a different observer than deterministic Safety Rate. Initiative entropy treats equal initiative as descriptively high even when one participant should retain authority. HIR counts simulator steps, not human minutes, attention, interruptions, effort, expertise, or opportunity cost.

Appendix C.8 gives a **plan** for auditing 600 judged items with two labels plus adjudication and appropriate agreement metrics (pp. 51–52), but reports no results. Scenario-level agreement in Table 13 cannot validate outcome/process judges. Claims that judged metrics are safeguarded or calibrated are therefore premature.

## Evidence

The main A1–A3 table reports average gains of 8.4 Pass@1 points, 11.5 Task Score points, and 26.9 safety points, but variation is large: GPT-4.1 Research improves 53.3 Pass@1 points while GPT-4.1 Airline falls 6.5; DeepSeek Telecom falls 5; Llama averages essentially no gain (pp. 9–10). No uncertainty intervals accompany this full table.

The Coding/Research GPT-4.1 sweep reports A1→A3→A4 gains and task-bootstrap intervals in Figure 2; A4 rescues 27 A3 failures and breaks 13 A3 successes (pp. 10–11). The 13 harms are classified by the same general evaluation machinery as seven premature and six distracting/redundant interventions, with no human-coded protocol or uncertainty (p. 47).

Single-channel ablations show that Full is not uniformly best: in five of six patterns the strongest single channel beats Full on the chosen natural metric (pp. 11–12). This supports an over-collaboration hypothesis but does not identify channel causality cleanly: enabling a channel changes prompts/tools and observed trajectories; recovery is conditioned on A1 failures; channel opportunities differ; and selected “natural metrics” differ across rows.

Persona max–min ranges are large in Bargaining, Coding, and Research (pp. 12–13), but each persona packages assertiveness, cooperativeness, patience, expertise claims, preferences, disclosure policy, and response content. There are only three hand-authored personas per domain and one run each. The result establishes sensitivity to three simulator prompts, not variability across people.

Four reviewers each assess roughly 59–60 of 79 scenarios, with three labels per scenario. The reported mean is 18.1/20, pass rate 91.1%, exact agreement .78, and majority agreement .97 (pp. 36–37, 50). Reviewer recruitment, expertise, domain assignment, independence from authorship, training, compensation, blind status, and per-dimension disagreement are absent. Majority agreement is mechanically permissive with three raters; no chance-corrected or hierarchical reliability is reported. Unresolved cases are discussed, but adjudication lineage and changed labels are not shown.

## Unique insight

The durable contribution is an **authority-bearing participation event**, not a five-level agency score. Every intervention should be represented as:

`participant realization → assigned role → observation basis → permitted channel → initiation/trigger → information or proposed action → decision right → response/action → agent uptake → environment consequence → burden → observer`

This chain exposes four separable questions that HAS-Bench partly conflates:

1. **Availability:** Could a participant be contacted or act?
2. **Exercise:** Did the participant provide information, feedback, authorization, veto, takeover, or execution?
3. **Uptake:** Did the agent respond, and was the contribution adopted correctly?
4. **Effect:** Did that contribution improve quality/safety relative to a valid matched counterfactual, at what burden?

A graph edge proves availability, a trace event proves exercise, FUR may indicate uptake, and paired randomized/repeated evidence is needed for effect. None establishes that a simulator models a real person. Likewise, “more agency” is not ordinal unless information, tools, authority, initiative, and burden move on a defensible common scale; in this implementation they are a policy bundle.

## Limitations and validity threats

1. Main “human” participants are LLM simulators; no real humans perform benchmark tasks.
2. Human review validates sampled scenario descriptions, not simulator behavior, collaboration outcomes, or judge labels.
3. The planned 600-item human audit of judged quantities has no reported results in v1.
4. No official benchmark/results artifact could be verified, despite a release claim.
5. A1→A3 changes prompt, tools, visible users, hidden information, authority, and budget simultaneously.
6. Several A1 service/bargaining tasks lack a meaningful autonomous specification, biasing rescue and uplift interpretations.
7. A3→A4 also changes prompts, proactive timing, engagement encouragement, and control thresholds.
8. A4 is a fixed one-shot intervention, not a general agent-assisted or human-led workflow.
9. A2 and A5 are defined but not evaluated.
10. One rollout per cell provides no within-task stochastic reliability.
11. The main per-domain table has no intervals, paired tests, model/task clustering, or multiplicity control.
12. Task selection favors interaction richness and evaluator availability; the inference population is not professional work.
13. Construction relies heavily on LLM assignment/review, with no released panel agreement or revision flow.
14. The final 397 tasks' relation to 301 bases is not accompanied by a full lineage/rejection inventory.
15. Scenario reviewers' expertise, independence, recruitment, training, and per-dimension reliability are unspecified.
16. Process judges share GPT-4.1 with the default simulator and some evaluated-agent cells.
17. FUR measures apparent adoption, not feedback correctness, necessity, causal use, or outcome benefit.
18. CQS/CRJ/ASR require normative ground truth not validated against domain experts.
19. HIR and tokens are not measures of actual human cost or burden.
20. Initiative entropy has no demonstrated relationship to appropriate authority allocation or outcome utility.
21. Equal-weight Task Score dimensions are not calibrated for dependency, severity, or professional utility.
22. Rescue Rate conditions on observed A1 failures and one paired realization; regression-to-noise and changed interfaces remain.
23. Persona ranges use only three bundled prompts per domain and cannot support population generalization.
24. The simulator sensitivity study shows sign stability on 60 selected tasks, not human parity or magnitude stability.
25. The same judge evaluates outputs produced with and without answer-bearing simulator feedback, leaving criterion-cue dependence possible.
26. Permission enforcement, event expiry/failure semantics, multiple-human conflict resolution, unavailable humans, latency, malicious input, and escalation behavior are described incompletely or not tested.
27. Costs omit real-human latency, scheduling, training, cognitive load, accountability, and privacy.
28. Adaptations may introduce authored hidden requirements that create the apparent need for participation rather than sample naturally occurring dependence.

## Reproducibility and operational realism

Reproducibility is weak despite unusually extensive appendix prompts. The paper provides task schema, construction/review prompts, channel semantics, metric formulas, judge prompts, counts, and tables. It does not provide a verifiable HAS-Bench release URL, exact scenario files, framework code, run configuration, raw traces, raw judge outputs, model snapshots, API dates, seeds, result inventory, costs, or a replay command. The LiteLLM link is a dependency, not benchmark evidence.

Operational realism is mixed. Hidden information, protected writes, iterative review, multiple stakeholders, goal changes, and stateful tools resemble real collaboration. Yet synthetic personas respond instantly, consistently, and at token cost; real participants have variable expertise, incomplete context, incentives, fatigue, privacy constraints, availability, and accountability. The benchmark models channels and authority more realistically than it models people.

## Relation to existing skill-bench evidence

- **AgentCoop** shows that typed edges do not prove semantic handoff or causal repair. HAS-Bench adds participant authority and intervention channels, but similarly needs receiver uptake and downstream consequence evidence rather than graph declarations alone.
- **TheAgentCompany** shows simulated coworkers are versioned stochastic environment interventions. HAS-Bench improves configurability and process instrumentation, but does not establish simulator–human parity or occupational validity.
- **Expert participation and disagreement reviews** require real contributor identity, authority, consent, independent labels, and adjudication lineage. A persona prompt cannot inherit those properties.
- Existing configured-system, trace, metric, task-health, and validity contracts already provide homes for these requirements; HAS-Bench does not justify a separate human-agent subsystem.

## Transfer to skill-bench

1. **Add participant realization to configured-system identity.** Record whether each social-role node is a real human, model simulator, scripted policy, hybrid, or replay; pin model/prompt/profile/private state/sampling and prohibit the label `human` from implying realization.
2. **Treat participation settings as factorial treatment vectors, not ordinal labels.** Separately version prompt, visible participants, channels/tools, information access, action authority, initiative trigger, control threshold, budget, and observer. Estimate only contrasts that hold the rest fixed.
3. **Represent authority-bearing events end to end.** Preserve initiator, target, trigger, observation basis, requested decision/action, scope, response, latency, expiry/failure, uptake evidence, environment consequence, burden, and grader view.
4. **Separate availability, exercise, uptake, and effect.** A channel-enabled run is not an intervention; an intervention is not uptake; uptake is not beneficial effect.
5. **Require valid autonomous counterfactuals.** Do not call restoration of deliberately withheld indispensable information a capability rescue. Compare against matched conditions such as disclosed-equivalent information, oracle information, simulator channel, real-human channel, and no-assistance where each task remains well-defined.
6. **Measure burden as plural evidence.** Keep simulator steps/tokens separate from real-human active minutes, waiting time, interruption count, cognitive demand, expertise level, correction work, privacy exposure, and decision accountability.
7. **Fail closed on judge calibration.** A planned human audit is not calibration evidence. Store independent labels, disagreement, adjudication, uncertainty, evidence views, and per-metric error before licensing process scores.
8. **Do not collapse process desirability.** Clarification, feedback, authorization, initiative, safety, uptake, outcome, and burden should remain separate; appropriate collaboration may be asymmetric and low-interaction.
9. **Use compound patterns.** Preserve multiple concurrent reasons for participation and test interactions rather than forcing one primary label into causal interpretation.
10. **Validate real participation before human claims.** A future pilot should randomize or counterbalance a small set of consented contributors across matched tasks/settings, repeat tasks or use equivalent forms, record burden and latency, and compare simulator behavior/outcome sensitivity without treating either as ground truth.

## Concrete repository actions

No new queue task is added. The evidence is nonduplicatively absorbed by existing machinery and pending consolidation:

- configured-system records should carry participant realization and the full participation-policy vector;
- trace/metric contracts should distinguish participation availability, event exercise, uptake, effect, and burden;
- validity arguments should explicitly exclude human-participation and professional-collaboration claims for simulator-only trials;
- expert participation/disagreement records should remain separate from benchmark user-simulator nodes.

## Bottom line

HAS-Bench materially improves the vocabulary of collaboration evaluation: humans or simulators should not be an untyped chat endpoint, and clarification, feedback, control, authority, initiative, uptake, safety, and burden should be observable separately. Its v1 evidence does not yet match that conceptual ambition. The central experiments are single-run comparisons among bundled prompt/tool/information/authority treatments using model-backed users and mostly model-backed process observers, while the only completed human study reviews scenario artifacts. For `skill-bench`, retain the graph, channel semantics, authority-bearing events, event-conditioned denominators, and explicit over-collaboration harms; repair participant provenance, treatment identification, real-human burden, judge calibration, and claim licensing.