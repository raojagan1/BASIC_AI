# Day 20: Scheduled API Report

## Project

Fetch data from a public API and write a timestamped JSON report that can be run repeatedly by cron.

## Run it

```bash
python3 api_report.py "$HOME/automation-lab/api-report.json"
cat "$HOME/automation-lab/api-report.json"
```

## Schedule it

Open the user crontab:

```bash
crontab -e
```

Add a line using the absolute path to this project:

```text
0 * * * * /usr/bin/python3 /home/yourname/Aaradya/AI_ATOMATION/day-20-scheduled-api-report/api_report.py /home/yourname/automation-lab/api-report.json
```

This runs the report at the start of every hour.

## Test

```bash
python3 api_report.py "$HOME/automation-lab/api-report.json"
report="$HOME/automation-lab/api-report.json"
test -s "$report"
grep -q '"retrieved_at":' "$report"
grep -q '"source":' "$report"
grep -q '"id": 1' "$report"
grep -q '"title":' "$report"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

A scheduled report combines a trigger such as cron, API data retrieval, JSON processing, and a persistent output file. Re-running the script refreshes the report.
