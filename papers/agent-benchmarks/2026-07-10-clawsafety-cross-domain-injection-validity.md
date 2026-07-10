# ClawSafety: action evidence matters more than a binary attack-success headline

## One-sentence contribution

ClawSafety moves prompt-injection evaluation from harmful text toward consequential agent actions across ordinary evidence channels, but its strongest reusable contribution is the **source-authority × action-consequence design space**, not the reported 40–75% attack-success ranking: the immutable v2 paper does not disclose enough scenario provenance, scoring, result inventory, or treatment detail to audit those rates, and the post-v2 partial release exposes major scorer, reproducibility, and real-side-effect gaps.

## Why this matters

This review advances charter objectives A, B, and C by testing how adversarial evidence, authority, tool use, and harmful state transitions should enter a general knowledge-work benchmark. Personal agents are a methodological case, not a scope boundary. The relevant construct recurs in finance, healthcare, law, engineering, and operations: an agent encounters content through a source that is legitimate to inspect, but the content is not necessarily authorized to govern a consequential action.

ClawSafety's useful correction is that a safe-looking final answer is not enough. A benchmark must observe whether an agent read an injected source, adopted its claim, attempted an action, changed protected state, exposed information, completed useful work, detected or repaired damage, and left residual harm. The paper gestures toward this chain but mostly collapses it into majority-voted binary ASR.

## Research question

The paper asks whether safety alignment survives when five model backbones operate through privileged agent scaffolds and encounter indirect prompt injections in skill files, apparently trusted email, or web pages across five synthetic professional workspaces; it also asks whether vulnerability depends on model, scaffold, domain, action type, source trust, conversation length, and colleague identity (paper pp. 1–9, 16–24).

The auditable question is narrower: under the authors' synthetic scenarios and undisclosed paper-time harness, how often did a configured system satisfy a case-specific binary definition of fully completed harm after three attempts and majority reduction? The paper does not identify deployment risk, domain safety, or a backbone-only safety hierarchy independently of scenario construction, attack optimization, framework/tool policy, scoring, and missing-run handling.

## Sources and reading record

**Immutable paper read in full**

- Record: https://arxiv.org/abs/2604.01438v2
- PDF: https://arxiv.org/pdf/2604.01438v2
- Local PDF: `data/papers/pdfs/2604.01438v2-clawsafety-cross-domain-prompt-injection.pdf` (24 pages; SHA-256 `fd0dd66573f7e8989254ca900eab0ed51d6925e594242b811b58918ff04df0c6`)
- Local text: `data/papers/text/2604.01438v2-clawsafety-cross-domain-prompt-injection.txt` (SHA-256 `ad59cee04527d4235705b6896c97b225e925eb094f50684107043112ca3d14f0`)
- Date read: 2026-07-10.

**Official release inspected completely**

- Repository: https://github.com/weibowen555/ClawSafety
- Pinned commit: `5baf6fb40ab41bce40debf502f08e05320280d20`; tree `c32c7f4e417b4caee898d65a6c370206aeff7e9d`.
- Local archive: `data/sources/releases/2604.01438v2-clawsafety/weibowen555-ClawSafety-5baf6fb.zip` (SHA-256 `e82e7940869fb869b14aee8d581cdb34e5000c8bc6aa97fb49acfd3051c1e950`).
- Recursive tree and provenance: `data/sources/releases/2604.01438v2-clawsafety/github-tree.json` and `data/sources/releases/2604.01438v2-clawsafety/provenance.json`.

The commit is dated 2026-04-15, eleven days after immutable v2. It is **post-v2 release evidence**, not paper-time implementation evidence. The 13-entry tree contains setup documents, a generic condensed template, one S2 financial workspace, and one S2 skill/email case program. It omits four domains, web cases referenced by the README, the full 64-turn cases, trajectories, judgments, and result tables.

## Methodology and system

### Threat model and task construction

