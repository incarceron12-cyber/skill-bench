# Paper Review: LH-Bench — Skill-Grounded Evaluation of Long-Horizon Agents

- **Paper:** https://arxiv.org/abs/2603.22744v2
- **Authors:** Ishan Gupta and Abhishek Chandwani
- **Date read:** 2026-07-10
- **Venue / source:** arXiv preprint; manuscript marked “Agent Skills ’26” with placeholder ACM DOI
- **Tags:** long-horizon-agents, expert-rubrics, procedural-knowledge, artifact-contracts, trace-evaluation, verifier-feedback, enterprise-benchmarks
- **Local PDF:** `data/papers/pdfs/2603.22744-lh-bench-skill-grounded-evaluation-of-long-horizon-agents.pdf` (22 pages; SHA-256 `56267f12178b4ddda24fda7fb76e62b6a3e03a3ea6d28ff40ed0e5d288bc6f33`)
- **Local text:** `data/papers/text/2603.22744-lh-bench-skill-grounded-evaluation-of-long-horizon-agents.txt`
- **Version read:** v2, 29 May 2026

## One-sentence contribution

LH-Bench operationalizes subjective enterprise-agent quality as three linked but separately scored objects—an expert-authored procedural skill, inspectable intermediate/final artifact contracts, and independent human preferences—and shows that observable workflow anchors improve cross-LLM judge agreement, while structured verifier feedback makes failures recoverable in-loop.

## Why this matters for skill-bench

This is the closest primary-source implementation found so far of `skill-bench`’s central thesis: tacit professional expertise becomes evaluable when it is decomposed into workflow phases, observable events, artifact conventions, completion thresholds, and failure signatures. The paper’s most reusable object is not `SKILL.md` as a file format. It is a **crosswalk from expert procedure to evidence**:

`expert expectation → execution guidance → trace-visible boundary → artifact hook → grader evidence → failure label`.

That crosswalk turns “work professionally” into claims such as “the token file existed before component implementation,” “all routes in the manifest were covered,” or “a visual inspection caused at least one repair.” Those claims can be inspected without pretending that the whole task has one crisp answer (Sections 3.1, 4.1, 5.1, Appendix E).

The paper also exposes a design hazard that `skill-bench` must not copy uncritically: a dual-use skill is simultaneously an intervention and part of the measuring instrument. If the agent sees the exact rubric boundaries, the benchmark may measure compliance with disclosed evaluator cues rather than transfer of professional judgment. The right transfer is therefore not “publish the complete grader as a skill,” but “derive public guidance and private checks from a common expert model, version them independently, and test how much each changes behavior and measurement.”

## Research question

The paper asks whether long-horizon, subjective enterprise work can be scored reliably by grounding evaluation in expert procedural knowledge rather than binary completion or generic LLM-authored rubrics. Subquestions are whether this design distinguishes harnesses, whether its ranking converges with human preference, whether skills causally improve execution, and whether structured verifier feedback supports recovery.

The evidence is strongest for **measurement consistency** (cross-judge agreement increases under the expert rubric) and **diagnostic usefulness** (skill-level profiles and recovery categories). It is much weaker for the causal claim that expert skills improve task quality, because the execution ablation has only seven paired runs.

## Methodology

### Environments and units

LH-Bench evaluates end-to-end commercial harness/model combinations rather than base models:

- **Figma-to-code:** 33 real `.fig` tasks. Agents inspect Figma through MCP, export structure/assets, implement all frames/routes, preview, repair, and deploy. Ground truth includes a frame manifest and 2× PNG exports; Playwright captures the built application for VLM comparison (Section 4.1).
- **Programmatic content:** 183 chapters in 41 courses. Agents work in persistent data rooms and produce code-rendered videos, animations, or presentations, including revision turns. Sources are normalized to line-addressable Markdown so claims can be tied to spans; render, synchronization, structural, and viewport verifiers run during execution (Section 4.2).
- **Systems:** Claude Code, Codex CLI, and Gemini CLI, seven harness × model configurations overall. The main skill-score comparison uses one flagship configuration per family (Sections 3.2 and 7.1; Appendix D).

This is operationally realistic in several ways: tasks use stateful tools and real artifacts; sessions can exceed context limits; persistent manifests support restart recovery; agents encounter infrastructure and tool errors; and deployment is part of the workflow. It is less controlled than a model benchmark because harness, model, native skill support, context compaction, and verifier-hook integration vary together.

### The skill / rubric / artifact structure

