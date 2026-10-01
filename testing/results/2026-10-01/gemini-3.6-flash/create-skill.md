---
skill: create-skill
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 5
---

# create-skill — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Server-status procedure | 7 | 10 | Baseline: no explicit trigger in description |
| 2 | Over-broad request | 9 | 9 | Both push back correctly |
| 3 | PR-review overlap | 9 | 9 | Both detect review-code overlap |
| 4 | Weekly report skill | 7 | 10 | Baseline: no trigger |
| 5 | SQL formatting | 9 | 10 | Baseline: unnecessary coding category; treatment: minimal |

## Trigger probes

- **Positive:** pass — turn-into-skill request loaded create-skill
- **Negative:** pass — skill-lookup question routed to review-code

## Wrongness notes

- **Explicit-trigger descriptions are the discriminator**: baselines write behavior descriptions ("Check server status by running...") without trigger language; treatment writes "Use when the user asks to...".
- Scope discipline (T2) and duplicate detection (T3) are solid in both conditions.
- Ratio 1.17.

## Verdict

- **Fail** — treatment avg 9.6 vs baseline avg 8.2 (ratio 1.17 < 2.0; pct_of_max 96%).
- Marginal value: treatment avg 9.6 vs baseline avg 8.2

## Refinements

- [ ] Trigger-language in descriptions is load-bearing for skill discoverability.
