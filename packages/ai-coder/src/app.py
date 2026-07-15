"""Huobz multi-model coding agent CLI (lite) — parity with Continue / Aider entrypoints."""
from __future__ import annotations
import argparse, json, urllib.request

DEFAULT = "http://127.0.0.1:11435"

def chat(base: str, prompt: str, model: str = "huobz-coder") -> str:
    req = urllib.request.Request(
        f"{base}/v1/chat/completions",
        data=json.dumps({"model": model, "messages": [
            {"role": "system", "content": "You are Huobz coder. Return concise code-focused answers."},
            {"role": "user", "content": prompt},
        ]}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())
    return data["choices"][0]["message"]["content"]

def main():
    ap = argparse.ArgumentParser(description="Huobz AI Coder")
    ap.add_argument("prompt", nargs="?", default="Write a Python hello world")
    ap.add_argument("--base", default=DEFAULT)
    ap.add_argument("--model", default="huobz-coder")
    args = ap.parse_args()
    try:
        print(chat(args.base, args.prompt, args.model))
    except Exception as e:
        print(f"[offline] {args.prompt}\n# start server: python3 packages/ai/openai_compat_server.py\n# error: {e}")

if __name__ == "__main__":
    main()
