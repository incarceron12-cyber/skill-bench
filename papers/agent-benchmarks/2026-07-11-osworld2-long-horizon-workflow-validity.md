# Paper Review: OSWorld 2.0 — Long-Horizon Workflow Validity

- **Paper:** https://arxiv.org/abs/2606.29537v1
- **Version read:** immutable v1, submitted 28 June 2026; arXiv metadata contains no withdrawal/retraction notice
- **Date read:** 2026-07-11
- **Local PDF:** `data/papers/pdfs/2606.29537v1-osworld2-long-horizon-workflow-validity.pdf` (68 pages; SHA-256 `25943e787486d74b89a13ff51d6c6b86435f01d00f1db130f20a3c479cdfa33b`)
- **Local text:** `data/papers/text/2606.29537v1-osworld2-long-horizon-workflow-validity.txt` (SHA-256 `e1cd07997830838ec70751152ed47ac1c48b274c4d6a7d3671c837e2d15bea02`)
- **Official release inspected:** https://github.com/xlang-ai/OSWorld-V2 tag `v2026.06.24`, commit `2b9b7b4eb73243d557bdbf2998fe18d8e18e19c6`; this is the exact release named for the paper experiments and predates v1 by four days
- **Release archive:** `data/sources/releases/2606.29537v1-osworld2/OSWorld-V2-v2026.06.24.tar.gz` (SHA-256 `49f246943f2902a3ad821a1d8de7367f234e8163e3db329535f1ba033503d66f`)
- **Release provenance:** `data/sources/releases/2606.29537v1-osworld2/provenance.json`
- **Evidence boundary:** the complete 68-page paper and exact tagged public code were read. The 108 official task classes are auto-gated on Hugging Face; their metadata/file manifest was inspected, but their contents were not downloaded or inferred. Public trajectory archive metadata was inspected, not the large archives themselves.
- **Tags:** computer use, long horizon, workflow state, partial reward, dynamic environment, safety, release lifecycle

## One-sentence contribution

OSWorld 2.0 makes a real methodological advance over OSWorld 1.0 by changing the evaluated unit from a short desktop action to a dense, stateful workflow with cross-source evidence, evolving requirements, user clarification, artifact checks, and separate safety diagnostics; however, it demonstrates difficulty and richer observability on 108 heavily authored environments—not representative professional capability—because roughly 90% of tasks came from internally trained annotators, checkpoints are development-shaped by frontier rollouts, nearly all results are single attempts, and the exact tagged release does not yet enforce the release-verification contract its paper claims.

## Why this matters for skill-bench

This review advances charter objectives A, B, and D. OSWorld 2.0 is the explicit successor gap in `docs/concepts/web-tool-computer-benchmark-evolution.md`, and it tests a general hypothesis central to skill-bench: **does moving from isolated actions to end-to-end workflows reveal failures that final-state tasklets hide?** The evidence says yes. Agents commonly reach about half of checkpoint credit while rarely satisfying every obligation, and failures concentrate in stale evidence, unresolved conflict, missing user escalation, incomplete verification, and state drift rather than elementary clicking (Sections 3–4, pp. 7–14).

The benchmark is a methodological case, not a commitment to computer-use evaluation. Its reusable machinery is a workflow-state ledger: requirements and evidence arrive over time; intermediate decisions depend on earlier sources; checkpoints observe selected final consequences; process diagnostics detect unsafe shortcuts; and an exposure label asks whether a designed challenge was actually reached. The central caution is that more realistic surfaces do not automatically yield a valid occupational sample or complete oracle.

## Research question and claim boundary

The paper asks whether computer-use agents can complete long, coherent workflows in stateful desktop environments, especially when tasks require cross-application coordination, hidden-state recovery, changing information, user interaction, domain artifacts, and verification.

The evidence supports these bounded conclusions:

