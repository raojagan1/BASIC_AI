# Day 1: Linux Automation Workspace

## Project

Create a Linux workspace and an input file for future automation projects.

## Commands used

```bash
mkdir -p ~/automation-lab
echo "Automation is useful" > ~/automation-lab/input.txt
```

## Test

```bash
test -d ~/automation-lab
test -f ~/automation-lab/input.txt
cat ~/automation-lab/input.txt
```

## Result

- Test result: PASS
- Expected text: `Automation is useful`
- Completed: 2026-09-25

## What I learned

Linux automation can create folders, create files, and verify conditions with `test`.
