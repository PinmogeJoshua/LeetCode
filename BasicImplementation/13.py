"""
13-罗马数字转整数
罗马数字包含以下七种字符: I, V, X, L:50, C:100, D:500 和 M:1000
这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。
"""
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        num = 0
        prev_value = 0
        
        for char in reversed(s):  # 从右向左遍历字符串
            current_value = roman_dict[char]
            if current_value < prev_value:  # 如果当前值小于前一个值，执行减法
                num -= current_value
            else:  # 否则执行加法
                num += current_value
            prev_value = current_value  # 更新前一个值
        
        return num
