---
skill: create-skill
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 5
---

# create-skill — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Server-status procedure | 9 | 10 | Treatment: 5-step workflow + rules + anti-patterns |
| t2 | Over-broad 'skill for coding' | 10 | 10 | Baseline narrowed to Python Unit Test Gen! Treatment narrowed to review-code |
| t3 | PR review overlap | 10 | 10 | Baseline created differentiated review-pull-request (delegates to review-code); treatment said reuse existing — both valid |
| t4 | Weekly report skill | 9 | 10 | Treatment: NO tool categories (least privilege) |
| t5 | SQL formatting | 9 | 10 | Treatment: 10-step workflow + anti-patterns |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 9.4 (ratio 1.06; pct_of_max 100.0%).
- Marginal value: treatment avg 10.0 vs baseline avg 9.4

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
