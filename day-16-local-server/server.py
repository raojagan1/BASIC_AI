from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys


class AutomationHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self.send_json(200, {"status": "ok"})
        elif self.path == "/api/status":
            self.send_json(200, {"service": "ai-automation", "ready": True})
        else:
            self.send_json(404, {"error": "not found"})

    def log_message(self, format_string: str, *args: object) -> None:
        return


def run_server(port: int) -> None:
    server = HTTPServer(("127.0.0.1", port), AutomationHandler)
    print(f"Server listening on http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped")
    finally:
        server.server_close()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    run_server(port)
