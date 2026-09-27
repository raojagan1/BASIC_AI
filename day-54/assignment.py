PROMPTS = {'v1': 'Classify the message.', 'v2': 'Classify the message and explain confidence.'}

def generate_metadata(version: str) -> dict:
    if version not in PROMPTS: raise ValueError('unknown prompt version')
    return {'prompt_version': version, 'prompt': PROMPTS[version]}

if __name__ == '__main__':
    assert generate_metadata('v1')['prompt_version'] == 'v1'
    print('PASS: prompt version metadata was recorded')
