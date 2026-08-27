# Publishing to the official MCP Registry

This repo ships a [`server.json`](./server.json) manifest for
[registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io).
The server name `io.github.tuanone123/hotlikeshop-mcp` is namespaced to this
GitHub account, so publishing is authorized via GitHub — no domain proof needed.

## Automated (recommended) — GitHub Actions + OIDC

The workflow [`.github/workflows/publish-mcp.yml`](./.github/workflows/publish-mcp.yml)
publishes automatically using GitHub OIDC (**no secrets to store**). It runs when a
version tag is pushed, or manually from the Actions tab.

```bash
# tag a release -> the workflow publishes server.json to the registry
git tag v1.0.0
git push origin v1.0.0
```

Or open **Actions → Publish to MCP Registry → Run workflow**.

## Manual (from your machine)

```bash
# 1) install the CLI (macOS/Linux)
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher

# 2) log in with GitHub (device-code flow opens github.com/login/device)
./mcp-publisher login github

# 3) publish the manifest in this folder
./mcp-publisher publish
```

After publishing, the server appears at
`https://registry.modelcontextprotocol.io/v0/servers?search=hotlikeshop`
and is pulled by registry aggregators (Claude, Cursor, etc.).
