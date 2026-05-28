# Week 12 远程调用与环境配置记录

本项目记录了如何使用手机端 Termius 远程控制电脑，克隆作业仓库，解决 Python 环境依赖冲突，并最终成功启动摄像头服务的全过程。

## 文件与目录结构

通过 Git 将远程仓库克隆至本地，目录结构如下：

```text
~/ai-robot-class.github.io/
└── week12_starters/
    ├── camera_bridge.py
    └── requirements.txt

```

## 安装依赖与环境配置

针对 Ubuntu 24.04 及后续版本中关于 `PEP 668`（外部管理环境）的限制，本项目通过创建 Python 虚拟环境（Virtual Environment）来解决依赖冲突问题：

```bash
# 1. 进入克隆好的项目根目录
cd ~/ai-robot-class.github.io

# 2. 创建独立虚拟环境 env
python3 -m venv env

# 3. 激活虚拟环境
source env/bin/activate

# 4. 在虚拟环境中成功安装依赖
pip install -r week12_starters/requirements.txt

```

## 运行方式

1. **网络连接**：手机与电脑同时开启 **Tailscale**，确保双方处于同一虚拟局域网。
2. **远程控制**：手机打开 **Termius**，配置 Host 并通过电脑的 Tailscale IP (`100.118.234.115`) 远程连接。
3. **启动服务**：在手机 Termius 的虚拟环境下，直接执行以下命令启动 Flask 服务器：
```bash
python3 week12_starters/camera_bridge.py

```


4. **移动端查看**：保持 Termius 在后台运行，打开手机浏览器访问以下地址：
```text
[https://100.118.234.115:5000](https://100.118.234.115:5000)

```


*注意：访问时需手动忽略浏览器的 https 自签名证书安全警告，并允许网页调用手机摄像头。*

## 实际使用与测试流程

* **数据保存**：手机端浏览器成功调用摄像头后，采集并保存的标定图片会自动写入电脑的路径：`/home/wang-jiaxiong/ai-robot-class.github.io/calib_images`
* **ArUco 码检测测试**：使用手机摄像头对准符合 `DICT_4X4_50` 字典且 ID 为 `0` 的 ArUco 黑白方块标记，程序可进行实时识别。
* **终止服务**：测试完成后，切回手机 Termius 终端，在键盘上按下 `Ctrl + C` 组合键即可关闭服务器。

```

```
