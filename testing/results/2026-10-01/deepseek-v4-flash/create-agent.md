---
skill: create-agent
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 5
---

# create-agent — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Slack community assistant | 8 | 10 | Treatment: 1 grant (least privilege) + richer prompt |
| t2 | Research reporter | 8 | 10 | Treatment: 2 grants (least-privilege) + richer prompt |
| t3 | Code review specialist | 8 | 10 | Treatment: 2 read-only grants + self-containment verified |
| t4 | CI monitor | 10 | 10 | Baseline already minimal (2 grants); treatment adds richer prompt |
| t5 | Marketing copywriter | 7 | 10 | Baseline: 5 grants! Treatment: 1 grant |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 8.2 (ratio 1.22; pct_of_max 100.0%).
- Marginal value: treatment avg 10.0 vs baseline avg 8.2

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
