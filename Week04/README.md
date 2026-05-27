# Week 04 - PyBullet Quadruped Robot Simulation

> This week moved from ROS2 basics into physics simulation by loading and controlling a robot model in PyBullet.

## Overview

| Item | Content |
| --- | --- |
| Main topic | PyBullet robot simulation |
| Keywords | PyBullet, URDF, quadruped, physics simulation |
| Output | Four-legged robot simulation screenshot |

## Goals

- Set up a PyBullet physics simulation environment.
- Load robot models with URDF/SDF resources.
- Practice basic multi-joint robot motion and physical simulation concepts.

## Environment And Tools

- Ubuntu 24.04 LTS
- Python 3
- PyBullet
- VS Code / Terminal

## Task Workflow

1. Installed the PyBullet package.
2. Created a basic simulation world with gravity and a ground plane.
3. Loaded a quadruped robot model.
4. Observed robot posture and motion behavior in the simulation window.

## Key Commands

```bash
pip install pybullet
python3 simulation.py
```

## Result

<img src="./images/dog.png" width="720" alt="PyBullet quadruped robot simulation" />

The simulation demonstrated basic robot model loading and visual inspection inside the PyBullet GUI.

## What I Learned

- PyBullet provides a fast way to test robot models and physical interactions.
- URDF/SDF files describe robot geometry, joints, and physical properties.
- Simulation helps validate robot motion ideas before working with real hardware.
