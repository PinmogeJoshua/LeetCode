"""
如果数组是单调递增或单调递减的，那么它是 单调 的。

如果对于所有 i <= j, nums[i] <= nums[j]，那么数组 nums 是单调递增的;
如果对于所有 i <= j, nums[i] >= nums[j]，那么数组 nums 是单调递减的。

当给定的数组 nums 是单调数组时返回 true, 否则返回 false。
"""
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        return increasing or decreasing

           