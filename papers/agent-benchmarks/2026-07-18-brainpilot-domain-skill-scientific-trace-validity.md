# BrainPilot: domain scaffolding and inspectable workflow are real; expertise, trace integrity, and reported results remain different claims

## Bottom line

BrainPilot is a substantial open scientific-agent system rather than a paper-only architecture. The full paper specifies a PI–specialist workflow, a neuroscience retrieval corpus, a routed Skill library, an Auditor, a Graph of Trace (GoT), three Agents' Last Exam (ALE) tasks, four new domain benchmark tasks, and five case studies. The acquisition-time official releases contain the multi-agent runtime, 74 Skill files, GoT code, Auditor prompts, and all four BrainPilotBench-v0 task packages. The benchmark release builds and its 208-test suite passes (205 passed, three explicitly skipped integration tests).

The paper's central validity problem is that four different things are repeatedly adjacent but not empirically joined:

1. **domain material is present** — papers/books are indexed and method documents exist;
2. **an agent can retrieve or load it** — searches and loads occur;
3. **the material is source-faithful and appropriate for this case** — claims, parameters, applicability, and omissions are independently validated;
4. **using it improves scientific work** — adoption changes a decision or artifact and an independent observer verifies the consequence.

BrainPilot provides meaningful evidence for (1), executable machinery for (2), almost no item-level evidence for (3), and a domain-knowledge ablation that is adverse more often than beneficial for (4): among the 26 BrainPilotBench cells valid in both conditions, knowledge increased eight scores, reduced 14, and left four unchanged. The released library contains 74 `SKILL.md` files, not the paper's 72, but both pinned repositories postdate immutable arXiv v1, so this is release drift rather than proof that the paper-time count was false. More importantly, none of the 74 released Skills is marked `community-reviewed` or `expert-verified`: 51 say `ai-generated`, and 23 have no `review_status`. The release demonstrates a Skill-production and verification *process*, not verified domain expertise.

The GoT similarly records a curated, agent-reported account of work; it is not an execution-derived, tamper-evident scientific evidence graph. The paper says the record is append-only and forbids retrospective edits, cycles, and orphan references. In the inspected release, `updateNode()` can change descriptions, artifacts, parents, and metadata; `createNode()` and `addRelation()` do not validate parent existence or acyclicity. The Trace agent may merge, skip, split, and infer relations. These are useful narrative-provenance features, but current release conformance does not support the stronger append-only DAG claim. The timing boundary again matters: the release was authored after v1, so exact paper-time behavior remains unverified rather than directly falsified.

The Auditor is a well-scoped evidence checker in the released prompt, with an explicit `confirmed / unverified / disputed` vocabulary and a second pass for visible scientific-validity defects. But it cannot inspect the GoT, other agents' mailbox histories, or external sources; it is forbidden to rerun analyses or compute missing evidence. It therefore audits a workspace view, not the complete claimed trace, and cannot independently validate source correctness, omitted evidence, runtime behavior, or scientific interpretation. The paper itself ultimately states the right ceiling: researchers retain responsibility, while broader methodological, statistical, and interpretive checks remain future work.

BrainPilotBench-v0 has stronger engineering than the paper's empirical record: task-local artifact contracts, private labels for three tasks, no-network container inference, typed missingness, data locks, and tests. Yet the released snapshot contains no raw paper run bundles, trial trajectories, score records, exact configured-system manifests, or cost/provider receipts. Reported tables and case-study numbers cannot be reconstructed from released rows. Three task packages also differ materially from the paper appendix: RSC changed its place-cell definition, BCI changed from one-subject accuracy to nine-subject mean kappa, and Sleep-EDF changed from 20-fold leave-one-subject-out to a fixed 14/2/4 split. The post-v1 release is therefore evidence of an evolving benchmark, not the immutable instrument that generated every paper cell.

The strongest warranted claim is narrow: **BrainPilot is an inspectable, runnable domain-scaffolded research-agent framework, and its authors report single-run configured-system outcomes on three adapted ALE tasks and four preliminary neuroscience task packages.** The evidence does not establish transfer of neuroscience expertise, scientific correctness, trace completeness or integrity, Auditor independence from shared evidence failures, repeat reliability, discovery acceleration, expert equivalence, lower total operational cost, or readiness for scientific decision making.

## Source and reading record

### Complete primary source read

