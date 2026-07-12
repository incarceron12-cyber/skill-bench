# Paper Review: ArtisanCAD Demonstrates a Procedural Scaffold, Not Industrial Readiness

- **Paper:** https://arxiv.org/abs/2607.05750v1
- **Authors:** Yunhan Xu, Qifeng Wu, Xunjin Li, Yuanwei Bin, Qingsong Yao, Jianghang Gu, Guan Wang, Weihao Lv, Huiyu Yang, Wenfa Luo, Jiao Xiang, Yuntian Chen, and Shiyi Chen
- **Date read:** 2026-07-12
- **Venue / source:** immutable arXiv preprint v1, 7 July 2026
- **Tags:** CAD, procedural-expertise, knowledge-distillation, intermediate-representation, native-artifacts, editability, industrial-validity
- **Local PDF:** `data/papers/pdfs/2607.05750v1-artisancad.pdf` (12 pages; SHA-256 `4c3c1c0510159eb0220529a7abe4de5e42f7039e36b2c98af4f021b1fa41b98b`)
- **Local text:** `data/papers/text/2607.05750v1-artisancad.txt` (SHA-256 `0c45c6f7c79fa12e45e92da0f0a2af8a016dfc803712bc68b20a34a28df8f53f`)
- **Release status checked:** v1 contains no project, code, data, DOI, or supplement URL. Exact-title and arXiv-ID searches on 2026-07-12 found no author-owned repository; only arXiv and third-party summaries. A mutable v2 had appeared by the search date, but this review and all claims below concern immutable v1.

## One-sentence contribution

ArtisanCAD proposes a typed procedural IR that converts CATIA recordings and engineering notes into component-family templates and then adapts those templates into CATIA-native B-Rep variants; a 100-case public ablation supports the value of the IR scaffold for geometric similarity, but the four-family industrial demonstration provides no released lineage, quantitative artifact checks, independent expert judgments, or counterfactual edit tests sufficient to establish expert transfer, production readiness, or even the reported industrial success rate.

## Why this matters for skill-bench

This review advances charter objectives A and B through narrow expansion into a structurally different knowledge-work artifact: dependency-bearing native CAD. The reusable hypothesis is cross-domain: expertise transfer is more inspectable when source records become a typed procedure whose parameters, operations, dependencies, outputs, and checks can be traced into an executable artifact. CAD is a bounded test, not a benchmark scope decision.

The concrete evidence is the immutable full paper plus this reconstruction of the proposed chain:

`expert records → agent-authored part skill → template CAD-IR → request-conditioned IR patch → backend calls → native artifact/views → checks`

The central uncertainty is whether success comes from transferred expert procedure, a privileged component template, the IR’s structure, CATIA/backend affordances, or evaluator coupling. The paper isolates IR structure on a public benchmark, but does not isolate those factors in its industrial cases. Useful completion is therefore a claim boundary and a lineage design, not a new CAD-specific schema. Existing expertise-transfer, task-projection, artifact-admissibility, procedural-skill, and counterfactual-artifact machinery can represent the implications; no duplicate build task is added.

## Research question and bounded answer

The paper asks whether expert CAD traces can be distilled into reusable skills that let an agent convert ambiguous, high-level variant requests into editable, production-oriented native CAD models (pp. 1–3). It claims that CAD-IR both scaffolds vague text-to-CAD generation and transfers expert operations to new variants in four automotive component families (pp. 3, 9–10).

The evidence supports a narrower answer:

1. On 100 sampled Text2CAD prompts, an ArtisanCAD condition with explicit CAD-IR has better mean/median Chamfer Distance and mean solid IoU than an internal no-IR condition, with all 100 outputs executable (Table 2, p. 8).
2. The paper shows rendered examples of four source parts and sixteen requested variants that the reported system produced using four component-specific templates (Figure 4, pp. 9–10).
3. The proposed IR is a plausible carrier for operation order, parameters, tool bindings, generated entities, dependencies, and checks (Equations 2–3, p. 5).

It does not establish that the four skills faithfully capture expert reasoning, that variants preserve dependency integrity, that native files remain usefully editable, that outputs satisfy engineering/manufacturing requirements, that experts approved them, or that the package is production-ready.

