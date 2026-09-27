from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

MAX_BODY_SIZE = 1_000_000


class WebhookHandler(BaseHTTPRequestHandler):
    log_path = Path("webhook-events.jsonl")

    def send_json(self, status_code: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        if self.path != "/webhook":
            self.send_json(404, {"error": "not found"})
            return

        try:
            body_size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json(400, {"error": "invalid content length"})
            return
        if body_size > MAX_BODY_SIZE:
            self.send_json(413, {"error": "request too large"})
            return

        try:
            payload = json.loads(self.rfile.read(body_size))
        except json.JSONDecodeError:
            self.send_json(400, {"error": "request must contain valid JSON"})
            return
        if not isinstance(payload, dict):
            self.send_json(400, {"error": "JSON payload must be an object"})
            return

        event = {
            "received_at": datetime.now(timezone.utc).isoformat(),
            "payload": payload,
        }
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(event) + "\n")
        self.send_json(200, {"accepted": True})

    def log_message(self, format_string: str, *args: object) -> None:
        return


def run_server(port: int, log_path: Path) -> None:
    WebhookHandler.log_path = log_path
    server = HTTPServer(("127.0.0.1", port), WebhookHandler)
    print(f"Webhook receiver listening on http://127.0.0.1:{port}/webhook")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Webhook receiver stopped")
    finally:
        server.server_close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    log_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("webhook-events.jsonl")
    run_server(port, log_path)
