# 2026-04-02 学习会话记录

> **日期**：2026-04-02
> **核心主题**：NumPy 基础 + JSON/requests API调用 + 大模型基础概念
> **学习形式**：代码实操 + 理论讲解

---

## 学员提问

- NumPy 是做数组的（已有基础认知）
- JSON 到底是什么？有什么用？
- 什么是 requests.get/post？
- 大模型是怎么训练出来的？
- GPU 为什么比 CPU 快？
- 梯度下降下降的是什么？

---

## 讲解内容

### NumPy 基础

| 知识点 | 状态 | 代码 |
|-------|------|------|
| 创建数组 `np.array()` | ✅ | `np.array([1,2,3])` |
| 广播机制 | ✅ | `arr + 10` |
| reshape 变形 | ✅ | `arr.reshape(2,3)` |
| flatten 拍扁 | ✅ | `arr.flatten()` |
| 转置 `.T` | ✅ | `arr.T` |
| 数组属性 shape/ndim/size/dtype | ✅ | `arr.shape` |
| 切片 | ✅ | `arr[1:3, 1:3]` |
| 排序 `np.sort()` vs `arr.sort()` | ✅ | 前者返回新数组，后者原地修改 |
| 求逆矩阵 | ✅ | `np.linalg.inv(arr)` |
| 最大/最小/平均/中位数/标准差 | ✅ | `np.max/min/mean/average/std` |
| 内积 `np.dot()` | ✅ | `np.dot(a, b)` |

### JSON

| 知识点 | 状态 | 说明 |
|-------|------|------|
| `json.dumps()` | ✅ | 字典 → JSON字符串 |
| `json.loads()` | ✅ | JSON字符串 → 字典 |
| 单双引号区别 | ✅ | 外层单引号是Python包装，内层双引号是JSON标准 |
| `ensure_ascii=False` | ✅ | 保留中文 |
| `indent=4` | ✅ | 美化输出格式 |
| `json.dump/load` | 📖 | 文件操作（未深入） |
| 嵌套数据提取 | ✅ | 字典+列表的逐层访问 |

### requests

| 知识点 | 状态 | 说明 |
|-------|------|------|
| `requests.get()` | ✅ | 获取数据 |
| `requests.post()` | ✅ | 发送数据 |
| `response.status_code` | ✅ | 状态码检查 |
| `response.json()` | ✅ | 解析返回数据 |
| `headers` 参数 | ✅ | 传递API Key |
| `json` 参数（post） | ✅ | 发送JSON数据 |

### 大模型基础概念

| 知识点 | 状态 | 说明 |
|-------|------|------|
| 梯度下降 | ✅ | 猜→算错误→调参数→重复，目标是降低损失值 |
| GPU vs CPU | ✅ | GPU核心多，并行计算，适合矩阵乘法 |
| 本地 vs 云端 | ✅ | 本地慢但免费，云端快但付费 |
| H100/A100/H800/A800 | ✅ | 知道区别和封禁原因 |
| 神经网络层 | ✅ | 输入→矩阵乘法+激活→输出，多层叠加 |
| PyTorch/TensorFlow | 📖 | 知道是什么，还没装 |
| Transformer | 📖 | 知道是注意力机制，主流架构 |

---

## 学员问题与解答

**Q: json.dumps 输出的双引号变单引号了？**
A: 外层单引号是Python的"包装纸"，内层双引号才是JSON内容，打印时外层不显示

**Q: json只能用字典吗？**
A: 不是，JSON支持：字典、列表、字符串、数字、布尔值、None

**Q: response.status_code == 200 和 response == 200 有区别吗？**
A: 前者正确（取对象的属性），后者错误（对象本身不是数字）

**Q: requests.post 怎么用？**
A: `requests.post(url, headers={}, json={})`，注意参数是 `json=` 不是 `data=`

**Q: 梯度下降下降的是什么？**
A: 下降的是损失值（错误程度），目标是把错误降到最低

---

## 今日代码练习

```python
# NumPy 广播
arry = np.array([12, 34, 32, 12, 34, 56])
print(arry + 10)  # 广播加法

# reshape + flatten + T
arr1 = arry.reshape(2, 3)
print(arr1.T)  # 转置

# JSON 嵌套提取
temp = api_data["current_condition"][0]["temp_C"]

# requests 调用 API
response = requests.post(url, headers=headers, json=data)
result = response.json()

# 大模型 API 调用（智谱）
# 路径待确认（/api not found 错误）
```

---

## 知识漏洞

| 考点 | 问题 | 状态 |
|-----|------|------|
| json.dump/load | 文件操作未深入 | 待补充 |
| NumPy argmax/argmin/where | 未苏格拉底式讲解 | 待补充 |
| 智谱API路径 | /api not found，需确认正确路径 | 待确认 |

---

## 今日收获

1. ✅ NumPy 数组操作基本掌握
2. ✅ JSON 数据处理学会
3. ✅ requests API 调用入门
4. ✅ 理解大模型底层原理（矩阵乘法 + 梯度下降）
5. ✅ 理解 GPU 为什么比 CPU 快
6. ✅ 理解 H100/H800 等显卡区别

---

## 明日计划

- [ ] 确认智谱API正确路径
- [ ] 补充 json.dump/load 苏格拉底式教学
- [ ] 补充 NumPy argmax/argmin/where
- [ ] 继续巩固循环结构（while/for）
- [ ] 安装 PyTorch，体验 GPU 加速
