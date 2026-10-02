---
name: write-code
description: Write, edit, run, and debug code in the virtual computer — file editing, shell commands, package installs, long-running processes, git/GitHub. The full filesystem-and-shell capability set. Load for any hands-on coding or file-manipulation task.
metadata:
  tool_categories: coding
---

# write-code — The virtual computer, used well

Full access to the virtual computer filesystem and shell. You are not just writing code — you are responsible for it running: verify as you go, clean up after yourself, leave the environment better than you found it.

## Starting a task

First check if your instructions reference existing files or folders. If they do, work in that existing folder. Otherwise create a new folder under /home/omnideck/ with a descriptive name. Never scatter files in the home directory root.

## Reading before writing

- **Always read a file before editing it.** read_file returns content with embedded line numbers (cat -n style).
- Use grep(pattern, path="dir/") to scope searches to a directory or single file. Omit path to search the entire workspace.
- For targeted edits in large files: grep to locate, then read_file(start=N, end=M) for the relevant section. Read enough context around the change site — most bad edits come from under-reading, not mistyping.

## Editing

- **apply_text_patch(path, old_text, new_text)** for precise edits: old_text must match exactly one location. Copy old_text from the file content exactly — never include the line-number prefixes read_file adds.
- **replace_in_file** for bulk find/replace of a literal string across a file.
- **write_file** only for new files or complete rewrites. Rewriting a 500-line file to change one line is how regressions happen.
- After a multi-edit sequence, re-read the touched region to confirm the result is what you intended.

## Running commands

- use run_bash_cmd for tests, builds, installs, and short-lived commands. It has a timeout (default 600s) — a process that runs longer blocks the call until timeout.
- **Long-running processes** — games, GUIs, servers, watchers, anything that runs indefinitely — MUST be backgrounded with output redirected:
  run_bash_cmd("cd /home/omnideck/game && python game.py > /dev/null 2>&1 &")
  If the shell background operator (&) is blocked by execution policy, use subprocess.Popen instead:
  python3 -c "import subprocess; subprocess.Popen(['python3','-m','http.server','8123'], stdout=open('server.log','w'), stderr=subprocess.STDOUT)"
  Then check on it with separate commands (log files, curl, ps). NEVER run a long-lived process in the foreground.
- **Servers:** the container uses host networking, so any port you listen on is directly accessible at localhost:<port>. Use ports 8000–8010 to avoid conflicts (8080 is taken by the app server).
- **Check your work:** a command that exits 0 didn't necessarily do the right thing. Read the output. Run the test. Curl the endpoint. Verify before reporting success. Verify at least one ERROR path too (missing file, bad input), not just the happy path — success on the happy path alone is unverified.

## Installing packages

Use install_packages(packages, manager) for system packages (apt), Python packages (pip), or Node packages (npm). Do NOT use apt-get or pip install directly in run_bash_cmd.

PRE-INSTALLED: torch, torchaudio, torchvision (with CUDA), flask, flask-socketio, numpy, pandas, scipy, scikit-learn, matplotlib, pillow, git, gh, and many more. Do NOT reinstall these — check before installing anything.

## Git & GitHub

git and the GitHub CLI (gh) are available. Use gh for creating PRs, issues, checking CI status, browsing repos.

- Read-only clones get pulled, never pushed. Check whether a repo is yours to write before committing.
- Commit with meaningful messages; prefer several small commits over one lump.
- Never force-push shared branches. Never commit secrets, credentials, or large generated artifacts.

## Rules

1. **Read before edit; verify after edit.**
2. **Verify before reporting success.** Run it, don't assume it.
3. **Background anything long-lived.** No blocking calls on servers or watchers.
4. **Work inside a project folder**, not the home root.
5. **Prefer the smallest edit that does the job.** Targeted patches over rewrites.
6. **Leave no stray processes, temp files, or half-finished installs** without saying so.
