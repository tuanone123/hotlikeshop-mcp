#!/usr/bin/env python3
"""HOTLIKESHOP MCP - Python quickstart (stdlib only, no pip install).
Calls the remote MCP endpoint over JSON-RPC 2.0 (Streamable HTTP).
    run:  python quickstart/python/search.py gmail
"""
import json
import sys
import time
import urllib.request

ENDPOINT = "https://hotlikeshop.com/api/mcp"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


def rpc(method, params=None):
    body = json.dumps(
        {"jsonrpc": "2.0", "id": int(time.time()), "method": method, "params": params or {}}
    ).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers=HEADERS, method="POST")
    with urllib.request.urlopen(req, timeout=30) as resp:
        text = resp.read().decode()
    # Endpoint may reply as JSON or a single SSE "data:" line - handle both.
    for line in text.splitlines():
        if line.startswith("data:"):
            return json.loads(line[5:].strip())
    return json.loads(text)


def main():
    keyword = sys.argv[1] if len(sys.argv) > 1 else "facebook"

    tools = rpc("tools/list")
    print(f"Available tools: {len(tools['result']['tools'])}")

    out = rpc("tools/call", {"name": "search_products", "arguments": {"query": keyword, "limit": 5}})
    print(f'\nTop matches for "{keyword}":')
    content = out.get("result", {}).get("content", [])
    print(content[0]["text"] if content else json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
