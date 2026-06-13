# TODO

## Open Questions

- Confirm the exact Claude Code plugin marketplace manifest spec beyond the
  public `anthropics/skills`, `anthropics/knowledge-work-plugins`, and
  `anthropics/claude-plugins-official` example repos.
- Confirm whether Claude Code accepts HTTPS Git URLs for
  `claude plugin marketplace add`, especially on GitHub Enterprise domains.
- Confirm the exact install scope of Claude marketplace plugins:
  user-level, project-level, or selectable.
- Confirm how Claude plugin updates are pulled after marketplace registration.
- Confirm whether Claude plugin install and management commands differ between
  CLI, desktop app, IDE integrations, and hosted surfaces.
- Confirm whether Codex documents a stable direct plugin install command
  (`codex plugin add <plugin>@<marketplace>`) or whether plugin-directory UI is
  the only fully documented install path after marketplace registration.
- Confirm how Codex plugin install and plugin management differ across CLI, app,
  IDE extension, and cloud/web surfaces.
- Confirm the final published repository location for `vibe-mentor`.
- Replace placeholder GitHub Enterprise URLs and branch names in all manifests.
- Add automated cross-client smoke tests once stable install commands are
  confirmed for both clients.

## Nice To Have

- Publish a second skill focused on prototype-to-production review.
- Add screenshot assets for the Codex plugin manifest.
- Add a small release workflow for validating manifests before tagging.
