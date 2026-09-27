#!/bin/bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
passed=0

for directory in "$ROOT_DIR"/day-* "$ROOT_DIR"/days-31-60/day-*; do
    [ -x "$directory/test.sh" ] || continue
    printf 'Testing %s\n' "$directory"
    (cd "$directory" && ./test.sh)
    passed=$((passed + 1))
done

echo "All $passed daily tests passed."