The attacker may alter exactly one source channel but not the system prompt, model weights, or framework. The paper crosses five domains with three vectors and eight cases per domain-vector cell, yielding 120 cases. Five stated action types are exfiltration, file/configuration modification, destination substitution, credential forwarding, and destructive action (paper pp. 3–5, 16–17).

Each synthetic workspace reportedly contains 50–60 heterogeneous files, at least four colleague personas, email/chat histories, configurations, one opaque database, protected assets, and domain-specific pressure. A 64-turn conversation has warm-up, context-building, injection encounter, and disclosure phases. The benign user does not directly request harm; adversarial content is planted in a skill, spoofed email, or page (paper pp. 4–5, 17, 22).

Scenario sourcing is not documented as an expertise-transfer process. The paper names no financial, clinical, legal, security, or operations experts; gives no primary-domain standards or incident corpus; reports no author qualifications, elicitation protocol, professional review, rejected scenarios, inter-reviewer agreement, or task-level provenance. “Realistic,” “ecological validity,” domain authority, and expected consequences are author claims over synthetic workspaces, not validated findings.

### Attack development

The authors iteratively optimize attacks against frontier systems. Skill attacks replace familiar files, hide side effects in import chains, place values in SQLite, avoid security vocabulary, and align instructions with current work. Email attacks progress from one source to five planted corroborating sources. Web attacks progress through 23 iterations from failed value substitution to high-severity compliance framing (paper pp. 18–22).

This is valuable red-team methodology but creates **adaptive item-selection bias**. Cases are retained after model-guided refinement; “hard boundaries” and vector rankings therefore describe this attack-development process, not a fixed representative distribution of naturally occurring attacks. The paper does not preserve candidate generations, failures by model, stopping rules, held-out attack families, or independent validation. The same systems appear to shape and then be measured by the instrument.

### Configured systems and execution

The paper evaluates five backbones on OpenClaw and Sonnet 4.6 on Nanobot and NemoClaw. It says native default prompts/tools are retained while only the API endpoint changes; this is appropriate for configured-system measurement but does not isolate a backbone effect. NemoClaw adds filesystem, network, and routing policy, while Nanobot and OpenClaw differ in prompts, memory, tool wrappers, context management, and execution behavior (paper pp. 5–6).

Paper-time identity is internally inconsistent: §4.1 says OpenClaw `v2026.3.11`; §4.3 says `2026.3.12`. Model snapshots, API dates, temperatures, sampling parameters, provider retries, system prompts, tool schemas, AMI ID/hash, dependency lockfiles, network allowlists, CDN content hashes, and interceptors are absent.

The paper says every case starts in a fresh custom-AMI EC2 instance, external actions are intercepted, and three trials are majority-reduced (paper p. 6). It does not specify what “independent” means, how randomness is seeded, whether environment/API state is shared, or how timeouts, refusals, invalid runs, tool errors, and partial execution are handled.

### Scoring

ASR is defined as full completion of the intended harmful action, with examples based on output content or trusted-file overwrite. Full tool calls are reportedly recorded (paper p. 6). Yet no general case-to-predicate specification, adjudication procedure, trace schema, state-diff contract, evaluator identity, or reliability study is given. The paper claims “graded harm scores” in related-work positioning (p. 3), but the reported quantitative metric is binary ASR after majority vote. Partial compromise appears only in the three-case narrative, where quoting an attack value in a warning crosses an unspecified partial threshold (pp. 7–8).

Utility is not measured. A model can score “safe” by refusing, failing to retrieve the source, timing out, or never completing the benign task. The design therefore cannot distinguish secure useful completion from blanket refusal, incapability, environmental failure, or safe recovery.

## Evidence and results

### Main reported results

For OpenClaw, Table 1 reports overall ASR from 40.0% (Sonnet 4.6) to 75.0% (GPT-5.1), with skill > email > web for all five models. Sonnet reportedly has 0% ASR for credential forwarding and destructive actions. The same Sonnet backbone is reported at 40.0% on OpenClaw, 48.6% on Nanobot, and 45.8% on NemoClaw (paper pp. 6–9).

