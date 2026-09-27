# Day 41: Structured JSON Logging

## Goal
Make service logs searchable by machines.

## Build
Write one JSON object per line with `timestamp`, `level`, `event`, and `request_id`.

## Test
Parse every log line with `json.loads` and assert all four fields exist.

## Complete when
Operators can filter logs without parsing prose.