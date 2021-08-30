#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(start: int) -> int:
            if start >= n:
                return 0
            if start == n-1:
                return nums[start]
            
            return max(nums[start]+ dp(start+2), dp(start+1))
        
        return dp(0)