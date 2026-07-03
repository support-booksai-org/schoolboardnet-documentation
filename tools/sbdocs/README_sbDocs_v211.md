# sbDocs v2.1.1 LTS

This release fixes the v2.1 validation noise.

## What changed

- Default validation now checks only user-facing documentation pages.
- Internal Markdown files under `docs/assets/` and capture-session/tool folders are skipped by default.
- Repair now adds missing standard metadata and missing standard sections to user-facing pages.
- Leading HTML comments before YAML front matter are moved below the front matter.
- Full validation including assets is still available as menu item 13.

## Install

Copy these into your `tools/sbdocs` folder:

- `sbdocs_v211.py` → rename to `sbdocs.py`
- `config_v211.yaml` → rename to `config.yaml`
- `run-sbdocs_v211.command` → rename to `run-sbdocs.command`

Then run menu item:

`5. Repair User Pages + Validate`
