# Day 19: Retry and Error Handling

## Project

Retry an operation when a temporary error occurs, record each attempt, and stop after a maximum number of attempts.

## Run it

The argument controls how many attempts fail before success:

```bash
python3 retry_task.py 2
```

A value of `2` succeeds on the third attempt. A value of `3` exhausts all three attempts and returns failure.

## Test

Eventual success:

```bash
python3 retry_task.py 2 > success.txt
status=$?
test "$status" -eq 0
grep -q 'Attempt 3: success' success.txt
```

Permanent failure:

```bash
if python3 retry_task.py 3 > failure.txt; then
    echo "FAIL: permanent failure was reported as success"
    exit 1
fi
test "$(grep -c 'temporary service failure' failure.txt)" -eq 3
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Retries help recover from temporary failures, but a maximum attempt count prevents an automation from running forever. Error logs explain what happened on each attempt.
