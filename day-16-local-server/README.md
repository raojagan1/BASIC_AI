# Day 16: Local HTTP Server

## Project

Build a local Python HTTP server with JSON endpoints.

Endpoints:

- `GET /health` -> `{"status": "ok"}`
- `GET /api/status` -> service readiness information
- Any other path -> HTTP 404

## Run it

```bash
python3 server.py 8765
```

In another terminal, request an endpoint:

```bash
curl http://127.0.0.1:8765/health
```

Stop the server with `Ctrl+C`.

## Test

```bash
python3 server.py 8765 &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null || true' EXIT
for attempt in 1 2 3 4 5; do
    curl -fsS http://127.0.0.1:8765/health >/dev/null && break
done
curl -fsS http://127.0.0.1:8765/health | grep -q '"status": "ok"'
curl -fsS http://127.0.0.1:8765/api/status | grep -q '"ready": true'
if curl -fsS http://127.0.0.1:8765/missing; then
    echo "FAIL: missing route returned success"
    exit 1
else
    echo "PASS: HTTP server routes behave correctly"
fi
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

A local HTTP server lets programs communicate over HTTP without needing an external service. JSON responses make the service easy for other automation tools to consume.
