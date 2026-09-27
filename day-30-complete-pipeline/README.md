# Day 30: Complete AI Automation Pipeline

## Project

Build a complete automation pipeline:

```text
JSON sensor trigger -> classify conditions -> choose actions -> write audit result
```

Rules:

- Soil moisture below `40` -> `pump_on`
- Soil moisture `40` or above -> `pump_off`
- Temperature `35` or above -> `temperature_alert`

The pump and alert are simulated as recorded actions. No physical hardware is changed.

## Run it

Create a trigger event:

```bash
printf '{"soil_moisture": 25, "temperature": 36}\n' > sensor-event.json
python3 pipeline.py sensor-event.json pipeline-result.json
cat pipeline-result.json
```

## Test

Normal conditions:

```bash
printf '{"soil_moisture": 55, "temperature": 24}\n' > normal-event.json
python3 pipeline.py normal-event.json normal-result.json
grep -q '"pump_off"' normal-result.json
grep -q '"status": "completed"' normal-result.json
```

Dry and hot conditions:

```bash
printf '{"soil_moisture": 25, "temperature": 36}\n' > alert-event.json
python3 pipeline.py alert-event.json alert-result.json
grep -q '"pump_on"' alert-result.json
grep -q '"temperature_alert"' alert-result.json
```

Invalid input must fail safely:

```bash
printf '{"temperature": "unknown"}\n' > invalid-event.json
if python3 pipeline.py invalid-event.json invalid-result.json; then
    echo "FAIL: invalid input was accepted"
    exit 1
fi
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

A production-style automation pipeline needs a trigger, processing rules, actions, logging, and failure handling. Each stage can later be upgraded with real sensors, an AI model, hardware controls, and notifications.
