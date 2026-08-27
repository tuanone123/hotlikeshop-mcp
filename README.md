<div align="center">

# HOTLIKESHOP MCP Server

**Search & buy MMO / social-media accounts, proxies and digital services from any AI assistant — right inside the chat.**

[![MCP](https://img.shields.io/badge/MCP-Streamable_HTTP-blue)](https://modelcontextprotocol.io)
[![Endpoint](https://img.shields.io/badge/endpoint-live-brightgreen)](https://hotlikeshop.com/api/mcp)
[![Tools](https://img.shields.io/badge/tools-19-orange)](https://hotlikeshop.com/ai)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![hotlikeshop-mcp MCP server](https://glama.ai/mcp/servers/tuanone123/hotlikeshop-mcp/badges/score.svg)](https://glama.ai/mcp/servers/tuanone123/hotlikeshop-mcp)
[![Website](https://img.shields.io/badge/website-hotlikeshop.com-ff2d55)](https://hotlikeshop.com)

🌐 **[English](./README.md)** · **[🇻🇳 Tiếng Việt](./README.vi.md)**

</div>

---

## What is this?

**HOTLIKESHOP MCP Server** is a public, production [Model Context Protocol](https://modelcontextprotocol.io) server that lets any MCP-capable AI assistant — **Claude, Cursor, ChatGPT, Gemini, Perplexity, Windsurf, Cline** — browse and purchase from [HOTLIKESHOP](https://hotlikeshop.com), a Vietnamese e-commerce marketplace for **social-media & MMO accounts** (Facebook, Instagram, TikTok, X/Twitter, Gmail, Outlook…), **proxies/VPN** and related **digital services**, delivered automatically 24/7.

- ✅ **No API key needed for lookup** — search, compare, recommend, best-sellers work out of the box.
- 🔐 **Safe agentic checkout** — a 2-step `quote_order` → `buy_product` flow with a short-lived confirm token, so the AI **cannot spend money on its own**.
- 🌍 **Bilingual** — every tool speaks English & Vietnamese; prices in VND.
- ⚡ **Remote Streamable HTTP** — nothing to install, just point your client at the endpoint.

> **Endpoint:** `https://hotlikeshop.com/api/mcp` · **Docs:** [hotlikeshop.com/ai](https://hotlikeshop.com/ai)

---

## Quick start

Add HOTLIKESHOP to any MCP client using the remote endpoint. Most desktop clients connect through the [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) bridge:

```json
{
  "mcpServers": {
    "hotlikeshop": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://hotlikeshop.com/api/mcp"]
    }
  }
}
```

<details>
<summary><b>Claude Desktop</b></summary>

Edit `claude_desktop_config.json` (Settings → Developer → Edit Config) and paste the snippet above, then restart Claude. See [`examples/claude_desktop_config.json`](./examples/claude_desktop_config.json).
</details>

<details>
<summary><b>Cursor</b></summary>

Add it in **Settings → MCP → Add new server**, or drop the snippet into `.cursor/mcp.json`. See [`examples/cursor_mcp.json`](./examples/cursor_mcp.json).
</details>

<details>
<summary><b>Cline / Roo (VS Code)</b></summary>

Open **Cline → MCP Servers → Configure** (edits `cline_mcp_settings.json`) and add the same `mcpServers` entry:

```json
{
  "mcpServers": {
    "hotlikeshop": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://hotlikeshop.com/api/mcp"]
    }
  }
}
```
</details>

<details>
<summary><b>Windsurf</b></summary>

Edit `~/.codeium/windsurf/mcp_config.json` and paste the `mcpServers` snippet above, then reload.
</details>

<details>
<summary><b>Native remote (clients that support Streamable HTTP directly)</b></summary>

```json
{
  "mcpServers": {
    "hotlikeshop": { "type": "http", "url": "https://hotlikeshop.com/api/mcp" }
  }
}
```
</details>

Test the endpoint with plain `curl`:

```bash
curl -X POST https://hotlikeshop.com/api/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

> The endpoint accepts **POST only** (JSON-RPC 2.0 over Streamable HTTP). A `GET` returns 405 — that is expected.

Prefer code? Copy-paste, dependency-free examples live in [`quickstart/`](./quickstart) (Node & Python). A live docs page is published at **[tuanone123.github.io/hotlikeshop-mcp](https://tuanone123.github.io/hotlikeshop-mcp/)**.

---

## The 18 tools

> 🌍 **International-friendly:** product prices are returned in **both VND and USD** (`price_usd`, live rate), `topup_guide` and `how_to_start` speak **English** (`lang:"en"`), and you can top up with **USDT (TRC20/EVM)** — no Vietnamese required.

### 🔎 Lookup & onboarding — public, free, no key (10)

| Tool | What it does |
|------|--------------|
| `how_to_start` | New-user onboarding: 4 steps to create an account, get an API key, top up (USDT for international users) and buy. English or Vietnamese (`lang`). |
| `search_products` | Search public products by keyword; returns id, name, price (VND + USD), stock, category, url. |
| `get_product` | Full details of one product by id (including description). |
| `list_categories` | All public categories with product counts. |
| `list_category_products` | Products inside a category by `category_id`. |
| `recommend_products` | Suggest in-stock products by budget and/or keyword/category, cheapest first, with a combo hint. |
| `best_sellers` | Best-selling in-stock products (most sold first). |
| `latest_products` | Newest in-stock products (recently added first). |
| `compare_products` | Compare 2–5 products side by side with a quick summary (cheapest / most stock / best seller). |
| `similar_products` | Given a product id, list similar in-stock alternatives (same category first). |

### 🛒 Purchase — needs your shop API key (4)

| Tool | What it does |
|------|--------------|
| `get_my_balance` | Your account balance (VND), level and discount. |
| `quote_order` | Price an order and return a short-lived **confirm token** (step 1 of 2). |
| `buy_product` | Complete the purchase using the confirm token (step 2 of 2). |
| `check_order_status` | Track an order's delivery status. |

> Get your API key at [hotlikeshop.com/profile](https://hotlikeshop.com/profile) → **API**. The two-step quote → confirm flow means an AI agent can never silently drain your balance.

### 🧰 MMO utilities — free (4)

| Tool | What it does |
|------|--------------|
| `check_live_facebook` | Check whether a Facebook UID is live or dead (pass your own `proxy` for reliable checks). |
| `check_health_bulk` | Bulk live/dead check for up to 20 accounts (Facebook / Instagram / Telegram / TikTok). |
| `deep_inspect` | Deep public profile lookup (followers, bio, verified, media / members / avatar). |
| `topup_guide` | Explain how to add funds. Info only — MCP never processes payments. |

---

## Why connect?

- **Agentic commerce, done safely.** Real production storefront with a public, spec-compliant MCP server and a two-step confirm-token checkout.
- **Zero-friction evaluation.** The whole lookup group is free and keyless — connect and query in seconds.
- **Machine-readable everywhere.** Public [`llms.txt`](https://hotlikeshop.com/llms.txt), `llms-full.txt` and a [Catalog JSON](https://hotlikeshop.com/api/public/catalog) feed alongside the MCP server.

---

## Resources

| | |
|---|---|
| 🔌 MCP endpoint | `https://hotlikeshop.com/api/mcp` (Streamable HTTP) |
| 📖 Docs & config | [hotlikeshop.com/ai](https://hotlikeshop.com/ai) |
| 🗂️ Catalog JSON | [/api/public/catalog](https://hotlikeshop.com/api/public/catalog) |
| 🤖 llms.txt | [/llms.txt](https://hotlikeshop.com/llms.txt) |
| 🏪 Website | [hotlikeshop.com](https://hotlikeshop.com) |
| 💬 Support | [Zalo](https://zalo.me/0772868229) · [Telegram](https://t.me/hotlikesp) |

---

## Keywords

MCP server · Model Context Protocol · Claude · Cursor · ChatGPT · agentic commerce · AI shopping · e-commerce MCP · social media accounts · MMO · proxy · Vietnam · Streamable HTTP · remote MCP.

## License

[MIT](./LICENSE) for this documentation & configuration. The HOTLIKESHOP service itself is operated at [hotlikeshop.com](https://hotlikeshop.com); connecting to the MCP server is free.
