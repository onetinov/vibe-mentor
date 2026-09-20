#!/usr/bin/env python3

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def load_json(path: Path):
    return json.loads(path.read_text())


WRAPPER_ROOTS = (ROOT / ".agents" / "skills", ROOT / ".claude" / "skills")
LINK_PATTERN = re.compile(r"\]\(([^)#\s]+)\)")


def iter_skill_files():
    plugins_root = ROOT / "plugins"
    if plugins_root.exists():
        yield from sorted(plugins_root.rglob("SKILL.md"))


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

    # An unquoted ": " inside a plain YAML scalar is a parse error in strict
    # loaders, which silently drops the skill.
    for line in frontmatter.splitlines():
        key, sep, value = line.partition(": ")
        value = value.strip()
        if sep and value and value[0] not in "\"'|>" and ": " in value:
            errors.append(f"frontmatter `{key}` has an unquoted ': ' (quote the value)")

    # Installed plugins are copied without the rest of the repo, so every
    # relative link in a skill must resolve inside its own plugin directory.
    plugin_dir = next((p for p in path.parents if p.parent == ROOT / "plugins"), None)
    for target in LINK_PATTERN.findall(parts[2]):
        if "://" in target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"link `{target}` does not resolve")
        elif plugin_dir and plugin_dir.resolve() not in resolved.parents:
            errors.append(f"link `{target}` leaves the plugin package; it will not exist after install")

    return errors


def validate_wrappers() -> list[str]:
    """Repo-local skill wrappers must be symlinks to the packaged skill."""
    errors = []
    for root in WRAPPER_ROOTS:
        if not root.exists():
            continue
        for entry in sorted(root.iterdir()):
            rel = entry.relative_to(ROOT)
            expected = (ROOT / "plugins" / entry.name / "skills" / entry.name).resolve()
            if not entry.is_symlink():
                errors.append(f"{rel}: must be a symlink to plugins/{entry.name}/skills/{entry.name}")
            elif entry.resolve() != expected:
                errors.append(f"{rel}: points at {entry.resolve()}, expected {expected}")
    for stale in ("skills", "content"):
        if (ROOT / stale).exists():
            errors.append(f"{stale}/: skill content belongs inside plugins/<name>/skills/<name>/")
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
            if codex_entry.get("source") != f"./plugins/{name}":
                errors.append(f"Codex marketplace source for {name} is not ./plugins/{name}")

        claude_entry = claude_plugins.get(name)
        if not claude_entry:
            errors.append(f"Claude marketplace missing plugin entry for {name}")
        else:
            if claude_entry.get("source") != f"./plugins/{name}":
                errors.append(f"Claude marketplace source for {name} is not ./plugins/{name}")

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
    errors.extend(validate_wrappers())

    if errors:
        print("Repo validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repo validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
