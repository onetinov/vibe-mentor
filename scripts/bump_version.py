#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def update_json(path: Path, updater):
    data = json.loads(path.read_text())
    updater(data)
    path.write_text(json.dumps(data, indent=2) + "\n")


def iter_plugin_manifests():
    for plugin_dir in sorted((ROOT / "plugins").iterdir()):
        if not plugin_dir.is_dir():
            continue

        for rel in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
            manifest = plugin_dir / rel
            if manifest.exists():
                yield manifest


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: bump_version.py <x.y.z>")
        return 1

    version = sys.argv[1].strip()
    if not SEMVER_RE.match(version):
        print(f"Invalid semver: {version}")
        return 1

    (ROOT / "VERSION").write_text(version + "\n")

    update_json(
        ROOT / ".claude-plugin" / "marketplace.json",
        lambda data: data["metadata"].__setitem__("version", version),
    )

    for manifest in iter_plugin_manifests():
        update_json(manifest, lambda data: data.__setitem__("version", version))

    print(f"Bumped all linked components to {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
