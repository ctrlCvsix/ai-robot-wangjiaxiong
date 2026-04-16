# Week 04：基于 PyBullet 的四足机器人运动仿真

## 1. 实验目标
- 搭建 PyBullet 物理仿真环境。
- 学习导入 URDF/SDF 格式的机器人模型。
- 通过 Python 脚本控制多关节（关节空间）机器人运动，并进行物理属性（如碰撞检测、摩擦力）的仿真验证。

## 2. 实验环境
- **操作系统**: Ubuntu 24.04 LTS
- **物理引擎**: PyBullet (Bullet Physics Engine)
- **编程语言**: Python 3
- **开发工具**: VS Code, Terminal

## 3. 实验步骤与内容

### 3.1 安装与环境配置
首先安装了 PyBullet 库：
```bash
pip install pybullet