- Haoxuan Li et al., *BrainPilot: Automating Brain Discovery with Agentic Research*.
- Immutable record: <https://arxiv.org/abs/2607.15079v1>; PDF: <https://arxiv.org/pdf/2607.15079v1>.
- Local PDF: `data/papers/pdfs/2607.15079v1-brainpilot.pdf` (47 pages; 21,819,949 bytes; SHA-256 `6d5f960f23e7734ef61f092d371d2b30251b177173be485ab62e3d20f036e269`).
- Local full text: `data/papers/text/2607.15079v1-brainpilot.txt` (SHA-256 `af4fc7ff8de659f542f4400c729c50fb94235eb8bb5d0bb88081b24475e097c0`).
- Local arXiv source: `data/papers/source/2607.15079v1-source.tar.gz` (SHA-256 `1528b377125751613827247ca791cfab1a45c8f5f5a6010434d585d55f0764fa`).
- Read 18 July 2026 through architecture, knowledge construction, GoT, ALE evaluation, BrainPilotBench, all case studies, discussion, limitations, appendices, task prompts, and scorer definitions. The API reports v1 published 16 July; the manuscript header displays 18 July. No withdrawal/retraction notice is present.

### Official releases audited

- BrainPilot: <https://github.com/NeuroAIHub/BrainPilot>, pinned acquisition-time commit [`7d3853f62caa23e6501a6e35f177c15b3f786af5`](https://github.com/NeuroAIHub/BrainPilot/commit/7d3853f62caa23e6501a6e35f177c15b3f786af5), authored 17 July 2026. Local archive: `data/sources/releases/2607.15079v1-brainpilot/NeuroAIHub-BrainPilot-7d3853f.zip`; SHA-256 `53fd6995922ae58ebf11d08d838a9e9326739679b655a93138c37a4c62d69fea`.
- BrainPilotBench: <https://github.com/NeuroAIHub/BrainPilotBench>, pinned acquisition-time commit [`eb87ad6b67fdbb0ae00bcaae291e0a868f79d470`](https://github.com/NeuroAIHub/BrainPilotBench/commit/eb87ad6b67fdbb0ae00bcaae291e0a868f79d470), authored 17 July 2026. Local archive: `data/sources/releases/2607.15079v1-brainpilot/NeuroAIHub-BrainPilotBench-eb87ad6.zip`; SHA-256 `d6e14481a57e95884f1e6fc86b7fbfdd80cbadd8f60f5ac25c468f74c51dad98`.
- Provenance and inventory: `data/sources/releases/2607.15079v1-brainpilot/provenance.json` and `inventory.json`.

Both release commits postdate the arXiv v1 publication timestamp. Findings below distinguish **paper claim**, **current release conformance**, and **paper-time implementation**. The release can show present agreement or drift; without earlier history and raw run manifests it cannot establish the exact code that generated v1 results.

The benchmark archive was extracted, built with `npm run build`, and tested with `npm test`: 208 tests discovered, 205 passed, zero failed, and three Docker/dependency integration tests skipped by declared opt-in conditions. An initial test command before build discovered zero compiled tests; that non-result was not treated as validation.

## One-sentence contribution

BrainPilot makes domain resources, specialist handoffs, artifact production, and pre-delivery audit unusually inspectable in one open scientific-agent framework, while its paper and release show that presence, retrieval, authority, adoption, trace integrity, and independently valid scientific consequence remain separate warrants.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C through narrow expansion and consolidation at the domain-expertise-to-benchmark boundary. The concrete evidence is an immutable full-paper record, two pinned official snapshots, a complete Skill-status inventory, code-level GoT/Auditor audit, task-protocol comparison, and real benchmark-framework test run. It clarifies when a domain package supports an inspectable configured-workflow claim rather than expertise transfer, scientific validity, cost-effectiveness, professional equivalence, or readiness. Classification: expansion plus consolidation; neuroscience is a bounded mechanism case, not a scope commitment. Useful completion is the claim-bounded cross-domain chain developed below, without duplicating existing Skill-authority, evidence-transition, trace, or participation machinery.

## Research question

The paper asks whether a multi-agent system grounded in neuroscience-specific resources can coordinate literature work, experimental planning, analysis, writing, and audit while keeping a long scientific workflow inspectable and cheaper than general agent harnesses.

Its concrete contributions are:

