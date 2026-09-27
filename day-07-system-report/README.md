# Day 7: Linux System Information Report

## Project

Collect basic Linux system information and save it to a report file.

The report includes:

- hostname
- kernel version
- memory usage
- root filesystem usage

## Run it

```bash
chmod +x system_report.sh
./system_report.sh
cat "$HOME/automation-lab/system-report.txt"
```

Optional output path:

```bash
./system_report.sh /tmp/my-system-report.txt
```

## Test

The report must exist and contain all four required sections:

```bash
./system_report.sh
report="$HOME/automation-lab/system-report.txt"
test -s "$report"
grep -q 'Hostname:' "$report"
grep -q 'Kernel:' "$report"
grep -q 'Memory:' "$report"
grep -q 'Disk:' "$report"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Linux provides system information through commands such as `hostname`, `uname`, `free`, and `df`. A Bash script can combine their output into a useful report.
