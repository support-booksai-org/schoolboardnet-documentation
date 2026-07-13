#!/usr/bin/env python3
"""Build the included dependency-free static review site from MkDocs Markdown."""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

NAV = [
    ("Quick Start", "index.md"),
    ("Sign in and accounts", "sign-in.md"),
    ("Find a meeting", "find-a-meeting.md"),
    ("Review an agenda", "review-an-agenda.md"),
    ("Public and private materials", "materials.md"),
    ("Search and print", "search-and-print.md"),
    ("Accessibility and help", "accessibility-and-help.md"),
    ("Meeting checklist", "meeting-checklist.md"),
    ("Reference and review notes", "reference.md"),
]


def strip_front_matter(text: str) -> tuple[dict[str, str], str]:
    meta: dict[str, str] = {}
    if not text.startswith("---\n"):
        return meta, text
    _, block, body = text.split("---\n", 2)
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, body


def slug_for(filename: str) -> str:
    return "" if filename == "index.md" else Path(filename).stem


def output_url(filename: str) -> str:
    slug = slug_for(filename)
    return "index.html" if not slug else f"{slug}/index.html"


def relative_root(filename: str) -> str:
    return "" if filename == "index.md" else "../"


def rewrite_href(target: str, current: str) -> str:
    if target.startswith(("http://", "https://", "#", "mailto:")):
        return target
    if target.endswith(".md"):
        return relative_root(current) + output_url(target)
    return target


def inline_markup(text: str, current: str) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\x00{len(placeholders)-1}\x00"

    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{m.group(1)}</code>"), text)
    text = re.sub(
        r"\[([^]]+)\]\(([^)]+)\)",
        lambda m: stash(f'<a href="{html.escape(rewrite_href(m.group(2), current), quote=True)}">{m.group(1)}</a>'),
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    for idx, value in enumerate(placeholders):
        text = text.replace(f"\x00{idx}\x00", value)
    return text


def render_markdown(text: str, current: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    table_rows: list[list[str]] = []
    idx = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            joined = " ".join(x.strip() for x in paragraph)
            out.append(f"<p>{inline_markup(joined, current)}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    def flush_table() -> None:
        nonlocal table_rows
        if not table_rows:
            return
        header, *body = table_rows
        out.append("<table><thead><tr>" + "".join(f"<th>{inline_markup(c, current)}</th>" for c in header) + "</tr></thead><tbody>")
        for row in body:
            out.append("<tr>" + "".join(f"<td>{inline_markup(c, current)}</td>" for c in row) + "</tr>")
        out.append("</tbody></table>")
        table_rows = []

    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()

        if stripped.startswith("<div") or stripped.startswith("</div") or (stripped.startswith("<a ") and stripped.endswith("</a>")):
            flush_paragraph(); close_list(); flush_table()
            out.append(line)
            idx += 1
            continue

        if stripped.startswith("!!! "):
            flush_paragraph(); close_list(); flush_table()
            match = re.match(r'!!!\s+(\w+)(?:\s+"([^"]+)")?', stripped)
            kind, title = match.groups() if match else ("note", "Note")
            body: list[str] = []
            idx += 1
            while idx < len(lines) and (lines[idx].startswith("    ") or not lines[idx].strip()):
                if lines[idx].strip(): body.append(lines[idx].strip())
                idx += 1
            out.append(f'<div class="admonition {kind}"><p class="admonition-title">{html.escape(title or kind.title())}</p><p>{inline_markup(" ".join(body), current)}</p></div>')
            continue

        image = re.fullmatch(r"!\[([^]]*)\]\(([^)]+)\)(?:\{[^}]*\})?", stripped)
        if image:
            flush_paragraph(); close_list(); flush_table()
            alt, src = image.groups()
            out.append(f'<img class="doc-screenshot" src="{relative_root(current)}{html.escape(src, quote=True)}" alt="{html.escape(alt, quote=True)}">')
            idx += 1
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph(); close_list()
            cells = [x.strip() for x in stripped.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                table_rows.append(cells)
            idx += 1
            continue
        else:
            flush_table()

        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            flush_paragraph(); close_list()
            level = len(heading.group(1))
            title = heading.group(2)
            anchor = re.sub(r"[^a-z0-9]+", "-", re.sub(r"[*_`]", "", title).lower()).strip("-")
            out.append(f'<h{level} id="{anchor}">{inline_markup(title, current)}</h{level}>')
            idx += 1
            continue

        item = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        bullet = re.match(r"^-\s+(.+)$", stripped)
        if item or bullet:
            flush_paragraph()
            desired = "ol" if item else "ul"
            if list_type != desired:
                close_list(); list_type = desired; out.append(f"<{desired}>")
            value = (item or bullet).group(2 if item else 1)
            checkbox = re.match(r"\[([ xX])\]\s+(.+)", value)
            if checkbox:
                checked = " checked" if checkbox.group(1).lower() == "x" else ""
                value = f'<input type="checkbox" disabled{checked}> {inline_markup(checkbox.group(2), current)}'
            else:
                value = inline_markup(value, current)
            out.append(f"<li>{value}</li>")
            idx += 1
            continue

        if not stripped:
            flush_paragraph(); close_list(); flush_table(); idx += 1; continue

        paragraph.append(stripped)
        idx += 1

    flush_paragraph(); close_list(); flush_table()
    return "\n".join(out)


def page_template(title: str, description: str, body: str, current: str) -> str:
    root = relative_root(current)
    nav_html = "".join(
        f'<li><a class="{"active" if name == current else ""}" href="{root}{output_url(name)}">{html.escape(label)}</a></li>'
        for label, name in NAV
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <title>{html.escape(title)} | schoolboard.net Board Member Help</title>
  <link rel="stylesheet" href="{root}assets/stylesheets/extra.css">
</head>
<body data-root="{root}">
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header">
    <button class="menu-button" type="button" aria-expanded="false" aria-controls="site-navigation">Menu</button>
    <a class="brand" href="{root}index.html"><strong>schoolboard.net</strong><span>Board Member Help</span></a>
    <div class="site-search">
      <label for="doc-search">Search Board Member help</label>
      <input id="doc-search" type="search" placeholder="Search Board Member help" autocomplete="off">
      <div id="search-results" class="search-results" role="listbox"></div>
    </div>
  </header>
  <div class="site-shell">
    <nav id="site-navigation" class="site-nav" aria-label="Documentation">
      <h2>Board Member Help</h2>
      <ul>{nav_html}</ul>
    </nav>
    <div class="content-wrap">
      <main id="main-content" class="doc-content">{body}</main>
      <footer class="page-footer">Version 1.0 review · schoolboard.net Board Member documentation</footer>
    </div>
  </div>
  <script src="{root}assets/javascripts/search-index.js"></script>
  <script src="{root}assets/javascripts/site.js"></script>
</body>
</html>"""


def main() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    shutil.copytree(DOCS / "assets", SITE / "assets")
    search_index = []
    for label, filename in NAV:
        meta, markdown = strip_front_matter((DOCS / filename).read_text(encoding="utf-8"))
        title = meta.get("title", label)
        description = meta.get("description", "schoolboard.net Board Member help")
        body = render_markdown(markdown, filename)
        destination = SITE / output_url(filename)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(page_template(title, description, body, filename), encoding="utf-8")
        plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
        search_index.append({"title": title, "description": description, "text": plain, "url": output_url(filename)})
    index_js = "window.__DOC_SEARCH__ = " + json.dumps(search_index, ensure_ascii=False) + ";\n"
    (SITE / "assets/javascripts/search-index.js").write_text(index_js, encoding="utf-8")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(NAV)} pages in {SITE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
