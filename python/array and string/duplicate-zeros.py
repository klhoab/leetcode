#https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans = []
        for v in arr:
            ans.append(v)
            if v== 0:
                ans.append(v)
        for i in range(len(arr)):
            arr[i] = ans[i]