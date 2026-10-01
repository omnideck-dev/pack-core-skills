---
skill: humanize-text
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# humanize-text — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | De-AI the productivity article | 7 | 8 | Baseline added em-dashes; both over-compressed |
| 2 | Human-but-rough draft (overcorrection test) | 5 | 6 | BOTH formalized the casual message |
| 3 | Technical passage w/ hedges | 9 | 9 | Both preserve precision |

## Trigger probes

- **Positive:** pass — "sounds too AI" loaded humanize-text
- **Negative:** pass — proofreading loaded nothing

## Wrongness notes

- **Register-preservation FAIL for this model**: unlike deepseek (where treatment preserved the rough register), gemini's treatment ALSO formalized the casual message. The skill's discipline did not transfer.
- Both conditions over-compress T1 (drop the article's structure).
- Ratio 1.1.

## Verdict

- **Fail** — treatment avg 7.67 vs baseline avg 7.0 (ratio 1.1 < 2.0; pct_of_max 76.7%).
- Marginal value: treatment avg 7.67 vs baseline avg 7.0

## Refinements

- [ ] The register-preservation rule needs to be more emphatic in the skill prompt — it did not stick for gemini.
