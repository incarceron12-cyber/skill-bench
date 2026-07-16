# Paper-replication: inspectable workspace closure is not source-complete or scientifically valid replication

## One-sentence contribution

Paper-replication turns a long scientific reconstruction into a persistent target → execution → artifact → provenance → comparison → report record, but its released completion gate establishes only self-consistency relative to an agent-authored target set and acceptance records: executed mutations show that the gate still passes after a source claim is removed, acceptance metrics are made failing, the report is reduced to locator comments, an execution hash is corrupted, or a source trace is made vacuous.

## Why this matters for `skill-bench`

This source addresses a central charter problem: how can consequential, long-horizon work survive context loss and end in inspectable evidence rather than an agent's assertion of completion? The paper's answer—externalize task state, enforce one active target, retain failed/replaced executions, hash artifacts and implementation inputs, require claim-specific comparisons, and close every target before completion—is more useful than a final-answer score.

Its release also reveals the next validity boundary. A dense evidence graph can be internally coherent around an incomplete or permissive interpretation. The decisive question is not only whether every **recorded** target has records; it is who authorized the target inventory and acceptance predicates, whether the predicates were actually evaluated, whether source claims are entailed, whether report locators carry substantive findings, and whether execution records bind to the accepted bytes.

**Verdict:** high-value workflow and release evidence for durable, inspectable workspace conformance; weak evidence for source-complete paper replication, scientific correctness, procedural-skill efficacy, general reliability, or professional research capability. The paper itself often states this narrower boundary. The release audit makes the boundary executable and sharper.

## Sources and reading record

### Immutable primary source read in full

- Atharva Hans and Ilias Bilionis, *Coding-agents can replicate scientific machine learning papers*, arXiv:2607.02134v2 (10 July 2026): <https://arxiv.org/abs/2607.02134v2>
- PDF: [`data/papers/pdfs/2607.02134v2-paper-replication-workspace-evidence.pdf`](../../data/papers/pdfs/2607.02134v2-paper-replication-workspace-evidence.pdf) — 16 pages; SHA-256 `db7b06c89677763cc003a6dfc5152dedf2a32f8f80eb6353dc670ee483a5ca92`.
- Full layout extraction: [`data/papers/text/2607.02134v2-paper-replication-workspace-evidence.txt`](../../data/papers/text/2607.02134v2-paper-replication-workspace-evidence.txt) — SHA-256 `cfac0b8c95ad59f09e220073123a8e024939192efdd64ad02e5af1113f1c7121`.
- Metadata: [`data/papers/source/2607.02134v2-metadata.xml`](../../data/papers/source/2607.02134v2-metadata.xml). The immutable API record contains no withdrawal or retraction notice.
- Date read: 2026-07-17 UTC.

### Official release inspected and executed

- Repository: <https://github.com/PredictiveScienceLab/paper-replication-paper>
- Audited commit: `e030a7b5dc625acb7cfc1b9b5630161b7a4a1ed2`; tree `47aa26370d7ac39e5e926f22a13c41b9f01a19df`.
- Archive: `data/sources/releases/2607.02134v2-paper-replication/PredictiveScienceLab-paper-replication-paper-e030a7b.zip` — SHA-256 `1b12187a7e5244524aab7e8bd85b2b216ac894ee5fa0d7b2732f216b34d7675e`; 7,892 files; 360,225,828 uncompressed bytes.
- Provenance: [`data/sources/releases/2607.02134v2-paper-replication/provenance.json`](../../data/sources/releases/2607.02134v2-paper-replication/provenance.json).
- Executed release audit and mutation results: [`data/sources/releases/2607.02134v2-paper-replication/release-audit.json`](../../data/sources/releases/2607.02134v2-paper-replication/release-audit.json).

The pinned commit is dated after arXiv v1 and before v2. It is the requested official release evidence, not proof of byte identity with the exact implementation or every analysis artifact used for either manuscript version. The top-level repository is Apache-2.0, but embedded source-paper materials have separate or absent license records; repository licensing must not be projected onto all copied paper assets.

## Research question and contribution

The paper asks how a coding agent can reconstruct computational claims from paper materials while preserving progress and requiring evidence outside the final chat message. It contributes three linked objects (Sections 1–2, pp. 2–7):

