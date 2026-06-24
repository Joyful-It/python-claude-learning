# 2026-06-24 会话笔记

## 今日理解跃迁

从"知道量化和KV Cache是什么" → "能写出完整的显存估算公式，讲清推理两阶段(Prefill/Decode)和显卡三大指标(容量/算力/带宽)的对应关系"

## 会话概览

- **日期**：2026-06-24
- **核心主题**：大模型部署与训练速查——学员独立总结
- **产出**：一份速查笔记，覆盖 Transformer推理/QKV/KV Cache/量化/显存估算/LoRA/显卡选型

## 学员总结正文（原稿保留）

### Transformer推理流程
```
输入 → Tokenization → Embedding → Transformer Block×N(Attention+FFN) → LM Head → 输出下一个Token
```

### QKV核心
- Q = 我要找什么信息
- K = 我有什么信息
- V = 我的实际内容
- 公式：Attention(Q,K,V) = Softmax(QKᵀ)V
- 作用：融合上下文信息

### 推理两个阶段

| 阶段 | 做什么 | 特点 |
|------|--------|------|
| **Prefill** | 一次性计算全部Token的QKV，建立KV Cache | 计算密集型，看GPU算力(Tensor Core) |
| **Decode** | 逐Token生成，只算新Token的Q，读历史KV Cache | 带宽密集型，看显存带宽 |

### KV Cache
- 缓存：所有历史Token的K和V
- 目的：避免重复计算Attention
- 公式：`KV Cache = 2 × Layers × SeqLen × HiddenSize × Bytes`
- 与层数/隐藏维度/上下文长度相关，与模型参数量不直接相关
- 长上下文吃显存：KV Cache ∝ SeqLen，上下文翻倍→KV Cache翻倍

### 量化
- 目的：降低显存占用

| 精度 | 每参数 |
|------|--------|
| FP32 | 4字节 |
| FP16/BF16 | 2字节 |
| FP8 | 1字节 |
| INT8 | 1字节 |
| INT4 | 0.5字节 |

经验公式：
- FP16: 1B ≈ 2GB
- INT8: 1B ≈ 1GB
- INT4: 1B ≈ 0.5GB

FP8 vs INT8：
- FP8：省显存 + 支持Tensor Core加速，生产部署主流
- INT8：省显存，加速能力较弱

### 部署显存估算

**推理显存 = 模型权重 + KV Cache + 少量开销**
- 显存利用率控制在80%左右

**训练显存（全参数微调）= FP16权重 × 6~8**
- 例：7B → 14GB × 6~8 ≈ 84~112GB

| 方式 | 经验公式 |
|------|---------|
| LoRA | 推理显存 × 1.5 |
| QLoRA | INT4推理显存 × 2 |

### 显卡判断三步
```
① 模型大小 = 参数量 × 精度
② 加余量 ×1.2~1.5（给KV Cache/框架/系统）
③ 比较显存
```
例：32B INT4 = 32×0.5=16GB，加余量≈20GB，24GB显卡可部署

### 训练卡 vs 推理卡

| | 推理卡(4090/5090) | 训练卡(A100/H100/H200) |
|------|------|------|
| 特点 | 算力强/价格低/显存较小 | 显存大/带宽高/NVLink/ECC |
| 适合 | 部署/Agent开发/LoRA/QLoRA | 全参训练/企业推理/高并发 |

### 显卡三大指标（口诀）
- **容量** → 能跑多大模型
- **算力** → 训练多快
- **带宽** → 生成多快

### LoRA/量化/蒸馏/剪枝 一句话区别

| 技术 | 作用 | 本质 |
|------|------|------|
| LoRA | 降低训练成本 | 冻结原模型，训练少量Adapter |
| 量化 | 降低部署成本 | 降低权重精度 |
| 剪枝 | 减少参数数量 | 删除不重要参数 |
| 蒸馏 | 让小模型学大模型 | 知识迁移 |