1. a PI agent coordinating Librarian, Experimentalist, Engineer, Writer, Auditor, and Trace roles;
2. a claimed 7,233-item retrieval corpus and 72-unit Skill library;
3. a progressively loaded Skill router;
4. a GoT interface intended to connect steps, artifacts, and dependencies;
5. a mandatory pre-delivery Auditor pass for substantive drafts;
6. evaluation on three neuroscience ALE tasks;
7. BrainPilotBench-v0 with RSC calcium imaging, TOPS-fMRI, BCI IV 2a, and Sleep-EDF tasks; and
8. five end-to-end case studies.

The important question for `skill-bench` is not whether these components exist—they substantially do—but **which links turn a domain package into evidence of domain competence and a trace into evidence of scientific validity**.

## Methodology and evidence

### System organization

The PI decomposes work and delegates to specialists. Specialists are prompted to search Skills before nontrivial methods, record tangible outputs, and return results through the PI. Report-like material goes through the Writer before the Auditor. A separate Trace agent receives self-reported trace events and curates them into a graph.

This separation has real design value. It creates named intervention points, avoids treating one opaque transcript as the only evidence, and makes the intended handoffs visible. It also creates shared-failure risks: agents use related models, prompts, workspace artifacts, and source packages. Calling a role “independent” denotes organizational separation, not statistical or epistemic independence.

### Domain knowledge assets

The paper reports 7,233 indexed books/papers, 377,868 title/abstract tokens, OCR with DeepSeek-OCR, 1,500-character chunks with 200-character overlap, 1,024-dimensional BGE-M3 embeddings, and BGE reranking (Section 3.2, pp. 6–7). It describes 72 Skills across seven grouped domains from LLM-authored, paper-derived, and repository-derived pipelines.

The public release does not contain the corpus payload: documented knowledge-source, chunk, model, and vector-store directories are placeholders, and `packages/docs/content/docs/skills-knowledge-base.mdx` explicitly says the open-source package does not ship a hosted public knowledge base. Thus the 7,233-item corpus composition, permissions, OCR quality, chunk lineage, retrieval quality, and result citations cannot be audited from the release. The paper gives aggregate counts, not a source manifest, item-level rights ledger, deduplication report, retrieval test set, relevance judgments, or citation-faithfulness evaluation.

The Skill release is inspectable. A full frontmatter inventory found 74 files across 21 repository directories: eight meta-skills and 66 other Skills. Of these, 51 explicitly carry `review_status: ai-generated`; 23 omit `review_status`; none says `community-reviewed` or `expert-verified`. This does not mean every statement is wrong. It means the release provides no item-level evidence that an authorized domain expert accepted any Skill's parameters, scope, exceptions, or citations.

The `paper-to-skill` meta-skill contains several good controls: preserve exact numbers, record source locations, flag missing information, identify context distortion, and require self-verification. But the verifier is the same agentic production process checking its own extraction unless an independent human intervenes. The `verify-skill` meta-skill asks a reviewer for familiarity, parameter judgments, and a scenario, then changes status based primarily on self-reported familiarity (4–5 → expert-verified; 2–3 → community-reviewed). It does not require credential evidence, domain-specific conflict checks, a second reviewer, disagreement retention, signed approval of each correction, empirical replication, or demonstrated consequence. It even instructs the agent to apply and commit corrections before presenting the diff for reviewer confirmation. This is useful community workflow scaffolding, not a validated authority protocol.

### Domain-knowledge intervention evidence

The paper evaluates each ALE and BrainPilotBench cell with knowledge disabled and enabled. That is the right basic intervention shape, but the treatment is compound: retrieval corpus access, Skill search/load, domain MCP calls, context expansion, and potentially changed trajectories all vary together. There is no matched budget, exact retrieved-content log, adoption annotation, or item-to-artifact lineage in the release.

The empirical pattern does not support a general benefit claim. On BrainPilotBench, among 26 cells valid in both conditions, knowledge improves eight, worsens 14, and leaves four unchanged (Section 4.2, p. 11). ALE outcomes also reverse in places: for BrainPilot with GPT-5.5, T1 falls from 1.00 to 0.00; with Opus 4.8, T1 similarly falls from 1.00 to 0.00; several T3 runs become ungradable. These single runs cannot distinguish harmful knowledge from stochasticity, context cost, retrieval mismatch, or unrelated trajectory variation. They do decisively block the inference “the presence or use of this domain library transfers expertise.”

### Graph of Trace

The paper claims schema-validated nodes with descriptions, artifacts, parent steps, inferred dependency edges, an append-only record, and guards against edits, cycles, and orphan references (Section 3.3, pp. 7–8).

