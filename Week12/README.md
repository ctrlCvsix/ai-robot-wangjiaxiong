# Week 12 — 手机摄像头、ArUco 识别与距离估算

## 实验目标

通过 OpenCV 和 ArUco 库，完成视觉标记的生成、识别与距离估算，理解机器人视觉定位的基本原理。

本次实验完成内容：

1. 生成自定义 ArUco 标记（DICT_4X4_50，ID 6）
2. 识别图像中的 ArUco 标记并标注 ID
3. 根据像素宽度估算标记与摄像头的实际距离
4. 保存识别结果和距离估算截图

## 实验环境

| 组件 | 说明 |
|------|------|
| 编程语言 | Python 3 |
| 视觉库 | OpenCV (cv2.aruco) |
| 标记字典 | DICT_4X4_50 |
| 标记 ID | 6 |
| 标记尺寸 | 5 cm × 5 cm |

## 实验原理

### ArUco 标记

ArUco 是一种黑白方形基准标记，广泛应用于机器人视觉定位。每个标记有唯一 ID，摄像头通过检测角点和解码内部编码来识别。

### 识别流程

```
输入图像 → 灰度转换 → 四边形检测 → 字典匹配 → 输出 ID + 角点
```

### 距离估算

基于相似三角形原理：

```
距离 = 实际宽度 × 焦距 / 像素宽度
```

| 参数 | 值 | 说明 |
|------|-----|------|
| 实际宽度 | 0.05 m | ArUco 标记真实尺寸 |
| 焦距 | 700 px | 摄像头像素焦距（估算值） |
| 像素宽度 | 由角点计算 | 图像中检测到的标记宽度 |

## 目录结构

```
Week12/
├── README.md                    # 本报告
├── aruco_generate_detect.py     # ArUco 生成、识别与距离估算程序
└── img/
    ├── aruco_detect.png         # ArUco ID 6 识别结果
    └── distance_demo.png        # 距离估算标注结果
```

## 实验步骤

### 1. 生成 ArUco 标记

使用 `DICT_4X4_50` 字典生成 ID 为 6 的 ArUco 标记，输出为 300×300 像素的黑白图像。

### 2. 识别标记

将标记放置在白色画布上，调用 `detectMarkers` 检测角点和 ID，确认是否正确识别。

### 3. 距离估算

从识别到的四个角点计算标记的像素宽度，结合已知的实际宽度和估算焦距，推算出标记与摄像头的距离。

## 关键命令

```bash
# 安装依赖
pip install opencv-python numpy

# 运行 ArUco 生成与检测程序
python3 aruco_generate_detect.py
```

## 代码核心逻辑

```python
# 生成标记
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
marker_img = aruco.generateImageMarker(dictionary, marker_id=6, marker_size=300)

# 识别标记
corners, ids, rejected = detector.detectMarkers(canvas)

# 距离估算
pixel_width = (edge1 + edge2) / 2
distance_m = real_marker_size_m * focal_length_px / pixel_width  # 0.05 * 700 / pixel_width
```

## 实验证据

<img src="img/aruco_detect.png" width="800" alt="ArUco ID 6 识别结果">

*程序生成的 ArUco ID 6 标记识别结果*

<img src="img/distance_demo.png" width="800" alt="距离估算标注">

*距离估算数值标注在检测框上方*

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| OpenCV 版本兼容性 | 新版 OpenCV 使用 `ArucoDetector` 类，旧版使用 `detectMarkers` 函数 | 使用 `hasattr` 判断版本，分别实现两种调用方式 |
| 距离估算偏差较大 | 焦距参数 700 为粗略估算值，未经过标定 | 可通过标准棋盘格标定获得更精确的焦距值 |
| 低光照下识别率下降 | ArUco 依赖清晰的边缘检测 | 确保充足光照，或增大标记尺寸提高对比度 |

## 总结与反思

### 核心收获

1. **视觉定位原理**：通过已知尺寸的标记和单目摄像头即可估算距离，这是机器人定位的基础技术。公式 `距离 = 实际尺寸 × 焦距 / 像素尺寸` 简洁但实用
2. **ArUco 的优势**：相比 QR 码，ArUco 专为机器视觉优化——边框清晰、角度鲁棒、可同时识别多个标记
3. **工程兼容性**：OpenCV 不同版本的 API 差异较大，编写兼容代码是工程实践的重要环节

### 延伸思考

距离估算的精度高度依赖摄像头标定精度。在后续项目中（如机器人抓取），可以：
- 使用 ChArUco 棋盘进行更精确的相机标定
- 结合多个 ArUco 标记进行位姿估计（PnP 算法）
- 融合 IMU 数据进行多传感器定位

---

[返回实验导航](../README.md)
