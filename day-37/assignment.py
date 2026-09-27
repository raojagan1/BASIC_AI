import sys


def page(items: list, number: int, size: int) -> list:
    if number < 1 or not 1 <= size <= 100:
        raise ValueError('invalid page')
    start = (number - 1) * size
    return items[start:start + size]

if __name__ == '__main__':
    result = page(list(range(25)), 2, 10)
    assert result == list(range(10, 20))
    print('PASS: pagination returned the requested page')
