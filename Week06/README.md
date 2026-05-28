# Week 06 - KITTI Publishing And RViz2 Visualization

## Lab Objective

This lab publishes KITTI-style data and checks point cloud / image visualization in ROS2 tools.

## Folder Structure

<pre>
Week06/
|-- README.md              # weekly lab report
|-- images/                # visualization screenshot
</pre>

## Environment

- ROS2
- KITTI dataset
- RViz2
- RQT

## Workflow

1. Prepare KITTI data.
2. Run the publisher node.
3. View data in RViz2 and RQT.

## Commands

<pre><code class="language-bash">
ros2 run ros2_kitti_publishers publisher_node
rviz2
</code></pre>

## Evidence

<img src="images/zidongjiashi.png" width="800" alt="KITTI visualization evidence">

## Reflection

Visualization tools make sensor data easier to verify and debug.

---

[Back to Lab Navigator](../README.md)
