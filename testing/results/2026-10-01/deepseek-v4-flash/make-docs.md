---
skill: make-docs
profile: code_expert
model: deepseek/deepseek-v4-flash-0731
date: 2026-10-01
trials: 3
---

# make-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline | Treatment | Notes |
|---|------|----------|-----------|-------|
| t1 | Create retention-policy docx | 7 | 10 | Treatment: Subtitle + front-loaded exec summary + retention table + List Bullet |
| t2 | Add section at correct level | 9 | 9 | Both appended H1 correctly |
| t3 | Structure inspection | 9 | 9 | Both correct: navigable in Word |

## Trigger probes

- **Positive:** pass
- **Negative:** pass

## Verdict

- **Fail** — treatment avg 9.33 vs baseline avg 8.33 (ratio 1.12; pct_of_max 93.3%).
- Marginal value: treatment avg 9.33 vs baseline avg 8.33

## Refinements

- [ ] See skill-refinements.md for the consolidated list.
