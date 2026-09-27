# Day 38: Idempotent Webhooks

## Goal
Prevent duplicate effects when a provider retries an event.

## Build
Require `event_id`; store it under a unique constraint before performing the side effect.

```bash
curl -X POST http://127.0.0.1:8000/webhook -d '{"event_id":"evt-1","type":"file.created"}'
```

## Test
Send the same event twice. Verify one database record and one side effect.

## Complete when
Network retries are safe.