### QLoRA = Quantization + LoRA
```
FP16模型 → INT4量化加载 → 冻结权重 → LoRA训练
目的：进一步降低训练显存
```

### 面试核心公式速查

| 项目 | 公式 |
|------|------|
| FP16权重 | 1B ≈ 2GB |
| INT8权重 | 1B ≈ 1GB |
| INT4权重 | 1B ≈ 0.5GB |
| 推理显存 | 模型权重 + KV Cache |
| KV Cache | 2 × Layers × SeqLen × HiddenSize × Bytes |
| 全参训练 | FP16权重 × 6~8 |
| LoRA | 推理显存 × 1.5 |
| QLoRA | INT4推理显存 × 2 |

### 下一步学习方向（学员标注）
多头注意力(MHA/GQA)、PagedAttention、vLLM、张量并行(TP)、数据并行(DP)、ZeRO

## 学习效果评估

- **量化/显存估算**：从概念→能写出完整公式，实用级掌握
- **KV Cache**：昨天自己推导含义，今天能写出公式和OOM关系——两天贯通
- **显卡选型**：训练卡 vs 推理卡，三大指标口诀清晰
- **下一阶段**：从"会用模型"走向"能部署生产系统"

---

## 补充：推理优化 + 训练并行（学员独立总结 第二部分）

### 十三、MHA（多头注意力）
- 作用：让模型从多个角度理解上下文
- 结构：Token → 32个Attention Head → 拼接 → 输出
- 每个Head维度 = HiddenSize ÷ Head数（如 4096÷32=128）
- 特点：效果好，但 KV Cache 较大

### 十四、GQA（分组查询注意力）
- 传统MHA：32 Q Head + 32 K Head + 32 V Head
- GQA：32 Q Head + 8 K Head + 8 V Head（多个Q共享KV）
- 效果：KV Cache减少、推理更快、显存更省
- 主流模型：Llama3、Qwen2.5、DeepSeek、Gemma

### 十五、PagedAttention
- 核心：KV Cache 分页管理（= KV Cache版虚拟内存）
- 传统问题：连续存储→显存碎片、利用率低
- 解决：切成 Page→通过页表记录→减少碎片、提高并发

### 十六、vLLM
- 定位：高性能LLM推理框架
- 核心技术：PagedAttention + Continuous Batching（请求结束立即补新请求）
- 企业常用：vLLM / TensorRT-LLM / SGLang

### 十七、DP（数据并行）
- 思路：复制多份模型，不同GPU训练不同数据
- 特点：简单、但显存占用大（每张卡都装完整模型）

### 十八、TP（张量并行）
- 思路：拆模型权重分到不同GPU
- 例：Linear(10000×10000) → GPU1(5000×10000) + GPU2(5000×10000)
- 解决单卡放不下，但通信开销大

### 十九、ZeRO（零冗余优化器）—— 减少训练显存

| 级别 | 拆分内容 | 记忆 |
|------|---------|------|
| ZeRO-1 | Optimizer State | P完整 G完整 O拆分 |
| ZeRO-2 | Optimizer + Gradient | P完整 G拆分 O拆分 |
| ZeRO-3 | Parameter + Gradient + Optimizer | P拆分 G拆分 O拆分（最强）|

### 知识图谱总览
```
推理优化：MHA → GQA(省KV Cache) → PagedAttention(分页) → vLLM(框架)
训练优化：DP(拆数据) → TP(拆模型) → ZeRO(1拆O/2拆O+G/3拆O+G+P)
```

### 高频面试一句话版
- MHA：标准多头注意力
- GQA：多Q共享KV，减少KV Cache
- PagedAttention：分页管理KV Cache
- vLLM：高性能推理框架，PagedAttention+Continuous Batching
- DP：复制模型拆数据
- TP：拆模型分权重
- ZeRO-1/2/3：依次拆优化器/梯度/参数
