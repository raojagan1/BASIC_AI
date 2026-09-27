from datetime import datetime, timezone
import json
from pathlib import Path
import sys


def check_temperature(temperature: float, limit: float, output_path: Path) -> bool:
    alert = temperature >= limit
    event = {
        "sensor": "simulated-temperature",
        "temperature": temperature,
        "limit": limit,
        "status": "ALERT" if alert else "NORMAL",
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(event, indent=2) + "\n", encoding="utf-8")
    return alert


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print("Usage: temperature_alert.py TEMPERATURE LIMIT [OUTPUT_FILE]")
        return 2
    try:
        temperature = float(sys.argv[1])
        limit = float(sys.argv[2])
    except ValueError:
        print("Temperature and limit must be numeric")
        return 2

    output_path = Path(sys.argv[3]) if len(sys.argv) == 4 else Path("temperature-alert.json")
    alert = check_temperature(temperature, limit, output_path)
    print("ALERT: temperature limit exceeded" if alert else "NORMAL: temperature is safe")
    return 1 if alert else 0


if __name__ == "__main__":
    raise SystemExit(main())
