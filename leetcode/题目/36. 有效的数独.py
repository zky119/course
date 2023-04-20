from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1、先生成三个数组
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[0] * 9 for _ in range(9)]
        # 遍历行
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    # 计算当前数字所在的子数独
                    k = (i // 3) * 3 + j // 3
                    # 如果当前数字已经出现过，返回 False
                    if rows[i][num] or columns[j][num] or subboxes[k][num]:
                        return False
                    # 否则，将当前数字标记为已出现
                    rows[i][num] = columns[j][num] = subboxes[k][num] = 1

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Solution().isValidSudoku(board)
