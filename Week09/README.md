# Week 09 — ROS2 语音交互与路径规划

## 实验目标

探索 ROS2 中语音交互（TTS/STT）的消息管道设计，理解语音系统如何通过话题/服务与机器人控制系统对接。同时涉及路径规划算法的基本概念。

## 实验环境

| 组件 | 说明 |
|------|------|
| 中间件 | ROS2 Humble |
| 语音 TTS | `/tts/speak` 话题（std_msgs/String） |
| 语音 STT | `/stt/listen` 话题（std_msgs/String） |
| 路径规划 | A* 算法概念 + ROS2 导航栈 |

## 目录结构

```
Week09/
├── README.md         # 本报告
├── math_run.png      # 数学基础运行截图
├── path_result.png   # 路径规划结果截图
└── ros2_voice_topic.png  # ROS2 语音话题截图
```

## 实验步骤

### 1. 语音话题探索

列出 ROS2 中与语音相关的话题，查看消息类型和流向：

```bash
ros2 topic list | grep -E "tts|stt|speak|listen"
```

### 2. 消息管道分析

监听 TTS 话题，分析语音指令如何从文本转换为机器人动作：

```bash
ros2 topic echo /tts/speak
```

### 3. 路径规划实验

运行路径规划节点，观察机器人如何在障碍物间生成最优路径：

```bash
ros2 topic echo /plan
```

## 关键命令

```bash
# 查看所有话题
ros2 topic list

# 监听语音指令
ros2 topic echo /tts/speak

# 查看话题消息类型
ros2 topic info /tts/speak

# 发布语音测试消息
ros2 topic pub /tts/speak std_msgs/msg/String "{data: '前进'}"
```

## 语音交互架构

```
用户语音 → STT(语音识别) → /stt/listen → NLP处理节点 → 动作指令 → /cmd_vel → 机器人
机器人状态 → /robot/status → TTS节点 → /tts/speak → 语音播报 → 用户听到反馈
```

ROS2 中语音交互被抽象为标准的话题发布/订阅模式：
- **STT（语音转文本）**：麦克风 → 语音识别引擎 → `/stt/listen` (String)
- **TTS（文本转语音）**：`/tts/speak` (String) → 语音合成引擎 → 扬声器

## 实验证据

### 数学基础运行

<img src="img/math_run.png" width="800" alt="数学基础运行截图">

### ROS2 语音话题

<img src="img/ros2_voice_topic.png" width="800" alt="ROS2 语音交互话题">

*ROS2 环境中语音相关话题的运行状态*

*路径规划相关数学基础的运行验证*

### 路径规划结果

<img src="img/path_result.png" width="800" alt="路径规划结果">

*路径规划算法在仿真环境中生成的最优路径*

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 语音话题无数据 | 未启动 TTS/STT 节点 | 先启动相应的语音处理节点，再监听话题 |
| 中文语音识别准确率低 | 通用语音模型对中文支持有限 | 使用支持中文的 STT 引擎（如 Whisper） |
| 路径规划结果不合理 | 代价地图未正确配置障碍物信息 | 检查 LiDAR/深度相机话题是否正确发布 |

## 总结与反思

### 核心收获

1. **语音即话题**：在 ROS2 中，语音交互被优雅地抽象为普通话题发布/订阅。一条 `ros2 topic pub` 命令就能模拟语音指令，极大简化了开发调试
2. **模块化思维**：STT → NLP → 动作生成 → TTS，每个环节是独立节点，可单独替换升级而不影响整体
3. **路径规划基础**：A* 算法是机器人导航的经典方案，理解代价地图和启发函数是后续深入导航栈的前提

### 延伸思考

语音交互让机器人从"编程控制"升级为"自然语言控制"。结合 Week12 的 ArUco 视觉定位，可以实现「语音说"去拿那个东西"→ 视觉识别目标 → 路径规划 → 自主导航 → 抓取」的完整智能流程。

---

[返回实验导航](../README.md)
