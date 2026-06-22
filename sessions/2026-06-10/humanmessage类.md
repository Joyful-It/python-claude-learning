你现在这个阶段，**其实不用急着理解面向对象的全部理论**（类、继承、多态那些），只要先搞懂：

> **什么叫“创建对象”**

就够了。

------

# 一、先从现实世界理解

比如：

```text
汽车
```

这是一个概念。

你可以说：

```text
汽车有颜色
汽车有品牌
汽车能跑
```

但这辆车还不存在。

------

相当于代码里的：

```python
class Car:
    pass
```

这里只是在定义：

```text
汽车这个模板
```

------

然后你去买了一辆车：

```text
红色
比亚迪
```

这辆具体的车就出现了。

------

对应：

```python
my_car = Car()
```

这就叫：

```text
创建对象
```

或者：

```text
实例化
```

（面试常说实例化）

------

# 二、最简单代码

例如：

```python
class Student:
    pass
```

这里：

```python
Student
```

是类（模板）。

------

创建对象：

```python
s1 = Student()
```

此时：

```python
s1
```

就是对象。

------

可以理解：

```text
Student
=
学生设计图

s1
=
具体学生
```

------

# 三、为什么要创建对象

因为对象可以存数据。

例如：

```python
class Student:
    def __init__(self, name):
        self.name = name
```

创建：

```python
s1 = Student("张三")
s2 = Student("李四")
```

得到：

```text
s1
  name=张三

s2
  name=李四
```

------

相当于：

```text
按照同一张模板

制造出两个不同的人
```

------

# 四、回到 HumanMessage

你看到：

```python
HumanMessage(content=prompt)
```

其实和：

```python
Student(name="张三")
```

几乎一样。

------

例如：

```python
msg = HumanMessage(
    content="你好"
)
```

相当于创建了一个消息对象。

里面保存：

```python
msg.content
```

值：

```python
"你好"
```

------

可以想象成：

```text
HumanMessage
=
消息模板
```

------

创建：

```python
HumanMessage(
    content="你好"
)
```

得到：

```text
一条具体消息
```

------

# 五、为什么不直接传字符串

很多人会问：

```python
llm.invoke("你好")
```

不行吗？

------

有些模型可以。

但 LangChain 统一成：

```python
HumanMessage
AIMessage
SystemMessage
```

三种对象。

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

模型就知道：

```text
第一条是系统提示

第二条是用户提问
```

------

如果全是字符串：

```python
[
    "你是老师",
    "什么是Transformer"
]
```

模型不知道谁是谁。

------

所以要创建对象。

------

# 六、对象里面有什么

例如：

```python
msg = HumanMessage(
    content="你好"
)
```

内部大概类似：

```python
{
    "type":"human",
    "content":"你好"
}
```

只是封装得更漂亮。

------

你可以这样理解：

```python
HumanMessage(...)
```

其实是在帮你生成一个特殊的数据结构。

------

# 七、为什么要加括号

这里：

```python
HumanMessage
```

只是类名。

模板。

------

例如：

```python
Student
```

只是：

```text
学生这个概念
```

------

只有：

```python
Student()
```

才会真正创建一个学生。

------

所以：

```python
HumanMessage
```

和：

```python
HumanMessage(...)
```

完全不同。

------

前者：

```text
消息模板
```

后者：

```text
具体消息对象
```

------

# 八、Agent代码里怎么判断是不是在创建对象

一个经验：

看到：

```python
大写字母开头(...)
```

通常就在创建对象。

例如：

```python
HumanMessage(...)
AIMessage(...)
SystemMessage(...)
Document(...)
```

------

而：

```python
print(...)
join(...)
split(...)
invoke(...)
```

通常是在调用函数或方法。

------

# 九、你目前可以这样记

看到：

```python
HumanMessage(
    content=prompt
)
```

不要想什么类、继承。

直接翻译：

```text
创建一条用户消息

消息内容是 prompt
```

------

看到：

```python
Document(
    page_content=text
)
```

翻译：

```text
创建一个文档

文档内容是 text
```

------

看到：

```python
AIMessage(
    content="你好"
)
```

翻译：

```text
创建一条AI回复消息
```

------

现阶段最重要的一句话：

```text
类(Class) = 模板

对象(Object) = 按模板造出来的具体东西

HumanMessage(content=prompt)
=
按照 HumanMessage 模板
创建一个具体消息对象
```

等你后面学到 `__init__`、`self` 的时候，你会突然发现：

```python
HumanMessage(content=prompt)
```

其实和你自己写的：

```python
Student(name="张三")
```

本质上一模一样。那时“创建对象”这个概念就彻底打通了。