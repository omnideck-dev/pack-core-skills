---
skill: research
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# research — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Latest stable Python version | 6 | 3 | Baseline answered from training knowledge w/ caveat; treatment HARD-STOPPED per skill rule (no web access = no source = refuse) |
| t2 | SQLite vs PostgreSQL | 7 | 3 | Baseline: full comparison w/ caveats; treatment HARD-STOPPED |
| t3 | JavaScript original name | 7 | 3 | Baseline answered (Mocha/Eich) w/ caveat; treatment HARD-STOPPED |

## Trigger probes

- **Positive:** not-run
- **Negative:** not-run

## Verdict

- **Fail** — treatment avg 3.0 vs baseline avg 6.67 (ratio 0.45; pct_of_max 30.0%).
- Marginal value: treatment avg 3.0 vs baseline avg 6.67

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
