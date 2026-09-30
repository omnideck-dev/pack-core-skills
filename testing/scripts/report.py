#!/usr/bin/env python3
"""report.py — generate test-run reports for pack-core-skills.

Primary mode (run folder):
    python3 testing/scripts/report.py --run <run-folder>

Reads every <run-folder>/<profile-id>/<skill-id>.json and writes:

  * <run-folder>/SUMMARY.md   — human-readable run summary (run date, profiles +
                                models, skills tested, pass/refine/fail counts,
                                ranking table per skill per profile).
  * <run-folder>/report.html  — self-contained styled HTML report (inline CSS,
                                no external deps) with the same data plus
                                per-skill trial detail tables, trigger probe
                                results, a cross-profile comparison table, and
                                the exclusion-list note.

Backward-compatible mode (no --run):
    python3 testing/scripts/report.py [testing-dir]

Reads testing/results/<profile-id>/<skill-id>.json and writes:

  * testing/results/<profile-id>/REPORT.md  — per-profile ranking table
  * testing/results/COMPARISON.md           — cross-profile aggregation

Pure Python stdlib, no third-party dependencies. Exits 0 even when the folder
is empty (nothing to aggregate).
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date

# --- Constants --------------------------------------------------------------

MAX_SCORE = 10  # per-trial maximum (5 criteria x 2)
PASS_RATIO = 2.0
PASS_PCT = 70.0

# Skills out of test scope (mirrors the exclusion list in SKILL.md / README).
EXCLUDED = [
    ("create-app", "Excluded by owner decision"),
    ("generate-image", "Needs a live image generator (not present in the test environment)"),
    ("install-skill", "Added post-testing-window — pending"),
    ("visualize", "Needs a Playwright interaction pass"),
]

_YYMMDD = re.compile(r"^\d{6}$")


# --- Loading ----------------------------------------------------------------

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


# --- Verdict / helpers ------------------------------------------------------

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


def _fmt_num(value) -> str:
    if value is None:
        return "—"
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.1f}"


def _all_skills(profiles: dict) -> list:
    return sorted({sid for skills in profiles.values() for sid in skills})


def _profile_model(profile: str, skills: dict) -> str:
    return next((s.get("model", "") for s in skills.values() if s.get("model")), "")


def _verdict_counts(skills: dict) -> dict:
    counts = {"pass": 0, "needs-refinement": 0, "fail": 0, "unknown": 0}
    for record in skills.values():
        counts[_verdict(record)] = counts.get(_verdict(record), 0) + 1
    return counts


def _ranking_rows(skills: dict) -> list:
    """Return [(skill_id, baseline_avg, treatment_avg, ratio, verdict)] ranked."""
    rows = []
    for skill_id, record in skills.items():
        totals = record.get("totals") or {}
        rows.append((
            skill_id,
            totals.get("baseline_avg"),
            totals.get("treatment_avg"),
            totals.get("ratio"),
            _verdict(record),
        ))
    rows.sort(key=lambda r: (-(r[2] or 0), (r[1] or 0), r[0]))
    return rows


def _run_date(run_dir: str, profiles: dict) -> str:
    """Best-effort run date: folder basename if yymmdd, else record date, else today."""
    base = os.path.basename(os.path.normpath(run_dir))
    if _YYMMDD.match(base):
        return f"20{base[:2]}-{base[2:4]}-{base[4:6]}"
    dates = [r.get("date", "") for skills in profiles.values() for r in skills.values() if r.get("date")]
    if dates:
        return sorted(dates)[0]
    return date.today().isoformat()


# --- SUMMARY.md -------------------------------------------------------------

def write_summary(run_dir: str, profiles: dict) -> None:
    """Write <run_dir>/SUMMARY.md."""
    run_date = _run_date(run_dir, profiles)
    pids = sorted(profiles)
    skills = _all_skills(profiles)

    lines = [
        "# Skill Test Run Summary",
        "",
        f"> Run folder: `{run_dir}`",
        f"> Run date: {run_date}",
        f"> Generated: {date.today().isoformat()}",
        "",
        f"**{len(pids)} profile(s)**, **{len(skills)} skill(s) tested.**",
        "",
        "## Profiles & models",
        "",
        "| Profile | Model | Skills | Pass | Needs refinement | Fail |",
        "|---------|-------|--------|------|------------------|------|",
    ]
    for pid in pids:
        counts = _verdict_counts(profiles[pid])
        lines.append(
            f"| {pid} | {_profile_model(pid, profiles[pid]) or '—'} | {len(profiles[pid])} | "
            f"{counts['pass']} | {counts['needs-refinement']} | {counts['fail']} |"
        )
    lines += ["", "## Skills tested", ""]
    lines += [f"- `{sid}`" for sid in skills]
    lines += ["", "## Ranking (per skill per profile)", ""]
    lines.append("| Skill | " + " | ".join(pids) + " |")
    lines.append("|-------|" + "|".join(["---"] * len(pids)) + "|")
    for sid in skills:
        cells = []
        for pid in pids:
            rec = profiles[pid].get(sid)
            if rec is None:
                cells.append("—")
            else:
                totals = rec.get("totals") or {}
                cells.append(
                    f"{_fmt_num(totals.get('treatment_avg'))} "
                    f"({_fmt_ratio(totals.get('ratio'))}) {_verdict(rec)}"
                )
        lines.append(f"| {sid} | " + " | ".join(cells) + " |")
    lines.append("")

    for pid in pids:
        model = _profile_model(pid, profiles[pid])
        lines += [
            f"## {pid} ranking",
            "",
            f"> Model: {model or '—'}",
            "",
            "| Rank | Skill | Baseline | Treatment | Ratio | Tier | Verdict |",
            "|------|-------|----------|-----------|-------|------|---------|",
        ]
        for rank, (sid, ba, ta, ratio, verdict) in enumerate(_ranking_rows(profiles[pid]), 1):
            lines.append(
                f"| {rank} | {sid} | {_fmt_num(ba)} | {_fmt_num(ta)} | "
                f"{_fmt_ratio(ratio)} | {_tier(ratio)} | {verdict} |"
            )
        lines.append("")

    lines += [
        "## Notes",
        "",
        "Verdicts are recomputed from each record's `totals` and `trigger` fields per `SCHEMA.md`.",
        "",
    ]
    with open(os.path.join(run_dir, "SUMMARY.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# --- report.html ------------------------------------------------------------

def _esc(value) -> str:
    return html.escape(str(value), quote=True)


def _html_table(headers: list, rows: list) -> str:
    out = ["<table><thead><tr>"]
    out += [f"<th>{_esc(h)}</th>" for h in headers]
    out.append("</tr></thead><tbody>")
    for row in rows:
        out.append("<tr>")
        out += [f"<td>{_esc(c)}</td>" for c in row]
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def _verdict_badge(verdict: str) -> str:
    cls = {"pass": "pass", "needs-refinement": "refine", "fail": "fail", "unknown": "unknown"}.get(verdict, "unknown")
    return f'<span class="badge {cls}">{_esc(verdict)}</span>'


def write_html(run_dir: str, profiles: dict) -> None:
    """Write <run_dir>/report.html — self-contained, inline CSS, no external deps."""
    run_date = _run_date(run_dir, profiles)
    pids = sorted(profiles)
    skills = _all_skills(profiles)

    css = """
    :root { --bg:#f6f7f9; --card:#ffffff; --ink:#1c2330; --muted:#6b7280;
            --line:#e5e7eb; --accent:#2563eb; --pass:#16a34a; --refine:#d97706;
            --fail:#dc2626; --unknown:#6b7280; }
    * { box-sizing:border-box; }
    body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
           background:var(--bg); color:var(--ink); line-height:1.5; }
    .wrap { max-width:1080px; margin:0 auto; padding:32px 20px 64px; }
    header.hero { background:linear-gradient(135deg,#1e3a8a,#2563eb); color:#fff;
                  border-radius:14px; padding:28px 32px; margin-bottom:28px; }
    header.hero h1 { margin:0 0 6px; font-size:26px; }
    header.hero p { margin:2px 0; opacity:.92; font-size:14px; }
    h2 { font-size:19px; margin:34px 0 12px; padding-bottom:6px; border-bottom:2px solid var(--line); }
    h3 { font-size:16px; margin:24px 0 8px; }
    .card { background:var(--card); border:1px solid var(--line); border-radius:12px;
            padding:18px 20px; margin-bottom:18px; box-shadow:0 1px 2px rgba(0,0,0,.04); }
    table { border-collapse:collapse; width:100%; font-size:13.5px; margin:8px 0; }
    th,td { border:1px solid var(--line); padding:7px 10px; text-align:left; vertical-align:top; }
    th { background:#f1f5f9; font-weight:600; }
    tr:nth-child(even) td { background:#fafbfc; }
    code { background:#eef1f5; padding:1px 5px; border-radius:4px; font-size:12.5px; }
    .badge { display:inline-block; padding:1px 8px; border-radius:999px; font-size:11.5px;
             font-weight:600; color:#fff; }
    .badge.pass { background:var(--pass); }
    .badge.refine { background:var(--refine); }
    .badge.fail { background:var(--fail); }
    .badge.unknown { background:var(--unknown); }
    .muted { color:var(--muted); font-size:13px; }
    .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; }
    .stat { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:16px; }
    .stat .num { font-size:26px; font-weight:700; }
    .stat .lbl { color:var(--muted); font-size:12.5px; text-transform:uppercase; letter-spacing:.04em; }
    .excl { background:#fff7ed; border:1px solid #fed7aa; border-radius:10px; padding:14px 18px; }
    .excl ul { margin:6px 0 0; padding-left:20px; }
    .trial-detail { margin:10px 0 0; }
    .trial-detail summary { cursor:pointer; font-weight:600; color:var(--accent); }
    footer { margin-top:40px; color:var(--muted); font-size:12.5px; text-align:center; }
    """

    parts = [
        "<!DOCTYPE html>",
        '<html lang="en"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>Skill Test Run — " + _esc(run_date) + "</title>",
        "<style>" + css + "</style></head><body><div class='wrap'>",
        "<header class='hero'>",
        "<h1>Skill Test Run Report</h1>",
        f"<p>Run folder: <code>{_esc(run_dir)}</code></p>",
        f"<p>Run date: {_esc(run_date)} · Generated: {_esc(date.today().isoformat())}</p>",
        f"<p>{len(pids)} profile(s) · {len(skills)} skill(s) tested</p>",
        "</header>",
    ]

    # Overview stats
    total_pass = total_refine = total_fail = 0
    for pid in pids:
        c = _verdict_counts(profiles[pid])
        total_pass += c["pass"]; total_refine += c["needs-refinement"]; total_fail += c["fail"]
    parts.append("<div class='grid'>")
    for lbl, num in (("Profiles", len(pids)), ("Skills tested", len(skills)),
                     ("Pass", total_pass), ("Needs refinement", total_refine), ("Fail", total_fail)):
        parts.append(f"<div class='stat'><div class='num'>{num}</div><div class='lbl'>{_esc(lbl)}</div></div>")
    parts.append("</div>")

    # Profiles & models
    parts.append("<h2>Profiles &amp; models</h2><div class='card'>")
    rows = []
    for pid in pids:
        c = _verdict_counts(profiles[pid])
        rows.append((pid, _profile_model(pid, profiles[pid]) or "—", len(profiles[pid]),
                     c["pass"], c["needs-refinement"], c["fail"]))
    parts.append(_html_table(["Profile", "Model", "Skills", "Pass", "Needs refinement", "Fail"], rows))
    parts.append("</div>")

    # Skills tested
    parts.append("<h2>Skills tested</h2><div class='card'>")
    parts.append("<p class='muted'>" + ", ".join(f"<code>{_esc(s)}</code>" for s in skills) + "</p>")
    parts.append("</div>")

    # Cross-profile comparison
    parts.append("<h2>Comparison across profiles</h2><div class='card'>")
    parts.append("<p class='muted'>Rows = skills, columns = profiles. Cells show treatment average and verdict.</p>")
    cmp_rows = []
    for sid in skills:
        cells = []
        for pid in pids:
            rec = profiles[pid].get(sid)
            if rec is None:
                cells.append("—")
            else:
                totals = rec.get("totals") or {}
                cells.append(f"{_fmt_num(totals.get('treatment_avg'))} {_verdict_badge(_verdict(rec))}")
        cmp_rows.append([f"<code>{_esc(sid)}</code>"] + cells)
    parts.append(_html_table(["Skill"] + pids, cmp_rows))
    parts.append("</div>")

    # Per-profile sections with ranking + trial details + trigger probes
    for pid in pids:
        model = _profile_model(pid, profiles[pid])
        parts.append(f"<h2>{_esc(pid)}</h2><div class='card'>")
        parts.append(f"<p class='muted'>Model: {_esc(model) or '—'}</p>")
        rank_rows = []
        for rank, (sid, ba, ta, ratio, verdict) in enumerate(_ranking_rows(profiles[pid]), 1):
            rank_rows.append((rank, f"<code>{_esc(sid)}</code>", _fmt_num(ba), _fmt_num(ta),
                              _fmt_ratio(ratio), _tier(ratio), _verdict_badge(verdict)))
        parts.append(_html_table(["Rank", "Skill", "Baseline", "Treatment", "Ratio", "Tier", "Verdict"], rank_rows))

        # Trial detail tables + trigger probes per skill
        for sid in sorted(profiles[pid]):
            rec = profiles[pid][sid]
            trials = rec.get("trials") or []
            trigger = rec.get("trigger") or {}
            parts.append(f"<details class='trial-detail'><summary>{_esc(sid)} — trials &amp; probes</summary>")
            if trials:
                t_rows = []
                for t in trials:
                    t_rows.append((t.get("id", ""), t.get("task", ""),
                                   _fmt_num(t.get("baseline_score")),
                                   _fmt_num(t.get("treatment_score")),
                                   t.get("notes", "") or "—"))
                parts.append(_html_table(["#", "Task", "Baseline", "Treatment", "Notes"], t_rows))
            else:
                parts.append("<p class='muted'>No trial records.</p>")
            pos = trigger.get("positive", "—")
            neg = trigger.get("negative", "—")
            parts.append(
                "<p>Trigger probes — positive: "
                + _verdict_badge("pass" if pos == "pass" else "fail")
                + " · negative: "
                + _verdict_badge("pass" if neg == "pass" else "fail")
                + "</p>"
            )
            parts.append("</details>")
        parts.append("</div>")

    # Exclusion list note
    parts.append("<h2>Exclusion list</h2><div class='excl'>")
    parts.append("<p><strong>Out of test scope.</strong> These skills are excluded and were not run:</p><ul>")
    for sid, reason in EXCLUDED:
        parts.append(f"<li><code>{_esc(sid)}</code> — {_esc(reason)}</li>")
    parts.append("</ul></div>")

    parts.append("<footer>Generated by testing/scripts/report.py · pure stdlib · "
                 "verdicts recomputed from totals &amp; trigger per SCHEMA.md</footer>")
    parts.append("</div></body></html>")

    with open(os.path.join(run_dir, "report.html"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts) + "\n")


# --- Backward-compatible mode (testing/results) -----------------------------

def write_profile_report(profile: str, skills: dict, out_path: str) -> None:
    """Write a single profile's ranking REPORT.md."""
    rows = _ranking_rows(skills)
    model = _profile_model(profile, skills)
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
            f"| {rank} | {skill_id} | {_fmt_num(baseline_avg)} | {_fmt_num(treatment_avg)} | "
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
    all_skills = _all_skills(profiles)
    profile_ids = sorted(profiles)
    lines = [
        "# Cross-Profile Comparison",
        "",
        f"> Aggregated across {len(profile_ids)} profile(s) · generated {date.today().isoformat()}",
        "> Cells are **treatment averages**. The baseline average per profile is in its own REPORT.md.",
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
                cells.append(_fmt_num(ta))
        lines.append(f"| {skill_id} | " + " | ".join(cells) + " |")
    lines += ["", "## Pass counts per profile", ""]
    for pid in profile_ids:
        pass_count = sum(1 for r in profiles[pid].values() if _verdict(r) == "pass")
        lines.append(f"- **{pid}**: {pass_count}/{len(profiles[pid])} skills passing")
    lines.append("")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# --- main -------------------------------------------------------------------

def main(argv: list) -> int:
    parser = argparse.ArgumentParser(
        description="Generate test-run reports for pack-core-skills.",
    )
    parser.add_argument(
        "--run", metavar="RUN_FOLDER",
        help="Run folder (e.g. <skills-dir>/test/260930). Writes SUMMARY.md + report.html there.",
    )
    parser.add_argument(
        "testing_dir", nargs="?", default=None,
        help="[backward compat] testing/ dir; writes results/<profile>/REPORT.md + results/COMPARISON.md.",
    )
    args = parser.parse_args(argv)

    if args.run:
        run_dir = os.path.abspath(args.run)
        if not os.path.isdir(run_dir):
            print(f"ERROR: run folder does not exist: {run_dir}", file=sys.stderr)
            return 1
        profiles = load_results(run_dir)
        if not profiles:
            print(f"No result JSON files found under {run_dir}; nothing to aggregate.")
            return 0
        write_summary(run_dir, profiles)
        print(f"wrote {os.path.join(run_dir, 'SUMMARY.md')} ({len(profiles)} profile(s))")
        write_html(run_dir, profiles)
        print(f"wrote {os.path.join(run_dir, 'report.html')}")
        return 0

    # Backward-compatible mode.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    testing_dir = os.path.abspath(args.testing_dir) if args.testing_dir else os.path.dirname(script_dir)
    results_dir = os.path.join(testing_dir, "results")
    profiles = load_results(results_dir)
    if not profiles:
        print(f"No result JSON files found under {results_dir}; nothing to aggregate.")
        return 0
    for profile, skills in profiles.items():
        out_path = os.path.join(results_dir, profile, "REPORT.md")
        write_profile_report(profile, skills, out_path)
        print(f"wrote {out_path} ({len(skills)} skills)")
    comparison_path = os.path.join(results_dir, "COMPARISON.md")
    write_comparison(profiles, comparison_path)
    print(f"wrote {comparison_path} ({len(profiles)} profiles)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))