# Day 6: Schedule a Script with Cron

## Project

Create a task that writes a timestamp to a log file whenever it runs.

## Run it manually

```bash
chmod +x scheduled_task.sh
./scheduled_task.sh
cat "$HOME/automation-lab/scheduled-task.log"
```

## Schedule it every day at 8 PM

First find the project path:

```bash
pwd
```

Open your user crontab:

```bash
crontab -e
```

Add this line, replacing `/home/yourname/Aaradya/AI_ATOMATION` with the path printed by `pwd`:

```text
0 20 * * * /home/yourname/Aaradya/AI_ATOMATION/day-06-cron-task/scheduled_task.sh
```

List the saved entries:

```bash
crontab -l
```

## Test

The manual run must create or update the log file, and the newest line must contain `scheduled task ran successfully`.

```bash
./scheduled_task.sh
last_line=$(tail -n 1 "$HOME/automation-lab/scheduled-task.log")
echo "$last_line" | grep -q 'scheduled task ran successfully'
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Cron starts commands automatically according to a time pattern. The five fields are minute, hour, day of month, month, and day of week.
