# 学习会话记录 - 2026-05-26

## 今日内容

> 上午：每日晨考——HuggingFace 生态七问
> 下午：知识蒸馏 + GELU vs ReLU + 学习率预热
> 晚间：DL全链复习（张量→梯度→ML/DL→CNN/RNN/LSTM/Transformer）+ IMDB情感分析项目拆解

---

## 🔆 每日晨考（独立板块）

### Q1：Tokenizer 三个参数——return_tensors / truncation / padding

| 参数 | 作用 | 为什么需要 |
|------|------|-----------|
| `return_tensors="pt"` | 返回 PyTorch Tensor | 数据直接喂模型，`"tf"` 返回 TensorFlow 格式 |
| `truncation=True` | 超长截断 | Token 数 > 模型上限(如 512) → 切掉尾部 → 防 OOM |
| `padding=True` | 对齐填充 | batch 内句子长短不一 → 短的补 `[PAD]` → 矩阵对齐 |

---

### Q2：Tokenizer 处理四步 + 输出三个字段

#### 处理流程

```
① 标准化       去空格、大小写统一、Unicode 规范化
② 预分词       "Hello World" → ["Hello", "World"]
③ 模型分词     WordPiece/BPE 切子词 → 映射 Token ID → [7592, 2088]
④ 后处理       加特殊标记 [CLS]... [SEP] → [101, 7592, 2088, 102]
               然后做 padding / truncation
```

#### 输出字典

| 字段 | 含义 | 作用 |
|------|------|------|
| `input_ids` | Token ID 序列 | 模型真正读的数字 |
| `attention_mask` | 1=有效文本, 0=`[PAD]` | 自注意力忽略填充位 |
| `token_type_ids` | 0=第一句, 1=第二句 | 句对任务(问答/NLI)区分两句 |

---

### Q3：Pipeline 三阶段 + 4 个任务名

#### 三阶段自动衔接

```
原始文本 → [① Tokenizer(文本→ID)] → [② Model(前向推理)] → [③ Postprocess(ID→标签/文字)] → 结果
```

#### 4 个标准任务名（精确到字符串）

```
'sentiment-analysis'     → 情感分析
'ner'                    → 命名实体识别（配合 aggregation_strategy="simple"）
'question-answering'     → 问答任务
'text-generation'        → 文本生成（内部调 .generate()）
```

---

### Q4：HuggingFace 五大核心组件

| 组件 | 一句话 | 核心 API |
|------|-------|---------|
| **Transformers** | 核心模型库，数万预训练模型 | `AutoTokenizer` / `AutoModel` / `Trainer` |
| **Datasets** | 数据集一键加载，流式处理 | `load_dataset()` |
| **Evaluate** | 标准评测指标 | Accuracy / BLEU / F1 / ROUGE |
| **Accelerate** | 分布式加速，少改代码多卡跑 | DDP / 混合精度 / TPU |
| **Hub** | AI 界 GitHub，托管模型+数据 | `huggingface.co` |

---

### Q5：词嵌入 + 序列建模 演进方向

#### 词嵌入：从静态到动态

```
Word2Vec/GloVe（静态）
  → 一词一向量，"苹果"不管在水果还是手机句子里向量一样
  → 无法解决一词多义

ELMo/BERT（动态）
  → 同一词在不同上下文里向量不同
  → "吃苹果" vs "买苹果手机" → 两个不同的"苹果"向量
```

#### 序列建模：从不看全局到全局直连

```
RNN → LSTM → Seq2Seq(编码器-解码器) → 注意力 → Transformer

方向：
  信息流动更精细、记忆访问更灵活
  彻底丢弃 RNN 串行 + 长程遗忘的包袱
```

---

### Q6：注意力机制本质 + 解决什么问题

#### 本质

```
一种动态信息筛选机制——不是你给我的我都看，是我挑着看。

Q（查询）：我想要什么信息？        ← "翻译当前这个词需要什么上下文？"
K（键）：  每个位置有什么信息？    ← "我这个位置的含义是什么？"
V（值）：  每个位置的实际内容      ← "我具体是什么？"

Attention = softmax(QK^T / √d_k) @ V
             ↑ 算相关性       ↑ 挑着取
```

#### 解决的问题

| 问题 | 怎么解决的 |
|------|----------|
| RNN 长程梯度消失/爆炸 | 每两个位置直接算相似度，不经过时间步 |
| Seq2Seq 信息瓶颈（长句全挤进一个向量） | 解码器每步直接看编码器所有位置 |

