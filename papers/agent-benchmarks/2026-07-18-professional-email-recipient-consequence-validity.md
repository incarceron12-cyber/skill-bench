# Professional-email field experiment: randomized rewriting changed a sentiment proxy, not recipient engagement

## Source and review status

**Deep review of the complete immutable primary source and pinned official analysis release.** I read the full 18-page arXiv v1 paper, including methods, references, and treatment-compliance appendix, and audited every substantive file in the complete four-file official repository snapshot. The arXiv metadata contains no withdrawal or retraction notice.

- **Paper:** Ziv Ben-Zion and Teddy Lazebnik, *Playful AI in Professional Email: A Field Experiment on Tone and Recipient Engagement*, arXiv:2607.11749v1 (13 July 2026), <https://arxiv.org/abs/2607.11749v1>
- **Local PDF:** `data/papers/pdfs/2607.11749v1-professional-email.pdf` (18 pages; SHA-256 `6a2a592200c99c96155b2a2bce6082f51a6949e626aecc72bc2a097180a0dc06`)
- **Full local text:** `data/papers/text/2607.11749v1-professional-email.txt` (40,796 bytes; SHA-256 `3ae11402908042a7003513febd4099a60cd8554cfc5cb1c2c280aa224a82def5`)
- **Metadata:** `data/papers/source/2607.11749v1-metadata.xml` (SHA-256 `15b009570a9f4b14492fc666e086ca4d5db186ec0b6ac8867582678eb36def98`)
- **Official release:** <https://github.com/zivbz1/Playful-AI-in-Professional-Email>, pinned at commit `e42fae22fdee831f0d47fd6deab7cfefee5cd0bb` (12 July 2026), tree `ae3e4565bba549e97fd1b318d56084cbb1e8a348`
- **Release provenance:** `data/sources/releases/2607.11749v1-professional-email/provenance.json`; complete archive SHA-256 `4cc8014e191de9ea440d0bc7c143951ee6ade8e327c60f66e589a2e114fdf711`

The release contains only `.gitignore`, `README.md`, `analysis_pipeline.R`, and `analysis_verification.py`. The README says the de-identified 16,880-row email-level table is request-only and no raw email text, names, or addresses are released. Consequently, neither the manuscript results nor paper–code numerical conformance can be publicly replayed. The code audit below concerns the declared estimators and data contract, not independently reproduced findings.

## One-sentence contribution

The paper reports a rare sender-level randomized three-period workplace intervention over 16,880 real emails and directly joins assigned rewriting, a final-message sentiment proxy, and recipient events, but the only randomized outcome supported by its reported analysis is a shift in that proxy: no assigned condition changed opening, replying, or response time, while the claimed behavioral mediation is an exploratory, confounded within-sender association estimated with a model that omits period, sequence, recipient, and company dependence.

## Why this matters for skill-bench

This review advances charter objectives A, B, and E through a bounded field-validity case. Email is not a proposed benchmark domain. The reusable question is:

> When an agent changes a professional artifact and downstream stakeholder telemetry is available, what evidence licenses the transitions from assigned intervention to realized artifact delta, recipient exposure, behavior, utility, value, capability, and readiness?

The paper gets closer to real consequence than an artifact-only rubric: ordinary messages were sent in six companies, and opens and replies were observed. Its negative randomized result is especially valuable. A demonstrable artifact-property shift is not automatically a stakeholder effect, and a stakeholder event is not automatically useful work. The case therefore adds a concrete stop rule to the repository's consequence ladder:

```text
assigned rewriting policy
→ rewriting opportunity and realized adoption
→ source-faithful artifact delta
→ recipient delivery and valid exposure observation
→ recipient behavior
→ communication objective attainment
→ workflow/productivity/stakeholder value
→ transportable configured-system capability or readiness
```

No arrow inherits the next. The paper reports the first arrow only at sender-week assignment level, observes a sentiment-score difference on final messages, and reports null intent-to-treat effects on recipient behavior. It does not observe whether every draft was submitted, whether the rewrite was accepted unchanged, whether meaning was preserved, whether the intended recipient actually opened the message, whether a reply was responsive or useful, or whether work improved.

This is nonduplicate relative to existing evidence. AlphaEval studies production-demand-to-task projection; Nubank reports an adaptive offline-to-live deployment loop; the criterion-validity paper studies retrospective score–outcome association; Chiron reports retrospective workflow tables. This source uniquely combines randomized field assignment with a real artifact and recipient telemetry—but then illustrates why randomizing the upstream intervention does not automatically randomize an observed mediator or validate its downstream meaning.

## Methodology and system

### Design, sample, and assignment

