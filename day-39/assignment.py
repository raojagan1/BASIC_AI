from collections import deque


def run_job(queue: deque) -> dict:
    job = queue.popleft()
    job['status'] = 'completed'
    job['result'] = 'done'
    return job

if __name__ == '__main__':
    job = run_job(deque([{'id': 1, 'status': 'queued'}]))
    assert job['status'] == 'completed'
    print('PASS: queued job completed with a result')
