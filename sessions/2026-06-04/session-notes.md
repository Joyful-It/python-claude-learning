# 学习会话记录 - 2026-06-04

## 今日理解跃迁

> 从"Agent 代码会写就行" → "Middleware 是洋葱皮、Memory 要 thread_id、中间件日志得过滤，工程落地全是细节"

---

## 会话概览

- **日期**：2026-06-04
- **核心主题**：智能差旅助手 Agent 实战（tools+middleware+memory）+ 晨间薄弱点速固
- **代码文件**：`Agent/langchain/chenkao.py`
- **产出**：完整的差旅 Agent（2tool+3中间件+记忆+流式交互）

---

## 学员提出的问题

- "怎么隐藏中间日志呢"
- "刚才需要记忆的你能帮我在稳固一下吗"

---

## 概念与教学内容

### 1. 智能差旅助手 Agent 实战

**需求**：2+ Function Calling、2+ Middleware、开启记忆

**最终代码结构**：
```
导入 → 工具定义 → 模型初始化 → 中间件配置 → 记忆 → Agent组装 → 交互循环
```

**工具**：
- `ask_airport(start_point, end_point, date, time)` — 机票查询
- `book_hotel(city, date, people, budget)` — 酒店预订

**中间件**：
- `SummarizationMiddleware(model=model)` — 记忆压缩，需传 model
- `PIIMiddleware(pii_type="email")` — 邮箱脱敏
- `PIIMiddleware(pii_type="credit_card")` — 银行卡脱敏

**记忆**：
- `InMemorySaver()` — LangGraph checkpointer
- `config={"configurable": {"thread_id": "..."}}` — 必须传 thread_id

### 2. 踩坑记录

| 错误 | 原因 | 修复 |
|------|------|------|
| `transformers` import 卡死 | 库文件损坏 | `pip install --upgrade transformers --force-reinstall` |
| `SummarizationMiddleware()` 缺参数 | 需要传 model | 加 `model=model` |
| `PIIMiddleware()` 缺参数 | 需要传 pii_type | 加 `pii_type="email"` |
| `PIIMiddleware(pii_type="all")` 报错 | 不支持 "all"，只有5种 | 改为 email+credit_card 各一个实例 |
| 中间件日志刷屏 | stream 输出所有 chunk | 过滤只取 `key=="model"` 且 `content!=""` |
| checkpointer 报错 | 缺 thread_id | 加 `config={"configurable": {"thread_id": "..."}}` |

### 3. Agent 流式输出过滤

```python
for chunk in agent.stream(...):
    for key in chunk:
        if key == "model":
            for msg in chunk[key].get("messages", []):
                if hasattr(msg, "content") and msg.content:
                    print(msg.content, end="", flush=True)
```

### 4. 薄弱点速固口诀

| 知识点 | 口诀 |
|--------|------|
| 参数顺序 | **位默元字词** — 位置→默认→*args→关键字→**kwargs |
| HF五件套 | **变数词评加** — Transformers/Datasets/Tokenizers/Evaluate/Accelerate |
| LoRA省256倍 | **(r×2)/d = 16/4096 ≈ 1/256** |
| 消息流转 | **问→空壳调→工具返→最终答** |

---

## 今日核心理解

学员对参数类型的理解：
> "位置参数，关键词参数，关键词在最后"

学员对 LoRA 计算：
> "r=8是小矩阵4096*8 相乘后变为4096*8"

学员对 zero_grad：
> "这是梯度清零吧，不写会将上一轮梯度带进下一轮，导致更新权重不准"

---

## 踩坑与纠正

（详见上方表格，6个踩坑全部修复）

---

## 知识漏洞

- `*args`/`**kwargs` 完整顺序需巩固（口答"位置→默认→*args→关键字→**kwargs"目前不完整）
- HF 五大组件只记住 3/5（缺 Evaluate、Accelerate）
- LoRA 参数计算能说思路，但算不出具体倍数

---

## 关键总结

**PIIMiddleware 五种类型**：`email`、`credit_card`、`ip`、`mac_address`、`url`（不支持 "all"）

**Agent stream 三过滤**：
> model key + content 非空 = 用户看到的文字

**Middleware 踩坑总纲**：
> Summarization 要 model，PII 要 pii_type，Memory 要 thread_id

---

## 完成的练习

- `Agent/langchain/chenkao.py`：完整差旅 Agent（2tool+3middleware+memory+流式交互）
- 晨间复习 9 题
- 薄弱点速固（4口诀）

---

## 学习效果评估

| 考点 | 前值 | 后值 | 备注 |
|------|------|------|------|
| Middleware 实操 | 60% | 70% | 踩坑6个全修复，理解参数依赖 |
| 消息流转 | 70% | 75% | 四步口诀巩固 |
| Agent 完整搭建 | 40% | 65% | 独立完成从导入到交互全流程 |
| *args/**kwargs | 25% | 40% | 口诀"位默元字词" |
| HF五件套 | 30% | 50% | 口诀"变数词评加" |
| LoRA 倍数 | 30% | 50% | 速算公式(r×2)/d |