The release implements node creation, updating, relation addition, persistence, event emission, and graph rendering. It also tests edge direction and trace-reminder behavior. But current semantics are weaker than the prose:

- `packages/runtime/src/trace.ts:createNode()` accepts `parent_ids` without checking that parents exist;
- `addRelation()` appends parent IDs without cycle detection;
- `updateNode()` deliberately mutates the node by `Object.assign`, including description, artifacts, parents, and metadata, then preserves only the original ID and creation time;
- the store is a mutable JSON document, without a hash chain, signatures, event sequence, immutable prior versions, artifact content hashes, or execution attestation;
- `packages/runtime/src/personas.ts` tells the Trace agent it may merge duplicate events, skip events, split events, and infer relations;
- `packages/runtime/src/extensions/trace-reminder.ts` observes events and prompts agents to record outputs, but does not establish that every consequential action, source read, parameter choice, failed attempt, or correction is captured.

Accordingly, GoT is an **agent-curated workflow account**. It may improve navigation and post hoc review. It does not by itself prove completeness, faithful causality, artifact integrity, or root-cause localization. A dependency edge inferred from context is a hypothesis unless bound to execution reads/writes or independently confirmed. This differs from scientific-workspace evidence graphs that retain exact target bytes, command events, produced artifacts, checks, and immutable cross-record bindings; even those stronger graphs establish closure and inspectability before they establish scientific correctness.

### Auditor

The paper's Auditor checks numerical claims, artifact references, and citations against session files and labels each `confirmed`, `unverified`, or `disputed`. The current release prompt expands this to inspect visible leakage, invalid metrics, baseline confusion, circular analysis, multiple comparisons, pseudoreplication, and claim overstatement.

This is one of the release's strongest pieces of process design: it demands concrete paths, treats plausibility as insufficient, preserves a report, and tells the PI—not the Auditor—to make the final delivery decision. It should be retained.

Its evidence view imposes hard limits:

- it cannot call `get_trace_graph`;
- it cannot inspect other agents' mailbox histories;
- it cannot access external sources;
- it may not run scientific code, recompute a number, call APIs, or re-execute experiments;
- it audits a Writer/PI draft and workspace artifacts, not raw expert output;
- it may ask at most two follow-up questions, then must classify unresolved gaps.

The design can detect a draft number absent from workspace evidence. It cannot establish that the workspace evidence is itself correct, complete, untampered, source-faithful, or generated by the stated code. It can miss coordinated error, fabricated supporting files, silent exclusions, wrong external citations, and scientific defects not visible in retained artifacts. Because it cannot read GoT, “traceability” and “audit” are separate evidence channels in the release, not one integrated verification chain.

### ALE evaluation

The paper selects all three ALE tasks it identifies as brain science from a benchmark exceeding 1,000 tasks. Eight configured harness–backbone packages are evaluated with and without domain knowledge, one run per cell. Deliverables are graded with ALE's withheld artifact graders, but BrainPilot uses code rather than desktop GUI interaction and runs through an adapter outside ALE's hosted environment. This is a valid artifact-equivalent evaluation under the task contract, not evidence of computer-use capability.

The paper reports large cost differences—$0.08 for BrainPilot/DeepSeek-V4-Pro versus $22.53 for Codex/GPT-5.5 across three knowledge-enabled runs—and states BrainPilot uses 8–63% of matched harness time and 5–56% of cost. The comparison is configured-system evidence: harness, backbone, trajectory length, failure behavior, and provider pricing differ. There are only three purposively domain-matched tasks and one trial each; no uncertainty, repeat reliability, complete environment identity, raw token ledger, billing receipt, or score bundle is released. Lower endpoint spend in these runs is not lower total research cost, lower expert verification burden, or better cost-effectiveness.

Relative to the prior ALE review, BrainPilot adds a neuroscience-specific configured-system slice but inherits ALE's task-selection and inference boundaries. Three tasks cannot validate neuroscience-work coverage, and re-scoring outside the hosted environment requires adapter-equivalence evidence that the paper describes but the release does not preserve per run.

### BrainPilotBench-v0

The four tasks are meaningfully different and artifact-first:

- RSC: analysis summary, report, and figures;
- TOPS-fMRI: raw linear signature, manifest, inference program, edge-order validation, model card, and report;
- BCI IV 2a: submitted model class trained/evaluated by the grader;
- Sleep-EDF: submitted model class trained/evaluated on held-out subjects.

