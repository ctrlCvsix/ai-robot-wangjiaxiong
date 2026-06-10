import time

print("Week 6：闭环控制与避障逻辑模拟")
print("--------------------------------")

front_distance = 0.3
safe_distance = 0.8

print(f"当前前方距离: {front_distance} m")
print(f"安全距离阈值: {safe_distance} m")

if front_distance < safe_distance:
    print("检测到前方障碍物，开始避障")

    for i in range(3):
        print(f"第 {i + 1} 次后退")
        time.sleep(0.5)

        print(f"第 {i + 1} 次左转")
        time.sleep(0.5)

    print("避障动作完成")
else:
    print("前方安全，继续前进")

print("--------------------------------")
print("程序结束")
