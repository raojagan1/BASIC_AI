#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

for script in "$ROOT_DIR"/day-*/auto_run.sh "$ROOT_DIR"/days-31-60/day-*/auto_run.sh; do
    [ -x "$script" ] || continue
    "$script"
done

echo "All available daily automatic-run hooks completed."