TOPS, BCI, and Sleep use held-out evaluator information and release code that isolates submitted inference in no-network, non-root containers with read-only mounts. The framework distinguishes valid zero from unscored failure, binds data by hash, validates artifact contracts, and has extensive unit tests. This is stronger machinery than report-only scientific benchmarks and resembles the best parts of AstaBench's typed solve→score separation. It should be treated as a preliminary portfolio of four different estimands, not one brain-research scale.

#### Release drift from the paper instrument

The current task packages do not freeze the exact paper appendices:

1. **RSC:** the paper appendix classifies place cells using a pointwise lower-bound tuning-curve criterion against a 97.5th-percentile shuffled curve. Released `prompt/turns.yaml` and `checks/benchmark.py` use observed spatial information above a cell-specific null quantile. This changes the scientific object and reference ratio.
2. **BCI IV 2a:** the appendix says `subject_id = 1` and `final_score = downstream_accuracy × 100`. The release trains/evaluates all nine participants and uses mean Cohen's kappa as primary.
3. **Sleep-EDF:** the paper case/appendix uses 20-fold leave-one-subject-out training. The release fixes subjects 0–13 for training, 14–15 for validation, and 16–19 for private test, with held-out kappa primary.
4. **RSC task version** is already `0.2`; the others are `0.1`.

These may be sensible repairs. They prevent the release from being treated as a byte-identical reproduction package for the paper's 56 cells. A frozen release bridge should name which task version, prompt hash, grader hash, data hash, and configured-system manifest generated each result.

#### RSC observer weakness

The released RSC automatic grader does not recompute the submitted analysis. It reads four self-reported values from `benchmark_summary.json` and compares them with a public `reference.json`: place-cell ratio within a ±0.10 band around `0.3862502045956126`, expected significance `true`, and decoding improvement at least `0.5657052247971856`. The agent prompt does not print these values, but the public grader does. A submission can copy compliant numbers without producing the analysis. The Oracle intentionally writes a synthetic passing summary and placeholder 1×1 PNG; the human rubric does not participate in Oracle validation.

This validates the scorer plumbing, as the comments correctly say, but not task correctness. The three human rubric dimensions are only names plus one-line descriptions, without level-specific anchors, required evidence views, disqualifying failures, reviewer qualification, independent ratings, or agreement. The paper says visual/trial-bin/firing-rate outputs are diagnostics; the release's README says deterministic checks plus human rubric, creating another score-semantics boundary. RSC requires an evaluator that recomputes values from submitted arrays or execution artifacts, checks figure/report consistency, and treats unsupported self-report as invalid.

#### Missing empirical records

Neither release contains raw paper trial bundles, `scores.json` rows, complete event traces, GoT files, audit reports, task-level configured-system manifests, exact model endpoint dates, seeds for all stochastic stages, cost events, or billing/provider receipts. The benchmark archive contains rendered result imagery and code, but no table-building dataset. Thus the paper's 56-cell count, 53 valid scores, RSC two-run selection, per-cell costs, domain-resource calls, and all case-study values remain author-reported rather than release-reconstructible.

### Case studies

The five cases show that the framework can organize plausible multi-artifact scientific work. They also expose why a polished chain is not scientific validation:

- RSC reports held-out decoding MAE 16.8 cm and `r = 0.646`, but no raw run bundle is released.
- The mouse visual hierarchy case preserves a substantive citation error: anatomical scores are attributed to Harris et al. in the agent output although they came from Siegle et al. The paper explicitly calls for human verification. This is direct evidence that Writer/Auditor/trace structure did not prevent a source-authority failure.
- The fMRI case reports one split, small subgroups, threshold optimization within test cohorts, imperfect edge-order verification, and no weight stability inference.
- Motor imagery reports a nonsignificant improvement over EEGNet across nine subjects and three seeds; the task release uses a different formal protocol.
- Sleep staging reports 20-fold LOSO performance but lacks a same-code reproduced DeepSleepNet baseline and differs from the released benchmark split.

These are demonstrations of configured workflow and artifact assembly, not independent replications, discoveries, or expert-accepted scientific conclusions.

## Unique insight: an inspectable domain scaffold can still be epistemically open-loop

BrainPilot's distinctive lesson is that adding knowledge, Skills, traces, specialists, and an Auditor can improve **process legibility** without closing the scientific-validity loop.

A defensible domain-skill chain is:

