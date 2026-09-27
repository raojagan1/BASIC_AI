# Day 9: Python File Renamer

## Project

Rename files with a date or custom prefix and a three-digit sequence number while preserving extensions.

Example:

```text
photo.jpg -> 2026-09-25-001.jpg
notes.txt -> 2026-09-25-002.txt
```

## Run it

```bash
python3 rename_files.py
```

Optional arguments:

```bash
python3 rename_files.py FOLDER PREFIX
```

## Test

Use a custom prefix to make the expected names easy to check:

```bash
mkdir -p "$HOME/automation-lab/rename-inbox"
printf 'one\n' > "$HOME/automation-lab/rename-inbox/first.txt"
printf 'two\n' > "$HOME/automation-lab/rename-inbox/second.pdf"
printf 'three\n' > "$HOME/automation-lab/rename-inbox/third.jpg"
python3 rename_files.py "$HOME/automation-lab/rename-inbox" test-file

test -f "$HOME/automation-lab/rename-inbox/test-file-001.txt"
test -f "$HOME/automation-lab/rename-inbox/test-file-002.pdf"
test -f "$HOME/automation-lab/rename-inbox/test-file-003.jpg"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Python can generate predictable names with `enumerate`, preserve extensions with `Path.suffix`, and refuse to overwrite an existing destination.
