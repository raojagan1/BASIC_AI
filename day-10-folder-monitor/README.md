# Day 10: Python Folder Monitor

## Project

Monitor a folder and print a message whenever a new file appears.

## Run it

```bash
python3 monitor_folder.py "$HOME/automation-lab/watch"
```

The monitor checks every two seconds. Stop it with `Ctrl+C`.

## One-shot test mode

The `--once` option scans the current folder once and reports its files. It is useful for testing without leaving a continuous process running:

```bash
mkdir -p "$HOME/automation-lab/watch"
printf 'new file\n' > "$HOME/automation-lab/watch/example.txt"
python3 monitor_folder.py "$HOME/automation-lab/watch" --once
```

## Test

The output must report the new file:

```bash
output=$(python3 monitor_folder.py "$HOME/automation-lab/watch" --once)
echo "$output" | grep -q 'New file detected: example.txt'
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Python can compare the current directory contents with a previous snapshot. A loop and `time.sleep` turn that comparison into a simple polling monitor.
