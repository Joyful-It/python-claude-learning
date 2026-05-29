# 学习会话记录 - 2026-05-19

## 今日理解跃迁

> 从"卷积核怎么动" → "16核×10参数=160，各学各的，同时并行滑动——没人规定谁学什么，全靠损失函数+梯度下降自己卷出来"

> 从"模型代码每次要重写" → "所有模型 = 同一套5步骨架，只换中间第③块（模型结构）和第④块（损失函数）"

---

## 第一节：PyTorch 深度学习五块模板（背！所有 DL 项目通用）

```
① 数据加载     df → copy → fillna → 编码 → 切分 → 标准化    ← 每个项目不一样
② DataLoader   Dataset 类 + DataLoader(batch, shuffle)        ← 基本不变
③ 模型定义     Linear/Conv/LSTM 搭积木                        ← 换！核心变化
④ 训练配置     损失函数 + 优化器 + lr + epochs                 ← 损失换，其余微调
⑤ 训练循环     forward→loss→backward→step→zero_grad           ← 永远不变，写死
```

| 任务 | 泰坦尼克号 | MNIST | YOLO实时检测 |
|------|-----------|-------|------------|
| ③ 模型 | Linear(9→128→64→1) | CNN(Conv+Pool+FC) | YOLOv8(预训练) |
| ④ 损失 | BCEWithLogitsLoss | CrossEntropyLoss | 内置 |
| ⑤ 循环 | **不变** | **不变** | **不变** |

---

## 第二节：泰坦尼克号数据处理链（按执行顺序背）

```
1. X = df[features].copy()          ← copy 斩断引用，防 SettingWithCopyWarning
2. X['Age'] = fillna(中位数)         ← 数值用中位数（防极端值）
3. X['Embarked'] = fillna(众数)      ← 类别用众数（字母不能加减）
4. X['Sex'] = X['Sex'].map({male:0, female:1})  ← 二分类映射
5. X = pd.get_dummies(X, columns=['Embarked'])  ← One-Hot: S→[1,0,0], C→[0,1,0]
6. train_test_split(..., stratify=y)            ← 分层抽样，保正负比例
7. X_train = X_train.copy()                     ← 切片先 copy 再改
8. X_train = scaler.fit_transform(X_train)      ← 训练集：学+用（记住均值/标准差）
9. X_val = scaler.transform(X_val)              ← 验证集：只用不学（防数据泄露！）
10. Dataset + DataLoader                        ← Dataset=菜单, DataLoader=服务员
```

**口诀**：
```
切片先 copy，数值中位数，类别填众数
类别做 One-Hot，分层抽样 stratify
fit_transform 训练用，transform 验证用——反过来就是数据泄露
```

---

## 第三节：CNN 卷积核心速查

### 卷积 vs 全连接

| | 全连接 `X @ W` | 卷积 `input ⊗ kernel` |
|---|---|---|
| 数学 | 矩阵乘法 | 滑动内积 |
| 参数 | W 矩阵 | kernel 小矩阵 × N个 |
| 谁教的 | 反向传播 + 梯度下降 | **同样！** |

### 通道数

```
nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3)

in_channels=1   → 输入是黑白图（1通道）
out_channels=16 → 这一层用 16 个卷积核，产出 16 张特征图
```

### 参数数计算公式

```
nn.Conv2d(1, 16, 3, bias=True)
每核：3×3×1 + 1(bias) = 10
总共：10 × 16 = 160 个参数（不是 10 个！各核不共享！）

nn.Conv2d(16, 32, 3, bias=True)
每核：3×3×16 + 1 = 145
总共：145 × 32 = 4640
```

### 卷积核分工——无人预设，自己卷出来

```
① 16 个核随机初始化 → 各不相同
② 前向：并行滑动 → 16 张特征图 → 汇合出预测
③ 损失 = 法官 → 每个核按贡献领罚
④ 反向传播 → 各收各的梯度
⑤ 有用的加强，没用的推往其他方向
——训练结束自动分工，核1检测横线，核2检测竖线...
```

### 漏斗规律

```
通道数：浅层少 → 深层多（特征越来越丰富）
空间尺寸：浅层大 → 深层小（逐层压缩，只留最重要的）
```

