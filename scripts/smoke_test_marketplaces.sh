#!/usr/bin/env bash
# Install every plugin from the marketplace into throwaway Claude and Codex
# homes, then check the INSTALLED copy: a successful install proves nothing if
# the skill it installed points at files that were not installed with it.
#
# Usage: scripts/smoke_test_marketplaces.sh [owner/repo] [git-ref]
#   scripts/smoke_test_marketplaces.sh                                  # public main
#   scripts/smoke_test_marketplaces.sh onetinov/vibe-mentor my-branch   # a pushed branch

set -euo pipefail

REPO="${1:-onetinov/vibe-mentor}"
REF="${2:-main}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP_ROOT="$(mktemp -d /private/tmp/vibe-mentor-smoke.XXXXXX)"
CLAUDE_HOME="$TMP_ROOT/claude-home"
CODEX_HOME="$TMP_ROOT/codex-home"
PLUGINS=$(cd "$ROOT/plugins" && ls -d */ | tr -d /)

cleanup() {
  rm -rf "$TMP_ROOT"
}

trap cleanup EXIT

mkdir -p "$CLAUDE_HOME" "$CODEX_HOME"

# Every relative markdown link in every installed SKILL.md must resolve inside
# the installed plugin.
check_installed() {
  local client="$1" plugin="$2" root="$3"
  python3 - "$client" "$plugin" "$root" <<'EOF'
import re, sys
from pathlib import Path
client, plugin, root = sys.argv[1], sys.argv[2], Path(sys.argv[3])
skills = sorted(root.rglob("SKILL.md"))
if not skills:
    sys.exit(f"{client} {plugin}: no SKILL.md installed under {root}")
for skill in skills:
    for target in re.findall(r"\]\(([^)#\s]+)\)", skill.read_text()):
        if "://" in target:
            continue
        if not (skill.parent / target).resolve().is_file():
            sys.exit(f"{client} {plugin}: {skill.relative_to(root)} links to missing {target}")
print(f"ok  {client} {plugin}: {len(skills)} skill(s), all links resolve")
EOF
}

echo "== Claude: validate plugins =="
for plugin in $PLUGINS; do
  claude plugin validate "$ROOT/plugins/$plugin"
done

echo "== Claude: fresh-home marketplace add + install ($REPO @ $REF) =="
HOME="$CLAUDE_HOME" claude plugin marketplace add "https://github.com/$REPO.git#$REF"
for plugin in $PLUGINS; do
  HOME="$CLAUDE_HOME" claude plugin install "$plugin@vibe-mentor"
  check_installed claude "$plugin" "$(find "$CLAUDE_HOME/.claude/plugins/cache/vibe-mentor/$plugin" -mindepth 1 -maxdepth 1 -type d | head -1)"
done

echo "== Codex: fresh-home marketplace add + install ($REPO @ $REF) =="
CODEX_HOME="$CODEX_HOME" codex plugin marketplace add "$REPO" --ref "$REF"
for plugin in $PLUGINS; do
  CODEX_HOME="$CODEX_HOME" codex plugin add "$plugin@vibe-mentor"
  check_installed codex "$plugin" "$(find "$CODEX_HOME/plugins/cache/vibe-mentor/$plugin" -mindepth 1 -maxdepth 1 -type d | head -1)"
done

echo "Smoke tests passed."
