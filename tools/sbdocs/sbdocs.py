#!/usr/bin/env python3
"""schoolboard.net Documentation Workbench v2.1 LTS

Stable documentation workbench for MkDocs + Material, Dia, and Snagit.

Core LTS features:
- Stable YAML front matter page template (no HTML comments before front matter)
- New page wizard
- Front matter repair/validation
- Window size profiles
- Capture session launcher
- Screenshot inventory
- Local build/serve helpers
- Automatic backups before destructive or build actions
"""
from __future__ import annotations

import datetime as _dt
import os
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    print("PyYAML is not installed. Run: python3 -m pip install pyyaml")
    sys.exit(1)

APP_VERSION = "2.1.1 LTS"
CONFIG_FILE = Path(__file__).with_name("config.yaml")

REQUIRED_SECTIONS = ["Quick Summary", "Related Topics", "Revision History"]
REQUIRED_META = ["title", "description", "audience", "applies_to", "version", "status", "author"]
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]+\]\(([^)]+)\))")


def pause() -> None:
    input("\nPress Return to continue...")


def run(cmd: List[str], cwd: Optional[Path] = None, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True, capture_output=True, check=check)


def open_path(path: Path) -> None:
    if path.exists():
        subprocess.run(["open", str(path)])
    else:
        print(f"Not found: {path}")


def open_url(url: str, browser_app: Optional[str] = None) -> None:
    if browser_app:
        subprocess.run(["open", "-a", browser_app, url])
    else:
        subprocess.run(["open", url])


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"&", " and ", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "untitled"


def read_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        print(f"Missing config: {path}")
        sys.exit(1)
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def write_yaml(path: Path, data: Dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def load_config() -> Dict[str, Any]:
    cfg = read_yaml(CONFIG_FILE)
    cfg.setdefault("version", APP_VERSION)
    cfg.setdefault("default_profile", "documentation")
    cfg.setdefault("window_profiles", {})
    cfg.setdefault("features", {})
    return cfg


def save_config(cfg: Dict[str, Any]) -> None:
    write_yaml(CONFIG_FILE, cfg)


def project_root(cfg: Dict[str, Any]) -> Path:
    return Path(cfg["project_root"]).expanduser()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def active_window(cfg: Dict[str, Any]) -> Dict[str, Any]:
    profile_name = cfg.get("default_profile", "documentation")
    profiles = cfg.get("window_profiles", {})
    if profile_name in profiles:
        return profiles[profile_name]
    return cfg.get("window", {"left": 0, "top": 25, "width": 1600, "height": 1200})


def resize_app(app_name: str, win: Dict[str, Any]) -> None:
    left, top = int(win.get("left", 0)), int(win.get("top", 25))
    width, height = int(win.get("width", 1600)), int(win.get("height", 1200))
    script = f'''
tell application "{app_name}"
    activate
end tell
delay 0.8
tell application "System Events"
    tell process "{app_name}"
        if (count of windows) > 0 then
            set position of front window to {{{left}, {top}}}
            set size of front window to {{{width}, {height}}}
        end if
    end tell
end tell
'''
    result = run(["osascript", "-e", script])
    if result.returncode != 0:
        print("Window resize did not complete. Check System Settings > Privacy & Security > Accessibility.")
        if result.stderr.strip():
            print(result.stderr.strip())


def get_front_matter(text: str) -> Tuple[Optional[Dict[str, Any]], str, bool]:
    if not text.startswith("---\n"):
        return None, text, False
    end = text.find("\n---", 4)
    if end == -1:
        return None, text, False
    raw = text[4:end]
    body = text[end + 4:].lstrip("\n")
    try:
        meta = yaml.safe_load(raw) or {}
        return meta, body, True
    except Exception:
        return None, body, True


def page_template(title: str, description: str = "", audience: Optional[List[str]] = None,
                  applies_to: str = "schoolboard.net", status: str = "Draft") -> str:
    audience = audience or ["District Administrator", "Group Administrator", "Board Clerk", "Administrative Assistant"]
    today = _dt.date.today().isoformat()
    meta = {
        "title": title,
        "description": description or f"Documentation page for {title}.",
        "audience": audience,
        "applies_to": applies_to,
        "version": "1.0",
        "status": status,
        "author": "schoolboard.net, LLC",
        "review_cycle": "Annual",
        "last_reviewed": today,
        "fullWidth": False,
        "tocVisible": True,
        "tableWrap": True,
    }
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm}\n---\n\n# {title}\n\n## Quick Summary\n\nAdd a short plain-language summary here.\n\n## Main Content\n\nAdd the page content here.\n\n## Related Topics\n\n- Add related pages here.\n\n## Revision History\n\n| Date | Change | Author |\n| --- | --- | --- |\n| {today} | Initial draft. | schoolboard.net, LLC |\n"