1. the authors built and evaluated 108 substantially longer workflows than OSWorld 1.0, with median estimated skilled-human operation time around 1.6 hours, 27.25 checkpoints per task on average, and 31 self-hosted services (Sections 2.1–2.2, pp. 2–7);
2. the best reported configured system completed 20.6% of tasks and earned 54.8% partial score at 500 steps, showing a large last-mile gap under this instrument (Table 3, p. 8);
3. final-state checkpoints distinguish no progress from substantial incomplete work, while separate trajectory audits reveal shortcut and safety behavior invisible to main reward;
4. dynamic updates, bounded user simulation, cross-source artifacts, and multi-item state make information maintenance observable in ways OSWorld 1.0 did not;
5. the exact release includes substantial runnable infrastructure, evaluator and safety libraries, pinned task/website tags, a task hash, and provider image identities; and
6. longer human-estimated tasks have lower single-run binary completion in the evaluated sample (Table 21, p. 38).

It does **not** establish that 108 tasks represent professional work, that the human-time estimates are reliable occupational durations, that internal annotators acquired expert-equivalent domain judgment, that each checkpoint set is sound and complete, that partial reward is interval-scaled progress, that phenomenon tags isolate causal capabilities, that provider images are equivalent, that scores are repeatable, or that success/failure predicts deployment readiness.

## Methodology and system

### Task sourcing: authentic artifacts without occupational sampling

Candidate workflows came from brainstorming, trained-annotator research, practitioner interviews, questionnaires, and LLM proposals. About 90% of retained tasks were produced by a small internal annotator group who learned domains from tutorials, official documentation, and software experimentation, then designed the instruction, artifacts, setup, and evaluator; a second annotator checked feasibility, redundancy, and ambiguity (Section 2.1.1, pp. 2–3). Interviews yielded high-quality but costly ideas; questionnaires had poor retention; synthetic proposals were shallow, unrealistic, and reward-hack-prone.

This is unusually candid and useful evidence against easy scaling assumptions. It also limits the “professional” claim. Appendix D says external practitioners only supplied high-level inspiration; they did not operate tasks, verify rubrics, inspect trajectories, or validate artifacts, and received no compensation (p. 34). Internal tutorial-trained authors may create plausible workflows, but the paper reports no occupation sampling frame, author count by domain, author proficiency assessment, task-to-practitioner lineage, expert approval, inter-author disagreement, or comparison against naturally occurring work products. “Authentic artifacts” and a wage-bill mapping do not convert convenience-authored tasks into a representative sample of professional performance.

The economic analysis is especially weak as validity evidence. An LLM helped author rules that deterministically map instructions/application metadata to SOC families; qualitative match strength becomes high/medium/low confidence, and wage bills are summed as a “GDP proxy” (Appendix G.1, pp. 37–38). This describes nominal coverage. It is not task-frequency weighting, economic-value weighting, or evidence that benchmark scores estimate labor substitutability.

### Environment and workflow state

Every task starts from a task-specific workspace containing files, open documents/tabs, website records, messages, prior submissions, and reference material. Thirty-one self-hosted services replace live email, banking, chat, travel, and business portals. Cookie-scoped identities and state/file APIs allow reset and concurrent users; the open web remains accessible (Section 2.1.2, pp. 3–4; Appendix C.1–C.2, pp. 27–29).

This repairs major OSWorld 1.0 weaknesses: information is distributed across coherent sources, state can evolve, and services can be reset. Yet the substrate is still authored. Self-hosted clones stabilize layouts and histories at the cost of production behavior, institutional policy, permissions, latency, edge cases, and downstream consequences. Renaming services prevents accidental navigation to real sites but may also create benchmark-specific cues. Open-web access preserves retrieval realism while adding search/provider/time variation and a route to task leakage.

Ten tasks inject semantically relevant messages during execution; six include continuously moving visual state; six require proactive user interaction. The distinction between **dynamic environment** (task facts change) and **streaming interaction** (screen state changes between observation and action) is conceptually sharp and worth retaining (Appendix C.5, pp. 31–33). However, the moving-popup example is described as structurally impossible for screenshot-based agents. Such a task measures an observation/action interface limitation as much as reasoning. It is diagnostic only if the configured-system treatment records streaming access and the claim is bounded accordingly.

### Evaluation and checkpoint semantics

