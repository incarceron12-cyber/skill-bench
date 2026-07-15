# Skills Are Not Islands: declared dependency reachability is not installed, invoked, or harmful behavior

## Bottom line

*Skills Are Not Islands* contributes a useful representational correction: a procedural Skill is not necessarily one self-contained prompt file. Its operational boundary may include other Skills, software packages, and external services, and the identity, source, version, relationship evidence, and transitive closure of those components matter to reproducible agent evaluation. The proposed SkillBOM makes this boundary explicit and the paper's two-annotator study provides meaningful—though unreleased—evidence that dependency clues can be extracted from mixed YAML, instructions, and scripts.

The paper does **not measure agent capability or realized supply-chain risk**. Its graph primarily represents dependencies inferred from static text and registry state. It does not observe what was installed, loaded into model context, selected, invoked, authorized, reached, or allowed to alter state during a trial. Optional, example-only, declared, install-time, runtime, and service-authority relations are not represented as separate estimands. Consequently, a path from a root Skill to a flagged package, regex, or service is evidence for **audit reachability**, not evidence that a vulnerable version was present, malicious content was visible to the model, an agent adopted it, a dangerous action was attempted, or harm occurred.

The strongest empirical claim is also narrower than “whole dependency graphs accurately and comprehensively.” SKILL-DEP's direct layer has 500 stratified documents and very high annotator overlap; its multi-layer layer has only 100 depth-selected Skill graphs, no competing graph extractor, and no reported package/service transitive gold breakdown. The same authors developed the analyzer, annotation guideline, and benchmark, while the code, labels, schema, snapshot, outputs, and manual security confirmations are not released. The reported F1 values cannot be independently reproduced, and the 1.43-million-root findings inherit unquantified extraction, identity-resolution, duplication, repository-clustering, and snapshot errors.

The unique transferable insight for `skill-bench` is a **configured-component realization ladder**:

`declared/reference evidence → resolved versioned component graph → installed/mounted graph → model/tool-visible graph → selected/invoked graph → attempted action → realized state/information-flow consequence → diagnosed harm or utility`.

A benchmark must freeze and observe each relevant rung. A SkillBOM-like lock is valuable as configured-system identity and preflight evidence, but static transitive reachability must not be promoted into trial exposure, causal skill effect, safety, professional validity, or readiness.

## Why this matters: charter relevance and decision filter

This review advances charter objectives A, B, and C through narrow expansion and instrument validation. Public agent Skills are a methodological case for configured interventions, not a proposal to narrow the benchmark to coding assistants or to optimize Hermes for its own sake.

- **Objective advanced:** configured-system evaluation, evidence traceability, intervention/instrument separation, safety diagnosis, and reproducibility.
- **Concrete evidence:** immutable v1 PDF/text, a full method/results audit, and a release-availability record.
- **Uncertainty clarified:** whether a single Skill hash is enough to identify an intervention, and what a static dependency/risk graph can validly establish.
- **Mode:** expansion with a bounded build implication.
- **Duplication check:** SkillsBench, LH-Bench, Agentic Skills at Scale, and SLBench evaluate Skill effects or relations; none locally models transitive Skill/package/service realization across a trial.
- **Useful completion:** preserve a typed configured-component graph while separating static declarations from observed runtime realization and consequence.

## Sources and reading record

### Immutable primary source read in full

- Changguo Jia, Tianqi Zhao, Runzhi He, and Minghui Zhou, *Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply Chains*.
- Immutable arXiv v1: <https://arxiv.org/abs/2607.01136v1>; PDF: <https://arxiv.org/pdf/2607.01136v1>.
- Local PDF: `data/papers/pdfs/2607.01136v1-skill-supply-chain.pdf` (11 pages; 1,037,259 bytes; SHA-256 `4337dc42449e48c22fd162b230d9473c4509d62e21cbb55702713f0ff9c11e7a`).
- Complete layout extraction: `data/papers/text/2607.01136v1-skill-supply-chain.txt` (85,543 bytes; SHA-256 `0010520e0a3dda224d84f91705ef15d7a11a38a495a7c9a7dbec4dcf33cbb556`).
- Read 15 July 2026 through the final references. The local PDF title, full byline, 11-page count, and v1 marker were verified. The canonical abstract page says submitted 1 July 2026 and showed no withdrawal or retraction notice.

