# Week 7：前半学期复习与模拟练习

## 实验内容

本周主要复习前半学期内容，包括 ROS2 基本命令、Python 节点编程、机器人运动学、传感器、RViz 和 PID 控制。

---

## 1. ROS2 常用命令复习

启动 turtlesim：

`ros2 run turtlesim turtlesim_node`

查看节点：

`ros2 node list`

查看话题：

`ros2 topic list`

监听位置：

`ros2 topic echo /turtle1/pose`

发布速度命令：

`ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0}, angular: {z: 0.0}}"`

---

## 2. Python 节点练习

本周练习使用 Python 程序控制小乌龟走正方形。

运行命令：

`python3 square_review.py`

---

## 3. 运动学计算

已知左轮速度 0.5m/s，右轮速度 1.5m/s，轮间距 0.5m。

线速度：

v = (0.5 + 1.5) / 2 = 1.0 m/s

角速度：

ω = (1.5 - 0.5) / 0.5 = 2.0 rad/s

---

## 4. PID 控制复习

P：比例控制，根据当前误差调整输出。  
I：积分控制，根据历史误差累积进行修正。  
D：微分控制，根据误差变化速度进行调整，可以减少震荡。

---

## 实验截图

### Python 程序运行




---

## 总结

通过本周复习，我重新整理了 ROS2 基础命令、Python 节点控制、运动学计算和 PID 控制的基本知识。

## 实验截图



### 小乌龟正方形轨迹

![正方形轨迹](img/square_result.png)
