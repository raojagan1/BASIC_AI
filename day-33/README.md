# Day 33: SQLite Event Database

## Goal
Persist automation events across program restarts.

## Build
Create an `events` table with `id`, `name`, and `payload`; insert one JSON event using Python's `sqlite3` module.

## Test
Close and reopen `events.db`, then query the inserted event.

```bash
python3 app.py
python3 query.py
```

## Complete when
The event remains available after the first process exits.