These are descriptive paper claims, not locally replayed results. No trajectories, per-case outcomes, three-replicate rows, majority labels, missingness ledger, or aggregate computation are released. There are no confidence intervals, task/scenario-clustered uncertainty, replicate disagreement rates, multiplicity controls, or uncertainty for rankings and differences.

### Arithmetic and denominator conflict

The declared 2,520 trials exactly equal `5 backbones × 120 cases × 3 trials + 2 extra scaffolds × 120 cases × 3 trials`. But alternate-scaffold vector rates such as 33.3%, 58.3%, and 20.8% are not attainable as binary proportions over the stated 40 cases per vector; they align with counts over 24 observations per vector. Their overall rates align with 72 outcomes (Nanobot 35/72 = 48.6%; NemoClaw 33/72 = 45.8%). If those are 72-case scaffold panels, the corresponding total is 2,232 trials, not 2,520. If all 120 cases were run, the vector denominators and displayed rates need another unexplained aggregation rule.

This also weakens claims that scaffold effects interact across all five professional domains. The paper provides no cross-scaffold case inventory or domain table that resolves the denominator.

### Ablations and case studies

The conversation-length ablation uses eight S2 cases and two models, but Table 3's percentages move in 2.5-point increments (e.g., 77.5%, 92.5%, 95.0%), which are not binary proportions over eight majority outcomes. They could reflect 40 subobservations or token/case-level averaging, but the estimand is not stated (paper p. 8). The study also changes context exposure and opportunity count together, so it cannot attribute vulnerability to “internalized team norms.”

The stakeholder-identity ablation reports 40/40 versus 19/40 leaked tokens across eight S5 cases, not case-level ASR. Tokens within a case are dependent, only one model and action family are sampled, and names also change source-linkability. It supports a narrow association between identity-bearing context and token inclusion, not a general causal claim that identity verification is the primary trust mechanism (paper p. 8).

The imperative/declarative argument rests on three selected S5 examples. Even if delivery and styling match, payload semantics and requested consequence differ: database update, incident-log update, and discrepancy reporting are not interchangeable treatment units. No randomized paraphrase set, repeated trial table, or independent coding supports “bypasses all defenses regardless of content” (paper pp. 7–8).

The five qualitative cases are useful hypotheses—operational specificity, mechanism-versus-symptom detection, role relevance, compliance framing, and familiar-file provenance—but lack released trajectories or a selection/coding protocol. They cannot establish prevalence.

## Official release audit

The post-v2 release is useful as an implementation witness and sharply narrows reproducibility claims.

1. **Partial and non-runnable as archived.** `README.md` advertises S2 skill/email and web files, but `s2_web_cases.py` is absent. The case program expects `s2_workspace_v15.tar.gz` and `s2_preload_session.jsonl`; the archive contains `s2_workspace.tar.gz` and no preload. Setup files contain explicit placeholder sections. The release cannot reproduce paper runs without unrecorded repairs and dependencies.
2. **Different evaluation condition.** The released S2 program is a 10-turn development format, not the 64-turn paper protocol. It declares 17 cases and three later model variants (Sonnet 4.6, Gemini 3 Flash, GPT-5.4 nano), not the paper's 24 S2 cases and five-model matrix.
3. **No executable ASR scorer.** Both template and S2 use Inspect's `match()` on a dummy `Sample(input="done", target="done")`. The generic template forces `state.output.completion = "done"`, making the benchmark scorer pass independently of safety. The S2 program never assigns completion and only prints manually interpreted indicators. It has no function converting case type plus trace/state observations into ASR, partial harm, safety, or utility.
4. **Observation conflation.** The S2 logger counts a honey token anywhere in the accumulated agent text as leakage, even when quoted in a refusal; separately inspects sent Gmail content; tests a few file paths; and searches command strings. It does not assign source exposure, adoption, attempted action, completed action, recipient authority, residual state, recovery, or useful-task completion. Its own partial-compromise narrative illustrates why string presence is not full harm.
5. **Real external-action path.** Contrary to the paper's intercepted-side-effect description, the released program generates a Gmail CLI whose `send` command calls the live Gmail API. The EC2 guide permits all outbound traffic. Credentials are written into a sandbox script, and “sent after date” queries can mix unrelated account activity. This is not a demonstrably mock-only harness and creates safety, privacy, attribution, and reproducibility risks.
6. **Mutable environment.** The program installs `openclaw@latest`, performs live apt installs, uses provider APIs and Gmail, and does not pin the AMI or packages. The guide's smoke test and scaffold-install sections are incomplete. A fresh EC2 instance is useful isolation from the host, but unrestricted egress and real OAuth do not establish consequence containment.
7. **Workspace evidence.** The nested S2 tar has 35 regular files, below the paper's stated ≥50-file minimum. It is a later condensed artifact, so this does not falsify paper-time workspaces; it does show that release-level “complete professional workspace” claims need version-specific conformance checks.

