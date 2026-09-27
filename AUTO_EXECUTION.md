# Automatic Execution Setup

Every Day 1-60 directory contains:

- `README.md`: the project tutorial
- `auto_run.sh`: the project's named automatic-run hook

## Run one day

```bash
cd /home/user/Aaradya/AI_ATOMATION/day-01-linux-workspace
./auto_run.sh
```

For Days 31-60:

```bash
cd /home/user/Aaradya/AI_ATOMATION/days-31-60/day-31
./auto_run.sh
```

Each run records a timestamped line in:

```text
~/automation-lab/auto-runs/day-XX.log
```

## Run all 60 hooks

From the workspace root:

```bash
cd /home/user/Aaradya/AI_ATOMATION
chmod +x run_all_days.sh day-*/auto_run.sh days-31-60/day-*/auto_run.sh
./run_all_days.sh
```

## Schedule daily execution with cron

Open your user crontab:

```bash
crontab -e
```

Run the full hook set every day at 8 PM:

```text
0 20 * * * /home/user/Aaradya/AI_ATOMATION/run_all_days.sh >> /home/user/automation-lab/auto-runs/all-days.log 2>&1
```

Check the schedule:

```bash
crontab -l
```

The hooks record setup execution and project names. They do not replace each project's individual test command; run the README test when you want to verify project behavior.
