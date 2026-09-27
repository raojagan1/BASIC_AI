#!/bin/bash

set -u

LOG_FILE="${1:-server.log}"
ERROR_FILE="${2:-errors.txt}"

if [ ! -f "$LOG_FILE" ]; then
    echo "Log file does not exist: $LOG_FILE"
    exit 2
fi

grep -inE 'error|failed|fatal' "$LOG_FILE" > "$ERROR_FILE" || true
ERROR_COUNT=$(wc -l < "$ERROR_FILE")

echo "Found $ERROR_COUNT error entries"
echo "Saved results to $ERROR_FILE"
