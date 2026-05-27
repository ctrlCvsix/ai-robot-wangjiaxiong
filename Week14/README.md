# Mission Log 14 - Remote Calling And Camera Environment Configuration

> Mission focus: this week recorded the process of using a phone with Termius and Tailscale to remotely control a computer, configure Python dependencies, and run a Flask camera service.

## Mission Brief

| Item | Content |
| --- | --- |
| Main topic | Remote access and camera bridge experiment |
| Keywords | Termius, Tailscale, Flask, virtual environment, ArUco |
| Output | Remote camera workflow and test screenshots |

## Objectives

- Use a phone to remotely connect to the computer through Termius.
- Keep both devices reachable with Tailscale.
- Solve Python dependency issues using a virtual environment.
- Start a Flask camera bridge service and test mobile camera access.

## Payload

- Ubuntu 24.04
- Python virtual environment
- Termius
- Tailscale
- Flask
- Mobile browser camera
- ArUco marker test

## Command Sequence

1. Cloned the course project on the remote machine.
2. Created and activated a Python virtual environment.
3. Installed dependencies from `requirements.txt`.
4. Started the Flask camera bridge service.
5. Opened the service from the mobile browser through the Tailscale network.
6. Tested image collection and ArUco marker detection.

## Console Commands

```bash
cd ~/ai-robot-class.github.io
python3 -m venv env
source env/bin/activate
pip install -r week12_starters/requirements.txt
python3 week12_starters/camera_bridge.py
```

## Telemetry

<img src="./1.jpeg" width="720" alt="Remote camera experiment screenshot" />

<img src="./11.jpeg" width="720" alt="Remote camera and environment configuration result" />

Captured calibration images were saved to:

```text
/home/wang-jiaxiong/ai-robot-class.github.io/calib_images
```

## Operator Notes

- The phone and computer must both be connected to Tailscale.
- The browser may require manually accepting the self-signed HTTPS warning.
- Camera permission must be allowed in the mobile browser.
- Press `Ctrl + C` in Termius to stop the Flask server.

## Debrief

- Remote robot experiments require both network connectivity and environment management.
- Python virtual environments are the cleanest way to avoid dependency conflicts such as PEP 668 restrictions.
- Mobile cameras can be integrated into robot vision workflows through a web service bridge.

---

[Back to Mission Control](../README.md)


