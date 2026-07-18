# PaperRepro: implementation evidence recovery is not measured tacit-expertise transfer

## One-sentence contribution

PaperRepro combines citation-neighbor code, runtime feedback, and validation-selected cross-paper implementation patterns to reduce an official-result gap on a claimed ten-task paper-reproduction benchmark, but the design observes **configured code-source and debugging advantages**, not recovery of relational, somatic, or collective expert knowledge; benchmark inventory contradictions, target-code exposure ambiguity, comparator-resource confounding, and an unavailable release further prevent independent reconstruction of the result.

## Why this matters for `skill-bench`

This paper sits directly on the charter's expertise-to-evaluation boundary. It asks whether omissions in a professional artifact can be recovered from related artifacts, interaction with an environment, and repeated experience across cases. Scientific code reproduction is a bounded mechanism case, not a proposal to narrow `skill-bench` to machine learning.

The useful general question is:

> When does extra evidence help an agent complete omitted requirements, and what additional evidence would justify calling that improvement tacit-knowledge or expertise transfer?

PaperRepro's strongest design idea is a three-source intervention:

1. **relational evidence** from neighboring artifacts and implementations;
2. **interaction evidence** from execution, errors, logs, and performance; and
3. **cross-case procedural candidates** induced from recurring implementation outcomes.

Those are valuable benchmark primitives. The paper's category labels are not validated measurements, however. A copied module can help without representing tacit knowledge. Runtime debugging can improve a score without reproducing practitioner intuition. A model-generated rule retained because it improves a validation metric can be useful without being a community practice, source-faithful, expert-approved, or transferable. `skill-bench` should preserve the intervention and outcome while keeping the knowledge-status claim separate.

This review advances charter objectives A, B, C, and E through narrow expansion and claim-boundary consolidation. The concrete evidence is the full immutable paper and TeX source, a reproducible appendix-inventory/headline-arithmetic audit, and a time-bounded official-release search. Useful completion means distinguishing implementation-evidence recovery from expertise transfer and mapping the distinction into existing provenance, procedure, transfer, validity, task-health, and execution contracts rather than creating a paper-reproduction subsystem.

## Sources and reading record

### Immutable primary source read in full

- Lehui Li et al., *What Papers Don't Tell You: Recovering Tacit Knowledge for Automated Paper Reproduction*.
- Immutable arXiv v1: <https://arxiv.org/abs/2603.01801v1>; PDF: <https://arxiv.org/pdf/2603.01801v1>.
- Local PDF: `data/papers/pdfs/2603.01801v1-what-papers-dont-tell-you.pdf` (32 pages; SHA-256 `505f3d774edc5ab5314a73be83e1d630575fc722e8634b86a929f9a3c414b77e`).
- Local full text: `data/papers/text/2603.01801v1-what-papers-dont-tell-you.txt` (SHA-256 `6579d79f712ba4136063a5582b24976fb3543f1ead9a9c58a2af7c7a05bf1a5d`).
- Official arXiv TeX source: `data/papers/source/2603.01801v1/` (15 members); archive SHA-256 `ec8855b262ee79c7fc0dcd0067e62156219398092f4446e653f6d34c8f57363e`.
- Date read: 18 July 2026 UTC. The complete main text, benchmark appendix, baseline descriptions, prompts, proofs, tables, and figure captions were read. The inspected arXiv record contains no withdrawal notice.

### Release and internal-consistency audit

- Audit: `data/sources/releases/2603.01801v1-tacit-knowledge-reproduction/release-audit.json`.
- The paper says code will be released upon acceptance and a link added to the final version (abstract, p. 1). Neither the manuscript nor source contains a repository URL.
- Exact-title, arXiv-ID, mechanism, author, web, and GitHub repository searches on 18 July 2026 found no author-verifiable release. The similarly named `luolin101/PaperRepro` repository is an unrelated social-science reproducibility-assessment system and is not treated as evidence.
- Search absence is time-bounded; it does not prove that no private or later repository exists. At review time, however, the benchmark corpus, code, environments, induced knowledge bases, prompts-as-run, trajectories, results, and human ratings were unavailable for audit.

## Research question and claim boundary

The paper asks whether automated paper-to-code reproduction improves when an agent progressively receives citation-neighbor implementations, target execution feedback, and model-induced implementation practices from clusters of related papers (Sections 3–5, pp. 3–8).

