# Paper and Release Review: Synthetic Computers at Scale — Scale Is Not Workspace Validity

- **Paper:** https://arxiv.org/abs/2604.28181v1
- **Authors:** Tao Ge, Baolin Peng, Hao Cheng, and Jianfeng Gao
- **Date read:** 2026-07-13
- **Source:** complete immutable arXiv v1, submitted 2026-04-30
- **Tags:** synthetic-environments, workspace-generation, long-horizon-agents, professional-artifacts, simulated-collaboration, experiential-learning
- **Local PDF:** `data/papers/pdfs/2604.28181v1-synthetic-computers-at-scale.pdf` (33 pages; SHA-256 `19a38e975681e0f9554d3a4c00c69593413348d970f01c25849334091e539502`)
- **Local text:** `data/papers/text/2604.28181v1-synthetic-computers-at-scale.txt` (SHA-256 `dbb75fc35b1cd01e24381772f0101437819da24532ddd0b320441282e0b84dd3`)
- **Official dataset:** https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale/tree/40e780a399dc0426516dd4007c56ca3ff06db36f
- **Release evidence:** pinned README, 98-row Parquet metadata table, 500-report archive, and computer archive audit under `data/sources/releases/2604.28181v1-synthetic-computers/`; provenance: `data/sources/releases/2604.28181v1-synthetic-computers/provenance.json`
- **Timing boundary:** the large archives and Parquet were committed on 2026-04-30, around v1 submission; the inspected README revision is 2026-05-01, after v1. The paper pins no dataset revision. The release is related primary evidence, not proven byte-identical experiment input.

## One-sentence contribution

The paper proposes a persona → user profile → filesystem plan → dependency-conditioned artifact set → month-scale objective → daily simulated work pipeline and reports that lessons distilled from 900 synthetic trajectories improve matched agents on 100 held-out synthetic computers and GDPVal; its distinctive contribution is generating the **work substrate**, not merely prompts, but all realism, expertise, authority, objectives, rubrics, and retrospective lessons remain inside a model-authored closed loop with no human or operational validation.

## Why this matters for skill-bench

This advances charter objectives A, B, and C by exposing a reusable environment-authoring problem: consequential knowledge-work tasks need accumulated files, versions, project history, collaborators, and cross-artifact dependencies before an agent begins. The paper makes that substrate an explicit generated object rather than prompt decoration.

The case is not a reason to narrow `skill-bench` to productivity agents or synthetic data. Its cross-domain hypothesis is:

> Can a benchmark generate rich task contexts at scale while preserving an auditable chain from persona and professional claims through files, objectives, authority, artifacts, checks, and permitted validity claims?

The paper supplies a promising generator architecture and scale demonstration. It does not establish that generated computers represent occupations, that their contents are professionally legitimate, that “a month of human work” is calibrated, or that performance on them predicts real work.

## Research question and claim ladder

The defensible empirical question is:

> Within one model-authored simulation pipeline, do occupation-grouped lessons distilled from synthetic trajectories improve the same configured work agent on held-out generated worlds and an external artifact benchmark?

The stronger narrative crosses several unsupported links:

```text
abundant personas
→ occupationally representative users
→ internally coherent computers
→ authentic accumulated work history
→ professionally legitimate objectives
→ a month of human work
→ realistic collaboration and authority
→ valid professional artifacts and rubrics
→ trustworthy retrospective lessons
→ genuine learning transfer
→ productive intelligence / deployment fitness
```

The experiments address selected late, system-relative links. They do not validate the earlier substrate links on which interpretation depends.

## Methodology and system

### 1. Persona-to-computer generation

A sampled persona is expanded into a detailed profile containing identity, occupation, organization, responsibilities, work history, current projects, collaborators, common outputs, tool habits, naming conventions, and filesystem behavior (Section 2.1, pp. 3–4). A second planning stage creates:

- a filesystem policy and virtual time axis;
- project folders, file inventory, formats, timestamps, origins, and content modes;
- a directed file graph for references, derivation, versions, and extraction;
- logical OS paths later mapped to portable `drives/` paths.

