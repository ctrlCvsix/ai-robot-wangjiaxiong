# AI Robot Mission Control

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:0F172A,45:0E7490,100:22C55E&text=AI%20ROBOT%20MISSION%20CONTROL&fontColor=F8FAFC&fontSize=34&fontAlignY=38&desc=ROS2%20%7C%20PyBullet%20%7C%20Docker%20%7C%20OpenCV%20%7C%20Remote%20Vision&descAlignY=58&animation=fadeIn" alt="AI Robot Mission Control banner" />

![ROS2](https://img.shields.io/badge/ROS2-signal%20online-0F172A?style=for-the-badge&logo=ros&logoColor=white)
![Python](https://img.shields.io/badge/Python-control%20core-14532D?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-orbital%20container-0E7490?style=for-the-badge&logo=docker&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-vision%20deck-7C2D12?style=for-the-badge&logo=opencv&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-ground%20station-7F1D1D?style=for-the-badge&logo=ubuntu&logoColor=white)

**A mission-style AI Robot course portfolio by Wang Jiaxiong**

[Mission Index](#mission-index) | [Telemetry Gallery](#telemetry-gallery) | [Control Stack](#control-stack) | [Hangar Map](#hangar-map)

</div>

---

## Control Room

This repository is designed as a **robotics mission log** rather than a plain assignment folder. Each week is treated as a mission: environment setup, ROS2 communication, simulation, vision, deployment, or remote camera operation.

| Call Sign | Detail |
| --- | --- |
| Operator | Wang Jiaxiong |
| Program | Software Engineering |
| Base | Shinhan University |
| Mission Domain | AI Robot development and experiment documentation |
| Current Mode | Course portfolio / robot lab archive |

## Mission Signature

- **Ground station setup**: Ubuntu, ROS2, GitHub, and repeatable documentation.
- **Robot motion lab**: turtlesim control, PyBullet quadruped simulation, robotic-arm IK, and Trot gait control.
- **Vision deck**: KITTI visualization, OpenCV experiments, RGB/depth/segmentation camera concepts, and ArUco testing.
- **Deployment bay**: Docker ROS2 desktop, browser VNC workflow, and GitHub Pages practice.
- **Remote operation**: Termius, Tailscale, Flask camera bridge, and mobile camera access.

## Telemetry Gallery

| Navigation Test | Simulation Bay | Sensor Deck |
| --- | --- | --- |
| <img src="./Week02/images/xiaowugui.png" width="260" alt="ROS2 turtlesim verification result" /> | <img src="./Week04/images/dog.png" width="260" alt="PyBullet quadruped simulation" /> | <img src="./Week06/images/zidongjiashi.png" width="260" alt="ROS2 KITTI visualization" /> |

| Deployment Console | Remote Vision Link |
| --- | --- |
| <img src="./Week11/514.png" width="360" alt="GitHub Pages deployment practice" /> | <img src="./Week14/1.jpeg" width="360" alt="Remote camera experiment" /> |

## Mission Index

| Mission | Codename | Objective | Status | Log |
| --- | --- | --- | --- | --- |
| Week02 | Ground Station | Ubuntu and ROS2 environment verification | Complete | [Open](./Week02) |
| Week03 | Turtle Vector | ROS2 topic publishing and path control | Complete | [Open](./Week03) |
| Week04 | Quadruped Bay | PyBullet robot model loading and motion simulation | Complete | [Open](./Week04) |
| Week05 | Arm Vision | Robotic-arm IK with RGB/depth/segmentation sensing | Complete | [Open](./Week05) |
| Week06 | Sensor Orbit | KITTI data publishing and RViz2 visualization | Complete | [Open](./Week06) |
| Week08 | Container Dock | Docker ROS2 desktop and browser VNC access | Complete | [Open](./Week08) |
| Week09 | Voice Channel | ROS2 voice interaction workflow | Complete | [Open](./Week09) |
| Week10 | Vision Forge | Docker concepts and OpenCV experiment | Complete | [Open](./Week10) |
| Week11 | Launch Pad | GitHub Pages deployment practice | Complete | [Open](./Week11) |
| Week13 | Trot Engine | Laikago Trot gait control in PyBullet | Complete | [Open](./Week13) |
| Week14 | Remote Lens | Termius, Tailscale, Flask camera bridge | Complete | [Open](./Week14) |
| Week15 | Debrief Deck | Final course notes and review space | Ready | [Open](./Week15) |
| Week16 | Expansion Slot | Next extended AI Robot mission | Ready | [Open](./Week16) |
| Week17 | Final Uplink | Next extended AI Robot mission | Ready | [Open](./Week17) |

## Control Stack

| Layer | Tools |
| --- | --- |
| Robot OS | ROS2 Humble / Jazzy, RViz2, RQT |
| Simulation | PyBullet, URDF models, Laikago, robotic arm IK |
| Vision | OpenCV, KITTI data, RGB/depth/segmentation, ArUco |
| Runtime | Ubuntu 24.04, Linux terminal, Docker |
| Code | Python, NumPy |
| Publishing | Git, GitHub, GitHub Pages |
| Remote Ops | Termius, Tailscale, Flask, mobile browser camera |

## Hangar Map

```text
ai-robot-wangjiaxiong/
|-- README.md             # Mission Control home
|-- Week02/               # Ground station: Ubuntu / ROS2 / turtlesim
|-- Week03/               # Turtle vector: ROS2 topic communication
|-- Week04/               # Quadruped bay: PyBullet simulation
|-- Week05/               # Arm vision: IK and virtual sensing
|-- Week06/               # Sensor orbit: KITTI and RViz2
|-- Week08/               # Container dock: Docker ROS2 desktop
|-- Week09/               # Voice channel: ROS2 voice interaction
|-- Week10/               # Vision forge: Docker and OpenCV
|-- Week11/               # Launch pad: GitHub Pages deployment
|-- Week13/               # Trot engine: quadruped gait control
|-- Week14/               # Remote lens: phone camera bridge
|-- Week15/               # Debrief deck: final notes
|-- Week16/               # Expansion slot
`-- Week17/               # Final uplink
```

## Navigation Protocol

1. Start from the [Mission Index](#mission-index).
2. Open any weekly mission log to see its objective, payload, command sequence, telemetry, and debrief.
3. Use the gallery and linked assets to inspect screenshots, videos, and experiment results.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:22C55E,55:0E7490,100:0F172A" alt="footer wave" />

</div>
