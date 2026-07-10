# Paper and Release Review: DELEGATE-52 — Cycle Consistency Exposes Drift but Does Not Prove Edit Success

- **Paper:** https://arxiv.org/abs/2604.15597v1
- **Date read:** 2026-07-11
- **Primary evidence:** immutable arXiv v1, 36 pages
- **Local PDF:** `data/papers/pdfs/2604.15597v1-delegate52-llms-corrupt-your-documents.pdf` (SHA-256 `e19de696479dd9f671110640bde0abd8f3741b8ec2202ab1a5ed5d731de3151f`)
- **Local text:** `data/papers/text/2604.15597v1-delegate52-llms-corrupt-your-documents.txt` (SHA-256 `5d07d6967a1cb00b181195db41b50f253eea9db3afa223a6bd3a65828cf880a3`)
- **Official release:** https://github.com/microsoft/DELEGATE52 at commit `b896b804fdd29032f04aacc519c5cfa66e34226d`; archive `data/sources/releases/2604.15597v1-delegate52/microsoft-DELEGATE52-b896b80.zip` (SHA-256 `4abc5c12a0f5104b661fb6460e4f702d03c3cd164dcdc0867a08f49dfa9e3d5d`)
- **Dataset:** https://huggingface.co/datasets/microsoft/delegate52 at revision `9d325644687cc69533f8070e4decfc9cbf057b12`; local JSONL `data/sources/releases/2604.15597v1-delegate52/delegate52-9d32564.jsonl` (SHA-256 `5618f5ab6394e1d2befde3bc8dd50e247bbc872472999eafd9f075c734b488d4`)
- **Provenance:** `data/sources/releases/2604.15597v1-delegate52/provenance.json`
- **Tags:** document-editing, artifact-integrity, cycle-consistency, long-horizon, verifier-validity, delegation

## One-sentence contribution

DELEGATE-52 introduces a broad, automated stress test in which models repeatedly apply paired forward/inverse edits to real textual artifacts and are scored against the original by 52 domain parsers; it compellingly demonstrates cumulative cycle inconsistency under the tested configurations, but reconstruction alone cannot establish that requested forward edits succeeded, that collateral changes are professionally consequential, or that a model is ready for delegated work.

## Why this matters for skill-bench

This review advances charter objectives A, B, and C. It audits a cross-domain mechanism for measuring a central knowledge-work risk: an agent may satisfy a requested delta while silently damaging properties the user never asked to change. The concrete evidence is the complete v1 paper, pinned code, the full public 234-environment dataset, and three end-to-end environment traces.

The key uncertainty is **which claim cycle consistency licenses**. DELEGATE-52 measures whether an artifact survives a model-mediated edit-and-inverse cycle. That is valuable integrity evidence. It is not direct evidence that either edit was correctly executed, that the inverse is a realistic later request, or that every parser-visible difference is semantic corruption. This is cross-domain methodological expansion, not a proposal to narrow `skill-bench` to document editing.

## Research question and claim ladder

The paper asks whether LLMs can execute long delegated document-editing workflows without cumulative corruption. Its interpretation moves through:

```text
real source artifact
→ researcher/LLM-authored reversible edit pair
→ forward model output
→ inverse model output
→ parser-weighted similarity to the seed
→ artifact-preservation capability
→ delegated-work readiness and trust
```

The experiment strongly instantiates the middle chain. The first and last links require more evidence: source realism does not make authored transformations professionally representative, and reconstruction loss is not itself a calibrated readiness or trust threshold.

## Methodology and system

### Benchmark construction

The authors brainstormed more than 100 candidate domains with LLM subagents and selected 52 textual, unencoded formats across five categories. Each domain has six environments, for 310 total, with a 2–5k-token seed, 5–10 reversible edit pairs, and 8–12k tokens of related distractors (paper §§2.2, K.1–K.8, pp. 3–4, 30–34). Seed documents came primarily from GitHub and public repositories; provenance and license were recorded. Personas inspired edits, but the paper reports no domain-expert elicitation, practitioner authorship, or expert acceptance study.

