"""
1822-数据元素积的符号
已知函数 signFunc(x) 将会根据 x 的正负返回特定值：

如果 x 是正数，返回 1 。
如果 x 是负数，返回 -1 。
如果 x 是等于 0 ，返回 0 。
给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。

返回 signFunc(product) 。
"""
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for x in nums:
            if x < 0:
                res *= (-1)
            elif x == 0:
                res = 0
                break
        
        return res
