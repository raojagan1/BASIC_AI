REQUIRED_FIELDS = {'id', 'title', 'completed'}

def contract_valid(response: dict) -> bool:
    return REQUIRED_FIELDS.issubset(response)

if __name__ == '__main__':
    assert contract_valid({'id': 1, 'title': 'x', 'completed': False})
    assert not contract_valid({'id': 1})
    print('PASS: external API contract validation passed')
