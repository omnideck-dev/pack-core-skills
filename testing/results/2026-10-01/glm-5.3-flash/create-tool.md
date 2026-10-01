---
skill: create-tool
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 5
---

# create-tool — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Text stats tool | 6 | 10 | Baseline: partial failure handling |
| 2 | CSV→JSON (existing-tools check) | 5 | 10 | Treatment checked registry + stdlib first |
| 3 | Config validator + idempotency | 8 | 10 | Treatment: JSON error contract |
| 4 | File checksums | 5 | 10 | Baseline: raw stack trace |
| 5 | Directory stats | 4 | 10 | Baseline: nonexistent dir silently "succeeded" |

## Trigger probes

- **Positive:** pass — reusable-tool request loads create-tool
- **Negative:** pass — one-off script does not

## Wrongness notes

- **glm baselines have real failure-path defects**: T4 crashed with a raw FileNotFoundError traceback; T5 returned a misleading empty-success (exit 0) for a nonexistent directory; T2 silently returned `[]` for empty input. All fixed in treatment with clean JSON error contracts.
- Treatment T2 checked the tool registry, CLI alternatives (csvkit), and stdlib coverage before building — the R1 behavior.
- Treatment consistently parameterizes via stdin-JSON with documented interfaces; baselines use ad-hoc argv and no docs.
- Ratio 1.79 — biggest create-tool gap; failure-path discipline is load-bearing for this model.

## Verdict

- **Fail** — treatment avg 10.0 vs baseline avg 5.6 (ratio 1.79 < 2.0; pct_of_max 100%).
- Marginal value: treatment avg 10.0 vs baseline avg 5.6

## Refinements

- [ ] Strongest create-tool signal of the batch — failure-path discipline and interface documentation.