The authors enrolled 121 volunteers from six companies in software, hardware, IT services, and medical devices across Israel, the United Kingdom, Sweden, and Ukraine. Company contributions ranged from 7 to 38 participants. Participants sent ordinary work email without a quota; the final table contains 16,880 messages: 5,633 unaided, 5,595 professional-rewrite, and 5,652 playful-rewrite messages, of which 41.4% were internal (paper pp. 3–4, 10–11, 17; extraction lines 88–115, 289–317, 541–569).

Every sender received one condition per week for three weeks. Six possible condition orders were assigned within each company to demographically similar subgroups. This is a sensible crossover skeleton: each sender can serve as a control, and counterbalancing can reduce systematic period/order imbalance (p. 10; lines 289–298).

However, the manuscript does not report the randomization algorithm, allocation concealment, sequence counts by company, subgroup sizes, seed, assignment table, baseline comparability by sequence, recruitment denominator, attrition, exclusions before the 121 completers, or a CONSORT-style flow. “Randomized” is therefore manuscript-reported rather than release-auditable. More importantly, counterbalancing is not analysis. The reported models do not include week/period, assigned sequence, prior-week treatment, treatment-by-period, or carryover. The repository's expected CSV columns do not even include sequence or crossover week, despite the Methods saying week was retained (paper p. 12; lines 378–388; release `README.md` lines 18–22). A three-week design cannot support the claim that period and carryover were controlled merely because six orders were intended to be balanced.

Assignment occurs at the **sender-week** level, while the analysis row is an email. The treatment has at most 363 sender-period assignments, not 16,880 independently randomized units. A sender random intercept accounts for one form of within-sender outcome dependence; it does not make thousands of messages independent treatment assignments or model heterogeneous sender treatment effects. No random treatment slope, sender-period cluster, small-cluster correction, sequence-level analysis, company-level sensitivity, or sender-level aggregate analysis is reported.

### Intervention and realized artifact

In the unaided week, senders wrote normally. In active weeks, they drafted first and then used GPT-5 with fixed prompts. The professional prompt asks for formal, concise rewriting while preserving meaning, facts, names, dates, deadlines, and actions. The playful prompt substitutes a specified style such as pirate, medieval, or theatrical voice while also demanding exact semantic preservation and workplace suitability (pp. 11–12; lines 319–344).

This is a **configured writing-package treatment**, not a general agent-capability test. The paper names “GPT-5 via the public API at default temperature” but gives no endpoint snapshot, API date, system message, seed, sampling parameters, retry/error policy, safety behavior, style allocation, client interface, or immutable model output. The repository does not archive a separate model configuration despite the manuscript saying the exact configuration is archived. The prompts are present only as manuscript text.

The claim that conditions differ “only” in tone is not established. A randomly selected active-arm subset was checked by one researcher for content preservation, tone, offensive content, and length within ±30 words, but neither subset size, sampling method, source/final pairs, criterion definitions, failure counts, correction policy, rater blinding, nor agreement is given (p. 12; lines 339–344). No draft identifier, rewrite identifier, adoption/edit event, source/final semantic comparison, or send-time realization appears in the released data contract. Thus assignment, LLM invocation, generated candidate, user acceptance, user modification, and final send are collapsed.

That collapse matters for both interpretation and benchmark design. A final-message positivity difference can arise from model rewriting, sender selection/editing, topic mix across weeks, recipient mix, or all of them. It is evidence about the realized condition package, not an intrinsic “tone-only” transformation or autonomous artifact correctness.

### Outcomes and observer validity

The three recipient behaviors are binary open, binary reply, and elapsed time to first open/reply. Opens are inferred from the first retrieval of a tracking pixel; replies come from sender email-system logs (p. 12; lines 346–355). These are operational events, but the paper does not validate either observer:

- tracking pixels can be blocked, prefetched, proxied, cached, or retrieved by security/privacy infrastructure rather than the intended human;
- a reply receipt establishes a message in a thread, not that the recipient read, understood, accepted, or productively acted on the focal email;
- recipient identity, repeated sender–recipient dyads, distribution lists, forwarding, automated replies, bots, thread state, subject, urgency, requested action, and send time are absent from the public contract;
- recipients can contribute many correlated outcomes and may receive messages from multiple enrolled senders, but no recipient or dyad random effect is possible with the declared columns.

The positivity mediator is `spacytextblob` polarity on the final full message, ranging from −1 to +1 (p. 12; lines 356–360). No human validation is reported for workplace email, multilingual content, playful styles, signatures, quoted threads, jargon, irony, or the distinction among positivity, humor, warmth, professionalism, authenticity, appropriateness, and content. The experimental prompts intentionally produce theatrical lexical cues likely to move a generic sentiment model. This validates a manipulation of **one configured text score**, not the latent emotional tone perceived by recipients.

