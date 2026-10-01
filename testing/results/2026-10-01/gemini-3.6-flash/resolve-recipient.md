---
skill: resolve-recipient
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# resolve-recipient — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Resolve 'Chris' (2 candidates) | 8 | 9 | Treatment asks directly with evidence; baseline picks + notes alternative |
| 2 | Group inference 'the team' | 8 | 8 | Both ask for the roster |
| 3 | Unambiguous Sam Rivera | 9 | 9 | Both resolve + proceed without asking |

## Trigger probes

- **Positive:** pass — "send email to Dave" loaded resolve-recipient
- **Negative:** pass — informational question loaded nothing

## Wrongness notes

- Treatment slightly better on the ambiguity case (asks directly vs picks-then-notes).
- Both conditions handle the unambiguous case identically well.
- Ratio 1.04 — net wash.

## Verdict

- **Fail** — treatment avg 8.67 vs baseline avg 8.33 (ratio 1.04 < 2.0; pct_of_max 86.7%).
- Marginal value: treatment avg 8.67 vs baseline avg 8.33

## Refinements

- [ ] gemini baseline already asks appropriately; little headroom for the skill.
