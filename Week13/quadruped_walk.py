import pybullet as p
import pybullet_data
import time
import math
import numpy as np


class LaikagoTrotController:
    def __init__(self, robot_id):
        self.robot_id = robot_id

        self.legs = {
            "FR": ["FR_hip_motor_2_chassis_joint",
                   "FR_upper_leg_2_hip_motor_joint",
                   "FR_lower_leg_2_upper_leg_joint"],

            "FL": ["FL_hip_motor_2_chassis_joint",
                   "FL_upper_leg_2_hip_motor_joint",
                   "FL_lower_leg_2_upper_leg_joint"],

            "RR": ["RR_hip_motor_2_chassis_joint",
                   "RR_upper_leg_2_chassis_joint",
                   "RR_lower_leg_2_upper_leg_joint"],

            "RL": ["RL_hip_motor_2_chassis_joint",
                   "RL_upper_leg_2_chassis_joint",
                   "RL_lower_leg_2_upper_leg_joint"],
        }

        self.joint_name_to_id = self.get_joint_name_to_id()
        self.leg_joint_ids = self.build_leg_joint_ids()

        # 站立姿态
        self.stand_angles = {
            "FR": [0.035, 0.70, -1.34],
            "FL": [-0.035, 0.70, -1.34],
            "RR": [0.035, 0.70, -1.34],
            "RL": [-0.035, 0.70, -1.34],
        }

        self.max_force = 170
        self.position_gain = 0.66
        self.velocity_gain = 0.45

    def get_joint_name_to_id(self):
        joint_name_to_id = {}

        print("机器人关节列表：")
        for i in range(p.getNumJoints(self.robot_id)):
            info = p.getJointInfo(self.robot_id, i)
            joint_name = info[1].decode("utf-8")
            joint_name_to_id[joint_name] = i
            print(i, joint_name)

        return joint_name_to_id

    def build_leg_joint_ids(self):
        """
        兼容不同 pybullet_data 版本中的 Laikago 关节命名。
        有些版本是 upper_leg_2_hip_motor_joint，
        有些版本是 upper_leg_2_chassis_joint。
        """
        result = {}

        for leg in ["FR", "FL", "RR", "RL"]:
            hip = f"{leg}_hip_motor_2_chassis_joint"

            upper_candidates = [
                f"{leg}_upper_leg_2_hip_motor_joint",
                f"{leg}_upper_leg_2_chassis_joint"
            ]

            lower = f"{leg}_lower_leg_2_upper_leg_joint"

            upper = None
            for name in upper_candidates:
                if name in self.joint_name_to_id:
                    upper = name
                    break

            if hip not in self.joint_name_to_id or upper is None or lower not in self.joint_name_to_id:
                raise RuntimeError(f"{leg} 腿关节识别失败，请检查打印出来的关节名称。")

            result[leg] = [
                self.joint_name_to_id[hip],
                self.joint_name_to_id[upper],
                self.joint_name_to_id[lower],
            ]

        return result

    def set_leg_angles(self, leg, angles, force=None):
        if force is None:
            force = self.max_force

        for joint_id, angle in zip(self.leg_joint_ids[leg], angles):
            p.setJointMotorControl2(
                bodyUniqueId=self.robot_id,
                jointIndex=joint_id,
                controlMode=p.POSITION_CONTROL,
                targetPosition=angle,
                force=force,
                positionGain=self.position_gain,
                velocityGain=self.velocity_gain
            )

    def reset_to_stand_pose(self):
        for leg, joint_ids in self.leg_joint_ids.items():
            for joint_id, angle in zip(joint_ids, self.stand_angles[leg]):
                p.resetJointState(self.robot_id, joint_id, angle, 0)

    def stand(self):
        for leg in self.leg_joint_ids:
            self.set_leg_angles(leg, self.stand_angles[leg], force=self.max_force)

    @staticmethod
    def smoothstep(s):
        s = max(0.0, min(1.0, s))
        return s * s * (3.0 - 2.0 * s)

    def trot(self, t, frequency=1.25, ramp=1.0):
        """
        更稳定的简化 Trot：
        - 对角腿同步
        - 支撑相：大腿向后推地
        - 摆动相：大腿向前摆，同时小腿抬起
        """

        duty = 0.58
        stride_amp = 0.28 * ramp
        lift_amp = 0.12 * ramp
        hip_sway_amp = 0.025 * ramp

        for leg in self.leg_joint_ids:
            if leg in ["FR", "RL"]:
                phase = 0.0
            else:
                phase = 0.5

            cycle = (frequency * t + phase) % 1.0
            base_hip, base_thigh, base_calf = self.stand_angles[leg]

            hip = base_hip + hip_sway_amp * math.sin(2 * math.pi * cycle)
            thigh = base_thigh
            calf = base_calf

            if cycle < duty:
                # 支撑相：脚贴地，腿向后扫来推动身体。
                progress = self.smoothstep(cycle / duty)

                stride = stride_amp * (0.5 - progress)
                lift = 0.0

            else:
                # 摆动相：腿向前回摆，同时抬脚避免拖地。
                progress = self.smoothstep((cycle - duty) / (1.0 - duty))

                stride = stride_amp * (progress - 0.5)
                lift = math.sin(math.pi * progress)

            # The course start orientation swaps body axes, so this sign matches
            # the observed forward direction for the free Laikago model.
            thigh = base_thigh - stride - 1.15 * lift_amp * lift
            calf = base_calf - 1.80 * lift_amp * lift

            self.set_leg_angles(leg, [hip, thigh, calf], force=self.max_force)