OSWorld 2.0 replaces OSWorld 1.0’s binary-only outcome with task-specific final-state checkpoints, averaging 27.25 per task. Binary completion is exactly partial score 1.0. Checkpoint order is not enforced, allowing alternative action paths (Section 2.1.3, pp. 4–5; Appendix G.2, p. 38). Functional checks are preferred; model judgments contribute 11.53% of total score and never more than half of one task.

This is a meaningful repair, but checkpoint credit is not self-interpreting “progress.” A checkpoint can be a prerequisite, an independently valuable outcome, a reversible intermediate residue, or a harmful shortcut. Averaging weighted checks assumes author-chosen weights and conjunction structure. The paper says humans reviewed “balanced weights,” but gives no weighting protocol, dependency graph, threshold calibration, recipient-utility study, or evidence that a 0.5 score has comparable meaning across tasks. Main reward also omits eight separate safety diagnostics by design. Partial score is therefore an instrument-specific coverage fraction, not a ratio scale of professional completion.

Model judges were tested on three states per task from 20 tasks, against human labels, across four judge models. Sonnet 4.6 achieved 98.5% checkpoint agreement and 98.6% score-weighted agreement (Appendix E.1, pp. 34–35). This supports selected-state classification, not judge reliability over all 108 tasks or adversarial outputs. The states came from rollouts plus manually added cases; sampling, class balance, annotator agreement, uncertainty, and held-out status are absent. Reusing Sonnet 4.6 as both judge and user simulator also introduces a shared model-dependent component.

### Quality assurance and development reuse

A coding agent generates unit tests; two humans solve/cross-check each task; multiple frontier-agent rollouts expose reward hacks, false negatives, and unanticipated paths. Disagreement triggers task/rubric revision or removal (Section 2.1.4, p. 5). This is strong instrument engineering. It is also outcome-conditioned development: evaluated model families help shape the final checkpoint set. Without a frozen pre-audit suite or held-out tasks, later scores partly measure systems against an instrument repaired around related frontier behavior. QA establishes a healthier benchmark, not unbiased generalization.

The release preserves broad OSWorld metric libraries and a native Python task interface. A task can set up files/services, collect final state, and return a scalar or richer result. But the official 108 implementations are auto-gated, so this review could not inspect per-task public-basis/checkpoint mappings, hidden-state accessibility, dynamic-update timing, or alternate-solution handling. Public `evaluation_examples` are largely OSWorld 1.0 examples, not substitutes for the gated v2 tasks.

## Evidence and results

Seven model families were evaluated with screenshot observations and either native Claude computer-use actions or pyautogui code. GPT-5.5 always batched actions; Claude batching was a separate tool condition. Output caps and reasoning settings differed; runs used release `v2026.06.24`, AWS in `us-east-1`, residential proxies, and a three-second post-action pause (Section 3.1, p. 7). These are configured-system comparisons, not model-only comparisons.

At 500 steps, Opus 4.8 max-thinking with batching scored 20.6% binary / 54.8% partial at about $72.40 and 224K output tokens per task; GPT-5.5 scored 13.0% / 49.5% at about $25.50 and 37.1K tokens (Table 3, p. 8). The paper usefully separates score, tokens, turns, and cost. Its claim that each added accuracy point costs disproportionately more is descriptive interpolation across different systems/settings, not a stable marginal-cost law. There are no confidence intervals, repeated runs, or paired stochastic comparisons.

Human-time bins show binary completion falling to zero in the longest bin for four shown systems (Table 21, p. 38). But each task was timed by two benchmark annotators using coarse ranges; range midpoints were combined by geometric mean. There is no direct human completion sample, timing agreement, censoring protocol, domain stratification, or adjustment for task composition. Horizon co-varies with apps, artifacts, phenomena, and domain. The evidence supports an association in this suite, not a causal horizon scaling law.

Phenomenon analysis improves on raw tags by labeling each model–task–phenomenon pair as Handled, Blocked, or Untested. This exposure distinction is a valuable diagnostic primitive: a low score should not be attributed to a challenge the trajectory never reached. Yet the paper does not specify who labeled all pairs, how many raters, agreement, blinding, adjudication, or uncertainty. Tags overlap heavily and only three models receive the main exposure audit. The labels remain post-hoc causal judgments, not interventions.

