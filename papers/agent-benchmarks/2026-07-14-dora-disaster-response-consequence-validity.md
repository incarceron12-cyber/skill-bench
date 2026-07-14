# Paper Review: DORA — Real Disaster Imagery Does Not Make a Tool-Pipeline Score an Operational-Response Outcome

- **Paper:** https://arxiv.org/abs/2605.11633v1
- **Authors:** Junjue Wang, Weihao Xuan, Heli Qi, Pengyu Dai, Kunyi Liu, Hongruixuan Chen, Zhuo Zheng, Junshi Xia, Stefano Ermon, Naoto Yokoya
- **Date read:** 2026-07-14
- **Source:** complete immutable arXiv v1, submitted 12 May 2026
- **Local PDF:** `data/papers/pdfs/2605.11633v1-dora-disaster-response-agent.pdf` (13 pages; SHA-256 `652e5163f6bac362bd9a260edda2d51851c302476cfc6aec5817102a0cba6942`)
- **Local text:** `data/papers/text/2605.11633v1-dora-disaster-response-agent.txt` (SHA-256 `b547cb591d4cb1a933bdbb0ea57a279d69652a2d8da00232fc96a15a225a3319`)
- **Immutable source:** `data/papers/source/2605.11633v1-source.tar.gz` (SHA-256 `82b106bc8e75797129ee3c0990158d2cc0f4a50433bcc172e2dcaaf5e775b801`); provenance: `data/sources/releases/2605.11633v1-dora/provenance.json`
- **Release boundary:** v1 says both that the authors “design and release” the tool library (p. 2) and that they “will release” all data, tools, and protocols (p. 10). The manuscript has no artifact URL, and renewed exact-title/ID searches found no verifiable author-owned DORA release. The source archive contains the main TeX, bibliography, class, and figures, but none of the repeatedly cited Appendices C–H.
- **Tags:** disaster-response, geospatial-agents, tool-use, gold-trajectories, consequence-validity, expert-authoring, multimodal-artifacts

## One-sentence contribution

DORA proposes a substantial closed-world geospatial-agent instrument—515 authored queries over 45 historical disaster events, 108 typed tools, approximately 3,500 reference calls, and deterministic typed endpoint scoring—but its unique lesson is also its central validity warning: real imagery and operational vocabulary can coexist with vague expert authority, one outcome-derived witness pipeline, uncalibrated endpoint tolerances, unreleased evidence, and no observation of safe or effective emergency response.

## Why this matters for skill-bench

DORA advances charter objectives A and B through a high-consequence version of the project's central question:

> What evidence is required before successful evidence fusion, routing, resource calculation, or report production can be interpreted as competent and safe operational knowledge work rather than agreement with an authored analytical package?

The benchmark is a useful stress test because it joins several structures that simpler agent benchmarks isolate: heterogeneous raster/vector evidence, model-backed perception, spatial operations, temporal loops, routes and facilities, resource calculations, and report artifacts. It also exposes why **ecological resemblance is not consequence validity**. The event may be real, yet the evaluated episode remains an offline reconstruction over selected historical layers, fixed tools, an authored query, a single reference answer, and no incident-command decision, field execution, affected-party review, or downstream outcome.

The transferable object is therefore not a disaster-specific schema. It is a cross-domain **analysis-to-consequence ladder**:

```text
source event and valid-time provenance
→ qualified role, mandate, and affected-party authority
→ public operational requirement and uncertainty state
→ admissible evidence and tool semantics
→ accepted analytical/decision alternatives
→ protected constraints and escalation/abstention policy
→ artifact and intended recipient
→ attempted and realized action
→ immediate and downstream consequence
→ bounded interpretation and decision
```

DORA directly observes selected middle links. It does not observe or validate the later ones.

## Research question and defensible claim boundary

The paper asks whether frontier LLM agents can compose heterogeneous geospatial tools to answer disaster-response queries spanning perception, spatial relations, operational planning, temporal evolution, and multimodal report synthesis (Sections 1, 3, and 4, pp. 1–10).

The strongest defensible claim is:

