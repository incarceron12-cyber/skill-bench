# Scouting note — human-review-to-executable-test projection gap

- **Timestamp:** 2026-07-16T20:38:56Z
- **Evidence status:** metadata/abstract and link triage only; the full paper was not read during scouting.

## Substantive finding — triage only

**Code Review Agent Benchmark (c-CRAB), arXiv 2603.23448v3** is a direct candidate for the expertise-to-evaluation stream:

- Immutable record: https://arxiv.org/abs/2603.23448v3
- Immutable PDF target: https://arxiv.org/pdf/2603.23448v3
- Authors: Yuntong Zhang, Zhiyuan Pan, Imam Nur Bani Yusuf, Haifeng Ruan, Ridwan Shariffdeen, Abhik Roychoudhury
- Primary category: `cs.SE`; submitted 2026-03-24 and updated 2026-04-07 according to the arXiv API.

The abstract says c-CRAB starts from human pull-request reviews and generates corresponding tests that act as held-out quality gates for reviews produced by code-review agents. It reports that the evaluated agents collectively solve only about 40% of tasks and often cover different aspects from human reviews. These are author claims requiring full-paper and release verification.

The first author's current publication page links the paper PDF but no c-CRAB code or data release. That is only a negative link check, not proof that no release exists.

## Why this is distinct

The reviewed corpus covers expert-authored rubrics, procedure-to-tool/oracle projection, source-to-task projection, generated evaluators, artifact checks, and benchmark audits. Repository searches found no treatment of arXiv 2603.23448 or a direct audit of this chain:

`real human review → represented issue/consequence → generated executable test → agent-review quality gate`.

The reusable benchmark question is whether an expert work product can be transformed into an executable observer without losing issue semantics, scope, severity, accepted alternatives, uncertainty, or authority. A generated test may faithfully detect one encoded consequence while still failing to establish that an agent review is correct, complete, useful to a recipient, or professionally acceptable.

## Charter decision filter and queue action

- **Objective advanced:** A (frontier research) and B (expertise-to-evaluation methodology).
- **Concrete evidence:** immutable v3 full-paper review plus any author-owned release audit.
- **Uncertainty clarified:** transformation fidelity and claim validity when human review feedback becomes executable hidden checks.
- **Mode:** narrow expansion; the queue had two pending tasks and no research/review backlog before this addition.
- **Duplication/scope check:** no paper-ID or equivalent projection review found; coding is one bounded work shape for a cross-domain transformation hypothesis, not a scope commitment.
- **Useful completion:** reconstruct and critique sampling, transformation lineage, authority, accepted alternatives, test semantics, generator/validator dependence, harness comparability, uncertainty, contamination, and reproducibility before recommending machinery.

Added one task: `review-crab-human-review-test-projection-validity` (priority 87). No full-paper claims or implementation task were added during scouting.
