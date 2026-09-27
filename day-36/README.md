# Day 36: API Authentication

## Goal
Protect API operations with a bearer token.

## Build
Read `API_TOKEN` from the environment and require `Authorization: Bearer TOKEN`.

```bash
export API_TOKEN=local-test-token
curl -i -H "Authorization: Bearer $API_TOKEN" http://127.0.0.1:8000/events
```

## Test
Missing and incorrect tokens return HTTP 401; the correct token succeeds.

## Complete when
Protected routes cannot be called anonymously.