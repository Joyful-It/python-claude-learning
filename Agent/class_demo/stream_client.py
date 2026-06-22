import json
import asyncio
from mcp import  ClientSession
from mcp.client.streamable_http import  streamable_http_client




async def call_tool(client_fn, arg, query, tool_name, params):
    """通用 MCP 工具调用函数"""
    async with client_fn(arg) as (reader, writer, _):

        async with ClientSession(reader, writer) as session:  # 对齐：json-rpc
            await session.initialize()
            result = await session.call_tool(tool_name, params)

            print(f"[返回] {result.content[0].text}")





async def main():
    await call_tool(
        streamable_http_client,
        "http://localhost:8001/mcp",
        "查订单状态",
        "query_order",
        {"order_id": 1001}
    )

if __name__ == "__main__":
    asyncio.run(main())