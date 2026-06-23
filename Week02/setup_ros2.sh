#!/bin/bash
# Week02 - ROS2 环境搭建脚本
# 在 Ubuntu 24.04 上安装 ROS2 Jazzy

echo "=== 添加 ROS2 GPG Key ==="
sudo apt update && sudo apt install -y curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "=== 添加 ROS2 仓库 ==="
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

echo "=== 安装 ROS2 Jazzy 桌面版 ==="
sudo apt update && sudo apt install -y ros-jazzy-desktop python3-colcon-common-extensions

echo "=== 配置环境变量 ==="
echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc
source ~/.bashrc

echo "=== 验证安装 ==="
ros2 run turtlesim turtlesim_node &
sleep 2
ros2 node list
echo "=== ROS2 环境搭建完成 ==="
