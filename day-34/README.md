# Day 34: Database Migrations

## Goal
Upgrade a database schema safely and repeatably.

## Build
Create a `schema_version` table and numbered migrations. Migration 2 adds `created_at` to `events`.

## Test
```bash
python3 migrate.py events.db
python3 migrate.py events.db
```

Inspect `PRAGMA table_info(events)` and verify the column appears once.

## Complete when
An empty database and an old database reach the same current schema.