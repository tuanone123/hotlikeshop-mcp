// HOTLIKESHOP MCP — Node quickstart (no dependencies, Node 18+).
// Calls the remote MCP endpoint over JSON-RPC 2.0 (Streamable HTTP).
//   run:  node quickstart/node/search.mjs "gmail"

const ENDPOINT = "https://hotlikeshop.com/api/mcp";
const HEADERS = {
  "Content-Type": "application/json",
  "Accept": "application/json, text/event-stream",
};

async function rpc(method, params) {
  const res = await fetch(ENDPOINT, {
    method: "POST",
    headers: HEADERS,
    body: JSON.stringify({ jsonrpc: "2.0", id: Date.now(), method, params }),
  });
  const text = await res.text();
  // The endpoint may answer as JSON or as a single SSE "data:" line — handle both.
  const line = text.split("\n").find((l) => l.startsWith("data:")) ?? text;
  return JSON.parse(line.replace(/^data:\s*/, ""));
}

const keyword = process.argv[2] || "facebook";

const list = await rpc("tools/list", {});
console.log(`Available tools: ${list.result.tools.length}`);

const out = await rpc("tools/call", {
  name: "search_products",
  arguments: { query: keyword, limit: 5 },
});
console.log(`\nTop matches for "${keyword}":`);
console.log(out.result?.content?.[0]?.text ?? JSON.stringify(out, null, 2));
