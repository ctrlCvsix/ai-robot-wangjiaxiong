# Week 08 - Docker ROS2 Desktop Container

## Lab Objective

This lab runs ROS2 desktop tools from a Docker container and accesses them through a browser interface.

## Folder Structure

<pre>
Week08/
|-- README.md              # weekly lab report
|-- screenshots/           # recommended evidence
</pre>

## Environment

- Docker
- ROS2 desktop image
- Browser VNC

## Workflow

1. Start the ROS2 desktop container.
2. Map the access port.
3. Run GUI-based ROS2 tools.

## Commands

<pre><code class="language-bash">
docker run -it --rm -p 6080:80 tiryoh/ros2-desktop-vnc:humble
</code></pre>

## Evidence

The container desktop can be opened through the mapped browser interface.

## Reflection

Docker reduces environment drift between machines.

---

[Back to Lab Navigator](../README.md)
