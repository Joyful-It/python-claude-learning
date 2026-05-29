import cv2
#版本号  print("ban ben hao :",cv2.__version__)

data1=cv2.imread("C:/project/python/openCV/OIP.jpg")
# 打印 图片信息 print(data1)

print("=================灰图=====================")
data2=cv2.imread("C:/project/python/openCV/OIP.jpg",cv2.IMREAD_GRAYSCALE)
print(data2)
cv2.imshow("girl",data2)
cv2.waitKey(0)
print(data2.shape)
print(data1.dtype)