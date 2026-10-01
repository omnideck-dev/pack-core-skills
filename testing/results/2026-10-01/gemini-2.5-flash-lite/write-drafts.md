---
skill: write-drafts
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# write-drafts — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Decision email w/ deadline | 7 | 8 | Treatment tighter |
| 2 | Rewrite drafty message | 8 | 8 | Both fine |
| 3 | Conference bio w/ unknowns | 4 | 6 | Baseline invented "Alex" + interests; treatment [NEEDS] marks but first-person violation |

## Trigger probes

- **Positive/negative:** not run — the model confuses skills with tools ("write_drafts tool is not available"); probes unreliable.

## Wrongness notes

- **Baseline invents specifics** (a name, interests) — the exact anti-pattern the skill targets. Treatment used [NEEDS] marks instead.
- Treatment T3 violated the third-person constraint (wrote "I specialize") — the skill's register rule partially applied.
- Protocol: flash-lite treats skills as tools; briefs must say "Do not load or call any tool or skill. Respond directly."
- Ratio 1.16.

## Verdict

- **Fail** — treatment avg 7.33 vs baseline avg 6.33 (ratio 1.16 < 2.0; pct_of_max 73.3%).
- Marginal value: treatment avg 7.33 vs baseline avg 6.33

## Refinements

- [ ] [NEEDS] marking works on flash-lite (the main discriminator held).
