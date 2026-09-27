# Day 31: Python Virtual Environment

## Goal
Isolate dependencies for one automation project.

## Build
```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -c 'import sys; print(sys.executable)'
```

## Test
```bash
test -x .venv/bin/python
.venv/bin/python -c 'import sys; assert sys.prefix.endswith("day-31/.venv")'
```

## Complete when
The project runs with its own Python interpreter.