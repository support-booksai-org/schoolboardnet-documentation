# sbDocs v2.2 Production Workflow

Install by copying these into `tools/sbdocs`:

- `sbdocs_v22.py` -> rename to `sbdocs.py`
- `config_v22.yaml` -> rename to `config.yaml` only if you want to replace your current config
- `run-sbdocs_v22.command` -> rename to `run-sbdocs.command`

New menu items:

- `11. Build / Validate / Deploy` — environment check, backup, repair/validate, clean build, optional git commit/push for Netlify.
- `12. Create build-mkdocs.command` — writes a reliable local build/serve script using `python3 -m mkdocs`.
- `16. Environment Check` — checks Python, PyYAML, MkDocs, and `mkdocs.yml`.

Important:

- This version still validates user-facing docs by default and skips internal `docs/assets/` tooling notes.
- Full asset/tool validation remains available as menu item `15`.
- Netlify updates after GitHub receives the push.
