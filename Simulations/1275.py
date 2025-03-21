"""
1275. 找出井字棋的获胜者
井字棋 是由两个玩家 A 和 B 在 3 x 3 的棋盘上进行的游戏。井字棋游戏的规则如下：
    玩家轮流将棋子放在空方格 (' ') 上
    第一个玩家 A 总是用 'X' 作为棋子，而第二个玩家 B 总是用 'O' 作为棋子
    'X' 和 'O' 只能放在空方格中，而不能放在已经被占用的方格上
    只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束
    如果所有方块都放满棋子（不为空），游戏也会结束
    游戏结束后，棋子无法再进行任何移动
给你一个数组 moves, 其中 moves[i] = [rowi, coli] 表示第 i 次移动在 grid[rowi][coli]
如果游戏存在获胜者(A 或 B), 就返回该游戏的获胜者;
如果游戏以平局结束，则返回 "Draw";
如果仍会有行动（游戏未结束），则返回 "Pending"
"""
from typing import List

class Solution:
    # 判断当前玩家是否满足胜利条件
    def checkWinner(self, board: List[List[str]], player: str) -> bool:        
        # 检查行、列和对角线是否满足胜利条件
        for i in range(3):
            # 检查行
            if all(board[i][j] == player for j in range(3)):
                return True
            # 检查列
            if all(board[j][i] == player for j in range(3)):
                return True
        # 检查主对角线
        if all(board[i][i] == player for i in range(3)):
            return True
        # 检查副对角线
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        # 如上述情况均不符合, 返回False
        return False
    
    # 判断游戏的最终结果
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 初始化3*3棋盘
        board = [[""] * 3 for _ in range(3)]
        # 玩家交替，A为先手
        for idx, move in enumerate(moves):
            if idx % 2 == 0:
                player = "A"
            else:
                player = "B"
            x, y = move
            board[x][y] = player
            # 检查当前玩家是否获胜
            if self.checkWinner(board, player):
                return player
        # 检查9个格子是否都填满
        if (len(moves)) == 9:
            return "Draw"
        # 否则游戏未完成
        return "Pending"