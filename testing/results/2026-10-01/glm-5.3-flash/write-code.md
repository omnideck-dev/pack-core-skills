---
skill: write-code
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# write-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | CSV summary CLI | 8 | 10 | Baseline happy-path only; treatment also error path |
| 2 | Targeted edit: get_timeout() | 9 | 10 | Treatment: read-before-edit + regression check |
| 3 | Flask health server | 9 | 9 | Both killed server + verified port free |

## Trigger probes

- **Positive/negative:** not run — default capability skill, low trigger risk.

## Wrongness notes

- All 6 runs clean in isolated workspaces. No false-success claims (unlike the deepseek batch's contaminated runs).
- Treatment deltas: error-path testing (T1), regression check after edit (T2), localhost bind (T3).
- Baseline T3 had a pkill self-match hiccup but recovered and verified cleanup.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 8.67 (ratio 1.11 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 8.67

## Refinements

- [ ] Ceiling: baseline already disciplined.
