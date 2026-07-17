# Paper Review: YIELD Learns Interviewer-Like Next Turns, Not Validated Information Acquisition

- **Paper:** Victor De Lima and Grace Hui Yang, *YIELD: A Large-Scale Dataset and Evaluation Framework for Information Elicitation Agents*, https://arxiv.org/abs/2604.10968v1
- **Date read:** 2026-07-17
- **Venue / source:** immutable 14-page arXiv v1 manuscript
- **Tags:** expertise-elicitation, dialogue-corpus, offline-RL, proxy-reward, human-evaluation, licensing, split-lineage, release-audit
- **Local PDF:** `data/papers/pdfs/2604.10968v1-yield-information-elicitation-agents.pdf` (14 pages; SHA-256 `ecb1b0fd584c88e255d83e0037003c8fc1abcb7965ca101e273750bbc89c4f94`)
- **Local text:** `data/papers/text/2604.10968v1-yield-information-elicitation-agents.txt` (SHA-256 `8433efe4e08542d863b07b6ea66178dda4371f936729badc58148cd8b2cba829`)
- **Official release inspected:** code commit `896cdd096f51ed2b1d12f003fedaf779e4d3b0df`; dataset revision `09d80908316b9d21ab2f42d5218ed410cebc2d23`; adapter revision `1eb18cfb7a94b59249cbcfb9a2eb14a22101c893`; PyPI `elicitation==1.0.1`. Complete paths, hashes, sizes, and post-v1 timing boundaries are in `data/sources/releases/2604.10968v1-yield/provenance.json`.

## Verdict

YIELD is a substantial, unusually inspectable corpus of 2,281 long, public human-to-human transcripts and a useful demonstration that LoRA adaptation can make three open models imitate the short next-turn distribution of corpus elicitors. It contributes a clean conceptual warning for agent evaluation: an elicitor serves an external objective and should be evaluated differently from a reactive assistant.

The study does **not** establish that its models acquire more useful information, pursue a specified institutional objective, elicit tacit expertise, conduct valid interviews, or are ready for interaction with people. Evaluation removes the final elicitor turn from a fixed six-turn window and generates one replacement; no model question receives a respondent answer. Perplexity measures reference imitation, Progression measures embedding distance, and turn-length ratio measures corpus asymmetry. The offline-RL reward is the count of previously unseen spaCy named entities in the *recorded human response after the recorded human question*, not factuality, relevance, novelty to an institutional decision, or information caused by the learned policy.

Release inspection tightens that ceiling. Dialogue-level splits prevent exact dialogue overlap, but the unsown split is only stratified by four broad domains and shares many elicitor/respondent identities and collections across train/test. Overlapping windows create up to 429 test examples from one dialogue, so 10,285 test blocks are not independent trials. The released ORL implementation also indexes the critic hidden state incorrectly: it uses `valid_mask.sum()-1` as an absolute sequence position even though target labels occur after a masked context. The value head therefore generally reads an early context position rather than the stated end-of-action state. Paper-level ORL competitiveness cannot be treated as a clean test of dialogue-level optimization.

Most importantly, “ethically sourced” is not established by public availability and copyright status. The paper reports no participant-consent, original study-use, reidentification, sensitive-content, withdrawal, or affected-person review. Speaker identities are deliberately preserved. The paper and dataset card label the aggregate release CC BY 4.0 while Appendix Table A.1 and release documentation identify Oyez as CC BY-NC 4.0. That unresolved license boundary alone makes blanket redistribution/use claims unsafe.

For `skill-bench`, retain YIELD's separation of external objective, interaction policy, respondent observation, and stopping—but repair the evaluand. A useful elicitation benchmark must observe the causal chain from question opportunity through answer, grounded claim adoption, objective-relevant update, burden/harm, and stopping. Human-style next-turn prediction is a candidate policy prior, not expertise transfer or elicitation success.

## One-sentence contribution

