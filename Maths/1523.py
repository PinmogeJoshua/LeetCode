"""
1523. 在区间范围内统计奇数数目
给你两个非负整数 low 和 high 
请你返回 low 和 high 之间（包括二者）奇数的数目
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low + 1) % 2 == 1:
            if high % 2 == 1:
                return (int)((high - low) / 2 + 1)
            else:
                return (int)((high - low) / 2)
        else:
            return (int)((high - low + 1) / 2)