### Release status

Provenance and the negative release audit are recorded at `data/sources/releases/2607.01136v1-skill-supply-chain/provenance.json`.

The paper and canonical abstract page provide no artifact URL for SkillDepAnalyzer (SDA), SKILL-DEP, the SkillBOM schema, annotation guideline, SkillsMP snapshot, extracted graphs, security-match table, manual confirmations, or developer reports. Exact-title and exact-tool searches found the paper and third-party summaries, but no author-owned release. Therefore this is a **full-paper deep review, not a release audit**. All implementation, corpus, label, and result-table claims remain author-reported and unreplayed.

## One-sentence contribution

The paper supplies a static analyzer and bill-of-materials representation for mixed Skill, package, and service dependency graphs, but its unreleased evidence validates author-defined audit reachability more strongly than configured runtime realization or security consequence.

## Research questions

The paper introduces Agent Skill Supply Chains (ASSCs): directed graphs with Skill, package, and external-service nodes and dependency/use edges. It develops SDA to parse front matter and natural language, classify candidate dependencies, recursively expand Skill and package dependencies, retain lower-confidence candidates as annotations, and serialize the result as a SkillBOM compatible in concept with SBOM tooling (Sections I and III, pp. 1–5).

It asks three questions (p. 2):

1. How accurately and comprehensively does SDA recover Skill metadata and dependencies?
2. What structural patterns characterize ASSCs?
3. How are security-relevant Skill, package, and service signals exposed through ASSCs?

This sequence is sensible: validate the instrument, use it descriptively, then inspect security signals. The validity problem is that the later claims depend entirely on the first instrument, while the first validation does not cover all later identity, transitive package, service, security, and population operations.

## Methodology and system

### 1. Static evidence extraction

SDA splits YAML front matter from the Skill body, extracts root metadata, and collects candidate dependency clues from fields, commands, manifests, imports, Docker snippets, URLs, scripts, MCP mentions, APIs, and webhooks (Section III-B–C, pp. 3–4). Strong package evidence such as install commands and manifests creates an edge; weaker textual mentions require exact registry matching plus contextual support. Candidate Skill dependencies are resolved using name, repository, path, owner, and repository stars. If exact names fail, prefix/suffix matches are ranked; the highest candidate above a confidence threshold is selected. Lower-confidence items remain annotations (pp. 4–5).

This is more defensible than treating every mention as a dependency, and retaining unresolved evidence rather than deleting it is a useful design choice. But “confidence” is not reported as a calibrated probability, the threshold and feature weights are absent, and the identity fallback can convert popularity into identity. That is especially concerning because the paper later reports that 58.73% of effective Skill names collide, 88.76% of colliding names cross repositories, and 99.31% correspond to different hashes (Section V-B, p. 7). The population result itself demonstrates that name-based resolution is a high-risk operation.

### 2. Recursive construction

Package dependencies are expanded from a local running environment when available and otherwise from a registry. Skill dependencies are recursively matched in a local environment or corpus; cycles are stopped with a visited set. Service records are **not** recursively expanded (Section III-D, pp. 4–5). Duplicate components are canonicalized and supporting evidence is retained in the SkillBOM (Section III-E, p. 5).

The representation combines several different relations:

- a textual declaration or requirement;
- a package-manager or registry relation;
- Skill-to-Skill workflow reuse;
- an external service mention/use assumption;
- local-environment observations when available.

