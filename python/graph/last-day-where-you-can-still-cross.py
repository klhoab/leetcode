#https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def walk(n):
            g = [[0] * col for _ in range(row)]
            v = [[0] * col for _ in range(row)]
            for i in range(n):
                x, y= cells[i]
                g[x-1][y-1] = 1

            s = []
            for j in range(col):
                if g[0][j] == 0:
                    s.append([0, j])
                    v[0][j] = 1

            while s:
                r, c = s.pop()
                
                if r == row - 1:
                    return True
                
                dir = [0, 1, 0, -1, 0] 
                for i in range(4):
                    nr, nc = r+ dir[i], c+ dir[i+1]
                    if 0 <= nr < row and 0 <= nc < col and g[nr][nc] == 0 and v[nr][nc] == 0:
                        v[nr][nc] = 1
                        s.append([nr, nc])
            
            return False
        
        
        left, right = 1, len(cells)
        ans = 0
        while left < right:
            mid = (left + right) // 2
            if walk(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid 
        return ans
    
        
                