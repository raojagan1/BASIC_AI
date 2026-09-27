# Day 32: Environment Configuration

## Goal
Read settings from environment variables instead of hard-coding them.

## Build
Create `config.py` that reads required `APP_MODE` with `os.environ`.

```bash
export APP_MODE=development
python3 config.py
unset APP_MODE
```

## Test
The first command succeeds; the second fails with a clear missing-configuration error.

## Complete when
Settings are separate from source code and secrets are not committed.