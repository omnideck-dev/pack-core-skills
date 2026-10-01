---
skill: create-tool
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 5
---

# create-tool — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Text stats tool | 9 | 9 | Both tested happy+failure |
| 2 | CSV→JSON (existing-tools check) | 7 | 10 | Baseline skipped the check; treatment checked registry first |
| 3 | Config validator + idempotency | 9 | 9 | Both verified |
| 4 | File checksums | 9 | 9 | Both documented + tested |
| 5 | Directory stats | 9 | 9 | Both clean errors |

## Trigger probes

- **Positive:** pass — reusable-tool request loaded create-tool
- **Negative:** pass — one-off script request did not

## Wrongness notes

- All 10 runs produced working, tested tools with clean error handling and JSON contracts. The only gap: baseline skipped the existing-tools check on T2 (built a duplicate instead of composing).
- Ratio 1.07.

## Verdict

- **Fail** — treatment avg 9.2 vs baseline avg 8.6 (ratio 1.07 < 2.0; pct_of_max 92%).
- Marginal value: treatment avg 9.2 vs baseline avg 8.6

## Refinements

- [ ] The existing-tools check (R1) is the only differentiating behavior; baselines skip it.
