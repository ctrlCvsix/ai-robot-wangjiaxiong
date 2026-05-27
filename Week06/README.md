# Week 06 - KITTI 数据集与 RViz2 可视化

## 1. 作业说明

本周发布 KITTI 数据并使用 RViz2/RQT 可视化点云与图像。

## 2. 文件结构

<pre>
Week06/
|-- README.md              # 必须
|-- images/                # 截图、效果图
</pre>

## 3. 实验环境

- ROS2
- KITTI Dataset
- RViz2
- RQT

## 4. 实验步骤

1. 准备 KITTI 数据。
2. 运行发布节点。
3. 使用 RViz2 查看结果。

## 5. 运行命令

<pre><code class="language-bash">
ros2 run ros2_kitti_publishers publisher_node
rviz2
</code></pre>

## 6. 结果展示

<img src="images/zidongjiashi.png" width="800" alt="KITTI 可视化截图">

## 7. 学习总结

熟悉了 ROS2 多传感器数据可视化流程。

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
