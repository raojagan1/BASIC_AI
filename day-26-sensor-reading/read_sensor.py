from datetime import datetime, timezone
import json
from pathlib import Path
import sys


def record_sensor_value(value: float, output_path: Path) -> None:
    reading = {
        "sensor": "simulated-temperature",
        "value": value,
        "unit": "celsius",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("a", encoding="utf-8") as output_file:
        output_file.write(json.dumps(reading) + "\n")


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: read_sensor.py VALUE [OUTPUT_FILE]")
        return 2
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Sensor value must be numeric")
        return 2

    output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path("sensor-readings.jsonl")
    record_sensor_value(value, output_path)
    print(f"Recorded {value:.2f} celsius to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
