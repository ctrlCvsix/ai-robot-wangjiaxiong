# Week 13 - Quadruped Robot Trot Gait Simulation

> This week focused on implementing a simple quadruped robot simulation with a Trot gait controller in PyBullet.

## Overview

| Item | Content |
| --- | --- |
| Main topic | Quadruped gait control |
| Keywords | PyBullet, Laikago, Trot gait, NumPy, joint control |
| Output | Python simulation script: `trot.py` |

## Goals

- Load a Laikago quadruped robot model in PyBullet.
- Read and control leg joints through Python.
- Generate a simple Trot gait using phase-shifted sine motion.
- Observe periodic leg motion in simulation.

## Environment And Tools

- Python 3
- PyBullet
- NumPy
- Laikago URDF model

## Task Workflow

1. Initialized the PyBullet GUI simulation.
2. Loaded the ground plane and Laikago robot model.
3. Created a `QuadrupedController` class for joint control.
4. Used diagonal leg phase pairing for a basic Trot gait.
5. Repeated simulation steps until manually stopped.

## Key Commands

```bash
pip install pybullet numpy --break-system-packages
python3 trot.py
```

## Result

The simulation runs a simple Trot-style movement where diagonal legs move in synchronized phases.

Core file:

```text
Week13/trot.py
```

## What I Learned

- Trot gait can be approximated with phase differences between diagonal leg pairs.
- PyBullet joint position control is useful for quick gait experiments.
- Even a simplified gait controller helps explain the relationship between timing, leg movement, and robot stability.
