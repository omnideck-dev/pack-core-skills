---
skill: make-pdfs
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# make-pdfs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Onboarding checklist PDF | 9 | 9 | Both visually verified |
| 2 | Extract text | 9 | 9 | Both clean |
| 3 | Create + merge | 9 | 9 | Both verified |

## Trigger probes

- **Positive:** pass — styled PDF request loads make-pdfs
- **Negative:** pass — image-wrap does not

## Wrongness notes

- glm baseline ALREADY does visual verification (rendered to PNG + vision-inspected) — unlike gemini and deepseek baselines, which skipped it. No headroom for the skill.
- Both arms used tool substitutions (pypdfium2 for pdftoppm, pdfplumber for pdftotext) with honest notes; poppler not installable.
- Ratio 1.0.

## Verdict

- **Fail** — treatment avg 9.0 vs baseline avg 9.0 (ratio 1.0 < 2.0; pct_of_max 90%).
- Marginal value: treatment avg 9.0 vs baseline avg 9.0

## Refinements

- [ ] Model-dependent: visual verification is already baseline behavior for glm.