1. **A target-level evidence contract.** Each selected claim becomes a target with source locator, method reconstruction, output, acceptance rule, status, and report anchor.
2. **A persistent workspace and validator implementation.** The agent records source inventory, specification, one active target, executions, provenance, comparisons, and report coverage; external utilities decide whether records are sufficient for `MATCHED` and completion.
3. **A repeated-run case-study analysis.** Four scientific-ML papers are each reconstructed three times, then compared on completion, target decomposition, paper-anchored scalar fidelity, elapsed time, replaced executions, and acceptance-rule type.

The unique contribution relative to PaperBench is the workspace contract rather than a dense author-informed scoring rubric. PaperBench can give partial credit against a fixed external hierarchy; Paper-replication asks the actor to construct and close its own claim inventory while retaining execution lineage. Relative to SciAgentArena, which separates scientific workflow stages and validates stage outputs, this paper emphasizes durable per-claim evidence through one long reconstruction. Relative to LH-Bench, it turns a procedural skill into an executable record discipline, but does not run a no-skill treatment or independently authored rubric. Those differences explain both its strength—inspectable process—and its central risk—actor-authored measurement authority.

## Methodology and system reconstruction

### 1. Task and evidence model

The agent starts from LaTeX source, referenced figures/tables, appendices, bibliography, and available data. Author code is forbidden. For each target `t_j`, it reconstructs an implementation `F_j`, runs it on data/configuration/stochastic state, and records an evidence bundle containing generated result, run record, provenance, comparison, and report coverage (Section 2.1, pp. 3–4).

The contract usefully distinguishes:

- a generated artifact from evidence;
- paper assets from generated outputs;
- a successful command from target acceptance;
- implementation provenance from mere visual resemblance;
- target-level matching from paper-level completion; and
- exact, numeric, distributional, qualitative-structural, and visual claim types.

Missing paper details are supposed to become explicit assumptions and experiments rather than silent choices. Failed and replaced executions remain in the run ledger. Code, configuration, paper trace, output, and selected source assets are hashed. This is a strong pattern for any knowledge-work benchmark in which the final artifact hides a path of interpretation and correction.

### 2. Completion definition

The manuscript defines completion as specification validity ∧ progress validity ∧ report coverage ∧ all recorded targets `MATCHED` ∧ no active target ∧ report PDF existence (Eq. 3, p. 6). It explicitly states that completion remains relative to the recorded target set and validation checks, and that accepted targets may omit aspects not included in their acceptance rules (pp. 6, 12–14).

The released validator implements this structure. It checks record presence, path and hash consistency, policy flags, one-active-target state, artifact location, direct source-asset hash equality, provenance fields, successful linked run ID, expected output path, comparison-record shape, report path/anchor substrings, matched statuses, and PDF existence.

However, the executable semantics are weaker than the prose in several places:

- tolerance strings from the reproduction matrix are never evaluated;
- comparison metric values need only exist and have a compatible broad type;
- paper-trace content is not checked for valid locator or entailment;
- expected artifact hashes in the run ledger are not compared with current accepted bytes;
- report coverage is substring presence in TeX, not semantic coverage or TeX↔PDF freshness;
- target completeness is not checked against an independently authorized source-claim inventory; and
- direct hash equality catches copied assets, but transformed copying or source-derived hard-coding remains outside the check.

### 3. Case-study design

The corpus contains four selected scientific machine-learning papers:

- PIFT, emphasizing posterior/distributional structure;
- PINN-I, emphasizing PDE solution errors;
- PINN-II, emphasizing coefficient discovery; and
- SINDy, emphasizing sparse support and trajectory geometry.

Each receives three independent Codex runs with the same paper materials, prompt templates, compute environment, no-author-code policy, and no shared workspace/code/output state (Section 2.5, pp. 7–8). The configured agent is Codex with GPT-5.4 at Extra High reasoning. Local execution used an M4 Max MacBook Pro with 128 GB memory; selected work used Purdue Gautschi CPU/GPU nodes, including H100 resources (Section 3, p. 9).

Long runs receive an initial prompt and a fixed queue of ten continuation prompts, each asking the agent to reopen the workspace, inspect status, and continue until the gate passes (p. 7). This is not a fixed-call benchmark budget: elapsed time includes work until the first post-gate completion report, while the number and timing of model calls, token usage, and monetary cost are not released.

