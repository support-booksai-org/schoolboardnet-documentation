# sbDocs Workbench v0.1.1

This is the working Python direction for schoolboard.net screenshot capture.

## What changed in v0.1.1

- Adds **Continue/open existing feature session**.
- Adds **Validate feature screenshots**.
- Creates a simple `README.md` inside each Snagit source folder.
- Supports the agreed workflow: **one `.snagx` source with several exported `.png` files**.
- Includes `run-sbdocs.command` for Terminal launching.

## Install / Update

Copy the contents of this package into:

```text
/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/tools/sbdocs
```

The folder should contain:

```text
sbdocs.py
config.yaml
requirements.txt
run-sbdocs.command
README.md
```

Install the dependency once:

```bash
cd "/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/tools/sbdocs"
python3 -m pip install -r requirements.txt
```

Run:

```bash
python3 sbdocs.py
```

or double-click:

```text
run-sbdocs.command
```

## Automator Launcher Script

Use this inside Automator > Application > Run Shell Script:

```bash
#!/bin/zsh
osascript <<'APPLESCRIPT'
tell application "Terminal"
    activate
    do script "cd '/Volumes/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/tools/sbdocs' && /usr/bin/python3 sbdocs.py"
end tell
APPLESCRIPT
```

## Dashboard model

Use one editable source:

```text
assets/source/snagx/dashboard/dashboard-home.snagx
```

Export multiple PNGs:

```text
assets/screenshots/dashboard/dashboard-home.png
assets/screenshots/dashboard/dashboard-login.png
assets/screenshots/dashboard/dashboard-search.png
assets/screenshots/dashboard/dashboard-upcoming-events.png
assets/screenshots/dashboard/dashboard-past-events.png
```

## Recommended first capture flow

1. Run sbDocs.
2. Choose `1. Start capture session`.
3. Choose `Dashboard / Home`.
4. Capture in Snagit and save the editable source as `dashboard-home.snagx`.
5. Annotate/export PNGs using the suggested names.
6. Run `3. Validate feature screenshots`.
7. Run `4. Screenshot inventory / Used In scan`.
