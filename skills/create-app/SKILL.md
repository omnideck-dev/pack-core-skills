---
name: create-app
description: Create and manage Omnideck Custom Apps — self-contained apps in the apps directory with a manifest (omnideck.json), a web/ frontend, optional app.py backend actions, and data persistence. Use when the user asks for an app, a dashboard, a tool with a UI, or something to open in its own window.
metadata:
  tool_categories: coding
---

# create-app — Build Omnideck Custom Apps

A Custom App is a folder the server discovers automatically and shows in the UI as its own window. Structure:

```
<app-slug>/
├── omnideck.json      # manifest: {"title", "description", "icon"}
├── web/               # frontend, served at the app's URL
│   └── index.html
├── app.py             # optional: backend actions
└── data/              # optional: persistent state (create as needed)
```

## Manifest (omnideck.json)

```json
{
  "title": "Pomodoro Timer",
  "description": "Focus timer with session history.",
  "icon": "bi-clock"
}
```

- `title`: required, 1–80 chars — shown as the app's name.
- `description`: optional, ≤240 chars.
- `icon`: optional Bootstrap icon name, must match `bi-<name>` (default `bi-window`). Pick a semantically right one.

The folder name is the app's slug. The app appears in the UI when the manifest and web/index.html both exist — no registration step.

## Frontend (web/)

Plain HTML/CSS/JS, served statically. Rules:

- Reference assets by path (`assets/chart.png`), never base64-inline.
- Single-page, self-contained; no build step required to iterate.
- Talk to backend actions via the injected SDK:

```js
const result = await window.omnideck.invoke("action_name", { param: value });
window.omnideck.chat.open();                       // open the chat panel
window.omnideck.chat.compose({ text: "..." });     // pre-fill a chat message
```

- `invoke` returns a promise resolving to the action's return value, or rejecting with an error.
- The SDK is injected by the server — don't include or polyfill it.

## Backend actions (app.py) — optional

For anything needing the filesystem, secrets, or computation the browser shouldn't do:

```python
from custom_apps import action

@action
def add_task(title: str, priority: int = 2) -> dict:
    # file I/O, subprocesses, anything server-side
    return {"id": 1, "title": title, "priority": priority}
```

- Decorate functions with `@action` (or `@action(name="custom_name")`). Undecorated functions are not callable from the frontend.
- Action names must be valid Python identifiers (≤64 chars).
- Arguments arrive as keyword arguments matching the frontend's args object — type them and validate them; the frontend is untrusted input.
- Return JSON-serializable values. Raise structured errors (or return error dicts) rather than letting exceptions escape raw.
- Each invocation runs in a fresh isolated subprocess with a timeout (~120s) — no in-memory state between calls. Persist state to `data/` as JSON/SQLite.
- Keep responses small (~1MB limit): paginate, summarize, or write files and return paths.

## Data persistence (data/)

- The app folder is the database. Write under `data/`, never scatter files in the app root.
- JSON for small state; SQLite for anything relational or larger.
- Design for the app being open in multiple contexts: don't assume a single session.

## Build loop

1. Scaffold the folder, manifest, and minimal frontend first — get it appearing in the UI.
2. Build the frontend against mocked data if the backend is nontrivial.
3. Add actions one at a time, testing each via invoke before wiring more UI.
4. Iterate: edit files, reload the app window.
5. Verify the full path: UI element → invoke → action → data written → UI updated.

## When an app is (and isn't) the answer

- **App:** recurring use, visual/interactive surface, state the user returns to (dashboard, tracker, editor).
- **Not an app:** a one-off transformation (use code), a procedure (use a skill), a scheduled job (use a routine). Don't build an app when a script and a good answer would do.

## Rules

1. **Assets by path, never base64.**
2. **Validate action inputs** — the frontend is untrusted.
3. **Stateless actions; state lives in data/.**
4. **Manifest and index.html must exist** or the app won't appear — check both first when debugging "my app isn't showing".
5. **Small invocations.** Big results go to files; return paths and summaries.