The eight-stage pipeline is substantial: parser/evaluator construction; isolated round-trip tests with GPT-5.2 and GPT-5 Mini, five runs per pair; low-score triage; scaling; LLM prompt minimization and semantic tagging; all-edit testing; LLM-based distractor-interference review; and 23 structural checks. It produced 2,125 edit pairs in the full benchmark (pp. 30–34). AI assisted curation, code, QA classification, prompt rewriting, and appendix writing (p. 13).

### Round-trip relay

For an artifact `s`, model `M` applies forward instruction `x→` and inverse `x←` in independent single-turn sessions. A domain evaluator computes `sim(s, ŝ)`, and ten round trips are chained in shuffled round-robin order for 20 interactions (pp. 2–5). Because intermediate references are unnecessary, this scales cheaply. But the atomic observation is the *composite* `M(x←; M(x→; s))`; the paper explicitly acknowledges that it cannot localize forward versus backward failure and that a high score may follow a poor or trivial forward edit (Appendix B, pp. 20–22).

### Evaluators

Each domain parser maps files to structured elements and computes a [0,1] weighted score. Ablation removes `K` of `N` logical blocks and requires score no greater than `1-K/N`; preprocessors tolerate selected formatting variants (pp. 4, 30–33). This is better than generic string or embedding similarity for the benchmark's chosen semantics. A post-hoc stratified comparison over 9,851 entries finds GPT-5.4 judge correlation of `.634` overall and `.474` on length-matched cases against the domain metric (pp. 22–23).

That comparison treats the custom score as criterion rather than independently validating it. Correlation shows generic methods disagree; it does not prove the custom parser is sound or complete. Block deletion mainly tests sensitivity to omissions, not false acceptance of additions, cross-field contradictions, invalid syntax, alternate legitimate representations, or professionally severe low-weight changes.

### Experimental design and evidence

Nineteen models from six families are run over the relay. Table 1 reports RS at every two interactions; the best three average roughly 25 points of loss by interaction 20, while the model average loses roughly 50 points (pp. 5–6). The paper reports sparse critical drops: thresholded ≥10-point round-trip losses account for 80–98% of gross degradation, and most models have at least one by round 20 (pp. 9, 25–26).

Targeted experiments compare four GPT-family models with a basic tool harness; vary GPT-5.4 document size over five selected scalable domains; extend four models to 100 interactions; remove distractors for four models; and compare round-robin to repeated-single-edit relays in one environment from 50 domains (pp. 6–8, 24, 28–29). These are informative mechanism probes, but there are no confidence intervals, environment/task-clustered uncertainty estimates, paired-seed details, missing/error policy, or model-level repeated main relays. Random task order is a material treatment when prior corruption changes later feasibility.

## Pinned release audit

The official archive contains the runner, agentic harness, and 52 domain modules. The pinned public JSONL contains **234 environments, 48 domains, 1,629 forward edits, 1,863 states, and 1,505 embedded files**. All 234 records have a nonempty origin and license field, spanning 82 literal license strings. Counts per released domain range from one (`recipe`, `slides`) to seven (`python`), rather than six uniformly. Four domains and 76/310 environments are withheld for licensing; therefore full-paper results are not reproducible from the public denominator and public domain mixtures differ.

The repository and dataset appear contemporaneous with v1 acquisition, but no manuscript-time result tables, model outputs, random schedules, failure annotations, QA logs, or exact full 310-environment corpus are released. The public code can reproduce new runs, not independently audit the reported ones.

### Trace 1: accounting ledger (`accounting1`)

The released Hack Club ledger records an ODC-By origin, one seed ledger, four distractor files, and ten forward edits. Examples split transactions by reimbursement recipient/category or convert the ledger to CSV; inverse prompts merge or convert back. The public graph has a return edge for every forward edge.