## Methodology and system

### Expert-to-skill acquisition

For each component family, the authors say they collect CATIA operation recordings, macro logs, drawing notes, descriptions, feature trees, and parameter tables (pp. 4–5). A part skill contains:

- a family description, function, and geometric properties (`D_s`);
- an expert operation order (`O_s`);
- parameter semantics, defaults, and ranges where available (`P_s`);
- a template CAD-IR (`Z_s`).

Low-level macro operations are grouped into semantic stages such as base sketch, guide curves, sweep, split, holes, and export. Codex-xHigh parses the heterogeneous records, abstracts recurring parameter patterns, and writes the skill/template; replay of the MCP chain is described as validation (p. 5).

This is the paper’s most important but least evidenced transformation. It reports no number or qualifications of source experts, recording duration, number of demonstrations per family, family-selection rule, macro size, contradictory demonstrations, extraction prompt, transformation review, expert read-back, replay acceptance criteria, rejected skills, or version history. “Expert-grounded” describes source origin, not verified fidelity of the resulting abstraction.

### CAD-IR

The global IR is defined as `Z = <P,T,O,E,V>`: parameters, required tools, ordered operations, generated entities/dependencies, and verification rules. Each operation records `id`, `intent`, `mcp_calls`, `arguments`, `outputs`, `depends_on`, and `verify` (p. 5). This is a useful representation because the agent can patch a procedure at operation level rather than regenerate a backend script.

Yet the manuscript gives only a schematic JSON fragment and prose. It provides no schema, typing rules, identity semantics, dependency-graph constraints, unit system, tolerance semantics, error model, transaction/rollback behavior, or executable verification examples. The “multi-backend” claim is architectural: CATIA is implemented; FreeCAD appears only as an illustrative backend in Figure 2, and no cross-backend execution is evaluated (pp. 5–7).

### Variant generation and feedback

Mimo-v2.5-Pro retrieves a component skill, maps a request to structured edits, fills missing parameters, preserves selected dependencies, and outputs a complete IR or patch (pp. 6–7). CATIA-MCP supports part/hybrid-body construction, sketches, profiles, sweeps, extrusion, datums, splits, visibility, save, and export. Execution emits status, errors, entities, and diagnostics (p. 7).

Eight canonical rendered views are merged into a board. The same model receives the request, skill, and IR summary and returns PASS/FAIL, visible errors, likely failed step, and correction hints; the loop stops on pass or budget exhaustion (Figure 2 and Equations 7–8, pp. 6–7). The maximum budget, visual judge prompt, model settings, stopping threshold, false-pass audit, and number/distribution of revisions are absent. Because the generator also judges its visual output, completion is not independent evidence.

## Experiments and evidence

### Public Text2CAD ablation

The authors randomly sample 100 intermediate-level Text2CAD test prompts and disable the expert skill library (pp. 7–8). Reported results are:

| Condition | Valid | CD mean ↓ | CD median ↓ | solid IoU mean ↑ |
|---|---:|---:|---:|---:|
| Text2CAD | 96/100 | 29.80 | 10.19 | 0.446 |
| CAD-Coder | 100/100 | 14.16 | 3.47 | 0.585 |
| ArtisanCAD without IR, intermediate prompt | 100/100 | 14.83 | 2.45 | 0.614 |
| ArtisanCAD with IR, intermediate prompt | 100/100 | 9.88 | 2.12 | 0.646 |
| ArtisanCAD without IR, expert description | 100/100 | 10.38 | 0.96 | 0.662 |

(Table 2, p. 8.) The abstract reports solid IoU as 0.654, while Table 2 and the results prose report 0.646 (pp. 1, 3, 8); the discrepancy is unresolved.

The cleanest comparison is the internal same-prompt IR versus no-IR pair: mean CD improves by 4.95 and IoU by 0.032. This supports package-level value of the explicit IR representation. However, the paper does not state whether the underlying model, prompt budget, tool access, retries, and selection policy are identical; it releases neither sampled IDs nor per-task paired values. There are no repeated generations, confidence intervals, paired tests, failure analyses, operation-level measures, or model-cost statistics. Mean CD is highly skew-sensitive—the median gap is only 0.33—and the expert-description row changes input content, so it is not a ceiling or matched expertise comparison.

