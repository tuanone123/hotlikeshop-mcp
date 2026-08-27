<div align="center">

# HOTLIKESHOP MCP Server

**Tra cứu & mua tài khoản MMO / mạng xã hội, proxy và dịch vụ số — ngay trong khung chat của trợ lý AI.**

[![MCP](https://img.shields.io/badge/MCP-Streamable_HTTP-blue)](https://modelcontextprotocol.io)
[![Endpoint](https://img.shields.io/badge/endpoint-live-brightgreen)](https://hotlikeshop.com/api/mcp)
[![Tools](https://img.shields.io/badge/tools-17-orange)](https://hotlikeshop.com/ai)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Website](https://img.shields.io/badge/website-hotlikeshop.com-ff2d55)](https://hotlikeshop.com)

🌐 **[English](./README.md)** · **[🇻🇳 Tiếng Việt](./README.vi.md)**

</div>

---

## Đây là gì?

**HOTLIKESHOP MCP Server** là một [Model Context Protocol](https://modelcontextprotocol.io) server công khai, đang chạy thật (production), cho phép mọi trợ lý AI hỗ trợ MCP — **Claude, Cursor, ChatGPT, Gemini, Perplexity, Windsurf, Cline** — duyệt và mua hàng từ [HOTLIKESHOP](https://hotlikeshop.com), sàn thương mại điện tử Việt Nam bán **tài khoản mạng xã hội & MMO** (Facebook, Instagram, TikTok, X/Twitter, Gmail, Outlook…), **proxy/VPN** và các **dịch vụ số** liên quan, giao hàng tự động 24/7.

- ✅ **Tra cứu KHÔNG cần API key** — tìm kiếm, so sánh, gợi ý, bán chạy dùng được ngay.
- 🔐 **Thanh toán an toàn cho AI** — quy trình 2 bước `quote_order` → `buy_product` kèm token xác nhận ngắn hạn, nên AI **không thể tự tiêu tiền của bạn**.
- 🌍 **Song ngữ** — mọi tool đều có mô tả Anh & Việt; giá theo VND.
- ⚡ **Remote Streamable HTTP** — không cần cài đặt, chỉ trỏ client vào endpoint.

> **Endpoint:** `https://hotlikeshop.com/api/mcp` · **Hướng dẫn:** [hotlikeshop.com/ai](https://hotlikeshop.com/ai)

---

## Bắt đầu nhanh

Thêm HOTLIKESHOP vào mọi MCP client qua endpoint remote. Đa số client desktop kết nối qua cầu [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

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

Mở `claude_desktop_config.json` (Settings → Developer → Edit Config), dán đoạn trên rồi khởi động lại Claude. Xem [`examples/claude_desktop_config.json`](./examples/claude_desktop_config.json).
</details>

<details>
<summary><b>Cursor</b></summary>

Vào **Settings → MCP → Add new server**, hoặc dán vào `.cursor/mcp.json`. Xem [`examples/cursor_mcp.json`](./examples/cursor_mcp.json).
</details>

<details>
<summary><b>Remote gốc (client hỗ trợ Streamable HTTP trực tiếp)</b></summary>

```json
{
  "mcpServers": {
    "hotlikeshop": { "type": "http", "url": "https://hotlikeshop.com/api/mcp" }
  }
}
```
</details>

Kiểm tra endpoint bằng `curl`:

```bash
curl -X POST https://hotlikeshop.com/api/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

> Endpoint chỉ nhận **POST** (JSON-RPC 2.0 qua Streamable HTTP). Gọi `GET` sẽ trả 405 — đúng như thiết kế.

---

## 17 công cụ (tools)

### 🔎 Tra cứu — công khai, miễn phí, không cần key (9)

| Tool | Chức năng |
|------|-----------|
| `search_products` | Tìm sản phẩm công khai theo từ khóa; trả id, tên, giá (VND), tồn kho, danh mục, url. |
| `get_product` | Chi tiết đầy đủ 1 sản phẩm theo id (kèm mô tả). |
| `list_categories` | Liệt kê danh mục công khai kèm số sản phẩm. |
| `list_category_products` | Sản phẩm trong 1 danh mục theo `category_id`. |
| `recommend_products` | Gợi ý SP còn hàng theo ngân sách và/hoặc từ khóa/danh mục, rẻ trước, kèm gợi ý combo. |
| `best_sellers` | SP bán chạy còn hàng (bán nhiều nhất trước). |
| `latest_products` | SP mới còn hàng (thêm gần đây nhất trước). |
| `compare_products` | So sánh 2–5 SP cạnh nhau kèm tóm tắt nhanh (rẻ nhất / nhiều hàng / bán chạy). |
| `similar_products` | Từ 1 product id, gợi ý các SP tương tự còn hàng (ưu tiên cùng danh mục). |

### 🛒 Mua hàng — cần API key của bạn (4)

| Tool | Chức năng |
|------|-----------|
| `get_my_balance` | Số dư (VND), hạng tài khoản và chiết khấu của bạn. |
| `quote_order` | Báo giá đơn và trả **token xác nhận** ngắn hạn (bước 1/2). |
| `buy_product` | Hoàn tất mua bằng token xác nhận (bước 2/2). |
| `check_order_status` | Theo dõi trạng thái giao đơn. |

> Lấy API key tại [hotlikeshop.com/profile](https://hotlikeshop.com/profile) → **API**. Quy trình báo giá → xác nhận 2 bước bảo đảm AI không thể âm thầm tiêu hết số dư.

### 🧰 Tiện ích MMO — miễn phí (4)

| Tool | Chức năng |
|------|-----------|
| `check_live_facebook` | Kiểm tra 1 UID Facebook sống/chết (truyền `proxy` riêng để check chuẩn). |
| `check_health_bulk` | Kiểm tra sống/chết hàng loạt tối đa 20 tài khoản (Facebook / Instagram / Telegram / TikTok). |
| `deep_inspect` | Soi sâu hồ sơ công khai (follower, bio, verified, media / thành viên / avatar). |
| `topup_guide` | Hướng dẫn nạp tiền. Chỉ thông tin — MCP không xử lý thanh toán. |

---

## Vì sao nên kết nối?

- **Agentic commerce an toàn.** Cửa hàng chạy thật với MCP server công khai, đúng chuẩn, thanh toán 2 bước bằng token xác nhận.
- **Test không rào cản.** Toàn bộ nhóm tra cứu miễn phí, không cần key — kết nối là query được ngay.
- **Máy đọc được ở mọi nơi.** Công khai [`llms.txt`](https://hotlikeshop.com/llms.txt), `llms-full.txt` và [Catalog JSON](https://hotlikeshop.com/api/public/catalog) song song với MCP server.

---

## Tài nguyên

| | |
|---|---|
| 🔌 MCP endpoint | `https://hotlikeshop.com/api/mcp` (Streamable HTTP) |
| 📖 Hướng dẫn & config | [hotlikeshop.com/ai](https://hotlikeshop.com/ai) |
| 🗂️ Catalog JSON | [/api/public/catalog](https://hotlikeshop.com/api/public/catalog) |
| 🤖 llms.txt | [/llms.txt](https://hotlikeshop.com/llms.txt) |
| 🏪 Website | [hotlikeshop.com](https://hotlikeshop.com) |
| 💬 Hỗ trợ | [Zalo](https://zalo.me/0772868229) · [Telegram](https://t.me/hotlikesp) |

---

## Giấy phép

[MIT](./LICENSE) cho phần tài liệu & cấu hình này. Dịch vụ HOTLIKESHOP vận hành tại [hotlikeshop.com](https://hotlikeshop.com); kết nối MCP server là miễn phí.
