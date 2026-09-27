# Day 4: Disk-Usage Warning

## Project

Check disk usage and warn when a filesystem reaches a chosen limit.

## Run it

```bash
chmod +x check_disk.sh
./check_disk.sh /
./check_disk.sh / 90
```

Optional arguments:

```bash
./check_disk.sh PATH WARNING_PERCENT
```

## Test

The normal threshold should report `OK`. A threshold of `0` should report `WARNING` and return exit code `1`.

```bash
./check_disk.sh / 100
if ./check_disk.sh / 0; then
    echo "FAIL: threshold warning was not triggered"
else
    echo "PASS: warning path triggered"
fi
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Linux `df` reports filesystem usage, and a script can compare that value with a threshold to trigger a warning.
