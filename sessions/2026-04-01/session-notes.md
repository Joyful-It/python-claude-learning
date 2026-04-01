# 学习会话记录 - 2026-04-01

## 会话概览
- **日期**：2026-04-01
- **时长**：约2小时
- **形式**：交互式教学（苏格拉底式）
- **核心主题**：数据分析预习 + JSON + requests + 调用大模型API

---

## 学员提出的问题

1. "数据分析是什么？NumPy是做数组的吧？"
2. "reshape变形是内存需要吗？"
3. "ndim怎么记？"
4. "json怎么使用？"
5. "json到底是用来干什么的？"
6. "request get怎么使用接接口？"
7. "request.get是获取还是发送？"
8. "怎么调用智谱大模型API？"

---

## 今日学习内容

### 一、NumPy 基础（预习）

#### 1. 创建数组
```python
import numpy as np
arr = np.array([80, 90, 75, 85])
```

#### 2. 数组运算（向量化）
```python
new_arr = arr * 2  # 一次性对整个数组运算
```

#### 3. 数组变形 reshape
```python
data = np.array([1,2,3,4,5,6,7,8])
table = data.reshape(4, 2)  # 变成4行2列
```
**学员理解**：变形不是为了内存，而是数据结构需要（图像处理、矩阵运算）

#### 4. 数组属性
- `shape`：形状
- `ndim`：维度（n-dim = n维度）
- `size`：元素总数
- `dtype`：数据类型

#### 5. 切片
```python
arr[1:4]           # 一维
table[0, :]        # 二维：第1行
table[:, 0]        # 二维：第1列
table[1:3, 1:3]    # 二维：行列同时切片
```

#### 6. 排序与搜索
```python
np.sort(arr)       # 返回新数组，原数组不变
arr.sort()         # 原地排序，返回None

np.argmax(arr)     # 最大值的索引
np.argmin(arr)     # 最小值的索引
np.where(arr > 30) # 满足条件的位置
```

**记忆口诀**：
- np.sort = 复制一份再排
- arr.sort = 自己排

---

### 二、JSON

#### 1. 基本概念
- JSON = 数据的"通用包装箱"
- 不同语言之间交换数据用的格式

#### 2. 核心操作
```python
import json

# 字典 → JSON字符串
json_str = json.dumps(data, ensure_ascii=False, indent=4)

# JSON字符串 → 字典
data = json.loads(json_str)

# 写入文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 读取文件
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

#### 3. 记忆要点
| 函数 | 作用 |
|-----|------|
| dumps | 字典 → 字符串（带s） |
| loads | 字符串 → 字典（带s） |
| dump | 字典 → 文件（不带s） |
| load | 文件 → 字典（不带s） |

#### 4. 单双引号问题
- Python字典可以用单引号或双引号
- JSON标准必须用双引号
- 外层单引号是Python的"包装纸"

---

### 三、requests 模块

#### 1. GET 请求（获取数据）
```python
import requests
response = requests.get(url)
data = response.json()
```

#### 2. POST 请求（发送数据）
```python
response = requests.post(
    url="...",
    headers={"Authorization": "Bearer key"},
    json={"model": "glm-5", "messages": [...]}
)
```

#### 3. GET vs POST
| 方法 | 作用 | 场景 |
|-----|------|------|
| get | 获取 | 查数据 |
| post | 发送 | 提交数据、调用API |

---

### 四、调用大模型 API（尝试）

#### 学员尝试调用智谱 GLM-5
```python
response = requests.post(
    url="http://xxx/api",
    headers={"Authorization": "Bearer key"},
    json={"model": "glm-5", "messages": [{"role": "user", "content": "你好"}]}
)
```

**遇到问题**：返回 `{"error": "Not Found", "message": "Route /api not found"}`

**原因**：API路径不正确，需要确认正确的endpoint

---

### 五、其他知识点

#### 1. time 模块
```python
import time
time.sleep(2)           # 暂停2秒
time.time()             # 时间戳
time.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间
```

#### 2. random 模块
```python
import random
random.random()         # 0-1随机数
```

#### 3. Pydantic（了解）
- 用类定义JSON结构
- 自动类型验证
- 点语法取值

---

## 学员完成的练习

1. ✅ NumPy reshape练习
2. ✅ NumPy 切片练习（取出指定行列）
3. ✅ JSON dumps/loads练习
4. ✅ requests.get 调用GitHub API
5. ✅ 嵌套JSON数据提取练习（模拟天气数据）
6. ✅ 尝试调用智谱API（未成功，路径问题）

---

## 知识漏洞

| 漏洞 | 状态 | 备注 |
|-----|------|------|
| json.dump/load 文件操作 | 待巩固 | 讲解时未用苏格拉底式 |
| argmax/argmin/where | 待巩固 | 讲解时未用苏格拉底式 |
| 大模型API调用 | 进行中 | URL路径需确认 |

---

## 学习效果评估

### 掌握较好的内容
- NumPy 数组创建、运算、切片 ✅
- JSON 基本操作 ✅
- requests.get 获取数据 ✅
- 嵌套数据提取逻辑 ✅

### 需要巩固的内容
- json 文件操作
- NumPy 搜索函数
- requests.post 调用大模型API

### 学员反馈
- "感觉这几天学的东西太多了，脑子跟不上了"
- 建议适当放慢节奏，多练习巩固

---

## 遗留任务

1. [ ] 确认智谱API的正确路径
2. [ ] 用苏格拉底式补充 json.dump/load
3. [ ] 用苏格拉底式补充 argmax/argmin/where
4. [ ] 天气API综合练习（可选）

---

## 下次计划

- 巩固今天学习的内容
- 完成大模型API调用
- 适当放慢节奏，多做练习
