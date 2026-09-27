#!/bin/bash

set -e

REPORT_FILE="${1:-$HOME/automation-lab/system-report.txt}"
mkdir -p "$(dirname "$REPORT_FILE")"

{
    echo "Linux System Information Report"
    echo "Generated: $(date '+%F %T')"
    echo
    echo "Hostname:"
    hostname
    echo
    echo "Kernel:"
    uname -sr
    echo
    echo "Memory:"
    free -h
    echo
    echo "Disk:"
    df -h /
} > "$REPORT_FILE"

echo "Report created: $REPORT_FILE"
