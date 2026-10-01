---
skill: make-docs
profile: 1ec63e21c30b
model: z-ai/glm-5.3-flash
date: 2026-10-01
trials: 3
---

# make-docs — Test Results (2026-10-01)

## Trials

| # | Task | Baseline score | Treatment score | Notes |
|---|------|---------------|-----------------|-------|
| 1 | Create retention-policy docx | 8 | 10 | Baseline: no outline step/tables; treatment: outline-first + tables |
| 2 | Add section at correct position | 7 | 10 | Baseline appended after Contact; treatment inserted correctly + caught own bug |
| 3 | Structure inspection | 9 | 9 | Both navigable (LibreOffice unavailable — structural inspection) |

## Trigger probes

- **Positive:** pass — Word doc request loads make-docs
- **Negative:** pass — markdown README routes to write-docs

## Wrongness notes

- Baseline T2 appended the new section after Contact (wrong outline position, no repositioning); treatment inspected the structure first, inserted before Contact, and caught + fixed its own XML-ordering bug on re-read.
- Treatment T1 front-loads the purpose and renders retention periods as a table.
- Render verification: LibreOffice not installable in this environment; both fell back to structural XML inspection (honestly noted).
- Ratio 1.21.

## Verdict

- **Fail** — treatment avg 9.67 vs baseline avg 8.0 (ratio 1.21 < 2.0; pct_of_max 96.7%).
- Marginal value: treatment avg 9.67 vs baseline avg 8.0

## Refinements

- [ ] Outline-position discipline on edit is load-bearing.
- [ ] Environment gap: PDF render verification needs LibreOffice; consider documenting the structural-inspection fallback in the skill.
