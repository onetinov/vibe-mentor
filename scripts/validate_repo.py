#!/usr/bin/env python3

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def load_json(path: Path):
    return json.loads(path.read_text())


def iter_skill_files():
    for root in (
        ROOT / "skills",
        ROOT / ".agents" / "skills",
        ROOT / ".claude" / "skills",
        ROOT / "plugins",
    ):
        if not root.exists():
            continue

        for path in sorted(root.rglob("SKILL.md")):
            yield path


def iter_plugin_dirs():
    plugins_root = ROOT / "plugins"
    if not plugins_root.exists():
        return

    for plugin_dir in sorted(plugins_root.iterdir()):
        if (plugin_dir / ".codex-plugin" / "plugin.json").exists():
            yield plugin_dir


def validate_skill_file(path: Path) -> list[str]:
    text = path.read_text()
    errors = []

    if not text.startswith("---\n"):
        errors.append("missing frontmatter start")
        return errors

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        errors.append("missing closing frontmatter delimiter")
        return errors

    frontmatter = parts[1]
    if "name:" not in frontmatter:
        errors.append("frontmatter missing name")
    if "description:" not in frontmatter:
        errors.append("frontmatter missing description")

    return errors


def validate_plugin_dir(plugin_dir: Path) -> list[str]:
    errors = []
    codex_manifest = plugin_dir / ".codex-plugin" / "plugin.json"
    claude_manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    skill_entry = plugin_dir / "skills"

    if not skill_entry.exists():
        errors.append("missing packaged skills directory")

    if codex_manifest.exists():
        codex = load_json(codex_manifest)
        if codex.get("name") != plugin_dir.name:
            errors.append(".codex-plugin/plugin.json name does not match plugin dir")

    if claude_manifest.exists():
        claude = load_json(claude_manifest)
        if claude.get("name") != plugin_dir.name:
            errors.append(".claude-plugin/plugin.json name does not match plugin dir")

    return errors


def validate_marketplaces() -> list[str]:
    errors = []

    codex_marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")

    codex_plugins = {plugin["name"]: plugin for plugin in codex_marketplace["plugins"]}
    claude_plugins = {plugin["name"]: plugin for plugin in claude_marketplace["plugins"]}

    for plugin_dir in iter_plugin_dirs():
        name = plugin_dir.name

        codex_entry = codex_plugins.get(name)
        if not codex_entry:
            errors.append(f"Codex marketplace missing plugin entry for {name}")
        else:
            source = codex_entry.get("source", {})
            if source.get("source") != "git-subdir":
                errors.append(f"Codex marketplace source for {name} is not git-subdir")
            if source.get("path") != f"./plugins/{name}":
                errors.append(f"Codex marketplace path for {name} is not ./plugins/{name}")
            if source.get("url") != "https://github.com/onetinov/vibe-mentor.git":
                errors.append(f"Codex marketplace url for {name} is not the public repo")
            if source.get("ref") != "main":
                errors.append(f"Codex marketplace ref for {name} is not main")

        claude_entry = claude_plugins.get(name)
        if not claude_entry:
            errors.append(f"Claude marketplace missing plugin entry for {name}")
        else:
            source = claude_entry.get("source", {})
            if source.get("source") != "git-subdir":
                errors.append(f"Claude marketplace source for {name} is not git-subdir")
            if source.get("path") != f"./plugins/{name}":
                errors.append(f"Claude marketplace path for {name} is not ./plugins/{name}")
            if source.get("url") != "https://github.com/onetinov/vibe-mentor.git":
                errors.append(f"Claude marketplace url for {name} is not the public repo")
            if source.get("ref") != "main":
                errors.append(f"Claude marketplace ref for {name} is not main")

    return errors


def main() -> int:
    run(sys.executable, str(ROOT / "scripts" / "validate_versions.py"))

    errors = []

    for skill_file in iter_skill_files():
        skill_errors = validate_skill_file(skill_file)
        if skill_errors:
            rel = skill_file.relative_to(ROOT)
            for error in skill_errors:
                errors.append(f"{rel}: {error}")

    for plugin_dir in iter_plugin_dirs():
        plugin_errors = validate_plugin_dir(plugin_dir)
        if plugin_errors:
            rel = plugin_dir.relative_to(ROOT)
            for error in plugin_errors:
                errors.append(f"{rel}: {error}")

    errors.extend(validate_marketplaces())

    if errors:
        print("Repo validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repo validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
