import time

print("Week 13：四足机器人步态模拟")
print("--------------------------------")

print("四足机器人基本结构：")
print("LF：左前腿")
print("RF：右前腿")
print("LH：左后腿")
print("RH：右后腿")

print("--------------------------------")
print("开始模拟 Trot 对角步态")

for step in range(1, 7):
    print(f"Step {step}")

    if step % 2 == 1:
        print("支撑腿：LF 左前腿 + RH 右后腿")
        print("摆动腿：RF 右前腿 + LH 左后腿")
    else:
        print("支撑腿：RF 右前腿 + LH 左后腿")
        print("摆动腿：LF 左前腿 + RH 右后腿")

    print("身体保持平衡，进入下一步")
    print("--------------------------------")
    time.sleep(0.3)

print("四足机器人步态模拟完成")
print("项目核心功能测试完成")
