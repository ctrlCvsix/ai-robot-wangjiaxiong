# Week 08 — Docker ROS2 桌面容器

## 实验目标

使用 Docker 容器运行 ROS2 桌面工具，并通过浏览器界面进行访问。

## 目录结构

<pre>
Week08/
|-- README.md              # 周实验报告
|-- screenshots/           # 推荐证据
</pre>

## 实验环境

- Docker
- ROS2 桌面镜像
- 浏览器 VNC

## 实验流程

1. 启动 ROS2 桌面容器。
2. 映射访问端口。
3. 运行图形化 ROS2 工具。

## 命令

<pre><code class="language-bash">
docker run -it --rm -p 6080:80 tiryoh/ros2-desktop-vnc:humble
</code></pre>

## 实验证据

容器桌面可通过映射后的浏览器端口打开访问。

## 总结与反思

Docker 有效减少了不同机器之间环境差异导致的问题。

---

[返回实验导航](../README.md)
