# Day 29: Smart Greenhouse Simulation

## Project

Combine simulated soil-moisture and temperature readings to decide whether a water pump should run.

Rule:

```text
If soil moisture < threshold, pump ON; otherwise, pump OFF.
```

## Run it

```bash
python3 greenhouse.py 25 31 40 "$HOME/automation-lab/greenhouse-decision.json"
cat "$HOME/automation-lab/greenhouse-decision.json"
```

## Test

Dry soil must turn the pump on. Moist soil must turn it off:

```bash
python3 greenhouse.py 25 31 40 "$HOME/automation-lab/greenhouse-decision.json"
grep -q '"pump": "ON"' "$HOME/automation-lab/greenhouse-decision.json"
python3 greenhouse.py 55 24 40 "$HOME/automation-lab/greenhouse-decision.json"
grep -q '"pump": "OFF"' "$HOME/automation-lab/greenhouse-decision.json"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

A smart greenhouse combines sensor input, decision logic, and an actuator. The same pipeline can later use real moisture sensors and a safely controlled pump relay.
