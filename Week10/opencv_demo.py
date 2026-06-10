import cv2
import numpy as np

print("Week 10：OpenCV 图像处理实验")
print("--------------------------------")

# 创建一张简单图片
img = np.zeros((300, 300, 3), dtype=np.uint8)

# 绘制图形和文字
cv2.rectangle(img, (60, 60), (240, 240), (0, 255, 0), 3)
cv2.circle(img, (150, 150), 50, (255, 0, 0), -1)
cv2.putText(img, "OpenCV", (70, 280), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(gray, 100, 200)

# 保存结果
cv2.imwrite("opencv_result.png", edges)

print("已生成图像处理结果：opencv_result.png")
print("实验完成")