> On the authors' unreleased 515-task historical geospatial package, the reported ReAct configurations achieved lower agreement with GT-derived typed reference answers than an expert-authored tool-order oracle using the same model-backed perception layer; tool-order hints improved trajectory similarity much more than endpoint accuracy for three tested models, and one Gemma configuration showed small endpoint changes under three alternative scaffolds.

The evidence does **not** establish that:

- the 515 tasks sample emergency-response work, incidents, regions, affected populations, or decision consequences representatively;
- the unnamed experts had authority for each requirement, operational constant, route constraint, report convention, or acceptable response;
- the cited UNOSAT, Copernicus, FEMA, and OCHA materials entail each task, tool sequence, threshold, or answer;
- the single authored trajectory is necessary, sufficient, safe, optimal, or alternative-complete;
- the structured endpoint thresholds correspond to acceptable operational error;
- the generated route, allocation, map, or report would be usable by an incident commander or improve a real response;
- the reported failure labels isolate disaster knowledge rather than tool documentation, interface, perception, data, or scorer failures;
- trajectory length or tool heterogeneity causally produces the observed score gaps;
- the numerical tables are reproducible, statistically reliable, or stable across repeats;
- DORA validates professional capability, safe evacuation, operational reliability, production fitness, or readiness.

## Methodology and system

### Event and task frame

DORA aggregates 2,850 remote-sensing images and 460 vector layers from ten named source families into 45 disaster events on five continents (Figure 2, pp. 3–4). The sources include xBD, DisasterM3, BRIGHT, NAIP, Maxar Open Data, Landslide4Sense, GVLM-CD, Planet, RescueNet, CRASAR-U-DRoIDS, OpenEarthMap/JMA, OpenStreetMap, and Our World in Data. The paper reports ten event types, but the distribution is purposive and highly uneven: the figure lists 15 landslides and only one each for tsunami, explosion, and heat island. It provides no event inclusion frame, exclusion log, geographic/population weighting, date snapshot for mutable social layers, or task-per-event clustering table.

A task is `(Q, D, T*, A*)`: natural-language query, heterogeneous data manifest, expert-verified tool trajectory, and structured answer (Section 3.2, pp. 4–5). Inputs declare modality, GSD, coordinate system, bands, and paths; outputs use scalar, string, point, line, polygon, set, or dict fields. The five dimensions progress from perception (T1) through spatial analysis (T2), planning (T3), temporal reasoning (T4), and report synthesis (T5), with average authored paths from 3.35 to 11.96 calls (Figure 5, pp. 5–6).

This is a coherent package format, but it does not establish the claimed operational hierarchy. Coarse citations to international frameworks show that damage mapping, spatial analysis, decision support, temporal monitoring, and reporting exist in practice. The manuscript supplies no task-level clause, expert statement, authority, incident record, or recipient need linking an individual question and threshold to those frameworks. For example, the illustrated debris-clearance answer assumes “each car clears 10 m² per hour,” and the route example optimizes shortest undamaged path to a facility (Figure 1, p. 2). Such supplied constants and objectives create executable arithmetic; they do not establish equipment productivity, road traversability, facility capacity, equity, safety, authorization, or field feasibility.

### Tool library and environment

The reported 108 MCP tools comprise 31 perception, 18 raster, 31 vector, 15 logical, 11 visualization, and two fixed summarization tools (Table 2, p. 6). The architecture is valuable: typed JSON-RPC boundaries make tool name, argument, result, and dependency failures observable. The authors train perception models only on public training splits and create tasks from held-out test splits (p. 6), which addresses one narrow supervised perception leakage path.

It does not establish broader non-leakage or environment validity. Public test imagery and task-derived metadata may be exposed elsewhere; task and trajectory authors know the tools and answers; no model pretraining/exposure audit is reported; and the exact tool descriptions, versions, weights, dependencies, prompts, filesystem policy, network policy, data licenses, and runtime snapshots are absent. “Any MCP-compatible framework” is not automatic comparability: adapter prompts, tool rendering, schema coercion, error handling, context limits, and retry policy remain treatment components.