The public benchmark cannot validate expert transfer because the experiment explicitly excludes expert records and skills. It validates only an IR scaffold under the authors’ configured system and geometry metrics. Chamfer distance and voxel IoU do not measure feature-tree quality, reference robustness, semantic parameterization, editability, design intent, manufacturability, tolerances, assembly interfaces, or downstream usability.

### Industrial automotive demonstration

The authors report four real-workflow component families: hood panel, hinge reinforcement plate, outer panel bracket, and lock reinforcement plate. One skill is produced per family. CAD experts then provide four variant requests per family, and Figure 4 displays sixteen rendered outcomes (pp. 9–10). The paper says the full system succeeds while direct generation without skill-guided IR fails to complete the components.

No industrial result table is supplied. Missing denominators include attempted requests, retries, discarded variants, maximum-budget failures, and baseline completion counts. There is no criterion-level evaluation, measurement against requested dimensions, topology/dependency inspection, native-file audit, replay result, edit perturbation, manufacturing check, expert rating, blinded comparison, time/cost baseline, or statistical uncertainty. “Fails” and “successfully” have no operational threshold. Figure 4 can establish that plausible renderings exist; it cannot establish that all attempts succeeded or that the files satisfy the stronger properties claimed.

The experimental contrast also bundles every mechanism: expert records, component identity, parameter schema, operation order, template geometry, verification rules, retrieval, IR, CATIA-MCP, and visual feedback. A part-specific template may encode most of the solution. Adapting “deeper,” “longer,” or “wider” within one family tests constrained template transformation, not open-ended industrial CAD capability.

## Unique insight

### 1. Procedural representations are both interventions and causal hypotheses

CAD-IR does more than tell an agent what to do. Its dependency graph asserts a causal model of artifact construction:

`parameter/reference change → affected operation subgraph → regenerated entities → invariant checks → native model state`

That graph can be tested directly. A valid evaluation should mutate an authoritative parameter or reference, regenerate only the declared descendants, verify unaffected entities remain invariant, and inspect whether requested geometry and native editability survive. Static screenshots and file existence do not exercise the representation’s central claim.

This generalizes beyond CAD to workbooks, notebooks, linked charts, database transformations, and operational plans. Whenever expertise is encoded as an ordered dependency-bearing procedure, the benchmark should test counterfactual propagation—not merely final-state resemblance.

### 2. Expert-source lineage must distinguish preservation from invention

A macro records what an expert did in one instance. Distillation adds semantics: stage grouping, parameter names/ranges, family invariants, verification rules, and which operations may change. Some of those may come directly from the expert; others may be inferred by Codex or authored by the research team. Treating the whole skill as “expert knowledge” erases the transformation boundary.

Each IR field should therefore carry origin and approval:

```yaml
ir_field: operations[12].depends_on
source_record_ids: [macro_07:event_184]
transformation: direct_parse | semantic_grouping | parameter_abstraction | model_inference | author_rule
transformer_version: ...
expert_review: approved | disputed | unreviewed
replay_evidence: ...
held_out_variant_evidence: ...
```

This fits the existing expertise-transfer provenance model; it does not require a CAD-only contract.

### 3. “Native and editable” is a behavioral claim, not a file-format label

A CATPart or B-Rep export may open while still having broken references, flattened geometry, opaque feature naming, overconstrained sketches, nonlocal rebuild failures, or parameters that do not drive intended features. Native-format production is evidence of artifact type. Editability requires perturbation and rebuild tests; maintainability requires structural conventions and qualified review; production usability requires downstream threshold evidence.

The appropriate claim ladder is:

1. **executable:** backend produced a parseable model;
2. **geometrically similar:** specified shape metrics pass;
3. **structurally editable:** declared parameters/references propagate under mutation;
4. **maintainable:** feature structure, naming, dependency robustness, and repair burden meet expert criteria;
5. **professionally acceptable:** independent experts approve under matched requirements;
6. **production-ready:** downstream manufacturing/assembly/compliance gates and operational use are demonstrated.

