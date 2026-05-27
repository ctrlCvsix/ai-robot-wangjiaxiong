# Week 02 - Ubuntu 24.04 And ROS2 Environment Setup

> This week focused on installing the Linux and ROS2 environment, then verifying the setup with the classic turtlesim demo.

## Overview

| Item | Content |
| --- | --- |
| Main topic | Ubuntu and ROS2 environment setup |
| Keywords | Ubuntu 24.04, ROS2 Jazzy, turtlesim, terminal |
| Output | Verified ROS2 desktop environment and turtlesim result |

## Goals

- Install and configure Ubuntu 24.04 for robot development.
- Install ROS2 and prepare shell environment variables.
- Run turtlesim to confirm that ROS2 nodes and GUI tools work correctly.

## Environment And Tools

- Ubuntu 24.04 LTS
- ROS2 Jazzy / Humble concepts
- Terminal
- VS Code

## Task Workflow

1. Configured the Ubuntu development environment.
2. Installed ROS2 desktop components.
3. Loaded the ROS2 environment in the terminal.
4. Ran turtlesim to verify the installation.

## Key Commands

```bash
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node
```

## Result

<img src="./images/xiaowugui.png" width="720" alt="ROS2 turtlesim verification result" />

The turtlesim window confirmed that the ROS2 graphical demo could run successfully in the configured environment.

## What I Learned

- ROS2 needs the environment setup script to be sourced before using ROS2 commands.
- Turtlesim is a simple but useful way to check whether ROS2 installation and GUI support are working.
- A stable Ubuntu and ROS2 environment is the base for later robot experiments.
