# Day 17: Webhook Receiver

## Project

Receive JSON events over HTTP and append them to a JSON Lines log file.

Endpoint:

```text
POST /webhook
```

## Run it

```bash
python3 webhook_receiver.py 8765 "$HOME/automation-lab/webhook-events.jsonl"
```

Send a test event from another terminal:

```bash
curl -X POST http://127.0.0.1:8765/webhook \
  -H 'Content-Type: application/json' \
  -d '{"event":"file.created","file":"report.pdf"}'
```

## Test

A valid JSON object must return `accepted: true` and be written to the log. Invalid JSON must return HTTP 400.

```bash
python3 webhook_receiver.py 8765 "$HOME/automation-lab/webhook-events.jsonl"
curl -X POST http://127.0.0.1:8765/webhook \
  -H 'Content-Type: application/json' \
  -d '{"event":"test"}'
cat "$HOME/automation-lab/webhook-events.jsonl"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

A webhook is an HTTP callback. One program sends an event to another program, which validates the request and records or processes it automatically.
