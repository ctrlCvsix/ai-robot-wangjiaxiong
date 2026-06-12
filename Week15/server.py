#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""方向 A 常驻程序：PyBullet 迷宫 + 四足机器人 + WebSocket 遥控服务。

一个程序里同时做三件事（本周的核心工程原则——单一常驻程序）：
  1) 监听网络（WebSocket），接收手机网页发来的控制命令；
  2) 推进 PyBullet 仿真，并做墙体碰撞检测、终点判定；
  3) 把机器人状态 + 迷宫信息回传给网页，让网页画出俯视图。

迷宫本身在 maze.py 里定义；想换地图只改 maze.py。
"""
import asyncio
import json
import math
import os
import time
from datetime import datetime
from pathlib import Path

from aiohttp import WSMsgType, web
import pybullet as p
import pybullet_data

import maze as maze_module
import agent as agent_module


HOST = "0.0.0.0"
PORT = 8765
ROBOT_HEIGHT = 0.45
DOG_RADIUS = 0.18          # 机器狗碰撞半径（缩小后可通过更窄通道）
MOVE_SPEED = 0.9           # 前进速度（米/秒）
TURN_SPEED = 1.6           # 转向速度（弧度/秒）

# 自动导航参数
WAYPOINT_THRESHOLD = 0.4   # 到达路点的距离阈值（米）
ANGLE_THRESHOLD = 0.12     # 朝向对齐阈值（弧度），越小越精确但越慢
STUCK_TIMEOUT = 2.0        # 卡住超时（秒），超时重新规划

# Agent 参数（v3: 只在岔路口调用，不需要决策间隔）

# 右手法则参数
RH_DECISION_INTERVAL = 0.8      # 右手法则决策间隔（秒）
RH_MAX_DURATION = 60.0          # 右手法则最长运行时间，超时回退 BFS

# 轨迹日志
LOG_DIR = Path(__file__).parent / "logs"


class MazeDogServer:
    def __init__(self):
        # 优先开 GUI 窗口（noVNC 桌面 / 本机有显示时）；无显示则退回 DIRECT 无头模式
        self.gui = False
        want_gui = os.environ.get("PYBULLET_GUI", "1") != "0"
        if want_gui:
            try:
                self.physics_client = p.connect(p.GUI)
                self.gui = True
            except Exception:
                self.physics_client = p.connect(p.DIRECT)
        else:
            self.physics_client = p.connect(p.DIRECT)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        p.setTimeStep(1.0 / 120.0)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

        self.maze = maze_module.build_maze()
        self.wall_aabbs = self.maze["aabbs"]
        self.goal = self.maze["goal"]                       # (x, y, r)
        sx, sy = self.maze["start"]
        self.start_pose = (sx, sy, ROBOT_HEIGHT)

        self.robot_id = None
        self.command = {"move": 0.0, "turn": 0.0}
        self.blocked = False
        self.goal_reached = False
        self.continuous_yaw = 0.0   # 连续朝向（不受 ±π 限制）

        # 自动探索状态
        self.auto_mode = False         # False | "bfs" | "agent"
        self.waypoints = []            # [(x, y), ...] 路点列表
        self.waypoint_idx = 0
        self.stuck_timer = 0.0         # 卡住计时器

        # Agent 状态
        self.agent = None              # 延迟初始化（需要 API key）
        self.agent_timer = 0.0         # 距上次决策的累计时间
        self.agent_decision = None     # 最近一次 Agent 决策
        self.agent_failures = 0        # 连续失败计数
        self.agent_reasoning = ""      # 最近一次推理文本（前端展示用）
        self.agent_latency_ms = 0      # 最近一次 API 延迟
        self.agent_enabled = False     # API key 是否可用

        # 记忆：走过的格子和最近动作
        self.visited_cells = []
        self.recent_actions = []

        # 防打转：格子访问计数 + 死胡同黑名单
        self.cell_visit_count = {}        # {(cx,cy): count}
        self.blacklisted_cells = set()    # 禁止再进入的格子
        self._stuck_position = None
        self._turn_streak = 0
        self._agent_asked_at_idx = -1     # 避免同一岔路口重复问 Agent

        # 右手法则状态
        self.rh_timer = 0.0          # 决策计时器
        self.rh_decision = None      # 当前决策
        self.rh_start_time = 0.0     # 启动时间

        # 轨迹日志
        self._log_file = None
        self._log_events = []
        self._trajectory = []        # [(x, y, ts), ...]
        self._mode_start_time = 0.0

        self._build_world()

        if self.gui:
            center = self.maze["size"] / 2.0
            p.resetDebugVisualizerCamera(
                cameraDistance=self.maze["size"] * 0.95,
                cameraYaw=45, cameraPitch=-55,
                cameraTargetPosition=[center, center, 0],
            )

    def _build_world(self):
        p.loadURDF("plane.urdf")
        self._build_maze()
        self._build_markers()
        self.robot_id = self._load_robot()
        self.reset_robot()

    def _build_maze(self):
        color = [0.27, 0.40, 0.62, 1.0]
        h = self.maze["wall_height"]
        for cx, cy, hx, hy in self.maze["walls"]:
            half = [hx, hy, h]
            collision = p.createCollisionShape(p.GEOM_BOX, halfExtents=half)
            visual = p.createVisualShape(p.GEOM_BOX, halfExtents=half, rgbaColor=color)
            p.createMultiBody(
                baseMass=0,
                baseCollisionShapeIndex=collision,
                baseVisualShapeIndex=visual,
                basePosition=[cx, cy, h],
            )

    def _build_markers(self):
        gx, gy, gr = self.goal
        # 终点：绿色圆盘
        goal_vis = p.createVisualShape(
            p.GEOM_CYLINDER, radius=gr, length=0.04, rgbaColor=[0.13, 0.77, 0.37, 0.9]
        )
        p.createMultiBody(baseMass=0, baseVisualShapeIndex=goal_vis,
                          basePosition=[gx, gy, 0.02])
        # 起点：橙色圆盘
        sx, sy = self.maze["start"]
        start_vis = p.createVisualShape(
            p.GEOM_CYLINDER, radius=gr * 0.8, length=0.04, rgbaColor=[0.96, 0.62, 0.07, 0.85]
        )
        p.createMultiBody(baseMass=0, baseVisualShapeIndex=start_vis,
                          basePosition=[sx, sy, 0.02])

    def _load_robot(self):
        for urdf in ("laikago/laikago_toes.urdf", "laikago/laikago.urdf"):
            try:
                return p.loadURDF(urdf, list(self.start_pose), useFixedBase=False,
                                  globalScaling=0.55)
            except Exception:
                continue
        raise RuntimeError("无法在 pybullet_data 中加载四足机器人 URDF。")

    def reset_robot(self):
        quat = p.getQuaternionFromEuler([0.0, 0.0, 0.0])
        p.resetBasePositionAndOrientation(self.robot_id, self.start_pose, quat)
        p.resetBaseVelocity(self.robot_id, [0, 0, 0], [0, 0, 0])
        self.command = {"move": 0.0, "turn": 0.0}
        self.blocked = False
        self.goal_reached = False
        self.continuous_yaw = 0.0   # 连续朝向（不受 ±π 限制）
        self.auto_mode = False
        self.waypoints = []
        self.waypoint_idx = 0
        self.stuck_timer = 0.0
        self.agent_timer = 0.0
        self.agent_decision = None
        self.agent_failures = 0
        self.agent_reasoning = ""
        self.agent_latency_ms = 0
        self.visited_cells = []
        self.recent_actions = []
        self.rh_timer = 0.0
        self._stuck_position = None
        self._turn_streak = 0
        self.rh_decision = None
        self.cell_visit_count = {}
        self.blacklisted_cells = set()
        self._flush_log()

    # ── 自动探索 ────────────────────────────────────────────

    @staticmethod
    def _norm_angle(a):
        """将角度规约到 [-pi, pi]。"""
        while a > math.pi:
            a -= 2 * math.pi
        while a < -math.pi:
            a += 2 * math.pi
        return a

    def start_auto_explore(self):
        """启动自动探索：BFS 寻路并进入导航模式。"""
        self.waypoints = maze_module.find_path(self.maze)
        if not self.waypoints:
            print("[auto] 未找到路径")
            return
        self.waypoint_idx = 0
        self.auto_mode = True
        self.stuck_timer = 0.0
        print(f"[auto] 开始自动探索，共 {len(self.waypoints)} 个路点")

    # ── 右手法则导航（Agent 失败时的兜底） ──────────────

    def _scan_4dir(self, rx, ry, yaw):
        """快速 4 方向扫描，返回 {'front','right','left','back': bool}（True=空）。"""
        return {
            d: not self._check_wall_at(rx, ry, yaw, d, 0.6)
            for d in ("front", "right", "left", "back")
        }

    def _check_wall_at(self, rx, ry, yaw, direction, dist=0.65):
        """检测机器人某方向 dist 米处是否有墙。direction: 'front','right','left','back'"""
        offsets = {
            "front": 0, "right": -math.pi/2, "left": math.pi/2, "back": math.pi,
        }
        a = yaw + offsets[direction]
        cx = rx + math.cos(a) * dist
        cy = ry + math.sin(a) * dist
        r = DOG_RADIUS
        for min_x, min_y, max_x, max_y in self.wall_aabbs:
            if (min_x - r) <= cx <= (max_x + r) and (min_y - r) <= cy <= (max_y + r):
                return True
        return False

    def _right_hand_navigate(self, dt):
        """右手法则导航 v2：支持拐弯完成检测 + 倒车防卡 + 死胡同脱困 + 黑名单。"""
        if self.goal_reached:
            self._log("goal_reached", {"mode": "right_hand"})
            self.stop_auto()
            return

        self.rh_timer += dt
        elapsed = time.time() - self.rh_start_time

        # 访问计数（右手法则也需要防打转）
        position, _ = p.getBasePositionAndOrientation(self.robot_id)
        rx, ry = position[0], position[1]
        cc = maze_module.cell_from_position(self.maze, rx, ry)
        self.cell_visit_count[cc] = self.cell_visit_count.get(cc, 0) + 1
        if self.cell_visit_count[cc] > 5:
            self.blacklisted_cells.add(cc)

        # 超时：右手法则太久 → BFS 接管
        if elapsed > RH_MAX_DURATION:
            self._log("fallback", {"from": "right_hand", "to": "bfs",
                        "reason": f"右手法则运行 {elapsed:.0f}s 超时"})
            print(f"[rh] 超时 {elapsed:.0f}s，回退到 BFS")
            self.auto_mode = "bfs"
            self.waypoints = maze_module.find_path(self.maze)
            self.waypoint_idx = 0
            self.stuck_timer = 0.0
            return

        if self.rh_timer < RH_DECISION_INTERVAL:
            return
        self.rh_timer = 0.0

        position, orientation = p.getBasePositionAndOrientation(self.robot_id)
        yaw = p.getEulerFromQuaternion(orientation)[2]
        rx, ry = position[0], position[1]

        # 用稍大的检测距离判断方向是否有墙
        right_open = not self._check_wall_at(rx, ry, yaw, "right", 0.7)
        front_open = not self._check_wall_at(rx, ry, yaw, "front", 0.7)
        left_open = not self._check_wall_at(rx, ry, yaw, "left", 0.7)
        back_open = not self._check_wall_at(rx, ry, yaw, "back", 0.7)

        # 死胡同脱困：三面墙 + 连续 blocked → 原地转 120° 找路
        if self.blocked and not right_open and not front_open and not left_open:
            self._log("rh_escape", {"maneuver": "spin if blocked"})
            print("[rh] 三面墙且 blocked，原地右转脱困")
            self.set_command(0.0, 1.0)  # 原地右转
            return

        # 倒车防卡：如果上次倒车但 blocked=true，说明倒车撞墙，换策略
        prev_action = self.recent_actions[-1] if self.recent_actions else ""
        if self.blocked and "back" in prev_action:
            self._log("rh_escape", {"maneuver": "back-blocked, turn right"})
            print("[rh] 倒车撞墙，右转 90° 脱困")
            self.set_command(0.0, 1.0)
            self.recent_actions.append("rh:escape_turn")
            return

        # 检查各方向是否会进入黑名单格子
        current_cell = maze_module.cell_from_position(self.maze, rx, ry)
        def _would_enter_blacklisted(direction):
            a = yaw + {"right": -math.pi/2, "front": 0, "left": math.pi/2, "back": math.pi}[direction]
            cx = rx + math.cos(a) * 1.2
            cy = ry + math.sin(a) * 1.2
            next_cell = maze_module.cell_from_position(self.maze, cx, cy)
            return next_cell in self.blacklisted_cells

        right_blacklisted = _would_enter_blacklisted("right")
        front_blacklisted = _would_enter_blacklisted("front")
        left_blacklisted = _would_enter_blacklisted("left")

        # 右手法则优先级：右转 > 直行 > 左转 > 倒车（跳过黑名单方向）
        if right_open and not right_blacklisted:
            action = "right"
            self.set_command(0.0, 1.0)
        elif front_open and not front_blacklisted:
            action = "forward"
            self.set_command(1.0, 0.0)
        elif left_open and not left_blacklisted:
            action = "left"
            self.set_command(0.0, -1.0)
        elif back_open:
            action = "back"
            self.set_command(-1.0, 0.0)
        else:
            # 所有方向都堵了或黑名单 → 原地右转找路
            action = "right"
            self.set_command(0.0, 1.0)

        self.recent_actions.append(f"rh:{action}")
        if len(self.recent_actions) > 20:
            self.recent_actions = self.recent_actions[-10:]
        self._log("rh_decision", {"action": action, "right": right_open,
                    "front": front_open, "left": left_open, "back": back_open,
                    "blocked": self.blocked})

    # ── 打转检测 ────────────────────────────────────────

    def _detect_loop(self):
        """检查是否在死胡同里打转。返回 True 表示检测到打转。"""
        if len(self.visited_cells) < 6:
            return False
        recent = self.visited_cells[-8:]
        # 统计最近格子中重复最多的次数
        from collections import Counter
        counts = Counter(recent)
        most = counts.most_common(1)[0][1]
        return most >= AGENT_LOOP_THRESHOLD

    # ── 轨迹日志 ────────────────────────────────────────

    def _start_log(self):
        """开始记录本次探索轨迹。"""
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._log_file = LOG_DIR / f"trajectory_{ts}.jsonl"
        self._log_events = []
        self._trajectory = []
        self._mode_start_time = time.time()
        maze_info = {
            "cols": self.maze["grid"]["cols"],
            "rows": self.maze["grid"]["rows"],
            "cell": self.maze["grid"]["cell"],
            "size": self.maze["size"],
            "walls_count": len(self.maze["walls"]),
            "start": list(self.maze["start"]),
            "goal": list(self.goal),
        }
        self._log("session_start", {"maze": maze_info, "mode": self.auto_mode})

    def _log(self, event_type, data=None):
        """记录一条事件。"""
        entry = {
            "ts": round(time.time() - self._mode_start_time, 3),
            "event": event_type,
        }
        if data:
            entry.update(data)
        self._log_events.append(entry)

    def _log_position(self, x, y, yaw):
        """记录轨迹点（每帧调用，内部节流到 ~0.2s）。"""
        now = time.time()
        if self._trajectory and now - self._trajectory[-1][2] < 0.2:
            return
        self._trajectory.append((round(x, 3), round(y, 3), round(now - self._mode_start_time, 3)))

    def _flush_log(self):
        """写出日志文件。"""
        if not self._log_file or not self._log_events:
            return
        # 添加轨迹摘要
        self._log("trajectory_points", {
            "count": len(self._trajectory),
            "points": self._trajectory[::5],  # 每5个点存1个，节省空间
        })
        with open(self._log_file, "w", encoding="utf-8") as f:
            for entry in self._log_events:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"[log] 轨迹已保存: {self._log_file} ({len(self._log_events)} 条事件)")

    def stop_auto(self):
        """退出自动模式，停车，写出日志。"""
        self._flush_log()
        self.auto_mode = False
        self.waypoints = []
        self.waypoint_idx = 0
        self.stuck_timer = 0.0
        self.agent_decision = None
        self.agent_failures = 0
        self.agent_reasoning = ""
        self.rh_timer = 0.0
        self.rh_decision = None
        self._stuck_position = None
        self.set_command(0.0, 0.0)

    def _auto_navigate(self, dt):
        """每帧调用的自动导航逻辑。"""
        if (not self.auto_mode or self.goal_reached
                or self.waypoint_idx >= len(self.waypoints)):
            if self.auto_mode and self.goal_reached:
                print("[auto] 到达终点！")
            self.stop_auto()
            return

        # 当前目标路点
        wx, wy = self.waypoints[self.waypoint_idx]
        position, orientation = p.getBasePositionAndOrientation(self.robot_id)
        yaw = p.getEulerFromQuaternion(orientation)[2]
        rx, ry = position[0], position[1]

        # 距离与角度
        dx, dy = wx - rx, wy - ry
        dist = math.hypot(dx, dy)
        desired_angle = math.atan2(dy, dx)
        angle_error = self._norm_angle(desired_angle - yaw)

        # 卡住检测：撞墙时累计，超时则重新规划
        if self.blocked:
            self.stuck_timer += dt
        else:
            self.stuck_timer = max(0.0, self.stuck_timer - dt * 2.0)

        if self.stuck_timer > STUCK_TIMEOUT:
            print("[auto] 卡住超时，从当前位置重新规划...")
            current_cell = maze_module.cell_from_position(self.maze, rx, ry)
            # 从当前格重新寻路到终点
            # 构造一个以当前位置为起点的临时 maze 副本并求路径
            self._replan(current_cell)
            self.stuck_timer = 0.0

        # 到达当前路点 → 下一个
        if dist < WAYPOINT_THRESHOLD:
            self.waypoint_idx += 1
            if self.waypoint_idx >= len(self.waypoints):
                self.stop_auto()
                return
            return  # 下一帧处理新路点

        # 朝向未对齐 → 原地转向
        if abs(angle_error) > ANGLE_THRESHOLD:
            turn_dir = 1.0 if angle_error > 0 else -1.0
            self.set_command(0.0, turn_dir)
        else:
            # 朝向前进，同时微调方向
            correction = angle_error * 2.0   # P 控制器
            correction = max(-1.0, min(1.0, correction))
            self.set_command(1.0, correction)

    def _replan(self, start_cell):
        """从指定格子重新 BFS 寻路到终点。"""
        # 在 maze 上做一次从 start_cell 到 goal_cell 的 BFS
        from collections import deque
        goal = self.maze["goal_cell"]
        neighbors_fn = self.maze["neighbors"]
        center_fn = self.maze["cell_center"]

        q = deque([start_cell])
        prev = {start_cell: None}
        found = False
        while q:
            cur = q.popleft()
            if cur == goal:
                found = True
                break
            for nb in neighbors_fn(cur):
                if nb not in prev:
                    prev[nb] = cur
                    q.append(nb)

        if not found:
            print("[auto] 重新规划失败，无可行路径")
            self.stop_auto()
            return

        # 回溯路径
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = prev[node]
        path.reverse()
        self.waypoints = [center_fn(cx, cy) for cx, cy in path]
        self.waypoint_idx = 0
        print(f"[auto] 重新规划完成，{len(self.waypoints)} 个路点")

    # ── Agent 导航 ────────────────────────────────────────

    def _init_agent(self):
        """延迟初始化 Agent（首次使用时，避免启动阻塞）。"""
        if self.agent is not None:
            return self.agent_enabled
        try:
            self.agent = agent_module.MazeAgent()
            if not self.agent.api_key:
                print("[agent] 未设置 DEEPSEEK_API_KEY，Agent 不可用，回退到 BFS")
                self.agent_enabled = False
            else:
                self.agent_enabled = True
                print(f"[agent] 初始化完成，模型: {self.agent.model}")
        except Exception as e:
            print(f"[agent] 初始化失败: {e}")
            self.agent_enabled = False
        return self.agent_enabled

    def start_agent_explore(self):
        """启动 Agent「评论员」模式：BFS 执行 + Agent 点评。"""
        if not self._init_agent():
            print("[agent] Agent 不可用，回退到 BFS")
            self.start_auto_explore()
            return
        self.auto_mode = "agent"
        self.agent_failures = 0
        self.agent_reasoning = ""
        self.agent_latency_ms = 0
        self.visited_cells = []
        self.recent_actions = []
        self.cell_visit_count = {}
        self.blacklisted_cells = set()
        self._stuck_position = None
        self._agent_asked_at_idx = -1
        self.waypoints = maze_module.find_path(self.maze)
        self.waypoint_idx = 0
        self._start_log()
        self._log("mode_start", {"mode": "agent_v4_commentator", "model": self.agent.model})
        print(f"[agent] Agent v4 评论员模式，日志: {self._log_file}")

    def start_auto_explore(self):
        """启动 BFS 模式自动探索。"""
        self.auto_mode = "bfs"
        self.waypoints = maze_module.find_path(self.maze)
        if not self.waypoints:
            print("[auto] 未找到路径")
            return
        self.waypoint_idx = 0
        self.stuck_timer = 0.0
        self._start_log()
        self._log("mode_start", {"mode": "bfs", "waypoints": len(self.waypoints)})
        print(f"[auto] BFS 模式启动，共 {len(self.waypoints)} 个路点，日志: {self._log_file}")

    def _agent_navigate(self, dt):
        """Agent v4「评论员」模式：BFS 执行导航 + Agent 旁观点评。"""
        # ── 完全复用 BFS 导航逻辑（100% 可靠）──
        self._auto_navigate(dt)

        # ── 岔路口时问 Agent 意见（不影响执行，仅记录）──
        if (self.waypoint_idx > 0
                and self.waypoint_idx < len(self.waypoints)
                and not self._agent_asked_at_idx == self.waypoint_idx):
            self._agent_asked_at_idx = self.waypoint_idx
            position, _ = p.getBasePositionAndOrientation(self.robot_id)
            current_cell = maze_module.cell_from_position(
                self.maze, position[0], position[1])
            neighbors_fn = self.maze["neighbors"]
            if len(neighbors_fn(current_cell)) >= 3:
                self._ask_agent_opinion(current_cell)

    def _ask_agent_opinion(self, current_cell):
        """问 Agent 对当前 BFS 路径的看法（纯记录，不改变执行）。"""
        if not self._init_agent():
            return
        remaining = self.waypoints[self.waypoint_idx:]
        bfs_cells = [maze_module.cell_from_position(self.maze, wx, wy)
                     for wx, wy in remaining]
        bfs_cells = [current_cell] + bfs_cells

        result = self.agent.analyze_path(
            bfs_cells,
            self.visited_cells,
            self.blacklisted_cells,
        )
        verdict = result.get("verdict", "agree") if result else "error"
        reasoning = result.get("reasoning", "") if result else ""
        print(f"[agent] 💬 {verdict}: {reasoning}")
        self._log("agent_opinion", {
            "cell": list(current_cell),
            "verdict": verdict,
            "reasoning": reasoning,
            "agent_calls": self.agent.call_count,
        })

    def _switch_to_right_hand(self):
        """切换到右手法则模式。"""
        self.auto_mode = "right_hand"
        self.rh_timer = 0.0
        self.rh_decision = None
        self.rh_start_time = time.time()
        self._log("mode_switch", {"to": "right_hand"})
        print("[rh] 右手法则模式启动")

    def set_command(self, move, turn):
        self.command["move"] = float(move)
        self.command["turn"] = float(turn)

    def stop(self):
        self.set_command(0.0, 0.0)

    def _hits_wall(self, x, y):
        """点 (x,y) 加上机器狗半径后，是否与任何墙体包围盒相交。"""
        r = DOG_RADIUS
        for min_x, min_y, max_x, max_y in self.wall_aabbs:
            if (min_x - r) <= x <= (max_x + r) and (min_y - r) <= y <= (max_y + r):
                return True
        return False

    def step(self, dt):
        position, orientation = p.getBasePositionAndOrientation(self.robot_id)
        yaw = p.getEulerFromQuaternion(orientation)[2]
        # 连续 yaw：跟踪方向旋转的净变化，避免 ±π 跳变
        prev_yaw = getattr(self, '_prev_pybullet_yaw', yaw)
        dyaw = yaw - prev_yaw
        if dyaw > math.pi:
            dyaw -= 2 * math.pi
        elif dyaw < -math.pi:
            dyaw += 2 * math.pi
        self.continuous_yaw += dyaw
        self._prev_pybullet_yaw = yaw

        # 终点到达后锁定
        if self.goal_reached:
            self.stop_auto()
            p.stepSimulation()
            return

        # 自动导航模式
        if self.auto_mode == "bfs":
            self._auto_navigate(dt)
        elif self.auto_mode == "agent":
            self._agent_navigate(dt)
        elif self.auto_mode == "right_hand":
            self._right_hand_navigate(dt)

        # 轨迹记录
        if self.auto_mode:
            self._log_position(position[0], position[1], yaw)

        # 更新朝向（手动模式或自动模式都能工作）
        yaw += self.command["turn"] * TURN_SPEED * dt

        # 再尝试前进/后退，撞墙则原地不动
        nx = position[0] + self.command["move"] * MOVE_SPEED * math.cos(yaw) * dt
        ny = position[1] + self.command["move"] * MOVE_SPEED * math.sin(yaw) * dt
        lo, hi = DOG_RADIUS, self.maze["size"] - DOG_RADIUS
        nx = min(max(nx, lo), hi)
        ny = min(max(ny, lo), hi)

        if self.command["move"] != 0.0 and self._hits_wall(nx, ny):
            self.blocked = True
            nx, ny = position[0], position[1]   # 撞墙：保持原位
        else:
            self.blocked = False

        quat = p.getQuaternionFromEuler([0.0, 0.0, yaw])
        p.resetBasePositionAndOrientation(self.robot_id, [nx, ny, ROBOT_HEIGHT], quat)

        gx, gy, gr = self.goal
        if (nx - gx) ** 2 + (ny - gy) ** 2 <= gr ** 2:
            self.goal_reached = True
            self.stop()
            self._log("goal_reached", {
                "position": [round(nx, 3), round(ny, 3)],
                "mode": str(self.auto_mode),
                "total_time_s": round(time.time() - self._mode_start_time, 1),
                "agent_calls": self.agent.call_count if self.agent else 0,
            })

        p.stepSimulation()

    def get_state(self):
        position, _ = p.getBasePositionAndOrientation(self.robot_id)
        return {
            "position": {
                "x": round(position[0], 3),
                "y": round(position[1], 3),
                "z": round(position[2], 3),
            },
            "yaw": round(self.continuous_yaw, 3),
            "command": dict(self.command),
            "blocked": self.blocked,
            "goal_reached": self.goal_reached,
            "auto_mode": self.auto_mode,
            "waypoints": [
                {"x": round(wx, 3), "y": round(wy, 3)}
                for wx, wy in self.waypoints
            ],
            "waypoint_idx": self.waypoint_idx,
            "agent": {
                "reasoning": self.agent_reasoning,
                "latency_ms": int(self.agent_latency_ms),
                "failures": self.agent_failures,
                "call_count": self.agent.call_count if self.agent else 0,
            },
            "log_file": str(self._log_file) if self._log_file else "",
            "maze": {
                "size": self.maze["size"],
                "walls": [
                    {"cx": cx, "cy": cy, "hx": hx, "hy": hy}
                    for (cx, cy, hx, hy) in self.maze["walls"]
                ],
                "goal": {"x": self.goal[0], "y": self.goal[1], "r": self.goal[2]},
                "start": {"x": self.maze["start"][0], "y": self.maze["start"][1]},
                "robot_radius": DOG_RADIUS,
            },
        }

    def close(self):
        p.disconnect(self.physics_client)


async def index(request):
    html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
    return web.Response(text=html, content_type="text/html")


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    app = request.app
    sim = app["sim"]
    app["clients"].add(ws)
    await ws.send_json({"type": "state", "data": sim.get_state()})

    try:
        async for msg in ws:
            if msg.type != WSMsgType.TEXT:
                continue
            data = json.loads(msg.data)
            msg_type = data.get("type")
            if msg_type == "command":
                sim.set_command(data.get("move", 0.0), data.get("turn", 0.0))
            elif msg_type == "stop":
                sim.stop()
                sim.stop_auto()
            elif msg_type == "reset":
                sim.reset_robot()
            elif msg_type == "auto_explore":
                sim.start_auto_explore()
            elif msg_type == "agent_explore":
                sim.start_agent_explore()
            elif msg_type == "stop_auto":
                sim.stop_auto()
            await ws.send_json({"type": "state", "data": sim.get_state()})
    finally:
        app["clients"].discard(ws)
    return ws


async def simulation_loop(app):
    sim = app["sim"]
    while True:
        sim.step(1.0 / 60.0)
        payload = json.dumps({"type": "state", "data": sim.get_state()})
        stale = []
        for ws in app["clients"]:
            if ws.closed:
                stale.append(ws)
                continue
            await ws.send_str(payload)
        for ws in stale:
            app["clients"].discard(ws)
        await asyncio.sleep(1.0 / 10.0)


async def on_startup(app):
    app["sim"] = MazeDogServer()
    app["clients"] = set()
    app["sim_task"] = asyncio.create_task(simulation_loop(app))


async def on_cleanup(app):
    app["sim_task"].cancel()
    try:
        await app["sim_task"]
    except asyncio.CancelledError:
        pass
    app["sim"].close()


def main():
    app = web.Application()
    app.router.add_get("/", index)
    app.router.add_get("/ws", websocket_handler)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)
    print(f"PyBullet starter listening on http://{HOST}:{PORT}")
    web.run_app(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
