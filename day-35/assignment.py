import json
import sys


def validate_event(payload: dict) -> tuple[bool, str]:
    if not isinstance(payload.get('name'), str) or not payload['name'].strip():
        return False, 'name must be a non-empty string'
    if not isinstance(payload.get('payload'), dict):
        return False, 'payload must be an object'
    return True, 'valid'

if __name__ == '__main__':
    valid, message = validate_event(json.loads(sys.argv[1]) if len(sys.argv) > 1 and '--test' not in sys.argv else {'name': 'test', 'payload': {}})
    if '--test' in sys.argv:
        assert valid and not validate_event({'name': ''})[0]
        print('PASS: REST input validation works')
    else:
        print(message)
        raise SystemExit(0 if valid else 1)
