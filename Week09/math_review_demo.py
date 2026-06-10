import math
from collections import deque

print("Week 9：机器人与机器视觉数学基础")
print("--------------------------------")

# 1. 二维旋转矩阵验证
theta = math.radians(45)
point = [1.0, 0.0]

rotated_x = math.cos(theta) * point[0] - math.sin(theta) * point[1]
rotated_y = math.sin(theta) * point[0] + math.cos(theta) * point[1]

print("1. 二维旋转矩阵验证")
print(f"原始点: ({point[0]:.2f}, {point[1]:.2f})")
print("旋转角度: 45 度")
print(f"旋转后: ({rotated_x:.2f}, {rotated_y:.2f})")

print("--------------------------------")

# 2. 简单 BFS 路径规划
print("2. BFS 路径规划演示")

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

queue = deque()
queue.append((start, [start]))
visited = set()
visited.add(start)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
path = []

while queue:
    (x, y), current_path = queue.popleft()

    if (x, y) == goal:
        path = current_path
        break

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            if grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), current_path + [(nx, ny)]))

print(f"起点: {start}")
print(f"终点: {goal}")
print(f"路径: {path}")

print("--------------------------------")
print("程序结束")
