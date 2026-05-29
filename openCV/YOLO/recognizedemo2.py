"""
YOLOv8 实时摄像头检测 —— 统计画面中的人数
流程骨架（背这 5 步）：
  ① 加载模型      YOLO("模型文件").to(设备)
  ② 打开摄像头     cv2.VideoCapture(0)
  ③ 循环读帧      cap.read() → frame
  ④ 模型检测      model(frame) → 遍历结果画框
  ⑤ 显示 + 按键   cv2.imshow + cv2.waitKey
"""
import cv2
import torch
from ultralytics import YOLO
import datetime

# ==================== ① 加载模型 ====================
# device：有 GPU 用 GPU，没有用 CPU（你电脑只有核显，走 CPU）
device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
# YOLO("yolov8n.pt")：加载预训练模型（n=nano，最小最快，6MB）
# .to(device)：把模型权重搬到指定设备
model = YOLO("yolov8n.pt").to(device)
print("使用设备：", device)

# ==================== ② 打开摄像头 ====================
# VideoCapture(0)：0 = 默认摄像头（笔记本自带的前置），外接可能用 1
cap = cv2.VideoCapture(0)

# isOpened()：检查摄像头是否成功打开
if not cap.isOpened():
    print("摄像头无法打开")
    exit()

print("摄像头已开启。按 q 退出，按 s 截图")

# ==================== ③ 主循环：逐帧读取 + 检测 + 显示 ====================
while True:
    # cap.read() 返回两个值：
    #   ret  = True/False（是否成功读到帧）
    #   frame = numpy 数组 [高, 宽, 3]（BGR 格式）
    ret, frame = cap.read()
    if not ret:
        print("无法读取画面")
        break

    # ========== ④ 模型检测 ==========
    # model(frame)：输入一帧图像，YOLO 自动检测所有物体
    #   stream=True：流式模式，不缓存，摄像头实时用
    #   verbose=False：不在终端打印检测日志（画面够用了）
    results = model(frame, stream=True, verbose=False)

    person_count = 0  # 本帧人数计数器

    # results 是列表，每张图一个结果（这里一次只送一帧，所以只有一个 result）
    for result in results:
        boxes = result.boxes  # 所有检测到的边界框

        for box in boxes:
            # --- 解析每个框的信息 ---
            # box.xyxy[0]：边界框坐标 [x1, y1, x2, y2]（左上角 + 右下角）
            # map(int, ...)：坐标转整数（像素没有小数）
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # box.conf[0]：置信度（0~1，模型觉得"这确实是个物体"的程度）
            conf = float(box.conf[0])

            # box.cls[0]：类别编号（0=人, 39=瓶子, ... 共 80 类 COCO 数据集）
            cls_id = int(box.cls[0])

            # model.names：字典 {0: 'person', 1: 'bicycle', ...}
            cls_name = model.names[cls_id]

            # --- 只统计人，置信度 > 0.5 才算 ---
            # cls_id == 0：COCO 数据集中 0 号类别是 person（人）
            # conf > 0.5：模型至少 50% 确定是人，太低可能是误检
            if cls_id == 0 and conf > 0.5:
                person_count += 1
                # 画框：绿色 (0, 255, 0)，线宽 2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # 在框上方写标签："person 0.85"
                label = f'{cls_name} {conf:.2f}'
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # --- 左上角显示总人数 ---
    info_text = f'persons: {person_count}'
    cv2.putText(frame, info_text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # ========== ⑤ 显示画面 ==========
    cv2.imshow('YOLOv8 Real-time Detection', frame)

    # waitKey(1)：等待 1ms，同时捕获按键
    # & 0xFF：取低 8 位（兼容 64 位系统）
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # 按 s → 截图保存
        fn = datetime.datetime.now().strftime('%y%m%d%H%M%S') + '_screenshot.jpg'
        cv2.imwrite('openCV/' + fn, frame)
        print(f"截图已保存: {fn}")
    if key == ord('q'):  # 按 q → 退出循环
        break

# ==================== 清理 ====================
cap.release()            # 释放摄像头
cv2.destroyAllWindows()  # 关闭所有 OpenCV 窗口
