#!/usr/bin/env bash

set -euo pipefail

REPO_URL="${1:-https://github.com/onetinov/vibe-mentor.git}"
TMP_ROOT="$(mktemp -d /private/tmp/vibe-mentor-smoke.XXXXXX)"
CLAUDE_HOME="$TMP_ROOT/claude-home"
CODEX_HOME="$TMP_ROOT/codex-home"

cleanup() {
  rm -rf "$TMP_ROOT"
}

trap cleanup EXIT

mkdir -p "$CLAUDE_HOME" "$CODEX_HOME"

echo "== Claude: validate plugin =="
claude plugin validate plugins/architecture-mentor

echo "== Claude: isolated marketplace add/install/list/uninstall =="
HOME="$CLAUDE_HOME" claude plugin marketplace add "$REPO_URL"
HOME="$CLAUDE_HOME" claude plugin marketplace list
HOME="$CLAUDE_HOME" claude plugin install architecture-mentor@vibe-mentor --scope local
HOME="$CLAUDE_HOME" claude plugin list
HOME="$CLAUDE_HOME" claude plugin uninstall architecture-mentor --scope local

echo "== Codex: isolated marketplace add/install/list/remove =="
CODEX_HOME="$CODEX_HOME" codex plugin marketplace add "$REPO_URL" \
  --sparse .agents/plugins \
  --sparse plugins \
  --json
CODEX_HOME="$CODEX_HOME" codex plugin list
CODEX_HOME="$CODEX_HOME" codex plugin add architecture-mentor@vibe-mentor --json
CODEX_HOME="$CODEX_HOME" codex plugin list
CODEX_HOME="$CODEX_HOME" codex plugin remove architecture-mentor@vibe-mentor

echo "Smoke tests passed."
