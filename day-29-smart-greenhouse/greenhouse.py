from datetime import datetime, timezone
import json
from pathlib import Path
import sys


def greenhouse_decision(
    moisture: float,
    temperature: float,
    moisture_threshold: float,
    output_path: Path,
) -> str:
    pump_state = "ON" if moisture < moisture_threshold else "OFF"
    decision = {
        "system": "smart-greenhouse-simulation",
        "soil_moisture": moisture,
        "temperature": temperature,
        "moisture_threshold": moisture_threshold,
        "pump": pump_state,
        "decided_at": datetime.now(timezone.utc).isoformat(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(decision, indent=2) + "\n", encoding="utf-8")
    return pump_state


def main() -> int:
    if len(sys.argv) not in (4, 5):
        print("Usage: greenhouse.py MOISTURE TEMPERATURE MOISTURE_THRESHOLD [OUTPUT_FILE]")
        return 2
    try:
        moisture = float(sys.argv[1])
        temperature = float(sys.argv[2])
        moisture_threshold = float(sys.argv[3])
    except ValueError:
        print("Sensor values and threshold must be numeric")
        return 2

    output_path = Path(sys.argv[4]) if len(sys.argv) == 5 else Path("greenhouse-decision.json")
    pump_state = greenhouse_decision(moisture, temperature, moisture_threshold, output_path)
    print(f"Greenhouse pump: {pump_state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
