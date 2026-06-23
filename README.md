# AI Robot 实验导航

<div align="center">

<pre>
╔════════════════════════════════════════════════════════════╗
║                  AI ROBOT 实验导航                         ║
║         课程实验 · 仿真模拟 · 视觉记录                      ║
╚════════════════════════════════════════════════════════════╝
</pre>

**Wang Jiaxiong · 信韩大学 · 软件工程**

</div>

---

## 关于本仓库

这里是 AI 机器人课程的全部实验记录，覆盖 **Week 2 到 Week 14** 共 13 周内容。每周包含：详细实验报告（README）、运行截图、可执行代码，以及实验中遇到的问题与解决思路。

学期路线：ROS2 环境搭建 → 话题通信 → PyBullet 仿真 → 逆运动学 → KITTI 可视化 → Docker 容器 → 语音交互 → OpenCV 视觉 → GitHub Pages → ArUco 定位 → 步态控制 → 期末项目。

---

## 实验路线

| 周次 | 权重 | 实验主题 | 内容 | 链接 |
|------|------|----------|------|------|
| Week02 | 5 | Ubuntu 与 ROS2 环境搭建 | WSL2 安装、turtlesim 验证、节点话题探索 | [打开](./Week02) |
| Week03 | 5 | ROS2 话题通信与乌龟控制 | Twist 消息、Python 控制节点、长方形轨迹 | [打开](./Week03) |
| Week04 | 8 | PyBullet 四足机器人仿真 | Laikago 模型加载、物理引擎、里程计监听 | [打开](./Week04) |
| Week05 | 8 | 机械臂逆运动学与视觉仿真 | IK 求解、虚拟相机、RViz2 可视化 | [打开](./Week05) |
| Week06 | 8 | KITTI 数据发布与 RViz2 可视化 | 点云渲染、话题监控、避障逻辑 | [打开](./Week06) |
| Week07 | 5 | 半学期复习与实践 | 正方形轨迹、运动学计算、PID 控制 | [打开](./Week07) |
| Week08 | 8 | Docker ROS2 桌面容器 | 镜像拉取、noVNC 访问、容器化部署 | [打开](./Week08) |
| Week09 | 8 | ROS2 语音交互与路径规划 | TTS/STT 管道、A* 算法、话题架构 | [打开](./Week09) |
| Week10 | 10 | Docker 进阶与 OpenCV 实验 | 容器挂载、图像处理、环境一致性 | [打开](./Week10) |
| Week11 | 10 | GitHub Pages 部署实践 | 静态站点、Jekyll 配置、推送验证 | [打开](./Week11) |
| Week12 | 10 | 手机摄像头与 ArUco 识别 | 标记生成、距离估算、视觉定位 | [打开](./Week12) |
| Week13 | 15 | 四足机器人步态控制 | Trot 步态、PPO 训练、步态可视化对比 | [打开](./Week13) |
| Week14 | — | 期末项目：机器狗遥控与乌龟迷宫 | PyBullet + ROS2 + Docker + Tailscale 全栈 | [打开](./Week14) |

---

## 仓库地图

```
ai-robot-wangjiaxiong/
├── README.md                      # 本导航页
├── _config.yml                    # GitHub Pages 配置
│
├── Week02/                        # ROS2 环境搭建与 turtlesim 验证
├── Week03/                        # ROS2 话题通信、Python 控制乌龟
├── Week04/                        # PyBullet Laikago 四足机器人仿真
├── Week05/                        # 机械臂逆运动学、虚拟相机
├── Week06/                        # KITTI 点云发布、RViz2 可视化
├── Week07/                        # 半期复习、正方形轨迹、PID
├── Week08/                        # Docker ROS2 桌面容器、noVNC
├── Week09/                        # 语音交互管道、路径规划
├── Week10/                        # Docker + OpenCV 视觉处理
├── Week11/                        # GitHub Pages 静态站点部署
├── Week12/                        # ArUco 标记识别、距离估算
├── Week13/                        # 四足 Trot 步态、步态可视化
└── Week14/                        # 期末项目（机器狗 + 乌龟迷宫）
```

---

## 评审路径

1. 从上方实验路线表选择目标周次。
2. 打开对应文件夹，阅读 `README.md` 了解实验目标、步骤和结果。
3. 查看配套截图 / 视频 / GIF 获得直观理解。
4. 运行 Python 代码复现实验（如有）。
5. 通过 Git 历史查看迭代过程和提交频率。

---

## 技术栈总览

| 类别 | 涉及技术 |
|------|----------|
| 机器人 | ROS2 Humble、PyBullet、turtlesim、RViz2、TF |
| 视觉 | OpenCV、ArUco、虚拟相机（RGB/深度/分割） |
| 容器 | Docker、Docker Compose、noVNC |
| 网络 | Tailscale 内网穿透、WSL2 NAT 转发 |
| AI | DeepSeek API（Agent 模式）、PPO 强化学习 |
| Web | GitHub Pages、Jekyll、aiohttp、WebSocket |
| 工具 | Git、VS Code、Termius、RQT |
