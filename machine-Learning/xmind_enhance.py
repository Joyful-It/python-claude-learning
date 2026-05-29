"""增强机器学习脑图 —— 补充我们学习会话的核心推导内容"""
import json
import uuid
import copy
import zipfile
import os
import shutil

def new_id():
    """生成XMind节点ID"""
    return uuid.uuid4().hex[:32]

def make_node(title, children=None):
    """创建一个XMind节点"""
    node = {
        "id": new_id(),
        "title": title,
        "extensions": [],
        "position": {"x": 0, "y": 0}
    }
    if children:
        node["children"] = {"attached": children}
    return node

def find_node(nodes, title):
    """在节点列表中按标题查找节点（精确匹配）"""
    for n in nodes:
        if n["title"] == title:
            return n
    return None

def find_node_contains(nodes, keyword):
    """在节点列表中按关键词查找（包含匹配）"""
    for n in nodes:
        if keyword in n["title"]:
            return n
    return None

def get_children(node):
    """获取节点的子节点列表"""
    if "children" in node and "attached" in node["children"]:
        return node["children"]["attached"]
    return []

def ensure_children(node):
    """确保节点有children.attached，返回子节点列表"""
    if "children" not in node:
        node["children"] = {"attached": []}
    if "attached" not in node["children"]:
        node["children"]["attached"] = []
    return node["children"]["attached"]

def add_children(parent, new_nodes):
    """给父节点批量添加子节点"""
    children = ensure_children(parent)
    children.extend(new_nodes)

# ============================================================
# 加载原始文件
# ============================================================
with open("c:/Project/python/tmp_xmind/content.json", "r", encoding="utf-8") as f:
    data = json.load(f)

sheet = data[0]
root = sheet["rootTopic"]
root_children = get_children(root)

# ============================================================
# 1. 核心概念 → 增强关键术语 (权重w/偏置b/损失函数/正则化)
# ============================================================
hexin = find_node(root_children, "核心概念")
hexin_kids = get_children(hexin)

guanshu = find_node(hexin_kids, "关键术语")
guanshu_kids = get_children(guanshu)

guanshu_kids.extend([
    make_node("权重(w) — 模型要学的核心参数，θ=w，贝叶斯算的=梯度找的=正则约束的"),
    make_node("偏置(b) — 截距，wx+b中的b，控制起点"),
    make_node("损失函数 — 衡量预测ŷ与真实y的差距", [
        make_node("回归：MSE=Σ(ŷ-y)²/n（罚距离平方）、MAE=Σ|ŷ-y|/n（绝对值）"),
        make_node("分类：交叉熵=-[y·logŷ+(1-y)·log(1-ŷ)]（罚方向对不对）"),
    ]),
    make_node("正则化 — 防过拟合的约束项 = 贝叶斯先验的数学等价", [
        make_node("L2正则 = Ridge = λ·Σw² → w趋近0"),
        make_node("L1正则 = Lasso = λ·Σ|w| → 不重要w直接变0"),
    ]),
    make_node("梯度 — 损失函数对w的偏导数，指南针（指方向不说多远）"),
    make_node("学习率(lr) — 梯度下降的步长，最重要超参数"),
])

# 核心难题 → 补充正则化作为过拟合解决方案
henan = find_node(hexin_kids, "核心难题")
henan_kids = get_children(henan)
guonihe = find_node(henan_kids, "过拟合")
add_children(guonihe, [
    make_node("解决方案1：正则化 L1/L2 → 约束w大小"),
    make_node("解决方案2：更多数据 → 减少对噪音的拟合"),
    make_node("解决方案3：早停(Early Stopping) → 验证集误差不再降就停"),
    make_node("解决方案4：Dropout（深度学习）→ 随机关神经元"),
])

