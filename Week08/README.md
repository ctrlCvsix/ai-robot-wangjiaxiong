# Week 08 - Docker ROS2 桌面容器

## 1. 作业说明

本周使用 Docker 部署 ROS2 桌面环境，并通过浏览器访问。

## 2. 文件结构

<pre>
Week08/
|-- README.md              # 必须
|-- screenshots/           # 推荐
</pre>

## 3. 实验环境

- Docker
- ROS2 Desktop VNC
- Browser

## 4. 实验步骤

1. 检查 Docker。
2. 拉取 ROS2 桌面镜像。
3. 启动容器并映射端口。

## 5. 运行命令

<pre><code class="language-bash">
docker run -it --rm -p 6080:80 tiryoh/ros2-desktop-vnc:humble
</code></pre>

## 6. 结果展示

浏览器访问 http://127.0.0.1:6080/ 后可进入 ROS2 桌面环境。

## 7. 学习总结

理解了 Docker 容器化环境对机器人开发的价值。

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