The Figma skill uses YAML-frontmatter Markdown with ordered phases. Appendix D shows a minimal sequence: first read `manifest.json` for prior progress, then extract design structure through Figma MCP, export assets and reference frames, and continue through implementation and verification. The manifest stores preview/deployment URLs and completed steps, enabling session recovery (Appendix D.3–D.4).

The same workflow becomes four weighted process rubrics on anchored 1–5 scales (Appendix E, Table 14):

| Process dimension | Weight | Example observable 3→4 boundary |
|---|---:|---|
| Design inspection and asset extraction | 0.30 | Correctly exported assets become organized with semantic names/directory structure, and hierarchy inspection occurs before coding. |
| Design-token and style extraction | 0.25 | A referenced token file covering at least four categories also exists before components, uses semantic names, and has no hardcoded leaks. |
| Component and layout architecture | 0.25 | Correct reuse/layout/states also show upfront planning, full variant coverage, and an explicit props interface. |
| Build verification and iteration | 0.20 | A compiling build also gets previewed and receives at least one repair based on visual inspection. |

The artifact tier is separate. The Figma contract supplies frame IDs, node IDs, reference-image paths, and target routes (Appendix C), then scores component coverage, layout, colors, typography, assets, visual fidelity, responsiveness, and interactions with fixed weights (Appendix G, Table 16). Programmatic-content contracts tie task-specific rubric criteria to exact source spans and code-rendered outputs (Sections 4.2 and 5.2; Appendices B–C and I).

The evaluation pipeline preserves structured traces aligned to workflow phases rather than giving judges an unbounded transcript. Three conceptual judges consume different evidence: trajectory (transcript/tool traces for planning and recovery), process (trace plus skill rubric), and output (reference artifacts plus screenshots) (Section 5.3–5.4, Table 3). However, the reported Figma scoring detail centers on process and output tiers; the paper does not report an equally clear standalone trajectory leaderboard.

### Evaluation and evidence

- **Process scoring:** Gemini 3.1 Pro, Claude Sonnet 4.6, and GPT-5.2 judge four expert-authored process rubrics. The three tested harnesses rank Claude Code 3.27, Codex 3.16, Gemini CLI 2.80; mean pairwise quadratic-weighted Cohen’s κ is 0.60 (Tables 5–6).
- **Rubric comparison:** On the same 92 runs, eight LLM-authored generic rubrics yield κ=0.46 and mean judge variance 0.25; four expert-authored, workflow-phase rubrics yield κ=0.60 and variance 0.10 (Section 7.6, Table 9; Appendix F).
- **Output scoring:** A Gemini VLM compares captured frames against references. Seven configurations score from 3.59 to 4.27, though sample sizes differ by configuration (18–32 runs) (Table 4).
- **Human validation:** One Figma domain expert makes 135 blinded, position-randomized pairwise judgments over 31 tasks. Codex and Claude form an indistinguishable top tier (p=0.67), each preferred over Gemini (p=0.036 and p=0.047). Programmatic content has 275 matched SME pairwise comparisons (Section 7.6, Tables 10–11).
- **Execution ablation:** Seven paired Figma runs over three tasks compare a one-line instruction against `SKILL.md`, with tools held constant. Aggregate improvements are +0.15 for Claude, +0.87 for Codex, and +0.05 for Gemini; only two of seven no-skill runs deploy. The authors correctly call this directional (Section 7.5, Table 8).
- **Recovery:** An LLM pipeline extracts 590 error→recovery events from 96 Figma runs. Overall recovery is 70.3%; syntax, type, and build feedback yields >85% recovery, while configuration errors recover only 16.7% (Section 7.7, Tables 12–13).
- **Uncertainty:** Primary-candidate task means use 1,000 bootstrap resamples. Programmatic-content results aggregate at the course level (41 courses), avoiding the fiction that all 183 chapters are independent (Sections 7.1–7.3).

## Unique insight

The paper’s deepest insight is that **expertise improves evaluation when it is expressed as transitions between observable states, not adjectives**. Replacing “good planning” with “created a centralized token file before writing components” reduces degrees of freedom for a judge. The +0.15 κ result is therefore better understood as evidence for *observable-boundary rubric engineering* than for expert authorship in the abstract.

A second insight is that verifier output has two distinct roles: post-hoc evidence and test-time assistance. Error frequency alone is not a useful capability measure when one harness proactively avoids errors, another triggers and repairs them, and a third persists to deployment. The benchmark should preserve at least four quantities separately: exposure/opportunity, error count, feedback specificity, and successful recovery. Collapsing these into “task passed” discards the harness behavior that long-horizon evaluation is supposed to reveal.

