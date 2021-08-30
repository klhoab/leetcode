#https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @lru_cache(None)
        def getVal(i,j) -> int:
            if j==0 or i==j:
                return 1
            if i< 0 or j < 0 or j > i: 
                return 0
            return getVal(i-1, j-1) + getVal(i-1, j)
        
        arr = []
        for i in range(rowIndex+ 1):
            arr.append(getVal(rowIndex, i))
        return arr