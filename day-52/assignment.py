def grounded_answer(question: str, source: str) -> str:
    if not source.strip():
        return 'No relevant source found.'
    return f'Answer to {question}: based on source [{source}]'

if __name__ == '__main__':
    answer = grounded_answer('What failed?', 'incident.md')
    assert '[incident.md]' in answer
    print('PASS: generated answer includes a source citation')