The evidence, if the reported tables are accepted, supports a bounded claim:

> Under one unreleased benchmark and configured Claude Opus 4.5 pipeline, a package with graph pruning, neighbor-code relation analysis, iterative reference-metric feedback, and validation-selected cross-paper guidance achieved smaller official-result discrepancies than five reimplemented comparison packages.

It does **not** establish:

- that the package recovered knowledge held tacitly by experts;
- that its three mechanisms uniquely correspond to relational, somatic, and collective tacit knowledge;
- that the generated code is method-faithful or scientifically correct;
- that target code and answer-bearing resources were inaccessible;
- that the induced rules transfer across independent task, authoring, codebase, domain, or solver lineages;
- that performance-gap improvement causes greater reproducibility, research validity, professional utility, or reduced expert burden; or
- that the result can be reproduced from released evidence.

The paper's title-level thesis—paper reproduction is bottlenecked “not by information retrieval but by tacit knowledge”—is not tested against an information-matched alternative. The full method adds code, execution, target reference metrics, graph structure, cross-paper outcomes, validation selection, and compute together. Its gains cannot identify which omitted-information category was the bottleneck.

## Methodology and system

### Resource-relative taxonomy

The paper defines a target document `D`, official implementation `C`, required implementation decisions `Φ`, and four nested resource sets (Section 3.3, pp. 3–4):

- `R0`: target paper document;
- `R1`: `R0` plus documents and code for citation neighbors;
- `R2`: `R1` plus target execution feedback;
- `R3`: `R2` plus papers, implementations, and execution feedback from a broader implementation-related set.

A decision is called relational, somatic, or collective depending on the first resource level at which agent `A` can determine it. This is a clean **resource-sensitivity definition**, but it is not an empirical tacit-knowledge annotation. `Φ` is never independently enumerated, expert-held knowledge is never elicited, and successful determination is inferred from downstream code performance rather than decision-level labels.

The hierarchy assumes that adding resources cannot make determination worse. That monotonicity is especially fragile here: the paper motivates semantic pruning because extra papers can distract the model, cites distraction work, and reports that random graph partitioning hurts. For finite-context stochastic agents, more evidence can change attention, prompt length, tool use, and errors. Thus the formal categories are agent-, prompt-, resource-, and evaluation-relative treatment labels—not intrinsic properties of knowledge.

### Scientific graph pruning and relational aggregation

PaperRepro starts from target citation neighbors with public implementations. Five LLM reviewers rank candidate papers using Method and Experiments summaries; mean rank plus a rank-variance penalty selects a pruned neighborhood (Sections 4.1 and 5.1, pp. 4–6). Six experts later annotate associations in recommendation and time-series training sets, and the appendix reports Fleiss' `κ=0.82` plus retention of all “critical” nodes (Appendix C.1, pp. 10–11).

For each retained neighbor, an LLM classifies target implementation units as reusable, adaptable, or new, extracts or edits code into callable APIs, smoke-tests interfaces, and selects candidates using graph weight plus a fixed reuse bonus `β=0.15` (Section 4.2.1, pp. 4–5). The reported code-origin analysis says more than 70% of generated recommendation and time-series code is reused or adapted (Figure 7, pp. 7–8).

This is inspectable in concept, but “reused/adapted/new” is a model-produced provenance label, not an independently validated semantic lineage. Line counts or generated origin categories do not establish that the selected module implements the target method. The case study says a FREEDOM module was selected “consistent with” official PGL code (Figure 8, p. 8), which is an oracle-relative example and does not validate the classifier across tasks.

### Execution-feedback refinement

The initial implementation is repeatedly executed. The agent receives errors, logs, current metrics, and **reference metrics**, produces a diagnosis and patch, and stops when official-result discrepancy falls below a threshold or a maximum iteration budget is reached (Section 4.2.2, p. 5; Appendix F.4, pp. 29–30).

This is useful closed-loop engineering. It is not direct observation of “somatic” practitioner knowledge. The loop can discover shape errors, dependency defects, unstable training, or hyperparameters by search. More importantly, target reference metrics are answer-bearing feedback. Repeatedly optimizing against them can produce metric conformity without method fidelity, especially because the primary metric observes only final predictive performance. The paper does not report the stopping threshold, maximum refinement iterations, patch acceptance policy, per-attempt trace, or whether the same evaluation examples guide repair and final scoring.

