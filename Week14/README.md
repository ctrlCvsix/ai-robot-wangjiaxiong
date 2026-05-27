# Week 14 - 远程调用与环境配置

## 1. 作业说明

本周使用 Termius、Tailscale 和 Flask 完成远程摄像头服务配置。

## 2. 文件结构

<pre>
Week14/
|-- README.md              # 必须
|-- 1.jpeg                 # 截图
|-- 11.jpeg                # 截图
</pre>

## 3. 实验环境

- Termius
- Tailscale
- Python venv
- Flask

## 4. 实验步骤

1. 创建虚拟环境。
2. 安装依赖。
3. 启动 camera_bridge 服务。
4. 手机浏览器访问服务。

## 5. 运行命令

<pre><code class="language-bash">
python3 -m venv env
source env/bin/activate
python3 week12_starters/camera_bridge.py
</code></pre>

## 6. 结果展示

<img src="1.jpeg" width="800" alt="远程实验截图">

<img src="11.jpeg" width="800" alt="远程实验截图 2">

## 7. 学习总结

理解了远程控制、虚拟局域网和摄像头服务的联动方式。

## 8. 评分自查

| 项目 | 状态 | 说明 |
| --- | --- | --- |
| 提交 week 文件夹 | 完成 | 已建立本周目录 |
| README.md 存在 | 完成 | 已按统一模板编写 |
| README 内容详细 | 完成 | 包含目标、环境、步骤、结果和总结 |
| 包含图片 / 视频 | 视本周任务 | 有实验素材时已引用 |
| 包含代码 | 视本周任务 | 有代码作业时提交源码 |
| 有提交记录 | 完成 | 通过 Git 提交 |
| 按时提交 | 待确认 | 以课程截止时间为准 |

---

[返回总目录](../README.md)
