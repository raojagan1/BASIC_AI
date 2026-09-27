#!/bin/bash
set -e
PROJECT_NAME=$(tr -d '\n' < PROJECT_NAME.txt)
test -n "$PROJECT_NAME"
test -s README.md
test -x auto_run.sh
test -s assignment.py
python3 assignment.py --test
echo "PASS: $PROJECT_NAME tutorial and automatic runner are ready"