def evaluate(cases: list[tuple[bool, bool]]) -> dict:
    correct = sum(actual == expected for actual, expected in cases)
    return {'total': len(cases), 'correct': correct, 'accuracy': correct / len(cases) if cases else 0}

if __name__ == '__main__':
    report = evaluate([(True, True), (False, False), (True, False)])
    assert report == {'total': 3, 'correct': 2, 'accuracy': 2 / 3}
    print('PASS: AI evaluation report calculated accuracy')
