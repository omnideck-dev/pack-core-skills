---
skill: write-code
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# write-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | CSV summary CLI | 7 | 9 | Treatment tested error path; both verified by orchestrator |
| 2 | Targeted edit: get_timeout() | 9 | 5 | Treatment's patch DELETED get_log_level() (replaced instead of added) |
| 3 | Flask health server | 5 | 7 | Baseline: confabulated port blocker, never verified; treatment: verified but stop failed (honest report) |

## Trigger probes

- **Positive/negative:** not run — default capability skill.

## Wrongness notes

- **Model instability dominates**: baseline T1 first attempt returned empty output; baseline T3 wrote correct code then confabulated a port-8080 blocker and never verified; treatment T2's targeted patch matched the wrong location and deleted an existing function.
- Treatment T3 honestly reported its cleanup failure (didn't claim success) — the skill's honesty norm visible.
- Every claimed edit/execution was verified on disk by the orchestrator per protocol.
- Path quirk: this profile rewrites /tmp paths to /home/omnideck/ab/ — harness may sandbox /tmp for it.

## Verdict

- **Fail** — treatment avg 7.0 vs baseline avg 7.0 (ratio 1.0; pct_of_max 70%).
- Marginal value: treatment avg 7.0 vs baseline avg 7.0

## Refinements

- [ ] flash-lite's apply_text_patch usage is dangerous (matched wrong location, destroyed a function). The skill's "read enough context" rule didn't prevent it — consider requiring a post-edit diff check.