`domain_accounting.py` parses transactions and scores reference coverage, postings, amount, and comments. It is robust to some formatting changes, but its matching denominator is reference transactions. Extra unmatched candidate transactions do not directly reduce coverage or component averages. Thus a reconstructed ledger could retain every original transaction while adding unauthorized transactions and still receive a perfect score. This is precisely collateral corruption, yet the released evaluator can miss it. Comment statistics also appear defective: `compute_domain_statistics` checks singular `comment` keys although parsed records store `comments`.

### Trace 2: 3D fireplace (`obj3d1`)

This environment has OBJ/MTL seed files under Free Art License 1.3, five distractor documents/files, and edits that split by material, convert to JSON, or merge named parts into functional components. Inverses depend on generated bookkeeping (`manifest.txt`, component maps) to restore ordering.

`domain_obj3d.py` parses groups, vertices, faces, materials, and geometry. This makes preservation more inspectable than rendered-image judging, but its semantics are parser-defined: malformed face specifications are silently skipped, names drive group alignment, nearest-neighbor vertices ignore some topology, and count/material mixtures do not establish render equivalence or model validity. The bookkeeping file also changes the construct: restoration can become following an answer-bearing map rather than retaining knowledge through the artifact transformation.

### Trace 3: chocolate éclair recipe (`recipe1`)

The sole released recipe environment declares origin `n/a` and license `original content MIT`, despite the paper and dataset card repeatedly describing seed documents as real, online, and nonsynthetic. Its forward edits split the recipe, rewrite it as a personal blog post, and scale/convert units; inverse prompts reconstruct the formal recipe.

`domain_recipe.py` parses only lines matching `Ingredient N:`, `Step N:`, and `Tip N:`. Ingredient and tip matching divide by the number of reference items; extra candidate ingredients/tips are unpenalized. Step scoring incorporates candidate count only through `min(candidate, reference)/reference`, so extra steps also do not lower coverage, though they may affect text similarity. Unparsed prose is invisible. An artifact can therefore contain dangerous extra ingredients, instructions, or narrative while preserving recognized reference elements and scoring highly. Moreover the blog forward edit intentionally asks the model to invent a grandmother story and historical commentary, then the inverse deletes it; calling all such differences “corruption” conflates requested synthetic expansion with preservation risk.

### Release-wide graph and provenance checks

A static audit found a return-to-start inverse edge for all 1,629 public forward prompts. That confirms graph shape, not semantic invertibility. Many inverses rely on maps or position files created during the forward step, and the paper's “unique transformation path” is not proven by reference intermediate states or expert review. Public metadata enables source tracing, but literal license labels are not normalized and source authority/professional representativeness is not assessed.

## Evidence and claim boundaries

**Strongly supported:**

1. The authors built a broad, inspectable framework for repeatedly stress-testing parser-visible artifact preservation.
2. Under the reported model/configuration/schedule combination, reconstruction scores decline substantially with relay length.
3. Larger documents, more task diversity, and distractors are associated with worse reconstruction in the targeted ablations.
4. Failures are often concentrated in large round-trip score drops rather than smooth marginal loss.
5. Domain-specific structured evaluation captures distinctions that generic similarity methods do not reproduce.

**Partially supported:**

- **Instruction attempts:** a GPT-5.4 judge labels 93.8% of a score-stratified 12,409-step sample fully/partially attempted, but 16.7% are partial, no human reliability is reported, and stratification does not estimate natural prevalence without weights (pp. 19–20).
- **Tool effect:** the tested basic harness performs worse for four models, but it changes context exposure, interaction budget, token use, output method, and distractor access; this is not “agentic tools do not help” generally.
- **Semantic corruption:** custom scores detect selected parser-visible changes, but the release contains false-acceptance surfaces and no domain-expert consequence calibration.
- **Cross-domain breadth:** 52 formats are broad coverage, not a sample of occupations, professional tasks, or artifact consequences.

**Not supported by v1:**

- Correct completion of forward edits from reconstruction score alone.
- “25% of document content” as a literal fraction of professionally meaningful content; it is loss under heterogeneous weighted parsers.
- A universal 98% readiness threshold or delegated-work trust decision.
- Human-AI workflow realism; the official release explicitly says it is not intended to simulate realistic human interaction.
- Professional validity of researcher/LLM-authored edits and weights.
- General superiority of no-tool operation over optimized agent systems.
- Reproduction of full-benchmark results from the 234-environment public subset.

