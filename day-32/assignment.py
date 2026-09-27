import os
import sys


def read_mode() -> str:
    mode = os.environ.get('APP_MODE')
    if not mode:
        raise RuntimeError('APP_MODE is required')
    return mode

if __name__ == '__main__':
    if '--test' in sys.argv:
        os.environ['APP_MODE'] = 'test'
        assert read_mode() == 'test'
        print('PASS: configuration was read from environment')
    else:
        print(f'APP_MODE={read_mode()}')
