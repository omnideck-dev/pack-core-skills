---
skill: create-tool
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 5
---

# create-tool — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Text stats tool | 9 | 10 | Treatment: registered + idempotency + existing check |
| t2 | CSV→JSON (existing check) | 9 | 10 | Baseline checked existing! Treatment: registered + parameterized |
| t3 | Config validator + idempotency | 8 | 10 | Treatment: registered + parameterized |
| t4 | File checksums | 9 | 10 | Treatment: registered + edge cases |
| t5 | Directory stats | 9 | 10 | Treatment: registered + deterministic |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.8 (ratio 1.14; pct_of_max 100.0%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.8

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
