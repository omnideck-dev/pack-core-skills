---
skill: write-docs
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# write-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | README for csvsum.py | 9 | 9 | Both verified by running commands |
| 2 | API reference for config.py | 9 | 9 | Both accurate; treatment adds error-cases section |
| 3 | Correct stale doc claims | 9 | 9 | Both caught the falsehoods |

## Trigger probes

- **Positive:** pass — README request loads write-docs
- **Negative:** pass — blog post does not

## Wrongness notes

- Baselines already verify commands and write accurate tables. Treatment adds an error-cases section and deletes stale claims rather than hedging them.
- Ratio 1.0.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 9.0 (ratio 1.0 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 9.0

## Refinements

- [ ] Ceiling effect.
