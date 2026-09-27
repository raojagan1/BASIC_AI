# Day 8: Python File Organizer

## Project

Organize files into folders based on their file extension.

Supported categories:

- `.pdf` -> `pdf/`
- `.txt` -> `text/`
- `.jpg`, `.jpeg`, `.png` -> `images/`
- other extensions -> `other/`

## Run it

```bash
python3 organize_files.py
```

Optional arguments:

```bash
python3 organize_files.py SOURCE_FOLDER DESTINATION_FOLDER
```

## Test

Create test files, run the organizer, and verify each file reaches the expected folder:

```bash
mkdir -p "$HOME/automation-lab/inbox"
printf 'notes\n' > "$HOME/automation-lab/inbox/notes.txt"
printf 'pdf data\n' > "$HOME/automation-lab/inbox/report.pdf"
printf 'image data\n' > "$HOME/automation-lab/inbox/photo.jpg"
printf 'unknown\n' > "$HOME/automation-lab/inbox/data.csv"
python3 organize_files.py

test -f "$HOME/automation-lab/organized/text/notes.txt"
test -f "$HOME/automation-lab/organized/pdf/report.pdf"
test -f "$HOME/automation-lab/organized/images/photo.jpg"
test -f "$HOME/automation-lab/organized/other/data.csv"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Python's `pathlib` makes file paths portable, and `shutil.move` can automate file organization. The program leaves the original inbox empty after moving files.