---

### Q7：Transformer 三大核心优势

| # | 优势 | 本质 |
|---|------|------|
| ① | **完全并行** | 所有 Token 同时矩阵运算，不串行，GPU 利用率拉满 |
| ② | **任意距离直连** | 自注意力一步到位，两个位置不管隔多远直接通信 |
| ③ | **无与伦比的扩展性** | 不仅是 LLM 底座，已跨界到 ViT(视觉)、Whisper(语音)、CLIP(多模态) |

---

## 今日理解跃迁

> 从"HuggingFace 就是装模型的"→"HF 是一整套生态：Transformers(模型)+Datasets(数据)+Evaluate(评估)+Accelerate(加速)+Hub(社区)，五个组件各管一摊"

---

## 易混淆点纠偏

| 易混 | 区分 |
|------|------|
| `truncation` vs `padding` | truncation=切长的（超 max_length），padding=补短的（batch 内对齐）|
| `attention_mask` vs `token_type_ids` | mask=区分真假文本(防看[PAD])，type=区分句A句B(句对任务) |
| 静态词嵌入 vs 动态词嵌入 | 静态=一词一向量(Word2Vec)，动态=看上下文变(BERT) |
| Q/K/V 三个角色 | Q=我要啥，K=你有啥标签，V=你的实际内容 |

---

## 晨考速记卡

| 题 | 两秒回答 |
|----|---------|
| return_tensors="pt"？ | 返回 PyTorch Tensor |
| truncation？ | 超长切尾 |
| padding？ | 短的补 [PAD] 对齐 |
| Tokenizer 输出？ | input_ids + attention_mask + token_type_ids |
| Pipeline 四任务？ | sentiment / ner / qa / text-generation |
| HF 五组件？ | Transformers / Datasets / Evaluate / Accelerate / Hub |
| 词嵌入怎么演进？ | 静态→动态，一词一义→上下文决定 |
| 序列建模怎么演进？ | RNN→LSTM→Seq2Seq→Attention→Transformer |
| 注意力本质？ | Q查K挑出V，动态筛选 |
| Transformer 三优势？ | 并行 / 长程直连 / 跨界扩展 |

---

## 补充内容

> 下午内容：知识蒸馏、GELU vs ReLU、学习率预热

---

## 今日理解跃迁（下午新增）

> 从"大模型变小模型就是缩小参数" → "知识蒸馏是让大模型当老师，把软标签（灰度信息）+ 温度 T 软化输出一起教给学生，靠双损失函数平衡学老师和学标准答案"

---

## 知识蒸馏（Knowledge Distillation）

### 为什么需要？

大模型跑不动（慢/显存大/成本高）→ 需要小模型接近大模型效果

### 核心框架：老师-学生

```
冻结的大模型(老师) → 输出"软标签" [0.85, 0.10, 0.05]
                                         ↓
正在训练的小模型(学生) → 同时学：
                          ① 老师的软标签（蒸馏损失, KL散度）
                          ② 标准答案硬标签（学生损失, 交叉熵）
```

### 软标签 vs 硬标签

```
硬标签：[1, 0, 0]           ← 非黑即白，"猫"
软标签：[0.85, 0.10, 0.05]  ← 灰度信息，"猫，但有点像狗和老虎"

软标签的价值：
  学生学到了"猫和狗有点像，和老虎也有点像"
  这是硬标签永远教不会的！
```

### 温度 T（Temperature）

```
softmax(logits / T)

T=1（常温）：  [0.85, 0.10, 0.05]      ← 正常
T=5（升温）：  [0.40, 0.35, 0.25]      ← 次要类别更明显
T=20（高温）： [0.21, 0.20, 0.19, ...] ← 暴露更多隐藏信息

为什么需要 T？
  大模型太自信（猫=0.9999），不加温度软标签和硬标签没区别
  升温后大模型"不确定"的样子被放大，学生学到更多
```

### 双损失函数

```
总损失 = α × 蒸馏损失  +  (1-α) × 学生损失

① 蒸馏损失：学生(logits/T) vs 老师(logits/T)，KL散度
   → 学老师的"思维方式"
   乘以 T² 补偿梯度缩放

② 学生损失：学生(logits) vs 真实标签，交叉熵
   → 学标准答案，别跑偏

α：平衡系数，通常 0.7~0.9（更信老师）
```

### 同学说的复盘