The fixed summarization backend also changes the construct. If a shared tool extracts evidence and renders narrative, report quality partly belongs to the environment rather than the evaluated model. The paper does not specify what that backend contributes, which report content is model-authored, or how unsupported assertions, omissions, visual legibility, uncertainty communication, and recipient usability are checked.

### Expert authoring and gold construction

The three-stage annotation pipeline is:

1. unnamed “domain experts with remote-sensing and disaster-management backgrounds” write `Q` and a symbolic `T*`, including tool purposes and arguments;
2. a deterministic replay engine resolves dependencies, substitutes human-annotated ground-truth masks for perception calls, and executes downstream code to create `A*`;
3. an unspecified process cross-validates question–answer alignment, zero unknown types, and numerical sanity (Section 3.4, pp. 6–7).

This is the paper's most important construction mechanism: one symbolic plan is compiled into a numerical witness. But the evidence lineage is incomplete. The paper reports no expert count, identities, role split, qualification criteria, task allocation, independent review, disagreement, adjudication, correction rate, time, compensation, conflict policy, task rejection, or approval scope. The acknowledgment thanks one person for disaster-response guidance; it does not identify who authored or approved 515 tasks. Figure 6 labels quality control “AI-Assisted Evaluation,” while the prose says “systematic cross-validation,” with no description of the AI, human oversight, held-out checks, or error results.

More fundamentally, the reference is **outcome-derived from one authored analytical path**. The GT-mask substitution makes downstream arithmetic internally stable, but it does not validate the query, operational assumptions, selected evidence, path completeness, or alternatives. The authors acknowledge that multiple trajectories can be valid and make final answers primary (p. 7), yet they report no accepted alternative answers, equivalence policy, alternative route/allocation witnesses, uncertainty interval, abstention/escalation outcome, or adversarial false-accept/false-reject tests.

There are two different “gold” systems:

- annotation gold uses human GT masks to produce `A*`;
- the reported Gold Trajectory uses the authored order and arguments but model-backed perception, scoring only 80.48% against `A*` (Table 4, p. 7).

That 19.52-point deficit is informative: even the canonical plan is not sufficient when perception is imperfect. It also means “agent-to-gold” compares planning configurations under a shared but fallible perception package, not agents against operational truth. Gold-path agreement and answer agreement should remain separate from perception validity and downstream consequence.

### Scoring and aggregation

Trajectory metrics compare one predicted path to `T*`: tool-set recall, LCS-normalized order, matching-prefix length, and per-step argument match conditioned on the correct tool name (p. 7). They are useful diagnostics for the authored witness, not procedure-fidelity scores. Tool-set recall omits precision; prefix/LCS can penalize legitimate reordering or alternative tools; argument accuracy has a selected denominator; and none captures whether an intermediate action was unsafe, an observation was ignored, or an alternative path was valid.

Final fields reduce to four predicates (Table 3, p. 7):

- scalar within 20% relative error;
- normalized exact string;
- point within 20 pixels;
- polygon IoU at least .5.

Sets use string F1, lines use start/end/length, dicts average over key union, and report summaries are reduced to extracted key statistics and categories. These choices are not calibrated against responder decisions. A 20-pixel gate ranges from roughly 0.3 m at 1.5 cm GSD to 200 m at 10 m GSD if applied in native pixels; the paper does not state reprojection or physical-unit normalization. Relative error at a zero gold scalar collapses to exact equality. A .5 polygon IoU can admit materially different affected areas. Equal averaging lets dependent keys and low-consequence fields compensate for critical failures. Route endpoints and length do not establish road feasibility or collateral risk. Extracted report facts do not establish evidence provenance, uncertainty, legibility, prioritization, actionability, or absence of unsupported recommendations.

Efficiency is `|T*| / max(|Tpred|, |T*|)`. It rewards brevity relative to one witness even when the answer is wrong and cannot distinguish redundant recovery, necessary alternative work, skipped safety checks, or cheap premature stopping. It should not be interpreted without correctness, validity, and cost.

