# HippoCamp: composite personal context is a retrieval-and-inference instrument, not evidence of a faithful user model

**Source:** Zhe Yang et al., *HippoCamp: Benchmarking Contextual Agents on Personal Computers*, arXiv:2604.01221v1 (1 April 2026), 56 pages; https://arxiv.org/abs/2604.01221v1.  
**Local PDF:** `data/papers/pdfs/2604.01221v1-hippocamp-personal-context-validity.pdf` (SHA-256 `66283379c0befd282681599d54fa5d96cbd011d74bd022ff2bbad4e0796ce572`).  
**Full extraction read:** `data/papers/text/2604.01221v1-hippocamp-personal-context-validity.txt` (SHA-256 `82e71d97e9f7e8ea0947346f844c62d5b8c41ede172bdbdbcb848170f2a1ed55`).  
**Official release inspected:** `data/sources/releases/2604.01221v1-hippocamp-personal-context-validity/HippoCamp-e7eda45b2d3c3b37cbaae77d175ed730a53be691.tar.gz`, commit `e7eda45b2d3c3b37cbaae77d175ed730a53be691`, archive SHA-256 `1ee7ae03c4239deb597def771b5de4e0da9874ef9b94935bbcd7481733db7a23`; provenance: `data/sources/releases/2604.01221v1-hippocamp-personal-context-validity/provenance.json`. The commit is dated one day after v1 and is release evidence, not guaranteed manuscript-time code.

## Review status and charter fit

This is a deep review based on the complete immutable paper and all 176 paths in the pinned official code archive. I inspected the release documentation, configuration, agent wrappers, retrieval/evaluation implementation, judge and file-list metrics, and analysis scripts. The 42.4 GB Hugging Face corpus, gold annotations, prebuilt Docker images, paper result records, and human-audit records are linked but not present in the archived repository, so I do not claim a corpus-level replay or independent privacy/file-grounding audit.

The work advances charter objectives A–C through a cross-domain question: when heterogeneous contextual traces are available, which stages from access to consequence are actually measured? Personal computing is a substrate case, not a scope commitment.

## One-sentence contribution

HippoCamp contributes a large multimodal file-search and open-ended QA instrument with localized evidence annotations, but its three contributor-composite personas, author-written gold narratives, heterogeneous harnesses, and answer-only judge support claims about retrieval and semantic answer agreement more strongly than claims about authentic personalization, user authority, workflow competence, privacy, or consequential computer action.

## Why this matters

Knowledge-work agents routinely depend on contextual records whose presence does not automatically authorize their use or validate the inferences drawn from them. HippoCamp is therefore valuable as a stress test for separating evidence availability, multimodal access, entity binding, and answer acceptance—but also as a warning that these stages cannot substitute for action consequences or affected-party validation.

## Research question and construct

The paper asks whether agents can search, perceive, and reason over long-lived personal file systems to answer factual-retention and profiling questions (pp. 1–6). Its concrete instrument contains three archetypal profiles, 2,000+ files/42.4 GB, 521 factual-retention and 60 profiling questions, and 46.1K annotation units. Each record may specify a minimal file set, localized evidence, an authored rationale, and required-capability labels (pp. 4, 19–23).

A narrower defensible construct is: **given read access to one composite profile and one natural-language query, can a configured system return an answer semantically matching an authored reference and identify files overlapping one annotated support set?** It does not test file creation, modification, preservation, permission decisions, user confirmation, downstream action, or resulting state. “File management” and “personal assistant” therefore overstate an answer-only QA environment.

## Methodology and system

### Source construction and authority

The paper reports interviews with 100+ device users, 60–90 minute protocols, opt-in consent, post-extraction review, and screening for at least 500 files, four modalities, ten extensions, three months of activity, and cross-file corroboration (pp. 5, 14–15). Contributors are partitioned and condensed into only three fictional archetypes. Files are reassigned, conflicts removed or minimally edited, identifiers pseudonymized, sensitive media generated or reproduced, and legal/finance profiles augmented from FinanceBench and LegalBench-RAG (pp. 15–16).

