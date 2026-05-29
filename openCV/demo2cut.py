import cv2

# 1. 读取图片：返回 numpy 数组，shape=[高, 宽, 3(BGR三通道)]
data1 = cv2.imread("openCV/OIP.jpg")

# 2. 加载 OpenCV 预训练的人脸检测模型（Haar 级联分类器）
#    cv2.data.haarcascades = OpenCV 安装目录下存放预训练 xml 的路径
#    haarcascade_frontalface_default.xml = 正面人脸检测模型
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
#    创建级联分类器对象，加载 xml 里的训练好的特征规则

# 3. 转灰度图：BGR(3通道) → Gray(1通道)
#    人脸检测不关心颜色，只关心明暗轮廓，灰度图计算量更小
gray = cv2.cvtColor(data1, cv2.COLOR_BGR2GRAY)

# 4. 多尺度人脸检测 —— 核心操作
#    scaleFactor=1.1: 每次把图像缩小 10%，在不同尺度下找脸（小图找大脸，大图找小脸）
#    minNeighbors=5: 每个候选区域至少被 5 个重叠框确认才算人脸（值越大误检越少，但可能漏检）
#    返回值：list of (x, y, w, h)，每张脸的左上角坐标 + 宽高
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f"检测到 {len(faces)} 张人脸")

# 5. 遍历每一张检测到的人脸
for i, (x, y, w, h) in enumerate(faces):
    # 5a. 在原图上画绿色矩形框（BGR: 0=蓝, 255=绿, 0=红）
    #     参数：图片, 左上角, 右下角, 颜色, 线宽
    cv2.rectangle(data1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 5b. NumPy 切片裁剪人脸区域
    #     图片[行起始:行结束, 列起始:列结束]
    #     y:y+h = 垂直方向从头顶到下巴
    #     x:x+w = 水平方向从脸左边到右边
    face_crop = data1[y:y + h, x:x + w]

    # 5c. 显示裁剪出的人脸，"face_0"、"face_1"...
    cv2.imshow(f"face_{i}", face_crop)

# 6. 显示带检测框的原图
cv2.imshow("face_detected", data1)

# 7. waitKey(0): 等待按键（0=无限等待），不写这行窗口会一闪而过
cv2.waitKey(0)

# 8. 关闭所有 OpenCV 窗口，释放资源
cv2.destroyAllWindows()
