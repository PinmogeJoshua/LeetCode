"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix, 请按照 顺时针螺旋顺序, 返回矩阵中的所有元素
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 假如矩阵为空
        if not matrix or not matrix[0]:
            return []
        
        # 初始化结果列表
        result = []
        m = len(matrix) # 行数
        n = len(matrix[0]) # 列数
        # 定义矩阵边界
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # 遍历矩阵
        while top <= bottom and left <= right:
            # 从左到右遍历上边界
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            # 从右到左遍历下边界
            if top <= bottom:
                for j in range(right, left - 1, -1):  
                    result.append(matrix[bottom][j])
                bottom -= 1
            # 从下到上遍历左边界
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
        # 返回结果
        return result
