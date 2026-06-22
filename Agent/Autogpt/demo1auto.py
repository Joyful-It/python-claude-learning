# ============================================================
# AutoGPT 核心演示：Think-Act 循环（简化版）
# 流程：拆解任务 → 执行第一个 → 判断是否还有 → 继续/结束
# ============================================================

import sys, os
# ⚠️ model.py 在上级目录 Agent/，必须加入搜索路径
# 不能用 '..'（相对工作目录），用 __file__ 取脚本绝对路径再算上级目录
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model import llm
from typing import TypedDict

# ==================== Step 1: 定义状态 ====================
class Auto_state(TypedDict):
    objective: str    # 总目标（用户输入）
    tasks: list       # 待做任务列表（LLM拆的）
    result: str       # 上一步执行结果（空=刚开始）

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END


# ==================== Step 2: 定义节点 ====================

def think(state: Auto_state):
    """思考节点：让 LLM 拆解/重排任务列表"""
    if state["result"]:
        # 有执行结果 → 重排剩余任务（可调整）
        remaining = ",".join(state['tasks'])
        prompt = f"""目标：{state['objective']}
                    已完成：{state['result']}
                    剩余任务：{remaining}

                    请安排剩余任务。除非上一步结果提示有必要调整，否则原样输出。每行一个。"""
    else:
        # 刚开始 → 首次拆解目标为子任务
        prompt = f"目标：{state['objective']}    请按顿号分隔的子项拆成任务，每个子项作为一个任务，不要进一步拆分。每行一个，不要序号。"

    # 调 LLM 拆解任务
    # ⚠️ llm.invoke() 参数必须是列表 [HumanMessage(...)]，不能直接传 HumanMessage
    response = llm.invoke([HumanMessage(content=prompt)])
    tasks = [t.strip() for t in response.content.strip().split('\n') if t.strip()]

    label = "decompose again" if state["result"] else "first decompose"
    print(f"\n[{label}] 当前任务列表({len(tasks)})")
    for i, t in enumerate(tasks, 1):
        print(f"  {i}. {t}")

    # ⚠️ 节点必须 return dict 才能更新 State！只 print 不 return，State 拿不到
    return {"tasks": tasks}


def act(state: Auto_state):
    """执行节点：取任务列表第一条执行，返回剩余任务"""
    task = state["tasks"][0]                     # 取第一个任务
    print(f"act this task {task}")
    print(f"finshed task{task}")
    remaining_task = state["tasks"][1:]          # 剩下的任务
    # 返回：tasks 更新为剩余，result 标记已完成
    return {"tasks": remaining_task, "result": "task"}


def route(state: Auto_state):
    """路由函数：判断还有没有任务 → 决定下一站
    ⚠️ Route 返回 str（节点名），不是 dict！"""
    if state['tasks']:
        print(f"还剩{len(state['tasks'])}个任务，继续。。\n")
        return "think"    # 还有任务 → 回到 think 重评估
    print("finshed it")
    return END          # 没有任务 → 结束


# ==================== Step 3: 构建图 ====================

builder = StateGraph(Auto_state)                      # ⚠️ 必须传 State 类型！
builder.add_node("think", think)
builder.add_node("act", act)

builder.add_edge(START, "think")                      # 启动 → 思考
builder.add_edge("think", "act")                      # 思考 → 执行

# ⚠️ path_map 是路标字典：route返回的字符串 → 实际节点
# "think"（字符串）映射到 "think"（节点名）
# "END"（字符串）映射到 END（LangGraph 结束常量）
builder.add_conditional_edges("act", route)

# ==================== Step 4: 编译与运行 ====================

app = builder.compile()

result = app.invoke({
    "objective": "帮小明完成周末作业：做完数学卷子、背 20 个英语单词、写一篇 300 字日记",
    "result": ""
})
print(result)