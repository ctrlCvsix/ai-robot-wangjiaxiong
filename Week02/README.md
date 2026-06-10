# Week 02 — Ubuntu 与 ROS2 环境搭建

## 实验目标

搭建 Ubuntu 与 ROS2 基础环境，并通过 turtlesim 验证安装是否成功。

## 目录结构

<pre>
Week02/
|-- README.md              # 周实验报告
|-- images/                # 环境搭建截图
</pre>

## 实验环境

- Ubuntu 24.04 LTS
- ROS2 Jazzy / Humble
- 终端
- VS Code

## 实验流程

1. 准备 Ubuntu 与 ROS2 软件包。
2. 加载 ROS2 环境配置脚本。
3. 启动 turtlesim 验证环境是否就绪。

## 命令

<pre><code class="language-bash">
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node
</code></pre>

## 实验证据

<img src="images/xiaowugui.png" width="800" alt="ROS2 turtlesim 环境搭建证据">

## 总结与反思

稳定的 ROS2 环境是后续所有机器人实验的首要前提。

---

[返回实验导航](../README.md)
