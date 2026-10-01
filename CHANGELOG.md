# Changelog

## 0.2.0

- Removed `review-security` and `simplify-code` skills (see `skills/REJECTED.md`).
- Removed `data/upstream/` provenance directory.
- Removed all references to the former upstream repo (rlnorthcutt/core-skills).
- This repo is now the canonical source for these skills.
- 6 skills refined from multi-model A/B testing (commit 2112038):
  review-security (diff-attribution, clean-verdict), review-code (contract-mismatch),
  plan-learning (always-deliver), research (offline fallback),
  make-slides (edit-consistency), resolve-recipient (no-invented-specifics).
- Added `testing/results/2026-10-01/` — multi-model A/B testing results
  (4 models, 73 records, HTML report, skill-refinements.md).
- Added `skills/REJECTED.md` — rejected/dismissed skills with reasoning.

## 0.1.0

- Initial release: 24 general-purpose creation/review/writing skills
  with idempotent, non-destructive install.sh.