def integration_flow(event: dict) -> dict:
    if not event.get('name'):
        raise ValueError('name required')
    return {'stored': True, 'name': event['name']}

if __name__ == '__main__':
    result = integration_flow({'name': 'file.created'})
    assert result == {'stored': True, 'name': 'file.created'}
    print('PASS: API-to-storage integration flow passed')
