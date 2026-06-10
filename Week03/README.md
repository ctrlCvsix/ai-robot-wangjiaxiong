# Week 03 — ROS2 话题通信

## 实验目标

通过 ROS2 话题发布控制 turtlesim，展示 Twist 消息如何影响小乌龟的运动。

## 目录结构

<pre>
Week03/
|-- README.md              # 周实验报告
|-- images/                # 运动截图
</pre>

## 实验环境

- ROS2
- turtlesim
- geometry_msgs/msg/Twist

## 实验流程

1. 启动 turtlesim。
2. 发布速度指令。
3. 记录运动结果。

## 命令

<pre><code class="language-bash">
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
</code></pre>

## 实验证据

<img src="images/dawugui.png" width="800" alt="ROS2 话题控制证据">

## 总结与反思

话题发布是测试机器人指令流的一种简单而强大的方式。

---

[返回实验导航](../README.md)
