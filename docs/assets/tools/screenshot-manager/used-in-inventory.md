# Used-In Inventory

Do not manually maintain a large screenshot registry.

Instead, let the documentation files tell us where screenshots are used.

## Markdown image format

Use standard Markdown image links:

```markdown
![Dashboard home page](../assets/screenshots/dashboard/dashboard-home.png)
```

or the correct relative path for the page location.

## How inventory works

The optional script scans Markdown files under:

```text
docs/
```

and finds references to:

```text
assets/screenshots/
```

It produces a report listing:

- screenshot filename
- screenshot folder
- Markdown files where it is used

## Why this is better

You avoid updating two places every time a screenshot changes.

The Markdown page is the source of truth.

