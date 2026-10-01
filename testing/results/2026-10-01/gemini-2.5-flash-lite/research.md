---
skill: research
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# research — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Latest stable Python | 3 | 7 | Baseline REFUSED entirely; treatment answered w/ dated caveat |
| 2 | SQLite vs PostgreSQL | 7 | 8 | Treatment: per-claim confidence + context engagement |
| 3 | JavaScript original name | 5 | 7 | Treatment: confidence + dating |

## Trigger probes

- **Positive/negative:** not run — no web tools in this profile; probes moot.

## Wrongness notes

- **The skill's biggest effect: getting the model to answer at all.** Baseline T1 refused ("I cannot provide real-time information") when a training-knowledge answer with caveats was available. Treatment answered with honest dating.
- flash-lite has no web access in this harness — trials test knowledge discipline only.
- No fabricated sources in either condition.
- Ratio 1.47.

## Verdict

- **Fail** — treatment avg 7.33 vs baseline avg 5.0 (ratio 1.47 < 2.0; pct_of_max 73.3%).
- Marginal value: treatment avg 7.33 vs baseline avg 5.0

## Refinements

- [ ] The "answer from training knowledge with caveats" permission is what weak models need most — they over-refuse.
