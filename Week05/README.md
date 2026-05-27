# Week 05 - Robotic Arm IK And Visual Simulation

> This week focused on robotic-arm inverse kinematics and simulated visual sensing in PyBullet.

## Overview

| Item | Content |
| --- | --- |
| Main topic | Robotic arm control and camera simulation |
| Keywords | PyBullet, inverse kinematics, RGB, depth, segmentation |
| Output | Robotic-arm motion video and sensor-view experiment |

## Goals

- Load a complex robotic-arm URDF model in PyBullet.
- Use inverse kinematics to move the end effector toward target positions.
- Configure virtual camera outputs for RGB, depth, and segmentation data.

## Environment And Tools

- Ubuntu 24.04 LTS
- Python 3
- PyBullet
- Synthetic camera data

## Task Workflow

1. Built a simulated scene with a table and robotic arm.
2. Checked the initial end-effector position: `(0.835, 0.100, 1.435)`.
3. Used `calculateInverseKinematics` to calculate joint positions.
4. Captured multiple camera views from the simulation.

## Key Commands

```python
joint_poses = p.calculateInverseKinematics(robot_id, end_effector_id, target_position)
```

## Result

[View experiment video](./images/jixiebi.webm)

The experiment showed robotic-arm movement together with RGB, depth, and segmentation camera outputs.

## What I Learned

- Inverse kinematics converts a target end-effector pose into joint angles.
- Virtual cameras can simulate perception data used by robot vision systems.
- Combining motion control and visual sensing is a key step toward intelligent manipulation.
