# pack-core-skills

General-purpose creation, review, and writing skills for Omnideck — a portable
kit of 22 `SkillRecord` skills (create-*, review-*, write-*, make-*, research,
visualize, and more).

A pack in the Open Pack Format (OPF). A pack is a manifest plus embedded
files, containing one or more items: skills, tools, data, routines, or
artifacts. Packs install, update, and remove with zero native harness code.

See `spec/opf-spec-v1.md` in the opf-core repository for the format.

## Contents

- `manifest.json` — the OPF v1 manifest.
- `skills/<name>/SKILL.md` — the 22 skills in the standard Agent Skills
  format (agentskills.io): YAML frontmatter (`name`, `description`, and
  `metadata.tool_categories` — a comma-separated list Omnideck reads to
  grant tool categories; any other harness can ignore that key) plus a
  markdown body as the prompt. This is a harness-agnostic format by
  design — any Agent-Skills-compatible harness can load these directly,
  not just Omnideck.
- `.github/workflows/scan.yml`, `.gitlab-ci.yml` — CI scanning, already wired
  to opf-core's validator and scan template. No setup needed.
- `hooks/pre-commit` — a local pre-commit security scan (fast feedback, not
  a substitute for CI - see below).

## Skills

| Skill | Purpose |
|---|---|
| `review-code` | Correctness-focused review of code changes |
| `write-code` | Write, edit, run, and debug code in the virtual computer |
| `write-drafts` | Compose complete short-form drafts |
| `humanize-text` | Remove AI tells from writing |
| `resolve-recipient` | Resolve and verify recipients before sending |
| `personal-context` | Pull relevant memory before acting |
| `improve` | Reflect on a conversation and turn lessons into artifacts |
| `create-skill` | Create high-quality, well-scoped skills |
| `create-agent` | Create agent profiles |
| `create-tool` | Create custom tools |
| `create-app` | Create and manage Omnideck Custom Apps |
| `install-skill` | Install Agent Skills from any source |
| `write-docs` | Write and maintain technical documentation |
| `research` | Multi-source research with provenance |
| `plan-learning` | Build spaced-repetition learning plans |
| `make-docs` | Create and edit Word-style documents (.docx) |
| `make-sheets` | Create, edit, analyze, and chart spreadsheets |
| `make-slides` | Create and edit presentations |
| `make-pdfs` | Read, create, modify, and verify PDFs |
| `generate-image` | Generate or edit images with deliberate craft |
| `draw-charts` | Create data visualizations |
| `visualize` | Build interactive diagrams and simulations as HTML |

See `skills/REJECTED.md` for skills that have been considered and rejected,
with the reasoning — so they don't get re-added without new evidence.

## Install

Install this pack with the `pack-install` skill, or `scripts/install-pack.sh`
for a harness that runs scripts but not skills - never by copying this folder
by hand. If `manifest.json` declares `dependencies`, only `pack-install`
resolves the closure (installing each one first, in order, per spec Section
4.5); `install-pack.sh` alone does not - it installs only this pack and prints
a `NOTE` about the skipped dependencies. Either way requires opf-core's
tooling to be reachable by your harness (a checkout, with `OPF_CORE` set if
your harness needs it) - see opf-core's own README for that one-time setup. If
a dependency's skills don't show up after install, run `pack-doctor` to
diagnose why.

This pack has no `install.sh` lifecycle script - there's nothing harness-
specific to do. Each skill is a plain `SKILL.md`, so the generic Agent Skills
install step (reading `skills/<name>/SKILL.md`, registering it however the
target harness needs) is all any harness, Omnideck included, requires. An
Omnideck harness reads `metadata.tool_categories` from the frontmatter to
grant tool categories; a harness with no such concept just ignores that key.

## Validate

```
scripts/validate-pack.sh .
```

## Enable the pre-commit hook

Not automatic - git never reads `hooks/` on its own. Once per clone:

```
git config core.hooksPath hooks
```

This runs `validate-pack.sh` plus, where installed, `gitleaks` and the curated
semgrep ruleset before each commit, refusing it on an error-class finding. It
degrades gracefully (a NOTE, not a failure) for whatever isn't installed or
configured, and it's bypassed by `git commit --no-verify`. It's convenience
and fast feedback, not the enforced gate - that's CI. Run
`scripts/pack-doctor.sh` after cloning this pack if you're not sure whether
this is set.

## Testing

This pack ships a reproducible, deterministic skill-testing program in
[`testing/`](testing/README.md). It runs a strict A/B protocol — per skill,
baseline (skill not loaded) vs treatment (skill loaded) trials scored on a
rubric, plus trigger probes — to measure each skill's marginal value.

- **`testing/TESTING-PLAN.md`** — the A/B protocol and per-skill test specs.
- **`testing/SCHEMA.md`** — the JSON result schema and scoring rubric, pinned for
  cross-agent comparability.
- **`testing/fixtures/`** — reproducible, checksummed task seeds with
  `GROUND-TRUTH.md` anchors (immutable; see `fixtures/SHA256SUMS`).
- **`testing/scripts/report.py`** — regenerates per-profile `REPORT.md` and the
  cross-profile `COMPARISON.md`.
- **`testing/results/`** — testing results by date.

The **`test-skills`** skill (`skills/test-skills/SKILL.md`) teaches any agent how
to run the program. Five skills are out of test scope (`create-app`,
`generate-image`, `install-skill`, `visualize`, `review-security`); the reasons are documented in
`testing/README.md` and the skill itself.
