# Mission Log 09 - ROS2 Voice Interaction

> Mission focus: this week focused on the concept of voice interaction in ROS2 and how speech-related nodes can communicate through topics.

## Mission Brief

| Item | Content |
| --- | --- |
| Main topic | ROS2 voice interaction |
| Keywords | ROS2, speech recognition, TTS, topic communication |
| Output | Voice interaction workflow notes and topic tests |

## Objectives

- Understand how voice commands can connect with ROS2 nodes.
- Practice checking ROS2 topics related to speech input or TTS output.
- Review how message flow can be used for human-robot interaction.

## Payload

- ROS2
- Terminal
- Demo ROS2 nodes
- Voice interaction concept workflow

## Command Sequence

1. Listed active ROS2 topics.
2. Echoed a speech-related topic to inspect message output.
3. Ran ROS2 demo nodes to review topic communication.
4. Connected the idea of voice commands with robot control logic.

## Console Commands

```bash
ros2 topic list
ros2 topic echo /tts/speak
ros2 run demo_nodes_cpp talker
```

## Telemetry

The experiment clarified how speech recognition or text-to-speech components can be represented as ROS2 nodes and topics.

## Debrief

- Voice interaction can be modeled as a ROS2 communication pipeline.
- Topic inspection helps debug whether speech-related messages are being published.
- Human-robot interaction depends on reliable message flow between perception, decision, and action nodes.

---

[Back to Mission Control](../README.md)


