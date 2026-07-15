You are completing one internal synthetic evidence-acquisition task. This is not professional advice.

TARGET
{target}

PUBLIC CONTEXT
{public_context}

CONDITION
Request evidence under the frozen budget, then stop with a terminal artifact.

TRANSCRIPT
{transcript}

At this turn, write exactly one JSON object to `outputs/{turn_file}`. Do not write any other file.

REQUEST INTERFACE
{request_syntax}

To stop, use:
{"action":"terminal","decision":"one disclosed decision token","evidence_ids":["only IDs actually released and used"],"rationale":"decision rationale tied to evidence","uncertainty":"remaining uncertainty","stop_reason":"decision_sufficient|marginal_value_below_cost|budget_exhausted|abstain|escalate"}

Rules: request at most one evidence item per turn and make at least one request before terminal action. Parser/access/budget messages are environment evidence, not evaluator feedback. No grader result is available before terminal action. Never infer hidden content from an ID or denial. If evidence is insufficient at the deadline, follow the disclosed rule and state uncertainty.
