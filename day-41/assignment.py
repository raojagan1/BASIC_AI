import json
from datetime import datetime, timezone


def log_event(event: str, request_id: str) -> str:
    return json.dumps({'timestamp': datetime.now(timezone.utc).isoformat(), 'level': 'INFO', 'event': event, 'request_id': request_id})

if __name__ == '__main__':
    record = json.loads(log_event('test', 'req-1'))
    assert all(key in record for key in ('timestamp', 'level', 'event', 'request_id'))
    print('PASS: structured JSON log contains required fields')