The paper reports mean positivity of 0.072 unaided, 0.028 professional, and 0.136 playful, with adjusted active-versus-unaided coefficients of −0.041 and +0.068 (pp. 4–5; lines 97–130). Those shifts are credible as reported model outputs. Their substantive scale is uncalibrated: no minimally important difference, human-perception mapping, classification error, or relation to communication appropriateness is supplied.

### Direct randomized effects

The primary hypotheses concern condition effects on opening, replying, and response speed. The paper reports no omnibus condition effect:

- open: `χ²(2)=0.94`, `p=.62`;
- reply: `χ²(2)=2.34`, `p=.31`;
- time to open: `χ²(2)=1.69`, `p=.43`;
- time to reply: `χ²(2)=2.83`, `p=.24`.

Descriptively, rates are nearly identical: 57.0/22.2% unaided, 58.0/21.5% professional, and 57.7/22.2% playful for open/reply (pp. 4–6; lines 97–153). This is the paper's strongest behavioral finding: under its analysis, assigned rewriting did not detectably change the measured recipient events.

A null hypothesis test is not proof of equivalence. The paper gives no effect estimates and confidence intervals for all pairwise binary contrasts, equivalence margins, detectable-effect calculation, preregistration, or cluster-aware power analysis. It therefore supports “no detected effect under this instrument,” not “behavioral equivalence” or “the LLM was neither a bonus nor a penalty.”

The primary GLMMs include condition and sender random intercept only. They omit period/sequence/carryover, company, recipient type, sender–recipient dependence, message covariates, and treatment-by-company or treatment-by-period heterogeneity. The methods call the hierarchy emails-within-employees-within-companies but do not model company in the primary outcomes (p. 12; lines 378–404; R lines 101–117). Six companies are too few for casual generalization and require transparent cluster sensitivity rather than silent omission.

The time-to-event implementation has a sharper reproducibility defect. The paper says right-censoring is at 14 days for opens and 40 days for replies, corresponding to observed follow-up extremes. The R and Python scripts assign those fixed durations only when `opened/replied == 0`; an observed event keeps its recorded time even if it exceeds the nominal cutoff. They also assign every non-event the full fixed horizon regardless of message send date or actual observation end (R lines 34–49; Python lines 42–74). Unless every email has complete post-send follow-up of exactly those lengths, this creates unreported observation time. A 40-day reply window also extends beyond the three-week intervention itself. The release has no delivery date or administrative end column with which to verify censoring, delayed events, period overlap, or carryover.

### Exploratory mediator analysis

The paper centers each email's positivity by its sender's mean and fits opening/reply GLMMs with centered positivity and condition. It reports pooled odds ratios of 2.05 for open and 3.32 for reply per full one-unit positivity increase. It multiplies the condition→positivity coefficient by the positivity→behavior log-odds coefficient and applies a Sobel/delta-method test, yielding four nominally significant indirect products (pp. 6–7, 13; lines 158–205, 405–413).

This is not a valid basis for the repeated claims that tone “determined,” “shaped,” “influenced,” or was the “operative channel” for recipient behavior. The paper itself acknowledges that positivity was measured rather than independently manipulated and that topic, length, and specificity can confound it (p. 9; lines 267–277). The deeper problems are:

1. **Random treatment does not randomize the mediator.** Message content, urgency, recipient relationship, thread state, requested action, send time, week, and user editing can jointly affect final polarity and response. Sender centering removes stable sender means, not time-varying email confounding.
2. **The mediator observer is not validated.** The coefficient concerns a `spacytextblob` score, not recipient-perceived playfulness, warmth, or positivity.
3. **The pooled coefficient is composition-sensitive.** The paper notes pooled reply OR 3.32 falls to about 1.59/1.60 after internal/external stratification because internal messages are both warmer and more engaged (pp. 6–7; lines 169–180). Yet positivity was centered globally within sender, not within sender-by-recipient-context, leaving contextual composition in the purported within-sender mediator.
4. **Dependence is incomplete.** The a- and b-paths use the same clustered emails, but the product standard error treats the coefficients through a simple delta formula without their covariance, sender-period randomization, recipient clustering, or cluster bootstrap.
5. **Mixed-model mediation is nonlinear.** Multiplying an LMM mean difference by a subject-specific logistic coefficient does not directly yield a mediated probability effect. No counterfactual estimand, sequential-ignorability assumptions, natural/interventional effect, sensitivity analysis, or probability-scale effect is defined.
6. **The total effects are null and the adjusted direct effect barely moves.** The manuscript reports playful open OR changing 1.039→0.990 and reply OR 1.000→0.925 after adding positivity (p. 7; lines 191–196). That pattern can be compatible with inconsistent pathways, confounding, scale changes, or noise; it does not prove a behavioral effect that was “too small to surface.”
7. **The analysis was explicitly secondary, exploratory, and not preregistered.** Holm correction covers selected pairwise condition contrasts, not the full family of primary outcomes, interactions, stratified associations, quartiles, b-paths, and four mediation tests.

