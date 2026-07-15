# PASB Data Schema

Each row is a JSON object with one executable PASB episode.

## Core Fields

- `task_id`: unique task identifier, including scenario and delivery labels.
- `base_item_id`: source-normalized base item identifier.
- `source_subset`: source subset label, such as `PRF`, `CDL`, or `SOC`.
- `source_dataset`: source dataset name.
- `source_id`: source item id.
- `scenario`: one of `Personal-Opinion`, `Signed-Memory`, `Environment-Fact`, `Procedural-Workflow`.
- `delivery`: one of `All-at-Once`, `Progressive`, `Drip`, `Late-Shock`.
- `attribution`: whether the injected claim is user-attributed or unattributed.
- `claim_domain`: claim topic domain.
- `claim_length_words`: word count of the tested claim.
- `delivery_anchor`: intended delivery position across the five persist turns.
- `trigger`: tested claim and reference stance.
- `context_facts`: neutral facts carried from the source item.
- `query_target`: neutral downstream query target.
- `persist_dialog`: five persist-stage user turns.
- `query_dialog`: three query-stage user turns.
- `num_persist_turns`: number of persist-stage turns.
