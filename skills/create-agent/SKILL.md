---
name: create-agent
description: Create agent profiles — reusable agent configurations bundling a persona (system prompt), skill grants, model, and inference parameters. Use when the user asks for a specialized agent, or repeatedly assembles the same setup by hand.
metadata:
  tool_categories: coding,memory
---

# create-agent — Design reusable agent profiles

An agent profile is a saved configuration: system prompt (the persona and its essential knowledge), skill grants, model, and inference parameters. Profiles exist to make a recurring setup instant — instead of re-assembling the same context each session, the user spawns an agent that starts ready.

## 1. Establish the job

- What does this agent do, specifically? ("Reviews security-sensitive diffs" not "helps with code")
- What context does it need every time? (file paths, conventions, tool usage, rules) — that's the system prompt.
- What tools/skills does it actually use? Grant only those.

## 2. Write the system prompt

The system prompt is loaded once at spawn and cannot be revised mid-session, so it must teach everything essential:

- **Identity and job** in one paragraph.
- **Context the agent can't infer:** file paths, project layout, naming conventions, repo locations, house style.
- **Workflow:** the steps, in order, with what makes each step good.
- **Rules and boundaries:** what not to do, what requires confirmation, what output format is expected.
- **Verbatim reference material** where precision matters (templates, schemas, exact commands).

The prompt is instructions, not a bio. Every sentence should change the agent's behavior.

## 3. Choose skills and model

- **Skills:** minimum set the persona needs. Every grant is a capability surface — least privilege. If the agent only reads files, don't grant bash.
- **Model:** match to the task — strong reasoning for analysis/code, lighter models for routine or high-volume work. State the choice when it's a judgment call.
- **Inference parameters:** set temperature only with a reason (lower for code/analysis, default for prose). Leave the rest unset unless the persona demands it.

## 4. Validate

- id is unique, kebab-case; name is human-readable.
- System prompt is self-contained — a fresh agent with no conversation history can act on it.
- Skill grants are minimal and every granted skill is load-bearing.
- Spawn behavior is defined: what it should do on first turn, what it should report at the end.

## 5. Register and verify

Save the profile, confirm it appears in the profile list, and run one task end-to-end if feasible. Report: profile id, what it's for, its grants, and how to spawn it.

## Rules

1. **One profile, one job.** A profile that does everything is a persona in name only.
2. **Least privilege on skills.**
3. **Self-contained system prompts.** No references to conversations the agent won't have had.
4. **Prefer editing existing profiles** over proliferating near-duplicates.
5. **Sub-agents are stateless.** Every spawn gets complete instructions — the profile's job is making that cheap.
