# Day 28: Temperature Alert Automation

## Project

Check a temperature reading against a safety limit and record whether an alert is required.

Exit codes:

- `0`: normal temperature
- `1`: alert triggered
- `2`: invalid input

## Run it

```bash
python3 temperature_alert.py 24 30 "$HOME/automation-lab/temperature-alert.json"
```

## Test

```bash
python3 temperature_alert.py 24 30 "$HOME/automation-lab/temperature-alert.json"
grep -q '"status": "NORMAL"' "$HOME/automation-lab/temperature-alert.json"

if python3 temperature_alert.py 35 30 "$HOME/automation-lab/temperature-alert.json"; then
    echo "FAIL: high temperature did not trigger an alert"
    exit 1
fi
grep -q '"status": "ALERT"' "$HOME/automation-lab/temperature-alert.json"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

An alert automation should produce both a human-readable message and a machine-readable status or exit code that another program can act on.
