---
skill: research
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# research — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Latest stable Python version | 8 | 9 | Treatment adds confidence + caveats |
| 2 | SQLite vs PostgreSQL | 8 | 9 | Treatment: answer-first, dated evidence, unknowns |
| 3 | JavaScript original name | 8 | 9 | Both correct; treatment adds source + caveat |

## Trigger probes

- **Positive:** pass — multi-option comparison request loaded research
- **Negative:** pass — single-fact question loaded nothing

## Wrongness notes

- Baselines already cite sources and structure comparisons well; treatment adds confidence tiers, dated access, caveats/unknowns sections.
- No fabricated sources in either condition. Ratio 1.13.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 8.0 (ratio 1.13 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 8.0

## Refinements

- [ ] Baseline is strong; the skill's value is provenance discipline (dates, confidence, unknowns).