### 4. Analysis

The authors analyze five different objects:

1. **Workspace completion:** whether the released gate passes.
2. **Target coverage:** number of agent-authored targets per run, modeled with a Gamma-Poisson hierarchy.
3. **Paper-anchored scalar fidelity:** 13 hand-curated canonical anchors × 3 runs, using fixed author-selected thresholds and log10 headroom.
4. **Effort/correction:** elapsed hours plus tracked and replaced executions.
5. **Acceptance-rule variation:** agreement in broad rule type after semantic cross-run target alignment.

The distinction between workspace acceptance and the separate paper-anchored scalar analysis is methodologically important. It prevents `MATCHED` from becoming an undefined universal correctness score and reveals cases where the gate and independent analysis disagree.

The cross-run semantic alignment is not fully deterministic. Four Claude Opus agents produced paper-specific mappings from run targets to canonical claims; a planned verify stage could not run because its model alias was unavailable, so headline mappings were hand-confirmed against author LaTeX (`analysis/README.md`, lines 62–72). The scalar table is then hand-curated with selected metric keys, unit normalizations, paper values, and thresholds. This is inspectable author analysis, not independent scientific adjudication.

## Evidence and what it supports

### 1. Released completion and replay

All twelve released completion validators passed during this audit, reproducing the manuscript's target counts:

| Paper | Run target counts | Completion replay |
|---|---:|---|
| PIFT | 8, 8, 25 | 3/3 passed |
| PINN-I | 8, 8, 8 | 3/3 passed |
| PINN-II | 9, 9, 15 | 3/3 passed |
| SINDy | 20, 20, 20 | 3/3 passed |

The deterministic analysis stages also reran from the archive:

- 158 target rows;
- 684 extracted metric rows;
- 388 parsed acceptance predicates;
- 12 effort and 12 coverage records;
- 39 canonical scalar observations;
- 9 structural SINDy observations; and
- cross-run acceptance-rule agreement.

The regenerated extraction, coverage, structural, and drift files were byte-identical to the archive. `canonical_fidelity.csv` differed only in last-bit platform floating-point string rendering; values, threshold classifications, and conclusions were unchanged.

This is strong release evidence that the disclosed records support the disclosed descriptive analysis pipeline.

### 2. Completion does not imply scalar fidelity

The paper reports 37/39 scalar observations inside its fixed paper-anchored thresholds (Section 3.2, pp. 10–11). The audit reproduced exactly that classification. Two observations were outside:

- PINN-I Schrödinger run 3: relative L2 error about `0.048` against `0.01`;
- PINN-II Navier–Stokes λ2 run 1: coefficient error about `16.4%` against `10%`.

Both remained `MATCHED` under their workspace-authored acceptance records. This is the paper's most important empirical result: **record closure and scientific-fidelity analysis are different estimands**. A benchmark should preserve this disagreement rather than overwrite the workspace result or collapse it into one score.

The reported predictive probabilities—0.79, 0.90, and 0.73 for another scalar anchor-run falling inside threshold for PINN-I, PINN-II, and SINDy—should not be read as per-task reliability. Anchors are clustered within three papers, only three runs exist per paper, thresholds are curated, and PIFT contributes no scalar anchor. The authors correctly frame the models as descriptive of this corpus, not a paper-difficulty ranking (Discussion, p. 13).

### 3. Decomposition and judgment variation

PIFT's target count changes from 8/8 to 25 when one run splits composite figures into panels; PINN-II changes from 9/9 to 15 when appendix claims are added. Acceptance-rule agreement is only 8/11 for PIFT, 4/8 for PINN-I, 5/11 for PINN-II, and 19/20 for SINDy (Section 3.4, pp. 11–12).

This evidence undermines any assumption that “the paper” naturally determines one target inventory or one criterion type. Target boundaries and acceptance modes are outputs of interpretation. Because the same agent family performs that interpretation and the reproduction, the design measures a **self-scoped contract**. Independent claim inventory and criterion authority are needed before completion can support a source-completeness claim.

### 4. Effort and correction records

Elapsed time ranges from 1.2 to 13.0 hours. The paper reports posterior medians of 2.2 hours (PIFT), 5.0 (PINN-I), 6.9 (PINN-II), and 1.9 (SINDy), plus 25 replaced tracked executions, 21 in the two PINN papers (Section 3.3, pp. 11–12).

