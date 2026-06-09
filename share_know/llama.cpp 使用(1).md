
> **阅读指引**：以下内容按 **概念 → 环境搭建 → 获取模型 → 使用工具 → 参数参考 → 日常管理 → 速查表** 七步递进。如果你是第一次接触，按顺序读；如果只是回来查命令，直接跳到速查表。

---

### 第七部分：速查表

#### 7.1 量化等级速查
[[GGUF量化版本介绍#三、K 系列量化（K-Quants，当前主流）|详情]]参考

**具体选择：**

优先根据**设备硬件**条件与**使用需求**挑选对应量化版本：

1. 硬件资源充足、追求极致输出效果，优先选择 **FP 16、Q 8_0、Q 6_ K**；
2. 绝大多数日常使用场景，兼顾效果、体积与运行速度，首选 **Q 4 _K_M**，也可选用 **IQ 4_XS**；
3. 设备内存、显存有限，可接受小幅效果损耗，推荐 **Q 3 _K_M、IQ 3_ XXS、IQ 3_ XS**；
4. 老旧低配设备仅保证正常运行，可选择 **Q 2 _K、IQ 2_ XS、IQ 2_ XXS**，该类版本语义损失较大，非必要不选用。

| 等级 | 体积比（相对 FP16） | 效果 | 适用场景 |
|------|-------------------|------|----------|
| **FP16** | 100%（基准） | 最高精度 | 微调模型、超大内存机器；日常不用 |
| **Q5_K_M** | ~35% | 接近 FP16 | 追求极致效果、内存充裕 |
| **Q4_K_M** ⭐ | ~28% | 几乎无感知损失 | **全场景首选**（对话 + 向量，90% 场景用它） |
| **Q3_K_M** | ~22% | 略有损失 | 低内存电脑折中选择 |
| **Q2_K** | ~17% | 明显损失 | 老旧低配设备，不推荐 |

#### 7.2 常用命令速查

```bash
# ─── 快速测试模型 ───
main.exe -m models/ChatLLM/模型名-Q4_K_M.gguf

# ─── 开启对话 API 服务 ───
llama-server.exe -m models/ChatLLM/模型名-Q4_K_M.gguf --host 0.0.0.0 --port 8080 -ngl 99 -c 8192

# ─── 开启向量 API 服务 ───
llama-server.exe -m models/Embedding/模型名-Q4_K_M.gguf --embedding --host 0.0.0.0 --port 8080

# ─── 量化压缩 ───
quantize.exe 输入-f16.gguf 输出-Q4_K_M.gguf Q4_K_M

# ─── HF 原版转 GGUF ───
python convert-hf-to-gguf.py <HF模型文件夹> --outfile 输出-f16.gguf --outtype f16
```

#### 7.3 核心心法（三句话）

1. **llama.cpp = 文件即模型**：有 `.gguf` 就能跑，删 `.gguf` 即删模型，干净透明
2. **长期只守一条规矩**：所有模型归整到 `models/` 分类目录，只留最终 `Q4_K_M.gguf`
3. **获取模型三选一**：下载现成 GGUF → 最简单 / 从 Ollama 扒 → 已有 Ollama 时 / HF 原版手动转 → 自定义模型时

### 第一部分：概念篇

#### 1.1 什么是大模型推理

大模型本质上是一个**巨大的数学函数**：输入一段文字（Prompt），经过数十亿参数的计算，输出下一段文字。这个过程就叫「推理」（Inference）。

- **训练**：用海量数据调整参数（需要几百张显卡、数月时间）→ 产出一个「模型文件」
- **推理**：用训练好的模型文件，输入文字得到输出（可以在你自己电脑上跑）← **llama.cpp 干的就这件事**

#### 1.2 llama.cpp 是什么

**一句话：llama.cpp 是一个用 C/C++ 写成的大模型推理引擎（发动机）。**

它的特点：
- **纯底层**：没有图形界面、没有内置模型仓库、没有隐藏缓存
- **文件即模型**：有 `.gguf` 文件就能跑，删掉文件就删掉模型，干净透明
- **CPU 优先**：不装 CUDA 也能跑，当然装了显卡加速更快
- **可开 API 服务**：启动后可以通过 HTTP 接口调用（`http://127.0.0.1:8080`），Python / LangChain 等项目直接接入

> **llama.cpp vs 常见工具的关系：**
> - **Ollama** = 套在 llama.cpp 外面的可视化管理壳子（自动下载模型、命令行友好）
> - **LM Studio** = 同上，带图形界面
> - 它们底层跑的**都是同一个 llama.cpp 内核**。学会了 llama.cpp，你就理解了这一切的底层原理。

#### 1.3 模型文件的两种格式

| 格式          | 全称                          | 长什么样                                                                       | llama.cpp 能直接用吗 |
| ----------- | --------------------------- | -------------------------------------------------------------------------- | --------------- |
| **HF 原生格式** | HuggingFace 原版              | 一堆散文件：`pytorch_model.bin` / `.safetensors` + `config.json` + tokenizer 配置等 | ❌ 不能，必须先转换      |
| **GGUF 格式** | GGUF（GGML Universal Format） | **单个 `.gguf` 文件**，权重 + 分词器 + 全部配置打包在一起                                     | ✅ 唯一识别的格式       |

**记住：llama.cpp 只认 `.gguf`。** 你在 HuggingFace 下载的原始模型文件夹，必须经过转换才能用。详见第三部分「获取模型」。

#### 1.4 量化是什么

**量化 = 把高精度的浮点数权重「压缩」成低精度数字。**

打个比方：
- 原始模型权重是 **FP16**（每个数字占 16 位二进制），就像一张 100MB 的无损照片
- 量化后变成 **Q4_K_M**（每个数字大约占 4 位），就像同一张照片压成 25MB 的 JPEG

**量化的效果：**
- ✅ 模型文件体积大幅缩小（比如 FP16 的 14GB → Q4_K_M 的 4GB）
- ✅ 运行时占用内存/显存大幅降低
- ✅ 推理速度变快
- ⚠️ 轻微损失语义精度（Q4_K_M 基本感觉不到，Q2_K 才明显）

**llama.cpp 自带量化工具 `quantize.exe`**，可以把 FP16 的 GGUF 压成各种等级。

具体的量化版本介绍，参考 [[GGUF量化版本介绍]]。

---

### 第二部分：环境搭建

#### 2.1 下载 llama.cpp

使用命令，安装**统一 CLI 工具**，一个叫 `llama.exe` 的文件。
```
irm https://llama.app/install.ps1 | iex
```

从 [GitHub Releases](https://github.com/ggml-org/llama.cpp/releases) 下载（手动管理）：

1. **预编译二进制包**：
   - 文件名类似 `llama-bXXXX-bin-win-cuda-cuXX-x64.zip`
   - 里面只有 `.exe` 可执行文件（`llama-server.exe` / `main.exe` / `quantize.exe` 等）
   - 解压即用，不需要编译

2. **源码包 `Source code (zip)`**（需要模型转换时才下载）：
   - 里面包含 `convert-hf-to-gguf.py`（HF 原版模型 → GGUF 的转换脚本）
   - 和 `requirements.txt`（Python 依赖清单）
   - **如果你只下载现成的 GGUF，不需要这个**

#### 2.2 检查 CUDA 版本

如果你有 NVIDIA 显卡，需要下载与 [[CMD 常用命令#查询 CUDA|CUDA]] 版本匹配的二进制包才能启用 GPU 加速；前提在 Windows 下

```powershell
# 命令行查 CUDA 版本
nvidia-smi
# 看输出右上角的 "CUDA Version: 12.x"
```

#### 2.3 目录结构

llama.cpp 中只需要关注 **4 类核心文件**，其余不用碰：

| 文件 / 文件夹 | 作用 | 什么时候用 |
|--------------|------|-----------|
| `llama-server.exe` | **最重要**：开启 API 服务（聊天 + Embedding 向量化） | 开发项目、对接 LangChain 时 |
| `main.exe` | 本地命令行交互聊天 | 快速测试模型能不能跑 |
| `quantize.exe` | 量化工具：FP16 GGUF → Q4_K_M 等压缩版本 | 自制模型时 |
| `convert-hf-to-gguf.py` | Python 脚本：HF 原版多文件 → FP16 GGUF | 从 HuggingFace 原版自制模型时 |
| `models/`（自建） | **你自己的模型仓库**，所有 GGUF 统一放这里 | 日常管理 |

> **推荐目录规范**：在 llama.cpp 根目录手动新建 `models/`，内部再分两个子文件夹：
> ```
> models/
> ├── ChatLLM/      ← 对话大模型（Qwen、Llama、DeepSeek 等）
> └── Embedding/    ← 向量模型（BGE、GTE 等，用于 RAG 检索）
> ```

---

### 第三部分：获取模型

#### 3.1 下载 GGUF

HuggingFace 上有大量作者已经帮你做好量化的 GGUF 单文件。**下载单个 `xxx.Q4_K_M.gguf` → 丢入对应 `models/` 分类文件夹 → 直接用，一步到位。**

> 举例：需要 BGE 向量模型 → 搜索 `bge-large-zh-v1.5` → 下载 `bge-large-zh-v1.5-Q4_K_M.gguf` → 放进 `models/Embedding/`

#### 3.2 Ollama 提取 GGUF

如果你之前用过 Ollama 下载了模型，可以直接把 Ollama 的缓存「扒」出来给 llama.cpp 用：

1. 找到 Ollama 的 `blobs` 文件夹（一般在 `C:\Users\你的用户名\.ollama\models\blobs\`）
2. 找到**体积最大**的那个哈希命名文件（没有后缀名）
3. **复制**（不要剪切！）该文件到你的 `models/` 目录，重命名为 `模型名-Q4_K_M.gguf`
4. 其他小体积哈希文件 + `manifests` 文件夹 = Ollama 的私有索引，llama.cpp 用不上，不用管

> 之后如果你不再用 Ollama，可以把它的整个缓存目录删掉，llama.cpp 不受任何影响。

#### 3.3 Hugging Face 转换

当你需要某个模型但网上没人发布 GGUF 版本时，自己动手。**标准三步流程**（对话模型和向量模型通用）：

**第一步：克隆 HF 原版模型文件夹**
```bash
# 安装 huggingface-hub
pip install huggingface-hub

# 下载完整模型（所有 .safetensors + 配置文件）
huggingface-cli download 模型作者/模型名 --local-dir D:\HF模型存放路径
```

**第二步：用 `convert-hf-to-gguf.py` 生成 FP16 高精度 GGUF**

前制：
- 脚本所在的同级目录需要有 modules 文件夹。
- 安装环境依赖

```python
pip install torch transformers sentencepiece protobuf numpy accelerate
```

```bash
# 生成的模型文件存入，脚本所在的文件夹下 models 文件夹中。
python convert-hf-to-gguf.py D:\HF原模型文件夹路径 --outfile models/模型名-f16.gguf --outtype f16
```

**参数解释**

| 命令片段                    | 作用说明                           | 补充注意                            |
| ----------------------- | ------------------------------ | ------------------------------- |
| `python`                | 调用 Python 解释器，执行脚本             | Windows 终端默认已配置环境变量可直接使用        |
| `convert-hf-to-gguf.py` | 转换脚本，将 HF 模型转为 GGUF 格式         | 终端**必须进入该脚本所在目录**执行命令           |
| `D:\HF原模型文件夹路径`         | 源模型目录，待转换的 Hugging Face 模型完整路径 | 路径含空格 / 中文时，需用英文双引号包裹           |
| `--outfile`             | 固定参数，指定输出文件                    | 后跟文件路径 + 名称                     |
| `models/模型名-f16.gguf`   | 输出文件路径与文件名（相对路径）               | 代表**脚本同级目录**下的`models`文件夹，需提前创建 |
| `--outtype`             | 固定参数，指定模型精度格式                  | 控制量化类型                          |
| `f16`                   | 输出为 FP16 全精度格式                 | 无损转换，文件体积较大                     |

**第三步：用 `quantize.exe` 压缩成常用 Q4_K_M**
```bash
quantize.exe models/模型名-f16.gguf models/模型名-Q4_K_M.gguf Q4_K_M
```

> 转换完成后，HF 原版文件夹和中间产物 `-f16.gguf` 都可以删掉，只保留最终的 `-Q4_K_M.gguf`。

#### 补充理解：

为什么多了一个 FP16 中间文件？

直接下载和手动转换的流程对比：

```
方式一：下载现成 GGUF
  下载 Q4_K_M.gguf → 直接用               ← 一步，无中间产物

方式三：HF 原版手动转换
  HF原版文件夹 → convert脚本 → 临时-F16.gguf → quantize.exe → 最终-Q4_K_M.gguf
                  ↑ 格式翻译              ↑ 中间文件（用完可删）
```

**Q：这个 FP 16 中间文件不是量化流程要求的，是格式翻译流程带出来的。**

A：HuggingFace 原版文件夹里的 `.safetensors` 文件**不是 GGUF 格式**，llama.cpp 不认识它。你必须先用 `convert-hf-to-gguf.py` 做一次「格式翻译」——把权重从 `.safetensors` 里读出来，按 GGUF 规范重新打包。


**Q： 为什么翻译出来的是 FP 16？** 

A：因为 `convert-hf-to-gguf.py` 的 `--outtype` 参数默认值就是 `f16`。这不是随意的——大部分开源模型的原始权重本身就是 FP16 精度存储的（少数老模型用 FP32）。脚本直接按原精度读出、按 GGUF 规范写入，不做任何压缩。所以翻译产出的 GGUF 天然就是 FP16，体积和原版 `.safetensors` 差不多。如果你非要输出 FP32，加 `--outtype f32` 也行，但体积翻倍且毫无意义——FP16 做后续量化的起点已经绰绰有余。

翻译出来的那份 `-f16.gguf` 就是「中间文件」——第二步量化完就可以删掉。

**反过来说**：如果你从 HuggingFace 下载的直接就是 GGUF 文件（不管什么精度），根本不需要经过 FP16，`quantize.exe` 一步就能压到 Q4_K_M。

---

### 第四部分：命令启动

> **前置操作**：打开 CMD 或 PowerShell，切换到 llama.cpp 根目录再执行以下命令；
> 使用 power shell 前缀需要添加 .\

#### 4.1 命令行聊天测试

**用途**：使用`main.exe`快速验证**聊天模型**能不能跑，不需要开服务。

```bash
# 最简用法：加载模型，进入交互式聊天
main.exe -m models/ChatLLM/你的模型名-Q4_K_M.gguf

# 带 GPU 加速（N 卡）
main.exe -m models/ChatLLM/你的模型名-Q4_K_M.gguf -ngl 99

# 指定上下文长度
main.exe -m models/ChatLLM/你的模型名-Q4_K_M.gguf -ngl 99 -c 8192
```

运行后在终端直接打字聊天，输入 `/quit` 退出。

#### 4.2 开启 API 服务

**用途**：通过`llama-server.exe` 启动 HTTP API 服务，让其他程序通过网络调用模型；每个 `llama-server.exe` 只能加载一个模型。

##### 4.2.1 聊天模型
后缀跟参数，查[[#参数说明]]；
具体数值，查模型[[本地模型说明]]；

```bash
# 基础启动（纯 CPU）
./llama-server.exe -m 模型位置 --host 0.0.0.0 --port 8080

# 带 GPU 加速 + 上下文窗口
./llama-server.exe -m 模型位置 --host 0.0.0.0 --port 8080 -ngl 存入显存层数 -c 上下文窗口
```

- 浏览器打开 `http://127.0.0.1:8080` → 能看到内置的聊天网页
- API 地址：`http://127.0.0.1:8080/v1/chat/completions`（兼容 OpenAI 接口格式）

##### 4.2.2 向量模型

```bash
# 必须加 --embedding 参数
./llama-server.exe -m 模型位置 --embedding --host 0.0.0.0 --port 8080
```

- API 地址：`http://127.0.0.1:8080/v1/embeddings`
- 兼容 OpenAI Embedding 接口，LangChain 的 `OpenAIEmbeddings` 可以直接对接

**快速测试**

```Powershell
$body = '{"input":"今天天气真好"}' Invoke-WebRequest -Uri "http://localhost:8080/embeddings" -Method Post -ContentType "application/json" -Body $body
```

##### 4.2.3 多模态模型

```bash
# 需要同时加载大模型 + 图像编码器
llama-server.exe ^
  -m "E:\models\ChatLLM\Qwen3.6-35B-A3B-UD-Q4_K_M.gguf" ^
  --mmproj "E:\models\ChatLLM\Qwen3.6-mmproj-BF16.gguf" ^
  --host 0.0.0.0 --port 18080 ^
  -ngl 25 -c 8192
```

> `--mmproj` 是多模态模型的「眼睛」（图像编码器），负责把图片转成大模型能理解的向量。普通纯文本模型不需要这个参数。

##### 4.2.4 GPU 加速参数说明

| 参数 | 含义 | 怎么设 |
|------|------|--------|
| `-ngl N` | 把前 N 层神经网络放到显卡显存里运算 | 显存充足 → `-ngl 99`（全部上显卡）；显存不够 → `-ngl 25` 左右折中 |
| 不加 `-ngl` | 纯 CPU 推理 | 没显卡或没下 CUDA 版本时默认 |

> **注意**：`-ngl` 只在下载了 CUDA 版（或 Vulkan 版）llama.cpp 时生效。下载的是纯 CPU 版则加了这个参数也无效。

#### 4.3 量化压缩工具

通过`quantize.exe` 将 Hugging Face 的模型转换为 gguf 格式模型

具体命令参考[[#3.3 方式三：从 HF 原版手动转换（自定义模型必备）|模型下载]]中的参数介绍

```bash
# 格式：quantize.exe 输入文件 输出文件 量化等级
quantize.exe models/模型名-f16.gguf models/模型名-Q4_K_M.gguf Q4_K_M
```

---

### 第五部分：API 启动参数

#### 参数说明
[[#4.2.1 聊天模型]]

| 参数                  | 功能                 | 示例 / 建议                                         |
| ------------------- | ------------------ | ----------------------------------------------- |
| `-m <路径>`           | **指定模型文件**（必填）     | `-m models/ChatLLM/qwen-Q4_K_M.gguf`            |
| `--host <IP>`       | 监听地址               | `--host 0.0.0.0` 开放局域网访问；`--host 127.0.0.1` 仅本机 |
| `--port <端口>`       | 服务端口               | 默认 8080；建议换成 `18080` 避免端口占用冲突                   |
| `--embedding`       | 开启 Embedding 向量化功能 | 加载 BGE/GTE 等向量模型时必加                             |
| `--mmproj <路径>`     | 多模态图像编码器文件         | 仅多模态模型（LLaVA / Qwen-VL）需要                       |
| `-ngl <层数>`         | GPU 加速层数           | 显存够 → `99`；大模型显存不够 → `25` 左右                    |
| `-c <长度>`           | 上下文窗口（Token 数）     | `-c 8192` 即单次对话最多记 8K Token 历史                  |
| `--models-dir <目录>` | 自动扫描目录下所有 GGUF     | 配合 Web 控制台可以切换模型，可选                             |

#### 一键启动

在 llama.cpp 根目录新建 `start.bat`，写入（示例）：

**添加命令：**
cd /d "D:\Apply\AI\Model Apply\llama-cuda-13.3-x 64\Ins"
需要进入文件夹在执行；之后直接运行命令，不需要 ./

**启动聊天模型**
```python
# cpu
llama-server.exe -m D:\Apply\AI\Cache\models\Qwen3-8B-Q4_K_M.gguf --host 0.0.0.0 --port 8080

# Gpu
cd /d "D:\Apply\AI\Model Apply\llama-cuda-13.3-x64\Ins"
llama-server.exe ^
-m D:\Apply\AI\Cache\models\Qwen3-8B-Q4_K_M.gguf ^
--host 0.0.0.0 ^
--port 8080 ^
-ngl 99 

pause
```

**启动向量模型**
```python
./llama-server.exe -m D:\Apply\AI\Cache\models\bge-large-zh-v1.5-f16.gguf ^
--embedding --host 0.0.0.0 --port 8080
```

> ⚠️ 旧版 llama.cpp 的命令是 `llama serve --host ...`，新版统一改为 `llama-server.exe -m ...`。如果你看到 `llama serve` 的写法，那是老版本的用法。


**Q：没有使用 -ngl 参数的情况下，为什么 GPU 也繁忙？**
A：使用的 llama.cpp 是 CUDA 编译版（`llama-cuda-13.3-x64`）。即使不加 `-ngl`，**部分算子（如注意力计算、softmax）仍然会自动调用 GPU**。
它不是「纯 CPU」，是「CPU 为主 + GPU 打辅助」。所以你能看到 GPU 有占用——但大部分权重还是在内存里，CPU 算。

---

### 第六部分：模型日常管理

#### 6.1 存储规范

| 规则 | 说明 |
|------|------|
| 一个模型 = 一个 `.gguf` 文件 | 不存在什么「配套文件」，一个文件就是完整模型 |
| 统一放在 `models/` | 长期管理不乱，按 `ChatLLM/` 和 `Embedding/` 分类 |
| 中间产物用完即删 | HF 原版文件夹、`-f16.gguf` 转换后全部删除，只留最终 `-Q4_K_M.gguf` |

#### 6.2 切换模型

```bash
# 停止当前 llama-server（Ctrl+C），换 -m 参数里的 gguf 路径，重启
llama-server.exe -m models/ChatLLM/另一个模型-Q4_K_M.gguf --host 0.0.0.0 --port 8080
```

#### 6.3 删除模型

**直接删除对应的 `.gguf` 文件即可。** 没有隐藏缓存、没有残留文件。这是 llama.cpp 相比 Ollama 最大的优势——Ollama 用哈希文件名管理缓存，你根本不知道哪个文件对应哪个模型。

