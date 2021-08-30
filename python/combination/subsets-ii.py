#https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            t= sorted([nums[j] for j in range(n) if (i & (1 << j))])
            if t not in ans:
                ans= ans + [t]
        return ans

        
