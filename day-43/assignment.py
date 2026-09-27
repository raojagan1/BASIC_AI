class Metrics:
    def __init__(self):
        self.counters = {}
    def increment(self, name: str) -> None:
        self.counters[name] = self.counters.get(name, 0) + 1

if __name__ == '__main__':
    metrics = Metrics()
    metrics.increment('requests_total')
    metrics.increment('requests_total')
    assert metrics.counters['requests_total'] == 2
    print('PASS: metrics counter recorded two requests')
