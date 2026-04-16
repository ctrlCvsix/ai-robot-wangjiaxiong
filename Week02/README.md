# Week 01：Ubuntu 24.04 环境搭建与 ROS2 初探

## 1. 实验目标
- 在本地设备上安装并配置 Ubuntu 24.04 操作系统。
- 完成 ROS2 (Jazzy/Humble) 的环境安装。
- 通过运行经典的“小乌龟” (Turtlesim) 案例，验证 ROS2 环境的完整性并学习基本的节点通信。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **机器人框架**: ROS2 (Jazzy Jalisco)
- **开发工具**: VS Code, Terminal

## 3. 实验步骤与内容

### 3.1 环境安装
按照官方文档配置了软件源，并安装了 `ros-desktop` 核心组件。设置了环境变量：
```bash
source /opt/ros/jazzy/setup.bash