Retaining these executions is valuable: final success otherwise hides failed method choices and expensive repair. Yet `superseded` is derived retrospectively as failed or not linked by final provenance, so it combines execution failure, exploratory work, and later replacement. It is not a complete compute-cost measure, root-cause label, or proof that every meaningful attempt was tracked. The release lacks model-call counts, token/cost records, full environment snapshots, and agent transcripts.

## Executed mutation audit

All mutations used a temporary copy of released `case_studies/run_1/pift`; the immutable archive was untouched. Exact results are in `release-audit.json`.

### 1. Source-target omission passed

Removing `fig_ex1_posterior_collapse` from the reproduction matrix caused the completion gate to pass with 7/7 recorded targets matched. Nothing compared the reduced matrix with a frozen independent inventory.

**Meaning:** “all targets complete” is a denominator claim. If the actor controls the denominator, closure cannot establish source completeness.

### 2. Numerically failing acceptance evidence passed

For `fig_ex1_posterior_collapse`, the audit changed comparison metrics to violate two declared predicates: `std_monotone==1` and `std_ratio_beta1e5_to_1e2<=0.25`. Completion still passed with 8/8 targets matched.

**Meaning:** the release stores acceptance-rule text but the completion gate does not execute it. Record presence is not predicate satisfaction.

### 3. Locator-only report passed

The audit replaced `report/main.tex` with a minimal document whose comments contained each `output_path` and `report_anchor`, while retaining the old PDF. Completion passed.

**Meaning:** locator coverage does not establish that current report text explains the result, embeds the artifact, states deviations, or corresponds to the retained PDF.

### 4. Broken execution-artifact hash binding passed

The audit replaced the linked execution record's expected-artifact SHA-256 with 64 zeros. The provenance still matched the current artifact, and completion passed.

**Meaning:** provenance-to-current-artifact integrity and execution-to-artifact integrity are distinct. The released validator checks the former but not the latter.

### 5. Vacuous paper trace passed

The audit replaced one paper trace with `asserted paper trace`, updated the provenance hash, and reran completion. It passed.

**Meaning:** cryptographic self-consistency does not establish source entailment, locator validity, or paper-method fidelity.

### 6. Missing-provenance control failed

Removing the same target's provenance record produced an explicit validator error.

**Meaning:** the gate is not empty theater. It enforces useful structural requirements, but its claim ceiling must track which semantics are actually checked.

## Unique insight

The durable insight is a **workspace evidence closure graph with an authority boundary**.

Paper-replication gets the graph largely right:

`source claim → target → method reconstruction → execution → output → provenance → comparison → status → report location`

But the graph has two fundamentally different validity properties:

1. **Structural closure:** required nodes and links exist, hashes and paths agree, terminal state is reached.
2. **Substantive closure:** the target inventory covers authorized source claims, traces entail methods, executions produced the accepted bytes, criteria are legitimate and satisfied, reports carry findings and caveats, and independent review licenses the conclusion.

The paper and release strongly improve structural closure. They do not establish substantive closure. This distinction transfers beyond science to financial models, policy memos, investigations, spreadsheet workflows, legal analyses, and software changes. A polished evidence graph can still be a coherent projection of one actor's incomplete interpretation.

A second insight is that **completion disagreement is diagnostic evidence**, not noise. The two scalar cases that are workspace-matched but fail fixed paper-anchored thresholds reveal criterion-authority drift. `skill-bench` should retain at least three separate outcomes:

- contract closure under the trial's declared checks;
- independent criterion outcomes under frozen external checks; and
- source/claim completeness and validity status.

## Limitations and validity threats

### Construct validity

- The primary outcome is closed-world workspace conformance, not scientific correctness.
- Targets and acceptance rules are authored by the evaluated agent; source coverage and criterion legitimacy are not independently fixed.
- Broad `MATCHED` labels combine numeric, distributional, structural, and visual judgments whose evidence strength differs.
- Report path/anchor presence is not report quality, interpretability, or scientific argument quality.
- Paper-method provenance fields and hashes do not prove semantic fidelity.

### Internal validity and skill efficacy

