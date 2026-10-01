---
skill: write-docs
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# write-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | README for csvsum.py | 8 | 9 | Both verified by running commands; treatment adds verification report |
| 2 | API reference for config.py | 8 | 9 | Both accurate; treatment adds function index |
| 3 | Correct stale doc claims | 9 | 9 | Both caught the falsehoods |

## Trigger probes

- **Positive:** pass — README request loaded write-docs
- **Negative:** pass — blog post request did not

## Wrongness notes

- Baselines already verify commands and write accurate tables. Treatment adds a verification report and slightly better structure.
- No invented parameters in either condition. Ratio 1.08.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 8.33 (ratio 1.08 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 8.33

## Refinements

- [ ] Ceiling effect.
