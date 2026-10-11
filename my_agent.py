import asyncio
import json
import subprocess
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import requests
import os

MCP_PATH = os.environ.get("MCP_EXECUTABLE", r"E:\venv\Scripts\world-intel-mcp.exe")
# 你的本地 LM Studio 模型 API
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "qwen2.5-coder-7b-instruct"


async def main():
    # 1. 连接到你的 world-intel MCP 服务
    server_params = StdioServerParameters(
        command=MCP_PATH, # 你的exe路径
        args=[]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 2. 获取所有工具，只留下我们需要的那一个
            tools = await session.list_tools()
            target_tool = None
            for tool in tools.tools:
                if tool.name == "intel_daily_digest":
                    target_tool = tool
                    break

            if not target_tool:
                print("找不到 intel_daily_digest 工具")
                return

            print(f"成功连接工具: {target_tool.name}")

            # 3. 构造给模型的提示词（告诉它有什么工具，并让它决定是否调用）
            prompt = f"""
            你是一个安全助手。你现在有一个工具叫 {target_tool.name}，
            描述是：{target_tool.description}。
            用户请求：帮我查询最近24小时关于金融系统网络攻击的新闻。
            如果需要调用工具，请直接输出JSON格式的调用指令，不要输出其他内容。
            格式：{{"tool": "intel_daily_digest", "arguments": {{"keywords": "financial systems network attack", "time_range": "24h"}}}}
            如果不需要，直接回答。
            """

            # 4. 发送给本地大模型，让它输出行动计划
            payload = {
                "model": MODEL_NAME,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1
            }
            resp = requests.post(LM_STUDIO_URL, json=payload).json()
            ai_reply = resp["choices"][0]["message"]["content"]
            print(f"模型打算调用: {ai_reply}")

            # 5. 如果模型决定调用工具，我们就手动执行它！
            if "intel_daily_digest" in ai_reply:
                # 这里我们按模型给的参数去调用 MCP 工具
                result = await session.call_tool("intel_daily_digest",
                                                 arguments={"keywords": "financial systems network attack",
                                                            "time_range": "24h"})

                print("\n" + "=" * 50)
                print("🎉 成功调用 MCP 工具！返回的真实数据如下：")
                print("=" * 50)
                # 打印真实返回的数据，证明它不是瞎编的
                for content in result.content:
                    if hasattr(content, 'text'):
                        print(content.text)
            else:
                print("模型没有选择调用工具，它直接回答了：", ai_reply)


if __name__ == "__main__":
    asyncio.run(main())