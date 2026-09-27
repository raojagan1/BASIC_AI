# Day 46: Unit Tests for Business Rules

## Goal
Test decisions without networking or databases.

## Build
Use `unittest` or `pytest` for normal, boundary, invalid, approval, moisture, temperature, and retry cases.

```bash
python3 -m unittest discover
```

## Test
The suite passes and includes both success and error paths.

## Complete when
Core rules can change safely.