# 🛡️ 本地金融安全情报 Agent (Financial Security Intelligence Agent)

## 📖 项目简介
一个基于**本地大模型**与 **MCP (Model Context Protocol)** 协议的自动化安全情报分析 Agent。无需支付昂贵的云端 API 费用，利用本地算力（32G 内存笔记本）即可实现从全球开源情报源（OSINT）抓取数据，并自动生成金融网络威胁简报。

## ✨ 核心亮点 (Highlights)
- **手写 Agent 闭环**：绕过 LM Studio 界面的兼容性限制，使用 Python 手写 MCP Client，实现 `LLM 决策 -> Tool Calling -> 结果回传 -> 自动报告` 的完整闭环。
- **真实数据抓取**：集成 `world-intel-mcp` 的 132 个工具，成功捕获真实世界的 QakBot 恶意软件情报与高危 IP。
- **极客级环境隔离**：攻克 Windows 环境下 PEP 668 限制，完美隔离虚拟环境，杜绝路径污染。
- **向量检索支持**：集成 `fastembed` 与 `qdrant-client`，支持基于语义的情报检索。

## 🏗️ 系统架构
```text
[ 用户提问 ]
      ↓
[ my_agent.py (Python 客户端) ]
      ↓                                 ↓
[ LM Studio (本地 LLM) ] <----> [ MCP Client ]
      ↓                                 ↓
[ 输出自然语言简报 ]           [ world-intel-mcp (132个工具) ]
                                        ↓
                                 [ 真实互联网 OSINT 源 ]