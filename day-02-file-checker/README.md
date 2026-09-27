# Day 2: Bash File-Existence Checker

## Project

Create a Bash program that checks whether a file exists.

## Run it

```bash
chmod +x check_file.sh
./check_file.sh "$HOME/automation-lab/input.txt"
./check_file.sh "$HOME/automation-lab/missing.txt"
```

## Test

The existing file must return exit code `0` and print `The file exists`.
The missing file must return exit code `1` and print `The file does not exist`.

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Bash uses `if`, the `-f` file test, and exit codes to make decisions.