# 核心概念 → 新增 θ=w 统一理解
add_children(hexin, [
    make_node("θ=w 统一理解 — θ就是权重w：贝叶斯p(θ|X)求后验 = ML训练找最好w", [
        make_node("MLE(频率派)：只用似然p(X|θ)，数据说啥就是啥 → 损失=MSE"),
        make_node("MAP(贝叶斯)：p(X|θ)×p(θ)，数据+信念综合 → 损失=MSE+正则化"),
        make_node("贝叶斯→正则化链：高斯先验→L2/Ridge，拉普拉斯先验→L1/Lasso"),
    ]),
])

# ============================================================
# 2. 新增"模型五大派分类体系"
# ============================================================
root_children.append(make_node("模型五大派分类（按计算方式，不是按频率/贝叶斯）", [
    make_node("wx+b派（梯度下山） — 线性回归/逻辑回归/Ridge/Lasso/深度学习", [
        make_node("特点：有wx+b公式，损失函数求导，梯度下降迭代更新w"),
        make_node("深度学习 = wx+b + 多隐藏层 + 激活函数折弯"),
    ]),
    make_node("树派（贪心切蛋糕） — 决策树/随机森林/XGBoost/LightGBM", [
        make_node("特点：不用wx+b，不求导，暴力搜索最佳切分点"),
        make_node("用Gini(分类)/MSE(回归)衡量切的纯度"),
    ]),
    make_node("距离派（比邻居） — KNN", [
        make_node("特点：不训练，直接比距离（欧式/曼哈顿）"),
        make_node("必须标准化！因为特征间要互相比较"),
    ]),
    make_node("概率派（独立乘概率） — 朴素贝叶斯4种", [
        make_node("GaussianNB(连续正态)、MultinomialNB(计数)、BernoulliNB(0/1)、ComplementNB(不平衡)"),
        make_node("朴素=假设所有特征独立，P(特征1)×P(特征2)各算各的"),
    ]),
    make_node("边界派（找最大间隔） — SVM", [
        make_node("4核函数：linear(原空间)/poly(多项式)/rbf(无限维，默认)/sigmoid(几乎不用)"),
        make_node("感知机 = SVM 去掉最大间隔和核函数(1957→1990升级版)"),
    ]),
]))

# ============================================================
# 3. 新增"训练循环六步与五步框架"
# ============================================================
root_children.append(make_node("训练循环六步（所有模型的底盘）", [
    make_node("① 瞎猜 w,b → ② wx+b(+激活)算预测 ŷ → ③ 损失函数算错多少"),
    make_node("④ 梯度求方向(∂损失/∂w) → ⑤ w=w-lr×梯度 更新 → ⑥ 回到②"),
    make_node("sklearn：六步装进fit()一把梭 | PyTorch：亲手写每一步，loss.backward()只帮你自动求导"),
    make_node("深度学习 = 机器学习 + 多隐藏层。训练六步完全一样。"),
]))

root_children.append(make_node("ML五步标准框架", [
    make_node("第一步：选模型结构 — 线性→线性回归/逻辑回归，非线性→树/神经网络+激活函数"),
    make_node("第二步：定义损失函数 — 回归MSE/MAE，分类交叉熵"),
    make_node("第三步：加正则化（防过拟合）— L1/L2 = 贝叶斯先验，数学等价"),
    make_node("第四步：优化找最好w — 解析解(线性回归) or 梯度下降(lr控制步长)"),
    make_node("第五步：测试集评估泛化 — 回归看MSE/R²，分类看Accuracy/Recall/Precision/F1"),
]))

# ============================================================
# 4. 算法家族 → 补充深度学习
# ============================================================
suanfa = find_node(root_children, "算法家族")
suanfa_kids = get_children(suanfa)

add_children(suanfa, [
    make_node("深度学习（wx+b派升级版）", [
        make_node("隐藏层作用：逐层学抽象特征 — 像素→边角→形状→部件→整张脸"),
        make_node("激活函数：折弯直线让网络画任意形状", [
            make_node("ReLU(中间层默认)、Sigmoid(最后二分类)、Softmax(最后多分类)"),
            make_node("没激活→三层叠一起=一层，永远画直线"),
        ]),
        make_node("损失函数：只有最后一层有，中间层只折弯不打分"),
        make_node("PyTorch核心：loss.backward()自动求导，其余自己控制"),
        make_node("weight_decay = L2正则化的深度学习叫法", [
            make_node("optimizer = Adam(params, lr=0.001, weight_decay=1e-4)"),
        ]),
    ]),
])