### Graph-level induction

For each task, the method symmetrizes graph weights, applies Louvain clustering, reproduces papers within each subgraph, and asks an LLM to induce recurring trigger/action/rationale/verification/scope entries from refined implementations and execution outcomes (Section 4.2.3, pp. 5–6). Entries must exceed a frequency threshold and show “stable” validation gains. Training runs for three epochs; a validation-selected checkpoint is retained. At test time, guidance from the top three subgraphs is injected into reproduction.

The representation—trigger, action, rationale, verification, scope, frequency, confidence, evidence—is strong. The evidentiary status is not. The same system generates implementations, observes outcomes, induces rules, and selects them using its own validation endpoint. No expert verifies that a rule is a community convention, no source spans establish that practitioners use it, and no negative/misuse cases test scope. Frequency in a selected public-code cluster can reflect shared templates, libraries, authors, datasets, or benchmark leakage. Validation gain makes an entry a **benchmark-selected procedural candidate**, not “collective tacit knowledge.”

### Benchmark, configured systems, and scoring

The main text describes an extension of ReproduceBench covering recommendation, time series, and graph learning, with ten task types; 191 training, 30 validation, and 40 test papers; and two datasets per paper (Section 5.1, p. 6). Papers are said to be split by release date, with test papers after 2025 to mitigate contamination.

Five baselines are compared: ReAct, OpenHands, Paper2Code, DeepCode, and AutoReproduce. The appendix says all use Claude Opus 4.5, Python 3.10, PyTorch 2.7, CUDA 12.6, 64 A800 80GB GPUs, five reproduction attempts per paper, at most 50 LLM interaction rounds, deterministic seeds, and a two-hour timeout (Appendix E.3, p. 24). Baseline-specific recommended prompts are retained, while unavailable settings are tuned on validation data.

The primary endpoint is normalized absolute discrepancy between generated and official implementation performance; non-executable code receives generated performance zero (Eq. 12, p. 6). Three domain experts also rate method fidelity, experimental configuration, and code completeness on 1–10 scales. Table 1 reports task means and standard deviations over five runs; Table 2 reports method-level human means and Fleiss' kappa.

Equal backbone and hardware do not establish equal information or compute. PaperRepro uniquely receives citation-neighbor code, graph preprocessing, three epochs of reproduction over the training corpus, induced knowledge, and iterative target reference metrics. The manuscript does not give token/call counts, total GPU-hours, web/tool access logs, graph-building cost, or a baseline with the same evidence and budget but without the proposed organization. This identifies a whole-package contrast, not the effect of tacit-knowledge recovery or graph reasoning.

## Evidence and results

### Headline arithmetic

The ten displayed PaperRepro task means average to `10.038%`, reproducing the stated `10.04%`. AutoReproduce's ten means average to `34.72%`. Their difference is `24.682` **percentage points**; the relative reduction is about `71.09%`. The repeated claim that PaperRepro “improves ... by 24.68%” therefore uses a percent sign for an absolute point difference (Table 1 and Conclusion, pp. 7–8). The audit preserves the exact calculation.

The displayed PaperRepro means are lower than every baseline on all ten rows. That is substantial reported package-level evidence. But the denominator remains unclear. Forty test papers, two datasets per paper, five attempts/runs, and ten task aggregates create nested dependence. The paper does not say whether each cell first averages dataset, paper, seed, or successful attempt; how invalid/time-out runs enter beyond non-executable code; whether all five attempts are averaged or selected; or whether standard deviations are over seeds, papers, datasets, or their pooled observations. No paired paper-level effects, confidence intervals, task-cluster bootstrap, or multiplicity adjustment are reported.

### Benchmark inventory contradiction

The official TeX appendix permits a direct inventory audit. Counting rows under every train/validation/test marker yields:

- **171 training papers**, not 191;
- **21 validation papers**, not 30; and
- **40 test papers**, matching the claim.

The mismatch is not only numerical. Main Table 1 includes `GeneralGL` and `GSL` but omits Imputation and TGL. Appendix D inventories Imputation and TGL but has no `GeneralGL` or `GSL` sections. Thus the appendix's ten task identities are not the main result table's ten identities.