| 同学说的 | 判断 | 真相 |
|---------|------|------|
| "大模型是老师，小模型是学生" | ✅ 正确 | 标准框架 |
| "双损失函数" | ✅ 也对 | 蒸馏损失 + 学生损失 |
| 漏掉的 | ❓ | 软标签的灰度信息、温度 T 的作用、为什么软标签有价值 |

---

## 学习率（lr）+ 预热（Warmup）

### 学习率本质

```
w_new = w_old - lr × 梯度
                 ↑
             步伐大小

太大(0.1)：步子太飘，反复横跳，不收敛
太小(1e-7)：学到死都没变化，陷入局部最优
2e-5：微调黄金值（BERT/GPT 经典）
```

### 预热原因

```
刚开局模型面对新数据是懵的 → 上来就满额 lr → 被奇葩初始样本带偏 → 崩

预热：前 N% 步 lr 从 0 线性爬坡到目标值
      → 先热热身，状态稳了再高强度学
```

### 学习率曲线

```
lr
 ↑        ╱‾‾‾‾‾‾‾‾‾‾‾‾‾╲
 │      ╱                  ╲
 │    ╱                      ╲_________
 │  ╱                                    →
 └────────────────────────────────────→ 步数
     ↑ 预热期    ↑ 峰值维持    ↑ 衰减期
```

### 梯度爆炸 vs 学习率过大（不是同一个东西！）

| | 梯度爆炸 | 学习率过大 |
|------|---------|----------|
| 本质 | **梯度本身算出来就很大**（backward 已错） | 梯度和正常，**lr 把步伐放大过头** |
| 元凶 | 链式连乘，雅可比特征值>1 | 人为设太大 |
| 解法 | `clip_grad_norm_` 梯度裁剪 | 调小 lr，或用预热避开 |
| 症状 | loss 直接 NaN | loss 震荡，但不会直接 NaN |

> 同公式 w-lr×g 的两个因子出问题，不同根因。

---

## GELU vs ReLU

### 公式

```
ReLU(x) = max(0, x)        一刀切，负数全杀
GELU(x) = x × Φ(x)         负数按概率"软"处理，处处光滑
```

### 值对比

```
x:       -2    -1     0     1     2
ReLU:     0     0     0     1     2     ← 零点是硬断的
GELU:   -0.05 -0.16  0    0.84  1.95    ← 零点是平滑过渡的
```

### 核心区别

| | ReLU | GELU |
|------|------|------|
| 负数处理 | 直接清零 | 按概率留一点负值 |
| 零点 | 硬断，不可导 | 平滑，处处可导 |
| 谁在用 | CNN / MLP | **Transformer / BERT / GPT** |
| 一句话 | "不是正数就闭嘴" | "不太确定就小声说" |

### 为什么 Transformer 用 GELU？

深层网络（上百层）梯度需要平缓传递。ReLU 在零点砍死一半神经元 → 信息截断累积。GELU 光滑 → 梯度传得稳。

⚠️ **原论文用的是 ReLU！** BERT/GPT 后续改进才换成 GELU。论文原版 ≠ 工业落地版。

---

## 间隔复习 — Tokenizer 四步纠正

| 学员回答 | 正确 | 错在哪 |
|---------|------|-------|
| "将文字处理" | ① 标准化 | ✅ 对 |
| "切成短语" | ② 预分词 | ✅ 对 |
| "切为词语" | ③ 模型分词 | ⚠️ 是**子词**不是词语，BPE 拆更细 |
| "最后输出" | ④ 后处理 | ❌ 漏了关键一步：加 [CLS]/[SEP]、padding/truncation |

**记忆口诀**：标→预→模→后（标准化→预分词→模型拆子词→后处理加壳）

---

## 今日速记卡（新增）

| 题 | 两秒回答 |
|----|---------|
| 知识蒸馏本质？ | 大模型(老师)→软标签→教小模型(学生) |
| 软标签好处？ | 灰度信息，"猫有点像狗"，硬标签教不会 |
| 温度 T 干啥？ | 升温→次要类别更明显→学生学更多 |
| 双损失哪两个？ | 蒸馏损失(KL,学老师) + 学生损失(交叉熵,学标准答案) |
| 预热为什么？ | 开局懵圈，先慢走防崩 |
| lr 爆炸 vs 梯度爆炸？ | 梯度爆炸=方向信号疯了，lr 爆炸=把正常信号放大过头 |
| GELU vs ReLU 一句话？ | ReLU=不是正数闭嘴，GELU=不确定小声说 |
| 原 Transformer 用哪个？ | **ReLU**，GELU 是 BERT 后改的 |

