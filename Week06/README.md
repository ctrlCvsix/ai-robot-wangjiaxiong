# Mission Log 06 - KITTI Data Publishing And RViz2 Visualization

> Mission focus: this week focused on publishing autonomous-driving sensor data in ROS2 and visualizing it with RViz2 and RQT.

## Mission Brief

| Item | Content |
| --- | --- |
| Main topic | ROS2 sensor data visualization |
| Keywords | KITTI, PointCloud2, Image, RViz2, RQT |
| Output | Multi-sensor visualization screenshot |

## Objectives

- Read and organize KITTI-style sensor data.
- Publish point cloud and image data as ROS2 topics.
- Use RViz2 and RQT to inspect synchronized sensor streams.

## Payload

- Ubuntu 24.04 LTS
- ROS2 Jazzy / Humble
- KITTI Raw Dataset
- RViz2 / RQT

## Command Sequence

1. Stored KITTI data under `~/ros2_ws/data`.
2. Ran the custom publisher node.
3. Published point cloud and camera image topics.
4. Visualized the results with RViz2 and RQT.

## Console Commands

```bash
ros2 run ros2_kitti_publishers publisher_node
rviz2
rqt
```

## Telemetry

<img src="./images/zidongjiashi.png" width="720" alt="KITTI sensor data visualization in ROS2" />

The visualization confirmed that image and point-cloud data could be published and inspected in ROS2 tools.

## Debrief

- ROS2 can represent sensor streams with standardized message types.
- RViz2 is useful for checking spatial data such as point clouds.
- Multi-sensor visualization is important for autonomous-driving and robot perception tasks.

---

[Back to Mission Control](../README.md)


