#!/usr/bin/env python3
"""report.py — regenerate testing reports for pack-core-skills.

Reads every testing/results/<profile-id>/<skill-id>.json and emits:

  * testing/results/<profile-id>/REPORT.md   — per-profile ranking table
  * testing/results/COMPARISON.md            — cross-profile aggregation

Pure Python stdlib, no third-party dependencies. Exits 0 even when the results
directory is empty (nothing to aggregate).

Usage:
    python3 testing/scripts/report.py [testing-dir]

The testing-dir argument defaults to the directory containing this script's
parent (i.e. <pack>/testing). It can be overridden for testing.
"""

from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import date

# --- Paths -----------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TESTING_DIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(SCRIPT_DIR)
RESULTS_DIR = os.path.join(TESTING_DIR, "results")

MAX_SCORE = 10  # per-trial maximum (5 criteria x 2)
PASS_RATIO = 2.0
PASS_PCT = 70.0


def load_results(results_dir: str) -> dict:
    """Return {profile_id: {skill_id: record}} from all *.json result files."""
    profiles: dict = {}
    if not os.path.isdir(results_dir):
        return profiles
    for profile in sorted(os.listdir(results_dir)):
        pdir = os.path.join(results_dir, profile)
        if not os.path.isdir(pdir):
            continue
        skills: dict = {}
        for fname in sorted(os.listdir(pdir)):
            if not fname.endswith(".json"):
                continue
            path = os.path.join(pdir, fname)
            try:
                with open(path, encoding="utf-8") as fh:
                    record = json.load(fh)
            except (OSError, ValueError) as exc:
                print(f"WARNING: skipping unreadable/invalid JSON {path}: {exc}", file=sys.stderr)
                continue
            skill_id = record.get("skill") or os.path.splitext(fname)[0]
            skills[skill_id] = record
        if skills:
            profiles[profile] = skills
    return profiles


def _verdict(record: dict) -> str:
    """Recompute the verdict from a record's totals + trigger probes."""
    totals = record.get("totals") or {}
    trigger = record.get("trigger") or {}
    treatment_avg = totals.get("treatment_avg")
    baseline_avg = totals.get("baseline_avg")
    pct_of_max = totals.get("pct_of_max")
    if treatment_avg is None or baseline_avg is None or pct_of_max is None:
        return "unknown"
    if baseline_avg == 0:
        num_ok = treatment_avg > 0 and pct_of_max >= PASS_PCT
    else:
        num_ok = treatment_avg >= PASS_RATIO * baseline_avg and pct_of_max >= PASS_PCT
    triggers_ok = trigger.get("positive") == "pass" and trigger.get("negative") == "pass"
    if num_ok and triggers_ok:
        return "pass"
    if num_ok and not triggers_ok:
        return "needs-refinement"
    return "fail"


def _tier(ratio) -> str:
    """Classify a ratio into a tier, mirroring the historical report."""
    if ratio is None:
        return "—"
    if ratio >= 10:
        return "Capability"
    if ratio >= 2.5:
        return "Discipline"
    return "Craft"


def _fmt_ratio(ratio) -> str:
    if ratio is None:
        return "∞"
    return f"{ratio:.1f}×"


def write_profile_report(profile: str, skills: dict, out_path: str) -> None:
    """Write a single profile's ranking REPORT.md."""
    rows = []
    for skill_id, record in skills.items():
        totals = record.get("totals") or {}
        baseline_avg = totals.get("baseline_avg")
        treatment_avg = totals.get("treatment_avg")
        ratio = totals.get("ratio")
        verdict = _verdict(record)
        rows.append((skill_id, baseline_avg, treatment_avg, ratio, verdict))
    # Rank by treatment_avg desc, then baseline_avg asc, then name.
    rows.sort(key=lambda r: (-(r[2] or 0), (r[1] or 0), r[0]))

    model = next((s.get("model", "") for s in skills.values() if s.get("model")), "")
    lines = [
        f"# {profile} — Testing Report",
        "",
        f"> Profile `{profile}`{(' (' + model + ')') if model else ''} · generated {date.today().isoformat()}",
        f"> {len(skills)} skill(s) · per-skill records in `results/{profile}/`",
        "",
        "## Ranking (treatment avg / baseline avg)",
        "",
        "| Rank | Skill | Baseline | Treatment | Ratio | Tier | Verdict |",
        "|------|-------|----------|-----------|-------|------|---------|",
    ]
    for rank, (skill_id, baseline_avg, treatment_avg, ratio, verdict) in enumerate(rows, 1):
        lines.append(
            f"| {rank} | {skill_id} | {baseline_avg if baseline_avg is not None else '—'} | "
            f"{treatment_avg if treatment_avg is not None else '—'} | "
            f"{_fmt_ratio(ratio)} | {_tier(ratio)} | {verdict} |"
        )

    pass_count = sum(1 for r in rows if r[4] == "pass")
    lines += [
        "",
        f"**Pass count:** {pass_count}/{len(rows)}",
        "",
        "Verdicts are recomputed from each record's `totals` and `trigger` fields per `SCHEMA.md`.",
        "",
    ]
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def write_comparison(profiles: dict, out_path: str) -> None:
    """Write the cross-profile COMPARISON.md."""
    # Rows = skills, columns = profiles, cells = treatment avg.
    all_skills = sorted({sid for skills in profiles.values() for sid in skills})
    profile_ids = sorted(profiles)

    lines = [
        "# Cross-Profile Comparison",
        "",
        f"> Aggregated across {len(profile_ids)} profile(s) · generated {date.today().isoformat()}",
        f"> Cells are **treatment averages**. The baseline average per profile is in its own REPORT.md.",
        "",
        "## Treatment averages by skill",
        "",
        "| Skill | " + " | ".join(profile_ids) + " |",
        "|-------|" + "|".join(["---"] * len(profile_ids)) + "|",
    ]
    for skill_id in all_skills:
        cells = []
        for pid in profile_ids:
            record = profiles[pid].get(skill_id)
            if record is None:
                cells.append("—")
            else:
                ta = (record.get("totals") or {}).get("treatment_avg")
                cells.append(str(ta) if ta is not None else "—")
        lines.append(f"| {skill_id} | " + " | ".join(cells) + " |")

    lines += ["", "## Pass counts per profile", ""]
    for pid in profile_ids:
        pass_count = sum(1 for r in profiles[pid].values() if _verdict(r) == "pass")
        lines.append(f"- **{pid}**: {pass_count}/{len(profiles[pid])} skills passing")
    lines.append("")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main() -> int:
    profiles = load_results(RESULTS_DIR)
    if not profiles:
        print(f"No result JSON files found under {RESULTS_DIR}; nothing to aggregate.")
        return 0

    for profile, skills in profiles.items():
        out_path = os.path.join(RESULTS_DIR, profile, "REPORT.md")
        write_profile_report(profile, skills, out_path)
        print(f"wrote {out_path} ({len(skills)} skills)")

    comparison_path = os.path.join(RESULTS_DIR, "COMPARISON.md")
    write_comparison(profiles, comparison_path)
    print(f"wrote {comparison_path} ({len(profiles)} profiles)")
    return 0


if __name__ == "__main__":
    sys.exit(main())