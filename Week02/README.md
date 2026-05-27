# Week 02 - Ubuntu 24.04 与 ROS2 环境搭建

## 1. 作业说明

本周完成 Ubuntu 24.04 与 ROS2 环境配置，并通过 turtlesim 验证基础环境。

## 2. 文件结构

<pre>
Week02/
|-- README.md              # 必须
|-- images/                # 截图、效果图
</pre>

## 3. 实验环境

- Ubuntu 24.04 LTS
- ROS2 Jazzy / Humble
- Terminal
- VS Code

## 4. 实验步骤

1. 配置 Ubuntu 与 ROS2 环境。
2. 加载 ROS2 setup 脚本。
3. 启动 turtlesim 验证安装。

## 5. 运行命令

<pre><code class="language-bash">
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node
</code></pre>

## 6. 结果展示

<img src="images/xiaowugui.png" width="800" alt="ROS2 turtlesim 实验截图">

## 7. 学习总结

掌握了 ROS2 环境搭建和基础验证流程。

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
