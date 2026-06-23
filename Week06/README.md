# Week 06 — KITTI 数据发布与 RViz2 可视化

## 实验目标

使用 ROS2 发布 KITTI 自动驾驶数据集，在 RViz2 与 RQT 中可视化点云和图像数据，理解传感器数据在 ROS2 中的标准发布方式。

## 实验环境

| 组件 | 说明 |
|------|------|
| 中间件 | ROS2 Humble |
| 数据集 | KITTI（点云 + 图像） |
| 可视化 | RViz2（3D 渲染）、RQT（话题监控） |
| 发布节点 | `ros2_kitti_publishers` |

## 目录结构

```
Week06/
├── README.md            # 本报告
├── avoidance_flow.png   # 避障流程图
├── avoidance_run.png    # 避障运行截图
└── zidongjiashi.png     # KITTI 可视化证据
```

## 实验步骤

### 1. 准备 KITTI 数据

下载或使用课程提供的 KITTI 数据集子集，包含激光雷达点云和相机图像。

### 2. 运行发布节点

启动 KITTI 数据发布节点，将数据集以标准 ROS2 消息格式发布到话题上：

```bash
ros2 run ros2_kitti_publishers publisher_node
```

### 3. RViz2 可视化

打开 RViz2，订阅点云和图像话题，配置显示面板观察 3D 场景：

```bash
rviz2
```

### 4. RQT 监控

使用 RQT 查看话题列表和消息频率，验证数据发布状态：

```bash
rqt
```

### 5. 避障流程分析

基于传感器数据设计简单的避障逻辑：读取 LiDAR 扫描 → 判断前方障碍物距离 → 决策转向或停止。

## 关键命令

```bash
# 启动 KITTI 发布节点
ros2 run ros2_kitti_publishers publisher_node

# 启动 RViz2
rviz2

# 查看话题列表
ros2 topic list

# 查看点云消息频率
ros2 topic hz /kitti/velo/pointcloud
```

## 实验证据

### KITTI 可视化

<img src="images/zidongjiashi.png" width="800" alt="KITTI RViz2 可视化">
n<img src="images&zidongjiashi.png" width="800" alt="KITTI RViz2 可视化">
n<img src="images&zidongjiashi.png" width="800" alt="KITTI RViz2 可视化">
n<img src="images&zidongjiashi.png" width="800" alt="KITTI RViz2 可视化">

*KITTI 数据集在 RViz2 中成功渲染，点云和图像同步显示*

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| RViz2 中无点云显示 | 未正确设置 Fixed Frame | 将 Global Options → Fixed Frame 设置为 `velodyne` |
| 话题有数据但频率很低 | 数据集较大，节点处理速度不足 | 减小发布的数据量或使用 `--rate` 参数调节 |
| KITTI 路径配置错误 | 数据集路径与代码中硬编码不一致 | 修改 launch 文件中的 `data_path` 参数 |
| RQT 无法连接 | ROS_DOMAIN_ID 不匹配 | 确认终端中 `echo $ROS_DOMAIN_ID` 与节点一致 |

## 总结与反思

### 核心收获

1. **传感器数据标准化**：ROS2 使用 `sensor_msgs` 统一封装 LiDAR、相机、IMU 等传感器数据，屏蔽了硬件差异
2. **可视化即调试**：RViz2 不仅是展示工具，更是调试利器——数据是否正确发布、坐标系是否对齐，一眼可辨
3. **避障逻辑基础**：LiDAR → 距离判断 → 转向决策，是最简单的自主导航闭环，后续 Week13 的迷宫探索正是其延伸

### 延伸思考

KITTI 是自动驾驶领域的标准数据集。通过 ROS2 发布 KITTI 数据，可以在不拥有真实车辆的情况下，用公开数据测试和验证感知算法。这种"公开数据集 + 仿真验证"的研发模式，在机器人行业中被广泛使用。

---

[返回实验导航](../README.md)
