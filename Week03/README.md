# Week 03 - ROS2 话题通信与小乌龟控制

## 1. 作业说明

本周练习 ROS2 Topic 通信，并通过 Twist 消息控制 turtlesim。

## 2. 文件结构

<pre>
Week03/
|-- README.md              # 必须
|-- images/                # 截图、效果图
</pre>

## 3. 实验环境

- ROS2
- turtlesim
- Terminal

## 4. 实验步骤

1. 启动 turtlesim。
2. 查看 topic 列表。
3. 发布速度消息控制运动。

## 5. 运行命令

<pre><code class="language-bash">
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
</code></pre>

## 6. 结果展示

<img src="images/dawugui.png" width="800" alt="小乌龟控制截图">

## 7. 学习总结

理解了 ROS2 topic 发布机制和消息控制方式。

## 8. 评分自查

| 项目 | 状态 | 说明 |
| --- | --- | --- |
| 提交 week 文件夹 | 完成 | 已建立本周目录 |
| README.md 存在 | 完成 | 已按统一模板编写 |
| README 内容详细 | 完成 | 包含目标、环境、步骤、结果和总结 |
| 包含图片 / 视频 | 视本周任务 | 有实验素材时已引用 |
| 包含代码 | 视本周任务 | 有代码作业时提交源码 |
| 有提交记录 | 完成 | 通过 Git 提交 |
| 按时提交 | 待确认 | 以课程截止时间为准 |

---

[返回总目录](../README.md)
