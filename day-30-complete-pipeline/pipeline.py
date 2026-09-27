from datetime import datetime, timezone
import json
from pathlib import Path
import sys


def run_pipeline(input_path: Path, output_path: Path) -> int:
    try:
        event = json.loads(input_path.read_text(encoding="utf-8"))
        moisture = float(event["soil_moisture"])
        temperature = float(event["temperature"])
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Pipeline failed: invalid input ({error})")
        return 2

    actions: list[str] = []
    if moisture < 40:
        actions.append("pump_on")
    else:
        actions.append("pump_off")
    if temperature >= 35:
        actions.append("temperature_alert")

    result = {
        "processed_at": datetime.now(timezone.utc).isoformat(),
        "trigger": event,
        "classification": {
            "soil": "dry" if moisture < 40 else "adequately_moist",
            "temperature": "hot" if temperature >= 35 else "normal",
        },
        "actions": actions,
        "status": "completed",
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Pipeline completed: {output_path}")
    print(f"Actions: {', '.join(actions)}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: pipeline.py INPUT_JSON OUTPUT_JSON")
        raise SystemExit(2)
    raise SystemExit(run_pipeline(Path(sys.argv[1]), Path(sys.argv[2])))
