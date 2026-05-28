# Week 02 - Ubuntu And ROS2 Environment Setup

## Lab Objective

This lab builds the base Ubuntu and ROS2 environment, then verifies the installation with turtlesim.

## Folder Structure

<pre>
Week02/
|-- README.md              # weekly lab report
|-- images/                # setup screenshot
</pre>

## Environment

- Ubuntu 24.04 LTS
- ROS2 Jazzy / Humble
- Terminal
- VS Code

## Workflow

1. Prepare Ubuntu and ROS2 packages.
2. Source the ROS2 setup script.
3. Launch turtlesim as the first environment check.

## Commands

<pre><code class="language-bash">
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node
</code></pre>

## Evidence

<img src="images/xiaowugui.png" width="800" alt="ROS2 turtlesim setup evidence">

## Reflection

A stable ROS2 environment is the first requirement for every later robot experiment.

---

[Back to Lab Navigator](../README.md)
