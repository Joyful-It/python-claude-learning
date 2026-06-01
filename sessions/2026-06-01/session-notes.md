# 学习会话记录 - 2026-06-01

## 今日理解跃迁

> 从"tokenizer 和 model 随便配" → "tokenizer 词表和 model Embedding 层是配套训练的，分开了就是鸡同鸭讲，保存必须一起"

---

## 会话概览

- **日期**：2026-06-01
- **核心主题**：IMDB 情感分析项目收尾——代码改进 + 精度/指标概念深挖
- **代码文件**：`torch_pre/transform_all.py`

---

## 学员提出的问题（原文）

- "这个流程重要吗，我需要熟练记住吗"
- "fp16 是将内存变为原来的四分之一把"
- "fp32 是缩小多少，int8 是缩小多少"
- "fp8 是训练缩小四分之一 int32 是基准是吧，他们是怎么缩小的呢，原理是什么"
- "训练和推理，训练时反向传播，推理时前向传播吗，这两句在代码中，什么时候用"
- "为什么 tokenizer 也必须一起保存"
- "你怎么知道那个是预测值那个真实值，最后 f1 那个是什么语法"
- "意思是 logits 和 labels 是官方变量吗，eval_pred 我在上文都没找到"

---

## 概念与教学内容

### 1. 骨架要记，细节查文档

**核心结论**：不需要背每一行，要记的是六步骨架：
```
① 导库 → ② 加数据 → ③ tokenizer+model → ④ token化 → ⑤ DataCollator+TrainingArgs → ⑥ Trainer→train→save
```
参数值（learning_rate、batch_size）查文档就行。

---

### 2. FP32 / FP16 / INT8 精度对比

| 精度 | 位数 | 每参数占用 | 相对FP32 | 用途 |
|------|------|----------|---------|------|
| FP32 | 32位 | 4字节 | 基准 | 默认训练，最准确 |
| FP16 | 16位 | 2字节 | **一半** | 训练提速省显存 |
| INT8 | 8位 | 1字节 | **1/4** | 推理量化 |
| INT4 | 4位 | 0.5字节 | **1/8** | 超大模型加载 |

**口诀**：每少一半位数，显存砍一半。

**关键区别**：
- FP16 是**浮点数**，能表示小数，适合训练时梯度计算
- INT8/INT4 是**整数**，不能表示小数，梯度会变 0，**不能训练只能推理**

**代码里的位置**：
```python
# FP16 → 训练时用，写在 TrainingArguments 里
TrainingArguments(fp16=True)

# INT8 → 加载模型时用
AutoModel.from_pretrained(model_name, load_in_8bit=True)
```

---

### 3. 训练 vs 推理

| | 训练 | 推理 |
|--|------|------|
| 包含步骤 | 前向 + 反向 + 更新权重 | 只有前向 |
| 有梯度？ | ✅ | ❌ |
| 代码触发 | `trainer.train()` | `model.predict()` |

---

### 4. tokenizer 为什么必须和 model 一起保存

**核心**：model 的 Embedding 层输入是 token ID，tokenizer 的词表决定"哪个词→哪个 ID"。两者是配套训练的，词表换了 Embedding 就对不上，模型输出乱码。

**一句话**：tokenizer 是模型的翻译字典，字典必须跟模型配套。

---

### 5. compute_metrics 函数解析

```python
f1_metric = evaluate.load("f1")     # 加载评估器（只加载一次，放函数外）

def compute_metrics(eval_pred):
    # Trainer 自动传入 (模型输出, 真实标签) 元组，不需要自己定义 eval_pred
    logits, labels = eval_pred

    # logits → argmax → 预测类别（不是官方变量名，只是约定俗成）
    preds = np.argmax(logits, axis=-1)

    acc = (preds == labels).mean()

    # .compute() 返回字典 {"f1": 0.85}，["f1"] 是字典取值
    f1 = f1_metric.compute(predictions=preds, references=labels, average="binary")["f1"]

    return {"accuracy": acc, "f1": f1}
```

**eval_pred 从哪来**：Trainer 自动调用 compute_metrics，把 (模型输出, 真实标签) 打包塞进来，你的函数只是"等着被调用"。

**`logits` / `labels` 是官方名字吗**：不是，只是元组拆包时你起的名字，叫 `a, b` 也行，约定俗成用这两个词。

**`["f1"]` 是什么语法**：字典取值，跟 `d["key"]` 一样，`.compute()` 返回字典，取出数值。

---

## 今日代码改进（transform_all.py）

| 改进项 | 改前 | 改后 |
|--------|------|------|
| 评估指标 | 只有 accuracy（手算）| accuracy + F1（evaluate 库）|
| 显存优化 | 无 | `fp16=True` |
| 模型保存 | 只保存 model | model + tokenizer 一起保存 |
| Bug 修复 | `return {"f1": a.compute(logits, labels)}` | `return {"accuracy": acc, "f1": f1}` |

---

## 踩坑与纠正

