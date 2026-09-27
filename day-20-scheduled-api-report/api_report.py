from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.request import Request, urlopen

API_URL = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_report(output_path: Path) -> int:
    request = Request(API_URL, headers={"User-Agent": "ai-automation-learning"})
    try:
        with urlopen(request, timeout=10) as response:
            todo = json.load(response)
    except Exception as error:
        print(f"API report failed: {error}")
        return 1

    report = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source": API_URL,
        "item": {
            "id": todo.get("id"),
            "title": todo.get("title"),
            "completed": todo.get("completed"),
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"API report created: {output_path}")
    return 0


if __name__ == "__main__":
    import sys

    destination = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("api-report.json")
    raise SystemExit(fetch_report(destination))