This blocks reconstruction of the training/validation graph, validation-selection denominator, and two main graph-learning rows. It also weakens the date-split claim: without stable paper IDs, immutable code revisions, and exact split manifests, one cannot test citation edges, shared repositories, duplicate implementations, author overlap, or whether test targets or their official code leaked into graph construction and prompt tuning.

### Human evaluation

Table 2 reports PaperRepro at `8.49` average versus AutoReproduce at `6.23`, with PaperRepro Fleiss' `κ=0.76` (p. 7). This is potentially useful evidence that the generated repositories differ beyond one performance scalar.

The protocol is too incomplete to support “methodological intent” or expert-equivalence claims. The paper does not report evaluator identities or qualifications, assignment counts, which of 40 papers and five runs were rated, blinding, randomization, anchor examples, exact ordinal categories used for kappa, duplicate-label counts, disagreement/adjudication, criterion weights, uncertainty, or rating-level data. Fleiss' kappa is defined for categorical labels; the manuscript does not explain how 1–10 ratings were converted or whether ordinal distance was respected. One method-level mean cannot establish code correctness or general rater reliability.

### Ablations and transfer

Table 3 removes SSGP, node aggregation, execution feedback, or graph induction and reports only RecSys and TimeSeries aggregates, with no Graph Learning row, standard deviations, paired task effects, or resource-normalized controls (p. 7). Removing execution feedback hurts most, but that intervention also removes repeated execution, reference-metric observation, repair opportunities, and likely calls/compute. It does not isolate “somatic knowledge.”

Cross-model Figure 4 says induced guidance trained with Claude Opus 4.5 or Qwen3-Next-80B-A3B-Thinking improves four target models by `9.4%–13.2%` (p. 7). The underlying cells, model snapshots, task/paper denominators, run counts, variances, guidance hashes, and equal-context controls are absent from text and release. Transfer across model labels on the same task/code/validation lineage is weaker than transfer across independent work contexts. Figure 5 compares graph-based and random partitions, but graph partitioning can exploit shared implementation lineage without discovering community knowledge. Figure 6's progression from device rules to “methodological insight” is an author-selected narrative, not a validated knowledge trajectory.

## Unique insight: knowledge status must not be inferred from the channel that produced a useful patch

PaperRepro's most important transferable lesson is a claim-boundary failure:

> **The source of an intervention does not determine the epistemic status of its content.**

Neighbor code creates relational evidence, not automatically relational tacit knowledge. Execution creates interactive evidence, not automatically somatic knowledge. Cross-case induction creates a procedural candidate, not automatically collective knowledge. A candidate becomes evidence of transferred expertise only through additional links:

`source/participant authority → omitted decision identified → representation with scope and provenance → delivery opportunity → observed adoption → locally valid consequence → held-out transfer → professional acceptance/consequence`

PaperRepro mainly observes configured resource exposure and oracle-relative endpoint change. It does not observe the first, second, sixth, eighth, or final links robustly. This distinction matters beyond science. A finance agent may infer a spreadsheet convention from neighboring models; a legal agent may repair a filing after a validator error; an operations agent may induce a checklist from prior successful cases. Those can be effective system mechanisms while still being unsupported as expert practice.

For `skill-bench`, label candidate knowledge by **production and validation state**, not evocative category alone:

1. `artifact-derived candidate`;
2. `execution-induced repair heuristic`;
3. `cross-case recurring candidate`;
4. `source-entailed procedure`;
5. `authorized expert-approved procedure`;
6. `held-out locally effective procedure`;
7. `cross-context transferable procedure`;
8. `professionally accepted/useful procedure`.

These states may overlap; none should be promoted from one to another solely because endpoint performance improved.

## Transferable benchmark-design implications

### Retain

- **Typed evidence channels.** Separate target document, neighboring artifacts/code, runtime feedback, cross-case histories, and reference outcomes.
- **Implementation-unit lineage.** Record reuse, adaptation, and new construction at module/symbol granularity with source revision, license, transformation, and tests.
- **Trigger/action/verification/scope procedural records.** PaperRepro's induced-entry shape is stronger than free-form tips.
- **Closed-loop repair traces.** Preserve error → observation → diagnosis → patch → execution → outcome rather than only final code.
- **Date- and lineage-aware splits.** Time is useful, but it must be joined with repository, author, template, citation, dataset, and feedback-lineage controls.

