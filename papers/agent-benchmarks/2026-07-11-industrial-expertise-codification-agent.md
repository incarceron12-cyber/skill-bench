# Paper Review: Codified Expertise Improved Five Co-Designed Outputs, Not “Expert-Level” Work

- **Paper:** https://arxiv.org/abs/2601.15153v1
- **Authors:** Choro Ulan uulu, Mikhail Kulyabin, Iris Fuhrmann, Jan Joosten, Nuno Miguel Martins Pacheco, Filippos Petridis, Rebecca Johnson, Jan Bosch, and Helena Holmström Olsson
- **Date read:** 2026-07-11
- **Venue / source:** CAIN 2026; immutable arXiv preprint v1
- **Tags:** expertise-codification, industrial-case-study, visualization, RAG, procedural-rules, paired-evaluation, validity
- **Local PDF:** `data/papers/pdfs/2601.15153v1-how-to-build-ai-agents-by-augmenting-llms-with-cod.pdf` (11 pages; SHA-256 `60f467decf9fbb1806f643e8ec3ccfc41f9f1ccabe86ac3c16d178ae0eab51bf`)
- **Local text:** `data/papers/text/2601.15153v1-how-to-build-ai-agents-by-augmenting-llms-with-cod.txt` (SHA-256 `c3141788f67c603cef077135b84fda23a9814eac3f47c33a36c15e46278a4a13`)

## One-sentence contribution

An embedded Siemens case study turns two experts’ visualization guidance into executable rules, prompt instructions, request routing, and RAG-backed code generation, and reports much better ratings than an LLM+RAG baseline on five selected outputs; it demonstrates a plausible codification architecture and a strong **package effect on co-designed cases**, but does not identify tacit-knowledge transfer, non-expert capability, expert equivalence, cross-domain transfer, or the contribution of any individual component.

## Why this matters for skill-bench

This review advances charter objectives A and B through a directly on-scope industrial attempt to capture and operationalize expertise. Its concrete evidence is the immutable full paper and this reconstruction of the elicitation→representation→agent→evaluation chain. It clarifies an important uncertainty: when a system is authored and graded using the same expert rules, improved rule-conforming artifacts show that the package carries evaluator-relevant instructions—not necessarily that an agent acquired expert judgment.

The mode is targeted expansion. It does not narrow `skill-bench` to visualization: the reusable hypothesis is that expert guidance should be split by **execution semantics**—deterministic rules, contextual principles, and evidence-dependent judgments—and each representation should be independently ablated and tested on held-out incidents. Useful completion is a design boundary that prevents “codified expertise helped” from being upgraded to “non-experts now perform at expert level.” Existing expertise-transfer, participation, procedural-skill, validity, and paired-trial contracts already absorb the implications, so no duplicate build task is warranted.

## Research question and claimed answer

The paper asks how human domain knowledge can be captured, codified, and used to construct LLM-based agents capable of autonomous expert-level performance (pp. 1–2). It claims a four-step framework—expert interviews, complementary implementation, testing, and iteration—and a 206% output-quality improvement over LLM+RAG, with “expert-level” ratings across five scenarios (pp. 1, 8–10).

The evidence supports a narrower answer: two internal experts articulated concrete visualization rules; builders embedded those rules in a multi-component system; and 12 evaluators preferred the resulting five outputs on criteria substantially aligned with those rules. The study does not establish that tacit expertise was comprehensively captured, that a non-expert learned or retained it, or that the system matched independently sampled expert work.

## Methodology and system

### Industrial setting and elicitation

The first author was a Siemens employee with access to internal experts, proprietary data, documentation, and informal company discussions (p. 2). Two internal experts were interviewed separately for 60–90 minutes: one Simulation Analysis software expert and one visualization expert. Interviews were consented, screen-recorded, transcribed, and organized around workflow pain points, decision processes, rules, and heuristics. Open walkthrough questions were followed by direct and scenario-based probes (pp. 2–3).

