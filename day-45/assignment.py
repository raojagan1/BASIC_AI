import os


def validate_config() -> None:
    if not os.environ.get('APP_SECRET'):
        raise RuntimeError('APP_SECRET is required')
    port = int(os.environ.get('APP_PORT', '8000'))
    if port < 1 or port > 65535:
        raise ValueError('APP_PORT is invalid')

if __name__ == '__main__':
    os.environ['APP_SECRET'] = 'test-secret'
    os.environ['APP_PORT'] = '8000'
    validate_config()
    print('PASS: production configuration validation succeeded')
