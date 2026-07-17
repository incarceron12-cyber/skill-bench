# Scouting note — sparse production outcomes to critic-rubric validity gap

- **Timestamp:** 2026-07-17T04:41:02Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local corpus/queue duplicate searches, official GitHub metadata/tree and README triage, and Hugging Face model metadata only. The PDF/body, appendices, production traces, labels, rubric definitions, training data/code, model weights, experiments, statistical analyses, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**A Rubric-Supervised Critic from Sparse Real-World Outcomes** — Xingyao Wang, Valerie Chen, Heng Ji, and Graham Neubig, arXiv:2603.03800v1.

- Immutable record/PDF: https://arxiv.org/abs/2603.03800v1 and https://arxiv.org/pdf/2603.03800v1
- Official implementation: https://github.com/OpenHands/critic-rubrics at current inspected commit `9f03ba41f4431191c5ce17e9ccfc80ccda73ee69`
- Released 4B critic model: https://huggingface.co/OpenHands/openhands-critic-4b-v1.0 at inspected revision `80369c1468c5f0cad30f3cd8e9b8b7371e9d9b41`
- The arXiv API identifies a single v1 submission on 4 March 2026 in `cs.AI`/`cs.LG`; its summary contains no withdrawal notice. Versioned abstract and PDF endpoints returned HTTP 200. No arXiv HTML rendering was available at the checked v1 endpoint.
- The abstract describes a semi-supervised critic trained from sparse/noisy human-agent interaction outcomes and 24 trace-observable behavioral features. It reports downstream use for SWE-bench best-of-N reranking, early stopping, and critic-selected training-data curation. These are author claims awaiting full-paper audit.
- GitHub API inspection identifies the official 43-object repository tree at the pinned current commit. It exposes typed prediction/feature structures, trajectory rubric code, annotation and batch-processing utilities, tests, and documentation. The pinned README links the paper, 4B model, and OpenHands integration docs. The inspected tree does not expose an obvious production-trace dataset, sparse human-feedback labels, critic-training pipeline, experimental run records, or paper-result tables; a reviewer must verify release correspondence rather than infer absence from this root/tree triage.
- Hugging Face API metadata verifies a model repository and immutable inspected revision with configuration, tokenizer, and two weight shards. The model card, weights, training correspondence, and reproducibility were not audited.
- Repository-wide exact-title, arXiv-ID, and distinctive-phrase searches found no review, queue item, or prior scouting note.

## Why this is a narrow, useful gap

The corpus already covers production-derived trajectory reports (AgentLens), signal-enriched review sampling (Signals), judge reliability (AgentRewardBench and Many-Facet), rubric construction/adaptation, criterion validity, and selective-review decision policies. This source appears to connect those layers through a distinct learned-supervision chain:

`production interaction sampling → sparse/noisy human outcome proxy → trace-observable rubric annotation → semi-supervised critic → predicted process features/success → rerank, stop, or curate decision → benchmark outcome and resource consequence`.

Dense predicted rubric features can improve a downstream decision without being expert-authoritative, reliably observed, causally diagnostic, or valid proxies for real-world quality. Production traces may also be clustered by user/task/session, selectively retained, censored by stopping, or split in ways that leak actors and task lineages. SWE-bench gains validate neither the original sparse proxy nor cross-domain transport by themselves. Coding is therefore a bounded substrate for the general question of turning sparse work outcomes into scalable trace evaluation, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent-evaluation frontier), B (expert/outcome-to-evaluation validity), and C (trace, rubric, metric, and decision-policy infrastructure).
- **Concrete evidence:** immutable-v1 deep review and timing-aware audit of the official typed-rubric implementation and released critic model.
- **Uncertainty clarified:** authority and observability of the 24 features; provenance, missingness, and decision relevance of sparse outcome proxies; leakage and clustering in learned critics; and whether downstream improvements support only configured selection-policy claims or something stronger.
- **Mode:** narrow expansion feeding validation/consolidation. Before addition the queue had one pending consolidation, one pending human prerequisite, no pending review, no claimed work, and three blocked builds.
- **Duplication/scope:** adjacent reviews cover reports, sampling, judges, raters, rubrics, criterion validity, or confidence policies separately; none audits this production-proxy → dense-rubric → learned-critic → resource-allocation chain. Existing general machinery should absorb findings; no coding-specific schema is proposed.
- **Useful completion:** reconstruct sampling units, proxy authority/timing/missingness, rubric authorship and labels, critic information views and objectives, split/cluster/leakage boundaries, decision policies, costs, uncertainty, negative cases, and exact release correspondence; then state bounded retain/repair/test implications.

Added `review-critic-rubrics-sparse-production-outcomes-validity` (priority 8). No full-paper, release-completeness, rubric-validity, evaluator-reliability, causal-diagnosis, human-preference, production-utility, cross-domain-transfer, or readiness claim was made during scouting.