The paper does not define whether task scores are macro-averaged over fields, tasks, dimensions, events, or disaster types beyond the table labels. There is no dependency/cascade adjustment, event-clustered uncertainty, missing/invalid denominator, tool-failure disposition, or threshold sensitivity.

### Configured systems and interventions

Table 4 reports 13 ReAct model configurations, including five commercial and eight open-source systems, plus two tool-free VLM baselines and the Gold Trajectory (pp. 7–8). The paper names model families but omits exact service snapshots for several future-facing endpoints, prompts, tool schema presentation, context and step budgets, temperature, seeds, retries, timeouts, invalid-call policy, hardware, quantization, endpoint dates, rate failures, and run counts. No repeated trials, confidence intervals, usage, or cost are reported. Latency appears only for the Gemma scaffold ablation.

The tool-free VLM comparison is not a controlled estimate of tool value: those systems receive raw imagery and question but no tools, and apparently lack the vector, route, POI, and derived-state channels needed by many tasks. The comparison shows that an image-only interface performs poorly on a tool-required package; it does not isolate visual reasoning from tool composition.

The instruction-following intervention gives three models the gold tool order but requires them to infer arguments. It sharply raises path similarity and raises endpoint accuracy only 1.08–4.40 points (Table 5, pp. 8–9). This is useful evidence that order alone is insufficient within this package. It does not isolate “argument grounding”: residuals include perception errors, file/state references, output parsing, tool errors, scorer failures, and answer formatting.

The scaffold ablation compares ReAct, Plan-then-Execute, Reflexion, and ReWOO only for Gemma-4-31B (Table 6, p. 9). Plan-then-Execute gains 3.24 points while adding 99 seconds/task; Reflexion gains 1.57 while adding 87 seconds; ReWOO loses 6.91. With no repeats or uncertainty, these are descriptive configured-package differences, not stable scaffold effects.

## Evidence and results interpretation

### Main reported results

The Gold Trajectory scores 80.48% against GT-derived answers. The strongest reported agent, Gemini-3.0-Flash, scores 53.74%; Qwen3.5-397B-A17B scores 53.45%; other tool-enabled systems range from 24.01% to 52.89% (Table 4, p. 7). T5 report synthesis is generally lower than T4 temporal reasoning, while the model-backed gold is highest on T5. These results support a bounded observation: model configurations often fail to reproduce reference endpoints even when supplied the same tool ecosystem.

The manuscript promotes stronger explanations than the design licenses:

- **“Tool heterogeneity is dominant.”** T5 differs simultaneously in path length, output type, tool count, tool categories, report backend, and likely task/event mix. No matched intervention changes heterogeneity while holding those factors fixed.
- **“Length causes compositional decay.”** The five path-length bins contain 109, 150, 92, 94, and 70 tasks, but length is authored after task selection and confounded with dimension, modality, output, and event. A rising model-backed gold ceiling does not remove those confounds. No within-task length manipulation or clustered regression is reported.
- **“Agentic post-training matters more than parameter scale.”** One 31B model outperforming GPT-OSS-120B cannot isolate parameter scale from data, architecture, quantization, serving, prompts, or tool training.
- **“Unique disaster-domain failure modes.”** Wrong masks, stale indices, raster/vector confusion, missing intersections, and bad references may be especially consequential here, but they are also generic representation, type, dependency, and tool-interface errors. Domain uniqueness requires matched non-disaster controls.

### Failure analysis

Figure 7 reports damage-semantic grounding (20.3%), sensor-modality mismatch (14.8%), and disaster-pipeline composition (56.3%), with subcategories such as stale indices, raster/vector replacement, wrong upstream references, missing spatial tools, and wrong phenomenon tools (p. 8). The manuscript does not state the sampled runs, total errors, unit of annotation, who labeled them, whether labels are multi-label, whether categories are exhaustive, how disagreements were handled, or whether percentages are task-, call-, or failure-weighted. The figure legend allows shared categories, but no overlap table is provided. These numbers are useful hypotheses for diagnostic fixtures, not prevalence estimates or root-cause rates.