The paper says experts directly provided clear actionable rules, so “interpretive analysis” was unnecessary (p. 3). Examples include checking objective convergence before analysis, using history plots for that check, limiting history plots to two variables, showing non-convergence with dashed lines, grouping related objectives, highlighting best designs, normalizing scales, and avoiding ornamental styling (pp. 3–4).

This is closer to **structured rule acquisition** than demonstrated recovery of tacit cognition. There is no coding protocol, transcript-to-rule table, negative-case analysis, expert read-back, disagreement process, coverage assessment, incident inventory, novice contrast, or evidence locator linking a released rule to testimony. The first author’s informal access may add valuable context, but it creates an undocumented second elicitation channel.

### Representation and architecture

The implementation separates knowledge by form (pp. 4–5):

1. executable Python functions for algorithmic or if–then rules;
2. system-prompt guidance for contextual visualization principles;
3. a request classifier that routes requests to predefined processing scripts;
4. RAG over code examples and technical manuals;
5. a prompt constructor that combines user requirements, analytical reports, retrieved material, and design guidance before code generation.

The paper’s most useful design insight is that representation should follow operational semantics: deterministic checks can execute outside the model, while contextual principles may guide generation. Yet the claimed binary between “explicit rules” and “tacit guidelines” is asserted after two interviews, not derived through a reproducible analysis. Nor are the classifier, prompts, rules, retrieval corpus, generated scripts, data, or evaluation materials released.

### Development and evaluation conditions

The proposed system bundles classifier routing, executable expert rules, expert-derived prompt guidance, RAG, and an unspecified LLM. The baseline is an unspecified LLM with RAG and code examples (pp. 5–7). The manuscript does not report model/provider/version, decoding settings, system prompts, retrieval settings, classifier implementation, generation count, retry policy, output-selection policy, or whether conditions received equal context and compute.

Five “representative” cases are reported from “numerous examples”: two battery scripts, one electric-motor script, and one control-arm script, spanning history, 2D-relation, and parallel/radial plots (pp. 6–8). The unit called cross-domain is physical simulation subject matter; all cases remain in one Siemens product, one post-processing workflow, one visualization library context, and the same physics-agnostic rule family.

A mechanical engineer with one year of simulation experience and limited visualization expertise received a 30-minute system orientation and prompted the system (p. 3). However, no within-person baseline task performance, unaided work, retention test, or transfer test is reported. The evaluation is therefore primarily of generated artifacts, not of non-expert capability.

Twelve technically diverse Siemens evaluators rated each condition’s five scripts. Only two are described as domain experts; others include managers, AI/software engineers, a data scientist, engineers, a computer scientist, and a business economist (pp. 7–8). Code validity is binary. “Code correctness” sums efficiency, documentation, exception handling, and cleanliness into a 0–4 score. Output quality is a 0–3 judgment of dimension selection, visual encoding, and decision-relevant highlighting (pp. 7–8). Claude 4.5 Sonnet supplied one additional score per scenario and condition.

## Evidence and what it licenses

### Reported results

Across the five cases, human mean output quality was 2.60 for the proposed package and 0.85 for baseline, reported as a 206% improvement. Proposed modes were 3 in every case; baseline modes were 0 in four of five. Per-case proposed versus baseline means were 2.75 vs 0.75, 2.00 vs 1.17, 2.75 vs 0.50, 3.00 vs 0.42, and 2.50 vs 1.42 (pp. 8–9). Both systems’ scripts were rated syntactically valid. Proposed code-correctness means exceeded baseline in four cases and tied in one (Tables 1–2, pp. 7–8).

The qualitative examples make the package effect credible. Baseline plots used catastrophic scales, excessive variables, poor encodings, and weak highlighting; proposed outputs visibly applied normalization, convergence line styles, filtering, and hierarchy rules (pp. 5–9). The strongest bounded claim is therefore: **on five disclosed and apparently rule-aligned cases, the augmented package produced artifacts that the same organization’s evaluators rated substantially higher than LLM+RAG.**

