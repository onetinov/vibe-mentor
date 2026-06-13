#!/bin/sh
set -eu

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
git -C "$repo_root" config core.hooksPath .githooks
echo "Configured core.hooksPath=.githooks"