These are not equivalent operational dependencies. Registry fallback can resolve today's package graph rather than the graph available when the Skill was authored or run. A service mention can denote optional capability, documentation, an example, an intended endpoint, or actual invocation authority. The paper includes optional and other declared dependency types by design (Section VII-B, p. 10), but does not type optionality, phase, condition, activation, or observed realization in the reported graph statistics.

### 3. SKILL-DEP direct layer

The single-layer benchmark contains 500 root Skill documents, stratified by package, Skill, and service evidence type. Two software-engineering researchers with Skill-use experience calibrated a guideline on 50 Skills, froze it, and independently annotated the 500 documents. One produced 1,583 records and the other 1,590; 1,581 matched. Eleven disputes were discussed, five retained, and six rejected (Section IV-A, p. 5).

The overlap is genuinely high. From the reported counts, exact-record Jaccard overlap is 1,581 / (1,583 + 1,590 − 1,581) = 0.9931. This calculation is a check on the paper's counts, not an unreported reliability claim: the release does not provide labels, chance-adjusted agreement, per-channel disagreements, null documents, or the guideline. Consensus among two project researchers also does not establish construct validity when both learned the same project-defined dependency boundary.

Sampling is under-specified. The paper says evidence is sparse and therefore stratifies by dependency-evidence type, but does not identify the sampling frame, how evidence type was detected before annotation, the number of eligible roots per stratum, repository/content clustering, collision strata, negative-only roots, or whether SDA helped nominate candidates. If the analyzer or related patterns selected dependency-rich documents, benchmark F1 need not transport to the 1.43-million-root corpus.

### 4. SKILL-DEP multi-layer layer

The multi-layer benchmark contains 100 roots: 80 graphs of depth 3, 18 of depth 4, and two of depth 5. The same annotators and guideline are used. SDA reports precision 0.98, recall 0.93, and F1 0.95; no baseline supports this operation (Section IV-A–C, pp. 5–6).

This does not fully validate “whole dependency graphs”:

- the selection procedure that knew or estimated graph depth is not described;
- the unit appears to focus on Skill graph construction, while package and service transitive completeness are not separately reported;
- service dependencies are not recursively expanded by design;
- cycles, name collisions, missing repositories, version ambiguity, registry-time drift, and optional branches have no subgroup results;
- 100 roots are clustered inside repositories and reused dependency hubs, but uncertainty is absent;
- there is no held-out ecosystem, time split, adversarial identity set, or independent implementation.

The correct claim is high agreement with one project-defined, author-produced reference set on 100 selected Skill graphs—not demonstrated completeness over all mixed ASSCs.

### 5. Baselines and metrics

The direct benchmark compares SDA with five package-centric SBOM tools and a DeepSeek-v4-pro JSON extractor at temperature zero (Section IV-B, p. 6). SDA reports overall precision 0.92, recall 0.98, and F1 0.95, versus 0.52 F1 for DeepSeek and 0.18–0.25 overall F1 for SBOM tools (Table II, p. 7). Metadata accuracy is reported as 1.00 for SDA on name, repository, path, and license (Table III).

The package tools are useful negative controls for construct mismatch, not competitive ASSC analyzers: they are not designed to read Skill prose or emit Skill/service edges. The LLM baseline is more relevant, but its exact prompt, parser, model revision, endpoint, invalid-output count, and cost are unavailable. One deterministic call per item provides no repeated-call reliability. Metadata fields are largely explicit and the treatment of absent, ambiguous, or conflicting fields is not reported, making perfect accuracy difficult to interpret.

F1 is also criterion-local. It weights all dependency rows equally and does not measure graph edit distance, identity severity, reachability error, cycle preservation, version correctness, evidence-locator correctness, or downstream risk-decision loss. One false high-degree hub can distort thousands of later reachability counts while contributing one row error in direct F1.

## Evidence and results

### Corpus construction

