"""
58-最后一个单词的长度
给你一个字符串 s, 由若干单词组成, 单词前后用一些空格字符隔开
返回字符串中 最后一个 单词的长度
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串
"""
from typing import List

class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        words = s.split()  # 按空格分割字符串，得到单词列表
        return len(words[-1])  # 返回最后一个单词的长度