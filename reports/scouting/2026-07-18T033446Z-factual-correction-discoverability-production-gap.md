# Scouting note — production factual-correction discoverability gap

- **Timestamp:** 2026-07-18T03:34:46Z
- **Evidence status:** arXiv API metadata/abstract, immutable URL checks, arXiv HTML heading/external-link inspection, web discovery, and exact repository duplicate searches only. The paper body, appendices, source archive, customer records, human labels, prompts, traces, or results were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Iterate Until Retrieved: Factual Nugget Optimization for Discoverable Continual Corrections in Agentic RAG** — Moshe Hazoom, Gal Patel, Alon Talmor, and Tom Hope; arXiv:2605.25641v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2605.25641v1 · https://arxiv.org/pdf/2605.25641v1 · https://arxiv.org/html/2605.25641v1
- URL checks returned HTTP 200 for the immutable record and an 8,135,274-byte PDF. The arXiv API reports v1 submitted and last updated 25 May 2026; its summary contains no withdrawal or retraction notice.
- The abstract describes free-form response feedback converted into compact factual “nuggets,” then iteratively rewritten by replaying the triggering query and generated paraphrases through the production retrieval-and-answer stack until the correction is discoverable and used. It reports evaluation on two production B2B knowledge-assistance agents across multiple companies: a product-support agent and a support-ticket assistant. These are author-stated abstract claims awaiting full-paper verification.
- The arXiv HTML exposes sections for the production setting, factual corrections, retrieval stack, chat-agent correction set, held-out queries, support-ticket transfer, negative-control traffic, answer-level evaluation, actionability classifier, judge rubric, and cost. No author-linked code/data repository was visible in the HTML external links or targeted web search. Absence of a discovered release is a scouting observation, not proof that none exists.
- Exact arXiv-ID/title searches found no local review, task, or scouting note. The newly reviewed OpenAI/Thrive Tax AI case covers practitioner correction promotion into evals and product changes; existing RAG/memory/context reviews cover retrieval, authority, state, and adoption separately. None audits a production correction transformed specifically to optimize future discoverability and answer use through the deployed stack.

## Why this is a narrow, useful gap

The relevant chain is:

`free-form correction event → corrector identity/authority and affected tenant → supported factual proposition, scope, valid time, and contradiction state → actionability classification → nugget transformation and approval → indexed object/version → eligible future query → retrieval opportunity and rank → answer adoption/citation → independent factual consequence → stale/conflicting correction handling → maintenance cost and production value`.

The source is unusually direct for the repository’s current correction-to-eval work because it makes **storage insufficient**: a correction may be authorized and indexed yet remain undiscoverable or unused by the configured production agent. It may therefore supply evidence for separating correction capture, semantic fidelity, retrieval opportunity, delivery, answer adoption, and endpoint correctness.

The same loop creates important validity threats. Optimizing against the triggering query and generated paraphrases can overfit a query family; the production stack acts as both optimization environment and evaluator; automatic judges may share model or prompt dependencies with the optimizer; historical user feedback may be incomplete, mistaken, unauthorized, tenant-specific, stale, or privacy-sensitive; and a negative-control traffic result does not by itself establish absence of collateral retrieval, answer, or maintenance harm. Reported production transfer, human evaluation, and cost require exact eligible/selected/held-out/invalid denominators, company and correction clustering, configured-system identity, temporal split, missingness, uncertainty, and release boundaries.

This is a bounded production knowledge-assistance mechanism case, not a proposal to narrow `skill-bench` to RAG, support work, or one vendor.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent evaluation and context/memory engineering), B (evidence-bearing expertise/correction transfer), and D/E (cross-source consolidation and decision-relevant human learning).
- **Concrete evidence:** immutable-v1 full-paper/source audit with a typed correction-to-use chain, exact experimental denominators, production/held-out/transfer/negative-control estimands, human and automatic observer protocols, resource costs, release inspectability, and page/file-grounded retain/repair/test implications.
- **Uncertainty clarified:** when a free-form correction becomes an authorized, discoverable, adopted, and independently useful knowledge object rather than merely stored feedback or same-stack optimization success.
- **Mode:** narrow expansion. The queue had two autonomous consolidation tasks and one human prerequisite pending, but no review/source/research task; this restores one bounded primary-source evidence path without restarting broad scouting.
- **Duplication/scope check:** the Tax AI review covers correction-to-eval/product promotion, while this candidate tests correction-to-index-to-retrieval-to-answer realization. Existing contracts should host the findings; add no RAG-specific schema or pilot absent review evidence.
- **Useful completion:** distinguish correction authority, semantic fidelity, nugget optimization, retrieval, answer use, factual correctness, collateral effects, cost, and production value; preserve company/query/correction clustering and temporal/configuration identity; state the strongest licensed claim and blocked generalization/readiness claims.

Added one task: `review-production-factual-correction-discoverability` (review, priority 60). No second source was queued.