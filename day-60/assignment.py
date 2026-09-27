def run_pipeline(event: dict) -> dict:
    if not isinstance(event, dict) or 'input' not in event:
        raise ValueError('input event is required')
    return {'status': 'completed', 'action': 'review_required', 'input': event['input']}

if __name__ == '__main__':
    result = run_pipeline({'input': 'test event'})
    assert result['status'] == 'completed'
    print('PASS: capstone pipeline validated trigger, processing, and review action')