# ============================================================
# 5. 算法家族 → 填充SVM/贝叶斯/KNN细节
# ============================================================

# SVM → 填充
svm_node = find_node(suanfa_kids, "支持向量机")
svm_kids = get_children(svm_node)

mubiao = find_node(svm_kids, "目标")
add_children(mubiao, [make_node("找最大间隔分类线，支撑向量=离分类线最近的点")])

hejiqiao = find_node(svm_kids, "核技巧")
add_children(hejiqiao, [
    make_node("linear：原空间不动（线性可分）"),
    make_node("poly：多项式升维（知道大概几阶）"),
    make_node("rbf：升到无限维（默认首选，不知道什么形状先试它）"),
    make_node("sigmoid：模拟神经网络（几乎不用）"),
])

tedian = find_node(svm_kids, "特点")
add_children(tedian, [
    make_node("软间隔(C控制)：允许几个点越界，C大=罚狠=硬"),
    make_node("不适合：10万+条(太慢)、需要解释(黑盒)"),
    make_node("必须标准化！算间隔距离"),
    make_node("感知机 = SVM 去最大化间隔+核函数 → 升级版"),
])

# 朴素贝叶斯 → 填充
beiyesi = find_node(suanfa_kids, "贝叶斯方法")
by_kids = get_children(beiyesi)
pusu = find_node(by_kids, "朴素贝叶斯")
pusu_kids = get_children(pusu)

hexin_by = find_node(pusu_kids, "核心")
add_children(hexin_by, [make_node("朴素=假设所有特征互相独立 P(特征1)×P(特征2)各算各的")])

bianti = find_node(pusu_kids, "变体")
add_children(bianti, [
    make_node("GaussianNB：连续数据，正态分布（身高/成绩/价格）"),
    make_node("MultinomialNB：计数数据（词频统计）"),
    make_node("BernoulliNB：0/1数据（词出现/不出现）"),
    make_node("ComplementNB：不平衡文本改进版"),
])

# 贝叶斯方法 → 新增先验→正则化
add_children(beiyesi, [
    make_node("贝叶斯→正则化推导链", [
        make_node("MAP：p(θ|X) ∝ p(X|θ)×p(θ) → -log后 ∝ MSE + (-log先验)"),
        make_node("高斯先验 N(0,σ²) → -log = w²/(2σ²) → L2正则(=Ridge)"),
        make_node("拉普拉斯先验 → -log = |w| → L1正则(=Lasso)"),
        make_node("均匀先验(常数) → -log = 常数 → 无正则化(=MLE)"),
        make_node("正则化 ≠ 贝叶斯独有：频率派也用L1/L2防过拟合，殊途同归"),
    ]),
    make_node("Ridge vs BayesianRidge", [
        make_node("Ridge(频率派)：算出w=3.2一个数，λ手动调，秒级"),
        make_node("BayesianRidge(贝叶斯)：算出w概率分布±置信度，λ自动学，慢百倍"),
        make_node("工业界99%用Ridge：性价比；医疗/金融才用BayesianRidge：要置信度"),
    ]),
])

# KNN → 填充
knn_node = find_node(suanfa_kids, "K近邻")
knn_kids = get_children(knn_node)

knntedian = find_node(knn_kids, "特点")
add_children(knntedian, [
    make_node("唯一不训练的模型！直接比距离"),
    make_node("必须标准化（特征尺度不同→距离无意义）"),
])

juli = find_node(knn_kids, "距离度量")
add_children(juli, [
    make_node("欧氏距离：直线距离，最常用"),
    make_node("曼哈顿距离：街区距离，高维有时更好"),
])