`authorized source span`
`→ extracted rule/parameter with applicability and omissions`
`→ independent domain approval and disagreement`
`→ retrieval opportunity`
`→ content delivered`
`→ agent adoption or rejection`
`→ affected decision/artifact delta`
`→ independent scientific check`
`→ downstream consequence`.

BrainPilot exposes source categories, Skill files, searches/loads, artifacts, and audit reports. It does not preserve the complete chain at item level. Consequently:

- **availability is not adoption**: a Skill search/load count says content entered context, not that a decision used it;
- **adoption is not correctness**: following a paper-derived parameter may be inappropriate for a new acquisition regime;
- **source citation is not authority**: an LLM-authored distillation can distort context even when a paper exists;
- **internal consistency is not scientific validity**: an Auditor can confirm that a number appears in a file while the analysis is circular or the file is fabricated;
- **narrative lineage is not execution lineage**: a Trace agent's inferred edge can be plausible but not causally bound to reads, commands, and writes;
- **steerability is not exercised oversight**: an interface offers an intervention opportunity; a benchmark must record whether a qualified person saw, understood, changed, approved, or rejected the work.

This clarifies the relation to ReasFlow: both provide useful procedural-card structures, but paper/model-derived cards need source-span fidelity, authority, adoption, and consequence evidence before they count as expertise. It clarifies the relation to scientific-workspace benchmarks: persistent artifacts and graph closure improve inspectability, but edge semantics and root-cause claims require execution binding and mutation tests. It clarifies the relation to AstaBench: a common runner over heterogeneous tasks creates a portfolio, not one scientific-capability scale. Finally, it clarifies human oversight: named checkpoints are only affordances until observed participation and decision authority are recorded.

## Reproducibility and operational realism

**Paper inspectability: moderate to strong.** The 47-page manuscript includes architecture detail, exact table cells, limitations, cost definitions, and long task appendices. It candidly reports single runs, adverse knowledge ablations, case-study caveats, and continuing human responsibility.

**System release inspectability: moderate.** The runtime, prompts, 74 Skills, GoT implementation, Auditor policy, and tests are available. The knowledge corpus is absent, and release commits postdate v1.

**Benchmark machinery: strong for a preliminary framework.** Four task packages, data locks, private-data boundaries, artifact contracts, scorers, container controls, typed unscored states, and 208 tests are meaningful. Three skipped integration tests mean Docker isolation and one dependency-heavy RSC path were not exercised in this review environment.

**Empirical reproducibility: weak.** There are no raw paper runs or score table inputs; exact paper-time task versions are not frozen; commercial and future-dated model identities are mutable; and cost records are summary values. Reported scores can be read but not reconstructed from released bytes.

**Operational realism: mixed.** Real public neuroscience datasets, full repositories, model training, held-out labels, reports, and figures are stronger than quiz tasks. But the suite contains only four tasks, omits wet-lab execution, protocol registration, data governance, collaboration, manuscript peer review, replication, negative-result handling, long-term maintenance, and external decision consequences. Human oversight is supported by UI and prompts but not evaluated as a treatment with burden and decision outcomes.

## Limitations and validity threats

### Domain material and Skill authority

1. The 7,233-item corpus is not released as an item-level manifest or auditable index.
2. Rights-holder permission is asserted in one footnote, without a source-level rights ledger.
3. OCR, chunking, deduplication, retrieval recall, reranking quality, and citation fidelity are not evaluated.
4. Public knowledge payload directories are placeholders.
5. Paper count (72) and post-v1 release count (74) differ without a versioned membership bridge.
6. Seven paper domains are grouped reporting categories; the release has 21 directories, so coverage depends on a mapping not released as a frozen ontology.
7. No released Skill is marked community- or expert-verified.
8. Fifty-one Skills explicitly say AI-generated; 23 omit status, creating ambiguous authority.
9. Verification status can be promoted from self-reported familiarity without credential or conflict evidence.
10. No item-level disagreement, correction history, independent review, or empirical replication record is released.
11. A Skill's presence, search, and load are not separated from actual adoption.
12. Knowledge-enabled runs change multiple resources and context, not one isolated Skill treatment.
13. Single-run adverse and favorable ablations cannot identify knowledge-package causality.

### Trace and audit validity