YIELD releases 26.2M tokens of long public interview/proceeding transcripts, six SFT/ORL adapters, and conformity/progression/turn-ratio tools, showing strong corpus-style adaptation on fixed next-turn contexts while leaving information gain, institutional utility, consent, interactive validity, and professional transport unmeasured.

## Why this matters for skill-bench

This review advances charter objectives A, B, E, and F through targeted expansion on the measurement boundary between **asking an interviewer-like question** and **acquiring decision-useful expertise**. Interviewing is a methodological case, not a scope commitment.

YIELD complements nearby reviews without duplicating them:

- **Data Therapist** exposes model-selected questions to six real experts but lacks downstream truth validation. YIELD provides a much larger real-dialogue corpus, but no new respondent interaction and no expert-claim validation.
- **SimInstruct** shows that a simulated interlocutor changes expert production. YIELD avoids a simulated respondent during training, but its evaluation freezes the human context and never observes a response to the generated question.
- **Organizational tacit-knowledge simulation** makes planted claim reachability inspectable but has no real experts. YIELD has real historical speakers but no planted/validated claim inventory, source authority, or question-to-answer causal evidence.
- **ACTA/CDM** supplies probes for cues, thresholds, incidents, and expert/novice contrasts. YIELD's corpus was not collected or annotated for those primitives.
- The blocked **consented elicitation-session contract** remains correctly blocked. Public archival transcripts cannot validate a new contribution workflow, read-back, current consent, or downstream benchmark projection.

Useful completion is a bounded claim ceiling and cross-domain retain/repair/test guidance. No interview-specific schema or duplicate build task is justified.

## Contribution and research question

The paper asks how to define, train, and evaluate “Information Elicitation Agents” (IEAs): conversational agents that actively obtain information for an institutional or task objective rather than primarily respond to a user's agenda (Abstract and Section 1, pp. 1–2). It contributes:

1. a conceptual IEA distinction based on initiative, beneficiary/objective, and information extraction;
2. YIELD, 2,281 English dialogues / 390,205 turns / 26,249,014 tokens across academic interviews, journalistic investigations, judicial proceedings, and oral history;
3. full-dialogue and six-turn rolling-window forms with dialogue-level train/dev/test splits;
4. a finite-horizon POMDP interpretation and an AWR-style offline adaptation procedure;
5. conformity, Progression, and turn-length-ratio metrics;
6. prompt-only, SFT, and ORL comparisons over three model families; and
7. a 100-context, three-worker Mechanical Turk evaluation.

The evidence supports corpus, release, and configured next-turn statements. Fine-tuned models assign much higher likelihood to held-out human elicitor turns than prompt-only bases, generate shorter utterances, and resemble corpus progression/turn asymmetry. It does not support claims of increased acquired information, objective attainment, calibrated question choice, expert/tacit elicitation, respondent welfare, professional interview quality, deployment readiness, or cross-domain transport.

## Methodology and system

### Corpus sources, people, and authority

The four domain labels conceal materially different interaction regimes (Section 3 and Appendix A.1, pp. 3, 11–12):

- 621 Oyez Supreme Court oral arguments;
- 1,383 oral histories, dominated by 1,012 NASA/JSC and 270 JFK records;
- 148 academic interviews from multiple research collections; and
- 129 journalistic interviews from VOA and Wikinews.

These are not four samples from one stable elicitation construct. A justice testing counsel's legal position, an oral historian preserving memory, a qualitative researcher following a study protocol, and a journalist questioning a public official differ in authority, neutrality, disclosure expectations, respondent incentives, evidentiary standards, stopping rules, and consequences. The base prompt contains only the broad domain. No interview protocol, case issue, research question, missing-claim inventory, institutional decision, participant relationship, or allowed-question policy is represented.

The corpus preserves names/identifiers and multiple speakers per role, but implementation collapses all speakers into `elicitor` and `respondent` (Section 3.3, p. 4). This erases turn-level authority and role distinctions—for example, which justice, advocate, interviewer, interpreter, or co-respondent spoke—while leaving identity/style cues in text and metadata.

