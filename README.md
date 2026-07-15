# Huobz 🌐

Open **software ecosystem monorepo** — AI, edge, language, and coding tools.

## Download

```bash
git clone https://github.com/badrpk/huobz.git
cd huobz
```

## Packages

| Path | Product |
|------|---------|
| `packages/ai` | HuobzAi core |
| `packages/ai-lib` | Shared AI library |
| `packages/edge` | Edge runtime |
| `packages/lang` | HuobzLang |
| `packages/ai-coder` | Multi-model coding agent |
| root `ai/`, `api/`, … | Platform modules |

## Use

```bash
# Edge example
python3 packages/edge/huobz_edge_node.py  # if present

# AI coder
cd packages/ai-coder && python3 src/app.py  # if scaffolded
```

## Contribute

We want the community to **download, use, and improve** Huobz.  
See [CONTRIBUTING.md](CONTRIBUTING.md) · [COMMUNITY.md](COMMUNITY.md)

## License

See LICENSE files in packages; contributions welcome.
