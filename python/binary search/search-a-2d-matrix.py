#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if target <= arr[-1]:
                k = bisect_left(arr, target)
                return k != len(arr) and arr[k] == target
            
        return False