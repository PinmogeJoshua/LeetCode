"""
709. 转换成小写字母
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
"""
from typing import List

class Solution:
    def toLowerCase(self, s:str) -> str:
        result =[]
        for char in s:
            # 如果是大写字母
            if 'A' <= char <= 'Z':
                # 将其转化为小写字母
                result.append(chr(ord(char) + 32))
            # 如果是小写字母
            else:
                # 直接添加
                result.append(char)
        
        return ''.join(result)