14. Trace events are self-reported, not exhaustively captured from execution.
15. The Trace agent may merge, skip, split, and infer, changing the record through editorial judgment.
16. Current code permits node updates, contrary to a literal append-only claim.
17. Current code does not enforce acyclicity or parent existence.
18. Nodes do not bind artifact content hashes or immutable execution events.
19. No completeness denominator defines which actions must appear.
20. Dependency edges are inferred and do not establish causality or root cause.
21. The Auditor cannot access GoT, so trace and audit are not one joined evidence view.
22. The Auditor shares workspace evidence and can confirm internally coherent falsehoods.
23. External citation correctness is not independently checked online.
24. Re-execution is prohibited, preventing replication or detection of nondeterministic mismatch.
25. Two follow-ups and no mailbox visibility constrain contradiction resolution.
26. PI retains final delivery authority; no gate proves high-risk findings block output.
27. No evaluation measures Auditor sensitivity, specificity, severity calibration, or false reassurance.
28. Human inspection affordances are not evidence that qualified oversight occurred.

### Benchmark and inference validity

29. ALE evidence covers only three selected brain-science tasks.
30. Code-based ALE completion does not measure desktop computer use.
31. Adapter equivalence is described but raw hosted-versus-adapter bridge records are absent.
32. All reported evaluation cells are single runs except the selected RSC result.
33. RSC selects the higher of two runs, introducing outcome-conditioned reporting.
34. No confidence intervals, repeat reliability, or rank probabilities are reported.
35. Harness and backbone vary as configured packages, not isolated model treatments.
36. BrainPilotBench's four tasks are heterogeneous and do not support one latent brain-research capability scale.
37. Three released task protocols materially differ from paper appendices.
38. The RSC automatic grader trusts self-reported summary fields rather than recomputing analysis.
39. Public RSC reference thresholds make post-release answer copying possible.
40. RSC human rubric lacks performance-level anchors and agreement evidence.
41. Oracle/NOP gates validate scorer plumbing, not scientific oracle validity.
42. Absence of raw score rows prevents table reconstruction and missingness audit.
43. Public tasks, prompts, references, and code raise contamination/saturation risk.
44. No benchmark task tests literature citation fidelity, experimental design approval, cross-modal integration, or wet-lab consequence.
45. Missing/failed states are typed better than zero, but failure causes are not released for paper cells.

### Cost, case-study, and consequence validity

46. Cost uses list pricing and reported token use, not provider receipts.
47. Offline corpus creation, benchmark construction, human review, compute hardware, storage, and maintenance are excluded.
48. Lower spend is confounded with backbone, harness, failure, and trajectory length.
49. No quality-adjusted or consequence-adjusted cost metric is defined.
50. Case-study artifacts and traces are not released as reconstructible bundles.
51. The visual-hierarchy citation error demonstrates unresolved source provenance.
52. Several case studies use single splits, weak baselines, small subgroups, or descriptive physiological checks.
53. Scientific plausibility of figures does not validate methods or causal interpretation.
54. No external scientist independently reproduces or accepts the findings.
55. No evidence measures research time saved net of verification, correction, or failed runs.
56. No evidence links use to publication quality, replication, discovery, safety, or scientific decision outcomes.

## Transferable design patterns

### Retain

1. **Separate specialists by work function.** Named handoffs make evidence responsibilities inspectable.
2. **Require artifact-first outputs.** Reports, code, models, manifests, figures, and machine-readable results support plural evidence views.
3. **Use progressive Skill disclosure.** Search before full load is a sensible context-budget mechanism.
4. **Make evidence-state vocabulary explicit.** `confirmed / unverified / disputed` is better than fluent undifferentiated confidence.
5. **Preserve audit reports as artifacts.** The PI should cite and resolve them rather than silently overwrite concerns.
6. **Keep valid zero distinct from missing/failed.** BrainPilotBench's typed score state prevents denominator laundering.
7. **Stage held-out labels outside agent workspaces.** TOPS, BCI, and Sleep show credible data-boundary machinery.
8. **Treat Oracle/NOP as plumbing gates only.** The release correctly avoids calling them performance validation.
9. **Report adverse ablations.** Publishing the 8/14/4 knowledge pattern is more informative than selecting only benefits.
10. **State human responsibility.** The paper's discussion gives a more defensible ceiling than its broad acceleration framing.

### Repair

