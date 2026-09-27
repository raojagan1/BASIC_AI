from datetime import datetime, timezone


def audit(actor: str, action: str, target: str) -> dict:
    return {'actor': actor, 'action': action, 'target': target, 'created_at': datetime.now(timezone.utc).isoformat()}

if __name__ == '__main__':
    record = audit('learner', 'approve', 'job-1')
    assert record['action'] == 'approve' and record['target'] == 'job-1'
    print('PASS: audit record contains actor, action, target, and timestamp')