Artifacts are instantiated in dependency-aware topological order. Public files are retrieved from the web when possible and synthesized when retrieval fails; user-specific files are generated with artifact tools while conditioning on predecessors (Sections 2.2–2.3, pp. 4–7).

This is a stronger construction pattern than independently sampling files. The file graph is both an authoring schedule and a hypothesis about provenance. However, graph edges are generated descriptions, not verified semantic entailment. A downstream workbook conditioned on an upstream PDF can still mistranscribe it; shared generation lineage does not prove factual or professional coherence. The paper acknowledges only one narrow failure: a planned web download is checked after planning and may silently fall back to synthesis (footnote 2, p. 7).

### 2. Objective and collaborator generation

A Claude Opus 4.6 setup agent reads the profile and current computer, then invents three to five connected deliverable packages intended to represent about 20 working days. Packages specify milestones and multiple professional outputs. The same setup process creates five to eight collaborators with roles, communication styles, private reference files, preferences, and decision authority (Section 3.1, pp. 8–10).

The work agent receives the public profile, objectives, collaborator descriptions, and computer, but not private collaborator files until shared. This supports delayed evidence, corrections, approvals, and planted errors. Yet the setup agent simultaneously authors the worker's world, stakeholder authority, hidden evidence, expected work, and many eventual rubric premises. There is no independent employer, practitioner, client, or regulatory source establishing that these are legitimate tasks or that a generated collaborator may authorize the represented decision.

### 3. Month-scale simulation

Claude Sonnet 4.6 runs in the Claude Code SDK with Anthropic non-Office skills and MiniMax DOCX/XLSX/PPTX/PDF skills (Section 4.1, p. 13). The agent creates a weekly plan, then executes one separate session per workday. Each day restores state from the activity log, filesystem, collaborator replies, and shared files; execution mutates files and graph state and records outreach and progress (Section 3.2, pp. 10–13).

Across 1,000 reported runs, the paper gives means of 2,272 turns, 8.59 wall-clock hours, 5.5 collaborators, and 31 communications. Initial computers average 111.6 files and final computers 197.4; directory depth stays near 3.4 (Tables 1 and 3, pp. 13–14). These are useful resource and structure measurements. They do not calibrate human duration. “About a month of human work” is assigned by the setup agent; no human timing study, workload decomposition, or practitioner feasibility check is reported. Eight agent-hours and 20 simulated dates are not evidence for one human-month.

### 4. Rubric and retrospective generation

For 100 computers, the same setting is reportedly run five times. A judge inspects each run's deliverables and drafts a rubric using objectives, collaborator requirements, source materials, and its view of a good solution; five drafts are merged. Claude Opus 4.6 then scores final deliverables (Section 4.2.1, pp. 15–16). Criteria are labeled `spec`, `interaction`, `expertise`, `reference`, or `quality`.

This usefully spans existence, cross-file consistency, provenance, formulas, preferences, and visual quality. But the procedure is outcome-informed: observed outputs help generate the instrument later used to evaluate outputs. Multiple runs may broaden criterion coverage, yet they also allow candidate behavior to shape the ruler. The paper does not identify which run is scored, whether rubric authors are blinded to condition, how duplicates/conflicts are resolved, or whether alternative valid work is protected. No human rubric audit, inter-rater reliability, deterministic checker, or criterion-dependence analysis is reported.

A second Opus analysis converts each full trajectory and final score into a retrospective report describing strengths, failures, root causes, and lessons (Section 4.2.2, pp. 16–17; Appendix A, pp. 24–33). The example is diagnostically rich, but several causes are conjectures: ten blank messages “suggest” context or planning exhaustion, while the report itself lists multiple alternatives. A fluent causal narrative is not trace-grounded causal identification.

### 5. In-domain experience extraction

