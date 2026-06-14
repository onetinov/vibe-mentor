# Vibe Mentor

Public source repository for pragmatic mentoring skills that can be distributed
to both Claude Code and OpenAI Codex.

## What This Repo Provides

- One canonical, model-neutral architecture mentor skill
- A Claude Code marketplace wrapper
- A Codex plugin and marketplace wrapper
- Repo-scoped wrappers for local testing in both clients

The repository name is intentionally broader than the first skill. `vibe-mentor`
is the umbrella distribution repo; `architecture-mentor` is the first concrete
skill shipped from it.

The skill is aimed at:

- system architecture review
- trade-off analysis
- platform selection
- incident architecture and operational recovery shape
- enterprise and compliance constraints
- clarifying-question discipline
- pragmatic recommendations instead of generic best-practice sludge

## Why This Exists

AI coding tools can produce code that looks clever, compiles, and even demos
well while still having weak architecture.

That usually shows up as:

- business logic in the wrong place
- hidden or duplicated state ownership
- frontend-owned orchestration that should live elsewhere
- secrets and trust boundaries handled unsafely
- retry, async, and recovery behavior buried in ad hoc code
- systems that work on one laptop but degrade badly in production

The problem is not usually that the model cannot write code. The problem is that
without architecture guidance it will often produce structures that are harder to
operate, harder to maintain, and easier to break under real usage.

`vibe-mentor` is meant to intervene there. It is not a teaching course. It is a
practical advisory layer that helps a builder:

- choose a sane default shape early
- catch structural drift mid-build
- review an existing system without demanding a rewrite
- improve production readiness by fixing the right boundaries

The intended outcome is not "perfect architecture." It is a stronger next move:
better placement of logic, state, secrets, async work, and operational
responsibility.

## How The Skill Should Feel

The skill should act like an intervention tool, not a lecture.

It should usually give:

- one recommendation
- one reason
- one risk if ignored
- one next move

It should optimize for:

- stage-aware advice: before build, during build, after build
- strong defaults over option overload
- boundary placement over abstract theory
- momentum-preserving correction instead of architecture purity

## Supported Clients

- Claude Code
- OpenAI Codex

## Easy Install

### Codex

```bash
codex plugin marketplace add onetinov/vibe-mentor
codex plugin add architecture-mentor@vibe-mentor
```

### Claude Code

```bash
claude plugin marketplace add onetinov/vibe-mentor
claude plugin install architecture-mentor@vibe-mentor
```

These are the recommended install paths. No sparse checkout, skill installer,
or manual skill copying should be needed on current clients.

## Upgrade

### Codex

```bash
codex plugin marketplace upgrade vibe-mentor
```

### Claude Code

```bash
claude plugin marketplace update vibe-mentor
```

If a client does not pick up a new plugin version immediately, restart or
reload the client. Reinstalling the plugin may also be needed on stale caches.

## Planning Docs

For ongoing multi-session design work, start with:

- `docs/intent/vibe-mentor-intent.md`
- `docs/intent/skill-family-map.md`
- `docs/intent/session-sequence-guide.md`

## Repo Layout

```text
content/
  architecture-mentor.md
  architecture-mentor-review.md
skills/
  architecture-mentor/
    SKILL.md
    agents/
      openai.yaml
.claude/
  skills/
    architecture-mentor/
      SKILL.md
.claude-plugin/
  marketplace.json
.agents/
  plugins/
    marketplace.json
  skills/
    architecture-mentor/
      SKILL.md
plugins/
  architecture-mentor/
    .claude-plugin/
      plugin.json
    .codex-plugin/
      plugin.json
    README.md
    skills/
      architecture-mentor/
        SKILL.md
scripts/
  bump_version.py
  install_git_hooks.sh
  validate_repo.py
  validate_versions.py
.githooks/
  pre-commit
```

## Claude Code

### Confirmed today

Anthropic's public plugin repos document plugin marketplace install commands:

```text
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```

### Marketplace install

Tested against the public `onetinov/vibe-mentor` repo:

```text
claude plugin marketplace add onetinov/vibe-mentor
```

HTTPS Git URL form also worked in our smoke test:

```text
claude plugin marketplace add https://github.com/onetinov/vibe-mentor.git
```

Then install the plugin:

```text
claude plugin install architecture-mentor@vibe-mentor
```

For an isolated smoke test that does not touch your normal Claude setup, use a
temporary home and local install scope:

```bash
TMP_HOME="$(mktemp -d)"
HOME="$TMP_HOME" claude plugin marketplace add https://github.com/onetinov/vibe-mentor.git
HOME="$TMP_HOME" claude plugin install architecture-mentor@vibe-mentor --scope local
```

