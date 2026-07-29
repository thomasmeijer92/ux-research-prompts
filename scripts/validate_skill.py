#!/usr/bin/env python3
"""Validate the public UX Research Prompts skill repository."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILL_NAME = "ux-research-prompts"
EXPECTED_RECIPE_IDS = {str(number) for number in range(1, 101)} | {
    f"M{number}" for number in range(1, 26)
}
REQUIRED_FILES = {
    ".github/workflows/validate-skill.yml",
    "SKILL.md",
    "README.md",
    "LICENSE",
    "agents/openai.yaml",
    "references/method-selection-guide.md",
    "references/methodology-sources.md",
    "references/prompt-catalog.md",
    "references/prompt-library.md",
    "sources/notion-original-skill.md",
    "examples/usability-test-plan.md",
    "examples/interview-synthesis.md",
    "examples/discovery-research-plan.md",
    "scripts/validate_skill.py",
}
PUBLIC_COPY_FILES = {
    "README.md",
    "examples/usability-test-plan.md",
    "examples/interview-synthesis.md",
    "examples/discovery-research-plan.md",
}


class ValidationError(Exception):
    """Collect a reader-facing validation failure."""


def load_yaml_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, flags=re.DOTALL)
    if not match:
        raise ValidationError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")

    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValidationError(f"{path.relative_to(ROOT)}: frontmatter must be a map")
    return data


def validate_required_files(errors: list[str]) -> None:
    for relative_path in sorted(REQUIRED_FILES):
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")


def validate_skill_metadata(errors: list[str]) -> None:
    try:
        metadata = load_yaml_frontmatter(ROOT / "SKILL.md")
    except (ValidationError, yaml.YAMLError) as exc:
        errors.append(str(exc))
        return

    if set(metadata) != {"name", "description"}:
        errors.append("SKILL.md frontmatter must contain only name and description")
    if metadata.get("name") != EXPECTED_SKILL_NAME:
        errors.append(f"SKILL.md name must be {EXPECTED_SKILL_NAME}")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("SKILL.md description must be a non-empty string")

    try:
        agent_metadata = yaml.safe_load(
            (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        )
        interface = agent_metadata["interface"]
    except (OSError, TypeError, KeyError, yaml.YAMLError) as exc:
        errors.append(f"agents/openai.yaml: invalid interface metadata ({exc})")
        return

    short_description = interface.get("short_description", "")
    if not 25 <= len(short_description) <= 64:
        errors.append("agents/openai.yaml short_description must be 25-64 characters")

    default_prompt = interface.get("default_prompt", "")
    if f"${EXPECTED_SKILL_NAME}" not in default_prompt:
        errors.append(
            f"agents/openai.yaml default_prompt must mention ${EXPECTED_SKILL_NAME}"
        )


def validate_catalog(errors: list[str]) -> None:
    catalog_path = ROOT / "references/prompt-catalog.md"
    text = catalog_path.read_text(encoding="utf-8")
    recipe_ids = re.findall(r"^\| (M\d+|\d+) \|", text, flags=re.MULTILINE)
    counts = Counter(recipe_ids)

    duplicates = sorted(
        (recipe_id for recipe_id, count in counts.items() if count > 1),
        key=lambda value: (value.startswith("M"), int(value.lstrip("M"))),
    )
    missing = sorted(
        EXPECTED_RECIPE_IDS - set(recipe_ids),
        key=lambda value: (value.startswith("M"), int(value.lstrip("M"))),
    )
    unexpected = sorted(set(recipe_ids) - EXPECTED_RECIPE_IDS)

    if duplicates:
        errors.append(f"Duplicate recipe IDs: {', '.join(duplicates)}")
    if missing:
        errors.append(f"Missing recipe IDs: {', '.join(missing)}")
    if unexpected:
        errors.append(f"Unexpected recipe IDs: {', '.join(unexpected)}")
    if len(recipe_ids) != 125:
        errors.append(f"Expected 125 catalog rows, found {len(recipe_ids)}")


def markdown_files_to_check() -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "SKILL.md"]
    for directory in ("references", "examples"):
        paths.extend(sorted((ROOT / directory).glob("*.md")))
    return paths


def validate_local_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

    for path in markdown_files_to_check():
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if (
                not target
                or target.startswith(("http://", "https://", "mailto:", "#"))
            ):
                continue

            relative_target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / relative_target).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(
                    f"{path.relative_to(ROOT)}: link escapes repository ({target})"
                )
            elif not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: missing local link target ({target})"
                )


def validate_examples(errors: list[str]) -> None:
    for path in sorted((ROOT / "examples").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "Fictional example." not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing fictional-example label")
        if "No real participants" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing real-data disclaimer")
        if "**Evidence mode:**" not in text:
            errors.append(f"{path.relative_to(ROOT)}: missing evidence-mode label")


def validate_public_copy(errors: list[str]) -> None:
    for relative_path in sorted(PUBLIC_COPY_FILES):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if "\N{EM DASH}" in text:
            errors.append(f"{relative_path}: contains a banned em dash")


def main() -> int:
    errors: list[str] = []

    validate_required_files(errors)
    validate_skill_metadata(errors)
    validate_catalog(errors)
    validate_local_links(errors)
    validate_examples(errors)
    validate_public_copy(errors)

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Skill validation passed")
    print("- Required files present")
    print("- Skill and agent metadata valid")
    print("- 125 unique prompt recipes present")
    print("- Local Markdown links resolve")
    print("- Examples are labeled as fictional")
    print("- Public copy contains no em dashes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
