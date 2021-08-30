#https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr  = [ item for arr in matrix for item in arr ]
        arr2 = [ abs(item) for item in arr ]
        
        neg = 0
        for v in arr:
            if v < 0:
                neg ^= 1
        
        total, k = sum(arr2), min(arr2)
        ans = total - 2*k* neg
        return ans
        