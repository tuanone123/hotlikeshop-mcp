# Quickstart — call the HOTLIKESHOP MCP directly

Minimal, dependency-free examples that hit the remote endpoint
`https://hotlikeshop.com/api/mcp` over JSON-RPC 2.0 (Streamable HTTP).
Great for testing before wiring the server into Claude / Cursor.

## Node (18+)

```bash
node quickstart/node/search.mjs "gmail"
```

## Python (3.8+)

```bash
python quickstart/python/search.py gmail
```

## Raw curl

```bash
curl -X POST https://hotlikeshop.com/api/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_products","arguments":{"query":"gmail","limit":5}}}'
```

> Lookup tools are free and need no API key. Purchase tools (`quote_order`, `buy_product`, …)
> require your shop API key — get it at <https://hotlikeshop.com/profile> → **API**.
