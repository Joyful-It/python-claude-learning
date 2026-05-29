import ultralytics
from ultralytics import YOLO
print("numer:",ultralytics.__version__)

model=YOLO("yolov8n.pt") #创建模型对象
print(model)
r1=model("openCV/OIP.jpg")#加载图片，做目标检测
r1[0].save(filename='yologril.jpg')

