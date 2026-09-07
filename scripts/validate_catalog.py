#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "tools.json"
README = ROOT / "README.md"
TOOLS_MD = ROOT / "TOOLS.md"
SERVER = ROOT / "server.json"


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)} is not valid JSON: {exc}") from exc


def stated_tool_counts(text: str) -> list[int]:
    return [
        int(value)
        for value in re.findall(
            r"(?<!\d)(\d+)\s+(?:[A-Za-z][A-Za-z-]*\s+){0,4}tools\b",
            text,
            flags=re.IGNORECASE,
        )
    ]


def main() -> int:
    errors: list[str] = []

    try:
        catalog = load_json(CATALOG)
        server = load_json(SERVER)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    if not isinstance(catalog, list) or not catalog:
        errors.append("catalog/tools.json must be a non-empty JSON array")
        catalog = []

    names: list[str] = []
    required_annotations = {
        "title",
        "readOnlyHint",
        "destructiveHint",
        "idempotentHint",
        "openWorldHint",
    }

    for index, tool in enumerate(catalog):
        prefix = f"catalog/tools.json[{index}]"
        if not isinstance(tool, dict):
            errors.append(f"{prefix} must be an object")
            continue

        name = tool.get("name")
        description = tool.get("description")
        input_schema = tool.get("inputSchema")
        annotations = tool.get("annotations")

        if not isinstance(name, str) or not name.strip():
            errors.append(f"{prefix}.name must be a non-empty string")
        else:
            names.append(name)

        if not isinstance(description, str) or not description.strip():
            errors.append(f"{prefix}.description must be a non-empty string")

        if not isinstance(input_schema, dict) or input_schema.get("type") != "object":
            errors.append(f"{prefix}.inputSchema must be an object schema")

        if not isinstance(annotations, dict):
            errors.append(f"{prefix}.annotations must be an object")
            continue

        missing = sorted(required_annotations - annotations.keys())
        if missing:
            errors.append(f"{prefix}.annotations missing: {', '.join(missing)}")

        if not isinstance(annotations.get("title"), str) or not annotations.get("title", "").strip():
            errors.append(f"{prefix}.annotations.title must be a non-empty string")

        for key in required_annotations - {"title"}:
            if key in annotations and not isinstance(annotations[key], bool):
                errors.append(f"{prefix}.annotations.{key} must be boolean")

    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append(f"duplicate tool names: {', '.join(duplicates)}")

    tool_count = len(catalog)

    try:
        readme_text = README.read_text(encoding="utf-8")
        tools_text = TOOLS_MD.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: could not read documentation: {exc}")
        return 1

    for path, text in ((README, readme_text), (TOOLS_MD, tools_text)):
        counts = stated_tool_counts(text)
        if not counts:
            errors.append(f"{path.name} does not state a tool count")
        for count in counts:
            if count != tool_count:
                errors.append(
                    f"{path.name} states {count} tools but catalog/tools.json contains {tool_count}"
                )

    server_description = server.get("description", "") if isinstance(server, dict) else ""
    if isinstance(server_description, str):
        for count in stated_tool_counts(server_description):
            if count != tool_count:
                errors.append(
                    f"server.json description states {count} tools but catalog/tools.json contains {tool_count}"
                )

    documented_rows = re.findall(r"^\| `([^`]+)` \| (read|write) \|", tools_text, flags=re.MULTILINE)
    documented_names = [name for name, _kind in documented_rows]

    if len(documented_names) != tool_count:
        errors.append(
            f"TOOLS.md documents {len(documented_names)} tool rows but catalog/tools.json contains {tool_count}"
        )

    missing_from_docs = sorted(set(names) - set(documented_names))
    extra_in_docs = sorted(set(documented_names) - set(names))
    if missing_from_docs:
        errors.append(f"TOOLS.md is missing tools: {', '.join(missing_from_docs)}")
    if extra_in_docs:
        errors.append(f"TOOLS.md has unknown tools: {', '.join(extra_in_docs)}")

    by_name = {tool.get("name"): tool for tool in catalog if isinstance(tool, dict) and isinstance(tool.get("name"), str)}
    for name, kind in documented_rows:
        tool = by_name.get(name)
        if not tool:
            continue
        annotations = tool.get("annotations")
        if not isinstance(annotations, dict) or not isinstance(annotations.get("readOnlyHint"), bool):
            continue
        expected_kind = "read" if annotations["readOnlyHint"] else "write"
        if kind != expected_kind:
            errors.append(f"TOOLS.md marks {name} as {kind}, expected {expected_kind}")

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Catalog validation passed: {tool_count} tools")
    return 0


if __name__ == "__main__":
    sys.exit(main())
