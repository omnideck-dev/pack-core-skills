---
name: create-skill
description: Create high-quality, well-scoped skills — loadable bundles of a prompt plus tool categories. Gathers requirements, drafts the skill record, validates scope and naming, installs it, and verifies it loads. Use when the user asks for a new skill or to turn a procedure into a skill.
metadata:
  tool_categories: coding,memory
---

# create-skill — Author and install new skills

A skill is a loadable bundle: a prompt fragment (instructions for an agent) plus the tool categories that grant its tools. The catalog shows every agent each skill's name and one-line description, so the description is the skill's interface — the LLM decides whether to load it based on that line alone.

## 1. Scope the skill

Ask (or infer from the request):

- **Trigger:** what should cause an agent to load this skill? The trigger lives in the description.
- **Boundaries:** what is explicitly out of scope? A skill that tries to do everything loads too often and dilutes its instructions.
- **Tools:** which tool categories does it actually need? Grant the minimum — categories are capabilities, and least-privilege applies.

A good skill does one job a certain way. "Review code changes for correctness" is a skill. "Be helpful with code" is not.

## 2. Draft the record

Fields:

- `id`: verb-first kebab-case (`review-security`, `write-draft`). Must equal `name` and be unique across the catalog.
- `name`: same as id.
- `description`: one line, action-oriented, states what it does and when to use it. This is what the catalog shows — make the trigger explicit ("Use when the user asks for…", "Use before…").
- `prompt`: the instructions an agent follows once loaded. Written to the agent, in the imperative. Concrete over abstract; examples over adverbs.
- `tool_categories`: list of category ids (`coding`, `browser`, `webfetch`, `memory`, `planning`, `image_generation`, `music_generation`, `desktop`, and integration-backed `email`, `calendar`, `drive`, `contacts`, `http`).

## 3. Write the prompt well

- **Open with the job.** One sentence: what this skill accomplishes.
- **Workflow as numbered steps.** Each step says what to do and what makes it good.
- **Rules as a short list at the end.** The invariants, the failure modes to avoid, the honesty requirements.
- **Keep it tight.** Every sentence should change agent behavior. If removing it changes nothing, remove it.
- **Include the anti-patterns.** Agents drift toward generic behavior; name the drift and forbid it.

## 4. Validate

Before installing, check:

- id/name uniqueness and kebab-case shape
- description names its trigger explicitly
- tool categories are minimal and actually used by the prompt
- no overlap with an existing skill (if overlapping, either differentiate the scope or propose updating the existing skill instead)
- prompt contains no references to tools it doesn't grant

## 5. Install and verify

Write the skill record to the skills store, confirm it appears in the catalog, and load it once to verify it resolves. Tell the user: name, when it triggers, and the categories granted.

## 6. Iterate with usage

When the user reports a skill misfiring (loading when it shouldn't, or missing its moment), tune the description first — it's the trigger. Tighten the trigger, don't widen it. Keep the change history so regressions can be unwound.

## Rules

1. **One skill, one job.** Reject sprawling scope in your own drafts.
2. **Least privilege on categories.** Every granted category must be load-bearing.
3. **The description is the contract.** If the trigger isn't in the description, the skill won't fire when needed.
4. **Prefer editing over accumulating.** A focused catalog of excellent skills beats a junk drawer.
