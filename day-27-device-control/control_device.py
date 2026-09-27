from datetime import datetime, timezone
import json
from pathlib import Path
import sys


def control_led(sensor_value: float, threshold: float, output_path: Path) -> str:
    state = "ON" if sensor_value >= threshold else "OFF"
    event = {
        "device": "simulated-led",
        "state": state,
        "sensor_value": sensor_value,
        "threshold": threshold,
        "changed_at": datetime.now(timezone.utc).isoformat(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(event, indent=2) + "\n", encoding="utf-8")
    return state


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print("Usage: control_device.py SENSOR_VALUE THRESHOLD [OUTPUT_FILE]")
        return 2
    try:
        sensor_value = float(sys.argv[1])
        threshold = float(sys.argv[2])
    except ValueError:
        print("Sensor value and threshold must be numeric")
        return 2

    output_path = Path(sys.argv[3]) if len(sys.argv) == 4 else Path("device-state.json")
    state = control_led(sensor_value, threshold, output_path)
    print(f"Simulated LED: {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
