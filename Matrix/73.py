"""
73. 矩阵置零
给定一个 m x n 的矩阵, 如果一个元素为 0 , 则将其所在行和列的所有元素都设为 0
请使用 原地 算法
"""
from typing import List
class Solutions:
    def setZeros(self, matrix: List[List[int]]) -> None:
        """
        Don't return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_zero = col_zero = False

        # 检查第一列是否需要置零 
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break

        # 检查第一列是否需要置零
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break
        
        # 先遍历，查找所有为0的位置
        for i in range(1, m):
            for j in range(1, n):
                # 标记位置零
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        # 根据标志位置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] ==0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 如果第一行需要置零
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # 如果第一列需要置零
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
        