---

## 第四节：YOLO 实时检测 5 步骨架（背！）

```python
# ① 加载模型
model = YOLO("yolov8n.pt").to(device)

# ② 打开数据源（摄像头/视频文件/图片）
cap = cv2.VideoCapture(0)

# ③ 循环读帧
while True:
    ret, frame = cap.read()
    if not ret: break

    # ④ 模型检测
    results = model(frame, stream=True)

    for result in results:
        for box in result.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0])   # 坐标
            conf = float(box.conf[0])               # 置信度
            cls_name = model.names[int(box.cls[0])] # 类名
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

    # ⑤ 显示 + 按键
    cv2.imshow('window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

# 清理
cap.release()
cv2.destroyAllWindows()
```

### YOLO 各模型

| 模型 | 大小 | 速度 | 场景 |
|------|------|------|------|
| yolov8n | 6MB | 最快 | 入门/实时 |
| yolov8s | 22MB | 快 | 一般 |
| yolov8m | 52MB | 中 | 平衡 |
| yolov8l | 88MB | 慢 | 高精度 |
| yolov8x | 136MB | 最慢 | 最高精度 |

### 底层结构 = Conv + BN + SiLU 反复堆

```
每个检测块 = Conv2d(kernel 3×3 滑动内积) + BatchNorm2d(标准化) + SiLU(激活折弯)
几十层堆叠 → 漏斗：通道 3→16→32→64→128→256，尺寸 640→320→160→80→40→20
```

---

## 第五节：OpenCV 基础操作速查

```python
# 读图
img = cv2.imread("路径.jpg")                    # 返回 [H, W, 3] BGR
img_gray = cv2.imread("路径.jpg", cv2.IMREAD_GRAYSCALE)  # [H, W] 灰度

# 显示
cv2.imshow("窗口名", img)                       # 两个参数！窗口名 + 图片
cv2.waitKey(0)                                  # 0=无限等待按键
cv2.destroyAllWindows()                         # 关闭所有窗口

# 人脸检测（自动！不再手写坐标裁）
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 人脸检测先转灰度
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# 返回 [(x, y, w, h), ...] → 直接 img[y:y+h, x:x+w] 裁剪

# 切片裁剪
crop = img[y1:y2, x1:x2]                        # 先高(行)再宽(列)！

# 画框
cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)

# 写字
cv2.putText(img, "文字", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 字号, 颜色, 线宽)

# 保存
cv2.imwrite("路径.jpg", img)

# 摄像头
cap = cv2.VideoCapture(0)     # 0=自带摄像头
ret, frame = cap.read()       # ret=是否成功, frame=画面数组
cap.release()                 # 用完释放
```

---

## 第六节 PyTorch 常用小知识点

```python
# 设备选择（背这一句）
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)

# 多卡并行（知道就行，不常用）
model = nn.DataParallel(model)  # 入门，一行搞定

# 模型层数打印
print(model)  # 看到每层的 Conv2d/BatchNorm/激活 参数

# conv 输出尺寸公式
W_out = (W_in + 2P - K) / S + 1
# 例：K=3, P=1, S=1 → (28+2-3)/1+1 = 28 尺寸不变
# 例：K=3, P=1, S=2 → (28+2-3)/2+1 = 14 尺寸减半
```

---

## 第七节：关键对比速查

| 概念 | 含义 | 记号 |
|------|------|------|
| fit_transform | 学 + 应用（记住均值和标准差） | 训练集专用 |
| transform | 只用不学（用训练集学的值） | 验证/测试集 |
| Dataset | 菜单：第 i 条数据是什么 | 定义 `__getitem__` |
| DataLoader | 服务员：打包 + 乱序 + 上菜 | batch_size, shuffle |
| .view(-1, 1) | 把 `[A,B,C]` 变为 `[[A],[B],[C]]` | 对齐形状 |
| .to(device) | 把模型/张量搬到 GPU/CPU | 不下载，只搬运 |
| YOLO("xx.pt") | 下载 + 加载预训练模型 | 第一次自动下载 |
| .copy() | 斩断 DataFrame 引用链 | 防 SettingWithCopyWarning |
| .astype(np.float32) | bool→float 转换 | 防 numpy.object_ 报错 |

