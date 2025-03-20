"""
1572. 矩阵对角线元素的和
给你一个正方形矩阵 mat, 请你返回矩阵对角线元素的和
请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和 
"""
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        elementSum = 0
        n = len(mat)  # 矩阵的维度
        
        # 遍历对角线
        for i in range(n):
            # 主对角线元素
            elementSum += mat[i][i]
            # 副对角线元素
            elementSum += mat[i][n - 1 - i]
        
        # 如果矩阵维度为奇数，减去重复的中心元素
        if n % 2 == 1:
            elementSum -= mat[n // 2][n // 2]
        
        return elementSum
            