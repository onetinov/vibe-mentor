# Architecture Mentor Plugin

Cross-client plugin package for the `architecture-mentor` skill.

This directory contains:

- `.claude-plugin/plugin.json` for Claude Code
- `.codex-plugin/plugin.json` for OpenAI Codex
- `skills/architecture-mentor/SKILL.md` as the packaged skill entrypoint

The canonical skill instructions still live higher in the repo under
`skills/architecture-mentor/` and `content/`.

## What It Helps With

Use `architecture-mentor` when you want pragmatic advice about:

- architecture review
- mid-build correction without killing momentum
- prototype-to-production hardening
- repo and git hygiene
- deployment shape and production-readiness
- agentic system boundaries

The skill is biased toward:

- one recommendation
- one reason
- one risk
- one next move

It should preserve good product intent while challenging drift, wrong repo
scope, and regression back to laptop-only workflows.

## Good Trigger Prompts

These are good ways to invoke the skill in Claude Code or Codex:

- `Review this architecture the way Rob would. Preserve the idea but fix the design.`
- `I have a working prototype. Is this still laptopware?`
- `This app works locally. What is the next move to make it production-worthy?`
- `I want to launch this publicly. What architecture or deployment mistakes should I fix now?`
- `This repo feels messy. Is the git scope wrong, and what should stay vs go?`
- `We already have CI and deploy manifests. Help me improve local dev without breaking the path back to production.`
- `I am mid-build. Challenge any drift from production best practice, but do not turn this into a rewrite.`
- `Classify this project shape and tell me the simplest stronger topology.`
- `Review this agentic system. What should live in workflows, tools, prompts, or normal code?`

## Trigger Questions

If you are not sure whether to use the skill, ask questions like:

- `Are we still treating this like an experiment, or is this now an app?`
- `Does this repo boundary look wrong?`
- `Should this be in git at all?`
- `What would break if I redeployed, restarted, or retried this?`
- `Are we drifting away from the stated intent?`
- `Do we need short intent and session docs yet, or is that still overkill?`
- `Are we about to throw away deployability just to make local hacking easier?`
- `What production assumptions change if this becomes public facing or commercial?`

## Deployment Intent Labels

The skill now reasons differently based on intended exposure:

- `private experiment`
- `private app`
- `public facing`
- `team / commercial`

If you know which one applies, say it up front. It changes how hard the skill
should push on rigor, security, reproducibility, and collaboration hygiene.

## Grounding Docs

Once a project matures into an app, grows beyond trivial scope, or becomes
collaborative, the skill may recommend two short docs:

- an `intent` doc:
  mission, outcome, deployment intent, product shape, and core loop when it fits
- a `session` doc:
  current objective, freeform status, decisions made, open questions, and next move

These should stay compact. Local env quirks, repeated command mistakes, and
tool reminders should usually live in platform memory rather than git-tracked
project docs.