Behavior analysis is explicitly descriptive. GPT-5.5 xhigh generated labels from structured reports, humans verified them, and each of 108 trajectories per model received overlapping labels plus one dominant mode (Appendix F, pp. 35–37). The paper rightly notes one run per model and capability/strategy confounding. Still, headline statements such as “every model spends almost none of its budget on repair” depend on model-authored activity classification and fixed five-step windows, with no reported rater reliability.

## Safety evidence: the strongest conceptual repair, still diagnostic

Eight safety checks cover credential leakage, disk exhaustion, document integrity, privileged groups, lingering processes, Snap bypass, sudoers changes, and X11 access (Appendix E.2, pp. 35–36). The paper gives compelling cases where main reward passes despite a planted secret leak, a moving-popup task is solved through hidden same-origin APIs, and broad process kills discard LibreOffice recovery data (Appendix H.4, pp. 62–68).

This is the clearest evidence that final-state success alone is insufficient. The release’s `desktop_env/safety/` modules preserve baselines and append typed safety results separately from main reward. Skill-bench should retain that separation.

But only a subset of tasks receives safety checks, severe checks are sparse, and no denominators by check eligibility or false-positive/negative calibration are reported. The hidden fake-credential check has a fair professional basis—do not push secrets—but the paper does not show that every safety obligation is publicly grounded. “Bypassing user-visible interfaces” also mixes policy, construct, and method: direct APIs may be legitimate for a general computer-using agent unless the task declares a UI-bound workflow. Safety conclusions therefore require typed permission and interaction-boundary policies, not post-hoc disapproval of efficient paths.

## Unique insight

OSWorld 2.0’s deepest transferable contribution is **workflow completion as a conjunction over evolving obligations, not a long action count**:

`initial goal + source-backed constraints + discovered state + timed updates + user clarifications → decision revisions → artifact/state consequences + safety consequences`

A long task is diagnostically useful only when this chain is represented explicitly. The 27-checkpoint average is less important than the fact that obligations originate at different times and from different authorities. This suggests a **temporal obligation ledger** for skill-bench:

- requirement/evidence atom and authority;
- first-available event and whether the agent observed it;
- supersedes/contradicts/depends-on links;
- decision or artifact fields affected;
- required verification and repair;
- final check plus separate safety/side-effect check;
- challenge exposure status (`not_reached`, `reached_handled`, `reached_blocked`, `shortcut_bypassed`);
- observer-view sufficiency and adjudication evidence.

This separates four otherwise conflated failures: the benchmark never made evidence available; the agent never observed it; the agent observed but did not update its task model; or it updated locally but failed to propagate/verify the consequence. OSWorld 2.0’s prose analyses recognize these distinctions, but its public release does not expose them as a machine-auditable task contract.

A second insight is negative: **longer horizon amplifies oracle incompleteness as well as agent failure**. More applications, sources, updates, artifacts, and side effects create more legitimate paths and more omitted consequences. Fine-grained scoring makes partial work visible, but every additional checkpoint and hidden state also increases grader dependence. “Long horizon” is therefore both a construct intervention and an instrument stress test.

## OSWorld 1.0 → 2.0: retain, repair, and evidence that changed

| Claimed repair | What genuinely improved | What remains unsupported |
|---|---|---|
| Short actions → end-to-end workflows | Median annotated time rises from about 2 minutes to 1.6 hours; multi-app information dependencies and hundreds of actions expose state-maintenance failures | No representative work sampling, occupational frequency, or direct expert-time validation |
| Mostly binary → dense checkpoints | Partial work and last-mile failures become observable; binary completion remains strict conjunction | Weight validity, dependency semantics, cross-task scale comparability, alternate-solution error rates |
| Mixed/synthetic artifacts → “authentic” artifacts | Case studies show realistic receipts, tickets, drawings, videos, and prior records | Adaptation provenance, licenses per artifact, ecological fidelity, and expert acceptance are not fully reported |
| Static state → dynamic/user channels | Timed updates and clarification make stale grounding and escalation measurable | Timing equivalence, simulator behavioral validity, repeated reliability, and user-model treatment effects |
| Live web fragility → self-hosted services | Controlled state/reset, renamed clones, task-specific histories | Production semantics and consequences are projected away; hosted deployment and open web remain mutable |
| Final outcome → outcome plus safety | Separate checks catch harms that successful final states hide | Sparse coverage, eligibility denominators, fair-basis mapping, calibration, and severity aggregation |
| Mutable benchmark → release manifest | Tasks, website, code tag, task hash, AMI, and Docker artifact are named | Exact tagged runner does not enforce most manifest checks; provider equivalence is asserted, not demonstrated |

