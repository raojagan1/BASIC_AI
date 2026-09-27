def reliability_checkpoint(checks: dict[str, bool]) -> bool:
    return bool(checks) and all(checks.values())

if __name__ == '__main__':
    checks = {'logs': True, 'health': True, 'metrics': True, 'tests': True}
    assert reliability_checkpoint(checks)
    print('PASS: reliability checkpoint passed')
