---
skill: create-skill
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 5
---

# create-skill — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Server-status procedure | 9 | 9 | Both valid + trigger |
| 2 | Over-broad request | 6 | 10 | Baseline created a placeholder anyway; treatment pushed back |
| 3 | PR-review overlap | 5 | 8 | Baseline created duplicate without flagging overlap |
| 4 | Weekly report skill | 8 | 10 | Treatment: full trigger |
| 5 | SQL formatting | 7 | 10 | Treatment: trigger + minimal categories + semantics rules |

## Trigger probes

- **Positive:** pass — turn-into-skill loads create-skill
- **Negative:** pass — skill-lookup does not

## Wrongness notes

- **Scope discipline gaps in baseline**: T2-baseline wrote a placeholder `coding.json` despite the over-broad request; T3-baseline created `review-pr.json` without flagging the existing review-code skill. Treatment pushed back (T2) and offered differentiation (T3).
- Trigger-language in descriptions: baseline partial/missing on T4/T5; treatment full.
- Ratio 1.34.

## Verdict

- **Fail** — treatment avg 9.4 vs baseline avg 7.0 (ratio 1.34 < 2.0; pct_of_max 94%).
- Marginal value: treatment avg 9.4 vs baseline avg 7.0

## Refinements

- [ ] Scope discipline (push back on over-broad, detect duplicates) is load-bearing for glm.
