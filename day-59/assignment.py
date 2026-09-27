from datetime import datetime, timezone

def feedback(result_id: str, decision: str, comment: str = '') -> dict:
    if decision not in {'approved', 'rejected'}: raise ValueError('invalid decision')
    return {'result_id': result_id, 'decision': decision, 'comment': comment, 'reviewed_at': datetime.now(timezone.utc).isoformat()}

if __name__ == '__main__':
    assert feedback('r-1', 'approved')['decision'] == 'approved'
    print('PASS: reviewer feedback was captured')
