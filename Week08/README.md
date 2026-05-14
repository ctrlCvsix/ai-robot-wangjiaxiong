# Week8 - Docker ROS2

## 实验目标

学习 Docker 的基本使用，并在 Docker 容器中运行 ROS2 图形化桌面环境。

---

## 操作过程

### 1. 检查 Docker

```bash
docker --version
```

### 2. 测试 Docker

```bash
docker run hello-world
```

### 3. 拉取 ROS2 镜像

```bash
docker pull tiryoh/ros2-desktop-vnc:humble
```

### 4. 运行容器

```bash
docker run -it --rm -p 6080:80 tiryoh/ros2-desktop-vnc:humble
```

### 5. 浏览器访问

```text
http://127.0.0.1:6080/
```

### 6. 运行 turtlesim

```bash
ros2 run turtlesim turtlesim_node
ros2 run turtle_teleop_key
```

---

## 实验截图

### Docker Version
<img src="./img/1.png" width="700">

### Docker Hello World
<img src="./img/2.png" width="700">

### ROS2 Desktop
<img src="./img/3.png" width="700">

---

## 总结

通过 Docker 运行 ROS2，我理解了容器化环境部署方式，并成功在浏览器中运行了 ROS2 图形化桌面和 turtlesim。