1. **Create a Skill authority ledger.** For every Skill and claim atom, bind source spans, extraction actor, review status, reviewer authority, disagreement, applicability, forbidden uses, correction history, and signature/hash.
2. **Evaluate the full Skill causal chain.** Log eligible retrieval opportunities, candidates shown, full content loaded, clauses adopted/rejected, affected artifact spans, and independently checked consequences.
3. **Freeze paper-to-release bridges.** Every reported row needs task/prompt/grader/data/configuration hashes and immutable raw result paths.
4. **Make GoT event-sourced and tamper-evident.** Append immutable events; hash-chain them; bind artifact content; preserve revisions as new nodes; validate parents and cycles.
5. **Separate asserted and observed edges.** Label self-report, inferred dependency, execution read/write, human-confirmed dependency, and mutation-supported causal edge differently.
6. **Join audit to complete evidence views.** Give the Auditor read-only GoT and execution provenance, preserve source snapshots, and use an independent re-execution lane where safe.
7. **Test Auditor validity.** Plant missing evidence, coherent fabricated files, wrong citations, leakage, stale outputs, contradictory traces, and omitted failures; report detection and false-alarm rates.
8. **Recompute RSC results.** Score trusted arrays/code outputs, not submitted headline numbers; bind figures and report claims to recomputed values.
9. **Calibrate human rubrics.** Add level anchors, required evidence, disqualifiers, multiple qualified raters, disagreement, and adjudication.
10. **Preserve all runs.** Retain failures and repeats, avoid best-of-two selection, report cluster-aware uncertainty, and type every missingness cause.
11. **Measure human oversight as work.** Record who intervened, what they saw, decision authority, correction, latency, burden, and downstream effect.
12. **Use cost frontiers, not cheapest anecdotes.** Include model, tools, compute, retries, expert verification, curation, maintenance, and failed-run cost.

## Concrete changes for skill-bench

1. **Do not create a neuroscience-specific subsystem.** BrainPilot is a bounded scientific-domain case for the charter's general expertise-to-benchmark hypothesis. Existing expertise-transfer, evidence, configured-system, trace, participation, artifact, metric, task-health, execution, and claim-validity records are the durable homes.
2. **Add one cross-domain domain-scaffold validity fixture only if it is not already covered.** The fixture should contrast `available`, `retrieved`, `loaded`, `adopted`, and `artifact-changing` Skill states; include one source-faithful but inapplicable rule, one citation-bearing distortion, one expert dispute, and one harmful adoption. Completion means the benchmark refuses to promote load counts into expertise or benefit.
3. **Extend trace validation with a current-release conformance slice rather than a new graph schema.** Plant an orphan, cycle, retrospective mutation, stale artifact hash, inferred-but-false edge, omitted failed attempt, and Auditor/GoT disagreement. Require immutable event history and typed edge authority.
4. **Make result-table reconstructibility a release requirement.** A paper row is release-audited only when raw run identity, configured-system manifest, task/grader/data hashes, score record, missingness, resource events, and table-building code reproduce it.
5. **Use portfolio language for BrainPilotBench.** Preserve four task-specific score vectors, eligibility, coverage, resources, and noncompensatory scientific-integrity gates. Do not macro-average them into general neuroscience-agent capability without an intended-use weighting argument.
6. **Keep human verification non-substitutable.** Auditor output may nominate issues and evidence gaps; only an authorized human record can establish accepted scientific judgment, and acceptance still does not establish downstream correctness.

The first two implications overlap existing implemented machinery for Skill authority, evidence transitions, persistent-workspace use, longitudinal decision necessity, and trace mutation. Repository searches found explicit availability/visibility/adoption states and existing provenance, dependency, mutation, and cross-record audits. To avoid duplicate building, this review adds no new queue task; the BrainPilot evidence should inform the next scheduled consolidation of those existing contracts.

## Claim boundary

The immutable BrainPilot v1 paper and two post-v1 official release snapshots establish a real open-source multi-agent research framework with a substantial neuroscience Skill library, workspace-oriented Auditor policy, editable curated trace graph, and four runnable preliminary domain task packages. The benchmark framework builds and passes 205 of 205 exercised tests, with three declared integration skips. The paper reports single-run configured-system results and plausible end-to-end case studies, including candid adverse knowledge ablations and scientific limitations.

They do **not** establish that 7,233 corpus items or 72/74 Skills are source-faithful, expert-authorized, correctly retrieved, adopted, or beneficial; that GoT is complete, append-only, acyclic, orphan-free, tamper-evident, causal, or root-diagnostic; that the Auditor independently verifies external truth or scientific validity; that released tasks exactly generated paper results; that reported score/cost tables are reconstructible; or that BrainPilot transfers domain expertise, accelerates discovery, matches expert researchers, lowers total operational cost, improves scientific outcomes, or is ready for consequential research use.
