<!-- fullWidth: false tocVisible: false tableWrap: true -->
# Appendix: Google Docs and PDF to Expandable HTML

Use this appendix when a district has an approved Google Doc or PDF that should become Expandable HTML in a schoolboard.net agenda.

## V1 conversion path

The standard v1 path is:

**Approved Google Doc or other source → PDF → Gemini → semantic HTML and Review Items → human review → Expandable HTML**

For a Google Doc, download the approved document as a PDF before conversion. Existing approved PDFs can enter the workflow at the PDF step.

This PDF-first approach provides one consistent input format, preserves visual layout information for review, and does not require Google Drive access or a separate DOCX conversion service.

!!! note "A PDF is an input, not proof of accessibility"\
Exporting a document as PDF does not make the PDF accessible, and AI-generated HTML is not automatically conforming. The PDF remains the approved comparison source while a person reviews and corrects the HTML draft.

## Prepare a Google Doc

Before downloading the PDF:

1. Confirm that the correct document and approved version are open.
2. Resolve comments and suggestions.
3. Remove placeholders, drafting notes, and print-only material that should not appear online.
4. Use real heading styles, numbered and bulleted lists, descriptive links, and simple data tables.
5. Verify names, dates, times, dollar amounts, quotations, and other exact information.
6. Review images, charts, diagrams, and tables that will require a human accessibility decision.
7. Confirm that the document contains no information prohibited from the approved AI service.

### Download the PDF

In Google Docs:

1. Select **File**.
2. Select **Download**.
3. Select **PDF Document (.pdf)**.
4. Give the file a meaningful name and preserve the approved Google Doc according to district policy.

## Prepare an existing PDF

Before conversion:

- confirm that the PDF is the approved version;
- determine whether pages are scanned or contain handwriting;
- identify columns, complex tables, charts, diagrams, text embedded in images, and unusual reading order;
- confirm that text can be selected or note that OCR will be required; and
- confirm that the PDF contains no confidential or restricted information prohibited from the approved AI service.

!!! warning "Protect district information"\
Use only an AI account or service approved by the district. Do not upload confidential, private, attorney-client, student, personnel, executive-session, or otherwise restricted material unless the district has specifically approved that use.

## Convert the PDF with Gemini

1. Open the district-approved Gemini account.
2. Upload the approved PDF.
3. Use the quick command below for a simple document, or use the detailed prompt for greater control.
4. Keep the PDF available for page-by-page comparison.

### Quick command

```text
Convert to WCAG 2.1 Level A and Level AA compatible HTML for input to a Drupal 10.4.1 content block.
```

### Detailed v1 prompt

```text
Convert the attached approved PDF into clean semantic HTML for a
schoolboard.net Expandable HTML field in Drupal 10.4.1.

Preserve the exact wording, meaning, names, dates, times, numbers, dollar
amounts, quotations, list order, and logical reading order. Do not summarize,
rewrite, correct, omit, or invent content. Clearly flag text that is uncertain
because of scanning, OCR, layout, image quality, or unclear source formatting.

Use logical headings, paragraphs, ordered and unordered lists, descriptive
links, and simple data tables. For data tables, use table, thead, tbody, th,
and appropriate scope attributes.

Do not use scripts, forms, iframes, layout tables, font tags, page headers,
page footers, page numbers, empty paragraphs for spacing, Markdown, or styling
that carries no meaning.

Do not invent alternative text. Do not silently omit images, charts, complex
tables, diagrams, signatures, or other non-text visual content. Identify each
such item in Review Items and describe what a human must decide, add, or
verify.

For a simple financial data table, preserve it as a semantic table. Apply
class="sbn-currency" only to financial amount header and data cells. Format
amounts exactly as supplied; do not calculate, normalize, or add currency
symbols, commas, or decimal places. Do not apply the class to dates, IDs,
counts, or ordinary numbers.

Return:
1. exactly one HTML code block containing only the converted content; and
2. a separate Review Items list outside the HTML block.
```

!!! important "The source controls"\
If the AI changes a name, date, number, quotation, policy statement, or other approved wording, correct the HTML to match the PDF. Do not accept a rewrite merely because it sounds clearer.

## Review the conversion

Compare the HTML with the PDF from beginning to end. Confirm that:

- every page and every required section is present;
- names, dates, times, dollar amounts, quotations, and legal language are exact;
- headings reflect the document structure rather than its visual size;
- numbered and bulleted content uses real lists;
- links are descriptive and point to the correct destination;
- tables have the correct reading order and header relationships;
- columns and text boxes appear in a logical reading order;
- OCR did not change words, punctuation, numbers, or page order;
- informative visuals have a human-written alternative or accessible explanation; and
- no prompt text, AI commentary, Review Items, Markdown markers, or invented content appears in the HTML.

## Move the HTML into Expandable HTML

1. Save or open the generated HTML in a web browser.
2. Review the displayed page for missing content and conversion errors.
3. Right-click the page and select **View Page Source** or **View Source**.
4. Copy the intended content from its opening `<div>` through the matching closing `</div>`.
5. Open the correct public or private **Expandable HTML** component.
6. Select **Source** in the editor toolbar. On a smaller window, it may be under **…**.
7. Paste the HTML into the Source editor.
8. Return to the normal editing view and inspect the content.
9. Save the agenda in Draft Mode.
10. Open the saved agenda, expand the content, and compare it with the approved PDF.

!!! note "The editor cleans pasted HTML"\
The editor may remove markup it considers unsupported or incompatible. This can remove unnecessary code, but it can also change the result. Always review both the normal editing view and the saved agenda.

!!! warning "Copy only the intended content"\
Do not copy the browser page's `<html>`, `<head>`, scripts, stylesheets, prompt, or Review Items. Copy only the intended content container.

## If Claude is the approved service

A district may upload the same PDF to an approved Claude account and use the same detailed prompt. Apply the same privacy rules, page-by-page comparison, human review, Source-editor procedure, and saved-agenda testing.

For recurring document types, the district may compare Gemini and Claude using the same nonconfidential PDF and prompt. Evaluate text fidelity, reading order, semantic structure, HTML cleanliness, accessibility decisions requiring correction, and total human correction time.

The provider is replaceable; the required controls are not.

## Final responsibility

AI can assist with conversion, but it does not determine or certify WCAG conformance. The district must review the content, decide whether it is suitable for publication, and evaluate the saved result with appropriate automated and manual accessibility checks.