The 1,000 computers are split into 900 “training” and 100 held-out computers; model weights are not updated. Retrospective items from the 900 are grouped by occupation, merged and frequency-ranked by an LLM, and compiled by Anthropic's skill-creator into one occupation-specific skill. Baseline and skill agents then run on the same 100 held-out worlds, with skill availability as the stated difference (Section 4.3, pp. 17–18).

Reported mean rubric score rises from 61.6% to 68.6%, and the skill condition wins 83 of 100 paired computer comparisons. Skills from 10, 100, 500, and 900 training computers win 50%, 64%, 75%, and 83% of paired comparisons (Table 4 and Figure 7, p. 18).

The matched substrate is a strength. Important identification gaps remain:

- no repeated trajectory per condition estimates agent variance;
- no interval or test accompanies the +7.0-point in-domain mean;
- task/occupation clustering is ignored;
- skill length and context cost grow with training scale and are not controlled;
- broader occupation coverage and better lesson estimation are asserted, not separately ablated;
- occupation labels, generators, setup agent, worker, rubric judge, retrospective judge, and skill compiler are parts of one synthetic ecosystem;
- the exact split, skills, raw scores, trajectories, and configurations are unreleased.

This supports a package-level instruction effect within the generator, not learned professional expertise.

### 6. Out-of-domain GDPVal comparison

The authors apply the same skills to 220 GDPVal gold tasks with official rubrics and pairwise Opus judging. Baseline and skill-augmented agents are compared for Sonnet 4.6, Haiku 4.5, and Opus 4.6 (Section 4.4, pp. 18–19). Sonnet records 105 wins, 48 ties, and 67 losses, with reported one- and two-sided sign-test p-values of 0.002 and 0.005. Haiku records 104/36/80; Opus 99/50/71.

This is the paper's strongest evidence that the distilled instructions are not useful only on the exact 20-day harness. Still, GDPVal is shorter (31 turns, 17 minutes, 1.18 reference files on average) and uses a model judge. The experiment does not establish transfer to real workplaces, new generator families, unseen professional procedures, or stateful month-scale work. The paper does not report judge blinding/order randomization, repeated outputs, effect sizes on official scores, cost, per-occupation results, or correction for three model comparisons.

## Evidence and what it supports

### Supported within the reported configured system

- A pipeline generated 1,000 persona-conditioned computer descriptions and completed long agent simulations with the reported structural/runtime statistics (Tables 1–3, pp. 13–14).
- Generated environments contain many structured artifacts and explicit cross-file relationships; Office formats make up 67.8% of reported files (Figure 5, p. 14).
- On 100 held-out generated computers, adding the generated occupation skill is associated with a +7.0-point mean rubric difference and 83/100 paired wins (Table 4, p. 18).
- On GDPVal, skill-augmented outputs win more pairwise judgments than baseline outputs for three tested model configurations, significantly so under the reported sign tests for Sonnet and Opus (Figure 8, p. 19).
- Released data demonstrate that rich metadata, actual artifact trees, and long retrospective reports can be packaged compactly enough for inspection.

### Not supported

- occupational representativeness or coverage;
- realistic prevalence of files, noise, projects, or collaboration patterns;
- professional correctness, expert authorship, or stakeholder authority;
- equivalence to a month of human labor;
- causal validity of retrospective root causes;
- model-weight learning, retention, or continual self-improvement;
- production usefulness, economic value, safety, or deployment readiness.

## Unique insight

The most transferable contribution is the separation between **task generation** and **substrate generation**. A realistic knowledge-work item is not just an instruction plus attachments; it begins from a versioned state whose files, dependencies, projects, people, and valid times constrain which actions and artifacts are legitimate:

```text
persona / organizational mandate
→ authority-bounded profile claims
→ project and valid-time state
→ file inventory + provenance graph
→ instantiated artifact views
→ objective and collaborator events
→ agent state mutations
→ final artifacts and consequential states
→ checks and bounded claims
```

The paper's central failure is equally useful: every arrow is generated inside one model-authored loop. **Internal consistency is a necessary generator-conformance property, not ecological or professional validity.** Scale amplifies this distinction. One thousand mutually coherent fictional worlds can provide diverse practice substrates while offering no estimate of real occupation prevalence or expert correctness.

