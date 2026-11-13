#!/usr/bin/env python3
"""Validate portable skill structure and linked local resources."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("Install development requirements: python3 -m pip install -r requirements-dev.txt")

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def validate(skill):
    errors = []
    entry = skill / "SKILL.md"
    if not entry.is_file():
        return [f"{skill.name}: missing SKILL.md"]
    text = entry.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return [f"{skill.name}: missing YAML frontmatter"]
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        return [f"{skill.name}: invalid YAML: {exc}"]
    if not isinstance(meta, dict):
        return [f"{skill.name}: frontmatter must be a mapping"]
    name = meta.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64 or name != skill.name:
        errors.append(f"{skill.name}: name must match directory and Agent Skills naming rules")
    description = meta.get("description")
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        errors.append(f"{skill.name}: description must be a nonempty string of at most 1024 characters")
    if meta.get("license") != "MIT":
        errors.append(f"{skill.name}: declare the repository's MIT license")
    if not parts[2].strip():
        errors.append(f"{skill.name}: missing instruction body")
    if len(text.splitlines()) >= 500:
        errors.append(f"{skill.name}: move detailed material to references; entry point must be under 500 lines")
    for document in skill.rglob("*.md"):
        for target in LINK.findall(document.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (document.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(skill.resolve()):
                errors.append(f"{document.relative_to(ROOT)}: resource escapes the self-contained skill: {target}")
            elif not resolved.exists():
                errors.append(f"{document.relative_to(ROOT)}: missing local resource: {target}")
    if (skill / "agents").exists():
        errors.append(f"{skill.name}: keep host-specific agents/ configuration outside the portable skill directory")
    return errors


def main():
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not skills:
        print("No skills found", file=sys.stderr)
        return 1
    errors = [error for skill in skills for error in validate(skill)]
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Validated {len(skills)} skills: frontmatter, local resource links, and platform-neutral structure.")
    print("This check does not evaluate agent behavior or engineering validity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