### Repair

- Replace tacit-category assignment by resource level with a **knowledge-status ledger** carrying producer, source authority, evidence locator, transformation, expert review, scope, contradiction, validation population, and transfer edge.
- Separate `target paper`, `neighbor implementation`, `official comparator`, `reference metric`, and `grader` roles. Each needs an explicit access policy and trial-time firewall.
- Add matched conditions: document only; document plus neighbors; document plus execution without reference metric; document plus execution with blinded held-out checks; induced candidate versus independently authored procedure; equal-token/equal-call/equal-GPU envelopes.
- Preserve endpoint vectors: executability, method identity, configuration fidelity, result correspondence, robustness, provenance, and scientific validity. Do not let a normalized performance gap stand in for reproduction.
- Treat official implementation as one comparator witness, not ground truth. It can contain bugs, undocumented assumptions, and one path among legitimate alternatives.
- Cluster uncertainty at paper/codebase/task lineage and report attempt-selection and missingness policies explicitly.

### Test

A reusable cross-domain test would construct paired tasks where an important requirement is omitted from the target artifact but recoverable through one controlled channel. Freeze source and target lineages; plant both useful and misleading neighbor practices; vary whether runtime feedback exposes only errors or answer-bearing reference metrics; then measure candidate extraction, adoption, local correctness, negative transfer, and held-out context transfer separately. The general hypothesis is whether evidence-channel organization improves valid requirement recovery without laundering benchmark feedback into “expertise.”

## Limitations and validity threats

1. The paper's tacit categories are defined by staged resources and agent success, not expert elicitation or decision-level ground truth.
2. `Φ`, the set of required decisions, is not independently enumerated or released.
3. The monotonic-resource assumption conflicts with finite context, stochasticity, distraction, and the paper's own pruning motivation.
4. All resource transitions bundle information, prompting, calls, tools, and compute.
5. Neighbor relevance and reuse/adapt/new relations are model-generated; validation is narrow and incomplete.
6. Six expert annotators cover only recommendation and time series training graphs; credentials, label protocol, denominators, and raw annotations are absent.
7. “Retains all critical nodes” lacks false-positive, calibration, and held-out task analysis.
8. Runtime repair sees reference metrics, creating answer-bearing feedback and potential target overfitting.
9. The stopping threshold and maximum refinement budget are unspecified.
10. The primary endpoint does not establish that generated code implements the claimed method.
11. Official implementation performance is treated as the comparator without validity or alternative-path analysis.
12. Test-paper official GitHub links are listed while trial-time target-code access controls are not specified.
13. Baselines have web access, but target-code blocking, mirrors, package provenance, and network logs are not reported.
14. PaperRepro receives materially different evidence and training compute from baselines; equal backbone/hardware is not equal treatment opportunity.
15. Prompt tuning for missing baseline settings can create unequal optimization and investigator degrees of freedom.
16. The claimed `191/30/40` inventory conflicts with the appendix's `171/21/40` rows.
17. Main-table task identities conflict with appendix task identities.
18. Forty papers × two datasets × five runs are collapsed without a complete aggregation or dependence policy.
19. Standard-deviation units and attempt selection are unclear; no paper-clustered inference is reported.
20. The stated `24.68%` gain is a 24.682-point difference, not a 24.68% relative reduction.
21. Human evaluation lacks released assignments, ratings, blinding, ordinal-kappa semantics, uncertainty, and adjudication.
22. Ablations omit graph-learning results and uncertainty and do not equalize calls/feedback/compute.
23. Cross-model transfer shares task, implementation, induced-rule, and validation lineage and lacks released cell-level evidence.
24. No cross-domain transfer experiment is reported despite three evaluation domains.
25. No code, benchmark, split manifest, official-code snapshot, environment image, induced knowledge base, trajectory, result ledger, or human label is released.
26. The 64×A800 setup, repeated paper reproductions, proprietary model endpoint, mutable web/code dependencies, and absent cost ledger make operational replication expensive and underspecified.
27. The manuscript has no explicit limitations section and makes broad reproducibility-impact claims without measuring scientific validation, user burden, or downstream consequence.

