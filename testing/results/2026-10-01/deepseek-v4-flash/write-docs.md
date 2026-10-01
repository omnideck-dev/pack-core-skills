---
skill: write-docs
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# write-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | README for csvsum.py (verify commands) | 8 | 9 | Both verified commands; treatment adds quickstart front-loading + error table |
| t2 | API reference for config.py | 9 | 10 | Treatment adds error-behavior section (KeyError vs .get) + regeneration note |
| t3 | Correct stale doc claims | 9 | 9 | Both caught --output + dedup falsehoods |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 8.67 (ratio 1.08; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 8.67

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