The defensible statement is narrower: assigned rewriting shifted a configured sentiment score, and that score was strongly associated with measured engagement within the fitted sender-intercept models. The causal effect of sentiment, the existence and magnitude of an indirect behavioral effect, and the mechanism remain unresolved.

### Compliance analysis

The appendix labels emails compliant when a separate LLM-writing detector is ≥.50 in active arms and <.50 unaided. It reports 100% compliance in both active arms but excludes 34.6% of unaided messages, leaving 14,931 rows; direct nulls and mediator associations remain similar (pp. 16–18; lines 521–615).

This does not strengthen treatment fidelity. No validation, calibration, error rates, language/domain transport, or independence from sentiment/style are shown for the detector. Calling every active email compliant while labeling more than one-third of ordinary workplace emails LLM-edited is at least as consistent with a detector/style artifact as with widespread control-arm contamination. The per-protocol restriction conditions on a post-assignment classifier that may be affected by message features related to outcomes and asymmetrically removes only control rows. It cannot estimate a complier effect and does not observe invocation, generated text, acceptance, or final user edits. The intent-to-treat analysis should remain primary; the detector result is an observer-validity warning, not confirmation.

## Evidence and claim ceiling

### What the full source supports

1. The authors report a three-period, six-sequence crossover assignment among 121 completing volunteers in six companies.
2. The study joins sender condition, final-message derived variables, and open/reply telemetry for 16,880 naturally occurring email rows.
3. Under a sender-intercept LMM, active conditions shift the configured sentiment-polarity score in opposite directions.
4. Under the reported sender-intercept GLMM and sender-stratified Cox analyses, no assigned condition has a detected direct effect on open, reply, or response-time outcomes.
5. Final-message positivity is strongly associated with open/reply outcomes under the reported exploratory models.
6. The released R and Python code makes the intended estimators and several manuscript–implementation boundaries inspectable.

### What it does not support

- causal effect of positivity, playfulness, professionalism, or perceived tone on recipient behavior;
- a valid mediated behavioral effect of LLM rewriting;
- semantic preservation, artifact correctness, or safe/appropriate rewriting;
- recipient understanding, useful reply, task completion, communication quality, reduced work, productivity, organizational value, or stakeholder welfare;
- equivalence of rewriting conditions on recipient behavior;
- model, prompt, scaffold, or autonomous-agent capability;
- transport across models, organizations, cultures, languages, channels, recipient relationships, or disclosure regimes;
- professional quality, human equivalence, deployment fitness, or readiness.

## Unique insight

The paper's unique value for `skill-bench` is not that tone mediates engagement; v1 does not establish that. It is the empirical separation of three tempting but non-equivalent observations:

1. a randomized package can reliably move an artifact proxy;
2. that proxy can strongly co-vary with a stakeholder event; and
3. the randomized package can still have no detected effect on the stakeholder event.

This triangulation is a practical falsification pattern for benchmark claims. If an intervention changes a rubric score but not an independently observed downstream consequence, the project must not rescue the intervention by treating score–outcome association as mediation. It should test observer validity, intervention adoption, mediator confounding, treatment contrast strength, opposing pathways, and outcome adequacy. Conversely, a null endpoint does not prove the artifact metric useless: it bounds the specific treatment, population, exposure, follow-up, and endpoint. The right object is a typed **intervention–artifact–recipient–consequence chain**, not a single “quality” score.

A second insight concerns recipient-relative validity. Artifact correctness cannot be fully inferred from the sender's file or a generic model judge when the work is communicative. Yet recipient telemetry is itself not ground truth. Opens, replies, acceptance, comprehension, decision change, burden, and legitimate value are different observations with different affected parties and failure modes. `skill-bench` should preserve this plurality rather than replacing artifact-only grading with a simplistic engagement metric.

## Limitations and reproducibility / operational realism

The field setting is a genuine strength: real employees, ordinary work, live recipients, no imposed email quota, and in-company processing are more operationally realistic than synthetic correspondence. The crossover also provides a credible route to within-sender contrasts. Those strengths are bounded by missing realization and governance evidence:

