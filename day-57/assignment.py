import re

EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
TOKEN = re.compile(r'Bearer\s+\S+', re.IGNORECASE)

def redact(text: str) -> str:
    return TOKEN.sub('[REDACTED_TOKEN]', EMAIL.sub('[REDACTED_EMAIL]', text))

if __name__ == '__main__':
    result = redact('email user@example.com Bearer secret-token')
    assert 'user@example.com' not in result and 'secret-token' not in result
    print('PASS: sensitive email and token values were redacted')
