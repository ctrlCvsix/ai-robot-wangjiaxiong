# Week 14 — 远程摄像头环境配置

## 实验目标

通过 Termius、Tailscale 和本地摄像头桥接，搭建远程摄像头环境。远程访问方案保留了实验中使用的 HTTPS 浏览器工作流。

## 目录结构

<pre>
Week14/
|-- README.md              # 周实验报告
|-- 1.jpeg                 # 截图
|-- 11.jpeg                # 截图
</pre>

## 实验环境

- Termius
- Tailscale
- Python 虚拟环境
- Flask / 摄像头桥接
- HTTPS 本地服务端点

## 实验流程

1. 创建虚拟环境。
2. 安装依赖项。
3. 启动摄像头桥接服务。
4. 在手机浏览器中访问 https://<tailscale-ip>:5000 并授予所需摄像头权限。

## 命令

<pre><code class="language-bash">
python3 -m venv env
source env/bin/activate
python3 week12_starters/camera_bridge.py
</code></pre>

## 实验证据

<img src="1.jpeg" width="800" alt="远程摄像头证据">

<img src="11.jpeg" width="800" alt="远程配置证据">

## 总结与反思

远程机器人实验既需要网络连接，也需要仔细处理浏览器权限。

---

[返回实验导航](../README.md)
