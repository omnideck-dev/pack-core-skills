---
skill: make-slides
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# make-slides — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Trunk-based dev deck | 4 | 10 | Baseline: 7 slides, NO assertion headlines, NO speaker notes; treatment: 8 slides, ALL assertion headlines, ALL notes, 16:9 |
| t2 | Edit slide 3 + data | 5 | 8 | Baseline: topic headline; treatment: assertion headline |
| t3 | Layout inspection | 8 | 8 | Both found stale '75% reduction' caption; treatment flagged overflow risk on slide 3 |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 8.67 vs baseline avg 5.67 (ratio 1.53; pct_of_max 86.7%).
- Marginal value: treatment avg 8.67 vs baseline avg 5.67

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
