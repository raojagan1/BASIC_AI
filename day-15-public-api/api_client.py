import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_todo(output_path: Path) -> int:
    request = Request(API_URL, headers={"User-Agent": "ai-automation-learning"})
    try:
        with urlopen(request, timeout=10) as response:
            data = json.load(response)
    except (HTTPError, URLError, TimeoutError) as error:
        print(f"API request failed: {error}")
        return 1

    required_fields = {"userId", "id", "title", "completed"}
    if not required_fields.issubset(data):
        print("API response is missing required fields")
        return 1

    result = {
        "id": data["id"],
        "title": data["title"],
        "completed": data["completed"],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Saved API result to {output_path}")
    return 0


if __name__ == "__main__":
    import sys

    destination = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("api-result.json")
    raise SystemExit(fetch_todo(destination))
