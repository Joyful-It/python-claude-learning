# 学习会话记录 - 2026-04-19

## 会话概览
- 日期：2026-04-19
- 形式：一对一教学
- 核心主题：复习 + 查漏补缺

## 学员提出的问题/需求
1. 想要复习之前学过的知识
2. 不确定复习方式
3. 想按抽查式复习 + 模块复习
4. 想看课件内容

## 讲解的概念与教学过程

### 1. 复习方式讨论
学员选了"抽查式 + 模块复习"结合的方式

### 2. 抽查式复习（4道题）

**问题1：self 是什么意思？**
- 学员回答：self 是对象的意思
- 评价：✅ 基本正确，更准确是"指向自己的指针"

**问题2：drop_duplicates vs dropna 区别？**
- 学员回答：忘了
- 正确答案：
  - drop_duplicates = 删除重复行
  - dropna = 删除含空值的行

**问题3：GET vs POST 区别？**
- 学员回答：GET获取，POST提取
- 更正：GET=拿，POST=放

**问题4：json.dumps vs json.loads？**
- 学员回答：忘了
- 更正：dumps=转字符串，loads=转对象

### 3. 面向对象练习

学员写了一个 Car 类：
```python
class car:
    def __init__(self, brand: str, color: str, price: float, year: int = 2014):
        self.brand = brand
        self.color = color
        self.price = price
        self.year = year
    
    def show_info(self):
        print(f"show all: {self.price}, {self.brand}, {self.color}, {self.year}")
    
    def get_discount(self):
        discount = float(input("please enter discount:"))
        print(f"after price: {self.price * discount}")
```

**遇到的问题：**
- `price: float` 但传了 `"123.4"` 字符串 → 运行时报错
- 解释：Python 类型提示不强制，只在运行时报错

### 4. Python 命名规范讲解

| 类型 | 规范 | 示例 |
|-----|------|------|
| 类名 | 大写开头 | `class Car:` |
| 变量/方法 | 小写+下划线 | `my_car` |
| 常量 | 全大写 | `MAX_SIZE` |
| 私有属性 | 单下划线 | `_name` |

### 5. 课件位置确认

学员课件在：`D:\Desktop\study\AI\课件`

课件清单 vs 进度对比：
- ✅ 01-14 已学
- ⏳ 15 Matplotlib/Seaborn 还没学
- ❌ 17 SQLAlchemy 没更新到进度
- ✅ 18 FastAPI 已学

## 识别的知识漏洞

| 漏洞 | 严重程度 |
|-----|---------|
| drop_duplicates/dropna 区分不清 | 低 |
| json.dumps/loads 区分不清 | 低 |
| Python 类型提示不强制 | 中 |

## 完成的练习
1. Car 类创建（属性+方法）
2. self 理解巩固
3. 折扣计算方法

## 今日代码文件
```
review/4.19/demo1！！！！.py  # Car 类练习
```

## 下次开始时说的话

```
继续复习，请读取：
1. progress/python-tracker.md
2. sessions/2026-04-19/session-notes.md
上次学到：SQLAlchemy还没学，Matplotlib还没学
```

## 作业状态
BERT 情感分析作业已完成 ✅

## 学习效果评估
- 面向对象基础：明显巩固
- 发现遗忘点：drop_duplicates/dropna、json操作
- 整体状态：积极复习中

---

# 复习内容 - 2026-04-19 下午追加

## 复习主题
知识漏洞复习：drop_duplicates/dropna、json.dumps/loads

## 复习内容

### 1. drop_duplicates vs dropna 区别
- **drop_duplicates** = 删除重复的行
- **dropna** = 删除含有空值（NaN）的行
- 学员理解：✅ 正确

### 2. json.dumps vs json.loads 区别
| 方法 | 作用 | 方向 |
|-----|------|------|
| dumps | 打包成JSON字符串 | Python对象 → 字符串 |
| loads | 解析JSON字符串 | 字符串 → Python对象 |

**生活比喻：**
- dumps = 把水果装进密封袋
- loads = 把密封袋打开取出水果

**记忆口诀：**
- dump = 往文件里**倒**（写）
- load = 从文件里**捞**（读）
- s = **s**tring（字符串）

**AI开发场景：**
```python
# 处理大模型API返回的JSON
response = requests.get("https://api.example.com/llm")
result = response.json()        # API返回的JSON字符串 → Python字典

# 保存数据到文件
with open("data.json", "w") as f:
    json.dump(data, f)         # Python对象 → 写入文件

# 从文件读取
with open("data.json", "r") as f:
    data = json.load(f)        # 从文件读取 → Python对象
```

## 检验问题
**Q：大模型API返回JSON字符串，应该用 json.loads 还是 json.dumps？**
**A：json.loads**（解析成Python对象才能在代码里操作）

## 下次继续
- 还需学习：Matplotlib/Seaborn（课件15）
- 还需学习：SQLAlchemy（课件17）
- 待继续复习：继承、重写、super()、封装、多态（OOP部分）
