# Installation Instructions

## 1. Copy this folder

Copy the contents into your project so the structure is:

```text
schoolboardnet-docs/
├── tools/
│   └── keyboard-maestro/
├── assets/
│   └── source/
│       └── snagx/
└── docs/
    └── capture-sessions/
```

## 2. Confirm the mounted NAS path

The macro assumes your project is available at:

```text
/Volumes/TFG_Diskstation/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs
```

Before running the macro, open Finder and verify the Synology/NAS is mounted.

To test the path, use Finder → Go → Go to Folder and paste:

```text
/Volumes/TFG_Diskstation/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/assets/source/snagx
```

If it opens, the path is correct.

## 3. Import the macro

In Keyboard Maestro:

1. Open Keyboard Maestro.
2. Choose **File → Import Macros Safely…**
3. Select:

```text
tools/keyboard-maestro/macros/schoolboardnet-documentation-workbench.kmmacros
```

4. Enable the macro group if Keyboard Maestro asks.

## 4. Accessibility permissions

Go to:

```text
System Settings → Privacy & Security → Accessibility
```

Enable:

```text
Keyboard Maestro
Keyboard Maestro Engine
```

If either is missing, add it from `/Applications`.

## 5. Macro settings

The main macro should contain these values:

```text
Documentation URL:
https://demo10.schoolboard.net

Project Root:
/Volumes/TFG_Diskstation/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs

Capture Root:
/Volumes/TFG_Diskstation/Current Projects/SBN/schoolboardnet-llc/schoolboardnet-docs/assets/source/snagx
```

Dia window action:

```text
Left: 0
Top: 25
Width: 1600
Height: 1200
```

## 6. Run

Press:

```text
Control + Option + Command + D
```

The macro should:

1. Activate Dia.
2. Move/resize Dia to upper left.
3. Open `https://demo10.schoolboard.net`.
4. Activate Snagit.
5. Open the Snagit source folder.
6. Show a ready notification.

## Troubleshooting

### Dia opens but does not resize

Check Accessibility permissions for both Keyboard Maestro and Keyboard Maestro Engine.

### Dia resizes slightly smaller than 1600 × 1200

That is acceptable. macOS may subtract menu bar or display scaling space. The target remains 1600 × 1200.

### Folder does not open

Confirm the NAS is mounted under `/Volumes/TFG_Diskstation`.

Do not use an `smb://` path inside Keyboard Maestro.

