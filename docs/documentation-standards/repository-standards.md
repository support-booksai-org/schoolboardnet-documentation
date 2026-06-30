---
title: Repository Standards
status: Draft
version: 0.1.1
---

# Repository Standards

The `schoolboardnet-docs` repository is the official source for schoolboard.net documentation.

## Repository root

The repository root is the `schoolboardnet-docs` folder.

## Required folders

| Folder | Purpose |
|---|---|
| `docs/` | Markdown source files used by MkDocs. |
| `docs/assets/` | Images, logos, screenshots, and downloadable assets used in documentation. |
| `scripts/` | Helper scripts for setup, preview, build, and cleanup. |
| `templates/` | Reusable Markdown templates. |
| `tools/` | Future documentation utilities. |
| `site/` | Generated website output. This folder is not committed. |

## Rule

Do not edit generated output in `site/`. All documentation changes must be made in Markdown source files under `docs/`.
