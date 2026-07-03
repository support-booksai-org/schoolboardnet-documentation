# Keyboard Maestro Screenshot Manager Notes

Keep the Keyboard Maestro workflow simple for now.

## Start Documentation Session

Recommended actions:

1. Activate Dia.
2. Move/resize Dia:
   - Left: 0
   - Top: 25
   - Width: 1600
   - Height: 1200
3. Open URL:
   - https://demo10.schoolboard.net
4. Activate Snagit.
5. Open screenshot folder:
   - /Volumes/TFG_Diskstation/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/assets/screenshots
6. Show notification:
   - Documentation Capture Ready

## Recommended capture path

Use the mounted macOS path, not an SMB URL:

```text
/Volumes/TFG_Diskstation/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/assets/screenshots
```

Do not use:

```text
smb://TFG_Diskstation...
```

## Suggested feature folders

```text
dashboard
users
groups
meetings
books
notifications
settings
```

