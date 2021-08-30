#https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        sq = [[0] * 9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                r, c = i//3, j//3
                k = r * 3 + c
                if board[i][j] == '.':
                    continue
                v = int(board[i][j]) - 1
                if row[i][v] or col[j][v] or sq[k][v]:
                    return False
                row[i][v] = col[j][v] = sq[k][v] = 1
        return True
                