A third, more cautionary insight comes from the disagreement results. Human and automated tiers recover the same broad ranking boundary, yet individual-run human/LLM concordance is only κ=0.08 for output and 0.06 for skill. In programmatic content, five-point VLM/human κ is only 0.082, despite better aggregate directional alignment. Thus aggregate ranking convergence does **not** validate fine-grained automated grades. `skill-bench` should treat an LLM score gap as diagnostic evidence, not automatically as a perceptible professional-quality difference.

## Transferable design patterns

### 1. Store an expert-model crosswalk, not only prose guidance

For every procedural requirement, store independently versioned fields for:

- public instruction or rationale;
- expected workflow phase and ordering relation;
- observable trace event(s);
- required/intermediate artifact and state predicate;
- private or public check boundary;
- anchor levels and decision threshold;
- permitted feedback payload during execution;
- provenance to an expert elicitation or primary source;
- known failure signatures and root-cause labels.

This extends the current bundle’s `primitive → check_ids` relationship: it makes *when and how evidence appears* explicit, rather than leaving sequence requirements buried in `pass_criteria` prose.

### 2. Separate process, artifact, and preference claims

Report three score families separately:

- **process compliance:** did the trajectory instantiate expert workflow invariants?
- **artifact acceptability:** does the deliverable satisfy objective and expert-judged contracts?
- **professional preference / release threshold:** would a domain expert choose or approve it?

Do not average them into one number until empirical correlations and threshold consequences are understood. Pairwise preference and absolute readiness are not interchangeable even in LH-Bench: only 60% of pairwise-winning Figma outputs meet the expert’s ≥4 pass threshold (Section 7.6).

### 3. Public/private split without hidden-rule unfairness

A defensible `skill-bench` split is:

- **Public:** task objective, allowed tools, safety constraints, artifact interface, general workflow phases, evidence/citation expectations, and actionable runtime verifier messages. These define legitimate professional expectations.
- **Private:** exact grader prompts/models, reference artifacts, held-out source contradictions, trap locations, exact weights, anchor boundary implementations, perturbation variants, and non-actionable audit checks. These preserve discrimination and detect superficial rubric gaming.
- **Internal calibration:** expert rationale, alternative acceptable procedures, adjudication examples, disagreement cases, and check-difficulty statistics.

Crucially, private checks should test consequences of public professional principles, not surprise obligations. A hidden check that demands an undisclosed formatting convention measures mind-reading; a hidden check that tests whether citations actually support a publicly required claim measures generalization.

### 4. Version interventions and measuring instruments independently

Each trial should record at least `skill_id/version/hash`, `rubric_id/version/hash`, `grader prompt/model/version`, `tool-interface version`, and `feedback-policy version`. LH-Bench’s generic `versions` dictionary (Appendix M) is a useful starting point, but typed fields and hashes are needed to prevent silent drift. The experiment matrix should include:

1. no skill + independent rubric;
2. public skill + independent hidden rubric;
3. public skill + rubric derived from the same expert model;
4. optionally, exact rubric disclosed to estimate evaluator-cue compliance.

Only this factorial structure can separate skill transfer, rubric quality, and leakage.

### 5. Make recovery a causal trace object

Represent error → feedback → attempted fix → verification outcome as linked events. Grade feedback specificity separately from recovery. Exclude or flag environment failures rather than crediting/penalizing the model, but retain them for operational diagnostics. The present schema’s causal event IDs can support this; it needs explicit feedback/recovery relation types and verifier-message visibility.

## Limitations and validity threats