def main():
    p.connect(p.GUI)
    p.resetSimulation()

    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    p.setGravity(0, 0, -9.8)
    p.setTimeStep(1 / 240)

    p.setPhysicsEngineParameter(
        fixedTimeStep=1 / 240,
        numSolverIterations=160,
        numSubSteps=4
    )

    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

    plane_id = p.loadURDF("plane.urdf")
    p.changeDynamics(
        plane_id,
        -1,
        lateralFriction=2.0,
        spinningFriction=0.08,
        rollingFriction=0.02
    )

    # 保留你的姿态，不改
    start_orientation = p.getQuaternionFromEuler([math.pi / 2, 0, math.pi / 2])

    robot_id = p.loadURDF(
        "laikago/laikago_toes.urdf",
        [0, 0, 0.48],
        start_orientation,
        flags=p.URDF_USE_SELF_COLLISION
    )

    for i in range(-1, p.getNumJoints(robot_id)):
        p.changeDynamics(
            robot_id,
            i,
            lateralFriction=1.8,
            spinningFriction=0.08,
            rollingFriction=0.02,
            linearDamping=0.04,
            angularDamping=0.04
        )

    controller = LaikagoTrotController(robot_id)

    controller.reset_to_stand_pose()

    p.resetBasePositionAndOrientation(
        robot_id,
        [0, 0, 0.48],
        start_orientation
    )
    p.resetBaseVelocity(robot_id, [0, 0, 0], [0, 0, 0])

    dt = 1 / 240
    sim_t = 0.0

    print("先稳定站立 5 秒...")

    for _ in range(1200):
        controller.stand()
        p.stepSimulation()
        time.sleep(dt)
        sim_t += dt

    print("开始 Trot 行走...")

    try:
        while True:
            walk_t = sim_t - 5.0

            # 5 秒渐进启动，防止突然发力翻倒
            ramp = min(1.0, max(0.0, walk_t / 5.0))

            controller.trot(
                t=walk_t,
                frequency=1.25,
                ramp=ramp
            )

            p.stepSimulation()
            time.sleep(dt)
            sim_t += dt

    except KeyboardInterrupt:
        print("仿真结束")

    p.disconnect()


if __name__ == "__main__":
    main()
