# Day 12: JSON Task Tracker

## Project

Create, list, and complete tasks stored in a JSON file.

## Commands

```bash
python3 task_tracker.py --file tasks.json add "Learn Python"
python3 task_tracker.py --file tasks.json add "Build an automation"
python3 task_tracker.py --file tasks.json list
python3 task_tracker.py --file tasks.json done 1
python3 task_tracker.py --file tasks.json list
```

## Test

```bash
rm -f tasks.json
python3 task_tracker.py --file tasks.json add "Learn Python"
python3 task_tracker.py --file tasks.json add "Build an automation"
python3 task_tracker.py --file tasks.json done 1
python3 task_tracker.py --file tasks.json list > task-list.txt

test "$(python3 -c 'import json; print(len(json.load(open("tasks.json"))))')" -eq 2
grep -q '\[done\] 1: Learn Python' task-list.txt
grep -q '\[open\] 2: Build an automation' task-list.txt
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

JSON stores structured data that programs can read and update. Command-line subcommands make one program useful for several related actions.
