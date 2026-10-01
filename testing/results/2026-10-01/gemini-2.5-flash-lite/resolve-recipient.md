---
skill: resolve-recipient
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# resolve-recipient — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Resolve 'Chris' (2 candidates) | 7 | 9 | Treatment showed both candidates + asked; baseline picked |
| 2 | Group inference 'the team' | 6 | 6 | Neither asked for confirmation; both invented the delay reason |
| 3 | Unambiguous Sam Rivera | 9 | 9 | Both resolve + proceed |

## Trigger probes

- **Positive/negative:** not run — framing instability.

## Wrongness notes

- T1: the ask-vs-guess discipline transferred (treatment laid out both candidates and asked).
- T2: BOTH conditions invented the delay reason ("unforeseen issues in final testing") — the no-invented-specifics rule failed in both. Neither asked for group confirmation.
- Ratio 1.09.

## Verdict

- **Fail** — treatment avg 8.0 vs baseline avg 7.33 (ratio 1.09 < 2.0; pct_of_max 80%).
- Marginal value: treatment avg 8.0 vs baseline avg 7.33

## Refinements

- [ ] The no-invented-specifics rule needs to be stated for MESSAGE BODIES too, not just recipients — both conditions fabricated the delay reason.
