# Day 3: Automatic Bash Backup

## Project

Create a compressed, dated backup archive from a source folder.

## Run it

```bash
chmod +x backup.sh
./backup.sh
```

Optional arguments:

```bash
./backup.sh SOURCE_FOLDER DESTINATION_FOLDER
```

## Test

The backup must be created and must contain the source file:

```bash
archive=$(find "$HOME/automation-lab/backups" -maxdepth 1 -type f -name 'backup-*.tar.gz' -print -quit)
tar -tzf "$archive"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Bash can pass arguments to a script, create compressed `.tar.gz` archives, and stop safely when a required folder is missing.
