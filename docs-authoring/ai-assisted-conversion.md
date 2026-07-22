# AI-Assisted HTML Conversion

Approved AI tools can speed up the preparation of clean HTML, especially when source content comes from Google Docs or a PDF. They create a **working draft**, not a finished or automatically conforming document.

schoolboard.net currently recommends:

- **Gemini** as the starting workflow for cleaning Google Docs content and converting it to semantic HTML; and
- **Claude** as the preferred current starting workflow for converting PDFs to HTML because its results have generally required the least cleanup in our experience.

These recommendations may change as the tools change. Neither tool guarantees WCAG 2.1 conformance. The district remains responsible for reviewing the content and the published result.

## Recommended quick command

For a straightforward conversion, begin with:

```text
Convert to WCAG 2.1 A compatible HTML for input to a Drupal 10.4.1 content block.
```

This concise command has worked well as a starting point with both Gemini and Claude. Use the detailed prompts below when the source contains headings, lists, tables, images, scanned text, or information that must be reproduced exactly.

!!! note "Compatibility still requires review"
    This command requests HTML designed around WCAG 2.1 Level A practices; it does not certify the result. Review the generated HTML, compare it with the approved source, and test the saved Drupal content before publication.

!!! warning "Protect district information"
    Follow district policy and use only an approved AI account or service. Never upload confidential, private, attorney-client, student, personnel, executive-session, or otherwise restricted material unless the district has specifically approved that use.

## Google Docs cleanup with Gemini

Gemini can work with a Google Doc directly when the feature is available to the district's Google Workspace account. It is useful for removing unnecessary Google Docs formatting and producing a simpler HTML draft.

### Recommended workflow

1. Finalize and approve the Google Doc.
2. Resolve suggestions, comments, placeholders, and drafting notes.
3. Confirm that the document contains no private or restricted information.
4. Ask Gemini to convert the approved content to clean semantic HTML.
5. Copy only the HTML portion of the response.
6. Review the HTML against the approved Google Doc.
7. Paste it into the appropriate public or private Expandable HTML field.
8. Save in Draft Mode and review the saved agenda.

### Suggested Gemini prompt

For simple material, use the [recommended quick command](#recommended-quick-command). For greater control, use this expanded prompt:

```text
Convert this approved Google Docs content into clean semantic HTML for a
schoolboard.net Expandable HTML field.

Preserve the wording, meaning, names, dates, numbers, quotations, and order.
Do not summarize, rewrite, or invent content.

Remove Google Docs formatting and unnecessary inline styles. Use only the
HTML needed for logical headings, paragraphs, ordered and unordered lists,
descriptive links, and simple data tables with proper header cells. Do not
use scripts, layout tables, font tags, page headers, page footers, page
numbers, empty paragraphs for spacing, or styling that carries no meaning.

Do not invent alternative text. Mark any image, complex table, unclear
reading order, or other item that requires a human accessibility decision.

Return:
1. one HTML code block containing the converted content; and
2. a separate Review Items list outside the HTML block.
```

!!! tip "Use the source as the authority"
    If Gemini changes a name, date, number, quotation, policy statement, or other approved wording, correct the HTML to match the source. A cleaner sentence is not necessarily the authorized sentence.

## PDF conversion with Claude

Claude can analyze uploaded PDFs, including visual elements in supported PDFs and models. In schoolboard.net's experience to date, Claude has generally produced the cleanest first draft for PDF-to-HTML conversion. This is a practical preference, not a guarantee that every PDF will convert accurately or accessibly.

### Recommended workflow

1. Confirm that the PDF is the approved version.
2. Determine whether the PDF contains scanned pages, handwriting, complex tables, charts, columns, or unusual reading order.
3. Confirm that the PDF contains no information prohibited from the approved AI service.
4. Upload the PDF and request semantic HTML.
5. Compare the response with the PDF page by page.
6. Correct extraction, OCR, reading-order, table, and link errors.
7. Add human-written alternative text where an image conveys information.
8. Paste the reviewed HTML into the correct Expandable HTML field.
9. Save in Draft Mode and review the saved agenda.

### Suggested Claude prompt

For simple material, use the [recommended quick command](#recommended-quick-command). For greater control, use this expanded prompt:

```text
Convert the attached approved PDF into clean semantic HTML for a
schoolboard.net Expandable HTML field.

Preserve the exact wording, meaning, names, dates, numbers, quotations, and
reading order. Do not summarize, rewrite, or invent missing content. Clearly
flag text that is uncertain because of scanning, OCR, layout, or image quality.

Use logical headings, paragraphs, ordered and unordered lists, descriptive
links, and simple data tables with proper header cells. Do not use scripts,
layout tables, font tags, page headers, page footers, page numbers, empty
paragraphs for spacing, or unnecessary inline styling.

Do not invent alternative text. Mark images, charts, complex tables, unclear
reading order, and other items that require a human accessibility decision.

Return:
1. one HTML code block containing the converted content; and
2. a separate Review Items list outside the HTML block.
```

!!! important "Scanned PDFs need extra review"
    OCR can silently change names, dates, dollar amounts, page order, punctuation, and legal language. Compare every converted section with the approved PDF and do not guess when the source is unclear.

## Required human review

Before publication, confirm that:

- every statement matches the approved source;
- names, dates, times, dollar amounts, vote language, quotations, and legal text are exact;
- heading levels are logical;
- numbered and bulleted content uses real lists;
- links are descriptive and open the intended destination;
- simple tables have correct row and column headers;
- complex tables have been simplified or given another accessible presentation;
- informative images have human-reviewed alternative text;
- reading order makes sense without the original visual layout;
- no comments, prompts, AI notes, placeholders, or invented content remain;
- public and private placement is correct; and
- the saved page works on desktop and mobile and can be used with a keyboard.

WCAG conformance requires more than generated markup. Accessibility evaluation uses automated, semi-automated, and manual testing, and the published content still requires informed human judgment.