The authors say sources were chosen for public-domain or Creative Commons status and call the release “ethically sourced” (Sections 1, 3.1, and Ethical Considerations, pp. 2–3, 10). Copyright permission does not establish participant consent for model training, current disclosure expectations, sensitivity, representational harm, or permission to build proactive institutional agents. The paper reports no collection-by-collection consent audit. Some academic records concern health workers, vaccination, food choice, organizational change, and COVID thresholds. Public archives may legitimately publish them while downstream model-training governance remains a separate question.

There is also an unresolved license contradiction. The paper says “We release YIELD under CC BY 4.0” (Abstract, p. 1), and the Hugging Face card declares `license: cc-by-4.0`; Appendix Table A.1 and `docs/data_sources.md` classify Oyez as CC BY-NC 4.0. A derivative collection cannot simply remove an upstream noncommercial condition. NASA/JSC is described as a government source but is absent from the paper's licensing table. This review does not make a legal determination; it records that the release does not provide a collection-level rights manifest sufficient to justify the aggregate license.

### Acquisition, annotation, and standardization

The paper reports weeks of manual correction: text extraction, removal of extraneous material, standardization of speaker references, and role/turn tagging (Section 3.2, p. 3). Release documentation confirms a pipeline with an explicitly manual, unreleased transformation stage between extracted text and standardized JSON (`docs/dataset_pipeline.md`, steps 2–4). `docs/cleaning_choices.md` lists extensive JSC removals and some specific modifications, including deletion of interpreter utterances.

This labor is valuable but not reproducible or reliability-tested. The release has source-fetch notebooks and standardized outputs, but not the complete raw/intermediate corpus, manual edit ledger, annotator identities/training, dual annotation, error sample, agreement, or source-to-final diffs. Removing interpreters can change who had access to which utterance and can erase a consequential mediation role. “Manually corrected” is therefore a transformation description, not evidence that speaker, turn, omission, or semantic fidelity is accurate.

### Split and window lineage

The paper uses dialogue-level 80/10/10 splits stratified by broad domain: 1,824 train, 228 dev, and 229 test dialogues (Section 3.3, p. 4). Release inventory reproduces those counts. There is no exact full-dialogue content overlap across splits in the pinned release.

The released split notebook calls `random.shuffle(files)` without a seed and stratifies only by the four domains. It does not group by collection, interviewer, respondent, case, recording series, institution, time, or source document family. Direct release audit found substantial identity reuse: 61 elicitor identities and 111 respondent identity strings occur in both train and test, including recurring Supreme Court justices and advocates. This is not item leakage in the strict dialogue-ID sense, but it means test perplexity and style alignment partly measure familiar speakers, institutions, formats, and recurring discourse.

Rolling six-turn windows are generated after splitting, preserving dialogue separation but creating severe within-dialogue dependence. The 10,285 test blocks come from only 202 dialogues that survive formatting; one dialogue contributes 429 blocks. Train has 83,181 blocks from 1,622 dialogues, with a maximum of 518 from one dialogue. Block-level aggregation consequently weights long dialogues heavily and cannot use 10,285 as an independent sample size. The paper reports point estimates only—no dialogue-clustered uncertainty, source-held-out evaluation, speaker-held-out evaluation, or leave-one-collection-out transport.

The formatter also drops leading elicitor turns, merges consecutive same-role turns, excludes windows over 512 Llama-tokenizer tokens, and removes segments whose final elicitor output has two words or fewer (Sections 6.3, pp. 7; release notebooks). These choices select shorter, alternating, substantive-looking interactions and remove backchannels. They change both the learned style and the target turn distribution; no attrition table by source, role structure, or conversational function is provided.

### POMDP formulation versus realized experiment

The paper defines latent respondent information `X_t`, elicitor action `A_t`, respondent observation `O_{t+1}`, a history-derived language-model state `S_t`, and reward `r(H_t,A_t,O_{t+1})` (Section 4, pp. 4–5). This is a useful conceptual decomposition, but the realized evaluation is not an interactive POMDP rollout:

- the respondent and transition dynamics are never instantiated for generated actions;
- the generated action does not produce `O_{t+1}`;
- no belief or explicit claim state is tracked;
- no institutional objective appears beyond a broad domain string;
- the horizon is one generated next turn in a fixed human trajectory; and
- no stopping action or policy is evaluated.

The hidden state of a causal model is treated as functionally mirroring a belief state, but it is neither calibrated over respondent information nor inspected for sufficient statistics. A next-token representation of the transcript does not by itself identify what is known, missing, contradicted, sensitive, authorized, or relevant to a decision.

### Factual-novelty reward and ORL

The reward counts previously unseen named entities in the recorded respondent turn following a recorded human elicitor turn (Section 6.2, p. 7). Release code uses spaCy `en_core_web_trf`; it excludes only `CARDINAL` entities and canonicalizes exact lowercased `label:text` strings. Despite paper wording about “entities, events, or facts,” there is no event/fact extraction, entailment, factuality, source authority, relevance, specificity, or causal attribution.

The proxy has several confounds:

- proper-name-rich or verbose speech receives more opportunity for reward;
- aliases, coreference, spelling, nested entities, and repeated facts are mishandled;
- a new name can be irrelevant, wrong, sensitive, or already known under another form;
- a valuable explanation with no new named entity scores zero;
- question quality and respondent disposition are inseparable in observational transcripts; and
- long future returns credit early human questions for all later human-trajectory entity introductions.

In the pinned test blocks, 67.8% have reward zero; the domain mean ranges from 0.296 in academic interviews to 1.792 in oral history, with an oral-history maximum of 223. This makes corpus/domain composition part of the reward scale. The paper notes outliers but does not normalize by respondent opportunity, source, dialogue, or question type.

The release's ORL implementation introduces a more direct reproducibility threat. `ValueHead.forward` computes `last_indices = (labels != -100).sum(dim=1)-1`, then indexes `hidden_states[batch,last_indices]`. Because context labels are masked and target labels occur later in the sequence, a count of target tokens is not their absolute endpoint index. The critic generally reads an early context token rather than the stated last unmasked EOS/action state. In addition, returns and advantages are normalized within shuffled batches of four, so the relative weight of an example depends on three co-batched examples; the value head is not released with the adapters; dev data is not used in the ORL script; and training logs/checkpoint-selection evidence are absent. The paper's SFT/ORL difference is small and unsupported by repeated training seeds or uncertainty. “ORL is competitive” is a configured outcome, not evidence that correctly implemented long-horizon optimization improved elicitation.

## Evaluation and evidence

### Conformity is source imitation

Perplexity scores the real held-out elicitor utterance under each model, pooled by target tokens (Section 5.1, pp. 5–6). Fine-tuning dramatically reduces perplexity—for Llama-3.1-8B in academic interviews, from 46.9 to 10.9 SFT / 12.5 ORL (Table 6, p. 8). This strongly supports adaptation to corpus language and recurring elicitor distributions.

It does not show that the model's generated question is useful. Multiple questions may be valid; likelihood of the historical turn rewards imitation of one realized interviewer, including leading, adversarial, ceremonial, backchannel, or source-specific behavior. Identity and collection reuse across splits further weakens out-of-source interpretation. “Conformity” should therefore be named reference-distribution fit, not professional or objective conformity.

Response length similarly shows style/efficiency differences, but the prompt-only condition receives a much longer detailed prompt while SFT/ORL receive only a base instruction. Prompt token counts (e.g., 540.4 versus 180.4 in academic) are part of the treatment, not an independently held resource envelope. Generation uses `pipeline(..., max_new_tokens=500)` with no disclosed `do_sample`, temperature, seed, stop, invalid-output, or repetition policy. Single generated outputs cannot establish reliability.

### Progression is semantic distance, not progress toward an objective