- There is no no-skill or alternative-workflow arm. The study characterizes products under the skill; it does not estimate the skill's effect.
- Ten continuation prompts are part of the treatment but no call-level intervention ledger is released.
- One model/interface/reasoning setting performs every evaluated run.
- The released Claude Code package has no evaluated run, so package availability is not cross-harness efficacy.
- The analysis's semantic alignment includes model and author judgment after the runs.

### Sampling and generalization

- Four papers are purposively selected from scientific ML, with three runs each.
- PIFT is coauthored by the study authors, creating unusually strong local domain familiarity and potential selection/interpretation advantage.
- Papers differ in missing data, stochasticity, compute, and claim form; four clusters cannot identify broad paper-level variance.
- No professional researcher baseline, independent replicator, recipient-use study, or downstream scientific review is included.

### Measurement and statistical limits

- Thirteen scalar anchors are hand-curated from three papers; PIFT has no scalar observations.
- The PINN-II 10% coefficient threshold is a stated analysis convention, not a direct equivalence between noise robustness and coefficient error.
- The resolution floor for exact equality is chosen from observed positive discrepancies, making one analysis transformation data-dependent.
- Hierarchical posterior diagnostics can show sampler behavior under a model; they cannot compensate for target/threshold selection, clustered data, or absent independent labels.
- Acceptance-rule agreement compares broad types after semantic alignment, not agreement on exact predicates, thresholds, or scientific decisions.

### Operational realism

- The work genuinely runs long computations and produces professional-style code, figures, tables, and reports, which is more realistic than short answer evaluation.
- However, the workspace does not retain agent transcripts, request/provider snapshot identity, token usage, monetary cost, exact Codex build, complete environment lock, container/image identity, or all cluster/runtime dependencies.
- Prompt paths are redacted in the release and initial prompts differ by workspace; this preserves privacy but prevents exact launch replay.
- The validator scripts have five distinct hashes across the twelve workspaces, so “same workflow” does not mean one immutable validator implementation.

## Reproducibility and release quality

### Strong points

- Full workspaces, source materials, prompts, code, configs, artifacts, run ledgers, provenance, comparisons, reports, and analysis outputs are present.
- All twelve zero-model-call completion validators replay.
- Deterministic extraction and drift analyses reproduce from released records.
- Bayesian draws, posterior-predictive arrays, sampler extras, summaries, and diagnostics are committed.
- The analysis README candidly identifies manual curation, semantic alignment, the failed verify-stage alias, and interpretive boundaries.

### Weak points

- No Python dependency manifest or lockfile is present. In the clean audit environment, deterministic stages 1–4 ran, but `05_bayes.py` could not run because `jax`/`numpyro` were absent and diagnostics could not run because `matplotlib` was absent.
- The committed diagnostics report max R-hat `1.00483`, minimum effective sample size `1387.62`, and zero divergences; these are inspectable outputs, not independently regenerated evidence in this audit.
- Source-paper licensing is incomplete at artifact level. Only three PIFT source copies expose `License.txt`; reuse rights for other copied sources are not established by the top-level Apache license.
- Exact model service identity and call evidence are absent.
- The release commit falls between v1 and v2, so exact manuscript-release correspondence remains unproven.

**Reproducibility grade:** high for record inspection and deterministic descriptive extraction; moderate for validator replay; moderate-to-low for full statistical environment recreation; low for hosted-agent trial replication; unestablished for scientific correctness.

## Transfer to `skill-bench`

### Retain

1. **Workspace as system of record.** Persist obligations, assumptions, active work, executions, artifacts, comparisons, and completion independently of chat.
2. **One active obligation with explicit terminal state.** This reduces lost work and makes unresolved scope visible.
3. **Typed evidence bundles.** Separate source locator, method/decision basis, execution, output, provenance, criterion result, and report location.
4. **Append-only correction lineage.** Keep failed and replaced work rather than exposing only a curated final artifact.
5. **Plural claim outcomes.** Preserve contract closure, independent correctness/fidelity, artifact quality, cost, and validity separately.
6. **Cross-run decomposition audits.** Target-count and criterion-type drift are measurements of authoring instability, not merely nuisance variation.

### Repair