| 错误 | 纠正 | 原因 |
|------|------|------|
| `fp16` 是缩小到 1/4 | ❌ 是缩小到 1/2 | FP32→FP16 是 32位→16位，减半不是减四分之三 |
| INT32 是基准 | ❌ 基准是 FP32 | INT32 是整数，FP32 是浮点数，训练用浮点 |
| 训练五步：forward→backward→loss→step→再次传播 | ❌ forward→loss→backward→step→zero_grad | loss 必须在 backward 之前（反向传播要对着 loss 求梯度），第五步是梯度清零不是再次传播 |
| `return {"f1": a}` | ❌ `a` 是评估器对象不是数值 | 需要调用 `.compute()` 才能得到 f1 分数 |
| 两个 return 语句 | ❌ Python 碰到第一个 return 就退出 | 两个指标放进同一个字典 return |

---

## 知识漏洞

- 训练循环五步顺序不稳定（第二次才答对）
- FP16/INT8 概念刚建立，需巩固

---

## 关键总结

**精度口诀**：
> FP16 是训练提速神器，INT8/INT4 是推理瘦身工具，不能混用。
> 每少一半位数，显存砍一半。

**训练循环五步口诀**：
> 前损后步清 → forward → loss → backward → step → zero_grad

**tokenizer 保存口诀**：
> tokenizer 是模型的翻译字典，分开了就是鸡同鸭讲，保存必须一起。

---

## 完成的练习

- `transform_all.py` 完成三处改进（fp16 / F1指标 / tokenizer保存）
- 修复 compute_metrics bug（两个 return → 一个 return）
- 全文加注释
- `review/fourthfuntion.py` 写出四种参数完整函数定义 + 函数体打印
- `review/xunhuan.py` 完成三道循环练习题（for遍历+条件 / while累加 / 猜数字）

---

## 学习效果评估

- 精度概念（FP32/FP16/INT8）：从混乱 → 有框架，掌握度约 50%
- tokenizer 必须配套保存：理解透彻
- 训练循环五步：第一次答错顺序，第二次答对，今日热身一遍过 ✅
- compute_metrics 结构：理解了 eval_pred 来源、字典取值语法

---

## 第二段：函数四种参数（A.1）

### 四种参数对照表

| 参数类型 | 语法 | 打包成 | 特点 |
|---------|------|-------|------|
| 位置参数 | `a` | - | 必传，顺序对应 |
| 默认参数 | `b=10` | - | 可不传，有默认值 |
| 可变位置参数 | `*args` | tuple | 任意个位置参数 |
| 可变关键字参数 | `**kwargs` | dict | 任意个关键字参数 |

**强制顺序**：位置 → 默认 → `*args` → `**kwargs`，**kwargs 永远压底

**命名规则**：`*` 和 `**` 是语法，`args`/`kwargs` 只是约定，可以换名字

### 今日独立写出的代码

```python
def order_food(table_number, discount=1.0, *food_number, **tips):
    pass
```

### 踩坑提醒

- `print("a=", a)` 和 `print(f"a={a}")` 的区别：前者等号后有空格（逗号自动加），f-string 无多余空格
- `*args` 之后的参数变成关键字专用参数（keyword-only），调用时必须写参数名
- `**kwargs` 后面不能再有任何参数，否则 SyntaxError

---

## 第三段：循环结构（A.1）

### Python for vs C for 区别

| C 风格 | Python |
|--------|--------|
| `for(i=0; i<10; i++)` 三段式 | `for i in range(10)` 从可迭代对象逐个取 |
| 手动控制起始/条件/步长 | `range(n)` 左闭右开，不含 n |

### while 要点

- `while 条件` 为假时一次都不执行
- 循环体内必须修改条件变量，否则死循环
- `break` 强制退出

### 今日三道练习（xunhuan.py）

```python
# 1. for + if —— 遍历筛选
scores = [85, 92, 78, 60, 55]
for i in scores:
    if i > 60:
        print(f'大于60的值:{i}')

# 2. while 累加
a = 0; b = 1
while b <= 100:
    a = a + b
    b += 1
print(a)   # 5050

# 3. 猜数字（while True + break）
answer = 7
while True:
    a = int(input())
    if a > answer:
        print('da')
    elif a < answer:
        print('xiao')
    else:
        print('dui')
        break
```

### 踩坑

- `input()` 必须放 while 循环**里面**，否则只输入一次变成死循环
- 猜对后必须 `break`，否则永远退不出来

---

## 今日学习效果总评

| 考点 | 前值 | 后值 | 备注 |
|------|------|------|------|
| 函数四种参数 | 25% | **70%** | 四种名称+顺序+独立写出+keyword-only |
| 循环结构 | 10% | **50%** | for/while基础+三道题全过 |
| 训练循环五步 | 65% | **75%** | 热身一遍过，顺序稳定 |
| 函数返回值 | 0% | **50%** | print vs return 彻底区分，默认返回 None，return 是函数终止点 |
| 变量作用域 | 0% | **45%** | 局部变量隔离 + global 打破隔离 |