This is neither a natural personal-device sample nor a purely synthetic corpus. It is a **human-derived, edited, cross-person composite instrument**. The manuscript does not report the number retained after screening, contribution counts per archetype, file-level contributor lineage, demographic distribution, consent form/use scope, withdrawal events, edit counts, synthetic/native/augmented proportions, or independent privacy audit. Contributor familiarity supplies useful authoring knowledge, but aggregation destroys the one-user-to-one-environment relation needed for literal user-model validity.

### Task and trajectory authoring

Contributor-linked “domain-aware” annotators and proprietary LLMs propose questions; humans consolidate, deduplicate, balance, and author a minimal support set, evidence locators, rationale, and capability labels (pp. 6, 24–27). Factual retention spans explicit facts, localization, temporal comparison, and normative clauses. Profiling spans preferences, behavioral patterns, schedules, retrospective reconstructions, and workflows (pp. 28–33).

The design's strongest artifact is the proposed chain `question → minimal files → localized evidence → rationale steps → answer`. But this is an **author justification graph**, not an observed agent trajectory. Required-capability tags are assigned from the item specification, then answer/file scores are grouped under those tags; this does not observe whether a system searched, perceived, or reasoned correctly. The release code archive contains no annotation JSON or raw files—only download instructions—so paper claims about 581 records and locator validity were not independently audited here.

### Evaluation regimes

The paper compares native RAG/search methods, terminal agents using five benchmark APIs, and hosted ChatGPT Agent Mode. Information scope is intended to remain profile-local, but budgets, parsers, model backends, interfaces, and orchestration differ (pp. 7, 42–46). The authors explicitly acknowledge that hosted mode is not tool-parallel and call it an “upper-bound-style” reference (p. 45). “Same underlying files and defaults” is not a matched treatment.

The pinned release makes the interfaces inspectable: `list_files`, `return_metadata`, `return_txt`, `return_img`, and `return_ori`; four prompt configurations ablate text/image/original access. This is useful configured-system variation. Yet the repository delegates the actual environment to downloadable Docker archives and services; the inspected archive does not prove filesystem/network containment or exact image identity for paper runs.

### Grading

GPT-4o receives question, gold answer, and prediction and returns binary `pred` plus a 0–5 score. It does **not** see source evidence, retrieved files, traces, capability tags, or the environment (pp. 8, 47–49). File precision/recall/F1 compare reported files with one minimal support set. The paper describes a stratified human audit but gives no sample size, annotator count, agreement, correction rate, audit table, or released adjudications.

Thus answer correctness and groundedness are separate observations. A semantically plausible answer can pass without evidentiary support; a valid alternative support set can be penalized; and the judge cannot verify professional claims, current authority, visual measurements, or whether an action would be safe and executable.

## Evidence and what it supports

Table 2 reports ChatGPT Agent Mode at 48.3% profiling accuracy and 62.8% factual-retention accuracy; other systems are lower on most answer metrics (p. 7). Table 8 instead reports 56.8% factual and 55.9% overall for ChatGPT Agent Mode (p. 51), contradicting Table 2's 62.8% factual figure. Table 8 also labels average judge score as a 0–10 rescaling, while the main result presentation mixes F1, accuracy, and capability bins. Without immutable per-item predictions, judge outputs, retry manifests, and inclusion rules, the headline result is not fully auditable.

The paper's most useful empirical pattern is that file overlap and answer acceptance diverge: search-oriented systems can retrieve more annotated files without producing accepted answers, while some systems achieve higher answer acceptance than file F1 (pp. 10, 50–51). This supports **measurement separation**, not the claimed causal diagnosis that perception is the primary bottleneck. Capability-wise “perception accuracy” is answer accuracy on items tagged as requiring perception, not direct evidence that the agent perceived the decisive region. Likewise, F1-above-accuracy does not isolate post-retrieval reasoning, and accuracy-above-F1 does not prove parametric recall; alternative evidence sets, incomplete file reporting, judge error, and harness observability are rival explanations.

The five-stage failure pipeline—retrieval mismatch, grounding avoidance, fabricated evidence, entity misbinding, and missing verification—is diagnostically useful (pp. 10–12), but appears based on qualitative case analysis without a reported coding sample, prevalence, independent raters, or agreement. It is a hypothesis-generating taxonomy, not estimated failure incidence.

