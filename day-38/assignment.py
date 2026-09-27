import sys


def process_once(event_id: str, seen: set[str]) -> bool:
    if event_id in seen:
        return False
    seen.add(event_id)
    return True

if __name__ == '__main__':
    seen = set()
    assert process_once('evt-1', seen)
    assert not process_once('evt-1', seen)
    print('PASS: duplicate webhook was ignored')
