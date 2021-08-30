#https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(r, c, val: str) -> bool:
            nr, nc = r//3*3, c//3*3
            for i in range(nr, nr+3):
                for j in range(nc, nc+3):
                    if val == board[i][j]:
                        return False
            for i in range(9):
                if board[r][i] == val or board[i][c] == val:
                    return False
            return True
        
        def fill(i=0, j=0):
            if j == 9:
                i+= 1
                j = 0
            if i == 9:
                return True

            if board[i][j] != '.':  #skip
                return fill(i, j+1)

            for k in range(9):
                if valid(i, j, str(k+1)):
                    board[i][j] = str(k+1)
                    if fill(i, j+1):
                        return True
                    board[i][j] = "."
                
            return False
        
        fill(0,0)
                    
        