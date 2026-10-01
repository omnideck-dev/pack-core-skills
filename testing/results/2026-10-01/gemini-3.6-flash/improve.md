---
skill: improve
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# improve — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Mine transcript, propose artifacts | 8 | 10 | Treatment classifies types (memory/tool/routine/profile) + cites verbatim moments |
| 2 | Smallest fix (UTC) | 9 | 10 | Both memory write; treatment structured |
| 3 | Build parser artifact | 8 | 9 | Treatment: tool schema + JSON contract + tests; baseline: untested script |

## Trigger probes

- **Positive:** pass — frustration/learning request loaded improve
- **Negative:** pass — recall question loaded nothing

## Wrongness notes

- Baseline proposals hedge on artifact type ("memory/preference setting", "tool or Python module", "routine or standalone script"); treatment commits to one type per lesson with justification.
- T3: baseline built a script with no tests; treatment built a JSON-contract tool with a test suite.
- Ratio 1.16.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 8.33 (ratio 1.16 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 8.33

## Refinements

- [ ] Classification behavior is the value; consider rubric emphasis on R2.
