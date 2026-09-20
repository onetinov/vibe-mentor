# Vibe Mentor Repo

This repository publishes mentoring skills as a plugin marketplace for both
Claude Code and OpenAI Codex.

Maintainer rules:

- Each skill lives, complete, in `plugins/<name>/skills/<name>/`: `SKILL.md`,
  `references/`, and `agents/openai.yaml`. That directory is what both clients
  install, so nothing a skill needs may live outside it.
- `.claude/skills/<name>` and `.agents/skills/<name>` are symlinks to it for
  repo-local testing. Never copy content into them.
- Rules an agent must follow go in `SKILL.md`, which always loads when the
  skill fires. `references/` is for reasoning and detail that may not be read.
- Run `scripts/validate_repo.py` before committing. Before merging a change
  to packaging, push the branch and run
  `scripts/smoke_test_marketplaces.sh onetinov/vibe-mentor <branch>`.
- Keep installation docs honest about what is confirmed versus inferred.