---

# 晚间：DL全链大复习

> 从张量到 Transformer，一条线串通，纠偏 7 个理解误区

---

## 今日理解跃迁（晚间新增）

> 从"各模型互不相关" → "CNN/RNN/Transformer 本质都是在'换连法'：全连接是全连，CNN是只连邻居，RNN是连自己上一刻，Transformer是直接全局注意力——全是wx+b的变体"

---

## ① 张量（Tensor）

```
标量 → 向量 → 矩阵 → 张量（三维及以上）

PyTorch 里一切皆 tensor：输入、权重 W、梯度、输出
tensor vs numpy：结构一样，但 tensor 能上 GPU + 自动求梯度

标量输入会报错吗？不会，PyTorch 自动转：
  torch.tensor(3.14)        → tensor(3.14)
  torch.tensor([1,2,3])     → tensor([1,2,3])
  torch.tensor([[1,2],[3,4]]) → tensor(2×4)
```

---

## ② 梯度（Gradient）

```
梯度 = 偏导数向量 = "最陡上坡方向"
你要的是下坡 → w_new = w_old - lr × 梯度

loss = (w - 3)²：
        loss ↑
            │    ·
            │   · ·        w=3 坑底，loss=0
            │  ·   ·
            │ ·     ·
            │·       ·
            └─────────→ w
            1  2  3  4  5

w=5（在坑底右边）：梯度 = +4（正）→ 往右 loss 更大 → 要往左，w 减小
w=1（在坑底左边）：梯度 = -4（负）→ 往右 loss 变小 → 要往右，w 增大

口诀：正梯度 → 退回来（w减），负梯度 → 继续走（w增）
```

---

## ③ 机器学习 vs 深度学习——不只是多几层！

| | 机器学习 | 深度学习 |
|------|------|------|
| 特征 | **人手工设计** | **网络自动学** |
| 代表 | XGBoost/SVM/逻辑回归 | CNN/RNN/Transformer |
| 数据量 | 小样本也好使 | 越多越好 |
| 可解释 | 好 | 黑箱 |

**核心区别不是层数，是谁来设计特征。**
**不是说"ML有标签 DL没标签"——两者都有监督学习，也都支持无监督。**

```
特征自动学 ≠ 不需要标签
  → 标签照样给，但"用哪些特征"网络自己决定
```

---

## ④ 深度学习层怎么连？

```
所有层统一公式：output = 激活( input × W + b )

层1 → 层2：h = ReLU(X @ W₁ + b₁)    输入3维 → 隐藏4维
层2 → 输出：ŷ = sigmoid(h @ W₂ + b₂)  隐藏4维 → 输出1维

前一层的输出 = 后一层的输入，W 矩阵决定"谁连谁、权重多少"
每层激活函数相同但 W 不同 → 学的东西不同

⚠️ 有些神经元到结束也学不到东西：
  "Dying ReLU"——输出永远 ≤ 0 → ReLU永远=0 → 梯度=0 → 永远不更新
  GELU 部分缓解（负数不直接杀）
```

---

## ⑤ CNN——卷积神经网络

### 解决什么？
全连接处理图像：224×224×3 → 1500万参数 → 爆炸
CNN：3×3 卷积核全图滑，共享参数 → 9 个参数搞定

### 卷积怎么乘？
```
图：        卷积核3×3：  一步一步滑：
1 2 3 4    ┌──┬──┬──┐
5 6 7 8    │+1│-1│ 0│   第1步盖(1,2,3,5,6,7,9,10,11) → 对应乘求和
9 0 1 2    ├──┼──┼──┤   第2步盖(2,3,4,6,7,8,0,1,2)   → 同上
3 4 5 6    │ 0│+1│-1│   ...
           ├──┼──┼──┤
           │+1│ 0│-1│   每步：对应位置相乘，全部求和 → 一个数
           └──┴──┴──┘
```

### 创新点
| 创新 | 做法 | 效果 |
|------|------|------|
| 局部连接 | 每个神经元只看 3×3 | 参数暴减 |
| 参数共享 | 同kernel全图滑 | 学一次到处用 |
| 层级抽象 | 浅→边缘，中→部件，深→完整物体 | 自动分层理解 |

### 缺点
不看全局，位置敏感（平移/旋转），不适合序列

---

