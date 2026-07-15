# Huobz — competitive parity

**Target:** OpenAI API + Ollama local serving + Continue/Aider coding agent entrypoints

| Feature | Path |
|---------|------|
| OpenAI-compatible chat | `packages/ai/openai_compat_server.py` → `POST /v1/chat/completions` |
| Models list | `GET /v1/models` |
| Embeddings | `POST /v1/embeddings` |
| Edge status/run | `/v1/edge/status`, `/v1/edge/run` |
| Multi-model coder CLI | `packages/ai-coder/src/app.py` |

```bash
python3 packages/ai/openai_compat_server.py
# PORT 11435
python3 packages/ai-coder/src/app.py "refactor this function"
```
