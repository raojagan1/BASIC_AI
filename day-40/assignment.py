def checkpoint(results: list[bool]) -> bool:
    return bool(results) and all(results)

if __name__ == '__main__':
    assert checkpoint([True, True, True])
    assert not checkpoint([True, False])
    print('PASS: backend checkpoint detects all passing components')
