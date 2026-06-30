# 2026-06-26 会话笔记

## 今日理解跃迁

从"知道 LoRA/QLoRA 省显存"→ "能根据 24GB 单卡算 Qwen3.6-27B 显存，给出唯一可行方案 QLoRA"

## 会话概览

- **日期**：2026-06-26
- **核心主题**：模块三高效微调——LLaMA Factory/Unsloth/DeepSpeed ZeRO/QLoRA 实操
- **形式**：教师晨考 15 题

## 教师晨考 15 题

### 一、单选/多选（12题）

**Q1** LLaMA Factory 和 Unsloth 的共同底层依赖？ → B：HuggingFace PEFT 库

**Q2** LLaMA Factory 相比 Unsloth 的优势？ → B：多卡/多硬件/WebUI

**Q3** Unsloth 相比 LLaMA Factory 的优势？ → B：手写算子优化，2x速度省50%显存

**Q4** ZeRO-1 切分什么？ → B：只切分优化器状态（O）

**Q5** 单卡放得下模型时，多卡优先选什么？[多选] → C：DDP(ZeRO-0)，无需跨卡通讯

**Q6** Unsloth 加载模型方法？ → B：FastLanguageModel.from_pretrained()

**Q7** Unsloth 挂载 LoRA 方法？ → B：FastLanguageModel.get_peft_model()

**Q8** train_on_responses_only 作用？ → B：只对 assistant 回答计算 loss，mask 掉 system/user

**Q9** QLoRA vs LoRA 在 Unsloth 中的唯一区别？ → B：from_pretrained 时指定 load_in_4bit=True

**Q10** DeepSpeed ZeRO 核心问题？ → B：解决单卡放不下模型（显存分摊）

**Q11** 关于 ZeRO 正确说法？[多选] → A/B/C（DDP不省显存；ZeRO-3省最多但通讯高；ZeRO-1性价比最高；不应盲目选ZeRO-3）

**Q12** 多任务微调需调整哪些参数？[多选] → A/B/C（更多LoRA层、更低学习率、更大epochs；max_seq_length无关）

### 二、判断（2题）

**Q13** Unsloth 中 from_pretrained 返回元组 → ✅ 正确（一次性返回模型+分词器）

**Q14** ZeRO 解决放不下，DDP 解决跑不够快 → ✅ 正确（ZeRO=显存瓶颈，DDP=效率瓶颈）

### 三、简答（1题）

**Q15** 单卡24GB微调 Qwen3.6-27B（BF16≈56GB），用全参/LoRA/QLoRA？

> **答案**：QLoRA，1张卡。全参=56GB权重+梯度+优化器>>24GB❌；LoRA仍需加载完整56GB权重→OOM❌；QLoRA=4bit压缩≈15GB，唯一可行✅

### 关键口诀

| 考点 | 口诀 |
|------|------|
| LLaMA Factory vs Unsloth | Factory=通用多卡WebUI，Unsloth=单卡极致快 |
| ZeRO选型 | 单卡够→DDP；单卡不够→ZeRO-1(切O)→ZeRO-2(切O+G)→ZeRO-3(全切) |
| QLoRA vs LoRA | 代码差一行：load_in_4bit=True |
| train_on_responses_only | 模型只学回答不学提问 |
| 多任务微调三调 | 加层、降lr、加epochs |

## 学习效果评估

- **微调工具链**：LLaMA Factory/Unsloth/DeepSpeed 基础覆盖
- **显存判断**：能从 BF16 权重倒推显存需求，选对微调方案
- **ZeRO 选型**：按单卡够不够→逐级选 ZeRO 的思路清晰
