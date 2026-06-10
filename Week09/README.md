# Week 09 — ROS2 语音交互

## 实验目标

记录 ROS2 中语音交互的话题通信思路与消息管道设计。

## 目录结构

<pre>
Week09/
|-- README.md              # 周实验报告
|-- README.md              # 实验报告
</pre>

## 实验环境

- ROS2
- 语音 / TTS 概念
- 终端

## 实验流程

1. 列出 ROS2 话题。
2. 检查语音相关消息。
3. 将语音流程与机器人控制相连接。

## 命令

<pre><code class="language-bash">
ros2 topic list
ros2 topic echo /tts/speak
</code></pre>

## 实验证据

语音交互以 ROS2 消息管道的形式记录下来。

## 总结与反思

语音系统可以抽象为节点、话题与消息的组合来进行推理与设计。

---

[返回实验导航](../README.md)
