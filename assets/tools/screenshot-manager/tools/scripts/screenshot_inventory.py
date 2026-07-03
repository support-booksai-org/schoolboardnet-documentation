#!/usr/bin/env python3
"""
Screenshot inventory scanner for schoolboard.net MkDocs documentation.

Run from the root of schoolboardnet-docs:

    python3 tools/screenshot-manager/tools/scripts/screenshot_inventory.py

It scans docs/*.md files for assets/screenshots references and writes:

    docs/capture-sessions/screenshot-inventory.md
"""

from pathlib import Path
import re
from collections import defaultdict

ROOT = Path.cwd()
DOCS = ROOT / "docs"
OUT = DOCS / "capture-sessions" / "screenshot-inventory.md"

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+assets/screenshots/[^)]+)\)")


def normalize(path: str) -> str:
    path = path.strip().split("#", 1)[0].split("?", 1)[0]
    marker = "assets/screenshots/"
    if marker in path:
        return marker + path.split(marker, 1)[1]
    return path


def main() -> None:
    if not DOCS.exists():
        raise SystemExit("Could not find docs/ folder. Run this from the schoolboardnet-docs root.")

    inventory = defaultdict(list)

    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in IMAGE_RE.findall(text):
            img = normalize(match)
            inventory[img].append(str(md.relative_to(ROOT)))

    OUT.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Screenshot Inventory",
        "",
        "Generated from Markdown references. Do not manually edit unless needed.",
        "",
    ]

    if not inventory:
        lines += ["No screenshot references found.", ""]
    else:
        for img, used_in in sorted(inventory.items()):
            lines.append(f"## `{img}`")
            lines.append("")
            lines.append("Used in:")
            lines.append("")
            for page in sorted(set(used_in)):
                lines.append(f"- `{page}`")
            lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
