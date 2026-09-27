import sys


def authorized(provided: str, expected: str) -> bool:
    return bool(provided) and provided == expected

if __name__ == '__main__':
    assert authorized('test-token', 'test-token')
    assert not authorized('wrong-token', 'test-token')
    print('PASS: bearer token authorization works')