## Unique insight

DELEGATE-52 makes clear that artifact evaluation needs **two orthogonal axes**:

```text
requested-delta correctness: did the edit achieve what was asked?
preservation-envelope correctness: did everything outside the authorized delta remain valid?
```

Round-trip reconstruction is a clever, scalable probe of the second axis, but only after the inverse operation and only through a parser. It cannot replace a forward-state witness/check. Conversely, a conventional task grader may verify the requested delta while ignoring collateral damage. A trustworthy benchmark must evaluate both on the same transition.

The deeper design requirement is an **artifact transition contract**:

```text
initial authoritative state
+ authorized mutation scope
+ must-change predicates
+ must-preserve predicates
+ permitted normalization/invariances
+ forbidden additions/deletions
+ intermediate and final observations
+ recovery/reversibility policy
→ transition outcome and licensed claim
```

Cycle consistency is one metamorphic test within that contract, not ground truth. It is especially useful when no unique forward reference exists, but it should be paired with execution/compliance checks and adversarial additions. This separates requested change, benign normalization, semantic corruption, stale initial defects, parser invalidity, and failed recovery.

## Limitations

1. Domains and edits were researcher/LLM brainstormed; no expert elicitation or professional acceptance evidence is reported.
2. Six environments per domain are convenience selections, not a task-distribution sample.
3. Real-source provenance does not prove representative or defect-free initial artifacts; `recipe1` is original content despite nonsynthetic claims.
4. Reversible, precise, structured edits exclude much consequential communication, judgment, deletion, and open-ended revision work.
5. Forward success is unobserved by the main metric; composite round trips obscure failure location and cancellation.
6. Partial execution can inflate reconstruction; 16.7% of judged steps are partial.
7. Bookkeeping artifacts can make inverse recovery artificially easy and leak restoration information.
8. Parser/evaluator validation emphasizes deletion sensitivity, not necessity, sufficiency, alternative validity, additions, or adversarial gaming.
9. Released accounting and recipe evaluators can under-penalize unauthorized additions.
10. Heterogeneous weights make “percent content corrupted” nonliteral and cross-domain comparability uncertain.
11. No expert severity study calibrates parser-score drops to professional consequence.
12. The 98% readiness threshold has no decision-loss, downstream acceptance, or human baseline basis.
13. Main-run uncertainty, stochastic repeats, order variance, clustered intervals, and missing/error policies are absent.
14. Critical-error thresholding at ten points is uncalibrated and round-trip, not interaction, localized.
15. The tool comparison changes several treatment dimensions and tests only a basic harness on four models.
16. Public release excludes 24.5% of environments and four domains; full reported results cannot be audited.
17. Reported trajectories, schedules, QA histories, and result tables are not released.
18. This audit inspected all public record structure and three environments/evaluators deeply, but did not spend money to rerun the 19-model experiment.

## Reproducibility and operational realism

Reproducibility is mixed. The immutable paper, pinned code, versioned public JSONL, complete domain modules, model IDs, prompts, and runner provide far more operational detail than paper-only benchmarks. The agentic Python tool is bubblewrap-isolated with read-only system mounts, workspace-only writes, disabled network, and timeout (Appendix M, pp. 34–35).

Exact result reproduction is blocked by withheld environments, API model mutability/access, absent outputs and schedules, and no frozen dependency/environment image. Operational realism is intentionally bounded: independent single-turn calls, no user review, clarification, approvals, version control, downstream consumer, or correction loop. Distractor files are restored each round and their edits discarded, while seed damage persists—an asymmetric state policy unlike many real workspaces. The released card properly warns against human, commercial, high-risk, and real-world claims.

## Comparison with adjacent skill-bench evidence

