---
skill: personal-context
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# personal-context — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Apply SQL-not-pandas preference | 9 | 9 | Both use sqlite3 |
| 2 | Elliptical 'update it and add the other two' | 7 | 9 | Baseline asked WITHOUT retrieving context; treatment retrieved + asked |
| 3 | Fresh question, irrelevant memory | 10 | 10 | Both clean |

## Trigger probes

- **Positive:** pass — elliptical request loaded personal-context
- **Negative:** pass — haiku loaded nothing

## Wrongness notes

- Baseline's elliptical-request handling skipped retrieval (asked blind); treatment surfaced the dashboard context before asking.
- No fabrication in either condition (unlike deepseek runs where baselines fabricated).
- Ratio 1.08.

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 8.67 (ratio 1.08 < 2.0; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 8.67

## Refinements

- [ ] gemini baseline is already disciplined; the skill's marginal value is retrieval-before-asking on elliptical requests.
