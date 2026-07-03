# schoolboard.net Screenshot Manager v1

This package simplifies screenshot naming, capture-session logging, and screenshot inventory.

## Core idea

Do not manually track every screenshot in a large registry.

Use:

1. **Feature folders** for screenshots.
2. **Simple descriptive filenames**.
3. **One capture-session log per session**.
4. **An optional inventory script** that scans Markdown files and reports where screenshots are used.

## Place this package here

```text
schoolboardnet-docs/tools/screenshot-manager/
```

## Screenshot folders

Use this structure in your main documentation project:

```text
schoolboardnet-docs/assets/screenshots/
├── dashboard/
├── users/
├── groups/
├── meetings/
├── books/
├── notifications/
└── settings/
```

## Capture session logs

Place session logs here:

```text
schoolboardnet-docs/docs/capture-sessions/
```

Example:

```text
2026-07-02-dashboard.md
```

## Filename convention

Use:

```text
<feature>-<screen>.png
```

Examples:

```text
dashboard-home.png
users-list.png
users-add.png
users-reset-password.png
groups-add-members.png
meetings-accordion-agenda.png
```

Only add a version if the screen meaningfully changes:

```text
users-add-v2.png
```

## Daily workflow

1. Start Keyboard Maestro Documentation Workbench.
2. Pick the feature you are documenting.
3. Save screenshots into that feature folder.
4. Use the capture session template.
5. Run the optional inventory script when you want a list of where screenshots are used.