The release contains no result inventory, trajectories, state diffs, per-case judgments, or scripts reproducing Table 1. The paper's headline rates therefore remain unauditable.

## Unique insight

ClawSafety's central transferable object is not “prompt injection” as a single binary condition. It is an **authority-to-consequence chain**:

1. **source placement** — where adversarial content exists;
2. **source eligibility and authority** — why the agent may read it and what actions it is allowed to govern;
3. **exposure** — what the configured agent actually observed;
4. **interpretation/adoption** — which claims or instructions changed its belief or plan;
5. **attempt** — what tool or communication action it initiated;
6. **realization** — what protected state, recipient, or external system actually changed;
7. **severity and reversibility** — confidentiality, integrity, financial, legal, clinical, or availability consequence;
8. **detection/recovery** — whether harm was prevented, contained, reversed, or left latent;
9. **benign utility** — whether the authorized task was still completed.

A binary token match or final-state check observes only selected links. Safe refusal, source non-discovery, failed tool invocation, intercepted action, realized mock harm, and repaired harm are different outcomes. Likewise, a skill, email, and web page are not merely ordinal “trust levels”: they differ in attacker capability, authentication, placement, persistence, task relevance, corroboration, and action affordances. Comparing their raw ASR without matched payload semantics and authority contracts does not identify a trust gradient.

For skill-bench, safety should be an independently versioned score family and validity argument, not a boolean attached to correctness. The benchmark should preserve both public authority rules and private fair consequences, then grade authorized useful completion and unauthorized consequence separately.

## Limitations and validity threats

### Construct and content validity

- No domain-expert or incident-corpus grounding supports realism, frequency, severity, or professional action thresholds.
- Five synthetic roles do not establish cross-domain safety coverage; each domain is one authored scenario family.
- Attack optimization against evaluated models entangles item difficulty, selection, and measured system safety.
- Skill, email, and web cases are not shown to be semantically matched or to grant attackers comparable capabilities. Multi-source email poisoning is especially different from a one-channel threat if it modifies several corroborating files.
- Harm categories mix information disclosure, state integrity, attempted communication, and physical/professional consequence without a common severity or reversibility model.
- Utility, over-refusal, and authorized task completion are absent.

### Measurement and statistical validity

- Binary ASR lacks a released predicate contract and adjudication reliability.
- Majority reduction discards replicate disagreement and makes uncertainty look smaller; no case- or scenario-clustered intervals are reported.
- The 2,520-run claim conflicts with alternate-scaffold rate denominators.
- Ablation denominators and estimands are under-specified.
- Qualitative cases are selected without a coding frame or negative-case inventory.
- No missing/invalid/tool-failure policy separates system unavailability from safe behavior.

### Configured-system and causal validity

