# Evidence-request interface ablation v2

This is a prospective, active-only matched interface study over the two internally authored synthetic shapes from `evidence-acquisition-matched-agent-v1`. It compares the original free-text request object with a minimally structured request-topic object while holding scenario bytes, latent evidence, budgets, access/release rules, prompt content outside the syntax block, configured system, grader, schedule, invalidity rules, and claim ceiling fixed.

The structured interface does **not** display evidence IDs, available choices, answers, or a request menu. The agent emits one concise topic. A frozen exact-synonym map either resolves that topic to one atom or fails closed as `unmatched`, `ambiguous`, or `parser_error`; it never guesses. Both interfaces receive identical public scenario content. This reduces parser freedom without adding answer-bearing options.

`audit_v1.py` produces a hash-pinned root/surface audit of every retained v1 active request, parser/access transition, terminal citation proxy, stop, and grade. It does not rescore or modify v1. The prospective v2 instrument must be committed and pushed before `run_study.py execute` permits model calls. Every declared attempt is retained; retries and replacements are forbidden.

Commands:

```bash
python pilots/evidence-request-interface-v2/audit_v1.py
python pilots/evidence-request-interface-v2/freeze_protocol.py
python pilots/evidence-request-interface-v2/run_study.py preflight
# commit and push the frozen instrument before model calls
python pilots/evidence-request-interface-v2/run_study.py execute
python pilots/evidence-request-interface-v2/run_study.py replay
```

The study supports only exact internal observations about these request-interface executions. It does not license causal inquiry, agent capability, expert/professional validity, cross-domain generality, production, safety, or readiness claims.
