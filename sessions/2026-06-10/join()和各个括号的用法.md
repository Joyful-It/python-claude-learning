这其实是 Python 初学者到进阶阶段最容易混乱的地方：

> **什么时候用 ()、什么时候用 []、什么时候用 {}？**

你现在看到的：

```python
remaining = "\n".join(state["tasks"])

response = llm.invoke([HumanMessage(content=prompt)])
```

本质上同时出现了三种括号。

我先讲这两个例子，再给你一个通用总结。

------

# 一、先讲 join()

代码：

```python
remaining = "\n".join(state["tasks"])
```

假设：

```python
state["tasks"] = [
    "做数学",
    "背单词",
    "写日记"
]
```

------

## join 的意思

可以理解成：

```text
把列表中的多个字符串

↓

用某个符号连接起来

↓

变成一个字符串
```

------

例如：

```python
",".join(["苹果","香蕉","西瓜"])
```

结果：

```python
"苹果,香蕉,西瓜"
```

------

再例如：

```python
"-".join(["1","2","3"])
```

结果：

```python
"1-2-3"
```

------

你的例子：

```python
"\n".join(
    [
        "做数学",
        "背单词",
        "写日记"
    ]
)
```

结果：

```python
"做数学\n背单词\n写日记"
```

显示出来：

```text
做数学
背单词
写日记
```

------

所以：

```python
split()
```

是：

```text
字符串
↓
列表
```

------

而：

```python
join()
```

是：

```text
列表
↓
字符串
```

它们是一对反操作。

------

# 二、state["tasks"] 为什么是中括号？

因为：

```python
state
```

是字典（dict）。

例如：

```python
state = {
    "tasks": ["做数学","背单词"],
    "result": ""
}
```

取值：

```python
state["tasks"]
```

结果：

```python
["做数学","背单词"]
```

------

这里：

```python
[]
```

表示：

```text
通过key取字典里的值
```

------

类似：

```python
student["name"]
student["age"]
```

------

# 三、再讲这个最容易懵的

```python
response = llm.invoke(
    [HumanMessage(content=prompt)]
)
```

很多层括号套一起。

拆开看。

------

## 第一层 HumanMessage()

```python
HumanMessage(content=prompt)
```

这是：

```python
类()
```

表示：

```text
创建对象
```

类似：

```python
Student(name="张三")
```

------

例如：

```python
msg = HumanMessage(
    content="你好"
)
```

得到：

```python
HumanMessage(
    content="你好"
)
```

一个消息对象。

------

这里：

```python
()
```

表示：

```text
调用函数
或者
创建对象
```

------

# 第二层 []

```python
[
    HumanMessage(content=prompt)
]
```

表示：

```text
列表
```

相当于：

```python
messages = [
    msg
]
```

------

为什么放列表？

因为 LangChain 支持：

```python
[
    SystemMessage(...),
    HumanMessage(...),
    AIMessage(...)
]
```

多轮对话。

------

例如：

```python
[
    SystemMessage(
        content="你是老师"
    ),

    HumanMessage(
        content="什么是Transformer"
    )
]
```

------

# 第三层 invoke()

```python
llm.invoke(...)
```

表示：

```text
调用模型
```

类似：

```python
calculator.add(1,2)
```

------

所以：

```python
llm.invoke(
    [HumanMessage(content=prompt)]
)
```

可以翻译成人话：

```text
创建一个HumanMessage对象

↓

放进列表

↓

把列表发给模型

↓

返回结果
```

------

# 四、Python 三种括号通用总结

这是最重要的。

------

## ()

圆括号

最常见。

### 函数调用

```python
print("hello")
```

------

### 方法调用

```python
text.split("\n")
```

------

### 创建对象

```python
HumanMessage(content=prompt)
```

------

### 数学运算优先级

```python
(1 + 2) * 3
```

------

记忆：

```text
()
≈ 执行动作
```

------

# []

中括号

### 列表

```python
[
    "苹果",
    "香蕉"
]
```

------

### 取列表元素

```python
tasks[0]
```

------

### 切片

```python
tasks[1:]
```

------

### 字典取值

```python
state["tasks"]
```

------

记忆：

```text
[]
≈ 数据容器
或者
取东西
```

------

# {}

大括号

### 字典

```python
{
    "name":"张三",
    "age":20
}
```

------

### 函数返回

```python
return {
    "tasks": tasks
}
```

------

### 集合(set)

```python
{
    1,
    2,
    3
}
```

不过Agent代码里很少见。

------

记忆：

```text
{}
≈ 键值对映射
```

------

# 五、Agent代码里最常见组合

你以后会天天看到：

```python
return {
    "tasks": [
        "做数学",
        "背单词"
    ]
}
```

拆开：

```python
{}
```

字典

里面：

```python
"tasks"
```

key

对应：

```python
[]
```

列表

里面：

```python
"做数学"
```

字符串

------

再比如：

```python
llm.invoke(
    [
        HumanMessage(
            content=prompt
        )
    ]
)
```

拆开：

```python
invoke()
```

函数调用

参数是：

```python
[]
```

列表

里面是：

```python
HumanMessage()
```

对象

对象里：

```python
content=prompt
```

参数赋值

------

你可以先记一个速查表：

| 符号 | 最常见用途         | 例子                                    |
| ---- | ------------------ | --------------------------------------- |
| `()` | 调用函数/创建对象  | `print()`、`invoke()`、`HumanMessage()` |
| `[]` | 列表、索引、切片   | `["a","b"]`、`tasks[0]`                 |
| `{}` | 字典               | `{"tasks": tasks}`                      |
| `.`  | 调对象的方法或属性 | `llm.invoke()`、`text.split()`          |
| `=`  | 赋值               | `x = 1`                                 |
| `:`  | 字典键值、切片     | `{"a":1}`、`[1:]`                       |

如果你把这些符号彻底搞懂，后面看 LangGraph、LangChain、RAG 的代码，至少能读懂 80% 的语法，不会再被各种括号套娃绕晕。