# Contributing

## Goal

Keep one canonical source of truth for each skill's actual mentoring content,
then wrap it for Claude and Codex with the thinnest possible adapter files.

## Add A New Skill

1. Add or extend shared markdown under `content/`.
2. Add a canonical skill directory under `skills/<skill-name>/`.
3. Add thin wrappers only where a client needs a different filesystem location
   or manifest format.
4. Update both marketplace manifests if the new skill should be installable.
5. Update `README.md` and `TODO.md` if the support story or open questions
   change.

## Rules

- Do not bury the real instructions only inside a Claude-only or Codex-only wrapper.
- Keep platform adapters small and obvious.
- Prefer imports or references to shared files over copy-paste duplication.
- Document uncertainty instead of guessing command support.
- Validate Codex-facing `SKILL.md` files before shipping.
- If you add a new plugin under `plugins/`, make sure both Claude and Codex
  manifests use the shared repo version from `VERSION`.

## Testing

Test at least one explicit trigger and one negative case in both clients:

- explicit: "Use the architecture mentor skill to review this design."
- negative: "What time is it in Singapore?"

If the two clients diverge, fix the shared content first unless the difference
is clearly platform-specific.