- recruitment is voluntary via management-distributed announcements, and only completers are described;
- recipient/dyad identity, message purpose, language, thread, urgency, send time, and organization policy are absent;
- participants were partially deceived and asked not to discuss the study, while recipient awareness and consent for tracking pixels are not discussed;
- the ethics statement covers participant consent but does not explain correspondent notice, lawful basis, company authorization, opt-out, tracking-pixel risks, data retention, incident response, or whether recipients in multiple jurisdictions were research subjects;
- only aggregated de-identified variables left company systems, which is privacy-preserving but prevents independent semantic, observer, and transformation audits;
- no raw messages, derived dataset, assignment table, codebook, environment lockfile, session info, package versions, model outputs, prompt/config artifact, or expected result files are public;
- the release claims the R script reproduces every number, but absent data this is not testable; the Python “independent verification” deliberately uses population-averaged GEE rather than the manuscript's subject-specific GLMM and therefore is a model sensitivity implementation, not an exact independent reproduction;
- the Python header names an output path inconsistent with the actual code/README, a minor sign that release conformance was not tested as a packaged artifact;
- neither script performs schema validation, assignment-balance checks, duplicate checks, missingness reporting, plausible-range checks, recipient dependence checks, proportional-hazards diagnostics, period/carryover tests, or outcome-window validation.

The study was not preregistered. Primary direct outcomes are clearly distinguished from exploratory mediation, which is commendable, but no protocol, analysis plan, sample-size rationale, or declared multiplicity family exists. Reported `p<.001` values on thousands of email rows should not be mistaken for strong causal evidence when the effective assignment units, observer validity, and mediator assumptions are weak.

## Transferable design implications

### 1. Preserve treatment realization separately from artifact state

For any guidance/Skill/agent intervention, record assignment, opportunity, invocation, generated candidate, human adoption/rejection/edit, final artifact hash, and send/use event. A final-score difference cannot identify which step realized the treatment.

### 2. Bind recipient events to explicit observer contracts

A recipient-side check needs event source, actor/dyad identity policy, false-positive/false-negative risks, observation window, censoring clock, automation/proxy handling, repeated-event policy, and evidence-view restrictions. `opened`, `replied`, `accepted`, `understood`, `acted`, and `benefited` must not share a generic success field.

### 3. Model the randomization unit and dependence graph

Trials should preserve assignment unit, analysis unit, sender/recipient/company/task clusters, period, sequence, carryover, and treatment-exposure windows. Large event counts do not replace independent assignments. Crossover balance must be tested and modeled, not merely asserted at authoring time.

### 4. Treat artifact proxies as configured observers

Sentiment, style, readability, aesthetics, and model-judge scores require versioned implementation, evidence view, domain/language calibration, human/consequence validation, and known invariances. A proxy deliberately targeted by the intervention is especially vulnerable to criterion gaming and cannot become the mediator construct by name alone.

### 5. Require a mediation claim contract

A mediation claim should declare treatment, mediator, endpoint, causal graph, mediator/outcome timing, confounders, interference, estimator scale, covariance/cluster treatment, sensitivity analysis, and whether the mediator was randomized. A product of two significant coefficients is insufficient.

### 6. Keep communication utility plural and affected-party aware

Pair artifact fidelity and safety with recipient comprehension, appropriate response, objective completion, delay, burden, trust/authenticity, disclosure, collateral effects, and sender/recipient preference. Engagement can be useful, neutral, manipulative, or harmful depending on objective and authority.

## Concrete repository actions

1. **No new email-specific schema, benchmark, or pilot.** Existing benchmark-bundle component identity, artifact-view/admissibility, trace, metric-monitoring, participation, task-health, and validity-argument records already have the right homes. The next consolidation pass should use this review to sharpen randomization-unit/analysis-unit, treatment-realization, observer-window, and mediator-claim guidance rather than create a parallel subsystem.
2. **Add this source to the human-facing indices as a Tier A validity case.** Its rare combination of upstream randomization and downstream null behavior directly tests the score-to-consequence boundary, while the mechanism claim remains weak.
3. **For a future cross-domain recipient-consequence validation—not an email pilot—require a predeclared chain:** immutable source artifact and candidate transformation; realized adoption; recipient-relative observer contract; assignment/cluster/censoring plan; artifact delta; independent endpoint; adverse/burden measures; and a validity argument whose claim ceiling remains at the weakest audited link.

No new queue task follows. The implications refine existing machinery and the repository already has consolidation routes for criterion/outcome, production, configured-system, participation, metric, and validity boundaries.
