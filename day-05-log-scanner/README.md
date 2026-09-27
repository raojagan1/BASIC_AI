# Day 5: Linux Log Error Scanner

## Project

Scan a log file and save lines containing `ERROR`, `FAILED`, or `FATAL` to a separate file.

## Run it

```bash
chmod +x scan_errors.sh
./scan_errors.sh server.log errors.txt
```

Optional arguments:

```bash
./scan_errors.sh LOG_FILE OUTPUT_FILE
```

## Test

The test log contains two matching entries and two normal entries. The output must contain exactly two lines, and normal entries must not appear.

```bash
./scan_errors.sh server.log errors.txt
test "$(wc -l < errors.txt)" -eq 2
! grep -q "INFO" errors.txt
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Linux pipes and `grep` can filter useful events from large log files. The script also handles a log with no matches without crashing.