## Comparison with adjacent reviewed systems

- **PaperBench** fixes an external author-assisted criterion inventory and exposes dense partial progress, but its compensatory score does not establish successful replication. PaperRepro uses a much thinner result-gap endpoint and an unreleased inventory; it adds richer neighbor/debugging interventions but weaker obligation and grader inspectability.
- **Paper-replication workspace** preserves target → execution → artifact → comparison → report lineage and explicitly separates workspace closure from scientific fidelity. PaperRepro reports better endpoint proximity without releasing the target inventory, execution graph, or artifact bindings needed to inspect how that proximity arose.
- **DeployBench** isolates fresh-machine execution and hidden-target deployment evidence. PaperRepro bundles implementation generation, environment execution, reference-metric feedback, and result comparison; executability and scientific reproduction should remain separate.
- **ReasFlow** represents procedural candidates as scoped, actionable knowledge cards but validates them through model-generated/model-judged loops. PaperRepro's induced entries have the same epistemic risk: validation-selected procedural text is not source-faithful or expert-approved merely because it improves an endpoint.
- **AFTER** supplies the right transfer-graph warning: source task, solver, updater, procedure version, target lineage, and feedback view must be independently identified. PaperRepro's cross-model figure shares task/code/validation lineage and therefore does not establish broad procedural transfer.
- **Existing expertise-transfer machinery** already has the right homes: elicitation/claim provenance for authority, procedure-package lineage for the intervention, benchmark-bundle traces for execution and evidence views, compounding lessons for candidate promotion/rollback, longitudinal records for feedback exposure, validity arguments for claim ceilings, task health for instrument defects, and metric specifications for clustered aggregation. The paper motivates stricter use of those contracts, not a new schema.

## Reproducibility and operational realism

Paper inspectability is good: the 32-page PDF includes formal definitions, major prompts, baseline descriptions, benchmark paper titles, headline tables, and hyperparameters. The immutable TeX source makes internal inventory and arithmetic audits possible.

Experiment reproducibility is poor. The benchmark and system are not released; appendix and main-text inventories disagree; target and neighbor code revisions are unpinned; proprietary model identity and API configuration are incomplete; web and filesystem access policies are missing; environment images, data versions, commands, seeds, timeouts-as-realized, retries, invalid runs, and raw metrics are absent; and 64 A800 GPUs plus repeated training/test reproduction impose a large unreported resource burden. The result is not currently replayable, and even exact replay would establish only the configured benchmark result—not tacit-expertise transfer or scientific validity.

Operationally, citation-neighbor reuse and execution feedback are realistic parts of research engineering. Repeated exposure to official reference metrics is less realistic as a blinded reproduction test and more like test-driven tuning against an answer-bearing oracle. A production evaluation should distinguish legitimate public evidence, privileged comparator observations, and private final checks, and should price graph construction, source acquisition/licensing, execution, model calls, expert review, and maintenance.

## Concrete repository changes and next actions

1. **Index this review and preserve the audit.** Add it to `data/papers/index.json` and `papers/topic-index.md`; retain `release-audit.json` as the machine-readable evidence for the `171/21/40` inventory, task-identity mismatch, release search, and headline arithmetic.
2. **No new build task.** The requirements map without duplication to existing expertise-transfer, procedure, compounding-lesson, benchmark-bundle, execution-isolation, validity, task-health, metric, and longitudinal contracts. A future consolidator should integrate the specific distinction `evidence-channel treatment ≠ knowledge-status claim` when next updating the canonical taxonomy and research synthesis.
3. **For any pilot using inferred procedures, require a claim ladder.** Report artifact-derived candidate, execution-induced candidate, expert-approved procedure, held-out local effect, transfer, and professional utility as separate statuses; preserve source/target firewalls and comparator visibility.
4. **For scientific or other executable tasks, run an oracle-access ablation.** Compare error-only feedback with reference-metric feedback and held-out private checks under equal call/token/compute budgets. A gain that disappears without answer-bearing metrics is debugging-to-oracle adaptation, not evidence of recovered tacit expertise.

No capability, scientific-correctness, expert-equivalence, cross-domain transfer, professional-validity, utility, or readiness claim is licensed by this review.