The successor is therefore not merely harder. It repairs observability and task structure. It does not yet repair inference-population validity, stochastic reliability, or fully executable release verification.

## Release audit and reproducibility

The exact tag contains 1,083 non-git files (about 50 MB unpacked), including runner/provider code, evaluator and safety libraries, a 14.2 GB Docker VM artifact identity, AWS AMI identity, task downloader, public v1 examples, and a benchmark release manifest. The task dataset API confirms 108 `task_*.py` paths and a manifest at revision `796f1aa...`; the website tag resolves to commit `0daaa450...`. This is substantially more inspectable than a paper-only benchmark.

However, release discipline is partly aspirational in the exact paper tag:

1. `benchmark_releases/osworld-v2-2026.06.24.json` says `status: active` while its description calls it a draft and says the matching code tag is pending—even though the tag exists.
2. `benchmark_releases/README.md` says the runner “should” later load the manifest, verify code/website/task/image identities, write verification status, and fail fast. Repository search found release selection in the **task downloader**, not enforcement of that full contract in the main runners.
3. provider equivalence is a maintainer statement; the release provides one AWS AMI and one Docker QCOW artifact, but no equivalence test report or state hash.
4. setup requires a 14.2 GB guest image, self-hosted GitLab/token for some tasks, hosted or separately deployed web services, AWS/network/security configuration, optional paid residential proxy, proprietary model APIs, and model-judge/user-simulator calls.
5. the public evaluation guide recommends inbound SSH and VNC from `0.0.0.0/0`, broad outbound traffic, and a documented default VM password. These are reproducibility instructions, not a secure isolation proof.
6. official task implementations are gated. Auto-approval reduces casual search leakage but is not a private test set; accepted users/models can still acquire setup and evaluator code, so access logging, rotation, canaries, and score-role transitions remain necessary.
7. the paper reports release provenance but not trial repeats, environment-health rates, invalid-run counts, retries, or uncertainty. Table 15 even has one missing Opus task score.

The release therefore supports implementation inspection and bounded reproduction attempts, but not cheap turnkey reproduction. The paper’s reported model costs alone imply thousands of dollars for one 108-task pass at the top configuration, before infrastructure, setup labor, judge/simulator calls, and repeats.

## Limitations and validity threats