For `skill-bench`, synthetic generation should therefore produce two ledgers:

1. **projection/conformance ledger:** did persona, files, graph, objectives, events, artifacts, and checks agree mechanically?
2. **authority/validity ledger:** which external source or contributor licenses each professional claim, threshold, hidden consequence, and interpretation?

A generator may pass the first while explicitly failing the second.

## Release audit

The official dataset revision exposes six root files: README, Parquet, two compressed artifact archives, one figure, and Git attributes. Static inspection found:

- the README and Parquet contain **98**, not the paper's promised 100, released computers: 50 Windows IDs `000000–000049` and 48 macOS IDs `000050–000099`, missing mac IDs `000052` and `000058`;
- the 98-row table has nine columns: ID plus JSON strings for persona, user profile, collaboration, objectives, project index, filesystem policy, file list, and graph;
- rows contain 56–171 file records (mean 81.96), three to five deliverables (mean 4.28), and five to nine collaborators (mean 5.56); the file-count mean differs materially from the paper's 111.6 pre-simulation mean, further showing that the 98-row release is not a simple public slice with identical reported statistics;
- the report archive contains exactly 500 distinct Markdown reports, IDs ranging from 0 to 896, with no manifest connecting report selection to the 900 training computers;
- the computer archive has 15,611 members and exactly the same 98 computer IDs. Root metadata for sampled Windows `000000` and macOS `000050` computers is JSON-equivalent to the Parquet fields; sampled DOCX and PDF bytes are valid containers, so this is a substantive artifact release rather than metadata-only placeholders;
- mapping all 8,032 released file-list records to documented physical `drives/` paths found 20 unmaterialized planned paths across eight Windows rows. These include deliverable-like DOCX/XLSX/PPTX/PDF paths and six bare outreach JSON paths, not merely unsupported formats. The release therefore does not satisfy its own implied file-list → byte-tree totality invariant;
- the README states that graph nodes correspond to file-list entries, but a static path/edge audit found at least one duplicate/path/edge/cycle inconsistency in **34 of 98 rows**: seven duplicate file paths, 69 duplicate node paths, 758 file paths absent from the base node set, 177 base nodes absent from the file list, 1,836 edges with an endpoint absent from that base node set, and 117 nodes in directed cycles. Several affected rows carry day-specific graph fields, suggesting mixed pre/post-simulation snapshots rather than one normalized graph. This is an audit of the released serialization, not proof that the paper-time internal generator used the same malformed representation;
- edge `type` is not a controlled vocabulary: beyond common `references`, `derived_from`, and `version_of`, the 98 rows contain hundreds of sparse relation spellings and 219 edges without a recognized `type` in the base field;
- the release's own limitation statement correctly calls the data fully synthetic, English-only, heterogeneous, and small-scale.

The release does not include the 1,000-computer experiment table, 900/100 split manifest, setup/work/judge prompts, exact Claude Code configuration, simulation trajectories, daily logs, collaborator simulators, five-run rubric drafts, merge decisions, final rubrics, raw in-domain scores, generated occupation skills, GDPVal outputs/judgments, cost records, or statistical inputs. The 500 reports refer to files such as `evaluation_summary.json`, `daily_sim_turns.jsonl`, and interaction logs that are not present in the report archive. Reports are evidence of model-generated analysis output, not independently replayable analyses.

The computer archive contains the released `drives/` artifact bytes and duplicate metadata, but it covers the 98-row public sample, not the paper's 1,000 runs or their post-simulation trajectories. Artifact availability permits format/content inspection; it does not bridge the missing experimental lineage.

## Limitations and validity threats

