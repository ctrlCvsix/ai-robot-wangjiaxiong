# Week 03 - ROS2 Topic Communication And Turtlesim Control

> This week focused on ROS2 topic communication and controlling turtlesim movement through command-line message publishing.

## Overview

| Item | Content |
| --- | --- |
| Main topic | ROS2 topic communication |
| Keywords | ROS2, topic, publisher, Twist, turtlesim |
| Output | Turtlesim motion control through topic commands |

## Goals

- Understand the ROS2 Topic communication model.
- Learn how publishers send messages to running nodes.
- Practice controlling robot motion with `geometry_msgs/msg/Twist`.

## Environment And Tools

- Ubuntu 24.04 LTS
- ROS2 Jazzy / Humble
- turtlesim
- Terminal

## Task Workflow

1. Started the turtlesim simulation node.
2. Checked available ROS2 topics.
3. Published velocity messages to control movement.
4. Observed how linear and angular values changed the turtle path.

## Key Commands

```bash
ros2 run turtlesim turtlesim_node
ros2 topic list
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
```

## Result

<img src="./images/dawugui.png" width="720" alt="ROS2 turtlesim path control result" />

The turtle moved according to the published velocity messages, showing the relationship between ROS2 topics and robot motion control.

## What I Learned

- ROS2 topics decouple message senders and receivers.
- `Twist` messages can describe both forward movement and rotation.
- Command-line publishing is useful for quickly testing robot behavior.
