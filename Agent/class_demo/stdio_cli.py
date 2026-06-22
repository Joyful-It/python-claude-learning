import json
import asyncio
from mcp.client.stdio import stdio_client
from mcp import  ClientSession,StdioServerParameters


async def call_tool(client_fn, arg, query, tool_name, params):
    # ════════════ 第 1 层：传输层 ════════════
    # client_fn(arg) 打通与 MCP Server 的物理连接（相当于"拉好电话线"）
    # stdio_client(): 拉起本地 python server.py 子进程,通过 stdin/stdout 通信
    async with client_fn(arg) as (reader, writer):
        # ════════════ 第 2 层：协议层 ════════════
        # ClientSession(reader, writer) 在原始流之上封装 JSON-RPC 2.0 协议
        # （相当于"装上电话机"——自动处理消息格式化、请求-响应配对）
        async with ClientSession(reader, writer) as session:

            await session.initialize()  # 握手: 通知服务端"我要开始通信了"

            res = await session.call_tool(tool_name, params)
            print(f"[返回] {res.content[0].text}")




# 告诉客户端 如何拉取本地 stdio 服务
stdio_pramas = StdioServerParameters(command="python", args=["server.py"])

# 调用stdio 服务  --  asyncio(function
asyncio.run(call_tool(client_fn = stdio_client,
            arg = stdio_pramas,
            query = "查用户信息",
            tool_name = "query_user",
            params = {"user_id": 1}
            )
            )


