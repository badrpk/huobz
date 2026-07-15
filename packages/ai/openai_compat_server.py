"""Huobz OpenAI-compat v3 + usage billing undercut."""
from __future__ import annotations
import json, time, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
sys.path.insert(0, str(Path(__file__).resolve().parent))
import payments as pay

MODELS = [
    {"id": "huobz-edge-mini", "object": "model", "owned_by": "huobz"},
    {"id": "huobz-coder", "object": "model", "owned_by": "huobz"},
    {"id": "huobz-lang-reasoner", "object": "model", "owned_by": "huobz"},
]
USAGE = {"tokens": 0, "requests": 0}
EDGE = {"nodes": 1, "status": "ready", "region": "local"}

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): return
    def _send(self, code, obj):
        data = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers(); self.wfile.write(data)
    def _read(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n).decode() or "{}") if n else {}
    def do_OPTIONS(self): self._send(204, {})
    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/health"):
            return self._send(200, {"ok": True, "service": "huobz-ai", "version": "3.0.0", "parity_target": "OpenAI/Ollama",
                "gaps_closed": ["usage_billing", "api_keys_stub", "function_calling_echo", "stripe"]})
        if path == "/capabilities":
            return self._send(200, {"ok": True, "competitor": "OpenAI + Ollama", "features": [
                "chat_completions","models","embeddings","tools","edge","usage","billing","stripe"]})
        if path == "/pricing": return self._send(200, {"ok": True, **pay.pricing_for("huobz")})
        if path == "/payments/rails": return self._send(200, {"ok": True, "rails": pay.list_rails()})
        if path == "/gap-analysis":
            return self._send(200, {"ok": True, "added": ["usage meters", "token packs $2.99 vs ~$10", "coder pro $6.99 vs ~$20"]})
        if path in ("/v1/models", "/api/tags"): return self._send(200, {"object": "list", "data": MODELS})
        if path == "/v1/edge/status": return self._send(200, {"ok": True, "edge": EDGE})
        if path == "/v1/usage": return self._send(200, {"ok": True, "usage": USAGE})
        self._send(404, {"error": "not_found"})
    def do_POST(self):
        path = urlparse(self.path).path
        body = self._read()
        if path in ("/v1/chat/completions", "/api/chat"):
            messages = body.get("messages") or []
            model = body.get("model") or "huobz-edge-mini"
            last = next((m["content"] for m in reversed(messages) if m.get("role")=="user"), "")
            tools = body.get("tools") or []
            reply = f"[huobz:{model}] {last[:500]}"
            if tools:
                reply += f" (tools: {', '.join(t.get('function',{}).get('name','tool') for t in tools)})"
            pt, ct = max(1, len(last)//4), max(1, len(reply)//4)
            USAGE["tokens"] += pt + ct; USAGE["requests"] += 1
            return self._send(200, {
                "id": f"chatcmpl_{int(time.time())}", "object": "chat.completion", "created": int(time.time()), "model": model,
                "choices": [{"index": 0, "message": {"role": "assistant", "content": reply}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": pt, "completion_tokens": ct, "total_tokens": pt+ct},
            })
        if path in ("/v1/embeddings", "/api/embeddings"):
            text = body.get("input") or body.get("prompt") or ""
            if isinstance(text, list): text = " ".join(map(str, text))
            vec = [((ord(c) % 13)/13.0) for c in (text[:64] or " ")]
            while len(vec) < 32: vec.append(0.0)
            USAGE["requests"] += 1
            return self._send(200, {"object": "list", "data": [{"object": "embedding", "index": 0, "embedding": vec[:32]}],
                                    "model": body.get("model") or "huobz-edge-mini"})
        if path == "/v1/edge/run":
            return self._send(200, {"ok": True, "result": {"echo": body, "node": EDGE}, "ms": 3})
        if path == "/v1/billing/topup":
            inv = pay.create_invoice("huobz", 0, "USD", method=body.get("method") or "stripe",
                                     customer=body.get("customer") or "dev", sku=body.get("sku") or "tokens_1m")
            return self._send(201, {"ok": True, "invoice": inv})
        if path == "/payments/create":
            inv = pay.create_invoice("huobz", float(body.get("amount") or 0), body.get("currency") or "USD",
                method=body.get("method") or "stripe", sku=body.get("sku"), customer=body.get("customer") or "dev")
            return self._send(201, {"ok": True, "invoice": inv})
        self._send(404, {"error": "not_found"})

def main():
    port = int(__import__("os").environ.get("PORT", "11435"))
    print(f"Huobz OpenAI-compat v3 on http://127.0.0.1:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
if __name__ == "__main__":
    main()
