# Install the Version 1.1.004 Review Polish Update

This cumulative update cleans the complete reviewer-facing documentation suite and includes the District Administrator Responsibilities addition.

## Install

1. Back up the current repository.
2. Open the update package.
3. Copy its contents into the root of `schoolboardnet-docs`.
4. Allow folders to merge and replace files when prompted.
5. Do not delete or replace the repository's `.git` folder.
6. Build the complete documentation suite and deploy normally.

## Validate after deployment

Confirm that:

- the Documentation Center and reviewer-status page show Version 1.1.004 Review Edition;
- all five guide names are consistent;
- **District Administrator responsibilities** appears near the beginning of that guide;
- Board Member search does not return District Administrator source or capture-session pages;
- Public Notifications and Accessibility remain separate navigation topics;
- Accordion Agenda Best Practices and Troubleshooting remain separate, focused topics;
- saved links to the former combined Public and Accordion Agenda pages still open their transition pages;
- guide images load and internal links open; and
- mobile Topics and page-table-of-contents navigation work as expected.

## Verification completed before packaging

- Five MkDocs strict-mode builds passed.
- Local Markdown link and image-reference validation passed.

