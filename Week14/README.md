# Week 14 - Remote Camera Environment Configuration

## Lab Objective

This lab records remote camera setup through Termius, Tailscale, and a local camera bridge. The remote access note keeps the original HTTPS browser workflow used in the experiment.

## Folder Structure

<pre>
Week14/
|-- README.md              # weekly lab report
|-- 1.jpeg                 # screenshot
|-- 11.jpeg                # screenshot
</pre>

## Environment

- Termius
- Tailscale
- Python virtual environment
- Flask / camera bridge
- HTTPS local service endpoint

## Workflow

1. Create a virtual environment.
2. Install dependencies.
3. Start the camera bridge.
4. Access https://<tailscale-ip>:5000 from the mobile browser and allow the required camera permission.

## Commands

<pre><code class="language-bash">
python3 -m venv env
source env/bin/activate
python3 week12_starters/camera_bridge.py
</code></pre>

## Evidence

<img src="1.jpeg" width="800" alt="remote camera evidence">

<img src="11.jpeg" width="800" alt="remote setup evidence">

## Reflection

Remote robot experiments require both network access and careful browser permission handling.

---

[Back to Lab Navigator](../README.md)

