---
skill: write-docs
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# write-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | README for csvsum.py | 5 | 6 | Baseline: invented MIT license, untested claims; treatment: honest license placeholder but wrong example outputs |
| 2 | API reference | 8 | 8 | Carried at parity |
| 3 | Correct stale doc claims | 9 | 9 | Both caught the falsehoods |

## Trigger probes

- **Positive/negative:** not run — framing instability.

## Wrongness notes

- Baseline invented a MIT License; treatment used an honest "[Specify License Here]" placeholder — the no-invented-content rule transferred.
- Treatment's example outputs didn't match reality (claimed 9 rows/mean 155.0; actual 8/157.14) despite claiming verification — flash-lite's "verification" is unreliable.
- T3 (stale-claim correction) solid in both conditions.
- Ratio 1.05.

## Verdict

- **Fail** — treatment avg 7.67 vs baseline avg 7.33 (ratio 1.05 < 2.0; pct_of_max 76.7%).
- Marginal value: treatment avg 7.67 vs baseline avg 7.33

## Refinements

- [ ] Weak models claim verification they didn't perform — docs skill should require pasting raw command output as proof.