SkillsMP listed 1,640,440 records on 6 June 2026; the authors successfully fetched 1,434,046 GitHub-backed records (87.42%). They retain repository/path metadata and content hashes and deliberately do not deduplicate the 0.52% hash-identical records because context may affect identity and resolution (Section V-A, p. 6).

That is a large and timely registry snapshot, but it is not 1.43 million independent Skills, installations, users, or workflows. Roots are nested within repositories, owners, copied families, templates, and hash-identical snapshots. Every reported root proportion needs at least repository-, content-family-, and owner-cluster sensitivity before being interpreted as ecosystem prevalence. The missing 12.58% is not random: inaccessible, deleted, or privatized repositories may differ in age, quality, security, and metadata.

### Metadata and structure

The descriptive findings are internally useful:

- 99.55% have front matter, 99.49% a name, and 99.52% a description;
- only 11.25% expose a license, 20.12% a version, and 1.40% a dependency-like field;
- 36.60% of roots have evidence in at least one Skill/package/service channel;
- direct Skill, package, and service proportions are 8.92%, 15.48%, and 22.25%; only 0.77% carry all three;
- dependency reuse is concentrated (reported normalized Gini 0.925 for Skills and 0.944 for packages);
- among dependency-bearing roots, 30.41% contain a cycle and 30.03% have convergent downstream nodes (Section V-B–C, pp. 7–8).

These findings support the paper's central governance diagnosis: activation metadata is much more common than identity, version, license, and dependency metadata. They do not establish that every inferred edge should be installed, that every cycle is a required cluster, or that registry records correspond to deployed configured systems.

### Amplification and hidden inventory

The paper defines amplification as transitive/direct dependencies. It reports median total amplification 0.5, p99 130.5, and package p99 350, with a maximum package amplification of 1,754. The `windows-95-web-designer` example declares three Skill dependencies and imports 1,754 packages and 1,938 components after recursion. It also reports that 22.42% of dependency-bearing roots gain packages only through reused Skills and that 71.87% of npm and 73.33% of PyPI package exposures are inherited through Skill reuse (Section V-C, p. 8).

This is the paper's most operationally important structural finding: reviewing only the root file can omit a large candidate inventory. But amplification depends on canonicalization, the denominator when direct count is zero, registry resolution time, optional/development dependencies, and whether recursive Skill references imply installation. The paper does not report these policies or a sensitivity analysis. “Hidden inventory” is therefore an inferred closure under SDA's relation rules, not an observed installation bill.

### Security propagation

The security study seeds graphs with public malicious-Skill reports, packages associated with supply-chain incidents, vulnerable/malicious MCP services, and regex families for remote execution, dangerous code, prompt injection, credential exfiltration, persistence/backdoors, secret exposure, service authority, and mechanism-only attack patterns (Section VI, pp. 8–9).

The paper reports large dependency-only shares: 60–78% for regex-based Skill signals, 98.01% for roots reaching `axios`, and 93.10% for reported vulnerable MCP service hits. It manually identifies copies of `clawhub1`/`clawbhub`, reports them to developers, and gives several path examples (pp. 9–10).

The paper itself correctly calls most of these **audit signals rather than confirmed vulnerabilities** (Section VII-B, p. 10). Interpretation must go further:

1. A package name is not a vulnerable version. `axios` reachability should not inherit the risk of one compromised release without version and valid-time resolution.
2. An unpinned install instruction creates version uncertainty, not proof that the bad version was installed.
3. Regex presence is not malicious semantics, model exposure, execution, or effect.
4. An MCP authority surface is not an invocation, authorization grant, or successful information flow.
5. A copied malicious Skill is serious candidate evidence, but developer notification is not remediation, confirmation, or measured harm.
6. A static dependency path has no agent, task, harness, tool policy, sandbox, network, secret, or action observer, so it cannot estimate attack success or benign utility.