kzhi = find_node(knn_kids, "K值选择")
add_children(kzhi, [
    make_node("K太小 → 过拟合(噪音敏感)"),
    make_node("K太大 → 欠拟合(太粗糙)"),
    make_node("用for循环试K值，画准确率曲线找最优"),
])

# 线性模型 → 补充正则化回归节点
xianxing = find_node(suanfa_kids, "线性模型")
xx_kids = get_children(xianxing)
zhengzehua = find_node(xx_kids, "正则化回归")
zhengzehua_kids = get_children(zhengzehua)

add_children(zhengzehua, [
    make_node("L1/L2 与损失函数的区别", [
        make_node("MSE(平方)罚预测误差 → 让预测ŷ接近真实y"),
        make_node("L2(平方)罚权重w → 让w趋近0"),
        make_node("数学都是²，但作用对象不同！"),
    ]),
    make_node("L1/L2 与贝叶斯先验对应", [
        make_node("L2=Ridge ↔ 高斯先验N(0,σ²)"),
        make_node("L1=Lasso ↔ 拉普拉斯先验"),
    ]),
    make_node("需要正则化的场景：特征多或相关 → 保命；特征少数据多 → 不需要"),
])

# ============================================================
# 6. 标准工作流程 → 补充评估指标细节 + 标准化决策树
# ============================================================
liucheng = find_node(root_children, "标准工作流程")
liucheng_kids = get_children(liucheng)

# 补充数据预处理 → 特征缩放中的标准化决策逻辑
yuchuli = find_node(liucheng_kids, "数据预处理")
yuchuli_kids = get_children(yuchuli)
tesuofang = find_node(yuchuli_kids, "特征缩放")
add_children(tesuofang, [
    make_node("标准化决策：两个特征凑一起运算→需要；各算各的→不需要", [
        make_node("需要：KNN(算距离)、SVM(算间隔)、神经网络(梯度步长)"),
        make_node("不需要：决策树/随机森林(只看阈值)、朴素贝叶斯(独立乘概率)"),
    ]),
])

# 模型评估 → 分类指标 → 补充公式和场景
pinggu = find_node(liucheng_kids, "模型评估")
pinggu_kids = get_children(pinggu)
fenlei = find_node(pinggu_kids, "分类指标")
fenlei_kids = get_children(fenlei)

# 准确率补充
zhunquelv = find_node(fenlei_kids, "准确率")
add_children(zhunquelv, [
    make_node("Accuracy=(TP+TN)/All — 全对÷全量，笼统"),
])

# 精确率补充
jingquelv = find_node(fenlei_kids, "精确率")
add_children(jingquelv, [
    make_node("Precision=TP/(TP+FP) — 喊Yes对几个，分母含FP虚惊"),
    make_node("高Precision→少误报：垃圾邮件过滤"),
])

# 召回率补充
zhaohuilv = find_node(fenlei_kids, "召回率")
add_children(zhaohuilv, [
    make_node("Recall=TP/(TP+FN) — 真Yes抓到几个，分母含FN漏的"),
    make_node("高Recall→少漏：疾病筛查、用户流失预测"),
    make_node("⚠️易错：分母是TP+FN(不是TN)，和Precision的FP区分"),
])

# F1补充
f1_node = find_node(fenlei_kids, "F1分数")
add_children(f1_node, [
    make_node("F1=2PR/(P+R) — P和R都高F1才高，调和平均"),
])

# AUC补充
auc_node = find_node(fenlei_kids, "AUC-ROC")
add_children(auc_node, [
    make_node("ROC曲线下面积，0.5=乱猜，1.0=完美"),
])

# 回归指标补充
huigui = find_node(pinggu_kids, "回归指标")
huigui_kids = get_children(huigui)
mse_node = find_node(huigui_kids, "均方误差")
add_children(mse_node, [
    make_node("MSE=(1/n)Σ(ŷ-y)² — 罚距离平方，大错重罚，对离群点敏感"),
    make_node("MAE=(1/n)Σ|ŷ-y| — 罚距离绝对值，不理离群点"),
])