ArtisanCAD provides quantitative evidence for levels 1–2 on public tasks and an unquantified demonstration relevant to levels 1–3 on industrial examples. It does not establish levels 4–6.

### 4. The right expertise-transfer ablation is not merely skill versus no skill

To separate causal mechanisms, hold model/backend/budget fixed and compare:

1. tools only;
2. typed generic IR without component skill;
3. IR plus operation order only;
4. plus parameter schema/ranges;
5. plus template entities/dependencies;
6. plus verification rules;
7. full expert-derived package;
8. matched non-expert or model-authored template.

Use held-out variants, structural perturbations, and at least one held-out family. This distinguishes representation benefit, privileged template reuse, expert-specific content, and backend effects.

## Limitations and validity threats

1. **Expert provenance is unspecified.** Counts, qualifications, selection, demonstration coverage, disagreement, and role assignments are absent.
2. **No released source-to-skill lineage.** Macro events, notes, prompts, normalized operations, skill files, and review records are unavailable.
3. **Model-authored abstraction is called expert-grounded without fidelity evidence.** Codex adds semantic stages, parameters, and rules with no reported expert approval.
4. **One/few demonstrations are not characterized.** Variation within a component family and saturation are unknown.
5. **IR is schematic, not reproducible.** No schema, examples, parser, validator, semantics, or error contracts are released.
6. **CATIA-MCP is private and under-specified.** Tool schemas, CATIA version, OS, licenses, transactions, and backend code are absent.
7. **Multi-backend support is not empirically shown.** Only CATIA execution is reported.
8. **Configured systems are incomplete.** Model snapshots, prompts, decoding, context, retry budgets, hardware, and cost are missing.
9. **Public sample IDs are absent.** “Random” sampling cannot be reproduced and selection timing is unknown.
10. **No repeated trials or paired uncertainty.** Stochastic generation and task-level variation are hidden by aggregate point estimates.
11. **Abstract/table inconsistency.** Solid IoU is 0.654 in the abstract but 0.646 in Table 2/results.
12. **Metrics cover geometry, not procedure.** CD/IoU cannot validate dependency integrity or editability.
13. **Baseline parity is unclear.** Prompt, budget, retry, execution, and selection equivalence are not documented.
14. **Industrial sample is tiny and family-constrained.** Four source components and sixteen shown requests do not support broad industrial generalization.
15. **No industrial denominators.** Attempts, failures, retries, and selection policy are not reported.
16. **Qualitative-only industrial results.** There are no dimension, topology, feature-tree, dependency, or invariant scores.
17. **No native artifacts are inspectable.** CATPart/STEP files, feature trees, and execution traces are not released.
18. **Editability is asserted, not exercised.** No parameter mutation, reference replacement, rebuild, rollback, or handoff test is reported.
19. **Expert judgment is not reported.** Experts supply requests, but independent blinded acceptance, disagreement, and adjudication are absent.
20. **Generator and visual evaluator are coupled.** Mimo-v2.5-Pro appears to generate/patch and judge views, creating self-confirmation risk.
21. **Visual checks under-observe the construct.** Eight renders cannot reveal hidden constraints, feature history, reference fragility, or manufacturability.
22. **Verification rules are not demonstrated.** Their source, examples, coverage, execution, and pass rates are absent.
23. **Bundled industrial intervention.** Skill, IR, template, backend, feedback, and component prior change together.
24. **Template proximity is unmeasured.** Variant requests may require local edits rather than new procedural planning.
25. **No held-out family transfer.** Reuse is within component family, not cross-family or cross-domain.
26. **No operational comparison.** Engineer time, correction burden, latency, cost, failure recovery, adoption, and maintenance are unmeasured.
27. **No safety/compliance evaluation.** Tolerances, assembly, crashworthiness, materials, manufacturability, access control, and IP leakage are outside the evidence.
28. **“Production-ready/industrial-grade” exceeds demonstrated evidence.** Native rendering and reported executability do not certify production use.
29. **No v1 official release.** Exact replication or audit is impossible from the paper alone.
30. **Post-v1 version drift.** A v2 already exists; claims must preserve the immutable version actually reviewed.