1. **The central rubric comparison is confounded.** v1.1 versus v1.2 changes author source (LLM vs expert), rubric count (8 vs 4), grouping, weights, anchor language, and observability at once (Appendix F). Higher κ cannot be attributed specifically to “expert-authored skills.” A factorial rewrite holding rubric dimensions constant is required.
2. **Agreement is not validity.** Judges can agree on a disclosed procedural rule that is irrelevant or gameable. The human data support only the broad ranking boundary, and individual-level concordance is weak. There is no independent human process annotation against which the skill judges are validated.
3. **Dual-use skills create criterion contamination.** Agents receive the procedural artifact that defines post-hoc scoring. This may be appropriate when measuring instruction following, but it weakens claims about latent professional skill. Claude’s native skill training/integration may also create format familiarity advantages (Appendix D.1).
4. **Execution evidence is underpowered.** The skill ablation has seven paired runs, only two or three per harness. Task and run stochasticity can dominate effects, and one Claude dimension (build verification) decreases with the skill.
5. **Harness comparisons are not controlled model comparisons.** Model, orchestration, context compaction, native hook support, and skill injection mechanism differ. Claude and Gemini receive automatic post-tool hooks; Codex gets raw preview output. These are real production differences but prevent causal attribution to model capability (Sections 3.3 and 9).
6. **Human baselines are narrow.** Figma preference comes from one domain expert. Position randomization helps bias but not inter-expert reliability, organizational preference variation, or calibration drift.
7. **The failure taxonomy uses an LLM extractor.** The paper does not report human validation accuracy for the 590 extracted error/recovery events. High recovery precision matters because adjacent retries and environment recovery can be mistaken for agent correction.
8. **Task sampling and missingness are incompletely characterized.** Figma scores use unequal run counts, output comparisons cover 31 rated tasks rather than all 33, and infrastructure failures are excluded. The exclusion protocol and missingness mechanism could affect rankings.
9. **Operational reproducibility is partial.** The paper names public Hugging Face datasets and a rubric path, describes containers and MCP tools, and gives schema/prompt examples. Yet commercial harness versions, proprietary models, credentials, production Figma APIs, Modal/GCS infrastructure, and placeholder venue metadata make exact reproduction expensive and time-sensitive.
10. **External validity remains open.** Two media/code-production environments demonstrate breadth of artifact type, not breadth of enterprise decision work. Neither directly tests regulated decisions, spreadsheets with material financial consequences, adversarial source contradictions, or stakeholder negotiation.
11. **Safety realism is limited.** Harnesses run in approval-bypass/trust modes inside isolated containers. Sandboxing is sensible, but it does not test authorization boundaries, irreversible side effects, or whether an agent appropriately refuses unsafe professional actions.

## Reproducibility and operational realism

The paper is unusually concrete about interfaces: frame manifests, line-span citations, process-rubric weights, output-rubric weights, sample judge JSON, skill injection paths, persistent state, tool categories, and environment setup all appear in the appendices. It also preserves production messiness by counting tool, dependency, configuration, runtime, and preview errors. Public dataset URLs are listed in Section 5.5.

However, “open release” should not be read as turnkey replication. The manuscript refers to a repository file (`verifiers/figma-to-code/process_rubrics.json`) without giving a repository URL in the paper, the DOI is a placeholder, and several evaluated model names are future/proprietary services. A replication should pin dataset revisions, skill/rubric hashes, exact CLI commits, tool-server versions, judge prompts, excluded-run logs, and all API-visible fixtures. `skill-bench` should consider a benchmark run non-reproducible if any of these identifiers is absent, even if a final score is present.

## Concrete changes for skill-bench

1. **Extend the bundle contract with a typed procedural-skill artifact and crosswalk.** Add `skill_id`, semantic version, hash, visibility, workflow phases, ordering constraints, failure signatures, completion criteria, and mappings to trace-event predicates, artifacts, and checks. Keep skills separate from graders.
2. **Add typed evaluation-version provenance to every trial.** Record task, skill, rubric, grader prompt/model, tool interface, harness, and feedback-policy versions/hashes. A free-form list of enabled skill names is insufficient for controlled ablations.
3. **Represent runtime feedback explicitly.** Add verifier-feedback events with `diagnostic_code`, `specificity` (structured/actionable/ambiguous), `visibility`, `recommended_next_action`, and links to error and recovery events. Compute recovery rate only from validated event chains.
4. **Preserve score tiers.** Add named process, artifact, deterministic-compliance, and human-preference summaries; prohibit a single aggregate unless the aggregation policy and tier weights are versioned.
5. **Require leakage review before release.** Every check should declare whether its exact boundary is shown to the agent, merely implied by public guidance, or fully held out. Validate that private checks do not introduce hidden requirements.
6. **Pilot with an ablation-ready task.** The first expertise-transfer pilot should have at least two valid procedures, public workflow principles, private consequence checks, and a four-condition skill/rubric design. Judge both compliance and artifact quality to see whether disclosed procedure improves professional outcomes or only process scores.
7. **Human-calibrate thresholds, not merely rankings.** Collect at least two experts’ independent release/readiness ratings plus pairwise preferences on a stratified subset. Report disagreement and adjudication; do not infer an approval threshold from automated ranking alone.

## Action items for repository

- [x] Preserve the full v2 PDF and text extraction under `data/papers/` and record the immutable paths/hash above.
- [x] Document the skill → trace boundary → artifact → grader crosswalk and the public/private split in this review.
- [ ] Build and test an ablation-ready procedural-skill/evaluation-version schema extension, including leakage declarations and verifier-feedback/recovery edges.
- [ ] Apply that extension to the first pilot scenario and run the four-condition skill/rubric ablation before treating `SKILL.md` compliance as domain-skill evidence.