Several labels also mix root and surface. A wrong upstream reference could originate in prompt/schema ambiguity, state tracking, a prior perception error, path serialization, or model reasoning. A missing intersection can be a planning omission or a valid alternative if another tool computes the same relation. “Damage-semantic grounding” may reflect undocumented class-index conventions. Root cause requires observer evidence plus intervention or adjudication, not taxonomy assignment from the terminal trace alone.

### Missing appendices and release evidence

The immutable paper repeatedly delegates decisive details to Appendices C (tool implementation and perception accuracy), D (quality control), E (agent implementation), F (LLM/human scoring), and H (failure examples). The 13-page PDF ends after references. The complete immutable source has one 702-line main TeX file and no appendix input, supplement, or appendix sections. The claims are therefore absent from the primary record actually available:

- tool/perception accuracy and version details;
- quality-control protocol and outcomes;
- prompts, budgets, retries, and execution details;
- LLM-judge and human scoring protocol, sample, agreement, and results;
- complete failure examples and labeling method.

Renewed exact-title and arXiv-ID searches on 14 July found only arXiv and third-party paper pages, not an author-owned DORA package. The manuscript/source contain no project URL. Without tasks, manifests, tools, GT masks, trajectories, prompts, outputs, grader records, or analysis, none of the empirical tables can be replayed or audited.

### Supported, partial, and unsupported claims

**Supported by manuscript evidence:** DORA specifies a coherent task tuple and typed tool/answer vocabulary; historical multimodal data can be assembled into longer geospatial workflows; one authored order is insufficient to overcome model-backed perception; reported order hints improve path agreement more than endpoint agreement; selected configured systems have low reference-answer agreement.

**Partially supported:** expert and framework grounding are asserted but lack task-level authority lineage; held-out perception splits reduce one leakage route but not benchmark exposure; deterministic replay supports one witness but not alternatives or operational correctness; failure categories are plausible but lack protocol and denominators.

**Unsupported:** representative disaster operations; safe or useful evacuation/resource decisions; causal length/heterogeneity explanations; calibrated error tolerances; failure prevalence; cross-framework comparability; human/LLM grader validity; reproducibility; professional capability; operational reliability; safety; production fitness; readiness.

## Unique insight

DORA's deepest transferable insight is the distinction between an **analytical witness** and a **consequence-bearing plan**.

An expert-authored pipeline plus deterministic replay can show:

```text
these selected inputs + this tool configuration + this path
→ this reference artifact
```

It cannot by itself show:

```text
this was the authorized evidence at decision time
→ the requirement and assumptions were operationally legitimate
→ the plan was safe among feasible alternatives
→ the intended recipient could act on it
→ action occurred without prohibited side effects
→ people or infrastructure benefited
```

This yields five cross-domain design rules:

1. **Historical reality attaches to sources, not automatically to tasks or consequences.** A real flood image can support source realism while the question, constants, route objective, answer, and use remain synthetic.
2. **GT compilation is an instrument-construction intervention.** Replacing perception with annotated masks produces stable downstream references but changes the evaluated system and can hide uncertainty that a responder would face.
3. **A gold trajectory is a witness path, not a safe policy.** Alternatives, abstention, escalation, protective constraints, and recipient authority need explicit representation and falsification.
4. **Endpoint distance must be decision-calibrated.** Pixel, IoU, scalar, and string tolerances are only operationally meaningful when tied to map scale, affected population, route feasibility, threshold loss, and downstream decisions.
5. **Consequential work needs a state/outcome observer beyond the artifact.** A route file or situation report is an intermediate product. Evaluation must observe recipient uptake, attempted/realized action, protected-state preservation, collateral effects, and outcome uncertainty before promoting the claim.

## Limitations and validity threats