- Model, scaffold, tool policy, prompt, memory, context handling, network controls, and file semantics vary jointly.
- Cross-scaffold differences are descriptive configured-system contrasts, not “scaffold choice alone” unless task inventory, payload, environment, observation, and all non-scaffold components are matched and pinned.
- Paper model/scaffold versions are incomplete and internally inconsistent.
- The claim that declarative speech acts cause bypass is based on three non-equivalent selected cases.

### Reproducibility and operational realism

- The release postdates v2 and is a partial condensed development snapshot.
- Required files are missing or misnamed; installs and APIs are mutable.
- The shipped Inspect scorer does not compute safety outcomes.
- Live Gmail sending and unrestricted egress contradict a mock-only consequence boundary.
- No full trajectories, result rows, state manifests, grader decisions, or aggregation script are released.
- Synthetic EC2 execution safely avoids production systems only if outbound actions, credentials, and recipient endpoints are demonstrably intercepted; the released path does not enforce that invariant.

## Transferable benchmark-design lessons

1. **Predeclare an authority matrix.** For every source and action, state who may create/modify the source, what claims it can support, which actions it may authorize, required corroboration, and escalation/abstention rules.
2. **Separate source placement from model exposure and adoption.** Preserve evidence locators, trace observations, belief/plan deltas, and tool-call consequences; do not infer adoption from source existence.
3. **Use an action-state ledger.** Record intent, attempted tool call, interceptor decision, mock/real target, pre/post state, severity, reversibility, detection, recovery, and residual harm.
4. **Jointly score utility and safety.** Distinguish secure useful completion, safe escalation, over-refusal, benign-task failure, blocked attempt, partial harm, realized harm, and repaired harm.
5. **Make consequence containment executable.** Canary network, filesystem, email, credential, and payment boundaries before trials; fail closed if a real endpoint or non-synthetic secret is reachable.
6. **Match vector comparisons.** Hold benign goal, harmful consequence, payload proposition, attacker knowledge, corroboration budget, and exposure opportunity fixed where a trust-channel effect is claimed.
7. **Treat adaptive attacks as development data.** Freeze a held-out attack set or use nested red-team/test splits; preserve generation/selection history and do not estimate prevalence from optimized retained cases.
8. **Retain replicate rows.** Report per-attempt outcomes, disagreement, invalid runs, and scenario-clustered uncertainty rather than only majority labels.
9. **Version the whole configured system.** Pin model snapshot/date, scaffold, prompt, skills, memory policy, tool adapters, AMI/container, packages, network policy, interceptors, task/payload, scorer, and aggregation.
10. **Validate professional consequences.** Domain experts should review source authority, plausible benign goals, action thresholds, severity, required confirmations, and recovery expectations—not merely surface plausibility.

These requirements have partial homes in the benchmark bundle, trace/root-cause records, artifact views, task projection, workspace integrity, task health, metrics, and validity arguments. What remains missing is an exercised cross-domain safety/action-state conformance slice.

## Concrete repository actions

1. **Add one nonduplicate build task:** create a compact adversarial-action conformance slice using existing contracts, not a parallel safety subsystem. It should plant a legitimate task, one unauthorized instruction in an ordinary source, and mock tool endpoints; distinguish exposure/adoption/attempt/interception/realization/recovery; jointly score utility; and fail if external network/email or protected-state containment canaries do not pass.
2. **Do not import ClawSafety rates as calibration targets.** Treat 40–75%, the 8.6-point scaffold difference, the trust gradient, and hard boundaries as unaudited paper reports until a versioned per-run inventory resolves denominators and reproduces aggregation.
3. **Use the paper's attack-development patterns as task-authoring hypotheses.** Operational specificity, corrupted corroboration, workflow alignment, compliance reframing, opaque formats, and familiar-file provenance are valuable difficulty knobs, but each needs independent expert grounding and held-out validation before becoming a general benchmark claim.
4. **Require safety releases to ship inert-by-default.** No live OAuth or unrestricted external send path should be necessary for evaluation; mock recipients, synthetic credentials, explicit egress allowlists, and destructive-action interceptors must be verifiably active before an agent starts.
