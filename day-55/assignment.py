def route(confidence: float, threshold: float = .8) -> str:
    return 'automatic_action' if confidence >= threshold else 'human_review'

if __name__ == '__main__':
    assert route(.95) == 'automatic_action'
    assert route(.45) == 'human_review'
    print('PASS: confidence threshold routed uncertain work to review')
