# Week 12：手机摄像头、ArUco 识别与距离估算实验

## 一、实验基本信息

- **课程**：AI Robotics
- **主题**：手机摄像头输入、ArUco 标记识别、距离估算
- **实验工具**：Python 3、OpenCV、ArUco

---

## 二、实验目标

本周实验主要围绕机器人视觉展开，目标是理解机器人如何通过摄像头识别视觉标记（ArUco），并进一步估算目标与摄像头之间的距离。

本次实验完成内容：

1. 使用 OpenCV 生成 ArUco 标记
2. 使用 `DICT_4X4_50` 字典识别 ArUco
3. 成功识别课堂要求的 ArUco ID 6
4. 根据标记像素宽度估算距离
5. 保存识别结果图和距离估算图

---

## 三、实验原理

### 1. ArUco 标记

ArUco 是一种常用于机器人视觉定位的黑白方形标记。每个标记都有唯一 ID，机器人可以通过摄像头识别 ID 和角点位置，用于定位、导航和增强现实等场景。

在本实验中，我使用的标记参数：

- 字典：`DICT_4X4_50`
- 标记 ID：`6`
- 标记实际尺寸：5 cm × 5 cm

### 2. ArUco 识别流程

ArUco 识别过程主要包括以下步骤：

1. **输入图像** — 从摄像头或文件读取图像
2. **转换为灰度图** — 降低计算复杂度
3. **检测候选方形区域** — 查找图像中的四边形候选区
4. **解码 ArUco ID** — 通过字典匹配确认标记 ID
5. **绘制检测框和 ID 信息** — 在原始图像上标注识别结果

### 3. 距离估算方法

当已知 ArUco 标记的实际宽度时，可以通过图像中的像素宽度估算距离。

基本公式：

```
距离 = 实际宽度 × 焦距 / 图像中的像素宽度
```

其中：
- `实际宽度`：ArUco 标记的真实尺寸（本实验为 0.05 m）
- `焦距`：摄像头像素焦距（本实验设为 700 px）
- `像素宽度`：图像中标记的像素宽度（由角点坐标计算）

---

## 四、代码实现 (`aruco_generate_detect.py`)

```python
import cv2
import numpy as np
import math
import os

os.makedirs("img", exist_ok=True)

print("Week 12：ArUco ID 6 生成、识别与距离估算")
print("----------------------------------------")

# 使用课堂常见的 4x4 字典
aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# 生成 ID 6 的 ArUco 标记
marker_id = 6
marker_size = 300

if hasattr(aruco, "generateImageMarker"):
    marker_img = aruco.generateImageMarker(dictionary, marker_id, marker_size)
else:
    marker_img = aruco.drawMarker(dictionary, marker_id, marker_size)

# 放到白色画布上，方便检测
canvas = np.ones((500, 600), dtype=np.uint8) * 255
canvas[100:400, 150:450] = marker_img

# 转成彩色图用于绘制结果
color_img = cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)

# 兼容不同 OpenCV 版本的检测写法
if hasattr(aruco, "ArucoDetector"):
    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(dictionary, parameters)
    corners, ids, rejected = detector.detectMarkers(canvas)
else:
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejected = aruco.detectMarkers(
        canvas, dictionary, parameters=parameters
    )

detected_img = color_img.copy()

if ids is not None:
    aruco.drawDetectedMarkers(detected_img, corners, ids)

    for i, detected_id in enumerate(ids.flatten()):
        pts = corners[i][0]

        # 计算图像中标记的像素宽度
        edge1 = np.linalg.norm(pts[0] - pts[1])
        edge2 = np.linalg.norm(pts[2] - pts[3])
        pixel_width = (edge1 + edge2) / 2

        # 简单距离估算：距离 = 实际宽度 × 焦距 / 像素宽度
        real_marker_size_m = 0.05
        focal_length_px = 700
        distance_m = real_marker_size_m * focal_length_px / pixel_width

        cv2.putText(
            detected_img,
            f"ID: {detected_id}",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.putText(
            detected_img,
            f"Distance: {distance_m:.2f} m",
            (30, 85),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 128, 0),
            2
        )

        print(f"识别成功：ArUco ID = {detected_id}")
        print(f"像素宽度：{pixel_width:.2f} px")
        print(f"估算距离：{distance_m:.2f} m")
else:
    print("未识别到 ArUco 标记")

# 保存结果图
cv2.imwrite("img/aruco_detect.png", detected_img)
cv2.imwrite("img/distance_demo.png", detected_img)

print("----------------------------------------")
print("已生成：img/aruco_detect.png")
print("已生成：img/distance_demo.png")
print("程序结束")
```

运行命令：

```bash
python3 aruco_generate_detect.py
```

---

## 五、实验结果与分析

程序成功生成了 ArUco ID 6 标记并进行了识别和距离估算。识别结果在图像上标注了标记 ID 和估算距离，验证了 ArUco 标记作为机器人视觉定位手段的可行性。

距离估算的精度受以下因素影响：
- 标记实际尺寸的测量精度
- 摄像头焦距的标定精度
- 图像中角点检测的精度

---

## 六、实验截图

### 1. ArUco ID 6 识别结果

![ArUco识别结果](img/aruco_detect.png)

### 2. 距离估算结果

![距离估算结果](img/distance_demo.png)

