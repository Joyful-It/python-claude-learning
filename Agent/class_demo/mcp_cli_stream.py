import asyncio, json
from mcp import ClientSession
from mcp.client.streamable_http import  streamable_http_client



async def call_tool(client_fn, arg, query, tool_name, params):
    """通用 MCP 工具调用函数"""

    # ════════════ 第 1 层：传输层 ════════════
    # client_fn(arg) 打通与 MCP Server 的物理连接（相当于"拉好电话线"）
    # streamable_http_client 返回 3 个值:
    #   - reader:  从服务端接收消息的流（听筒）
    #   - writer:  向服务端发送消息的流（话筒）
    #   - get_session_id: 获取当前 session ID 的回调函数（仅 streamable_http 有）
    # sse_client/stdio_client 只返回 2 个值 (reader, writer)
    async with client_fn(arg) as (reader, writer, get_session_id):
        
        # ════════════ 第 2 层：协议层 ════════════
        # ClientSession 在原始字节流之上封装 JSON-RPC 2.0 协议（相当于"装上电话机"）
        # 它会自动处理: JSON-RPC 消息格式化、请求-响应配对、生命周期管理
        # 这样上层代码就不用手动拼 json.dumps/json.loads 了
        async with ClientSession(reader, writer) as session:
            await session.initialize()     # 握手: 通知服务端"我要开始通信了"

            result = await session.call_tool(tool_name, params)  # 调用远端工具
            print(f"[返回] {result.content[0].text}")




async def main():
    await call_tool(
        client_fn=streamable_http_client,
        arg="http://localhost:8001/mcp",
        query="查订单状态",
        tool_name="query_order",
        params={"order_id": 1001}
    )

asyncio.run(main())