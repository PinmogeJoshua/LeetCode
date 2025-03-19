"""
1041. 困在环中的机器人
在无限的平面上, 机器人最初位于 (0, 0) 处, 面朝北方。注意:
北方向 是y轴的正方向; 南方向 是y轴的负方向; 东方向 是x轴的正方向; 西方向 是x轴的负方向。
机器人可以接受下列三条指令之一：
"G"：直走 1 个单位; "L"：左转 90 度; "R"：右转 90 度
机器人按顺序执行指令 instructions, 并一直重复它们
只有在平面中存在环使得机器人永远无法离开时, 返回 true。否则, 返回 false。
"""
from typing import List

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 初始位置和方向向量
        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 北、东、南、西
        direction_idx = 0  # 初始方向为北
        
        # 遍历指令
        for char in instructions:
            if char == "G":  # 前进
                dx, dy = directions[direction_idx]
                x += dx
                y += dy
            elif char == "L":  # 左转
                direction_idx = (direction_idx + 3) % 4  # 左转相当于减 1
            elif char == "R":  # 右转
                direction_idx = (direction_idx + 1) % 4  # 右转相当于加 1
        
        # 判断是否困在环中
        # 1. 回到原点
        # 2. 方向发生变化（不再朝北）
        return (x == 0 and y == 0) or direction_idx != 0
        