# Online Review Deployment

The package includes two supported review paths.

## Immediate local review

Run the prebuilt site with Python's built-in web server:

```bash
python -m http.server 8000 --directory site
```

Open `http://127.0.0.1:8000/`. Opening `site/index.html` directly supports basic page review, but browser security rules may limit search.

## Shared review URL

Upload the contents of `site/` to a static web host or internal web server. The host's document root should contain `index.html`, the task-page folders, and `assets/`.

Before sharing the URL:

1. Confirm whether access should be public, workspace-only, or limited to named reviewers.
2. Open the Quick Start and at least one nested task page.
3. Test search, mobile navigation, keyboard focus, and every screenshot.
4. Confirm that the host preserves folder-based URLs such as `/sign-in/`.
5. Send reviewers the site root URL and ask them to comment by page title and screenshot ID.

## MkDocs preview server

After installing `requirements.txt`, run:

```bash
mkdocs serve
```

This is intended for a writer or reviewer on the same computer or trusted network. It is not a production deployment.

## MkDocs static build

Run:

```bash
mkdocs build --clean --strict
```

Upload the resulting `site/` contents to the selected host.

## GitHub Pages option

If the documentation source is stored in a GitHub repository and the review site may use GitHub Pages, the MkDocs command below builds and publishes the site to the repository's Pages branch:

```bash
mkdocs gh-deploy --clean --strict
```

Confirm repository access and review-site visibility before using this command. Deployment is intentionally not performed by this package because the reviewer access policy and destination have not been selected.
