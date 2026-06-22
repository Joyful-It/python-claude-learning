# 2026-06-11 会话笔记

## 今日理解跃迁

从"AutoGPT Think-Act 循环能跑通" → 能独立区分 AutoGPT vs BabyAGI 的核心差异：AutoGPT 每次 think 重新生成任务列表，BabyAGI 只重排优先级。

## 会话概览

- **日期**：2026-06-11
- **核心主题**：AutoGPT/BabyAGI 课件测验（14题）+ 题库轻量索引建设
- **测验结果**：14题 ✅12 ❌2（Q1循环顺序、Q3 route返回值）

## 课件测验（14题）

### 答对题目

| 题号 | 知识点 | 掌握情况 |
|------|--------|---------|
| Q2 | AutoGPT vs BabyAGI 核心区别（重新生成 vs 重排） | ✅ |
| Q4 | BabyAGI 灵魂 = reprioritize 动态重排 | ✅ |
| Q5 | BabyAGI 执行完后先重排再继续 | ✅ |
| Q6 | act 移除已执行任务 + 记录结果 | ✅ |
| Q7 | 循环结构多选（ABC全对） | ✅ |
| Q8 | think 节点能力多选（ABD全对） | ✅ |
| Q9 | reprioritize 排序非硬编码 | ✅ |
| Q10 | think 非每次从零生成 | ✅ |
| Q11 | 终止条件 = 任务队列为空 | ✅ |
| Q12 | act 移除第1个任务 | ✅ |
| Q13 | think 初次 vs 再次拆解区别 | ✅ |
| Q14 | BabyAGI 动态重排原因 | ✅ |

### 踩坑与纠正

| 题号 | 错误 | 正确 | 原因 |
|------|------|------|------|
| Q1 | 选B「拆解→执行→观察→再拆解」 | A「拆解→观察→执行→再拆解」 | 概念划分：think节点观察+拆解合一，先读state再让LLM生成，逻辑上是"先看后想再动手" |
| Q3 | 选B「"act"」 | C「"think"」 | 和「上一个节点是act」搞混——route决定的是下一站去哪，不是回哪。口诀"route指向下一站，不是回头看" |

### 晨考薄弱

无（本次课件测验非正式晨考）

## 今日核心理解

学员在 AutoGPT/BabyAGI 对比上表现扎实，14题错2题，错因集中在"概念名称对应的代码行为"上（Q1 think=观察+拆解合一，Q3 route返回的是目标节点而非来源节点）。

## 关键总结

1. **AutoGPT vs BabyAGI**：AutoGPT 每次 think 重新生成任务列表（可增删改），BabyAGI 只对已有任务重排优先级
2. **route 口诀**："route指向下一站，不是回头看"——返回的是目标节点字符串
3. **think 节点行为**：初次 result 为空→从零拆解；再次 result 有内容→动态调整
4. **BabyAGI 灵魂 = reprioritize**：每步后用 LLM 重新校准优先级，因为初始顺序基于不完整信息
5. **循环终止**：两者都是任务队列为空→END

## 题库系统更新

- **新建** `knowledge-index-light.md`（152题轻量索引）
- **新建** `questions-gpt-light.md`（148题轻量索引）
- **新增** C031-C044 入库 `question-bank.md`（AutoGPT/BabyAGI 14题）
- **更新** `question-index.md` 索引
- **更新** `CLAUDE.md` 晨考执行流程 + 学员手动入库指南
- **新增** C045-C060（模块三HTML课件提取16题）：MessagesState内部机制/Fan-out-Fan-in/层级主管vs协作辩论/MCP三种传输模式/传输与协议分离/interrupt三件套关系/多Agent三种模式对比

## 课件知识点覆盖情况

| 章节 | 覆盖题目 |
|------|---------|
| 第1章 LangGraph入门 | C016-C020（State/Node/四步）, C030 |
| 第2章 状态管理 | **C045-C047**（MessagesState/追加vs覆盖/包列表）, C027（条件边） |
| 第3章 循环+HITL | **C051**（条件边循环）, **C056**（interrupt三件套）, **C058**（HITL原则）, C021（HITL） |
| 第4章 AutoGPT/BabyAGI | C031-C044（14题全覆盖） |
| 第5章 多Agent协作 | **C048-C050**（Fan-out/Fan-in/主管/辩论）, **C057**（三种模式对比） |
| 第6章 MCP协议 | **C052-C055**（C/S架构/三种传输/三步调用/FastMCP）, **C059**（传输与协议分离）, C029（MCP概念） |

## 学习效果评估

- **AutoGPT 循环**：75% → 85%（课件测验 12/14，概念对比清晰）
- **BabyAGI 机制**：新增 80%（reprioritize 动态重排理解到位）
- **题库系统**：80%（轻量索引模式理解，四文件分工清楚）

---

## 完整成果汇总（供压缩后恢复上下文）

### 一、题库轻量索引体系建设

**问题**：晨考从两个注入池各抽5题需读全文 ~1755行（knowledge-index 386行 + questions-gpt 1369行），浪费上下文。

**方案**：照搬 question-index → question-bank 的成功模式：

| 新文件 | 行数 | 用途 |
|------|------|------|
| `knowledge-index-light.md` | ~150行 | 注入池A：152题，ID+问题一句话 |
| `questions-gpt-light.md` | ~100行 | 注入池B：148题，ID+问题一句话 |

**效果**：晨考选号 2600行 → 300行，省 **~88%**。

**四文件分工速查**：
```
question-index.md（~50行）     → Bank核心题库目录
question-bank.md（~350行）     → Bank题库正文
knowledge-index-light.md（~150行）→ 注入池A目录
questions-gpt-light.md（~100行） → 注入池B目录
knowledge-index.md（~386行）   → 注入池A原文（按需grep）
questions-gpt.md（~1369行）    → 注入池B原文（按需grep）
```

### 二、题目入库

| 批次 | ID | 数量 | 来源 |
|------|-----|------|------|
| 课件测验 | C031-C044 | 14题 | AutoGPT/BabyAGI 选择/多选/判断/填空/简答 |
| HTML提取 | C045-C060 | 16题 | 模块三课件：MessagesState/Fan-out-Fan-in/多Agent/MCP |

**一天入库 30 题**，C 模块 30 → 60 题，六个章节全覆盖。

### 三、CLAUDE.md 更新

1. **晨考执行流程**：选号阶段读三个轻量索引（共~300行），按需grep取正文
2. **知识点沉淀规则**：晨考所有题的知识点（不论对错）→ session-notes
3. **学员手动入库指南**：
   - 自己踩的坑 → bank（核心题库）
   - 课件存货 → knowledge-index（备胎池A）
   - 面试标杆 → questions-gpt（备胎池B）
   - 理解总结 → session-notes

### 四、待办

- `chatpdf.py`：3个typo待修（similarty/similarty→similarity, temperture→temperature），api_key为空，交互层待补
- `handle_transform.py`：Transformer手搓停在QKV投影，下一步 `attn_scores = Q@K^T / sqrt(d_k)`
- `mutilauto.py`：多Agent协作，待看
- `pip install mcp`：PyPI超时，用清华源 `-i https://pypi.tuna.tsinghua.edu.cn/simple`