## ⑥ RNN——循环神经网络

### 解决什么？
全连接/CNN 处理序列：顺序信息丢了，"我爱你"和"你爱我"一样
RNN：h_t = tanh(x_t @ W_x + h_{t-1} @ W_h + b)
     比全连接多了一项"上一刻的自己"

### 创新点
| 创新 | 做法 |
|------|------|
| 时间记忆 | 每步输出喂回下一步 |
| 参数跨时刻共享 | 同一套 W_h 用所有时刻 |
| 变长序列 | 不限输入长度 |

### 缺点
串行不能并行（慢）、梯度消失/爆炸（W_h 反复乘自己）、长程依赖差

---

## ⑦ LSTM——长短期记忆

### RNN 升级版：三门 + 长期记忆 C_t

```
遗忘门：f_t = sigmoid(x@W_f + h@U_f)   "旧的哪些该忘？"
输入门：i_t = sigmoid(x@W_i + h@U_i)    "新的哪些该记？"
候选值：~C_t = tanh(x@W_c + h@U_c)     "新信息是什么？"
输出门：o_t = sigmoid(x@W_o + h@U_o)    "该输出什么？"

C_t = f_t × C_{t-1} + i_t × ~C_t    ← 加法！梯度 ∂C_t/∂C_{t-1}=f_t 直传
h_t = o_t × tanh(C_t)
```

### C_t 为什么用加法？防梯度消失（不是防爆炸）

```
如果纯乘法：C_t = C_{t-1} × 某数 → 100 步连乘 → 0 或 ∞
加法：C_t = f×C_{t-1} + 新内容 → ∂C_t/∂C_{t-1} = f_t，门控独立控制
  
f_t 可以接近 1（全记住）→ 梯度几乎无损穿过 → 不消失

⚠️ 但如果 f_t 一直 ≈ 0.01（全忘），梯度一样消失！
  加法只是给了一个可能性，不保证
```

### 缺点
还是串行、参数多（RNN×4）、极端长程仍吃力

---

## ⑧ Transformer——终极进化

### 扔掉循环？扔的是"串行依赖"，不是前向/反向传播！

```
RNN（串行）：          Transformer（并行）：
  "我" → h₁              "我" ─┐
    ↓                      "爱" ─┼─ 同时算，互相看
  "爱" → h₂              "你" ─┘
    ↓                   
  "你" → h₃            所有词同时扔进 QKV → 1 步全算完

前向/反向传播照样有，扔掉的是"必须等上一步"
```

### 核心机制

```
自注意力 = softmax(Q @ K^T / √d_k) @ V
Q=我要啥  K=你有啥标签  V=实际内容
每两个词直接算相似度 → 全局关系一步到位
```

### 创新点
| 创新 | 效果 |
|------|------|
| 完全并行 | GPU 利用率拉满 |
| 任意距离直连 | 长程依赖零损耗 |
| 位置编码 | 不用循环也知道顺序 |
| 多头注意力 | 语法/语义/指代各看各的 |

### 缺点
O(n²) 复杂度、没有内建序列归纳偏置、参数量巨大

---

## 全景串联图

```
              全连接 wx+b（所有DL的基础）
                     │
    ┌────────────────┼────────────────┐
    ↓                ↓                ↓
  CNN              RNN           Transformer
空间模式专家    时间序列专家      注意力万能王
    │                │                │
卷积替代全连接  h_{t-1}@W_h      QKV全场直连
参数共享消参   加入时间记忆      扔循环换并行
    │                │                │
 缺点：          缺点：          缺点：
只看局部       串行+梯度消失     O(n²)贵
    │                │
    └────────┬───────┘
             ↓
          LSTM
    三门控+C_t加法
    缓解RNN长程问题
    但还是串行
```

---

## 错题本 — 7 个纠偏

| 误解 | 纠正 |
|------|------|
| "DL就是多几层" | 区别在特征谁设计，不是层数 |
| "DL不提供标签" | 监督学习照样给标签，特征自动学≠不要标签 |
| "全连接每层一样" | 结构一样但 W不同，学的东西不同 |
| "Transformer扔掉了前向/反向传播" | 扔掉的是串行依赖，前向/反向照样有 |
| "C_t加法防爆炸" | 主要防消失，防爆炸靠梯度裁剪+门控 |
| "RNN参数每步不同" | 同一套 W_h 跨时刻共享 |
| "Dying ReLU不会发生" | 负数区 ReLU 永远 0 → 神经元"死"了 |

