You are completing one internal synthetic evidence-acquisition task. This is not professional advice.

TARGET
{target}

PUBLIC CONTEXT
{public_context}

CONDITION
{condition_instructions}

TRANSCRIPT AND SUPPLIED EVIDENCE
{transcript}

At this turn, write exactly one JSON object to `outputs/{turn_file}`. Do not write any other file.

To request evidence, use:
{"action":"request","raw_request":"natural-language request for one evidence item","intent":"why it matters","requested_scope":"scope","expected_value_basis":"how it could change the decision"}

To stop, use:
{"action":"terminal","decision":"one disclosed decision token","evidence_ids":["only IDs actually supplied/released and used"],"rationale":"decision rationale tied to evidence","uncertainty":"remaining uncertainty","stop_reason":"decision_sufficient|marginal_value_below_cost|budget_exhausted|abstain|escalate"}

Rules: request at most one evidence item per turn. In active condition, make at least one request before terminal action. Parser/access/budget messages are environment evidence, not evaluator feedback. No grader result is available before terminal action. Never infer hidden content from an ID or denial. If evidence is insufficient at the deadline, follow the disclosed rule and state uncertainty.
