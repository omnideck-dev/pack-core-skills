---
skill: review-code
profile: 0c6e7e6c9e12
model: google/gemini-2.5-flash-lite
date: 2026-10-01
trials: 3
---

# review-code — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Review inventory-service change | 4 | 7 | Baseline hallucinated APIs; treatment read real code |
| 2 | Same | 2 | 7 | Baseline flagged the TOCTOU trap as Critical; treatment avoided it |
| 3 | Same | 5 | 7 | Baseline invented findings; treatment solid |

## Trigger probes

- **Positive:** pass — review request → review-code
- **Negative:** fail — debugging request ALSO mapped to review-code (model doesn't distinguish review from debugging)

## Wrongness notes

- **The weak-model hypothesis confirmed**: baselines hallucinate API details (invented `skus_to_fulfill` dicts, `low_stock_threshold` params, "missing docstrings" that exist), miss planted bugs, and one baseline flagged the TOCTOU trap as a Critical race condition — the exact false positive the skill warns against.
- Treatment runs read the actual code (correct line numbers, quoted snippets), found ZeroDivisionError + O(n²) + non-atomicity, avoided the trap, and followed the skill's output format.
- Ratio 1.91 — just under the 2.0 bar. pct_of_max exactly 70%.
- Protocol note: run one pass per spawn (multi-pass tasks return empty output on this model).

## Verdict

- **Needs refinement** — treatment avg 7.0 vs baseline avg 3.67 (ratio 1.91 < 2.0; pct_of_max 70%). Numerically ok but ratio just misses; negative trigger failed.
- Marginal value: treatment avg 7.0 vs baseline avg 3.67 — the largest gap of any profile; the skill nearly doubles review quality on the weak model.

## Refinements

- [ ] Trigger description should explicitly exclude debugging requests ("review a diff/PR, not debug").
- [ ] This is the profile where the skill earns its keep — consider pass-rule calibration for weak models.