## Reproducibility and operational realism

Manuscript provenance is strong: immutable v1 PDF/text and hashes are preserved. Experimental reproducibility is poor. The paper gives enough architecture to imitate the approach but not enough to reproduce any number or industrial artifact. Missing resources include sample IDs, source records, prompts, skills, IRs, CATIA-MCP, model snapshots, native outputs, traces, grader outputs, expert labels, and analysis code. CATIA licensing and proprietary automotive data would remain practical barriers even with code.

Operational realism is mixed. Positive features include real professional software, native B-Rep construction, long operation chains, feature dependencies, company-affiliated authors, and variant requests reportedly supplied by CAD experts. But the evaluation is a selected demonstration without downstream handoff, independent review, edit/rebuild exercises, manufacturing or assembly checks, security boundaries, latency/cost, or maintenance. The environment is industrial; the evidence is formative.

## Relation to existing skill-bench evidence

- **Industrial expertise codification review:** both studies transform a small expert source into executable/prompted guidance and then grade closely aligned outputs. ArtisanCAD adds a stronger procedural carrier but weaker human evaluation. The same authorship-separation and claim-ceiling rules apply.
- **LH-Bench:** CAD-IR makes the procedure→trace→artifact concept concrete at operation/dependency level, but ArtisanCAD does not expose LH-Bench-style rubric anchors, trace evidence, recovery rates, or independent preferences.
- **MBABench:** a native workbook and a native CAD model share the same validity boundary: current-state correctness is weaker than counterfactual integrity. Parameter edits and rebuilds are the CAD analogue of assumption mutation and recalculation.
- **Artifact admissibility:** rendered views can judge visible geometry; native feature/dependency views are required for editability; execution/rebuild traces are required for robustness; qualified expert evidence is required for professional acceptance. Missing views should yield `insufficient_evidence`, not inferred success.
- **Task projection:** variant requirements, source model state, acceptable procedures, native witnesses, and checks should be projected from versioned requirement atoms. A template replay certificate proves executability, not semantic conformance of a new variant.

## Transfer to skill-bench

1. **Represent procedural lineage per field/operation.** Use existing expertise-transfer provenance to distinguish direct trace parsing, semantic grouping, abstraction, model inference, and author-added checks; require transformation review status.
2. **Treat procedure graphs as testable causal models.** Add pilot checks that mutate parameters/references, rebuild declared descendants, verify preserved regions, and compare resulting native/rendered states.
3. **Apply artifact-view admissibility rigorously.** Geometry views, native dependency state, executable rebuild traces, and expert acceptance answer different predicates and must not substitute for one another.
4. **Use a native-artifact claim ladder.** Report executable, geometrically conformant, structurally editable, maintainable, professionally acceptable, and production-ready separately.
5. **Ablate representation from expertise.** A generic IR/no-skill condition estimates scaffolding; content-factor ablations and matched non-expert templates estimate the contribution of expert-derived material.
6. **Measure task delta and template distance.** Record inherited entities/dependencies, required changed subgraph, preserved zones, new operations, and semantic distance from the source template rather than final artifact complexity alone.
7. **Require independent thresholds before readiness language.** Qualified experts who did not author the skill should inspect native files, execute held-out edits, and adjudicate acceptance under explicit consequences.

## Action items

- [x] Read and verify the complete immutable v1 PDF/text and preserve exact paths/hashes.
- [x] Search for an author-owned official artifact; none was verifiably linked for v1.
- [x] Reconstruct source→skill→IR→backend→artifact→evaluation lineage and its missing evidence.
- [x] Separate IR scaffold evidence from expert-transfer, editability, maintainability, and production-readiness claims.
- [x] Map implications to existing cross-domain machinery; no nonduplicate build task is warranted.
- [ ] When the next dependency-bearing pilot is instantiated, add a counterfactual propagation check and field-level transformation provenance under existing queued/consolidated contracts.
