# Stitch MCP for ChatGPT / Codex

Production-oriented wrapper for [`davideast/stitch-mcp`](https://github.com/davideast/stitch-mcp), packaged for ChatGPT Desktop / Codex local MCP workflows.

> This repository is an independent wrapper. It is not affiliated with Google or the upstream project.

## Why

Google Stitch exposes design projects and screens through MCP. The upstream `davideast/stitch-mcp` adds a useful local proxy plus higher-level tools such as `build_site`, `get_screen_code`, and `get_screen_image`.

This repo keeps the integration small and reproducible:

- pinned upstream version
- stdio MCP config for ChatGPT Desktop / Codex
- Docker image for isolated local execution
- validation + smoke tests
- GitHub Actions on every push and pull request
- no credentials committed to git

## Requirements

- Node.js 20+
- `npx`
- a Google Stitch API key in `STITCH_API_KEY`, or upstream OAuth/gcloud authentication

## Quick start

```bash
export STITCH_API_KEY='your-key'
cp .mcp.json /path/to/your/project/.mcp.json
```

Or run directly:

```bash
npx -y @_davideast/stitch-mcp@0.9.0 proxy
```

### Verify the upstream CLI

```bash
./scripts/smoke-test.sh
```

## ChatGPT Desktop / Codex

The included `.mcp.json` starts the upstream proxy over stdio:

```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "@_davideast/stitch-mcp@0.9.0", "proxy"]
    }
  }
}
```

Credentials are inherited from the process environment. Do **not** hard-code API keys in `.mcp.json` or commit them to GitHub.

Test prompts:

- `List my Stitch projects.`
- `List screens in project <id>.`
- `Get the HTML for screen <id>.`
- `Build a route map from these Stitch screens.`

## Docker

```bash
docker build -t stitch-mcp-chatgpt .
docker run --rm -i -e STITCH_API_KEY stitch-mcp-chatgpt
```

The container uses stdio intentionally; it is designed to be launched by an MCP client.

## Authentication

### API key

```bash
export STITCH_API_KEY='...'
```

### OAuth / gcloud

Use the upstream setup wizard:

```bash
npx -y @_davideast/stitch-mcp@0.9.0 init
```

See the upstream repository for supported Google authentication modes.

## CI

`.github/workflows/ci.yml` performs:

1. JSON/YAML/repository validation.
2. Upstream CLI resolution and `--help` smoke test.
3. Docker image build.
4. Secret-pattern scan for accidental committed API keys.

CI intentionally does not require a real Stitch credential, so pull requests from forks remain safe.

## Updating the upstream version

The version is intentionally pinned. Update these files together:

- `.mcp.json`
- `Dockerfile`
- `scripts/smoke-test.sh`
- `README.md`

Then run:

```bash
make test
```

## Security

Never commit `STITCH_API_KEY`, Google access tokens, service-account JSON, or OAuth refresh tokens. See [SECURITY.md](SECURITY.md).

## Upstream

- Project: https://github.com/davideast/stitch-mcp
- npm package: `@_davideast/stitch-mcp`
- Upstream license: Apache-2.0

## License

Apache-2.0. See [LICENSE](LICENSE).
