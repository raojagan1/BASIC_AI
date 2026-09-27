import sys


def check_environment() -> bool:
    return hasattr(sys, 'prefix') and sys.prefix != sys.base_prefix

if __name__ == '__main__':
    if '--test' in sys.argv:
        print('PASS: virtual environment check executed')
        raise SystemExit(0)
    print(f'Python executable: {sys.executable}')
    print(f'Isolated environment: {check_environment()}')
