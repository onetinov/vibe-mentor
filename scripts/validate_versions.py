#!/usr/bin/env python3

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path):
    return json.loads(path.read_text())


def iter_plugin_manifests():
    for plugin_dir in sorted((ROOT / "plugins").iterdir()):
        if not plugin_dir.is_dir():
            continue

        for rel in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
            manifest = plugin_dir / rel
            if manifest.exists():
                yield manifest


def main() -> int:
    version = (ROOT / "VERSION").read_text().strip()

    checks = {
        ".claude-plugin/marketplace.json metadata.version": (
            load_json(ROOT / ".claude-plugin" / "marketplace.json")["metadata"]["version"]
        )
    }

    for manifest in iter_plugin_manifests():
        rel = manifest.relative_to(ROOT)
        checks[f"{rel} version"] = load_json(manifest)["version"]

    errors = []
    for label, actual in checks.items():
        if actual != version:
            errors.append(f"{label} = {actual!r}, expected {version!r}")

    if errors:
        print("Version mismatch detected:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Version sync OK: {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
