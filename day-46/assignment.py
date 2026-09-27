def moisture_action(value: float, threshold: float = 40) -> str:
    return 'pump_on' if value < threshold else 'pump_off'

def temperature_action(value: float, limit: float = 35) -> str:
    return 'alert' if value >= limit else 'normal'

if __name__ == '__main__':
    assert moisture_action(25) == 'pump_on'
    assert moisture_action(40) == 'pump_off'
    assert temperature_action(35) == 'alert'
    print('PASS: business rule unit cases passed')