The scalar difficulty score combines eight authoring-derived features, hand-weighted interactions, a hard-case bonus, and a sigmoid (pp. 36–39). Profiling necessarily has longer references, more files, and more rationale steps because of how it is authored, then receives extreme scores (mean 89.1 versus 53.8). Correlation with model scores is criterion association under this construction, not calibrated difficulty, ecological frequency, or an independent latent trait.

## Unique insight: contextual authority is a staged claim, not a property of file access

HippoCamp exposes an important chain that benchmark designs should make explicit:

1. **available** — an artifact exists in the task environment;
2. **authorized** — its use is within contributor/user consent and task purpose;
3. **accessible** — the configured system can discover and render it;
4. **observed** — the trace shows a particular representation reached the model;
5. **interpreted** — a supported claim was extracted with correct entity, time, scope, and authority;
6. **adopted** — the claim materially informed the response or decision;
7. **accepted** — a grader judged the output against a reference;
8. **consequential** — an artifact/state/action changed correctly and safely;
9. **user-valid** — the affected person endorses the inference or action for its intended use.

HippoCamp strongly represents availability and authored support, partially measures reported access and answer acceptance, and does not measure adoption, consequence, or user validation. Consent described during corpus creation is not task-time authorization for every possible inference: a file may be legitimately present yet inappropriate for inferring health, relationships, or decision policies. This distinction is especially important for composite personas, where no single real user can validate the resulting “profile.”

## Limitations and validity threats

### Personalization, realism, and privacy

- Three edited composites cannot estimate variation across users or support population generalization. Profile effects are inseparable from domain, modality mix, file count, augmentation, question mix, and harness compatibility.
- Screening selects unusually rich, stable, auditable file systems. It excludes sparse, messy, shared, cloud-first, centrally managed, or irregular devices—the exact cases where personal-agent authority and ambiguity may be hardest.
- “Real-world files,” fictional identities, generated sensitive media, reproduced artifacts, public benchmark augmentation, and rewritten professional documents are mixed without released per-file provenance proportions.
- Participant sign-off is described but not quantified or released. Withdrawal from a composite after editing and cross-file rewriting requires lineage that the public schema shown in the paper does not expose.
- Privacy scanning for identifier patterns cannot establish absence of identity leakage, re-identification risk, sensitive inference, copyright compliance, or contextual-integrity violations.

### Task and gold validity

- Annotators familiar with source profiles author questions, evidence, rationales, answers, and capability tags in one pipeline, creating co-design dependence and hindsight-perfect support sets.
- “Minimal” evidence is asserted, not tested through leave-one-source-out necessity, alternate-set adjudication, or independent expert reconstruction.
- Profiling answers often transform a few authored episodes into stable preferences or decision rules. No held-out future behavior, user agreement, counterexample search, uncertainty, or harmful-inference review validates that abstraction.
- Professional examples include legal advice, financial attribution, compliance judgment, and scheduling recommendations. File-grounded semantic agreement does not establish professional correctness, current law/policy, duty of care, or safe action.
- The 521/60 imbalance and only 20 profiling items per archetype make broad personalization claims depend on a small, clustered authoring set.

### Measurement and statistics

- No repeated-run estimates, task/profile-clustered confidence intervals, multiplicity controls, or uncertainty on rankings are reported.
- Retry policy reruns malformed, empty, tool-failed, and timeout cases but not incorrect answers (p. 46); counts and first-attempt versus post-retry outcomes are absent. This mixes reliability intervention with capability scoring.
- Method-appropriate rather than matched budgets prevent causal model/harness comparison. Average latency omits invalid/nonpositive cases and does not report indexing, conversion, tool, or total monetary cost.
- File-set overlap cannot establish perception or causal use. Answer-only judging cannot establish grounding. Grouping those outcomes by required-capability labels does not create process measurement.
- The LLM judge's human audit is procedurally described but empirically unreported; extra “non-conflicting” details are accepted even though the judge cannot inspect sources for support.
- Main and appendix ChatGPT factual-retention figures conflict (62.8% versus 56.8%), and no raw paper result package resolves the discrepancy.

### Reproducibility and operational realism