def list_sections(cfg: Dict[str, Any]) -> Dict[str, str]:
    sections = cfg.get("sections") or {
        "getting-started": "Getting Started",
        "dashboard": "Dashboard",
        "users": "Users",
        "groups": "Groups",
        "meetings": "Meetings / Agendas",
        "notifications": "Notifications",
        "settings": "Settings",
        "administration": "Administration",
        "reference": "Reference",
    }
    return sections


def choose_from(keys: List[str], labels: List[str], prompt: str) -> Optional[str]:
    print()
    for i, label in enumerate(labels, 1):
        print(f"  {i}. {label}")
    print("  0. Cancel")
    while True:
        choice = input(f"\n{prompt}: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return keys[int(choice) - 1]
        print("Please enter a valid number.")


def create_page(cfg: Dict[str, Any]) -> None:
    root = project_root(cfg)
    title = input("\nPage title: ").strip()
    if not title:
        print("Cancelled.")
        return
    description = input("Description (optional): ").strip()
    sections = list_sections(cfg)
    key = choose_from(list(sections.keys()), list(sections.values()), "Section")
    if not key:
        print("Cancelled.")
        return
    filename = input(f"Filename [{slugify(title)}.md]: ").strip() or f"{slugify(title)}.md"
    if not filename.endswith(".md"):
        filename += ".md"
    path = root / "docs" / key / filename
    if path.exists():
        print(f"File already exists: {path}")
        open_path(path)
        return
    ensure_dir(path.parent)
    path.write_text(page_template(title, description), encoding="utf-8")
    print(f"\nCreated: {path}")
    add_nav = input("Open mkdocs.yml so you can add it to navigation? [Y/n]: ").strip().lower()
    if add_nav != "n":
        open_path(root / "mkdocs.yml")
    open_path(path)


def repair_front_matter_file(path: Path, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        return False
    # Common failure: HTML comments before YAML front matter.
    match = re.match(r"\s*(<!--.*?-->\s*)+---\n", text, flags=re.S)
    if not match:
        return False
    comments = re.findall(r"<!--.*?-->", match.group(0), flags=re.S)
    rest = text[match.end()-4:]  # begins at ---\n
    end = rest.find("\n---", 4)
    if end == -1:
        return False
    new_text = rest[:end+4] + "\n\n" + "\n".join(comments) + "\n" + rest[end+4:].lstrip("\n")
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def validate_file(path: Path, root: Path) -> List[str]:
    issues: List[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["Cannot read as UTF-8"]
    meta, body, has_fm = get_front_matter(text)
    if not has_fm:
        issues.append("Missing or invalid YAML front matter at very top of file")
    elif meta is None:
        issues.append("YAML front matter could not be parsed")
    else:
        for k in REQUIRED_META:
            if k not in meta or meta.get(k) in (None, "", []):
                issues.append(f"Missing metadata: {k}")
    h1s = re.findall(r"^#\s+", body, flags=re.M)
    if len(h1s) == 0:
        issues.append("Missing H1 heading")
    elif len(h1s) > 1:
        issues.append("More than one H1 heading")
    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", body, flags=re.M):
            issues.append(f"Missing section: {section}")
    # Heading jumps.
    levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s+", body, flags=re.M)]
    for prev, cur in zip(levels, levels[1:]):
        if cur > prev + 1:
            issues.append("Heading level jumps too far")
            break
    # Missing local images.
    for img in IMG_RE.findall(body):
        if img.startswith(("http://", "https://", "#", "mailto:")):
            continue
        img_path = (path.parent / img.split("#")[0].split("?")[0]).resolve()
        if not img_path.exists():
            issues.append(f"Missing image: {img}")
    return issues


def should_validate_md(md: Path, root: Path, cfg: Dict[str, Any]) -> bool:
    """Validate only user-facing documentation pages by default.

    Asset/tool/capture-session markdown files are useful internal notes, but they do
    not need the full production page template. This avoids hundreds of noisy
    warnings from README/INDEX files under docs/assets.
    """
    rel = md.relative_to(root).as_posix()
    excludes = cfg.get("validation_excludes", [
        "docs/assets/",
        "docs/capture-sessions/",
        "docs/_archive/",
        "docs/.trash/",
    ])
    return not any(rel.startswith(x) for x in excludes)


def extract_title_from_body_or_path(body: str, path: Path) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", body, flags=re.M)
    if m:
        return m.group(1).strip()
    name = path.stem
    if name.lower() == "index":
        name = path.parent.name
    return name.replace("-", " ").replace("_", " ").title()


def ensure_page_structure(path: Path, dry_run: bool = False) -> bool:
    """Repair a Markdown file into the stable v2.1 LTS page structure.

    Safe repairs performed:
    - Move HTML comments that appear before YAML front matter to after the front matter.
    - Add front matter if missing.
    - Fill missing standard metadata fields.
    - Add Quick Summary, Related Topics, and Revision History sections when absent.
    """
    original = path.read_text(encoding="utf-8", errors="ignore")
    text = original

    # Move any leading HTML comments below YAML front matter.
    leading_comments = []
    while True:
        m = re.match(r"\s*(<!--.*?-->)\s*", text, flags=re.S)
        if not m:
            break
        leading_comments.append(m.group(1))
        text = text[m.end():]

    meta, body, has_fm = get_front_matter(text)
    if not has_fm or meta is None:
        body = text.lstrip("\n")
        meta = {}
    title = meta.get("title") or extract_title_from_body_or_path(body, path)
    today = _dt.date.today().isoformat()
    defaults = {
        "title": title,
        "description": f"Documentation page for {title}.",
        "audience": ["District Administrator", "Group Administrator", "Board Clerk", "Administrative Assistant"],
        "applies_to": "schoolboard.net",
        "version": "1.0",
        "status": "Draft",
        "author": "schoolboard.net, LLC",
        "review_cycle": "Annual",
        "last_reviewed": today,
        "fullWidth": False,
        "tocVisible": True,
        "tableWrap": True,
    }
    changed = (text != original)
    for k, v in defaults.items():
        if k not in meta or meta.get(k) in (None, "", []):
            meta[k] = v
            changed = True

    if not re.search(r"^#\s+", body, flags=re.M):
        body = f"# {title}\n\n" + body.lstrip("\n")
        changed = True

    if leading_comments:
        comment_block = "\n".join(leading_comments).strip() + "\n\n"
        if comment_block.strip() not in body:
            body = comment_block + body.lstrip("\n")
            changed = True

    if not re.search(r"^##\s+Quick Summary\s*$", body, flags=re.M):
        body = re.sub(r"(^#\s+.+?\s*$)", r"\1\n\n## Quick Summary\n\nAdd a short plain-language summary here.", body, count=1, flags=re.M)
        changed = True
    if not re.search(r"^##\s+Related Topics\s*$", body, flags=re.M):
        body = body.rstrip() + "\n\n## Related Topics\n\n- Add related pages here.\n"
        changed = True
    if not re.search(r"^##\s+Revision History\s*$", body, flags=re.M):
        body = body.rstrip() + f"\n\n## Revision History\n\n| Date | Change | Author |\n| --- | --- | --- |\n| {today} | Standardized page structure. | schoolboard.net, LLC |\n"
        changed = True

    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    new_text = f"---\n{fm}\n---\n\n{body.lstrip()}"
    if new_text != original:
        changed = True
    if changed and not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return changed


def validate_docs(cfg: Dict[str, Any], repair: bool = False, full: bool = False) -> None:
    root = project_root(cfg)
    docs = root / "docs"
    if not docs.exists():
        print(f"Missing docs folder: {docs}")
        return
    fixed = 0
    skipped = 0
    all_issues: List[Tuple[Path, List[str]]] = []
    for md in sorted(docs.rglob("*.md")):
        if not full and not should_validate_md(md, root, cfg):
            skipped += 1
            continue
        if repair:
            # keep old comment-specific repair for compatibility, then do full structure repair
            if repair_front_matter_file(md):
                fixed += 1
            elif ensure_page_structure(md):
                fixed += 1
        issues = validate_file(md, root)
        if issues:
            all_issues.append((md, issues))
    print("\nValidation Report")
    print("=================")
    if skipped:
        print(f"Skipped internal asset/tool markdown files: {skipped}")
    if fixed:
        print(f"Files repaired: {fixed}")
    if not all_issues:
        print("PASS — no issues found in user-facing documentation pages.")
        return
    print(f"Issues found: {sum(len(i) for _, i in all_issues)} in {len(all_issues)} files\n")
    for path, issues in all_issues[:100]:
        print(path.relative_to(root))
        for issue in issues:
            print(f"  - {issue}")
    if len(all_issues) > 100:
        print(f"\n...and {len(all_issues)-100} more files.")

def backup_project(cfg: Dict[str, Any]) -> None:
    root = project_root(cfg)
    backup_root = root / cfg.get("backup_dir", "backup")
    stamp = _dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    dest = backup_root / stamp
    ensure_dir(dest)
    for name in ["mkdocs.yml", "config.yaml"]:
        src = root / name
        if src.exists():
            shutil.copy2(src, dest / name)
    for name in ["docs", "assets"]:
        src = root / name
        if src.exists():
            shutil.copytree(src, dest / name, dirs_exist_ok=True)
    print(f"Backup created: {dest}")


def build_docs(cfg: Dict[str, Any], clean: bool = False, serve: bool = False) -> None:
    root = project_root(cfg)
    if input("Create backup first? [Y/n]: ").strip().lower() != "n":
        backup_project(cfg)
    if clean and (root / "site").exists():
        shutil.rmtree(root / "site")
    cmd = [sys.executable, "-m", "mkdocs", "serve"] if serve else [sys.executable, "-m", "mkdocs", "build"]
    print("\nRunning:", " ".join(cmd))
    if serve:
        subprocess.run(cmd, cwd=str(root))
    else:
        result = run(cmd, cwd=root)
        print(result.stdout)
        if result.stderr.strip():
            print(result.stderr)
        print("Build finished." if result.returncode == 0 else f"Build failed: {result.returncode}")


def screenshot_inventory(cfg: Dict[str, Any]) -> None:
    root = project_root(cfg)
    screenshots = root / "assets" / "screenshots"
    docs = root / "docs"
    files = sorted([p for p in screenshots.rglob("*.png")]) if screenshots.exists() else []
    used: Dict[str, List[Path]] = {}
    for md in docs.rglob("*.md") if docs.exists() else []:
        text = md.read_text(encoding="utf-8", errors="ignore")
        for img in IMG_RE.findall(text):
            used.setdefault(Path(img).name, []).append(md)
    print("\nScreenshot Inventory")
    print("====================")
    print(f"PNG files: {len(files)}")
    unused = [p for p in files if p.name not in used]
    print(f"Unused PNG files by filename: {len(unused)}")
    if unused:
        print("\nFirst unused files:")
        for p in unused[:50]:
            print(" -", p.relative_to(root))


def source_name(feature: Dict[str, Any]) -> str:
    return feature.get("source_snaq") or feature.get("source_snagx") or feature.get("base_snaq") or "source.snagx"


def choose_feature(cfg: Dict[str, Any]) -> Optional[str]:
    features = cfg.get("features", {})
    if not features:
        print("No features defined in config.yaml")
        return None
    keys = list(features.keys())
    labels = [features[k].get("label", k) for k in keys]
    return choose_from(keys, labels, "Feature number")


def prepare_feature(root: Path, cfg: Dict[str, Any], feature_key: str) -> Dict[str, Path]:
    f = cfg["features"][feature_key]
    snagx_dir = root / f["snagx_dir"]
    png_dir = root / f["png_dir"]
    docs_file = root / f.get("docs_file", "docs")
    session_dir = root / cfg.get("session_dir", "docs/capture-sessions")
    ensure_dir(snagx_dir); ensure_dir(png_dir); ensure_dir(docs_file.parent); ensure_dir(session_dir)
    session = session_dir / f"{_dt.date.today().isoformat()}-{feature_key}.md"
    if not session.exists():
        exports = "\n".join(f"- [ ] `{x}`" for x in f.get("suggested_exports", [])) or "- [ ]"
        win = active_window(cfg)
        session.write_text(f"""# Capture Session: {f.get('label', feature_key)}

**Date:** {_dt.date.today().isoformat()}  
**Feature:** {feature_key}  
**Browser:** {cfg.get('browser_app', 'Dia')}  
**Requested Window:** {win.get('width')} × {win.get('height')}  
**Capture Tool:** {cfg.get('snagit_app', 'Snagit')}  

## Source Snagit File

`{f['snagx_dir']}/{source_name(f)}`

## PNG Exports

{exports}

## Notes

-
""", encoding="utf-8")
    return {"snagx_dir": snagx_dir, "png_dir": png_dir, "docs_file": docs_file, "session": session}


def start_capture(cfg: Dict[str, Any]) -> None:
    root = project_root(cfg)
    key = choose_feature(cfg)
    if not key:
        return
    feature = cfg["features"][key]
    paths = prepare_feature(root, cfg, key)
    browser = cfg.get("browser_app", "Dia")
    win = active_window(cfg)
    print(f"\nStarting capture: {feature.get('label', key)}")
    print(f"Window profile: {cfg.get('default_profile')} ({win.get('width')}×{win.get('height')})")
    open_url(feature.get("url", cfg.get("site_url", "https://demo10.schoolboard.net")), browser)
    resize_app(browser, win)
    subprocess.run(["open", "-a", cfg.get("snagit_app", "Snagit")])
    open_path(paths["snagx_dir"]); open_path(paths["png_dir"]); open_path(paths["session"])
    if paths["docs_file"].exists():
        open_path(paths["docs_file"])


def window_profiles(cfg: Dict[str, Any]) -> None:
    profiles = cfg.get("window_profiles", {})
    keys = list(profiles.keys())
    labels = [f"{profiles[k].get('description', k)} — {profiles[k].get('width')}×{profiles[k].get('height')}" + ("  [current]" if k == cfg.get("default_profile") else "") for k in keys]
    print("\nWindow Profiles")
    key = choose_from(keys + ["custom"], labels + ["Custom size..."], "Profile")
    if not key:
        return
    if key == "custom":
        name = slugify(input("Profile name: ").strip() or "custom")
        width = int(input("Width: ").strip())
        height = int(input("Height: ").strip())
        profiles[name] = {"description": name.replace("-", " ").title(), "left": 0, "top": 25, "width": width, "height": height}
        cfg["window_profiles"] = profiles
        key = name
    cfg["default_profile"] = key
    cfg["window"] = {k: profiles[key].get(k) for k in ["left", "top", "width", "height"]}
    save_config(cfg)
    print(f"Saved default profile: {key}")


def project_health(cfg: Dict[str, Any]) -> None:
    root = project_root(cfg)
    docs = list((root / "docs").rglob("*.md")) if (root / "docs").exists() else []
    imgs = list((root / "assets" / "screenshots").rglob("*.png")) if (root / "assets" / "screenshots").exists() else []
    print("\nProject Health")
    print("==============")
    print(f"Project root: {root}")
    print(f"Markdown pages: {len(docs)}")
    print(f"Screenshot PNGs: {len(imgs)}")
    print(f"Window profile: {cfg.get('default_profile')}")
    print(f"Browser: {cfg.get('browser_app', 'Dia')}")
    print(f"Snagit: {cfg.get('snagit_app', 'Snagit')}")


def open_existing_page(cfg: Dict[str, Any]) -> None:
    root = project_root(cfg)
    query = input("Search page title/filename: ").strip().lower()
    pages = sorted((root / "docs").rglob("*.md"))
    matches = [p for p in pages if query in p.name.lower() or query in p.read_text(encoding="utf-8", errors="ignore").lower()[:2000]] if query else pages[:50]
    if not matches:
        print("No matches.")
        return
    keys = [str(i) for i in range(len(matches))]
    labels = [str(p.relative_to(root)) for p in matches[:30]]
    choice = choose_from(keys[:30], labels, "Page")
    if choice is not None:
        open_path(matches[int(choice)])


def main() -> None:
    cfg = load_config()
    while True:
        print(textwrap.dedent(f"""
        =========================================
         schoolboard.net Documentation Workbench
                    Version {APP_VERSION}
        =========================================

        Project
        -------
        1. Create Documentation Page
        2. Open Existing Page
        3. Build Documentation
        4. Validate Documentation
        5. Repair User Pages + Validate

        Screenshots
        -----------
        6. Capture Screenshot
        7. Screenshot Inventory

        Environment
        -----------
        8. Window Profiles
        9. Backup Project
        10. Project Health

        Utilities
        ---------
        11. Clean Build
        12. Local Preview / Serve
        13. Full Validation Including Assets
        Q. Quit
        """))
        choice = input("Selection: ").strip().lower()
        cfg = load_config()
        try:
            if choice == "1": create_page(cfg)
            elif choice == "2": open_existing_page(cfg)
            elif choice == "3": build_docs(cfg)
            elif choice == "4": validate_docs(cfg, repair=False)
            elif choice == "5": validate_docs(cfg, repair=True)
            elif choice == "6": start_capture(cfg)
            elif choice == "7": screenshot_inventory(cfg)
            elif choice == "8": window_profiles(cfg)
            elif choice == "9": backup_project(cfg)
            elif choice == "10": project_health(cfg)
            elif choice == "11": build_docs(cfg, clean=True)
            elif choice == "12": build_docs(cfg, serve=True)
            elif choice == "13": validate_docs(cfg, repair=False, full=True)
            elif choice in ("q", "quit", "exit"): break
            else: print("Please choose a valid menu item.")
        except KeyboardInterrupt:
            print("\nCancelled.")
        except Exception as exc:
            print(f"\nError: {exc}")
        if choice not in ("12", "q", "quit", "exit"):
            pause()


if __name__ == "__main__":
    main()
