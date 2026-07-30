# AI-Assisted HTML Conversion

Approved AI tools can speed up the preparation of clean HTML, especially when source content comes from Google Docs, a Microsoft Word DOCX file, or a PDF. They create a **working draft**, not a finished or automatically conforming document.

schoolboard.net currently recommends:

- **Gemini** as the starting workflow for cleaning content that already lives in Google Docs; and
- **Claude** as the current starting workflow for file-based DOCX and PDF conversion.

Both services currently accept DOCX uploads, subject to account features and district configuration. The recommendation above keeps the workflow simple; it does not establish that one service will produce better results for every document. These recommendations may change as the tools change. Neither tool guarantees WCAG 2.1 conformance. The district remains responsible for selecting an approved service, reviewing the complete content, and evaluating the published result.

## Recommended quick command

For a straightforward conversion, begin with:

```text
Convert to WCAG 2.1 Level A and Level AA compatible HTML for input to a Drupal 10.4.1 content block.
```

This concise command has worked well as a starting point with both Gemini and Claude. Use the detailed prompts below when the source contains headings, lists, tables, images, scanned text, or information that must be reproduced exactly.

!!! note "Compatibility still requires review"
    This command requests HTML designed around WCAG 2.1 Level A and Level AA practices; it does not certify the result. Review the generated HTML, compare it with the approved source, and test the saved Drupal content before publication.

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

## Microsoft Word DOCX conversion with Claude

For an approved Microsoft Word file, schoolboard.net currently recommends Claude as the first file-based conversion workflow. This separates Word conversion from the Gemini workflow used for material already maintained in Google Docs.

Claude and Gemini both currently accept DOCX uploads. If Claude is not approved or available, Gemini may be used with the same requirements and human review. For a recurring document type, districts may compare a representative, nonconfidential sample in their approved tools and adopt the workflow that preserves the source most accurately with the least corrective work.

!!! important "DOCX images require separate review"
    Claude currently extracts text from non-PDF documents and does not interpret embedded DOCX images. Inspect every image, chart, diagram, text box, SmartArt item, equation, and visually arranged element in Word. Supply human-written alternative text or an accessible text equivalent where needed. Do not assume that an omitted visual was decorative.

### Prepare the Word file

1. Confirm that the DOCX file is the final approved version.
2. Accept or reject tracked changes and remove resolved comments, placeholders, and drafting notes.
3. Use Word's built-in heading, list, link, and table structure.
4. Run **Review > Check Accessibility** or the Accessibility Assistant available in the district's version of Word.
5. Remove print-only headers, footers, page numbers, and repeated decorative elements that do not belong in the web content.
6. Confirm that the file contains no confidential or restricted information prohibited from the approved AI service.
7. Save a separate approved conversion copy so the source record is preserved.

### Recommended workflow

1. Upload the approved DOCX conversion copy to Claude.
2. Request clean semantic HTML using the prompt below.
3. Compare the response with the Word file from beginning to end.
4. Restore any content omitted from text boxes, columns, headers, footers, images, charts, or other visual objects when that content belongs on the web page.
5. Correct headings, lists, links, tables, reading order, names, dates, numbers, quotations, and legal language.
6. Add human-reviewed alternative text or an accessible text explanation for informative visuals.
7. Follow [Move the converted HTML into schoolboard.net](#move-the-converted-html-into-schoolboardnet).
8. Save in Draft Mode and compare the saved agenda with the approved Word source.

### Suggested DOCX prompt

For simple material, use the [recommended quick command](#recommended-quick-command). For greater control, use this expanded prompt:

```text
Convert the attached approved Microsoft Word DOCX file into clean semantic
HTML for a schoolboard.net Expandable HTML field.

Preserve the exact wording, meaning, names, dates, numbers, quotations, list
order, and logical reading order. Do not summarize, rewrite, or invent content.

Remove Microsoft Word formatting, classes, metadata, and unnecessary inline
styles. Use only the HTML needed for logical headings, paragraphs, ordered and
unordered lists, descriptive links, and simple data tables with proper header
cells. Do not use scripts, layout tables, font tags, page headers, page footers,
page numbers, empty paragraphs for spacing, or styling that carries no meaning.

Do not invent alternative text. Identify any image, chart, diagram, text box,
SmartArt object, complex table, unclear reading order, or other item that
requires a human accessibility decision. If an item cannot be extracted from
the DOCX file, flag its location instead of silently omitting it.

Return:
1. one HTML code block containing the converted content; and
2. a separate Review Items list outside the HTML block.
```

!!! tip "When Gemini is the approved DOCX tool"
    Upload the approved DOCX file to Gemini and use the same DOCX prompt. File-upload availability and limits can vary by account. Apply the same source comparison, privacy controls, visual-content review, browser review, and saved-agenda testing.

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

## Move the converted HTML into schoolboard.net

After Gemini or Claude creates the HTML, review it in a browser before placing it in the agenda.

1. Save or open the generated HTML in a web browser.
2. Review the displayed page for missing content, unexpected formatting, and obvious conversion errors.
3. Right-click the page and select **View Page Source** or **View Source**.
4. In the source view, copy the content beginning with the opening `<div>` and ending with its closing `</div>`.
5. Open the appropriate public or private **Expandable HTML** component in the agenda.
6. Select **Source** in the content editor toolbar.
    - On a wide screen, **Source** may appear as the far-right toolbar icon.
    - On a smaller window, open the **…** overflow menu to find it.
7. Paste the copied HTML into the Source editor.
8. Return to the normal editing view and confirm that the content appears correctly.
9. Save the agenda in Draft Mode.
10. Open the saved agenda, expand the content, and compare it with the approved source.

!!! note "The editor cleans pasted HTML"
    When HTML is pasted or saved, the editor may remove markup it considers unsupported or incompatible. This cleanup can remove unnecessary code, but it can also change the result. Always review the normal editing view and the saved agenda after pasting. If important content or structure disappears, correct the HTML using markup supported by the editor.

!!! warning "Copy only the intended content"
    Copy the intended content container from its opening `<div>` through the matching closing `</div>`. Do not copy the browser page's `<html>`, `<head>`, scripts, stylesheets, prompts, review notes, or other surrounding code.

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
- the editor did not remove or alter necessary content when the HTML was pasted or saved;
- public and private placement is correct; and
- the saved page works on desktop and mobile and can be used with a keyboard.

WCAG conformance requires more than generated markup. Accessibility evaluation uses automated, semi-automated, and manual testing, and the published content still requires informed human judgment.
