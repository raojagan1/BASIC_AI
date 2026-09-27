# Day 27: Control an LED or Simulated Device

## Project

Turn a simulated LED on when a sensor value reaches a threshold, otherwise turn it off.

## Run it

```bash
python3 control_device.py 32 30 "$HOME/automation-lab/device-state.json"
cat "$HOME/automation-lab/device-state.json"
```

A real Raspberry Pi version can replace the state write with a GPIO output operation.

## Test

```bash
python3 control_device.py 25 30 "$HOME/automation-lab/device-state.json"
grep -q '"state": "OFF"' "$HOME/automation-lab/device-state.json"
python3 control_device.py 32 30 "$HOME/automation-lab/device-state.json"
grep -q '"state": "ON"' "$HOME/automation-lab/device-state.json"
```

## Result

- Test result: PASS
- Completed: 2026-09-25

## What I learned

Device automation converts a sensor decision into an output state. The same decision logic can control a simulated device, an LED, a relay, or a fan.