The pinned code release is substantial: wrappers, provider implementations, retrieval/indexing stack, prompt configurations, evaluator, metrics, configs, and reproduction documentation are present. However, exact reproduction requires mutable external assets: a 42.4 GB Hugging Face dataset, six Google Drive Docker archives, proprietary models/services, and image/audio/document conversion. The archive does not include dataset revision hashes, Docker-image digests, paper predictions, traces, judge records, retry inventories, human audit, consent instruments, contributor lineage, or per-file provenance.

Operationally, agents answer questions; they do not manage the filesystem. There are no writes, permission requests, user-confirmation checkpoints, protected-path checks, reversibility tests, side-effect graders, or post-action state. The “personal computer” substrate is mediated through benchmark APIs rather than a consumer OS, and hosted mode uses a different product interface. The benchmark is valuable for multimodal contextual QA but does not demonstrate safe personal-computer agency.

## Comparison with adjacent reviewed evidence

- **Workspace-Bench** adds persistent workspace artifacts and output production, but similarly shows that availability, authored relevance graphs, observed access, and causal use are distinct. HippoCamp is stronger on multimodal localized evidence and contributor-derived context; it is weaker on artifact/state consequence. Neither establishes professional or user-valid outcomes from scale alone (`papers/agent-benchmarks/2026-07-10-workspace-bench-file-dependency-validity.md`).
- **LongMemEval-V2** evaluates retrieval of evidence from prior interaction histories and cleanly separates a memory layer's evidence package from a fixed reader. HippoCamp instead exposes a static composite file system. Neither tests whether inferred context improves held-out action or remains safe under changed state; both need an evidence-to-action bridge (`papers/agent-benchmarks/2026-07-11-longmemeval-v2-environment-experience-memory.md`).

## Transfer to skill-bench

### Retain

1. **Modality-specific locators and evidence views.** Preserve file identity, representation/render identity, page/time/region locator, and transformation provenance.
2. **Separate support-set and answer observations.** Report discovery, view access, claim extraction, entity binding, temporal/authority reconciliation, answer quality, and consequence independently.
3. **Minimal-support hypotheses plus alternatives.** Store an author support set, but permit expert-approved equivalent sets and test necessity with source ablation.
4. **Entity and contextual-authority checks.** Personal or workplace tasks need explicit subject, affected party, source authority, purpose, valid time, consent/authorization, and inference sensitivity.
5. **Interface ablations.** HippoCamp's source/text/image prompt configurations are a useful pattern for measuring whether rendering assistance changes access rather than silently calling it model capability.

### Repair

1. Add a **context-to-consequence ladder** to task/trial evidence: availability → authorization → access → observation → interpretation → adoption → graded output → state consequence → affected-party review. Missing stages must fail closed rather than being inferred from a final answer.
2. Treat profiling claims as uncertain hypotheses with supporting and contradicting evidence, scope, valid time, confidence basis, prohibited uses, and an explicit confirmation policy—not as stable ground truth.
3. Version and hash corpus, file manifest, derived text/render representations, Docker image, tool API, model/harness, budget, retries, judge, and result inventory independently.
4. Validate gold support with independent reconstruction, alternate paths, leave-one-evidence-out tests, contradiction probes, and user/expert review appropriate to the claim.
5. For any contextual pilot, include a held-out action/state consequence and privacy/authorization checks; do not equate personal-context QA with professional task completion.

## Concrete repository actions

No new queue task is added. Existing bundle, artifact-view admissibility, expert-participation/consent, validity-argument, task-health, metric-monitoring, execution-isolation, and persistent-workspace machinery already house these requirements. The nonduplicate next use is a future diverse-pilot conformance case that joins one contextual inference to a reversible held-out artifact/state action and records every ladder stage; that should be folded into pilot selection rather than creating another schema.

## Bottom line

HippoCamp is a useful multimodal evidence-localization and open-ended QA benchmark with an unusually ambitious contributor-derived file substrate. Its central transferable lesson is not that 42.4 GB creates “true personalization,” but that contextual work must separate file availability, evidence access, interpretation, entity binding, answer acceptance, and downstream consequence. The paper and release support the first half of that chain. They do not yet establish faithful user modeling, task-time authorization, privacy safety, professional correctness, consequential computer management, or personalized-agent readiness.