---

## 第八节：试卷知识点速记

### 选择核心

| 题 | 考点 | 答案 | 口诀 |
|----|------|------|------|
| 1 | DL 核心思想 | B.分层特征学习 | 从低到高，自己学出来 |
| 2 | ML 范式 | C.AlphaGo=强化学习 | 有反馈=强化，没标签=无监督 |
| 3 | 激活函数 | C.ReLU负输入=0 | Sigmoid易梯度消失，ReLU现标配 |
| 4 | CNN 核心机制 | C.序列建模(不是CNN的) | CNN三件套：感受野+权值共享+池化 |
| 5 | 优化器王者 | B.Adam | 动量+自适应学习率 |
| 6 | MNIST | C.是彩色(❌灰度) | 28×28灰度，6万训练 |
| 7 | 长序列 | B.LSTM | 三门控遗忘输入输出 |
| 8 | 正则化 | A.L1=稀疏 | L1→0, L2→小, Dropout=训丢测全 |
| 9 | conv尺寸 | B.28×28 | K=3,P=1,S=1→尺寸不变 |
| 10 | 类别不平衡 | C.Focal Loss | 压易样本，专注难样本 |

### 简答核心

```
11. 为什么必须非线性激活？
    → 没有激活=线性堆线性=还是线性，多层白搭。加激活才能拟合任意函数。

12. 卷积层 vs 池化层
    → 卷积：提取特征（边缘/纹理），权值共享减参数
    → 池化：下采样缩小尺寸，保留主特征，增平移不变性

13. L1 vs L2
    → L1(|w|)：产生稀疏解，权重变0 → 特征选择
    → L2(w²)：权重变小但不为0 → 防过拟合
    → 共同目标：防过拟合，提泛化

14. CNN代码分析：
    - Conv2d(1,32,...): 1=灰度输入，32=32个卷积核
    - conv(28→28) + pool(28→14): 输出14×14
    - .view(-1, 64*7*7): 展平！28→14→7，64通道→64×7×7=3136
    - model.eval(): Dropout失效，BatchNorm用滑动均值（不是当前batch的）
```

---

## 第九节：今日错题本

| 问 | 错误 | 正确 |
|---|------|------|
| CNN 和 RNN 关系 | 卷积用到图像=RNN | **CNN≠RNN**：空间vs序列，完全不同 |
| bias 含在核里？ | 3×3=9含bias | bias 独立标量，加结果上，不在核里 |
| 16核参数 | 共享10参数 | **各核独立**，16×10=160 |
| 核滑动方式 | 一个接一个滑 | **16个同时并行**，各用各参数 |
| imshow参数 | 只传图片 | **imshow("窗口名", img)**，两个参数 |
| 切片语法 | `10:200.:` 多了个点 | `10:200:` 没有点 |
| fit_transform 验证集 | fit_transform | **只 transform**，否则数据泄露 |
| q 退出无效 | 没写 break | `if key == ord('q'): break` |
| 缩进 | YOLO 检测在循环外 | 检测/imshow/waitKey 全在 while 里 |
| %D 日期格式 | datetime 用 %D | 应该是 **%d**（小写） |
| 相对路径 | 以为相对脚本位置 | 相对**执行目录**，不是脚本位置 |

---

## 学习效果评估

- **DL 五块模板**：能说清每块的变与不变 ✓
- **泰坦尼克号 9 步数据处理链**：能按顺序说出，知道每步原因 ✓
- **数据泄露**：fit_transform vs transform 区分清楚 ✓
- **CNN 卷积核**：参数数计算正确，并行机制理解 ✓
- **卷积核分工**：理解涌现机制 ✓
- **YOLO 5 步骨架**：能独立写出流程 ✓
- **YOLO 底层结构**：理解=Conv+BN+SiLU 反复堆 ✓
- **OpenCV 基础**：读图/显示/人脸检测/裁剪/摄像头 ✓
- **试卷 14 题**：全部理解，简答能用自己的话讲 ✓
- **待验证**：明天独立重现泰坦尼克号代码

---
