def readiness(database_ok: bool, api_ok: bool) -> tuple[int, str]:
    return (200, 'ready') if database_ok and api_ok else (503, 'not ready')

if __name__ == '__main__':
    assert readiness(True, True) == (200, 'ready')
    assert readiness(False, True)[0] == 503
    print('PASS: health readiness separates dependency failures')