### Why “206%” is weaker than it looks

The percentage treats a bounded ordinal 0–3 rating as a ratio scale with a meaningful zero. A mean difference of 1.75 points is transparent; “206% improvement” suggests a ratio interpretation the rubric does not justify. The paper reports no paired effect estimate, confidence interval, hypothesis test, rater random effect, scenario uncertainty, or sensitivity to aggregation. Sixty ratings per condition are not 60 independent task replications: they are crossed observations from 12 raters on five selected artifacts.

No inter-rater agreement or reliability statistic is reported. Modes conceal disagreement: proposed Scenario 2 has mean 2.00, SD 1.21, and mode 3, while Scenario 5 has SD 1.00. The single Claude score per cell has no repeated-run uncertainty and cannot “triangulate” reliability. Agreement on code validity and some modal judgments does not validate an LLM judge, especially when its output-quality scores diverge materially from human means.

### Co-design and criterion overlap

The intervention and evaluation share content. Experts supplied normalization, convergence encoding, variable-selection, highlighting, and readability rules; output quality rewards effective dimension selection, encoding, and decision-relevant highlighting; scenarios explicitly request plot types where those rules apply. The paper even interprets unanimity in Scenario 4 as occurring when “codified rules align perfectly with scenario requirements” (p. 9).

This is not answer leakage in the narrow sense. It is a legitimate test of whether a package applies included procedures. But it makes the instrument **intervention-responsive by construction**. Without held-out experts, incidents, criteria, or domains, the result cannot distinguish reusable expert judgment from successful compliance with authored evaluator cues.

### No expert-equivalence comparison

The paper shows three qualitative “human result” plots, but does not report a sampled expert baseline scored under the same blinded rubric, under matched task inputs, time, tools, and selection policy. The final-visualization section says one 20-year visualization expert evaluated generated plots, while the 12-person tables assess code and output quality; it does not provide that expert’s complete ratings or a criterion for “expert-level.” A mode of 3 from a mixed-expertise panel is a top rubric category, not equivalence to expert work.

The 2D example explicitly says the proposed output was “less insightful than expert plots,” and the parallel-plot example lacks outlier detection (pp. 5–6). These observations directly bound the stronger abstract and conclusion language.

## Unique insight

The paper’s distinctive contribution is not its four-step loop, which is generic, but the collision between **representation choice and evaluation dependence**.

First, codified expertise has at least three execution types:

- **deterministic consequence:** convergence must be checked; scales can be tested; required variables can be counted;
- **contextual procedure:** select dimensions, grouping, hierarchy, and encodings in relation to an analytical goal;
- **open judgment:** decide which trade-off or outlier is consequential and whether the artifact is decision-ready.

The system operationalizes the first two but often claims the third. `skill-bench` should preserve those layers separately. A deterministic implementation can prove rule execution; a criterion score can show conformance; neither establishes that the agent recognizes when the rule is inappropriate or discovers an unanticipated insight.

Second, **expertise-transfer evidence needs an authorship-separation matrix**, not merely a skill/no-skill pair. In this case, overlapping people and content may influence elicitation, rules, scenario selection, implementation, examples, criteria, and evaluation. Each overlap is defensible for formative development, but together they make confirmatory claims circular. The remedy is not necessarily total personnel separation; it is explicit provenance plus held-out variation at several boundaries.

Third, “non-expert empowerment” is a separate estimand from artifact improvement. If the agent does all analytical work after a simple prompt, the evidence may support delegated package performance. To claim transferred capability, evaluate the person’s unsupported retention, ability to critique the agent, escalation decisions, or performance on new cases. `skill-bench` primarily evaluates configured agents, so it need not claim human learning—but it should not use that language accidentally.

Fourth, “physics-agnostic” is not “domain-general.” The five cases vary physical subject matter while holding product, workflow, artifact, rule family, organization, and evaluators mostly fixed. This is useful within-workflow scope transfer, not cross-domain expertise transfer.