---

## 速记口诀

```
张量→一切数据，梯度→指南针
ML靠人挑特征，DL靠网自己学
全连接全连，CNN只连邻居，RNN连自己，Transformer全看
CNN三宝：局部+共享+层级
RNN三缺：慢+消+忘
LSTM三救：门+加法+分通道
Transformer三绝：并行+长程+多头
```

---

# 晚间二：IMDB 情感分析项目拆解

> 从"大框架对但漏步骤"到"10 步精准确认"

## 完整流程（10 步）

| 步 | 做什么 | 关键代码 | 常见坑 |
|----|-------|---------|--------|
| ① | 导入库 | `transformers` / `datasets` / `evaluate` | evaluate 容易忘 |
| ② | 加载数据 | `load_dataset("stanfordnlp/imdb")` | 数据集名字要写对 |
| ③ | 加载模型+分词器 | `AutoModelForSequenceClassification` + `AutoTokenizer` | **不是参数，是模型本身** |
| ④ | token化 | `dataset.map(tokenizer, batched=True)` | `batched=True` 加速 |
| ⑤ | 数据对齐器 | `DataCollatorWithPadding(tokenizer)` | 动态 batch padding |
| ⑥ | 训练参数 | `TrainingArguments(...)` | 参数太多别硬背 |
| ⑦ | 评测指标 | `evaluate.load("accuracy")` + `compute_metrics` 函数 | logits要 argmax |
| ⑧ | Trainer 组装 | `Trainer(model, args, dataset, collator, metrics)` | 五件套 |
| ⑨ | 训练 | `trainer.train()` | — |
| ⑩ | 保存 | `trainer.save_model()` + `tokenizer.save_pretrained()` | 两个都要存 |

## 代码记不住怎么办？三招

```
第一层（必须背，5个导入）：
  from transformers import AutoTokenizer, AutoModelForSequenceClassification,
                            Trainer, TrainingArguments, DataCollatorWithPadding
  import evaluate
  
第二层（理解原理，查文档）：
  tokenizer 参数(truncation/max_length/padding)、TrainingArguments 参数
  知道有这个功能就行，忘了查

第三层（复制粘贴，项目通用）：
  compute_metrics 函数逻辑
  trainer.train() / evaluate() / save_model() 三板斧用三次就熟了
```

## 骨架 6 步速写

```python
# 1. 数据
dataset = load_dataset("xxx")

# 2. 模型+分词器
tokenizer = AutoTokenizer.from_pretrained("xxx")
model = AutoModelForSequenceClassification.from_pretrained("xxx", num_labels=2)

# 3. token化 + DataCollator
dataset = dataset.map(lambda e: tokenizer(e['text'], truncation=True, max_length=512), batched=True)
collator = DataCollatorWithPadding(tokenizer)

# 4. 训练参数
args = TrainingArguments(output_dir="./out", num_train_epochs=3,
                         per_device_train_batch_size=16,
                         evaluation_strategy="epoch", save_strategy="epoch",
                         load_best_model_at_end=True,
                         metric_for_best_model="accuracy")

# 5. 评测指标
acc = evaluate.load("accuracy")
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    return acc.compute(predictions=logits.argmax(-1), references=labels)

# 6. 训练+保存
trainer = Trainer(model=model, args=args, train_dataset=dataset["train"],
                  eval_dataset=dataset["test"], data_collator=collator,
                  compute_metrics=compute_metrics)
trainer.train()
trainer.save_model("./saved_model")
```

---

## 晚间速记卡

| 题 | 两秒回答 |
|----|---------|
| 张量是什么？ | 多维数据容器，PyTorch 一切皆 tensor |
| 梯度是什么？ | 最陡上坡方向，负梯度=下坡 |
| ML vs DL 核心区别？ | ML 人挑特征，DL 网自己学 |
| 层怎么连？ | 前层输出=后层输入，靠 W 矩阵 |
| CNN 怎么替全连接？ | 3×3 核全图滑，参数共享 |
| RNN 比全连接多什么？ | h_{t-1}@W_h，上一刻的自己 |
| LSTM C_t 为什么加法？ | 防消失，∂C_t/∂C_{t-1}=f_t 直传 |
| Transformer 扔的是什么？ | 串行依赖，不是前向/反向传播 |
| IMDB 项目 10 步？ | 导入→数据→模型+分词→token化→对齐→参数→指标→组装→训练→保存 |
