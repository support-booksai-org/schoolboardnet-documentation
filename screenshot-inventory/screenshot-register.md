<!-- fullWidth: false tocVisible: false tableWrap: true -->
---
title: Master Screenshot Register
description: Master inventory of every screenshot used throughout the schoolboard.net Documentation Suite.
author: schoolboardnet, LLC
product: schoolboard.net
document_type: Master Screenshot Register
version: 1.0.0
status: Active
last_updated: YYYY-MM-DD
---

# Master Screenshot Register

## Purpose

The Master Screenshot Register is the official inventory of every screenshot used throughout the schoolboard.net Documentation Suite.

It helps documentation authors:

- Track every screenshot.
- Prevent duplicate screenshots.
- Identify screenshots that require updating after software changes.
- Verify screenshot approval status.
- Locate where screenshots are used.
- Maintain consistency across all documentation.

---

# Screenshot Status

| Status    | Description                                                   |
| --------- | ------------------------------------------------------------- |
| Planned   | Screenshot has been identified but has not yet been captured. |
| Captured  | Screenshot has been captured but has not yet been reviewed.   |
| Annotated | Screenshot has been annotated with callouts or highlights.    |
| Approved  | Screenshot has been approved for publication.                 |
| Archived  | Screenshot is retained for historical reference.              |
| Obsolete  | Screenshot no longer represents the current software.         |

---

# Documentation Priority

| Priority | Description                            |
| -------- | -------------------------------------- |
| Critical | Required for Version 1 documentation.  |
| High     | Strongly recommended.                  |
| Medium   | Helpful but optional.                  |
| Low      | Rarely referenced or advanced feature. |

---

# Screenshot Register

| ID        | Section         | Title     | Filename                                   | Software Version | Status   | Priority | Used In                    | Capture Date | Owner     | Last Updated |
| --------- | --------------- | --------- | ------------------------------------------ | ---------------- | -------- | -------- | -------------------------- | ------------ | --------- | ------------ |
| SB-GS-001 | Getting Started | Home Page | SB-GS-001-schoolboardnet-home-page-v01.png | 10.4.1           | Approved | Critical | Welcome to schoolboard.net | 2026-07-03   | Mark Fien | 2026-07-03   |
| SB-ADM-001 | Administration    | Dashboard           | SB-ADM-001-dashboard-v01.png      | 10.4.1           | Planned | Critical | Dashboard         |              |       |              |\
| SB-ADM-002 | Administration    | Administration Menu | SB-ADM-002-admin-menu-v01.png     | 10.4.1           | Planned | High     | Dashboard         |              |       |              |\
| SB-USR-001 | Users             | User List           | SB-USR-001-user-list-v01.png      | 10.4.1           | Planned | Critical | Users Overview    |              |       |              |\
| SB-USR-002 | Users             | Add User            | SB-USR-002-add-user-v01.png       | 10.4.1           | Planned | Critical | Add User          |              |       |              |\
| SB-USR-003 | Users             | Edit User           | SB-USR-003-edit-user-v01.png      | 10.4.1           | Planned | High     | Edit User         |              |       |              |\
| SB-USR-004 | Users             | Reset Password      | SB-USR-004-reset-password-v01.png | 10.4.1           | Planned | High     | Reset Password    |              |       |              |\
| SB-GRP-001 | Groups            | Group List          | SB-GRP-001-group-list-v01.png     | 10.4.1           | Planned | Critical | Groups Overview   |              |       |              |\
| SB-GRP-002 | Groups            | Add Group           | SB-GRP-002-add-group-v01.png      | 10.4.1           | Planned | High     | Add Group         |              |       |              |\
| SB-PER-001 | Permissions       | Permissions Page    | SB-PER-001-permissions-v01.png    | 10.4.1           | Planned | Critical | Permissions       |              |       |              |\
| SB-AGD-001 | Accordion Agendas | Agenda List         | SB-AGD-001-agenda-list-v01.png    | 10.4.1           | Planned | Critical | Accordion Agendas |              |       |              |\
| SB-EXP-001 | Expandable HTML   | Empty Editor        | SB-EXP-001-empty-editor-v01.png   | 10.4.1           | Planned | Critical | Expandable HTML   |              |       |              |

---

# Section Summary

| Section           | Inventory File     | Planned | Approved |
| ----------------- | ------------------ | ------: | -------: |
| Administration    | administration.md  | 0       | 0        |
| Users             | users.md           | 0       | 0        |
| Groups            | groups.md          | 0       | 0        |
| Permissions       | permissions.md     | 0       | 0        |
| Accordion Agendas | agendas.md         | 0       | 0        |
| Agenda Sections   | agenda-sections.md | 0       | 0        |
| Agenda Items      | agenda-items.md    | 0       | 0        |
| Expandable HTML   | expandable-html.md | 0       | 0        |
| Public Files      | public-files.md    | 0       | 0        |
| Private Files     | private-files.md   | 0       | 0        |
| Notifications     | notifications.md   | 0       | 0        |
| Revisions         | revisions.md       | 0       | 0        |
| Publishing        | publishing.md      | 0       | 0        |
| Printing          | printing.md        | 0       | 0        |
| Search            | search.md          | 0       | 0        |
| Accessibility     | accessibility.md   | 0       | 0        |
| Microsoft Word    | word.md            | 0       | 0        |
| Google Docs       | google-docs.md     | 0       | 0        |
| AI Conversion     | ai-conversion.md   | 0       | 0        |

---

# Screenshot Standards

Every screenshot shall:

- Be captured from **demo10.schoolboard.net** unless otherwise noted.
- Use Google Chrome.
- Be captured at 100% browser zoom.
- Use the light theme.
- Exclude personal or confidential information.
- Follow the official screenshot naming convention.
- Be recorded in the appropriate Screenshot Inventory file.
- Be reviewed before publication.

---

# Maintenance Notes

When a new version of schoolboard.net changes the user interface:

1. Identify affected screenshots using the **Software Version** column.
2. Capture replacement screenshots.
3. Increment the screenshot version (for example, `v01` to `v02`).
4. Update the corresponding Screenshot Inventory document.
5. Update this Master Screenshot Register.
6. Verify all affected documentation before publishing.

---

# Revision History

| Version | Date       | Author              | Description                         |
| ------- | ---------- | ------------------- | ----------------------------------- |
| 1.0.0   | YYYY-MM-DD | schoolboardnet, LLC | Initial Master Screenshot Register. |
