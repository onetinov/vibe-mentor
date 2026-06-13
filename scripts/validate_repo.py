#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PYTHON = ROOT / ".venv" / "bin" / "python"


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def iter_skill_dirs():
    skills_root = ROOT / "skills"
    if not skills_root.exists():
        return

    for skill_dir in sorted(skills_root.iterdir()):
        if (skill_dir / "SKILL.md").exists():
            yield skill_dir


def iter_plugin_dirs():
    plugins_root = ROOT / "plugins"
    if not plugins_root.exists():
        return

    for plugin_dir in sorted(plugins_root.iterdir()):
        if (plugin_dir / ".codex-plugin" / "plugin.json").exists():
            yield plugin_dir


def main() -> int:
    if not PYTHON.exists():
        print(f"Missing venv python at {PYTHON}")
        return 1

    run(str(PYTHON), str(ROOT / "scripts" / "validate_versions.py"))

    for skill_dir in iter_skill_dirs():
        run(
            str(PYTHON),
            "/Users/rcherry/.codex/skills/.system/skill-creator/scripts/quick_validate.py",
            str(skill_dir),
        )

    for plugin_dir in iter_plugin_dirs():
        run(
            str(PYTHON),
            "/Users/rcherry/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py",
            str(plugin_dir),
        )

    print("Repo validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
