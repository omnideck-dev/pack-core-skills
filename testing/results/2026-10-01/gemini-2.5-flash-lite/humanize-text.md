---
skill: humanize-text
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# humanize-text — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | De-AI the productivity article | 3 | 3 | Both kept the tells; taxonomy didn't transfer |
| 2 | Human-but-rough draft | 4 | 9 | Baseline formalized; treatment preserved casual register |
| 3 | Technical passage w/ hedges | 8 | 8 | Both fine |

## Trigger probes

- **Positive/negative:** not run — framing instability ("tool not found" refusals).

## Wrongness notes

- **T1: the tells taxonomy did not transfer** — treatment kept "In today's fast-paced world", the rule-of-three (converted to a numbered list!), "unlock your full potential". flash-lite can't apply an 8-category pattern checklist.
- **T2: the register rule DID transfer** when emphasized explicitly ("CASUAL STAYS CASUAL") — treatment kept the lowercase casual message nearly untouched (correct abstention); baseline formalized it.
- Ratio 1.33, driven entirely by T2.

## Verdict

- **Fail** — treatment avg 6.67 vs baseline avg 5.0 (ratio 1.33 < 2.0; pct_of_max 66.7%).
- Marginal value: treatment avg 6.67 vs baseline avg 5.0

## Refinements

- [ ] The full tells checklist is too much for weak models; the register rule alone is what sticks. Consider a simplified 2-rule version (remove AI-isms; never change register).
