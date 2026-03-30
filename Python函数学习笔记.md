# Python 学习笔记 - 函数的参数

## 学习内容

### 1. 循环的思考
- **问题**：如何打印100遍"你好"？
- **引出**：用循环代替重复代码

### 2. if语句中的逻辑符号
| 逻辑 | Python符号 |
|------|-----------|
| 并且 | `and` |
| 或者 | `or` |
| 非 | `not` |

示例：
```python
if age >= 18 and age < 65:
    print("成年上班族")
```

### 3. 函数的参数（重点）

#### 3.1 形参 vs 实参
```python
def sum(num1, num2):  # num1, num2 是形参
    return num1 + num2

print(sum(1, 1))      # 1, 1 是实参
```

- **形参**：定义函数时的参数名
- **实参**：调用函数时传入的具体值

#### 3.2 四种参数形式

**1. 直接参数名**
```python
def show(name):
    print("欢迎", name)

show("张三")
```

**2. 参数默认值**
```python
def show(name='python'):
    print("欢迎", name)

show("张三")  # 传递就使用实参
show()       # 不传就使用默认值
```

**3. *args - 接收多个位置参数（转为元组）**
```python
def show3(name, *scores):
    print(name)
    for score in scores:
        print(score)

show3("李四", 11, 22, 33, 44)
```

**4. **kwargs - 接收多个关键字参数（转为字典）**
```python
def show4(name, **courses):
    print(name)
    for c in courses.keys():
        print(c, "的成绩：", courses[c])

show4("王麻子", s1=88, s2=90, s3=88)
```

### 4. 练习题
1. 实现判断闰年的函数
2. 实现求阶乘的函数
3. 实现指定范围内偶数之和的函数

---
*学习日期：2026-03-30*