RQ3 therefore establishes graph-based **candidate case finding** and root-only audit blind spots. It does not estimate vulnerability prevalence, exploitability, agent compromise, realized harm, safety improvement, or audit precision/recall over the corpus.

## Unique insight: configured interventions need a realization ladder

The paper's enduring value is not the “supply chain” label by itself. It reveals that a procedural intervention's configured identity is a graph whose edges may be latent, conditional, and realized at different phases.

`skill-bench` should preserve the following layers separately:

1. **Declared/reference graph:** exact source span, relation type, optionality, condition, version constraint, and confidence/dispute status.
2. **Resolved lock graph:** immutable source repository/blob, package/service identity, exact version or unresolved state, resolver and registry snapshot.
3. **Mounted/installed graph:** what bytes and components the harness actually made available.
4. **Visible graph:** what the model, scripts, tools, and subprocesses could observe under policy.
5. **Selected/invoked graph:** which Skill, package, command, endpoint, or service was actually chosen and called.
6. **Attempted-action graph:** requested authority, arguments, target, and policy decision.
7. **Realized-consequence graph:** state delta, information flow, external effect, collateral effect, and recovery.
8. **Diagnosis graph:** supported earliest cause, security/quality severity, utility, and uncertainty.

This ladder complements existing Skill-effect work:

- **LH-Bench** exposes expert procedure and rubric boundaries but treats the supplied Skill as a versioned intervention.
- **SkillsBench** compares matched Skill/no-Skill packages but needs the full dependency lock held fixed across arms.
- **Agentic Skills at Scale** derives tasks from copied packages; the present paper shows that copied top-level bytes may still omit runtime dependencies and service identity.
- **SLBench** types logical relations among procedural clauses; ASSC relations instead concern component realization and must not be conflated with semantic procedure preconditions or causal uptake.

The general benchmark implication is cross-domain. A spreadsheet procedure may depend on a parser and renderer; a research procedure on databases and APIs; a workplace Skill on another procedure, package, and service. Without graph identity, a reported “Skill effect” can be a dependency-resolution, environment, version, network, or permission effect.

## Limitations and validity threats

### Construct validity

- Static textual/registry reachability is not installation, visibility, invocation, action, or consequence.
- Optional, example, development, install-time, runtime, service-use, authority, and semantic procedure relations are insufficiently separated.
- Risk indicators mix confirmed malicious artifacts, incident-associated package names, vulnerable services, authority surfaces, and regex mechanisms.
- F1 over rows does not measure high-degree identity errors, graph reachability error, version validity, or downstream decision loss.

### Internal validity

- SDA is both the artifact under study and the instrument producing RQ2/RQ3 data.
- The analyzer's authors also define the annotation guideline and benchmark; independence and blinding are not reported.
- Stratification and depth selection may condition on analyzer-visible dependency evidence.
- Heuristic name/prefix/suffix/popularity resolution is evaluated without collision-focused or adversarial subgroup results despite severe measured collisions.
- No uncertainty propagates direct-edge error into million-root graph statistics.
- No repeated LLM baseline, threshold sensitivity, resolver sensitivity, or alternate implementation is reported.

### External validity

- The source is one rapidly changing registry snapshot of public GitHub-backed files.
- Missing/private/deleted records, duplicate/fork/template families, repositories, owners, and domains are not modeled as sampling clusters.
- Private enterprise procedures, installed-package populations, actual trial configurations, and production use are absent.
- One date cannot establish ecosystem trends, maintenance behavior, or persistence.

### Statistical validity

- No confidence intervals accompany F1 or corpus proportions.
- Root Skills are not independent; dependency hubs and repositories create strong clustering.
- Multiple security regex families and seed lists are reported without precision, false-positive, or multiplicity analysis.
- Manual confirmation has no sampling denominator, blinded protocol, agreement, or false-negative study.

## Reproducibility and operational realism

