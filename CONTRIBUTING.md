# Contributing

## Goal

Keep one canonical source of truth for each skill's actual mentoring content,
then wrap it for Claude and Codex with the thinnest possible adapter files.

## Add A New Skill

1. Create `plugins/<skill-name>/` with `.claude-plugin/plugin.json`,
   `.codex-plugin/plugin.json` and `README.md`.
2. Put the complete skill in `plugins/<skill-name>/skills/<skill-name>/`:
   `SKILL.md` (with the rules an agent must follow), `references/` (reasoning
   and detail), `agents/openai.yaml` (Codex display metadata).
3. Symlink it for repo-local testing:
   `ln -s ../../plugins/<skill-name>/skills/<skill-name> .claude/skills/<skill-name>`
   and the same under `.agents/skills/`.
4. Add a `"source": "./plugins/<skill-name>"` entry to both
   `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`.
5. Update `README.md` and `TODO.md` if the support story or open questions
   change.

## Rules

- A plugin must be self-contained. Installation copies only `plugins/<name>/`;
  a link that leaves it resolves to nothing after install.
- Anything an agent must obey goes in `SKILL.md`. Clients load `SKILL.md` when
  the skill fires; files in `references/` are read only if the agent chooses to.
- Keep one copy of every file. Wrappers are symlinks, not copies.
- Document uncertainty instead of guessing command support.
- Validate Codex-facing `SKILL.md` files before shipping.
- If you add a new plugin under `plugins/`, make sure both Claude and Codex
  manifests use the shared repo version from `VERSION`.

## Testing

`scripts/validate_repo.py` runs in the pre-commit hook and CI. It checks
frontmatter, links that leave the plugin package, wrapper symlinks, marketplace
entries and version sync.

`scripts/smoke_test_marketplaces.sh [owner/repo] [ref]` installs every plugin
into throwaway Claude and Codex homes and checks the installed copy. Run it
against your pushed branch before merging any packaging change.

Then test at least one explicit trigger and one negative case in both clients:

- explicit: "Use the architecture mentor skill to review this design."
- negative: "What time is it in Singapore?"

If the two clients diverge, fix the shared content first unless the difference
is clearly platform-specific.
