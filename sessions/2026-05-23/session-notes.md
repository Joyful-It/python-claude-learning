# 学习会话记录 - 2026-05-23

## 今日理解跃迁

> 从"数据清理就是填缺失" → "数据清理有标准决策链：分家→扔掉→补缺→转数字，但最关键的是标准化必须先切后 fit"

---

## 第一节：数据清理标准四步流程（背！）

```
① 分家：哪些是 X（特征），哪些是 y（标签）
② 扔掉：编号列、缺失 >50% 的列、纯乱码列
③ 补缺：数值列填什么？分类列填什么？（看分布）
④ 转数字：字符串 → 数字（映射 / One-Hot）
```

### 各类型列的决策速查

| 列的类型 | 行动 | 泰坦尼克号例子 |
|----------|------|---------------|
| 编号（PassengerId）| ❌ 扔掉 | 只是行号 |
| 文字乱码（Name, Ticket）| ❌ 扔掉 | 无规律 |
| 缺失太多（Cabin, >70%）| ❌ 扔掉 或 提取二元特征 | 891行缺了687 |
| 数值+有缺失（Age）| ✏️ 填中位数 | 有极端值 |
| 分类+有缺失（Embarked）| ✏️ 填众数 | 只有2个缺 |
| 数值+完整（Fare, SibSp, Parch）| ✅ 直接保留 | — |
| 二分类文字（Sex: male/female）| 🔄 map 转 0/1 | — |
| 多分类文字（Embarked: S/C/Q）| 🔄 One-Hot | drop_first=False（神经网络）|

---

## 第二节：基础代码速查（对着写）

```python
# ① 挑列
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = df[features].copy()        # .copy() 断开引用，防 SettingWithCopyWarning
y = df['Survived'].copy()

# ② 填缺失
X['Age'].fillna(X['Age'].median(), inplace=True)            # 数值 → 中位数
X['Embarked'].fillna(X['Embarked'].mode()[0], inplace=True) # 分类 → 众数
# mode()[0]：众数可能返回多个，取第一个

# ③ 文字转数字
X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})           # 二分类 → 手动映射
X = pd.get_dummies(X, columns=['Embarked'], drop_first=False) # 多分类 → One-Hot
# drop_first=False：神经网络不丢第一列

# ④ 转 numpy → 转 float32（PyTorch 需要）
X = X.values.astype(np.float32)
y = y.values.astype(np.float32)
```

### 关键区分

| 写法 | 结果 | 维度 |
|------|------|------|
| `df[['Survived']]` | DataFrame | 二维 |
| `df['Survived']` | Series | 一维 |

---

## 第三节：两种方案对比——基础版 vs 进阶版

### 基础版（10taitan.py 原版）
```
Cabin → 扔掉 ❌
Age → 全局中位数填
Sex → map(0/1)
Embarked → 填众数 + One-Hot
无衍生特征
```

### 进阶版（你朋友版本）
```
做了   Cabin → Has_Cabin 提取"有无船舱"二元特征    ← 更聪明
做了   Age → 按 Pclass+Sex 分组填中位数              ← 更精准
做了   FamilySize / FamilyType / AgeGroup 衍生特征    ← 有业务含义
做错   标准化在切分之前！                            ← ⚠️ 数据泄露
做错   没有切分 train/val！                          ← ⚠️ 无法评估模型
```

### 正确顺序（关键！）

```
① 特征工程（填缺失/编码/衍生）  ← 可以全局做
② 切分 train / val              ← stratify=y 保持比例
③ 标准化                         ← fit 只用 train，transform 给 val
```

**为什么③要在②之后？**
```
StandardScaler.fit(X_train) → 从训练集算均值和方差
如果先在全部数据上 fit → 测试集的信息"泄露"到了训练集 → 评估分数虚高
```

```python
# 正确写法：
scaler = StandardScaler()
X_train[['Age', 'Fare']] = scaler.fit_transform(X_train[['Age', 'Fare']])
X_val[['Age', 'Fare']] = scaler.transform(X_val[['Age', 'Fare']])  # 只用 transform！
```

---

## 第四节：错题本新增

| 问 | 模糊点 | 正确 |
|---|-------|------|
| .copy() 为啥要加？ | 不加也行吧？ | DataFrame 切片是视图，直接改触发 SettingWithCopyWarning，copy() 断开引用 |
| fit_transform vs transform | 都用 fit_transform | fit 是学均值和方差（从训练集）→ transform 只用学到的参数（给验证集）|
| 标准化什么时候做？ | 填完就做 | **切分之后**再做，fit 只用训练集 |
| mode()[0] 什么意思？ | mode() 返回啥？ | 可能多个众数，返回 Series，[0] 取第一个 |

---

## 更新学习效果评估

- **数据清理四步流程**：分家→扔掉→补缺→转数字 ✓
- **各类型列处理方式**：知道哪类填什么 ✓
- **基础代码速查**：会对着写 fillna/map/get_dummies/astype ✓
- **标准化顺序**：理解为什么必须先切后 fit ✓
- **两种方案对比**：能说出进阶版好在哪、错在哪 ✓
- **基础版 vs 进阶版**：理解了 feature engineering 怎么做更好 ✓
