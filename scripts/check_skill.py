#!/usr/bin/env python3
"""Check standalone Skill references, pinned provenance and local links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    manifest = json.loads((ROOT / "UPSTREAM.json").read_text(encoding="utf-8"))
    commit = manifest["commit"]
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Source revision must be an exact Git commit")
    source_base = manifest["repository"] + "/blob/" + commit + "/"
    expected_methods = {
        f"references/{name}{language}.md"
        for name in ("subagents-and-review-loop", "quality-gates")
        for language in ("", ".zh-CN")
    }
    entries = manifest.get("files")
    if not isinstance(entries, list) or not all(
        isinstance(item, dict) and isinstance(item.get("path"), str)
        for item in entries
    ):
        raise ValueError("Source manifest must list each bundled method exactly once")
    paths = [item["path"] for item in entries]
    if len(paths) != len(expected_methods) or set(paths) != expected_methods:
        raise ValueError("Source manifest must list each bundled method exactly once")
    for item in entries:
        path = (ROOT / item["path"]).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError("Reference path is outside the Skill")
        text = path.read_text(encoding="utf-8")
        original = text.replace("](" + source_base, "](../")
        for content, field in ((text, "bundled_sha256_lf"), (original, "source_sha256_lf")):
            if hashlib.sha256(content.encode("utf-8")).hexdigest() != item[field]:
                raise ValueError("Reference differs from provenance: " + item["path"])
    for language in ("", ".zh-CN"):
        text = (ROOT / ("SKILL" + language + ".md")).read_text(encoding="utf-8")
        if not text.startswith("---\nname: research-review\ndescription: "):
            raise ValueError("Invalid Skill frontmatter")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", path.read_text(encoding="utf-8")):
            link = urlsplit(target)
            if link.scheme or link.netloc or not link.path:
                continue
            resolved = (path.parent / unquote(link.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                raise ValueError(f"{path.name}: invalid local reference {target}")
    print("Skill entrypoints, bundled methods, provenance and local links verified.")


if __name__ == "__main__":
    main()
