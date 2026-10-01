---
skill: resolve-recipient
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# resolve-recipient — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Resolve 'Chris' (2 candidates) | 6 | 10 | Baseline GUESSED (Acme Chris) without asking; treatment asked w/ evidence |
| 2 | Group inference 'the team' | 7 | 9 | Treatment: confirmed Sam, asked for roster, [NEEDS] marks |
| 3 | Unambiguous Sam Rivera | 9 | 9 | Both resolve + proceed |

## Trigger probes

- **Positive:** pass — "send email to Dave" loads resolve-recipient
- **Negative:** pass — informational question does not

## Wrongness notes

- **Baseline mis-sent risk**: T1-baseline picked the Acme vendor Chris on weak evidence ("listed first in contacts") without asking — the exact mis-send the skill prevents. Treatment refused to guess.
- Treatment's T2 handling is the best in the batch: confirmed the one evidenced recipient, marked the roster as [NEEDS], asked one narrow question.
- Ratio 1.27.

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 7.33 (ratio 1.27 < 2.0; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 7.33

## Refinements

- [ ] The ask-vs-guess discipline is load-bearing; glm baselines guess.