### Enable, disable, uninstall

- Use `claude plugin install ...` to add the plugin
- Use Claude Code's plugin management UI or current `claude plugin` commands to
  disable or remove it

## Codex

### Confirmed today

Codex documents CLI marketplace commands via `codex plugin marketplace ...`
and `codex plugin add ...`.

### Marketplace install

Tested against the public `onetinov/vibe-mentor` repo:

```bash
codex plugin marketplace add onetinov/vibe-mentor
```

Then install the plugin:

```bash
codex plugin add architecture-mentor@vibe-mentor
```

HTTPS Git URL form should also work on current clients:

```bash
codex plugin marketplace add https://github.com/onetinov/vibe-mentor.git
```

For an isolated smoke test that does not touch your normal Codex setup, use a
temporary `CODEX_HOME`:

```bash
TMP_CODEX_HOME="$(mktemp -d)"
CODEX_HOME="$TMP_CODEX_HOME" codex plugin marketplace add onetinov/vibe-mentor
CODEX_HOME="$TMP_CODEX_HOME" codex plugin add architecture-mentor@vibe-mentor
```

Public marketplace add did not require `gh auth` in our smoke tests.

## Smoke Tests

Run the reusable cross-client smoke test script from the repo root:

```bash
scripts/smoke_test_marketplaces.sh
```

It uses temporary Claude and Codex homes under `/private/tmp` so it does not
modify your normal local plugin state.

### Enable, disable, uninstall

```bash
codex plugin marketplace list
codex plugin marketplace remove vibe-mentor
```

## How To Invoke The Skill

Try prompts like:

- "Use the architecture mentor skill to review this system design."
- "Do this the way Rob would: preserve the product idea, but fix the architecture."
- "Review this incident recovery plan with architecture mentor guidance."
- "Bear Rob's guidance in mind while we choose the platform shape."

Expected behavior:

- infer the likely system and operating context
- ask clarifying questions only when the missing information changes the design
- distinguish what to keep from what to move or remove
- make concrete recommendations with trade-offs

## Troubleshooting

- If simple marketplace add fails, check the client version first.
- If the skill does not trigger, use its name explicitly: `architecture-mentor`.
- If a marketplace does not appear in Codex, restart Codex after adding it.
- If a marketplace add fails against GitHub shorthand, retry with the HTTPS Git
  URL form.

## Version Caveats

- Codex marketplace commands are documented in current OpenAI Codex docs.
- Claude Code skill locations and `CLAUDE.md` are documented in current Claude
  Code docs.
- Claude plugin marketplace installation is confirmed by Anthropic's public
  plugin repositories, but GitHub Enterprise URL variants still need practical
  verification in a real Claude environment.
- Exact command behavior can differ between CLI, app, IDE extension, and hosted
  surfaces.

## Versioning And Hooks

This repo keeps a shared point-release version in `VERSION` and validates that
the version is synchronized across:

- `.claude-plugin/marketplace.json`
- every `plugins/*/.claude-plugin/plugin.json`
- every `plugins/*/.codex-plugin/plugin.json`

Validation runs in the repo pre-commit hook and in CI.

Install the repo hooks once if you want local enforcement:

```bash
./scripts/install_git_hooks.sh
```

Validate the whole repo manually:

```bash
./scripts/validate_repo.py
```

Bump every linked component together:

```bash
./scripts/bump_version.py 0.1.1
```

## Security And Trust

Inspect any skill or plugin repository before installing it.

Skills and plugins can influence prompts, tooling, file access patterns, and
automation behavior. Treat installation the same way you would treat running a
new code generator, shell helper, or MCP configuration from the internet.

## Sources

- Codex customization docs:
  https://developers.openai.com/codex/concepts/customization
- Codex plugin build docs:
  https://developers.openai.com/codex/plugins/build
- Codex manual:
  https://developers.openai.com/codex/codex-manual
- Claude `.claude` directory docs:
  https://code.claude.com/docs/en/claude-directory
- Claude memory and `CLAUDE.md` docs:
  https://code.claude.com/docs/en/memory
- Claude SDK skills docs:
  https://code.claude.com/docs/en/agent-sdk/skills
- Anthropic skills marketplace example:
  https://github.com/anthropics/skills
- Anthropic knowledge-work plugins:
  https://github.com/anthropics/knowledge-work-plugins
- Anthropic official plugin directory:
  https://github.com/anthropics/claude-plugins-official
