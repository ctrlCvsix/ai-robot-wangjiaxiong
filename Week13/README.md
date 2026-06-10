# Week 13 — 四足 Trot 步态仿真

## 实验目标

为 PyBullet 中的 Laikago 模型实现一个简单的 Trot 步态控制器。

## 目录结构

<pre>
Week13/
|-- README.md              # 周实验报告
|-- trot.py                # Python 代码
</pre>

## 实验环境

- Python
- PyBullet
- NumPy
- Laikago URDF

## 实验流程

1. 加载 Laikago 机器人模型。
2. 创建步态控制器。
3. 运行仿真循环。

## 命令

<pre><code class="language-bash">
pip install pybullet numpy
python3 trot.py
</code></pre>

## 实验证据

源代码文件：trot.py

## 总结与反思

步态控制器展示了如何通过相位差实现四足机器人的协调运动。

---

[返回实验导航](../README.md)