Reproducibility is weak despite the paper's structured proposal. The immutable PDF is readable and reports many aggregate counts, but no code, labels, guideline, prompts, thresholds, SkillBOM schema, crawl URLs/hashes, graph outputs, security seed snapshot, manual-review log, or result tables are available. Even the DeepSeek model revision and prompt are not released. The 1.43-million analysis is therefore not independently rerunnable.

Operational realism is limited to static public-file and registry analysis. The paper does not install a sampled graph in a clean environment, verify a lock, execute a Skill, capture model-visible bytes, record service authorization, replay a malicious path, or compare root-only versus graph-aware audit decisions on realized runs. Its governance recommendations—typed manifests, clusters, audit commands, and lockfiles—are plausible engineering proposals, not validated interventions.

## Transfer to `skill-bench`

### Retain

1. Treat procedural Skills and related configuration as first-class versioned components, not anonymous prompt text.
2. Preserve exact evidence locators and unresolved annotations rather than silently discarding ambiguous dependencies.
3. Type Skill, package, service, and future artifact/tool dependencies separately.
4. Record cycles and shared clusters instead of forcing a tree.
5. Freeze source, version, resolver, registry/environment snapshot, and hashes for every trial condition.
6. Inspect transitive candidate inventory before execution; root-only review is insufficient.

### Repair

1. Separate declared, resolved, installed, visible, invoked, attempted, and realized relations.
2. Add optionality, activation condition, phase, authority, version range, valid time, and resolution status to each edge.
3. Keep inferred edges and author-declared locked edges distinct; do not let an analyzer silently define the treatment.
4. Require collision/adversarial identity tests and fail closed on unresolved or multiply resolved components.
5. Attach security findings to exact version/time/evidence and a typed status: candidate signal, confirmed vulnerable component, runtime exposure, exploit attempt, realized consequence, or remediated.
6. Compare locked graph hashes across all trial arms so dependency drift cannot masquerade as a Skill effect.
7. Report graph-level and decision-level error, clustered uncertainty, and sensitivity—not only micro-F1.

### Falsification tests

- A top-level Skill hash remains fixed while one transitive package version changes; configuration identity must change.
- Two Skills share a name but differ by repository/blob; the resolver must abstain rather than use popularity.
- An example-only package mention must remain an annotation and never become installed treatment state.
- An optional service is declared but not authorized or invoked; audit reachability is true while runtime exposure and consequence are false.
- A flagged package name resolves to a safe version; name-level signal must not become vulnerability.
- A malicious transitive Skill is mounted but never visible to the model; mounted and exposure outcomes must differ.
- A service is invoked but sandbox/policy blocks the action; invocation, attempted action, policy decision, and state consequence must remain distinct.
- No-Skill and public-Skill arms differ only in the intended Skill visibility; all unrelated dependency-lock hashes must match.

## Concrete repository actions

Add one bounded, nonduplicate build task: extend the existing benchmark-bundle configured-system record with an optional **component dependency lock and realization ledger**, then exercise it on synthetic cross-domain cases covering name collision, optional/example-only references, version drift, mounted-but-unseen components, blocked service calls, and realized state change. This should extend existing configuration, trace, information-flow, action-safety, task-health, and validity machinery rather than create a standalone Skill package manager.

Do **not** use SDA-style inferred reachability as an execution allowlist, a safety verdict, or a benchmark score without independent release, calibration, and runtime evidence.

## Claim ceiling

This review supports the following project claim:

> A procedural intervention can depend on a transitive, mixed component graph, so benchmark configuration identity and diagnosis should preserve typed, versioned dependency evidence and runtime realization. Static graph reachability is useful audit evidence but is not exposure, invocation, causal effect, vulnerability, harm, utility, professional validity, capability, safety, or readiness.

It does not validate SDA on local data, reproduce SKILL-DEP, estimate the public Skill ecosystem, confirm the reported security cases, or justify modifying Hermes' own Skills. Those require released artifacts and observed configured executions.
