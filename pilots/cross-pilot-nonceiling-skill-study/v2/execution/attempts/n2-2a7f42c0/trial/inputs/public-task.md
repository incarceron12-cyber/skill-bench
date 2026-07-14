# LH evidence-synthesis cluster task v1

You are completing an isolated benchmark trial as a benchmark program analyst. Work only with files in this trial directory. Do not use the network, memory, external sources, or information outside this directory. Do not ask questions or modify inputs.

Advise whether to **adopt**, **pilot with controls**, or **do not adopt** skill-grounded scoring. Read every file under `sources/`; the polished adoption summary is a non-authoritative analyst argument, not a substitute for its cited rows. Reconcile aggregate judge consistency, individual human/automated concordance, absolute readiness, and the seven-run configured-system ablation.

Create both:

1. `outputs/evidence-matrix.csv` with columns `claim,evidence_id,authority,scope,caveat,decision_use`. Include at least one supporting and one disconfirming row. Every evidence ID must resolve to a supplied CSV row; preserve that row's authority, scope, and caveat exactly.
2. `outputs/recommendation.md` recommending exactly one allowed decision. Cite `[E##]` or `[E##, E##]` on the same line as every source-reported material number or causal claim. Mark analyst-chosen numeric thresholds as `{{PROSPECTIVE:<numeric text>}}`. State an explicit threshold, a minimum controlled experiment, at least one stop/reconsider condition, and which evidence would be needed to change the decision.

Different professional routes are allowed. The decision need not be `pilot with controls`; it must remain within the supplied evidence. Missing or conflicting evidence must be reported rather than guessed. No grader feedback, retry, or replacement attempt will be provided.
