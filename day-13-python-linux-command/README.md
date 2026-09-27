# Day 13: Run Linux Commands from Python

## Project

Use Python's `subprocess` module to run safe Linux commands and save their output.

The report includes:

- kernel information from `uname -sr`
- current directory from `pwd`
- root disk usage from `df -h /`

## Run it

```bash
python3 command_report.py
cat command-report.txt
```

Optional output path:

```bash
python3 command_report.py "$HOME/automation-lab/command-report.txt"
```

## Test

```bash
python3 command_report.py "$HOME/automation-lab/command-report.txt"
report="$HOME/automation-lab/command-report.txt"
test -s "$report"
grep -q 'Kernel:' "$report"
grep -q 'Current directory:' "$report"
grep -q 'Disk usage:' "$report"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Python can connect Linux tools to larger programs. Passing commands as argument lists with `subprocess.run` avoids shell parsing and makes the command boundary explicit.
