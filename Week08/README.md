# Mission Log 08 - Docker ROS2 Desktop Environment

> Mission focus: this week focused on using Docker to run a ROS2 desktop environment through a browser-accessible VNC container.

## Mission Brief

| Item | Content |
| --- | --- |
| Main topic | Docker-based ROS2 environment |
| Keywords | Docker, ROS2 Humble, VNC, container, turtlesim |
| Output | ROS2 desktop environment running inside Docker |

## Objectives

- Learn basic Docker image and container commands.
- Pull and run a ROS2 desktop VNC image.
- Access the containerized ROS2 desktop from a browser.
- Run turtlesim inside the Docker environment.

## Payload

- Docker
- ROS2 Humble desktop VNC image
- Browser
- Terminal

## Command Sequence

1. Checked the Docker installation.
2. Ran the `hello-world` test container.
3. Pulled the ROS2 desktop VNC image.
4. Started the container and mapped port `6080`.
5. Opened the browser VNC page and ran turtlesim.

## Console Commands

```bash
docker --version
docker run hello-world
docker pull tiryoh/ros2-desktop-vnc:humble
docker run -it --rm -p 6080:80 tiryoh/ros2-desktop-vnc:humble
```

## Telemetry

```text
http://127.0.0.1:6080/
```

The ROS2 desktop environment could be opened through the browser, making it possible to run graphical ROS2 tools inside a container.

## Debrief

- Docker helps isolate ROS2 environments and dependencies.
- Port mapping allows services inside a container to be accessed from the host.
- Browser-based VNC is useful for running GUI tools in a containerized workflow.

---

[Back to Mission Control](../README.md)


