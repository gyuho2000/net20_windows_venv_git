"""
12) 로컬 HTTP 서버(가장 쉬운 서버)
- 브라우저에서도 접속 가능: http://127.0.0.1:8001/hello
"""
from __future__ import annotations
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, obj: dict):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/health":
            return self._send(200, {"ok": True})
        if u.path == "/hello": 
            q = parse_qs(u.query)
            name = (q.get("name") or ["world"])[0]
            return self._send(200, {"message": f"hello {name}"})
        return self._send(404, {"error": "not found", "path": u.path})

def main():
    addr = ("127.0.0.1", 8001)
    print("Local HTTP server running:", f"http://{addr[0]}:{addr[1]}")
    HTTPServer(addr, Handler).serve_forever()

if __name__ == "__main__":
    main()
