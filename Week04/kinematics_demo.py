import math
import time

x = 0.0
y = 0.0
theta = 0.0

v_left = 1.0
v_right = 1.5
wheel_base = 0.5
dt = 0.5

print("Week 4：二维机器人运动学仿真")
print("-----------------------------")

for step in range(10):
    v = (v_left + v_right) / 2
    omega = (v_right - v_left) / wheel_base

    x = x + v * math.cos(theta) * dt
    y = y + v * math.sin(theta) * dt
    theta = theta + omega * dt

    print(f"Step {step + 1}: x={x:.2f}, y={y:.2f}, theta={theta:.2f}")
    time.sleep(0.2)

print("-----------------------------")
print("仿真结束")