1. Personas are sampled from a prior synthetic pool; no sampling frame links them to actual occupations or work prevalence.
2. Figure 4 reports the selected synthetic distribution, not occupational representativeness.
3. Profile elaboration can invent credentials, organizations, regulations, practices, and authority without source provenance.
4. Files are conditioned on generated descriptions and predecessors; shared lineage does not establish semantic fidelity.
5. Web retrieval occurs after planning and can fall back to synthesis, changing evidence authority without an explicit task-level claim boundary.
6. File size and Office-format frequency are weak proxies for content richness or quality.
7. The paper reports no human inspection sample, expert validity study, agreement, defect rate, or adversarial coherence audit.
8. “About a month of human work” has no human-time calibration or decomposition.
9. Collaborators are reactive simulations with setup-authored private facts and authority; the paper itself lists dynamic collaborators as future work (p. 21).
10. The same synthetic ecosystem authors profiles, objectives, hidden evidence, outputs, rubrics, retrospectives, and skills.
11. Five output-conditioned rubric drafts can encode candidate behavior and evaluator cues into the scoring instrument.
12. Rubric merge, weighting, dependence, admissible alternatives, and judge reliability are unspecified.
13. “Expertise” criteria are model-authored and are not expert evidence.
14. Full-trajectory retrospectives produce plausible root-cause stories without interventions or a reproducible causal-label protocol.
15. Occupation-level lesson frequency can amplify recurring generator artifacts or judge preferences as if they were professional norms.
16. No negative/contradictory lesson handling, source authority, uncertainty, held-out validation gate, or rollback is described.
17. In-domain evaluation has one apparent run per condition and no uncertainty interval for the mean effect.
18. Training-scale comparisons confound coverage, sample count, skill content, and skill length.
19. Split independence is under-specified; no persona/project/artifact similarity audit is reported.
20. The baseline/skill comparison does not cross independent versus shared rubrics, so guidance and evaluator alignment remain entangled.
21. GDPVal evidence is judge-relative and shorter-horizon; no official scalar score delta or human preference is reported.
22. Proprietary model/runtime versions and mutable external skills limit replay.
23. Compute, token, API, storage, and human-equivalent costs are absent despite at least 8.59 agent-hours per reported simulation.
24. The release has 98 rather than the paper's stated 100 computers and no explanation for the two omissions.
25. The released base graph/file serialization has substantial path, endpoint, vocabulary, and snapshot inconsistencies.
26. Public release artifacts are not the 1,000-run experiment package and cannot reproduce either effect estimate.
27. The paper's million/billion-world scaling argument extrapolates persona abundance and compute, not demonstrated quality-control throughput.
28. No safety, privacy attack, malicious artifact, prompt injection, licensing, or synthetic-sensitive-data audit is reported.

## Reproducibility and operational realism

Reproducibility is **moderate for inspecting 98 generated substrates and 500 retrospective narratives, weak for recreating the generator, and very weak for reproducing the experimental results**. The official revision is pinned and its three central downloadable artifacts have verifiable hashes. The metadata schema and actual file trees support independent audits of structure and samples.

The implementation and experiment lineage are absent. Reproduction would require reconstructing persona expansion, planning, retrieval fallback, artifact generation, collaboration, daily state restoration, rubric drafting/merging, retrospective extraction, skill compilation, and evaluation. Exact prompts, seeds, model snapshots, tool versions, environment images, trajectories, skills, and result matrices are unavailable.

Operational realism is mixed. Persistent artifact-rich workspaces, delayed collaborator evidence, interdependent deliverables, revisions, and multi-day state are materially closer to knowledge work than isolated prompts. But the worlds are cleanly authorable, objectives and authorities are synthetic, collaborators are reactive, external systems are mostly files/messages, deadlines have no real consequence, and no practitioner confirms that outputs or procedures are legitimate. The setup has high value as a **generated stress substrate**, not as a validated workplace sample.

## Transfer to skill-bench

The pipeline's reusable value is substrate generation and state persistence, but every generated projection must remain below a professional-validity gate until external authority and independent conformance evidence exist.

## Concrete repository actions

### Retain