1. Roughly 90% of tasks were internally authored after tutorial/document research, not contributed or approved by domain practitioners.
2. External interviews supplied inspiration only; practitioners did not validate tasks, artifacts, rubrics, or agent outcomes.
3. No occupational sampling frame or task-frequency weighting supports population claims.
4. The wage-bill “GDP proxy” maps nominal categories, not benchmark performance to economic value.
5. Authentic/adapted artifact provenance and fidelity are not reported task by task.
6. Self-hosted service realism is a projection, not production-system equivalence.
7. Dynamic-update schedules may couple performance to agent speed, batching, and the fixed three-second pause.
8. The user simulator is validated on isolated responses, not full interaction trajectories or treatment effects.
9. Model-judge validation uses selected states from only 20 tasks and reports no agreement uncertainty or human reliability.
10. Checkpoints and weights lack an explicit dependency/value model; partial scores are not calibrated units of completed work.
11. Frontier rollout-based rubric repair creates development reuse and possible benchmark-family favoritism.
12. Gated task code prevented independent per-task inspection in this run.
13. Almost all reported model-task outcomes are single attempts; stochastic reliability is unmeasured.
14. No task-clustered confidence intervals or paired uncertainty accompany system comparisons.
15. Models use different action languages, batching policies, caps, and reasoning settings.
16. Human duration is two annotators’ coarse expected ranges, not observed independent skilled-worker completion.
17. Horizon is confounded with domain, apps, artifacts, phenomena, and task composition.
18. Phenomenon tags overlap and do not isolate capability treatments.
19. Exposure labels are post-hoc causal judgments with no reported rater protocol or agreement.
20. Behavior labels are model-generated and human-verified without reported reliability.
21. Safety checks cover a subset and lack eligibility denominators, calibration, and severity thresholds.
22. UI bypass is not inherently unsafe unless the intended interaction/permission boundary is declared.
23. Main reward and safety remain separate but no validated aggregation or decision rule is supplied.
24. Open-web and residential-proxy dependence introduces time/provider contamination and variance.
25. Auto-gating slows leakage but does not prevent contamination after access.
26. The release manifest’s active/draft text is internally inconsistent.
27. Full release verification is documented as a future runner expectation, not enforced in the tagged runner.
28. Provider-image equivalence and reset determinism are asserted without a published conformance report.
29. Reproduction has high infrastructure, service, model, and human-operations cost.
30. No deployment, downstream recipient, or organizational study validates professional acceptance or consequences.

## Transfer to skill-bench: concrete changes

1. **Represent temporal obligations explicitly.** Extend existing task/source/trace records with availability event, authority, supersession, observation, adoption, affected decisions, repair, and verification links.
2. **Keep exposure separate from outcome.** A challenge label should produce `not_reached`, `handled`, `blocked`, or `shortcut_bypassed`; do not attribute raw task failure to every tag.
3. **Model checkpoint dependencies.** Distinguish prerequisites, gates, independent value, terminal deliverables, reversible residue, and safety consequences before weighting partial credit.
4. **Require partial-score calibration cases.** Plant no-progress, legitimate partial, superficially complete, unsafe complete, and alternative-complete states; estimate false pass/fail and test ordering/weight sensitivity.
5. **Treat dynamic timing as configured environment.** Record event trigger semantics (clock, action count, state condition), actual delivery/observation times, pause policy, batching, and replay equivalence.
6. **Validate user simulators end to end.** Compare scripted, model-simulated, and human-reviewed interactions on clarification correctness, information scope, latency, downstream effect, and inappropriate disclosure—not isolated response plausibility alone.
7. **Separate permission boundaries from outcome checks.** Declare whether APIs, shell, DOM, internal state, credential reuse, and direct file edits are allowed; score attempted and realized violations separately.
8. **Always pair workflow success with side-effect state.** Preserve pre/post snapshots and checks for integrity, secrets, permissions, resources, lingering processes, unrelated artifacts, and recovery/discard actions.
9. **Make release verification executable before claiming comparability.** Fail closed on code/task/source/environment hashes, provider-image identity, service health, reset result, external endpoints, and grader versions; do not rely on an `active` label.
10. **Use repeats selectively but honestly.** Given hour-scale cost, use task-clustered replicate allocation and report invalid/environment failures separately; one pass can be exploratory, not reliability evidence.
11. **Do not infer occupational value from category labels.** Require task-source sampling, expert acceptance, recipient handoff, and decision-loss evidence before professional/economic claims.
12. **Reuse existing contracts.** These requirements fit benchmark-bundle traces/checks, compounding evidence transitions, artifact-view admissibility, execution isolation, task health, validity arguments, and metric monitoring. No new schema task is warranted.

## Action items

- [x] Read the complete immutable v1 PDF/text and verify version/withdrawal status.
- [x] Archive and inspect the exact official code tag named by the paper.
- [x] Inspect task/trajectory release manifests and record gated/unmirrored boundaries.
- [x] Compare OSWorld 2.0 directly with the prior OSWorld 1.0 synthesis.
- [x] Separate observed successor repairs from unsupported professional, reliability, and release-comparability claims.
- [x] Map findings into existing contracts; add no duplicate build task.
