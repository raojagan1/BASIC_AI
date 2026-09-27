# Day 26: Sensor Reading

## Project

Read a simulated temperature value, add a timestamp, and append it to a JSON Lines log. A real GPIO, serial, or USB sensor can later replace the command-line value.

## Run it

```bash
python3 read_sensor.py 24.5 "$HOME/automation-lab/sensor-readings.jsonl"
cat "$HOME/automation-lab/sensor-readings.jsonl"
```

## Test

```bash
rm -f "$HOME/automation-lab/sensor-readings.jsonl"
python3 read_sensor.py 24.5 "$HOME/automation-lab/sensor-readings.jsonl"
python3 read_sensor.py 31.0 "$HOME/automation-lab/sensor-readings.jsonl"

python3 - <<'PY'
import json
from pathlib import Path

readings = [json.loads(line) for line in Path.home().joinpath('automation-lab/sensor-readings.jsonl').read_text().splitlines()]
assert len(readings) == 2
assert readings[0]['value'] == 24.5
assert readings[1]['value'] == 31.0
assert all(reading['unit'] == 'celsius' for reading in readings)
assert all(reading['recorded_at'] for reading in readings)
print('PASS: sensor readings were logged with values, units, and timestamps')
PY
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Hardware automation starts by converting a physical measurement into a timestamped program value. JSON Lines is useful for appending and processing readings one at a time.
