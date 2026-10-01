# pack-core-skills

General-purpose creation, review, and writing skills for Omnideck — a portable
kit of 24 `SkillRecord` skills (create-*, review-*, write-*, make-*, research,
visualize, and more) vendored from the upstream
[`rlnorthcutt/core-skills`](https://github.com/rlnorthcutt/core-skills) repo.

A pack in the Open Pack Format (OPF). A pack is a manifest plus embedded
files, containing one or more items: skills, tools, data, routines, or
artifacts. Packs install, update, and remove with zero native harness code.

See `spec/opf-spec-v1.md` in the opf-core repository for the format.

## Contents

- `manifest.json` — the OPF v1 manifest.
- `skills/<name>/skill.json` — the 24 vendored skills in Omnideck's
  `SkillRecord` JSON format (`id`, `name`, `description`, `prompt`,
  `tool_categories`). `install-skill/` also carries its `SKILL.md`.
- `data/upstream/` — provenance copy of the upstream repo's
  `scripts/install.sh` and `scripts/validate.py`, preserved verbatim.
- `.github/workflows/scan.yml`, `.gitlab-ci.yml` — CI scanning, already wired
  to opf-core's validator and scan template. No setup needed.
- `hooks/pre-commit` — a local pre-commit security scan (fast feedback, not
  a substitute for CI - see below).

## Skills

| Skill | Purpose |
|---|---|
| `review-code` | Correctness-focused review of code changes |
| `review-security` | Security-focused review of code changes |
| `simplify-code` | Quality cleanup of changed code |
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

`install.sh` copies each vendored `skill.json` into the live skills directory
(`$OMNIDECK_SKILLS_DIR`, else `/var/lib/omnideck/skills`, else
`~/.claude/skills`). It is **idempotent and non-destructive**: a skill that is
already installed live is reported and skipped, never overwritten. The live
catalog is authoritative for already-installed skills (several live copies are
newer than the vendored ones), so re-running install never clobbers them.

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
- **`testing/results-archive/`** — the historical single-model baseline record.

The **`test-skills`** skill (`skills/test-skills/SKILL.md`) teaches any agent how
to run the program. Four skills are out of test scope (`create-app`,
`generate-image`, `install-skill`, `visualize`); the reasons are documented in
`testing/README.md` and the skill itself.

## Upstream provenance

This pack vendors the skills from
[`rlnorthcutt/core-skills`](https://github.com/rlnorthcutt/core-skills) at
commit `62627d980db797afebcb4b52f3847c127d9815a4` (2026-09-12). The vendored
`skill.json` files are the clean, Omnideck-optimized implementations from the
upstream `skills/` directory; `data/upstream/` preserves the upstream
`scripts/` verbatim for reference. The upstream repo's own `README.md`
describes the skill catalog and rollout waves.