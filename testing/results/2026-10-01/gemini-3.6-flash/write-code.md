---
skill: write-code
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# write-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | CSV summary CLI | 9 | 9 | Both verified happy+error paths |
| 2 | Targeted edit: get_timeout() | 9 | 9 | Both used apply_text_patch; treatment re-read after edit |
| 3 | Flask health server | 9 | 9 | Both killed server + verified port free; treatment also 404 check |

## Trigger probes

- **Positive/negative:** not run — write-code is a default capability skill; trigger risk low.

## Wrongness notes

- All 6 runs clean in isolated workspaces: project-folder discipline, verify-before-success, no stray processes (both runs killed the T3 server and confirmed the port free).
- Treatment marginal gains: re-read-after-edit (T2), error-path curl (T3). Ratio 1.0.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 9.0 (ratio 1.0 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 9.0

## Refinements

- [ ] Ceiling: baseline already follows the discipline the skill teaches.
