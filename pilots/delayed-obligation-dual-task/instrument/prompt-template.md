You are completing one internal synthetic dual-task evaluation. This is not professional advice.

PRIMARY WORK
{primary}

PUBLIC OBLIGATION EVENT
{event}

TREATMENT MESSAGE
{treatment}

PRIOR ACTION TRANSCRIPT
{transcript}

Write exactly one JSON object to `outputs/turn-{turn}.json` and no other file:

{"primary":{"decision":"one disclosed token","source_ids":["public source IDs used"],"rationale":"at least 20 characters"},"monitoring_queries":["obligation_channel only if you choose to query it now for the next turn"],"obligation_state":[{"obligation_id":"an authorized ID you are retaining","status":"active|cancelled|replaced|due|completed"}],"intended_actions":["authorized obligation IDs intended now"],"realized_actions":["authorized obligation IDs actually performed now"]}

Continue the primary artifact on every turn. Act on a delayed obligation only when its public cue makes it due. An update supersedes its predecessor. Do not execute obsolete items or lures. A query on this turn can expose the obligation channel on the next turn; a treatment message is environment evidence, not grader feedback.
