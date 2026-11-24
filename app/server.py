"""Klauzula v0.1 — local web server (Python standard library only).

Run:  python3 app/server.py   → open http://localhost:8000
"""
import base64
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import engine  # noqa: E402
from engine import compare, parser, report  # noqa: E402

APP_DIR = Path(__file__).resolve().parent
STATIC = APP_DIR / "static"
SAMPLES = APP_DIR / "samples"
MAX_UPLOAD = 5 * 1024 * 1024
CONTENT_TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
                 ".js": "application/javascript; charset=utf-8", ".svg": "image/svg+xml"}


def document_text(payload, prefix=""):
    """Get contract text from {text} or {file_b64, filename}."""
    if payload.get(prefix + "text"):
        return payload[prefix + "text"]
    data = base64.b64decode(payload.get(prefix + "file_b64", ""))
    name = payload.get(prefix + "filename", "").lower()
    if name.endswith(".docx"):
        return parser.docx_to_text(data)
    if name.endswith((".txt", ".md")):
        return data.decode("utf-8", errors="replace")
    raise ValueError("Upload a .docx or .txt file, or paste the text.")


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type="application/json; charset=utf-8", headers=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False)
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/playbook":
            return self._send(200, engine.load_playbook())
        if path == "/api/samples":
            return self._send(200, {p.stem: p.read_text(encoding="utf-8") for p in sorted(SAMPLES.glob("*.txt"))})
        if path == "/api/status":
            return self._send(200, {"claude_available": engine.llm.available(), "model": engine.llm.MODEL})
        file = STATIC / ("index.html" if path == "/" else path.lstrip("/"))
        if file.resolve().parent != STATIC.resolve() or not file.is_file():
            return self._send(404, {"error": "Not found"})
        self._send(200, file.read_bytes(), CONTENT_TYPES.get(file.suffix, "application/octet-stream"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_UPLOAD * 2:
            return self._send(413, {"error": "File is larger than 5 MB."})
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
            if self.path == "/api/review":
                result = engine.review(document_text(payload), payload.get("filename", ""),
                                       use_claude=payload.get("use_claude"))
                return self._send(200, result)
            if self.path == "/api/compare":
                pb = engine.load_playbook()
                old = parser.split_clauses(engine.masking.mask(document_text(payload, "old_"))[0])
                new = parser.split_clauses(engine.masking.mask(document_text(payload, "new_"))[0])
                return self._send(200, compare.compare(old, new, pb))
            if self.path == "/api/export":
                review, decisions = payload["review"], payload.get("decisions", {})
                if payload.get("format") == "md":
                    return self._send(200, report.to_markdown(review, decisions), "text/markdown; charset=utf-8",
                                      {"Content-Disposition": 'attachment; filename="nda-review.md"'})
                return self._send(200, report.to_word_html(review, decisions), "application/msword",
                                  {"Content-Disposition": 'attachment; filename="nda-review.doc"'})
            return self._send(404, {"error": "Not found"})
        except (ValueError, KeyError) as exc:
            return self._send(400, {"error": str(exc)})

    def log_message(self, fmt, *args):
        sys.stderr.write("[klauzula] " + fmt % args + "\n")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("Klauzula v0.1 → http://localhost:{}  (Claude mode: {})".format(
        port, "on" if engine.llm.available() else "off, rule-based demo"))
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
