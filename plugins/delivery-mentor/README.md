# Delivery Mentor Plugin

Cross-client plugin package for the `delivery-mentor` skill.

This directory contains:

- `.claude-plugin/plugin.json` for Claude Code
- `.codex-plugin/plugin.json` for OpenAI Codex
- `skills/delivery-mentor/SKILL.md` as the packaged skill entrypoint

The canonical skill instructions live higher in the repo under
`skills/delivery-mentor/` and `content/delivery-mentor.md`.

## What It Helps With

`architecture-mentor` asks whether the system is shaped well. `delivery-mentor`
asks whether the work is landing well:

- blockers reaching the person who can clear them
- open and stacked pull requests actually landing
- review happening, not being bypassed
- CI gates and scheduled jobs that can actually run
- claims that someone else can re-run
- a standing agent brief that defines "done" as landed, not "still going"

It is written for fast builders who drive coding agents, and for those agents
directly. The rules are strict because an autonomous agent needs a bright line.

## Good Trigger Prompts

- `Use Delivery Mentor before I open this PR.`
- `I have eight open PRs. What should I land first?`
- `My agent hit a billing / credentials / approval blocker. Who needs to know, and how?`
- `I want to add a scheduled workflow. Check it can actually run.`
- `Review my agent's standing brief for delivery problems.`
- `Close out this session: what landed, what is open, what is escalated?`

## Putting It Where The Agent Reads It

Installing the plugin makes the skill available. It does not make an autonomous
agent consult it at the right moments. For that, add a line to the file the
agent reads at session start (`AGENTS.md` for Codex, `CLAUDE.md` for Claude
Code; keep both if both tools are used):

```markdown
Before opening, stacking or merging a PR, adding a CI workflow, or ending a
session, apply the delivery-mentor skill. Escalate any blocker that needs
someone else to that person, in a channel they read, as soon as you find it.
```