Progression averages decayed cosine distance between each utterance and preceding utterances using `all-MiniLM-L12-v2` (Section 5.2, pp. 6, 8). Shuffling yields larger distance than real order, which establishes sensitivity to local semantic ordering. It does not establish forward movement, relevance, information gain, or goal attainment. A coherent deep probe may remain semantically close; an abrupt irrelevant topic switch may score high.

The metric is also computed over five fixed human turns plus one generated turn, so most of each score is inherited context. Prompt-only models score *lower* than real while shuffled scores higher; there is no demonstrated optimum, calibrated acceptable region, or criterion validity against expert judgments/outcomes. Embedding model and `k=5, gamma=.5` are unablated. The package returns dialogue means and then unweighted domain means, while overlapping windows remain clustered.

### Turn-length ratio is an interaction prior, not an outcome

Turn-length ratio divides mean respondent-turn tokens by mean elicitor-turn tokens (Section 5.3, p. 6). In generated evaluation, the respondent turns are fixed historical context; the model cannot cause their length. Only the denominator changes. A terse generated question therefore moves the ratio toward the human corpus even without eliciting anything. The claim that adapted models “draw out” longer responses is unsupported by this offline design.

Long respondent turns can reflect narrative genre, legal argument, power imbalance, verbosity, distress, or poor interviewer control. Concision can be useful, but ratio >1 is not a universal success threshold and should not cross domains without respondent burden, content value, and objective evidence.

### Human evaluation

Mechanical Turk workers rated real, prompted, SFT, and ORL questions side by side for 100 stratified test blocks, three workers per block, on Progression, Conversational Control, Outcome Relevance, Probing Effectiveness, and Conformity (Section 6.6 and Appendix A.6, pp. 9, 13–14). Response positions were shuffled. Workers needed >500 HITs and >90% approval and were reportedly paid at a rate consistent with U.S. minimum wage.

This is useful as a perceptual check, but not an expert or outcome validation:

- workers' domain expertise, interview training, demographics, location, and worker count are absent;
- the exact pay, estimated/actual completion time, burden, exclusions, attention checks, and invalid assignments are absent;
- workers see all four alternatives together, creating comparative/contrast effects;
- the “Dialogue Setting” is only a broad domain, not the institutional objective or protocol;
- source identity may be inferable because real turns differ stylistically from model outputs;
- no respondent answer or downstream consequence is visible;
- sampled block IDs and raw ratings are not released; and
- the paper reports no inter-rater reliability, uncertainty, hypothesis tests, or domain/source breakdown.

The release notebook computes Krippendorff alpha but preserves no outputs. Its preprocessing drops worker IDs and retains assignment IDs, making a stable rater-by-item design unavailable. The reported means actually favor prompted questions on every dimension (e.g., Progression 4.25 versus real 3.89, SFT 3.65, ORL 3.70; Table 9, p. 9). Authors interpret this as crowd preference for polished, fuller, leading questions. That finding undermines the claim that human evaluation simply “corroborates” automatic alignment: raters prefer an output style that the conformity/length metrics treat as less human-like. It demonstrates construct disagreement, not confirmation.

## Unique insight

The deepest transferable insight is that **elicitation has four distinct objects that YIELD partly collapses**:

`question-form resemblance → respondent information caused by the question → objective-relevant evidence update → legitimate institutional consequence`

YIELD directly measures mostly the first. Its reward is observational association with the second on human trajectories; it never observes a model-caused answer, explicit update, or consequence. A benchmark must not promote style fit into information acquisition, nor acquisition into legitimate use.

Second, **an institutional objective cannot be represented by an occupational/domain label**. “Academic,” “journalistic,” “judicial,” and “oral history” determine surface conventions but not who is entitled to ask, what information is needed, which sources are authoritative, what questions are prohibited, when enough evidence exists, or whose welfare matters. The objective must be an inspectable object with decision use, missing claims, authority, constraints, stopping criteria, and loss.

Third, **respondent behavior is part of the treatment and the outcome**. Offline next-turn replacement freezes the respondent, so it is safe and scalable but cannot estimate elicitation. An interactive test must preserve respondent realization, answerability, refusal, uncertainty, burden, and disclosure authority. Longer answers and more entities are not automatically better; a correct refusal or bounded “I don't know” may be the professionally valid outcome.

