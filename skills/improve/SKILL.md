---
name: improve
description: 'Reflect on the current conversation — what worked, what didn''t — and turn those lessons into something concrete: a new skill, a custom tool, a change to an existing skill or tool, a custom app, or an agent profile. Use when the user says something like ''improve yourself'', ''make this easier next time'', or ''learn from this session''.'
metadata:
  tool_categories: coding,memory
---

# improve — Turn conversation lessons into durable improvements

You close the loop between how work actually went and how the system is set up. The unit of output is a concrete artifact, not a suggestion.

## 1. Mine the conversation

Look back over the current session and identify:

- **What worked** — flows that went smoothly, outputs the user praised, approaches worth repeating.
- **What didn't** — corrections the user made, repeated re-explanations, steps that took multiple attempts, formatting or content the user changed by hand afterward.
- **What was missing** — questions you had to ask that context should have answered, tools you wished existed, information you had to re-discover.

The strongest signal is friction the user paid for: every manual fix, repeated instruction, or "no, like this" is a lesson with a price already paid. Weak signals ("maybe next time...") are worth noting but never justify an artifact on their own.

## 2. Classify the lesson

Each lesson falls into one of:

- **Knowledge** — a fact or preference worth remembering (the user's timezone, naming conventions, output style). → Fix with a memory write.
- **Procedure** — a repeatable way of doing something (how to build a chart, how to file a report). → Fix with a skill.
- **Capability** — something that required ad-hoc scripting or manual steps. → Fix with a custom tool.
- **Setup** — a persona, toolset, or starting context that had to be assembled by hand. → Fix with an agent profile.
- **Interface** — something the user would want as a live view or dashboard rather than a chat answer. → Fix with a custom app.
- **Recurrence** — something that should happen on a schedule or trigger without being asked. → Fix with a routine.

Prefer the smallest fix that removes the friction. Don't build an app to remember a timezone.

## 3. Propose before building (unless told otherwise)

Show the user:
1. The lesson, stated in one sentence.
2. The artifact type and why it's the right size.
3. A sketch of the artifact (skill prompt outline, tool signature, profile shape).

Get a go-ahead for anything that writes files or changes shared state. Trivial memory writes don't need confirmation.

## 4. Build it for real

- **Skill:** create the skill record (id, name, one-line description for the catalog, prompt, tool categories). Follow the house style: verb-first kebab-case id equal to name, prompt written as instructions to an agent, no filler.
- **Custom tool:** prefer a parameterized, reusable operation over one-off code. Register it so it's discoverable via the custom-tool lookup; give it a clear description and typed parameters.
- **Agent profile:** include only the skills the persona actually needs, a system prompt that teaches the essentials (file layout, conventions, rules), and the right default model.
- **Custom app:** build in the standard app layout — manifest, frontend, optional actions, data persistence. Reference assets by path, never inline.
- **Routine:** define the trigger precisely (schedule, event, or condition) and the steps completely; routines run without you.

## 5. Verify and report

Confirm the artifact exists and loads (skill appears in the catalog, tool runs once end-to-end, app opens). Report: what was learned, what you built, where it lives, and how it will show up next time.

## Rules

1. **Every claim about the session cites the moment it happened.** Vague lessons are guesses.
2. **One lesson, one artifact.** Don't bundle unrelated improvements.
3. **Don't duplicate.** Check whether a skill, tool, or profile already covers this before creating a new one — modifying an existing artifact is usually better than adding another.
4. **Nothing silent.** The user should be able to veto any change.
5. **Don't over-automate.** A routine for a one-time task is clutter; only recurring, well-understood flows become routines.
