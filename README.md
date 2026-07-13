# schoolboard.net Board Member Online Review Site

This package is the online-first Board Member documentation deliverable. It contains MkDocs source and a prebuilt static site.

## Review immediately

The package includes a prebuilt site. For complete navigation and search, serve it with Python's built-in web server:

```bash
python -m http.server 8000 --directory site
```

Open `http://127.0.0.1:8000/`. This does not require MkDocs or internet access. Opening `site/index.html` directly also supports basic page and screenshot review, but browser security rules may limit search.

For a shared review URL, upload the contents of `site/` to any static web host. Do not upload the enclosing folder unless the host expects one project folder.

## Run with MkDocs

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open the local address printed by MkDocs, normally `http://127.0.0.1:8000/`.

## Build the production site

```bash
mkdocs build --clean --strict
```

The generated site is written to `site/`.

## Dependency-free fallback build

The package also includes a small fallback builder used to create the included static site:

```bash
python tools/build_static.py
```

## Content model

The online guide is organized around common Board Member tasks rather than the chapter order of the long-form guide. The Quick Start is the landing page. Screenshots are placed directly beside the relevant action.

## Review feedback

Return feedback by page title and screenshot ID. Example: `Search and print — SB-BRD-018`.