- **Workspace-Bench:** evaluates retrieval and artifact production in large file substrates. DELEGATE-52 adds repeated mutation and restoration, but has weaker observed-use and forward-success evidence.
- **MBABench/action safety:** consequential actions require explicit allowed/forbidden side effects and recovery. DELEGATE-52 reveals collateral artifact damage but does not assign consequence severity or authorization boundaries.
- **Artifact-view admissibility:** DELEGATE-52 correctly prefers structured representations, yet its parser false-acceptance surfaces show why representation admissibility is necessary but insufficient.
- **Initial-state validity:** a round trip compares against the seed, but it does not establish that the seed was professionally correct. Preservation can faithfully retain stale defects.
- **Evidence-chain machinery:** the benchmark has source URLs/licenses and graph states, but professional claim authority does not propagate from a real source into researcher/LLM-authored transformations, parser weights, or readiness decisions.

## Transfer to skill-bench

### Preserve

1. Use repeated transitions, not only final one-shot artifacts, to expose compounding drift.
2. Keep authoritative structured artifacts and domain parsers alongside human/rendered views.
3. Pair every transformation with explicit inverse/recovery semantics where reversal is professionally meaningful.
4. Store every intermediate artifact and score so earliest corruption can be localized.
5. Test context size, distractors, workflow length, task diversity, and harness as separate factors.
6. Preserve source URL, license, redistribution status, and immutable public/private denominator.

### Correct

1. **Dual-axis transition grading:** independently score forward requested-delta success and preservation-envelope integrity; never infer the first from cycle consistency.
2. **Typed preservation predicates:** declare forbidden additions/deletions, invariant fields/relations, allowed normalizations, scope, authority, and consequence severity before trials.
3. **Three-way artifact comparison:** initial → forward → recovered, with per-step provenance and root/surface diagnosis; composite-only scores are insufficient.
4. **Verifier falsification:** add unauthorized extras, duplicate records, contradictory fields, malformed-but-parseable content, parser omissions, benign reorderings, and alternate valid forms. Test both false acceptance and false rejection.
5. **Initial-defect ledger:** distinguish preserved pre-existing defects from agent-introduced corruption and task-authoring defects.
6. **Recovery realism:** mark whether inverse instructions and bookkeeping are natural workflow operations, synthetic probes, or answer-bearing aids.
7. **Consequence-calibrated thresholds:** readiness requires expert/downstream acceptance, error severity, review burden, and loss basis—not an arbitrary aggregate 98%.
8. **Hierarchical measurement:** repeat schedules/trials and report task, environment, domain, and configured-system uncertainty with invalid/missing outcomes separate.
9. **Denominator honesty:** report full/private and redistributable/public suites independently; do not project 48-domain public behavior to 52-domain full results without bridge evidence.

## Concrete next actions

1. **Add one nonduplicate build task:** create a compact artifact-transition conformance slice within the existing benchmark-bundle validator. It should represent authorized delta, must-change/must-preserve/forbidden-change predicates, initial/forward/recovered observations, and recovery legitimacy; planted cases should include forward no-op with perfect round-trip, correct requested edit plus unauthorized addition, benign normalization, pre-existing defect, parser-invalid output, and failed inverse.
2. Reuse the released accounting extra-transaction and recipe extra-content surfaces as provenance-linked adversarial fixtures; a candidate containing all reference elements plus harmful additions must not receive full preservation credit.
3. When any pilot edits an existing artifact, require an initial→forward→recovered transition report and keep requested-delta score separate from preservation score.
4. Do not use cycle consistency alone for capability, professional-readiness, or trust claims.

## Action items

- [x] Read the complete immutable arXiv v1 paper.
- [x] Inspect the complete pinned official code archive and public dataset revision.
- [x] Reconcile the 310/52 full and 234/48 redistributable denominators.
- [x] Audit all public graph return edges and metadata presence.
- [x] Trace accounting, OBJ/MTL, and recipe environments from source through prompts and evaluators.
- [x] Identify concrete false-acceptance and construct-validity boundaries.
- [x] Map findings against adjacent repository machinery.
- [ ] Validate artifact-transition predicates with domain experts and downstream acceptance before readiness claims.
