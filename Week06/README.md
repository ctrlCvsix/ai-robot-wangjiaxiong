# Week 06：ROS2 Kitti 数据集发布与 Rviz2 可视化

## 1. 实验目标
- 学习如何在 ROS2 环境下读取并解析自动驾驶数据集（Kitti）。
- 编写发布者节点，将点云数据（PointCloud2）和图像数据（Image）发布到对应的 Topic。
- 使用 Rviz2 和 RQT 进行多传感器数据的同步可视化。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **机器人框架**: ROS2 (Jazzy/Humble)
- **数据集**: Kitti Raw Dataset
- **工具**: RViz2, RQT

## 3. 实验内容与步骤

### 3.1 数据准备
将 Kitti 数据集存放于 `~/ros2_ws/data` 路径下，包含点云二进制文件和相机图像。

### 3.2 节点运行
通过自定义的 `ros2_kitti_publishers` 扩展包运行发布节点：
```bash
ros2 run ros2_kitti_publishers publisher_node