Fourth, **historical public dialogue is evidence about realized practice, not automatically a normative skill**. Courts, journalism, qualitative research, and oral history contain leading questions, power asymmetries, strategic answers, source-specific rituals, and historically contingent norms. Expert review is required before turning recurring behavior into guidance, a rubric, or a model objective.

Finally, the human/automatic disagreement is diagnostically valuable. Human workers preferred verbose prompted questions while corpus metrics preferred fine-tuned brevity. Plural measures should remain separate until a validity argument states whether the target is historical imitation, perceived question quality, supported claim yield, objective progress, respondent experience, or decision utility.

## Limitations and validity threats

1. **Construct substitution:** fixed-context next-turn generation replaces interactive information acquisition.
2. **No model-caused observation:** generated questions never receive respondent answers.
3. **No explicit objective:** broad domain labels stand in for institutional goals, missing claims, and decision use.
4. **No stopping evaluation:** the finite-horizon framing has no learned/evaluated stop, escalation, or clarification policy.
5. **Latent-state rhetoric:** LLM hidden representations are called belief-state analogues without calibration or sufficient-state evidence.
6. **Observational reward:** entity counts follow human questions in human trajectories and do not identify effects of model actions.
7. **Entity/fact conflation:** spaCy named entities are described as entities/events/facts but do not establish facts, novelty, relevance, or truth.
8. **Domain-dependent reward scale:** oral-history verbosity/outliers dominate potential return magnitude; 67.8% of pinned test blocks score zero.
9. **Reward gaming remains untested:** curated offline data prevents training-time action gaming, but a deployed learned policy could seek names, verbosity, or sensitive disclosures.
10. **ORL critic indexing defect:** the released value head generally reads the wrong sequence position.
11. **Batch-relative AWR:** batch-of-four return/advantage normalization makes weights dependent on co-batched examples.
12. **No repeated training seeds:** SFT/ORL differences have no run-level uncertainty or stability evidence.
13. **No interactive baseline:** no scripted, random, uncertainty-seeking, protocol-guided, human, or oracle policy is compared on actual answer yield.
14. **Unseeded split:** release split code uses global random shuffle without a recorded seed.
15. **Speaker/source leakage:** many elicitor and respondent identities, institutions, collections, and discourse formats span splits.
16. **Only broad-domain stratification:** no collection-, protocol-, speaker-, respondent-, institution-, time-, or topic-held-out evaluation.
17. **Overlapping-window dependence:** up to 429 test blocks derive from one dialogue; block counts are not independent trials.
18. **Length-weighted training/evaluation:** long dialogues and sources contribute far more windows and token mass.
19. **Formatter selection:** short backchannels, long windows, initial elicitor sequences, and nonalternating turns are altered or removed.
20. **Role collapse:** multiple speakers and mediators are reduced to two roles despite distinct authority.
21. **Manual transformation opacity:** no complete edit ledger, annotation protocol, agreement, or source-to-output fidelity sample.
22. **Interpreter deletion:** release documentation records removing interpreter utterances, potentially changing access and meaning.
23. **Historical practice is not normative:** corpus behavior may be leading, coercive, adversarial, ceremonial, outdated, or source-specific.
24. **Perplexity has one-reference bias:** many valid next questions exist; low likelihood does not imply low quality.
25. **Progression lacks criterion validity:** semantic distance can reward irrelevant topic change and punish productive depth.
26. **Context-dominated Progression:** five of six turns are fixed human context; only one turn differs by model.
27. **Turn ratio cannot measure elicited response:** respondent turns are frozen; only generated-question length changes.
28. **Unequal prompt treatment:** prompted models receive much longer explicit guidance than adapted models.
29. **Single generation per block:** no decoding repeats, uncertainty, invalid-output account, or reliability profile.
30. **No generation resource ledger:** training/inference tokens, GPU-hours, energy, latency, retries, and dollars are absent.
31. **Crowd workers are not domain experts:** eligibility filters indicate platform experience, not interviewing or professional authority.
32. **Comparative human-eval display:** four alternatives shown together can create contrast and style preference effects.
33. **Missing human-eval reliability:** raw results, worker IDs, exclusions, agreement outputs, and uncertainty are unavailable.
34. **Human/automatic disagreement:** prompted outputs lead every human dimension while automatic conformity favors adapted models.
35. **No respondent outcomes:** informativeness, comfort, refusal, disclosure regret, accuracy, trust, and burden are unobserved.
36. **No harm/safety evaluation:** leading questions, bias, coercion, sensitive data, and power imbalance are discussed but not measured.
37. **Copyright/consent conflation:** public or CC availability does not establish participant consent for model training or institutional-agent use.
38. **Aggregate-license conflict:** CC BY 4.0 release labeling coexists with an acknowledged CC BY-NC 4.0 Oyez component.
39. **Incomplete rights manifest:** collection-level source version, item license, attribution, participant-use basis, and withdrawal state are not machine-readable.
40. **Identifiability:** speaker names and transcript contents are preserved; no reidentification/sensitivity audit is reported.
41. **Model-card incompleteness:** per-adapter cards are largely unfilled templates and omit uses, risks, data, training, and evaluation.
42. **Release drift:** code/adapters/PyPI postdate v1 and the acquired dataset revision changed in July; none proves exact paper-time identity.
43. **No generated outputs/results release:** paper tables cannot be exactly recomputed without original generations, training logs, human ratings, and analysis outputs.
44. **Cross-domain transport unsupported:** four archive types in English do not establish elicitation across professions, cultures, languages, private settings, or live stakes.
45. **No expertise-transfer validation:** no cues, thresholds, incidents, contradiction resolution, artifact projection, or downstream checks are validated.

