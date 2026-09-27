#!/bin/bash

set -u

CHECK_PATH="${1:-/}"
WARNING_LIMIT="${2:-80}"

if [ ! -d "$CHECK_PATH" ]; then
    echo "Path does not exist: $CHECK_PATH"
    exit 2
fi

if ! [[ "$WARNING_LIMIT" =~ ^[0-9]+$ ]] || [ "$WARNING_LIMIT" -gt 100 ]; then
    echo "Threshold must be a whole number from 0 to 100"
    exit 2
fi

USAGE_PERCENT=$(df -P "$CHECK_PATH" | awk 'NR == 2 {gsub("%", "", $5); print $5}')

if [ "$USAGE_PERCENT" -ge "$WARNING_LIMIT" ]; then
    echo "WARNING: $CHECK_PATH is ${USAGE_PERCENT}% full (limit: ${WARNING_LIMIT}%)"
    exit 1
else
    echo "OK: $CHECK_PATH is ${USAGE_PERCENT}% full (limit: ${WARNING_LIMIT}%)"
    exit 0
fi
