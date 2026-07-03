#!/usr/bin/env python3
"""schoolboard.net Documentation Workbench v0.1.1

Stable direction: Python + Dia + Snagit.

This helper starts capture sessions, creates/opens folders, creates simple
feature README files, tracks one .snagx source with multiple PNG exports,
and scans where screenshots are used in Markdown.
"""
from __future__ import annotations

import datetime as _dt
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("PyYAML is not installed. Run: python3 -m pip install -r requirements.txt")
    sys.exit(1)

APP_VERSION = "0.1.1"
CONFIG_FILE = Path(__file__).with_name("config.yaml")


def load_config() -> Dict[str, Any]:
    if not CONFIG_FILE.exists():
        print(f"Missing config: {CONFIG_FILE}")
        sys.exit(1)
    with CONFIG_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def run(cmd: List[str], check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def open_path(path: Path) -> None:
    if path.exists():
        run(["open", str(path)])
    else:
        print(f"Not found, cannot open: {path}")


def open_url(url: str, browser_app: Optional[str] = None) -> None:
    if browser_app:
        run(["open", "-a", browser_app, url])
    else:
        run(["open", url])


def activate_app(app_name: str) -> None:
    run(["open", "-a", app_name])


def resize_app(app_name: str, left: int, top: int, width: int, height: int) -> None:
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
        print("Window resize did not complete. This is usually an Accessibility permission issue.")
        print("Allow Terminal in System Settings > Privacy & Security > Accessibility.")
        if result.stderr.strip():
            print(result.stderr.strip())


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def choose_feature(features: Dict[str, Any]) -> str:
    keys = list(features.keys())
    print("\nChoose feature:\n")
    for i, key in enumerate(keys, 1):
        print(f"  {i}. {features[key].get('label', key)} ({key})")
    print("  0. Cancel")
    while True:
        choice = input("\nFeature number: ").strip()
        if choice == "0":
            raise KeyboardInterrupt
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return keys[int(choice) - 1]
        print("Please enter a valid number.")


def project_root(config: Dict[str, Any]) -> Path:
    return Path(config["project_root"]).expanduser()


def source_name(feature: Dict[str, Any]) -> str:
    return feature.get("source_snaq") or feature.get("base_snaq") or "source.snagx"


def feature_readme(root: Path, feature_key: str, feature: Dict[str, Any]) -> Path:
    snagx_dir = root / feature["snagx_dir"]
    ensure_dir(snagx_dir)
    path = snagx_dir / "README.md"
    if path.exists():
        return path
    exports = "\n".join(f"- `{x}`" for x in feature.get("suggested_exports", [])) or "-"
    content = f"""# {feature.get('label', feature_key)} Screenshot Source

## Purpose

This folder stores the editable Snagit source file for the **{feature.get('label', feature_key)}** screenshots.

## Source File

`{source_name(feature)}`

## PNG Exports

Export finished PNG files to:

`{feature['png_dir']}`

Suggested exports:

{exports}

## Workflow

1. Capture the base screen in Snagit.
2. Save the editable source as `{source_name(feature)}`.
3. Duplicate/annotate inside Snagit as needed.
4. Export final PNG files using the names above.
5. Run sbDocs inventory/validation before publishing.
"""
    path.write_text(content, encoding="utf-8")
    return path


def session_md(root: Path, session_dir: Path, feature_key: str, feature: Dict[str, Any]) -> Path:
    today = _dt.date.today().isoformat()
    out = root / session_dir / f"{today}-{feature_key}.md"
    ensure_dir(out.parent)
    if out.exists():
        return out
    exports = feature.get("suggested_exports", [])
    suggested_block = "\n".join([f"- [ ] `{name}`" for name in exports]) or "- [ ]"
    content = f"""# Capture Session: {feature.get('label', feature_key)}

**Date:** {today}  
**Feature:** {feature_key}  
**Browser:** Dia  
**Requested Window:** 1600 × 1200  
**Zoom:** 100%  
**Capture Tool:** Snagit  

## Source Snagit File

`{feature['snagx_dir']}/{source_name(feature)}`

## PNG Exports

{suggested_block}

## Session Notes

- One editable `.snagx` may create several final `.png` exports.
- Keep filenames lowercase and descriptive.
- Do not manually maintain a giant Used In registry; use sbDocs inventory scan.

## Open Questions / Follow-up

-
"""
    out.write_text(content, encoding="utf-8")
    return out


def prepare_feature(root: Path, config: Dict[str, Any], feature_key: str) -> Dict[str, Path]:
    feature = config["features"][feature_key]
    snagx_dir = root / feature["snagx_dir"]
    png_dir = root / feature["png_dir"]
    docs_file = root / feature.get("docs_file", "docs")
    ensure_dir(snagx_dir)
    ensure_dir(png_dir)
    ensure_dir(docs_file.parent)
    readme = feature_readme(root, feature_key, feature)
    session = session_md(root, Path(config.get("session_dir", "docs/capture-sessions")), feature_key, feature)
    return {"snagx_dir": snagx_dir, "png_dir": png_dir, "docs_file": docs_file, "readme": readme, "session": session}


def print_feature_summary(feature_key: str, feature: Dict[str, Any], paths: Dict[str, Path]) -> None:
    print("\nFeature ready:")
    print(f"  Feature:          {feature.get('label', feature_key)}")
    print(f"  URL:              {feature.get('url', '')}")
    print(f"  Snagit source:    {paths['snagx_dir'] / source_name(feature)}")
    print(f"  PNG exports:      {paths['png_dir']}")
    print(f"  Session log:      {paths['session']}")
    print("\nSuggested PNG exports:")
    for name in feature.get("suggested_exports", []):
        marker = "✓" if (paths["png_dir"] / name).exists() else " "
        print(f"  [{marker}] {name}")


def start_session(config: Dict[str, Any]) -> None:
    root = project_root(config)
    if not root.exists():
        print("Project root does not exist:")
        print(root)
        print("\nEdit tools/sbdocs/config.yaml and set project_root to the real mounted path.")
        return
    try:
        feature_key = choose_feature(config.get("features", {}))
    except KeyboardInterrupt:
        print("Cancelled.")
        return
    feature = config["features"][feature_key]
    paths = prepare_feature(root, config, feature_key)

    browser = config.get("browser_app", "Dia")
    snagit = config.get("snagit_app", "Snagit")
    win = config.get("window", {})

    print("\nStarting capture session...")
    activate_app(browser)
    resize_app(browser, int(win.get("left", 0)), int(win.get("top", 25)), int(win.get("width", 1600)), int(win.get("height", 1200)))
    open_url(feature.get("url", config.get("site_url", "https://demo10.schoolboard.net")), browser)
    activate_app(snagit)
    open_path(paths["snagx_dir"])
    open_path(paths["png_dir"])
    open_path(paths["session"])
    if paths["docs_file"].exists():
        open_path(paths["docs_file"])
    open_path(paths["readme"])
    print_feature_summary(feature_key, feature, paths)


def continue_session(config: Dict[str, Any]) -> None:
    root = project_root(config)
    try:
        feature_key = choose_feature(config.get("features", {}))
    except KeyboardInterrupt:
        print("Cancelled.")
        return
    feature = config["features"][feature_key]
    paths = prepare_feature(root, config, feature_key)
    open_path(paths["snagx_dir"])
    open_path(paths["png_dir"])
    open_path(paths["session"])
    if paths["docs_file"].exists():
        open_path(paths["docs_file"])
    print_feature_summary(feature_key, feature, paths)


def validate_feature(config: Dict[str, Any]) -> None:
    root = project_root(config)
    try:
        feature_key = choose_feature(config.get("features", {}))
    except KeyboardInterrupt:
        print("Cancelled.")
        return
    feature = config["features"][feature_key]
    paths = prepare_feature(root, config, feature_key)
    print(f"\nValidation for {feature.get('label', feature_key)}\n")
    snagx_path = paths["snagx_dir"] / source_name(feature)
    print(f"Source .snagx: {'FOUND' if snagx_path.exists() else 'missing'} — {snagx_path}")
    for name in feature.get("suggested_exports", []):
        p = paths["png_dir"] / name
        print(f"PNG: {'FOUND' if p.exists() else 'missing'} — {name}")


def inventory(config: Dict[str, Any]) -> None:
    root = project_root(config)
    screenshots = root / "assets/screenshots"
    docs = root / "docs"
    if not screenshots.exists():
        print(f"No screenshot folder found: {screenshots}")
        return
    image_files = sorted(screenshots.rglob("*.png"))
    md_files = sorted(docs.rglob("*.md")) if docs.exists() else []
    print(f"\nScreenshot inventory / Used In scan ({len(image_files)} PNG files)\n")
    for img in image_files:
        rel = img.relative_to(root)
        rel_posix = str(rel).replace(os.sep, "/")
        used = []
        for md in md_files:
            try:
                text = md.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if img.name in text or rel_posix in text:
                used.append(str(md.relative_to(root)).replace(os.sep, "/"))
        print(f"- {rel_posix}")
        if used:
            for u in used:
                print(f"    used in: {u}")
        else:
            print("    used in: not found")


def open_project(config: Dict[str, Any]) -> None:
    open_path(project_root(config))


def open_config() -> None:
    open_path(CONFIG_FILE)


def main() -> None:
    config = load_config()
    while True:
        print(f"\nschoolboard.net Documentation Workbench v{APP_VERSION}")
        print("=" * 52)
        print("1. Start capture session")
        print("2. Continue/open existing feature session")
        print("3. Validate feature screenshots")
        print("4. Screenshot inventory / Used In scan")
        print("5. Open project root")
        print("6. Open config.yaml")
        print("0. Exit")
        try:
            choice = input("\nChoose: ").strip()
        except EOFError:
            print("\nThis tool needs to run in Terminal, not directly inside Automator.")
            return
        if choice == "1":
            start_session(config)
        elif choice == "2":
            continue_session(config)
        elif choice == "3":
            validate_feature(config)
        elif choice == "4":
            inventory(config)
        elif choice == "5":
            open_project(config)
        elif choice == "6":
            open_config()
        elif choice == "0":
            return
        else:
            print("Please choose a valid menu item.")


if __name__ == "__main__":
    main()
