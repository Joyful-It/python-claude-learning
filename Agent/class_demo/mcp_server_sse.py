import json
from mcp.server.fastmcp import  FastMCP


mcp = FastMCP("DatabaseService-sse",host="0.0.0.0",port=8001)

@mcp.tool()
def query_user(user_id: int) -> str:
    """查询用户信息"""
    users = {1: {"name": "张三", "role": "管理员"}, 2: {"name": "李四", "role": "普通用户"}}
    return json.dumps(users.get(user_id, {"error": "用户不存在"}), ensure_ascii=False)


@mcp.tool()
def query_order(order_id: int) -> str:
    """查询订单状态和金额"""
    orders = {1001: {"amount": 299, "status": "已完成"}, 1002: {"amount": 159, "status": "待发货"}}
    return json.dumps(orders.get(order_id, {"error": "订单不存在"}), ensure_ascii=False)


if __name__ == "__main__":
    transport = "sse"
    mcp.run(transport=transport)