1. **Generate the substrate before the task:** profile, projects, valid time, filesystem policy, file inventory, and dependencies should precede objective authoring.
2. **Persist state across sessions:** daily mutations, incoming evidence, collaborator replies, and open commitments should be first-class trial events.
3. **Represent connected work packages:** score dependencies and cross-artifact consistency, not only isolated deliverables.
4. **Keep private collaborator materials gated by authority events:** delayed evidence is a useful test when its public basis and authority are validated.
5. **Preserve process and outcome separately:** final artifacts cannot identify early retrieval, planning, communication, or propagation failures.
6. **Report substrate/resource statistics:** file/graph size, turns, time, communications, context use, and artifact counts help characterize difficulty without substituting for validity.

### Repair

1. Bind every generated professional claim, threshold, authority, trap, and hidden check to `external_source`, `consented_expert`, or explicit `synthetic_hypothesis`; never let fluent setup output inherit expert status.
2. Version each generation projection and hash persona, profile, plan, graph, instantiated files, objectives, events, rubric, and trial state independently.
3. Validate graph referential integrity, acyclicity where derivation ordering requires it, controlled relation types, valid-time order, and pre/post snapshot identity before release.
4. Distinguish retrieved authoritative files from synthetic fallbacks; a fallback must change evidence status and downstream permissible claims.
5. Measure workspace coherence with planted and sampled checks: path existence, graph endpoints, cross-file entailment, version supersession, source-to-claim fidelity, objective feasibility, authority scope, and artifact-view validity.
6. Calibrate workload with practitioners or task decomposition; use “20 simulated days” unless human effort has actually been measured.
7. Freeze rubrics before evaluated outputs or use independent authoring; preserve criterion provenance, dependence, alternatives, and public basis.
8. Treat retrospective lessons as candidates requiring evidence locators, uncertainty, contradiction handling, disjoint held-out validation, and rollback—not as professional rules.
9. Split by persona/project/file/claim clusters and audit near-duplicates, not only computer IDs or occupation labels.
10. Cross skill/no-skill with independent/shared rubrics and repeated runs; report paired cluster-aware uncertainty, cost, and invalid outcomes.
11. Keep generator conformance, synthetic-agent performance, professional validity, and deployment readiness as separate claim rungs.

### Falsifiable next validation experiment

Reuse existing workspace/projection and artifact-admissibility machinery rather than creating a synthetic-computer subsystem. Generate a small cross-domain set of workspace bundles with three independently versioned projections: profile → plan, plan → file graph, and graph → bytes. Plant balanced defects at each boundary:

- unsupported professional claim;
- missing or wrong-authority source;
- dangling dependency and cycle;
- stale derived artifact;
- synthetic fallback mislabeled as retrieved evidence;
- objective impossible from available state;
- collaborator instruction outside authority;
- structurally plausible but semantically inconsistent artifact.

Have generator-aware deterministic checks and blinded human reviewers localize defects. Measure detection by boundary, false acceptance, false rejection of legitimate alternatives, reviewer agreement/time, and whether repair preserves unrelated state. Then run matched agent trials only on bundles that pass conformance, while keeping professional-validity claims unsupported unless practitioners approve the relevant claims and artifacts. Useful completion would show that generated richness survives independent falsification; failure would demonstrate that scale is producing inspectable noise rather than benchmark-ready context.

No new queue task is added. Existing workspace, projection, evidence-chain, artifact-admissibility, task-generation, configured-system, validity, metric, longitudinal, and compounding-lesson contracts already provide the implementation homes; adding another schema before consolidation would duplicate them.

## Claim ceiling

This paper supports the claim that the authors' model-authored pipeline can create large, artifact-rich fictional computer substrates and long simulated trajectories, and that generated occupation instructions are associated with better model-judge outcomes on held-out synthetic computers and more pairwise wins on GDPVal for the tested proprietary configurations. It does **not** establish synthetic realism, occupational coverage, professional correctness, a month of human-equivalent work, causal retrospective diagnosis, learning transfer beyond external instructions, expert skill acquisition, economic value, production fitness, safety, or deployment readiness.
