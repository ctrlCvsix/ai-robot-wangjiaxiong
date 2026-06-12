#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LLM Agent 决策模块 v4 —— 「评论员」模式。

Agent 不做实时控制，而是在岔路口给出"建议路线"。
机器人始终用 BFS 算法执行（100% 可靠），Agent 的建议记录到日志。
报告里可以对比：Agent 选的路 vs BFS 最优解，分析 AI 的决策质量。
"""
import json
import os
import re
import time
import urllib.request
import urllib.error

DEFAULT_MODEL = "deepseek-chat"
DEFAULT_BASE_URL = "https://api.deepseek.com/v1"
REQUEST_TIMEOUT = 8

SYSTEM_PROMPT = """你是迷宫探索的 AI 策略分析师。

每次你会收到：
- 整条 BFS 规划路径（格子序列）
- 已走过的格子
- 死胡同黑名单

你的任务：评价 BFS 路径是否合理。如果觉得某段可以优化，给出替代路线。

## 输出格式
{"verdict":"agree"/"disagree","alternative":[[0,0],[1,0]],"reasoning":"<30字>"}

如果同意 BFS 路径，verdict=agree 且 alternative=[]。
如果不同意，verdict=disagree 且 alternative=你认为更好的格子序列（从前位置到终点）。"""


class MazeAgent:
    """DeepSeek API 驱动的路线分析器。"""

    def __init__(self, api_key=None, model=None, base_url=None):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY", "")
        self.model = model or DEFAULT_MODEL
        self.base_url = base_url or DEFAULT_BASE_URL
        self.call_count = 0
        self.total_latency = 0.0
        self.suggestions = []

    def analyze_path(self, bfs_path, visited_cells, blacklisted):
        """分析 BFS 路径，返回建议或 None（失败时）。

        bfs_path: [(cx,cy), ...] BFS 规划的完整路径
        visited_cells: [(cx,cy), ...] 已走过的格子
        blacklisted: {(cx,cy), ...} 黑名单格子
        返回: {"verdict": "agree"/"disagree", "alternative": [...], "reasoning": str}
        """
        # 精简输入
        current = bfs_path[0] if bfs_path else "?"
        goal = bfs_path[-1] if bfs_path else "?"
        path_len = len(bfs_path)

        msg = (
            f"当前位置: {list(current)}\n"
            f"终点: {list(goal)}\n"
            f"BFS规划路径 ({path_len}格): {[list(c) for c in bfs_path[:6]]}"
            f"{'...' if path_len > 6 else ''}\n"
            f"已走过: {[list(c) for c in visited_cells[-8:]]}\n"
            f"黑名单: {[list(c) for c in sorted(blacklisted)[:5]]}\n"
            f"评价这条BFS路径:"
        )

        try:
            t0 = time.time()
            raw = self._call_api(msg)
            elapsed = time.time() - t0
            self.call_count += 1
            self.total_latency += elapsed

            result = self._parse_verdict(raw)
            if result is None:
                return {"verdict": "agree", "alternative": [],
                        "reasoning": "parse error, default agree"}

            self.suggestions.append({
                "path": [list(c) for c in bfs_path[:6]],
                "verdict": result["verdict"],
                "alternative": result["alternative"],
                "reasoning": result["reasoning"],
                "latency_ms": int(elapsed * 1000),
            })
            return result

        except Exception as e:
            print(f"[agent] API 失败: {e}")
            return {"verdict": "agree", "alternative": [],
                    "reasoning": f"API error: {str(e)[:30]}"}

    def _parse_verdict(self, raw_text):
        text = raw_text.strip()
        for marker in ("```json", "```"):
            if marker in text:
                s = text.find(marker) + len(marker)
                e = text.find("```", s)
                if e > s:
                    text = text[s:e].strip()
                break
        try:
            obj = json.loads(text)
        except json.JSONDecodeError:
            m = re.search(r'\{[^{}]*"verdict"[^{}]*\}', raw_text)
            if m:
                try:
                    obj = json.loads(m.group())
                except json.JSONDecodeError:
                    print(f"[agent] JSON 解析失败: {raw_text[:100]}")
                    return None
            else:
                print(f"[agent] JSON 解析失败: {raw_text[:100]}")
                return None
        return {
            "verdict": obj.get("verdict", "agree"),
            "alternative": obj.get("alternative", []),
            "reasoning": obj.get("reasoning", ""),
        }

    def _call_api(self, user_message):
        url = f"{self.base_url}/chat/completions"
        payload = json.dumps({
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            "temperature": 0.3,
            "max_tokens": 200,
            "stream": False,
        }).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        })
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"].strip()

    @property
    def avg_latency_ms(self):
        if self.call_count == 0:
            return 0
        return self.total_latency / self.call_count * 1000
