# Week 03 - ROS2 Topic Communication

## Lab Objective

This lab controls turtlesim through ROS2 topic publishing and demonstrates how Twist messages affect movement.

## Folder Structure

<pre>
Week03/
|-- README.md              # weekly lab report
|-- images/                # movement screenshot
</pre>

## Environment

- ROS2
- turtlesim
- geometry_msgs/msg/Twist

## Workflow

1. Start turtlesim.
2. Publish velocity commands.
3. Record the movement result.

## Commands

<pre><code class="language-bash">
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
</code></pre>

## Evidence

<img src="images/dawugui.png" width="800" alt="ROS2 topic control evidence">

## Reflection

Topic publishing is a simple but powerful way to test robot command flow.

---

[Back to Lab Navigator](../README.md)