## Reproducibility and operational realism

Release inspectability is comparatively strong. The immutable paper, 51-file code snapshot, all 2,281 full dialogues, all 103,454 experimental blocks, six adapter snapshots, and complete evaluator wheel are locally preserved and integrity-checked. Counts match the paper. The dataset reveals source links, collections, speaker identities, turns, and split lineage. The code exposes prompts, formatting, reward computation, training, generation, metrics, and human-batch construction. This enabled the split, clustering, licensing, and critic-index audits above.

Exact experimental reproduction is nevertheless weak. The manual annotation stage and original/intermediate corpus are incomplete; split randomness is unseeded; dependency versions and base-model revisions are not locked; adapter cards omit training identity; training logs, value heads, generated outputs, metric tables, raw human ratings, sampled IDs, worker IDs, and costs are absent; and the release artifacts postdate v1. The code is closer to an inspectable implementation sketch than a paper-result replay package.

Operational realism is high for **surface exposure to historical interviewer language** and low for **agentic elicitation**. Real transcripts preserve long contexts, interruptions, multiple speakers, heterogeneous genres, and naturally occurring respondent language. But the experiment removes live respondents, institutional case state, question authority, protocols, consent, refusal, sensitive-information handling, source verification, contradiction, stopping, long-horizon memory, downstream decisions, and consequences. The POMDP is formal framing rather than an executable environment.

## Transfer to skill-bench

### Retain

- Separate elicitor action, respondent observation, latent/missing information, objective, and horizon.
- Use real practice corpora as candidate behavior evidence with source and transformation lineage.
- Preserve full dialogues and derived-window parent IDs rather than treating windows as independent tasks.
- Keep style conformity, information acquisition, objective progress, respondent burden, safety, cost, and decision utility as separate measures.
- Archive complete code/data/model/evaluator identities with timing boundaries.
- Treat human/automatic disagreement as a diagnostic signal rather than averaging it away.

### Repair before reuse

