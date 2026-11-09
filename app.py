
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class ORIVANTIQAI(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_OPTIONS(self):
        self.send_json(200, {"status": "ready"})

    def do_GET(self):
        self.send_json(200, {
            "name": "ORIVANTIQ AI",
            "status": "online"
        })

    def do_POST(self):
        if self.path != "/chat":
            self.send_json(404, {"error": "Endpoint not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            message = body.get("message", "").strip()

            if not message:
                self.send_json(400, {"error": "Please enter a message"})
                return

            self.send_json(200, {
                "assistant": "ORIVANTIQ",
                "reply": "Your message reached the ORIVANTIQ engine. The AI model will be connected next.",
                "received": message
            })

        except Exception:
            self.send_json(400, {"error": "Invalid request"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    server = HTTPServer(("0.0.0.0", port), ORIVANTIQAI)
    print("ORIVANTIQ AI engine started")
    server.serve_forever()


