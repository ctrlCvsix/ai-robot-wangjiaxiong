# AI Robot 实验导航

<div align="center">

<pre>
╔════════════════════════════════════════════════════════════╗
║                  AI ROBOT 实验导航                         ║
║         课程实验 · 仿真模拟 · 视觉记录                      ║
╚════════════════════════════════════════════════════════════╝
</pre>

**Wang Jiaxiong · 信韩大学 · 软件工程**

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-在线预览-blue?logo=github)](https://ctrlcvsix.github.io/ai-robot-wangjiaxiong/)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

</div>

---

## 关于本仓库

这里是 AI 机器人课程的完整实验记录，覆盖 **Week 2 到 Week 14** 共 13 周内容。从最基础的 ROS2 环境搭建，到四足机器人步态控制和期末全栈项目，每周包含：详细实验报告（README）、运行截图/视频、可执行代码，以及实验中遇到的问题与解决思路。

### 学期路线总览

```mermaid
graph LR
    A[Week02 ROS2基础] --> B[Week03 Python控制]
    B --> C[Week04 PyBullet仿真]
    C --> D[Week05 机械臂IK]
    D --> E[Week06 KITTI可视化]
    E --> F[Week07 半期复习]
    F --> G[Week08 Docker容器]
    G --> H[Week09 语音交互]
    H --> I[Week10 OpenCV视觉]
    I --> J[Week11 Pages部署]
    J --> K[Week12 ArUco定位]
    K --> L[Week13 步态控制]
    L --> M[Week14 期末项目]
```

### 学习阶段划分

| 阶段 | 周次 | 阶段目标 | 核心技能 |
|------|------|----------|----------|
| **基础入门** | Week 2-3 | ROS2 环境搭建、Python 控制节点 | 命令行操作、话题通信 |
| **仿真深化** | Week 4-6 | 物理引擎、逆运动学、传感器数据 | PyBullet、RViz2、TF |
| **中期巩固** | Week 7 | 半期知识串联与项目演练 | PID 控制、运动学回顾 |
| **工程能力** | Week 8-11 | 容器化、语音、视觉、Web 部署 | Docker、OpenCV、Pages |
| **进阶应用** | Week 12-13 | 视觉定位、强化学习步态 | ArUco、PPO 训练 |
| **综合实战** | Week 14 | 全栈机器人控制系统 | 多技术融合、远程组网 |

---

## 实验路线

| 周次 | 权重 | 实验主题 | 核心产出 | 链接 |
|------|------|----------|----------|------|
| Week02 | 5 | Ubuntu 与 ROS2 环境搭建 | WSL2 安装、turtlesim 验证、节点话题探索、环境配置脚本 | [打开](./Week02) |
| Week03 | 5 | ROS2 话题通信与乌龟控制 | Twist 消息机制、Python 控制节点发布、长方形轨迹绘制 | [打开](./Week03) |
| Week04 | 8 | PyBullet 四足机器人仿真 | Laikago 模型加载、物理引擎参数调试、里程计数据监听 | [打开](./Week04) |
| Week05 | 8 | 机械臂逆运动学与视觉仿真 | IK 解析求解、虚拟相机配置、RViz2 三维可视化 | [打开](./Week05) |
| Week06 | 8 | KITTI 数据发布与 RViz2 可视化 | 点云渲染管线、话题监控、避障决策逻辑 | [打开](./Week06) |
| Week07 | 5 | 半学期复习与实践 | 正方形轨迹闭环、运动学公式推导、PID 参数整定 | [打开](./Week07) |
| Week08 | 8 | Docker ROS2 桌面容器 | 镜像构建与拉取、noVNC 浏览器访问、容器化部署最佳实践 | [打开](./Week08) |
| Week09 | 8 | ROS2 语音交互与路径规划 | TTS/STT 管道搭建、A* 搜索算法实现、多话题协同架构 | [打开](./Week09) |
| Week10 | 10 | Docker 进阶与 OpenCV 实验 | 容器卷挂载、图像处理管线、跨平台环境一致性保障 | [打开](./Week10) |
| Week11 | 10 | GitHub Pages 部署实践 | 静态站点生成、Jekyll 主题配置、CI/CD 推送验证 | [打开](./Week11) |
| Week12 | 10 | 手机摄像头与 ArUco 识别 | 标记字典生成、PnP 距离估算、移动端视觉定位 | [打开](./Week12) |
| Week13 | 15 | 四足机器人步态控制 | Trot 步态生成器、PPO 强化学习训练、步态性能可视化对比 | [打开](./Week13) |
| Week14 | — | 期末项目：机器狗遥控与乌龟迷宫 | PyBullet + ROS2 + Docker + Tailscale + AI Agent 全栈融合 | [打开](./Week14) |

---

## 各周亮点

### Week02 · ROS2 环境搭建
首次在 Windows WSL2 中运行 Ubuntu 24.04 + ROS2 Humble，成功启动 turtlesim 小乌龟仿真。掌握了 `ros2 node list`、`ros2 topic list`、`ros2 topic echo` 等核心调试命令，理解了 ROS2 的 DDS 通信机制。

### Week03 · Python 乌龟控制
使用 Python 编写了第一个 ROS2 控制节点 `rectangle_mover.py`，通过发布 `/turtle1/cmd_vel` 话题的 Twist 消息，驱动小乌龟画出精确的长方形轨迹，掌握了 Publisher 模式和消息类型的正确使用。

### Week04 · PyBullet 仿真入门
加载 Laikago 四足机器人 URDF 模型到 PyBullet 物理引擎，实现了基础物理仿真环境。通过里程计监听获取机器人实时位姿，为后续步态控制打下数据基础。

### Week05 · 机械臂逆运动学
从末端执行器目标位姿出发，解析求解 6-DOF 机械臂的关节角度。配置 RViz2 虚拟相机（RGB / 深度 / 分割），录制 `.webm` 格式仿真视频。深入理解了运动学正解与逆解的区别。

### Week06 · KITTI 点云可视化
将 KITTI 自动驾驶数据集点云发布到 ROS2 话题，在 RViz2 中实时渲染。编写了避障决策节点 `obstacle_avoidance_demo.py`，基于前方点云密度判断是否需要转向。

### Week07 · 半期复习
系统回顾了前 6 周知识点：ROS2 通信模型、Python 节点编程、仿真环境配置、传感器数据可视化。使用 PID 控制器完成正方形轨迹的精确闭环，并对运动学公式进行了完整推导。

### Week08 · Docker 桌面容器
拉取 `tiryoh/ros2-desktop-vnc` 镜像，通过 Docker Compose 一键启动带完整桌面环境的 ROS2 容器。浏览器访问 noVNC（端口 6080）获得 Ubuntu 桌面，可运行 turtlesim、RViz2 等 GUI 应用。

### Week09 · 语音交互
搭建了 ROS2 语音交互管道：语音识别（STT）→ 语义理解 → 路径规划（A* 算法）→ 语音合成（TTS）反馈。设计了多话题协同架构，实现了"说话控制机器人"的完整闭环。

### Week10 · Docker + OpenCV
深入 Docker 卷挂载机制，实现宿主机与容器的代码/数据共享。在容器内运行 OpenCV 图像处理管线（灰度、模糊、边缘检测），验证了"一次封装，到处运行"的环境一致性优势。

### Week11 · GitHub Pages
从零搭建本课程的静态文档站点：选择 Jekyll Cayman 主题、配置 `_config.yml`、本地预览调试、推送到 GitHub 自动部署。成功实现了 13 周实验内容的在线导航和展示。

### Week12 · ArUco 视觉定位
使用手机摄像头拍摄 ArUco 标记，通过 OpenCV 检测标记角点、PnP 算法估算相机与标记的相对位姿。实现了基于单目视觉的 3D 距离估算，可应用于机器人视觉定位。

### Week13 · 步态控制
实现了四足机器人的 Trot 步态生成器：规划 4 条腿的周期性运动轨迹（正弦函数）、通过 PyBullet 关节控制执行步态。尝试 PPO 强化学习优化步态参数，对比分析了手工设计步态 vs 学习步态的优劣。

### Week14 · 期末项目
构建「手机网页 → Tailscale 内网穿透 → WSL2 虚拟机 → Docker/ROS2/PyBullet → 仿真机器人」完整控制链路。实现了两个方向：
- **方向 A**：DeepSeek AI Agent 驱动的机器狗自主探索
- **方向 B**：ROS2 TurtleSim 乌龟迷宫 Web 远程控制与可视化

---

## 仓库地图

```
ai-robot-wangjiaxiong/
├── README.md                      # 本导航页（实验索引）
├── _config.yml                    # GitHub Pages Jekyll 配置
├── LICENSE                        # MIT 开源协议
├── CODE_OF_CONDUCT.md             # 贡献者行为准则
├── CONTRIBUTING.md                # 贡献指南
│
├── Week02/                        # ROS2 环境搭建与 turtlesim 验证
│   ├── README.md                  # 实验报告（步骤 + 截图 + 心得）
│   ├── setup_ros2.sh              # 一键环境配置脚本
│   ├── img/                       # 实验截图（节点/话题/运行效果）
│   └── images/                    # 补充图片
│
├── Week03/                        # ROS2 话题通信、Python 控制乌龟
│   ├── README.md
│   ├── rectangle_mover.py         # 长方形轨迹控制节点
│   ├── img/
│   └── images/
│
├── Week04/                        # PyBullet Laikago 四足机器人仿真
│   ├── README.md
│   ├── kinematics_demo.py         # 运动学演示脚本
│   ├── img/
│   └── images/
│
├── Week05/                        # 机械臂逆运动学、虚拟相机
│   ├── README.md
│   ├── marker_demo.py             # RViz2 标记演示
│   ├── img/
│   └── images/
│
├── Week06/                        # KITTI 点云发布、RViz2 可视化
│   ├── README.md
│   ├── obstacle_avoidance_demo.py # 避障决策节点
│   ├── avoidance_flow.txt         # 避障逻辑流程说明
│   ├── img/
│   └── images/
│
├── Week07/                        # 半期复习、正方形轨迹、PID
│   ├── README.md
│   ├── square_review.py           # PID 正方形轨迹
│   └── img/
│
├── Week08/                        # Docker ROS2 桌面容器、noVNC
│   ├── README.md
│   ├── docker-compose.yml         # 容器编排文件
│   └── img/
│
├── Week09/                        # 语音交互管道、路径规划
│   ├── README.md
│   ├── math_review_demo.py        # A* 路径规划实现
│   └── img/
│
├── Week10/                        # Docker + OpenCV 视觉处理
│   ├── README.md
│   ├── opencv_demo.py             # 图像处理管线
│   └── img/
│
├── Week11/                        # GitHub Pages 静态站点部署
│   ├── README.md
│   ├── index.html                 # Web 实验页面
│   └── img/
│
├── Week12/                        # ArUco 标记识别、距离估算
│   ├── README.md
│   ├── aruco_generate_detect.py   # 标记生成与检测
│   └── img/
│
├── Week13/                        # 四足 Trot 步态、PPO 训练
│   ├── README.md
│   ├── trot.py                    # Trot 步态生成器
│   ├── quadruped_walk.py          # 步态执行脚本
│   ├── quadruped_project_demo.py  # 完整项目演示
│   ├── demos/                     # 分步演示（01-04）
│   ├── scripts/                   # 步态分析工具
│   └── img/
│
└── Week14/                        # 期末项目（机器狗 + 乌龟迷宫）
    ├── README.md                  # 完整项目文档
    ├── Week14_项目报告.pdf         # 期末报告 PDF
    ├── server.py                  # PyBullet 仿真服务器（817行）
    ├── agent.py                   # DeepSeek AI Agent 决策模块
    ├── maze.py                    # 迷宫地图生成与碰撞检测
    ├── explorer.py                # 迷宫自主探索算法
    ├── index.html                 # 手机端遥控面板
    ├── docker-compose.yml         # ROS2 容器编排
    ├── turtlesim_web_bridge.py    # ROS2 ↔ WebSocket 通信桥接
    ├── turtlesim_maze.py          # TurtleSim 迷宫地图
    ├── turtlesim_explorer.py      # 乌龟迷宫探索算法
    ├── turtlesim_index.html       # 乌龟控制 Web 面板
    ├── turtlesim_auto.mp4         # 🎬 TurtleSim 自动探索演示视频
    ├── week14_1~5.png             # 项目运行截图 ×5
    └── *.jpeg                     # 补充实验截图
```

---

## 技术栈总览

| 类别 | 涉及技术 | 出现周次 |
|------|----------|----------|
| 机器人框架 | ROS2 Humble、RQT、Gazebo | Week 2-14 |
| 物理仿真 | PyBullet、Laikago URDF、逆运动学 IK | Week 4-5, 13-14 |
| 可视化 | RViz2、turtlesim、noVNC、Matplotlib | Week 2, 5-6, 8, 13 |
| 视觉处理 | OpenCV、ArUco、KITTI 点云、虚拟相机 | Week 5-6, 10, 12 |
| 容器化 | Docker、Docker Compose、镜像管理 | Week 8, 10, 14 |
| 网络组网 | Tailscale 内网穿透、WSL2 NAT 转发、WebSocket | Week 2, 11, 14 |
| AI/ML | DeepSeek API（Agent 模式）、PPO 强化学习 | Week 13-14 |
| Web 全栈 | GitHub Pages、Jekyll、aiohttp、HTML5 | Week 11, 14 |
| 开发工具 | Git、VS Code、WSL2、Termius、bash | Week 2-14 |

---

## 技能成长矩阵

| 维度 | Week 2-3 | Week 4-7 | Week 8-11 | Week 12-14 |
|------|----------|----------|-----------|------------|
| ROS2 熟练度 | ⭐ 入门 | ⭐⭐ 熟悉 | ⭐⭐⭐ 掌握 | ⭐⭐⭐⭐ 精通 |
| Python 编程 | ⭐⭐ 基础 | ⭐⭐⭐ 应用 | ⭐⭐⭐ 应用 | ⭐⭐⭐⭐ 工程级 |
| 仿真操作 | — | ⭐⭐ 起步 | ⭐⭐⭐ 熟练 | ⭐⭐⭐⭐ 定制开发 |
| Docker | — | — | ⭐⭐⭐ 生产级 | ⭐⭐⭐ 生产级 |
| 计算机视觉 | — | ⭐ 了解 | ⭐⭐ 实践 | ⭐⭐⭐ 集成应用 |
| AI 集成 | — | — | — | ⭐⭐⭐ Agent 实战 |
| Web 部署 | — | — | ⭐⭐ 基础 | ⭐⭐⭐ 全栈 |

---

## 实验环境

| 组件 | 版本/规格 |
|------|-----------|
| 操作系统 | Windows 11 Home + WSL2 Ubuntu 24.04 |
| ROS2 | Humble Hawksbill |
| Python | 3.12 |
| Docker | Docker Desktop 4.x + Docker Compose v2 |
| 仿真引擎 | PyBullet 3.2.6 |
| 硬件 | Intel i7 / 16GB RAM / NVIDIA RTX 4060 |
| AI API | DeepSeek API（deepseek-chat） |
| 编辑器 | VS Code + WSL Remote 扩展 |

---

## 实验统计

| 指标 | 数量 |
|------|------|
| 实验周数 | 13 周（Week 2-14） |
| 实验报告 | 13 篇 |
| Python 脚本 | 18 个 |
| Docker 编排文件 | 3 个 |
| Web 前端页面 | 3 个（index.html ×2 + turtlesim_index.html） |
| 截图/图片 | 80+ 张 |
| 演示视频 | 2 个（机械臂 .webm + 乌龟迷宫 .mp4） |
| 代码总行数 | 约 3,500+ 行 |
| 期末报告 | 1 份完整 PDF |

---

## 快速开始

```bash
# 克隆本仓库
git clone https://github.com/ctrlCvsix/ai-robot-wangjiaxiong.git
cd ai-robot-wangjiaxiong

# Week14 期末项目 — 方向 A（机器狗仿真）
cd Week14
pip install pybullet aiohttp
DEEPSEEK_API_KEY=your_key PYBULLET_GUI=0 python3 server.py

# Week14 期末项目 — 方向 B（TurtleSim 乌龟迷宫）
cd Week14
docker compose up -d
# 浏览器访问 http://localhost:8080

# Week08 Docker ROS2 桌面
cd Week08
docker compose up -d
# 浏览器访问 http://localhost:6080 （noVNC 桌面）
```

---

## 贡献与反馈

欢迎提交 Issue 或 Pull Request 参与改进。请遵循 [贡献指南](./CONTRIBUTING.md) 和 [行为准则](./CODE_OF_CONDUCT.md)。

本项目基于 [MIT License](./LICENSE) 开源。

---

<div align="center">

**🚀 从环境搭建到全栈机器人，13 周的 AI Robotics 成长之路**

*Generated by GitHub Pages · [View on GitHub](https://github.com/ctrlCvsix/ai-robot-wangjiaxiong)*

</div>
