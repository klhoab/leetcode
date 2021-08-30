class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row0, col0 = False, False
        
        for j in range(m):
            if matrix[0][j] == 0:
                row0 = True 
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = True
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row0:
            for j in range(m):
                matrix[0][j] = 0
        if col0:
            for i in range(n):
                matrix[i][0] = 0