1. The 45-event frame is purposive, uneven, and lacks inclusion/exclusion or population inference.
2. Tasks nested in shared events, imagery, tools, and templates are treated without clustered uncertainty.
3. Mutable OSM, population, weather/temperature, and other social layers lack task-level snapshot and valid-time records.
4. Source licenses and redistribution constraints are not mapped to the promised package.
5. “Expert” count, identities, roles, qualifications, task allocation, independence, review, disagreement, adjudication, and time are absent.
6. Framework citations are dimension-level resemblance, not task-level requirement or threshold provenance.
7. No responder, incident-command, facility, community, or affected-party validation is reported.
8. Operational constants, objectives, and constraints may be author-supplied simplifications rather than field-authorized rules.
9. GT-mask answer construction suppresses perception uncertainty and creates a different system from evaluated agents.
10. Model-backed Gold Trajectory reaches only 80.48%, so canonical order is not a perfect-answer or operational oracle.
11. One witness trajectory does not establish necessity, safety, optimality, or alternative completeness.
12. No accepted alternative answers, routes, allocations, tools, partial orders, abstentions, or escalations are represented.
13. Trajectory metrics compare against one path and can penalize legitimate alternatives.
14. Tool-set recall omits extra-tool precision; argument accuracy conditions on correct tool names.
15. Efficiency rewards short wrong/unsafe attempts and is tied to one witness length.
16. Scalar, pixel, IoU, string, and composite thresholds are uncalibrated against operational decisions.
17. The 20-pixel point gate has radically different physical meaning across the stated 0.015–10 m GSD range unless normalized; normalization is not specified.
18. Report scoring reduces free text to extracted facts/categories and omits provenance, uncertainty, legibility, recipient utility, and unsupported advice.
19. Fixed summarization tools may perform part of the evaluated synthesis construct.
20. No observer checks unsafe intermediate actions, protected constraints, collateral state, or realized consequences.
21. Exact model/service snapshots, prompts, tool descriptions, budgets, temperature, seeds, retries, invalids, timeouts, and hardware are missing.
22. No repeat runs, confidence intervals, sensitivity analyses, or cost accounting are reported.
23. Tool-free VLM baselines have a different and structurally insufficient evidence/action interface.
24. Order-hint residuals cannot be attributed solely to argument grounding.
25. Scaffold differences are one-model, single-point configured-package comparisons.
26. Length, modality, dimension, event, output type, and tool heterogeneity are confounded.
27. Rising gold accuracy by length does not identify agent-side causal decay.
28. Failure-mode sampling, labeling, overlap, denominator, agreement, and adjudication are absent.
29. Failure labels conflate surface symptoms with root cause.
30. Public held-out dataset splits address one training leak but not task exposure, authoring leakage, or model pretraining.
31. The PDF/source omit Appendices C–H despite depending on them for tool, QC, harness, judge, human, and failure-analysis details.
32. The promised empirical release is not verifiable, blocking task, tool, trajectory, score, and analysis inspection.
33. The manuscript contradicts itself about whether the tool library is already released.
34. No evidence supports professional validity, operational reliability, safe evacuation, capability, production fitness, or readiness.

## Reproducibility and operational realism

Reproducibility is **low**. The immutable PDF, full extraction, TeX, figures, formulas, aggregate tables, and references are preserved. The task tuple and scoring atoms are described well enough to understand the intended design. Exact reproduction is blocked by absent tasks, event manifest, data snapshots, licenses, GT masks, tool code/weights/schemas, reference trajectories, quality-control records, prompts, model snapshots, run traces, invalid/tool-error ledger, report grader, human/LLM judgments, results, and analysis code. The missing appendices make even manuscript-only reconstruction incomplete.

Operational realism is **moderate at the source/interface layer and low at the authority/action/consequence layers**. Real historical imagery, varied sensors, GIS operations, paths, facilities, temporal scenes, and report formats are meaningful ingredients. But the environment is a retrospective closed-world analytical package. It does not model live sensor latency and uncertainty, stale/conflicting feeds, communications, incident command, legal jurisdiction, resource availability, facility capacity, accessibility, equity, community knowledge, changing hazards, field feedback, authorization, handoff, or action outcomes. Calling outputs “decision-ready” and the platform “reliable” is therefore aspirational.

## Transfer to skill-bench

### Preserve

