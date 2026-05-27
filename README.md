# AI Robot Course Portfolio

<div align="center">

![ROS2](https://img.shields.io/badge/ROS2-Humble%20%7C%20Jazzy-22314E?style=for-the-badge&logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

**Shinhan University AI Robot Course Practice Repository**

From Linux and ROS2 fundamentals to Docker, OpenCV, PyBullet simulation, sensor visualization, and remote robot experiments.

[Weekly Learning Map](#weekly-learning-map) • [Highlights](#highlights) • [Repository Structure](#repository-structure)

</div>

---

## About

This repository records my weekly practice for the **AI Robot** course. It combines environment setup, command-line practice, ROS2 communication, robot simulation, Docker containers, computer vision, GitHub Pages deployment, and remote camera experiments.

| Field | Detail |
| --- | --- |
| Author | Wang Jiaxiong |
| Major | Software Engineering |
| University | Shinhan University |
| Focus | AI Robot development, ROS2, simulation, vision, deployment |

## Highlights

- Built ROS2 development environments on Ubuntu and practiced topic/node workflows.
- Simulated robot motion with PyBullet, including quadruped motion and robotic-arm inverse kinematics.
- Used RViz2/RQT to visualize KITTI-style autonomous-driving sensor data.
- Practiced Docker-based ROS2 desktop environments and OpenCV experiments.
- Documented remote access workflows with Termius, Tailscale, Flask, and mobile camera testing.

## Featured Results

| ROS2 Turtlesim | PyBullet Quadruped | Sensor Visualization |
| --- | --- | --- |
| <img src="./Week02/images/xiaowugui.png" width="260" alt="ROS2 turtlesim result" /> | <img src="./Week04/images/dog.png" width="260" alt="PyBullet quadruped simulation" /> | <img src="./Week06/images/zidongjiashi.png" width="260" alt="ROS2 KITTI visualization" /> |

| Docker / Pages Practice | Remote Camera Experiment |
| --- | --- |
| <img src="./Week11/514.png" width="360" alt="Docker and GitHub Pages practice" /> | <img src="./Week14/1.jpeg" width="360" alt="Remote camera experiment" /> |

## Weekly Learning Map

| Week | Topic | Main Practice | Link |
| --- | --- | --- | --- |
| Week02 | Ubuntu and ROS2 environment setup | Turtlesim environment verification | [Open](./Week02) |
| Week03 | ROS2 topics and path control | Turtlesim topic communication | [Open](./Week03) |
| Week04 | PyBullet quadruped simulation | Robot model loading and motion simulation | [Open](./Week04) |
| Week05 | Robotic-arm IK and visual simulation | Inverse kinematics, RGB/depth/segmentation camera | [Open](./Week05) |
| Week06 | KITTI publishing and RViz2 visualization | Point cloud and image topic visualization | [Open](./Week06) |
| Week08 | Docker ROS2 desktop | Container setup and browser access | [Open](./Week08) |
| Week09 | ROS2 voice interaction | Voice interaction workflow notes | [Open](./Week09) |
| Week10 | Docker concepts and OpenCV | Container and vision experiment | [Open](./Week10) |
| Week11 | Docker advanced and GitHub Pages | Static site deployment practice | [Open](./Week11) |
| Week13 | Quadruped gait simulation | Laikago model and Trot gait control | [Open](./Week13) |
| Week14 | Remote calling and environment configuration | Termius, Tailscale, Flask camera bridge | [Open](./Week14) |
| Week15 | Final course notes | In progress | [Open](./Week15) |
| Week16 | Extended course practice | To be updated with the Week16 task | [Open](./Week16) |
| Week17 | Extended course practice | To be updated with the Week17 task | [Open](./Week17) |

## Tech Stack

| Area | Tools |
| --- | --- |
| Robot framework | ROS2 Humble / Jazzy, RViz2, RQT |
| Simulation | PyBullet, URDF models |
| Vision | OpenCV, RGB/depth/segmentation data |
| Runtime | Ubuntu 24.04, Linux command line, Docker |
| Programming | Python, NumPy |
| Collaboration | Git, GitHub, GitHub Pages |
| Remote workflow | Termius, Tailscale, Flask |

## Repository Structure

```text
ai-robot-wangjiaxiong/
├── README.md
├── Week02/              # Ubuntu / ROS2 / turtlesim
├── Week03/              # ROS2 topic communication
├── Week04/              # PyBullet quadruped simulation
├── Week05/              # Robotic arm IK and visual sensing
├── Week06/              # KITTI data and RViz2 visualization
├── Week08/              # Docker ROS2 desktop
├── Week09/              # ROS2 voice interaction
├── Week10/              # Docker and OpenCV
├── Week11/              # GitHub Pages deployment
├── Week13/              # Trot gait simulation
├── Week14/              # Remote camera experiment
├── Week15/              # Final notes
├── Week16/              # Extended practice
└── Week17/              # Extended practice
```

## How To Explore

1. Start with the [Weekly Learning Map](#weekly-learning-map).
2. Open a week folder to read the experiment goal, environment, commands, and result notes.
3. Check image and video assets inside weekly folders for screenshots and demonstrations.

## Learning Goals

- Understand ROS2 node, topic, and visualization workflows.
- Build confidence with Linux, Docker, Git, and GitHub-based project organization.
- Practice Python robot programming and simulation.
- Connect AI robot concepts with real sensor, camera, and remote-control experiments.

---

<div align="center">

**AI Robot learning archive by Wang Jiaxiong**

</div>
