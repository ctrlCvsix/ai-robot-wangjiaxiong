# Week 15 — Week14 项目存档与期末总结

## 实验目标

将 Week14 机器狗/乌龟迷宫项目的完整代码和项目报告归档至 Week15，作为课程期末成果展示。

## 目录结构

<pre>
Week15/
|-- README.md                   # 周实验报告
|-- Week14_项目报告.docx         # Week14 项目报告文档
|-- server.py                   # PyBullet 机器狗仿真服务器
|-- agent.py                    # AI Agent 决策控制器
|-- maze.py                     # 迷宫地图生成
|-- explorer.py                 # 迷宫自主探索器
|-- index.html                  # 机器狗网页控制界面
|-- docker-compose.yml          # Docker 容器编排配置
|-- turtlesim_web_bridge.py     # TurtleSim ROS2 Web 桥接
|-- turtlesim_maze.py           # 乌龟迷宫地图
|-- turtlesim_explorer.py       # 乌龟迷宫探索
|-- turtlesim_index.html        # 乌龟控制网页界面
</pre>

## 实验环境

- **方向 A — PyBullet 机器狗仿真**
  - Python 3.12 + PyBullet + aiohttp
  - WSL2 Ubuntu 24.04 + Docker Engine
  - DeepSeek API（Agent 模式）
  - Tailscale 内网穿透（手机远程操控）
- **方向 B — TurtleSim 乌龟迷宫**
  - ROS2 Humble（Docker 容器）
  - TurtleSim + 自定义迷宫/探索模块
  - Web 桥接实现浏览器控制

## 项目架构

```
手机网页控制器 → Tailscale → WSL2 → Docker(ROS2) / PyBullet仿真 → 机器人运动
```

- 端口 8765：方向 A 机器狗网页控制器
- 端口 8080：方向 B 乌龟控制器
- 端口 6080：noVNC 桌面远程访问
- `PYBULLET_GUI=0`：DIRECT 模式（低资源消耗）

## 关键命令

<pre><code class="language-bash">
# 启动 PyBullet 仿真（Agent 模式）
wsl -d Ubuntu-24.04 -u root bash -c "cd /mnt/d/ai-robotics-course/week14_starters/pybullet_dog && DEEPSEEK_API_KEY=sk-xxx PYBULLET_GUI=0 python3 server.py"

# 启动 Docker 容器（TurtleSim 方向 B）
wsl -d Ubuntu-24.04 -u root bash -c "service docker start && cd /mnt/d/ai-robotics-course/week14_starters/docker && docker compose up -d"

# 查看 PyBullet 日志
wsl -d Ubuntu-24.04 -u root bash -c "cat /tmp/pybullet_wsl.log"
</code></pre>

## 实验证据

- 项目代码完整归档：方向 A（PyBullet 机器狗）和方向 B（TurtleSim 乌龟迷宫）
- 项目报告：`Week14_项目报告.docx`
- 手机端可通过 Tailscale IP `100.66.42.5:8765` 远程操控

## 总结与反思

本项目打通了从手机网页到仿真机器人的完整链路：Tailscale 组网 → WSL2 虚拟机 → Docker/ROS2 → PyBullet 物理仿真。遇到的主要挑战包括 Windows 与 WSL2 的端口转发问题（最终绕过 Docker 直接在 WSL 运行 PyBullet 解决）、容器重建后依赖丢失（需固化至 Dockerfile），以及 PyBullet GUI 模式下资源占用过高（改用 DIRECT 模式）。

---

[返回实验导航](../README.md)
