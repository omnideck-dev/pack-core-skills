#!/usr/bin/env bash
#
# install.sh — pack-core-skills lifecycle script (OPF v1, spec Section 8).
#
# Idempotent. Runs with cwd = the staging copy and receives PACK_ROOT,
# PACK_NAME, PACK_DATA_DIR, PACK_VERSION, PACK_INSTALL_DIR from the harness.
# When run directly (not via the harness), it falls back to sensible defaults:
#   PACK_ROOT      -> the directory containing this script
#   PACK_DATA_DIR  -> sibling "<pack>-data" of the pack root
#
# Behavior:
#   a. Resolve the live skills directory:
#        - $OMNIDECK_SKILLS_DIR if set in the invoking env (matches the
#          upstream core-skills scripts/install.sh convention);
#        - else /var/lib/omnideck/skills (the Omnideck state skills dir).
#   b. For each skill vendored under skills/<name>/skill.json, copy it into
#      the live skills dir as <name>.json — but NEVER overwrite an existing
#      live skill. The live catalog is authoritative for already-installed
#      skills (several live copies here are newer than the vendored ones), so
#      an existing skill is reported and skipped, not clobbered. This keeps
#      install idempotent and non-destructive across repeated runs.
#   c. Echo a short summary. Exit 0.
#
set -euo pipefail

# --- Resolve harness-provided variables with sensible fallbacks ------------
PACK_ROOT="${PACK_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
PACK_NAME="${PACK_NAME:-pack-core-skills}"
PACK_VERSION="${PACK_VERSION:-0.1.0}"
PACK_DATA_DIR="${PACK_DATA_DIR:-$(dirname "$PACK_ROOT")/$PACK_NAME-data}"
PACK_INSTALL_DIR="${PACK_INSTALL_DIR:-$PACK_ROOT}"

# --- Resolve the live skills directory (step a) ----------------------------
if [[ -n "${OMNIDECK_SKILLS_DIR:-}" ]]; then
  LIVE_SKILLS="$OMNIDECK_SKILLS_DIR"
elif [[ -d "/var/lib/omnideck/skills" ]]; then
  LIVE_SKILLS="/var/lib/omnideck/skills"
else
  LIVE_SKILLS="$HOME/.claude/skills"
fi
mkdir -p "$LIVE_SKILLS"

# --- Install each vendored skill, skipping existing (step b) ---------------
installed=0
skipped=0
for skill_json in "$PACK_ROOT"/skills/*/skill.json; do
  [[ -e "$skill_json" ]] || continue
  name="$(basename "$(dirname "$skill_json")")"
  target="$LIVE_SKILLS/$name.json"
  if [[ -e "$target" ]]; then
    echo "  SKIP  $name (already installed at $target; not overwritten)"
    skipped=$((skipped + 1))
  else
    cp "$skill_json" "$target"
    echo "  INSTALL $name -> $target"
    installed=$((installed + 1))
  fi
done

# --- Summary (step c) ------------------------------------------------------
echo "pack-core-skills v$PACK_VERSION installed:"
echo "  skills installed:  $installed"
echo "  skills skipped:    $skipped (already present, left untouched)"
echo "  live skills dir:   $LIVE_SKILLS"
echo "  pack data dir:     $PACK_DATA_DIR"
exit 0