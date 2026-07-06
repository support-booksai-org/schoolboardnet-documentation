---
title: Tribal Knowledge
document: Documentation Project
author: schoolboardnet, LLC
version: 1.0.0
status: Living Document
last_updated: 2026-07-03
---

# Tribal Knowledge

## Purpose

This document records practical knowledge gained while developing, documenting, and supporting the schoolboard.net platform.

These notes may not belong in customer documentation but are valuable to future developers, technical writers, and support staff.

This is a living document and should be updated whenever a new best practice or lesson is discovered.

---

# Documentation Standards

## Versioning

Documentation versions and software versions are tracked separately.

Every documentation release receives its own version number and release notes.

---

## Releases

Every documentation release shall include:

- Version number
- Title
- Objective
- Deliverables
- Build instructions
- Git commit recommendation
- Release notes
- Changelog

---

# File Naming

## Uploaded Files

Avoid spaces in filenames.

Recommended

```
board-packet-v01.pdf
```

Avoid

```
Board Packet Final.pdf
```

---

## Allowed Characters

Recommended

- Letters
- Numbers
- Hyphen (-)
- Underscore (_)

Avoid

- Spaces
- Apostrophes
- Quotes
- Ampersands
- Parentheses
- Commas
- Multiple periods

---

## Version Numbers

Always include a version number when uploading files.

Examples

```
budget-v01.pdf

budget-v02.pdf

minutes-v03.pdf
```

Never overwrite an existing file using the same filename.

Version numbers help:

- Search indexing
- Browser caching
- Revision tracking
- User confidence

---

## Agenda Attachments

Always use the **Description** field.

Users should see descriptive titles rather than filenames.

Good

```
2026–2027 Proposed Budget
```

Not

```
budget-v03-final.pdf
```

---

# Microsoft Word

Always use Heading styles.

Avoid manual font formatting.

Use built-in lists.

Avoid multiple blank lines.

Tables should include header rows.

Use descriptive hyperlink text.

---

# Google Docs

Use Heading styles.

Avoid manual indentation.

Remove unnecessary formatting before exporting.

Verify document structure before conversion.

---

# HTML Conversion

Review AI-generated HTML before publishing.

Verify heading hierarchy.

Check tables.

Check lists.

Confirm hyperlinks.

Remove unnecessary inline styles.

---

# Expandable HTML

Prefer Expandable HTML over PDF whenever practical.

Advantages

- Accessible
- Searchable
- Mobile friendly
- Better indexing
- Easier updates

---

# Accessibility

Never communicate using color alone.

Provide descriptive link text.

Every image must include meaningful alt text.

Maintain proper heading order.

Use tables only for tabular data.

---

# Screenshots

Capture from:

```
demo10.schoolboard.net
```

Browser

Dia

Window

1600 × 900

Zoom

100%

Cursor

Hidden

Export

PNG

Keep Snagit project files.

---

# Documentation

Write in plain language.

Explain the reason as well as the procedure.

One task per section whenever practical.

Use numbered steps for procedures.

Use bullet lists for reference material.

---

# Knowledge Base

Every documentation chapter should have a matching Knowledge Base article.

Knowledge Base articles should include:

- Related Articles
- Troubleshooting
- Administrator Notes
- Best Practices
- AI Tips

---

# BooksAI

Documentation should answer questions rather than simply describe features.

Each article becomes part of the BooksAI training corpus.

Good documentation improves AI responses.

---

# Things We Never Do

- Store passwords in documentation.
- Capture confidential information.
- Publish screenshots containing personal information.
- Overwrite uploaded files without versioning.
- Depend solely on PDFs for public-facing information.
- Use "click here" as link text.

---

# Ideas for Future Improvement

Record ideas that are not yet implemented but may improve the platform or documentation.

Examples

- Interactive tutorials.
- Embedded videos.
- Animated workflows.
- AI-generated release notes.
- Automated screenshot validation.

---

# Demo10 Information

- All passwords are demo users is username[exclaimation_point]demo (does not apply to support or somebody)
- Move all demo agendas to private group after demos
- User Protect seems broken - Group Administrator can see Administrator accounts in People

---

# Public Questions

- I found my name in documents online doing a search and want it removed, what do I do?

# Revision History

| Version | Date | Author | Description |
|----------|------|--------|-------------|
| 1.0.0 | 2026-07-03 | schoolboardnet, LLC | Initial Tribal Knowledge document. |