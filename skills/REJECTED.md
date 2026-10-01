# Rejected & Dismissed Skills

Skills that have been considered for this pack and rejected or removed,
with the reasoning. Do not re-add these without new evidence that addresses
the concerns below.

---

## Removed from the pack

### review-security

**Removed:** 2026-10-01 (v0.2.0)

**Why:** Multi-model A/B testing showed the skill actively made security reviews
*worse* than not using it. The thoroughness pressure inflated severities and
suppressed correct "no findings" verdicts. On deepseek-v4-flash, the baseline
correctly identified a benign diff as clean while the treatment attributed
pre-existing gaps to the diff as Critical findings (ratio: 0.48 — treatment
worse than baseline).

The two failure modes (diff attribution and severity inflation) were fixed in
commit `2112038` and the refined skill was tested, but the average improvement
across all four models remained negative (-9%). The skill's core premise — that
a separate security-focused prompt improves security review — did not hold for
any model tested. Modern models already perform security review adequately as
part of a general correctness review, and the dedicated prompt encouraged
finding-theater over precision.

**Re-add only if:** a future model shows a specific security-review blind spot
that a targeted prompt can fix, AND the fix produces a positive improvement
across multiple models without inflating false positives.

---

### simplify-code

**Removed:** 2026-10-01 (v0.2.0)

**Why:** Multi-model A/B testing showed the skill provides zero measurable
value. On three of four models (glm-5.3-flash, gemini-3.6-flash,
deepseek-v4-flash), the baseline and treatment produced identical output —
the models already simplify code correctly without the skill. On
gemini-2.5-flash-lite, the treatment run hallucinated its entire output
(claimed edits that never happened on disk), making the comparison invalid.

The skill's four-pass methodology (reuse, simplification, efficiency,
altitude) is sound, but it describes what capable models already do
naturally. The skill added no discipline the model didn't already have.

**Re-add only if:** a future model produces demonstrably worse simplification
output without the skill (e.g. introduces behavior changes, misses obvious
consolidations), AND the skill's four-pass structure measurably improves
quality without over-correcting.

---

## Considered and rejected (never added)

### generate-image

**Status:** In the pack but excluded from testing (no live image generator in
the test environment). Not rejected — pending a testing environment with image
generation capability.

---

### install-skill

**Status:** In the pack but excluded from testing (added post-testing-window).
Not rejected — pending testing.

---

### visualize

**Status:** In the pack but excluded from testing (needs a Playwright
interaction pass — headless render alone is insufficient). Not rejected —
pending a testing environment with browser automation.

---

### create-app

**Status:** In the pack but excluded from testing (owner decision). Not
rejected — pending testing.

---

## Criteria for re-adding a removed skill

1. A specific, documented failure mode that the skill addresses.
2. A/B testing showing positive improvement across multiple models.
3. No increase in false positives or hallucination rate.
4. The improvement must be reproducible — not a single-model fluke.