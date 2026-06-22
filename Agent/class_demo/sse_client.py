import json
import asyncio
from mcp import  ClientSession
from mcp.client.sse import  sse_client


async def call_tool(client_fn, arg, query, tool_name, params):
    """通用 MCP 工具调用函数"""

    async with client_fn(arg) as (reader, writer):
        # 【注解】三步调用：initialize → list_tools → call_tool
        async with ClientSession(reader, writer) as session:  # 对齐：json-rpc
            await session.initialize()

            result = await session.call_tool(tool_name, params)

            print(f"[返回] {result.content[0].text}")



async  def main():
    await call_tool(
        sse_client,
        "http://localhost:8002/sse",
        "查订单状态",
        "query_order",
        {"order_id": 1001}
    )

if __name__ == "__main__":
    asyncio.run(main())