1. **Typed heterogeneous manifests:** modality, resolution, CRS, bands, source identity, and vector/raster roles should be explicit.
2. **Executable dependency traces:** symbolic output references make upstream/downstream failure propagation inspectable.
3. **Plural endpoint types:** scalar, set, geometry, route, timeline, visualization, and report require different observers.
4. **Separate path and endpoint observations:** one can diagnose plan/tool/argument failures without making path similarity the primary construct.
5. **Imperfect reference execution:** run canonical witnesses through the actual environment to expose tool/perception ceilings rather than assuming they pass.
6. **Matched intervention ideas:** order hints and scaffold changes are useful if repeated, fully configured, and interpreted narrowly.

### Repair

1. **Bind each task to an authority graph.** Preserve source snapshot/valid time/license; expert role and scope; framework clause or incident evidence; requirement, assumption, threshold, and transformation; reviewer disposition; and intended recipient.
2. **Separate three oracles.** Keep source/label truth, one analytical witness, and operational acceptability distinct. A GT mask is not a plan oracle; a plan witness is not a consequence oracle.
3. **Represent alternatives and abstention.** Store reviewed sufficient paths/answers, partial-order constraints, prohibited actions, escalation triggers, uncertainty states, and observer-insufficient outcomes.
4. **Calibrate geometry and numerical tolerances.** Express distance in physical/decision units, test boundary cases, and tie thresholds to consequence or reviewer loss rather than convenience.
5. **Grade reports plurally.** Check evidence provenance, uncertainty, unsupported claims, visual integrity, priority, recipient usability, accessibility, and contradictions separately from factual field agreement.
6. **Add a consequence ledger.** Record intended recipient/action, authorization, attempted versus realized state, protected constraints, collateral changes, affected stakeholders, and whether outcomes are simulated, expert-projected, or observed.
7. **Diagnose root versus surface.** Preserve raw tool request/result and environment validity; use interventions or qualified adjudication before naming domain knowledge as root cause.
8. **Estimate at the right cluster.** Report task, event, disaster-type, modality, and tool-family denominators; repeat stochastic runs; cluster uncertainty by shared event/task package.
9. **Freeze configured-system identity.** Hash prompt, scaffold, model endpoint/date, MCP schemas/server code, tool weights, data snapshot, adapter, budget, retry/error policy, grader, and aggregation.
10. **Maintain the claim ceiling.** A passing offline package licenses selected analytical-package execution, not emergency-response competence or safety.

## Concrete repository actions

1. **Do not add a DORA- or disaster-specific schema.** Existing expertise-transfer, authority, evidence-state, procedural-relation, artifact-view, action-safety, trace, root/surface, task-health, metric, and validity records already host the required links.
2. **Add one bounded consolidation task** to integrate the analytical-witness-to-consequence boundary into `docs/research-synthesis-index.md` and `docs/benchmark-design-taxonomy.md`: real-source versus task/consequence validity; GT label versus witness versus operational oracle; decision-calibrated geometry; accepted alternatives/abstention; recipient/action/consequence observations; event-clustered inference; and the missing-appendix/release ceiling.
3. **For a future high-consequence pilot**, use matched synthetic or expert-reviewed counterfactuals—not a new disaster pilot by default: hold source evidence fixed while varying stale/live layers, route feasibility, protected populations, uncertainty, escalation requirements, and alternative valid plans; observe artifact, attempted action, collateral state, and recipient disposition separately.

## Action items

- [x] Read the complete immutable v1 PDF/text through the final references.
- [x] Inspect the complete immutable source archive and verify that cited Appendices C–H are absent.
- [x] Recheck exact title/arXiv ID for an author-owned release; none was verifiable on 2026-07-14.
- [x] Reconstruct event/task frame, tool categories, expert/GT compilation, typed scoring, configured-system tables, order-hint and scaffold interventions, and failure analysis.
- [x] Separate source realism, analytical witness execution, artifact agreement, action, consequence, and operational claim.
- [x] Map implications to existing cross-domain contracts without proposing a disaster-specific subsystem.
- [ ] Consolidate the bounded analytical-witness-to-consequence ladder into canonical synthesis.
