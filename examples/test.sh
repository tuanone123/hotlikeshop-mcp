#!/usr/bin/env bash
# Quick smoke test for the HOTLIKESHOP MCP endpoint (Streamable HTTP, JSON-RPC 2.0).
# Usage: bash examples/test.sh
set -euo pipefail

ENDPOINT="https://hotlikeshop.com/api/mcp"

echo "== tools/list =="
curl -sS -X POST "$ENDPOINT" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'

echo
echo "== tools/call: search_products (keyword=gmail) =="
curl -sS -X POST "$ENDPOINT" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"search_products","arguments":{"query":"gmail","limit":3}}}'
echo
