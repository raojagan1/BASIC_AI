def validate_output(result: dict) -> bool:
    return (isinstance(result.get('category'), str) and isinstance(result.get('summary'), str) and isinstance(result.get('confidence'), (int, float)) and 0 <= result['confidence'] <= 1 and isinstance(result.get('next_action'), str))

if __name__ == '__main__':
    assert validate_output({'category': 'support', 'summary': 'ok', 'confidence': .9, 'next_action': 'review'})
    assert not validate_output({'category': 'support', 'confidence': 2})
    print('PASS: AI output schema validation passed')
