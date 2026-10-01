---
skill: make-pdfs
profile: 7908f0365989
model: google/gemini-3.6-flash
date: 2026-10-01
trials: 3
---

# make-pdfs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Onboarding checklist PDF | 7 | 10 | Baseline: no visual verify; treatment: rendered + inspected |
| 2 | Extract text | 9 | 9 | Both clean; treatment adds completeness check |
| 3 | Create + merge | 8 | 10 | Treatment visually verified the merge |

## Trigger probes

- **Positive:** pass — styled PDF request loaded make-pdfs
- **Negative:** pass — image-wrap request did not

## Wrongness notes

- **Visual verification is the discriminator**: baselines deliver PDFs without rendering them to images; treatment renders and inspects before delivery (the exact R4 behavior).
- Both used source-format authoring (HTML→Chrome headless), correct page counts, stated provenance.
- Ratio 1.21.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 8.0 (ratio 1.21 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 8.0

## Refinements

- [ ] Render-verification behavior is load-bearing; baselines reliably skip it.
