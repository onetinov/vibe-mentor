# TODO

## Open Questions

- Confirm the exact Claude Code plugin marketplace manifest spec beyond the
  public `anthropics/skills`, `anthropics/knowledge-work-plugins`, and
  `anthropics/claude-plugins-official` example repos.
- Confirm whether Claude Code accepts HTTPS Git URLs for
  `claude plugin marketplace add`, especially on GitHub Enterprise domains
  beyond the public GitHub smoke test we ran.
- Confirm the exact install scope of Claude marketplace plugins:
  user-level, project-level, or selectable.
- Confirm how Claude plugin updates are pulled after marketplace registration.
- Confirm whether Claude plugin install and management commands differ between
  CLI, desktop app, IDE integrations, and hosted surfaces.
- Confirm how Codex plugin install and plugin management differ across CLI, app,
  IDE extension, and cloud/web surfaces.
- Confirm the final published repository location for `vibe-mentor`.
- Replace placeholder GitHub Enterprise URLs and branch names in all manifests.
- Add automated cross-client smoke tests in CI once Claude/Codex auth handling
  is stable for noninteractive environments.

## Nice To Have

- Publish a second skill focused on prototype-to-production review.
- Add screenshot assets for the Codex plugin manifest.
- Add a small release workflow for validating manifests before tagging.