## Limitations and validity threats

1. **Two experts, one organization, undocumented sampling.** Roles and one evaluator’s experience are described, but recruitment criteria, independence, disagreements, representativeness, and coverage are absent.
2. **No reproducible elicitation analysis.** No protocol appendix, transcripts, codebook, rule ledger, locators, read-back, saturation, contradiction, or excluded-rule record is released.
3. **Informal knowledge channel.** The employee-author’s internal discussions and proprietary sources supplement interviews without a traceable boundary.
4. **Bundled intervention.** Classifier, rules, prompt guidance, RAG interactions, and possibly prompt length all change together; no component ablation identifies codification effects.
5. **Under-specified configured systems.** Model identity, prompts, retrieval, decoding, retries, budgets, and output selection are missing.
6. **Selected cases.** Five “representative” examples are reported from a larger undisclosed pool, with no sampling frame or inclusion rule.
7. **Single artifact per condition/case.** Generation variance and cherry-picking cannot be assessed.
8. **Criterion–intervention overlap.** Rules, scenarios, and scoring criteria reward closely related observable features.
9. **No independent expert comparator.** Top mixed-panel ratings are treated as expert-level without a matched expert distribution or equivalence margin.
10. **Evaluator heterogeneity.** Twelve raters have widely different expertise; no eligibility-by-criterion mapping or subgroup results are reported.
11. **No reliability or inferential analysis.** There is no agreement statistic, paired model, clustered uncertainty, or multiplicity treatment.
12. **Ordinal ratio misuse.** The 206% headline divides means on a 0–3 ordinal scale.
13. **AI-judge overclaim.** One Claude judgment per cell cannot establish reliability as a regression proxy.
14. **Non-expert claim not tested.** One user prompted the agent after orientation; unaided capability, learning, oversight, and retention were not measured.
15. **Narrow “cross-domain” range.** Three physics areas share one product and workflow; medical, financial, and non-simulation transfer is acknowledged as unvalidated.
16. **Safety and reliability dismissed rather than tested.** The paper excludes security and reliability because scripts are for visualization and single use, although generated code executes on proprietary engineering data and misleading plots can affect decisions.
17. **Proprietary evidence.** Product-team results, data, and technical materials are unavailable.
18. **Internal role overlap.** At least one expert both supplies standards and evaluates outputs; author/company involvement raises allegiance risk that is not analyzed.
19. **Contradictory result wording.** Section 6.2.5 says systems had equivalent code validity and correctness, while the tables show materially higher proposed correctness means in four of five scenarios.
20. **No operational outcome.** Reduced expert time, user productivity, decision quality, failure cost, adoption, and maintenance burden are asserted but not measured.

## Reproducibility and operational realism

Manuscript-level reproducibility is good: the immutable 11-page v1 PDF and full extraction are retained with hashes, and the five score tables and examples are inspectable. Experimental reproducibility is poor. No code repository, frozen prompts, model configuration, rule set, classifier, retrieval corpus, data, generated scripts, raw ratings, rater assignments, or analysis code is linked. A team could imitate the architecture but could not reproduce the reported comparison.

Operational realism is mixed. The work occurs inside an actual engineering-software company, uses proprietary simulation data and internal experts, and reveals a genuine expert-availability bottleneck. Yet the evaluation consists of selected static artifacts, not longitudinal use: there is no real user task completion, iteration, correction, abstention, escalation, maintenance, latency, cost, deployment monitoring, or consequence measurement. The architecture is industrial; the evidence remains a formative case demonstration.

## Transferable design requirements for skill-bench

### 1. Type codified knowledge by execution semantics

For each expert primitive, record:

```yaml
representation_semantics: deterministic_rule | contextual_procedure | open_judgment
implementation_locus: external_code | prompt | retrieval | classifier | model_reasoning
applicability_conditions: [...]
counterexamples_or_exceptions: [...]
expert_evidence_locators: [...]
transformation_review: approved | disputed | unreviewed
observable_consequence: ...
claim_ceiling: execution | criterion_conformance | contextual_transfer | professional_readiness
```

This refines existing expertise-transfer and procedural-skill records; it does not require a new contract.

### 2. Add an authorship-separation matrix to validity arguments

For every efficacy claim, disclose overlap across `expert_source`, `elicitor`, `primitive_coder`, `skill_author`, `task_author`, `reference_author`, `criterion_author`, `grader_author`, `scenario_selector`, and `evaluator`. For overlapping roles, add at least one held-out boundary and state the remaining claim ceiling.

### 3. Use a factorial evidence ladder

A defensible follow-up would separate:

1. LLM only;
2. LLM + identical RAG;
3. + deterministic rules;
4. + contextual expert guidance;
5. + classifier/routing;
6. full package.

Run repeated generations on preregistered development and held-out incidents. Hold model, harness, retrieval corpus, prompt budget, retries, and output-selection policy fixed where the construct permits. Report paired task-level effects and rater-aware uncertainty, not percentages of ordinal means.

### 4. Distinguish four transfer claims

- **Rule execution:** observable rule consequence appears.
- **Package efficacy:** the configured package improves artifacts on sampled tasks.
- **Contextual transfer:** improvement persists on held-out incidents not authored around the rule examples.
- **Professional equivalence/readiness:** performance is equivalent to qualified experts under matched conditions and decision thresholds.

The paper supplies evidence for the first two only.

### 5. Build independent expert anchors

Use experts who did not author the skill to create held-out incidents, counterexamples, and artifacts. Blind qualified raters to condition. Score expert and agent artifacts under the same criterion versions, preserve criterion-specific authority, estimate agreement, and predefine an equivalence or readiness margin. Include cases where blindly following a codified rule should fail.

### 6. Keep human learning separate

If a pilot claims that non-experts gain expertise, add unaided pre/post equivalent forms, delayed retention, critique/error-detection tasks, and escalation decisions. If the construct is configured-agent performance, call it delegation or access rather than human expertise transfer.

## Relation to existing evidence

- **ACTA/CDM:** provides richer critical-incident, cue, novice-contrast, and verification procedures than this paper’s direct-rule interviews. This case shows a deployment-oriented representation split but does not replace evidence-typed elicitation.
- **Data Therapist:** demonstrates that the elicitation interface changes testimony and that volume is not fidelity. This paper likewise treats directly articulated rules as high-fidelity without testing omissions or prompt effects.
- **SkillsBench:** supplies a stronger matched skill/no-skill multi-configuration design, while warning that skill-responsive task admission and task–skill–verifier co-design bound the estimand. This industrial case has an even tighter co-design loop and far fewer tasks.
- **LH-Bench:** connects expert procedure, artifacts, rubrics, and recovery. The current paper offers no independent public/private rubric boundary, trace, or recovery analysis.
- **Expert-participation contract:** approval should not automatically propagate from interview statements to Python functions, prompts, scenarios, or claims. The paper reports consent to recording but not contribution-use, attribution, ownership, withdrawal, or transformation approval.

## Action items

- [x] Read and verify the complete immutable v1 PDF/text and preserve local paths/hashes.
- [x] Reconstruct elicitation, representation, architecture, conditions, measures, evidence, and limitations with page evidence.
- [x] Separate the demonstrated package effect from tacit capture, non-expert learning, expert equivalence, and cross-domain transfer claims.
- [x] Map nonduplicate implications to existing contracts and reviews.
- [ ] Apply the representation-semantics and authorship-separation fields during the next real expertise-transfer pilot revision; no new queue task is needed because current contracts can represent them.
- [ ] Require future pilot analyses to report held-out incidents, repeated generations, qualified-rater reliability, paired uncertainty, and bounded claim levels before using “expert-level.”
