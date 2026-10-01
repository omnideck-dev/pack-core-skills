---
skill: research
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# research — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Latest stable Python | 6 | 9 | Baseline: knowledge-only; treatment: python.org |
| 2 | SQLite vs PostgreSQL | 7 | 9 | Treatment: primary docs + confidence |
| 3 | JavaScript original name | 7 | 10 | Treatment: primary sources + refused to guess the coiner |

## Trigger probes

- **Positive:** pass — comparison request loads research
- **Negative:** pass — single-fact question does not

## Wrongness notes

- **Harness finding**: glm baselines did NOT use web tools (answered from internal knowledge, marked unverified); treatments DID fetch primary sources. The skill prompt appears to trigger tool usage, not just methodology.
- T3 treatment found Brendan Eich's own blog (primary source) and explicitly refused to guess who coined "JavaScript" when no source named an individual — the exact honest-gap behavior the fixture tests.
- Ratio 1.4.

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 6.67 (ratio 1.4 < 2.0; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 6.67

## Refinements

- [ ] Primary-source discipline + honest-gap refusal are load-bearing; baselines guess.
