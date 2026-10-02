# Changelog

## 0.3.0

- Converted all 22 skills from Omnideck's proprietary `skill.json`
  (`SkillRecord`) format to standard `SKILL.md` (agentskills.io frontmatter +
  markdown body). The pack's skills are now harness-agnostic by default,
  matching OPF's "zero native harness code" goal — previously only
  `install-skill` and `test-skills` shipped a `SKILL.md`.
- Omnideck-specific tool-category grants now live at
  `metadata.tool_categories` (comma-separated) in the frontmatter, a
  spec-legal free-form field any other harness can ignore.
- Removed `install.sh`: it only ever copied/renamed `skill.json` into
  Omnideck's live skills directory. With plain `SKILL.md` as the source of
  truth, the generic Agent Skills install step covers it — no
  harness-specific lifecycle script is needed.
- Fixed `humanize-text`'s prompt, which had been stored with doubled escape
  sequences (literal `\n` instead of newlines) since it was authored,
  collapsing the whole prompt into one unreadable line.

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