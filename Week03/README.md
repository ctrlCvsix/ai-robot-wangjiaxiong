# Week 03：ROS 2 话题通信与小乌龟路径控制

## 1. 实验目标
- 深入理解 ROS 2 的话题 (Topic) 通信机制。
- 学习如何通过终端命令行手动发布消息（ros2 topic pub）。
- 观察并分析 `geometry_msgs/msg/Twist` 消息结构对机器人运动的影响。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **机器人框架**: ROS 2 (Jazzy/Humble)
- **核心概念**: 话题发布者 (Publisher)、消息类型 (Twist)

## 3. 实验内容与步骤

### 3.1 启动仿真环境
首先启动小乌龟仿真节点：
```bash
ros2 run turtlesim turtlesim_node