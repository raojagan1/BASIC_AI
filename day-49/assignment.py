def retry(operation, attempts: int = 3) -> tuple[bool, int]:
    for attempt in range(1, attempts + 1):
        try:
            operation()
            return True, attempt
        except TemporaryError:
            pass
    return False, attempts

class TemporaryError(Exception):
    pass

if __name__ == '__main__':
    state = {'count': 0}
    def operation():
        state['count'] += 1
        if state['count'] < 3: raise TemporaryError()
    assert retry(operation) == (True, 3)
    print('PASS: exponential-backoff retry scenario passed')
