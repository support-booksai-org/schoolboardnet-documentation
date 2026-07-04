<!-- fullWidth: false tocVisible: false tableWrap: true -->
---
title: Screenshot Capture Standard
document: Volume 0 – Documentation Standards
author: schoolboardnet, LLC
version: 1.0.0
status: Approved
last_updated: YYYY-MM-DD
---

# Screenshot Capture Standard

## Purpose

This document establishes the official standards for capturing screenshots used throughout the schoolboard.net Documentation Suite.

Following these standards ensures that every screenshot has a consistent appearance, remains easy to update, and can be reused throughout the Administrator Guide, Knowledge Base, Technical Reference, and BooksAI training library.

---

# Documentation Principle

Every screenshot should appear as though it was captured by the same person on the same computer using the same software.

Consistency is more important than perfection.

---

# Standard Capture Environment

| Item               | Standard                            |
| ------------------ | ----------------------------------- |
| Browser            | Dia                                 |
| Website            | demo10.schoolboard.net              |
| Browser Zoom       | 100%                                |
| Theme              | Light                               |
| Window Width       | 1600 pixels                         |
| Window Height      | 1200 pixels                         |
| Monitor Scaling    | Default                             |
| Browser Sidebar    | Hidden                              |
| Bookmarks Bar      | Hidden                              |
| Browser Extensions | Disabled unless required            |
| Login              | Documentation Administrator account |

---

# Dia Browser Profile

Create a dedicated Dia profile named:

```
schoolboard.net Documentation
```

Use this profile only for documentation work.

The profile should remain logged into the demo site whenever possible.

---

# Browser Window

Always capture screenshots using the same browser window size.

Recommended size:

```
1600 × 1200
```

Do not maximize the browser.

A consistent window size ensures:

- menus appear in the same position
- tables wrap consistently
- forms remain identical
- screenshots can be replaced without affecting documentation layout

---

# Snagit Workflow

Snagit is the official screenshot tool.

Every screenshot begins in Snagit.

Workflow:

```
Dia Browser

↓

Snagit Capture

↓

Save .snagx project

↓

Export PNG

↓

Review

↓

Approve

↓

Publish
```

---

# Screenshot Types

Three versions of every screenshot may exist.

## Raw

Original capture.

No annotations.

No editing.

Location

```
assets/screenshots/raw
```

---

## Annotated

Arrows

Callouts

Highlights

Step numbers

Location

```
assets/screenshots/annotated
```

---

## Approved

Final publication version.

Location

```
assets/screenshots/approved
```

---

# Source Files

Snagit project files are considered source code.

Never edit exported PNG files.

Always edit the original Snagit project.

Location

```
assets/source/snagx
```

---

# Naming Standard

Every screenshot shall follow this format.

```
SB-USR-002-add-user-v01.png
```

Where

SB

Schoolboard.net

USR

Users section

002

Sequential screenshot number

add-user

Description

v01

Version

---

# Scrolling Screens

Use Snagit's scrolling capture whenever practical.

Recommended for:

- User lists
- Permissions
- Configuration
- Revision History
- Search Results
- Notification History
- Long Agendas

Avoid scrolling capture for:

- Dialog boxes
- Confirmation windows
- Pop-up messages
- Small forms

---

# Before Capturing

Verify:

✓ Correct browser profile

✓ Correct account

✓ Correct district

✓ Browser zoom is 100%

✓ Browser window is 1600×1200

✓ No browser notifications

✓ No personal information visible

✓ No passwords

✓ No unnecessary tabs

✓ Light theme enabled

---

# After Capturing

Complete the following tasks.

## Save the Snagit project

```
assets/source/snagx
```

---

## Export PNG

```
assets/screenshots/raw
```

---

## Rename Screenshot

Example

```
SB-USR-002-add-user-v01.png
```

---

## Update Screenshot Inventory

Open

```
docs/screenshot-inventory/users.md
```

Update:

- Screenshot ID
- Title
- Navigation
- Alt Text
- Status
- Capture Date
- Software Version
- Notes

---

## Update Master Screenshot Register

Open

```
docs/screenshot-inventory/master-screenshot-register.md
```

Update

Status

Capture Date

Software Version

Last Updated

---

# Screenshot Quality Checklist

Before approving a screenshot verify:

☐ Correct page

☐ Correct browser size

☐ Correct zoom

☐ Correct filename

☐ Correct version

☐ No confidential information

☐ No spelling errors

☐ No browser warnings

☐ No temporary data

☐ No unnecessary whitespace

☐ Image is sharp

☐ Image is readable

☐ Alt Text completed

☐ Screenshot Inventory updated

☐ Master Screenshot Register updated

---

# Best Practices

Capture the entire workflow rather than isolated screens.

Capture after entering realistic sample information.

Use meaningful examples.

Avoid Lorem Ipsum whenever possible.

Keep screenshots current with each software release.

When the user interface changes, increment the screenshot version.

Never overwrite an older screenshot.

---

# Administrator Notes

The Description field should be used to display user-friendly file names on agendas.

The file name should remain consistent and follow the official File Naming Standard.

Use version numbers whenever replacing uploaded files to improve indexing reliability.

Avoid spaces and special punctuation in filenames.

---

# Revision History

| Version | Date       | Description                         |
| ------- | ---------- | ----------------------------------- |
| 1.0.0   | 2026-07-01 | Initial Screenshot Capture Standard |