r2_node = find_node(huigui_kids, "决定系数")
add_children(r2_node, [
    make_node("R²衡量模型比瞎猜均值好多少，1=完美，0=跟均值一样烂"),
])

# 新增：模型评估 → 场景决策表
add_children(pinggu, [
    make_node("指标选型场景", [
        make_node("挽留用户→优先Recall（漏一个丢钱）"),
        make_node("垃圾邮件→优先Precision（误删重要邮件严重）"),
        make_node("疾病筛查→优先Recall（漏诊命没了）"),
        make_node("精准广告→优先Precision（乱推只烦人）"),
    ]),
])

# 模型训练 → 补充梯度下降细节
xunlian = find_node(liucheng_kids, "模型训练")
add_children(xunlian, [
    make_node("梯度下降本质", [
        make_node("损失函数=海拔地图 | 梯度=斜率=方向 | 梯度=0→谷底→停下"),
        make_node("w_new = w_old - lr × 梯度 → 反复走到梯度≈0"),
        make_node("lr太小→慢；lr太大→震荡/跳过最优"),
    ]),
])

# ============================================================
# 7. 新增独立分支"标准化决策树" + "分类四指标速查"
# ============================================================
root_children.append(make_node("标准化完整决策", [
    make_node("需要标准化(特征互相比较)：KNN、SVM、神经网络、逻辑回归"),
    make_node("不需要(各算各的)：决策树/随机森林(只看阈值)、朴素贝叶斯(独立概率)"),
    make_node("判断口诀：两个特征凑一起运算→标准化；各玩各的→不用"),
    make_node("反例：年龄0-100 vs 收入3万-5万，KNN距离被收入主导，树只看自己阈值不受影响"),
]))

root_children.append(make_node("损失函数三人对比速查", [
    make_node("MSE=Σ(ŷ-y)²/n → 平方罚距离，大错重罚，对离群点敏感 → 线性回归"),
    make_node("MAE=Σ|ŷ-y|/n → 绝对值罚距离，不理离群点，梯度固定 → 数据有离群点"),
    make_node("交叉熵=-[y·logŷ+(1-y)·log(1-ŷ)] → 罚方向对不对，猜反往死里罚 → 分类用"),
    make_node("| | 罚什么 | 敏感离群点 | 用在哪 |"),
]))

# ============================================================
# 8. 补充"正则化 vs 贝叶斯先验"对照表
# ============================================================
root_children.append(make_node("先验分布→正则化速查", [
    make_node("均匀分布(常数)→log p(θ)=0 → 无正则化 → MLE"),
    make_node("高斯分布N(0,σ²)→log p(θ)=-θ²/(2σ²) → L2正则 → Ridge（w趋近0）"),
    make_node("拉普拉斯分布→log p(θ)=-|θ| → L1正则 → Lasso（不重要w直接变0）"),
    make_node("先验 = 起点（你信什么），后验 = 终点（训练把你从先验拽到后验）"),
]))

# ============================================================
# 保存增强后的JSON
# ============================================================
output_path = "c:/Project/python/tmp_xmind/content_enhanced.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 用增强后的JSON替换原content.json，重新打包为XMind
os.remove("c:/Project/python/tmp_xmind/content.json")
os.rename(output_path, "c:/Project/python/tmp_xmind/content.json")

xmind_output = "c:/Project/python/tmp_xmind/机器学习_增强版.xmind"
# 删除旧包（如果存在）
if os.path.exists(xmind_output):
    os.remove(xmind_output)

with zipfile.ZipFile(xmind_output, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root_dir, dirs, files in os.walk("c:/Project/python/tmp_xmind"):
        for file in files:
            if file.endswith('.xmind'):
                continue
            full_path = os.path.join(root_dir, file)
            arcname = os.path.relpath(full_path, "c:/Project/python/tmp_xmind")
            zf.write(full_path, arcname)

print(f"XMind增强版已生成: {xmind_output}")
