---
title: Screenshot Standard
document: Volume 0 – Documentation Standards
author: schoolboardnet, LLC
version: 1.0.0
status: Approved
applies_to: schoolboard.net Documentation Suite
last_updated: 2026-07-03
---

# Screenshot Standard

## Purpose

This document establishes the official screenshot standards for the schoolboard.net Documentation Suite.

Following these standards ensures every screenshot has a consistent appearance throughout the Administrator Training Guide, Technical Reference, Deployment Guide, Knowledge Base, and BooksAI training library.

---

# Guiding Principle

Every screenshot should appear as though it was captured:

- by the same person
- on the same computer
- using the same browser
- using the same capture tool

Consistency is more important than perfection.

---

# Standard Capture Environment

| Setting | Standard |
|----------|----------|
| Browser | Dia |
| Website | demo10.schoolboard.net |
| Browser Zoom | 100% |
| Browser Theme | Light |
| Window Size | **1600 × 900** |
| Capture Tool | Snagit |
| Export Format | PNG |
| Cursor | Hidden |
| Browser Chrome | Hidden unless required |
| Browser Bookmarks | Hidden |
| Browser Sidebar | Hidden |

---

# Screenshot Style

The schoolboard.net Documentation Suite uses three screenshot styles.

## Style A — Application (Default)

Used for approximately 90% of all documentation.

Characteristics

- Application only
- Browser chrome hidden
- Tight crop
- Clean layout
- No annotations
- Used for publication

Examples

- Dashboard
- Users
- Groups
- Agendas
- Search
- Notifications

---

## Style B — Browser

Used only when browser features are important.

Examples

- Login URL
- Browser settings
- Bookmark instructions

---

## Style C — Dialog Box

Used for:

- Confirmation dialogs
- Pop-up windows
- Settings dialogs

Crop tightly around the dialog.

---

# Cropping Standard

Crop tightly around the application.

Include approximately:

- 15–20 pixels above the application
- 15–20 pixels below the footer
- 15–20 pixels on the left
- 15–20 pixels on the right

Avoid excessive white space.

Do not crop controls.

---

# Screenshot Naming Standard

Every screenshot shall follow the naming convention:

```
SB-AAA-NNN-description-v01.png
```

Example

```
SB-USR-002-add-user-v01.png
```

Where

| Element | Description |
|----------|-------------|
| SB | schoolboard.net |
| AAA | Functional Area |
| NNN | Sequential Screenshot Number |
| description | Short descriptive name |
| v01 | Screenshot Version |

---

# Functional Area Codes

| Code | Area |
|------|------|
| GS | Getting Started |
| ADM | Administration |
| DASH | Dashboard |
| USR | Users |
| GRP | Groups |
| PER | Permissions |
| AGD | Accordion Agendas |
| SEC | Agenda Sections |
| ITM | Agenda Items |
| NITM | Nested Agenda Items |
| EXP | Expandable HTML |
| PF | Public Files |
| PRF | Private Files |
| NOT | Notifications |
| REV | Revisions |
| PUB | Publishing |
| SRCH | Search |
| PRT | Printing |
| ACC | Accessibility |
| WRD | Microsoft Word |
| GDOC | Google Docs |
| AI | AI Conversion |
| KB | Knowledge Base |
| QA | Quality Assurance |
| TECH | Technical Reference |

---

# Examples

```
SB-GS-001-home-page-v01.png

SB-DASH-001-dashboard-v01.png

SB-USR-003-add-user-v01.png

SB-GRP-002-edit-group-v01.png

SB-AGD-004-new-agenda-v01.png

SB-EXP-002-expandable-html-v01.png
```

---

# Screenshot Workflow

```
Dia Browser

↓

Capture using Snagit

↓

Save Snagit Project (.snagx)

↓

Export PNG

↓

Store Screenshot

↓

Update Screenshot Inventory

↓

Commit to GitHub
```

---

# Folder Structure

```
assets/

    source/
        snagx/

    screenshots/

        raw/

        annotated/

        approved/

        archive/
```

---

# Screenshot Inventory

Every published screenshot shall be recorded in the Screenshot Inventory.

Each entry should include:

- Screenshot ID
- Title
- Filename
- Alt Text
- Purpose
- Documentation Pages
- Notes

---

# Alt Text Standard

Alt text should describe what a user needs to understand.

Good

> Add User page showing account information, assigned groups, and permissions.

Poor

> Screenshot of Add User.

---

# Capture Checklist

Before capturing:

- □ Correct browser profile
- □ Demo site loaded
- □ Browser zoom 100%
- □ Browser window 1600 × 900
- □ Cursor hidden
- □ Notifications closed
- □ No personal information displayed

After capturing:

- □ Save Snagit project
- □ Export PNG
- □ Verify filename
- □ Update Screenshot Inventory
- □ Commit changes to GitHub

---

# Best Practices

- Capture realistic data.
- Avoid placeholder text whenever possible.
- Keep screenshots current.
- Never overwrite previous versions.
- Increment the screenshot version whenever the user interface changes.
- Capture one functional area at a time.
- Review screenshots before publication.

---

# Administrator Notes

The official screenshot library is considered part of the source documentation.

Snagit project files are the editable source.

PNG files are publication assets.

Always edit the Snagit project—not the exported PNG.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-03 | Initial Screenshot Standard. |