1. **Specify an objective record.** Declare beneficiary, decision/use, required claims, source authority, constraints, permissible questions, stopping/escalation rules, and stakeholder loss.
2. **Evaluate the causal interaction.** A generated question must receive a versioned respondent observation in a consented human, frozen simulator, or replay/intervention design; preserve nonresponse/refusal and invalid episodes.
3. **Use claim-level information gain.** Score supported propositions newly established, corrected, bounded, or ruled out relative to the objective—not named-entity count. Keep unsupported/sensitive disclosures negative or separately governed.
4. **Type question opportunity and effect.** Record what was already known, which question was asked, whether it was answerable/authorized, what answer arrived, what claim state changed, and whether the final artifact/decision used it.
5. **Make stopping evidence-based.** Track required claims as confirmed, contradicted, unknown, inaccessible, unauthorized, or escalated; measure premature closure and excess burden.
6. **Split for the intended claim.** Hold out speakers, respondent groups, collections/protocols, institutions, and time when claiming transport. Cluster inference at dialogue/source/contributor levels.
7. **Audit corpus authority and rights.** Maintain item-level license/consent/use basis, attribution, sensitivity, identity handling, prohibited uses, withdrawal/takedown, and transformation lineage. Resolve incompatible license conditions before aggregate release.
8. **Validate behavioral candidates.** Expert reviewers should decide whether recurring questions represent legitimate practice, domain-specific ritual, historical artifact, coercive behavior, or counterexample before skill/rubric projection.
9. **Use matched policy baselines.** Compare concise style imitation, protocol guidance, uncertainty-seeking, claim-value selection, random questions, and human experts under equal context, tools, time, and respondent realization.
10. **Repair and test the ORL implementation.** Index the true target endpoint, preserve the value head, freeze batch semantics, add unit tests, repeated seeds, held-out policy evaluation, and reward-hacking cases before mechanism claims.

### Bounded validation design

A cross-domain elicitation conformance slice could use a frozen respondent/evidence simulator derived from independently reviewed claim packs, not copied people. For each episode:

- disclose a legitimate role and bounded objective;
- plant required, optional, sensitive, unavailable, contradictory, and conditionally applicable claims;
- expose multiple question opportunities, refusals, and one misleading but plausible answer;
- compare equal-budget policies under repeated respondent realizations;
- require claim-level locators and a stop/escalate decision; and
- score supported claim gain, contradiction discovery, unauthorized request rate, unsupported adoption, burden/turns/tokens, premature stopping, and downstream artifact/check utility separately.

This tests information acquisition and stopping without claiming expert participation or professional transport. A later consented real session remains necessary to validate human burden, authority, read-back, and expertise projection.

The existing benchmark bundle, evidence-chain, trace, participation, metric-monitoring, validity-argument, task-health, and blocked elicitation-session machinery can represent these requirements. No new schema is needed.

## Concrete repository actions

1. **Index this review as release-audited elicitation-measurement evidence.** Claim ceiling: corpus-style next-turn adaptation under fixed historical contexts.
2. **Do not add a source-specific build task.** Existing contracts already house objective, evidence-view, lineage, metric, participation, and validity requirements.
3. **Use the four-link claim chain in the next expertise synthesis:** question-form resemblance → caused respondent information → objective-relevant evidence update → legitimate consequence.
4. **Keep the consented micro-pilot gate blocked.** YIELD's public historical data does not exercise present contribution consent, read-back, burden, or downstream approval.
5. **If any YIELD-derived model/data are reused, resolve item-level rights and sensitive-person governance first; do not rely on the aggregate CC BY label.**

## Bottom line

YIELD is valuable as a large historical-dialogue resource and as a caution against evaluating proactive elicitors like reactive assistants. Its release makes corpus and implementation assumptions unusually auditable. The study shows that fine-tuning can produce shorter, more human-distribution-like next questions on familiar archive families. It does not show that those questions cause useful, truthful, authorized, or decision-relevant information to be disclosed. `skill-bench` should preserve the action–observation–objective decomposition, but demand interactive claim-state updates, authority, stopping, burden, safety, clustered inference, and rights provenance before calling an agent an effective elicitor of expertise.