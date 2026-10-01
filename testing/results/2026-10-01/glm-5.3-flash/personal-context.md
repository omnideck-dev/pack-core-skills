---
skill: personal-context
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# personal-context — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Apply SQL-not-pandas preference + past rejection | 3 | 10 | Baseline USED PANDAS — ignored the preference AND re-proposed the rejected approach |
| 2 | Elliptical 'update it and add the other two' | 7 | 9 | Treatment retrieved dashboard context before asking |
| 3 | Fresh question, irrelevant memory | 10 | 10 | Both clean |

## Trigger probes

- **Positive:** pass — elliptical request loads personal-context
- **Negative:** pass — haiku does not

## Wrongness notes

- **Largest personal-context gap in the batch**: the glm baseline wrote a pandas-based script despite memory saying "plain SQL not pandas" AND memory recording that a pandas script was rejected for breaking the build. Treatment cited both facts and used plain SQL.
- No fabrication in either condition on T2; treatment retrieved before asking.
- Ratio 1.45.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 6.67 (ratio 1.45 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 6.67

## Refinements

- [ ] Preference-application is load-bearing; glm baselines ignore stored preferences.
