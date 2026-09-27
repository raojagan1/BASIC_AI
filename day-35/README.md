# Day 35: Validated REST API

## Goal
Accept structured input and reject invalid requests.

## Build
Add `POST /events`; require a non-empty string `name` and object `payload`.

```bash
curl -X POST http://127.0.0.1:8000/events -H 'Content-Type: application/json' -d '{"name":"file.created","payload":{"file":"a.txt"}}'
```

## Test
Valid input returns HTTP 201. Missing `name` or malformed JSON returns HTTP 400.

## Complete when
Clients receive predictable JSON success and validation errors.