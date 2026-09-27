#!/bin/bash

set -e

LOG_FILE="${1:-$HOME/automation-lab/scheduled-task.log}"
mkdir -p "$(dirname "$LOG_FILE")"
printf '%s - scheduled task ran successfully\n' "$(date '+%F %T')" >> "$LOG_FILE"
echo "Task completed: $LOG_FILE"