1. **Freeze or independently review the obligation denominator.** Bind every public source requirement/claim to at least one target, with explicit reviewed exclusions. The evaluated actor must not silently remove denominator items.
2. **Compile acceptance predicates into executable checks.** Every criterion must produce evaluated pass/fail/invalid/insufficient-evidence status, not just store metric names and tolerance text.
3. **Separate actor criteria from external criteria.** Actor-authored acceptance rules may guide work, but capability claims require frozen independent checks or adjudication.
4. **Bind execution to accepted bytes.** Verify run-record output hash → provenance artifact hash → current artifact hash, and preserve replacement/supersession events.
5. **Validate source entailment.** Paper/source traces need exact locators, quoted/structured propositions, scope, and reviewer status; a file hash alone is insufficient.
6. **Make report coverage semantic and fresh.** Parse actual artifact inclusion and claim/caveat sections; bind the current TeX/source hash to the rendered PDF.
7. **Record configured-system and resource identity.** Model/provider snapshot, harness/skill/validator hashes, prompts, call/attempt topology, environment image, compute, time, tokens, cost, failures, and censoring must be first-class.
8. **Calibrate completion with negative mutations.** Omission, failing predicates, stale execution, vacuous trace, locator-only report, copied/transformed evidence, and alternative-valid-path cases should be required validator tests.

### Cross-domain completion claim ladder

For any long-horizon knowledge-work workspace, `skill-bench` should issue separate statuses:

1. **record closure:** declared records and links are structurally present;
2. **predicate closure:** executable declared checks actually pass;
3. **obligation closure:** independently authorized requirements are covered or explicitly unresolved;
4. **artifact validity:** accepted bytes and native state satisfy independent checks;
5. **report/handoff validity:** current report accurately communicates outcomes, uncertainty, and deviations;
6. **professional validity/readiness:** expert, recipient, consequence, reliability, and decision evidence support the intended use.

Paper-replication demonstrates rung 1 and parts of rungs 2–5 in its unmutated cases; the mutation audit shows why completion cannot be promoted automatically.

## Action items

1. Build one small **workspace-closure conformance slice** against existing benchmark-bundle/task-health/validity machinery rather than a new subsystem. Use a frozen independent obligation inventory and planted mutations for omitted target, failing predicate, stale execution hash, vacuous source trace, locator-only report, stale PDF, and legitimate alternate implementation.
2. Add a treatment study only after the closure validator is sound: matched no-workflow/workspace-workflow conditions with identical task, model, tools, call budget, compute envelope, independent targets/checks, and repeated trials. Measure completion, independent correctness, repair retention, cost, and newly introduced errors separately.
3. For scientific pilots, require independent domain review before licensing “replication.” Workspace closure should remain an operational state, not a scientific validity decision.

## Claim ceiling

The full paper and executed release support:

- released record-conformance closure for 12 workspaces and 158 recorded targets;
- inspectable target, execution, artifact, provenance, comparison, status, and report-locator records;
- within-corpus variation in target decomposition, scalar outputs, elapsed time, correction paths, and criterion types;
- a hand-curated 37/39 paper-anchored scalar-threshold result with two explicit closure/fidelity disagreements; and
- a useful reusable workflow hypothesis for long-horizon evidence management.

They do **not** support:

- complete coverage of source-paper claims;
- scientific correctness or independent replication;
- sound execution of all target acceptance predicates;
- general procedural-skill efficacy or transfer;
- configured-system reliability;
- Claude Code or cross-harness efficacy;
- professional researcher equivalence; or
- operational/deployment readiness.

## Charter decision filter

- **Objectives advanced:** A (deep review of realistic agent evaluation), B (expertise/evidence-to-evaluation methodology), and C (executable validation implications).
- **Concrete evidence/artifact:** immutable full-paper review; pinned official-release audit; replay of 12 validators and deterministic analysis; six bounded mutation probes; machine-readable `release-audit.json`.
- **Uncertainty clarified:** durable workspace evidence materially improves inspectability, but closed-world record closure does not identify source completeness, criterion satisfaction, scientific validity, skill effect, reliability, or readiness.
- **Classification:** expansion plus validation.
- **Duplication/scope check:** complements PaperBench's external rubric, SciAgentArena's staged workflows, LH-Bench's procedural skill, and Workspace-Bench's file lineage; it does not narrow `skill-bench` to scientific ML because obligation authority, executable predicates, byte lineage, and report freshness are cross-domain primitives.
- **Useful completion:** exact release and mutation evidence yields a bounded claim ladder and one nonduplicate validator build path rather than another generic paper-replication summary.
