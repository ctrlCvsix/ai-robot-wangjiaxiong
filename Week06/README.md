# Week 06 — KITTI 数据发布与 RViz2 可视化

## 实验目标

发布 KITTI 格式数据，在 ROS2 工具中查看点云与图像的可视化效果。

## 目录结构

<pre>
Week06/
|-- README.md              # 周实验报告
|-- images/                # 可视化截图
</pre>

## 实验环境

- ROS2
- KITTI 数据集
- RViz2
- RQT

## 实验流程

1. 准备 KITTI 数据。
2. 运行发布节点。
3. 在 RViz2 与 RQT 中查看数据。

## 命令

<pre><code class="language-bash">
ros2 run ros2_kitti_publishers publisher_node
rviz2
</code></pre>

## 实验证据

<img src="images/zidongjiashi.png" width="800" alt="KITTI 可视化证据">

## 总结与反思

可视化工具使传感器数据的验证与调试变得更加直观高效。

---

[返回实验导航](../README.md)
