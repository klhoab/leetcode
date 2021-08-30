#https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        @lru_cache(None)
        def dp(i) -> bool:
            if i>= n-1:
                return True
            
            for j in reversed(range(0, nums[i])):
                if dp(i+j+1): return True
                
            return False
        
        #T= N^2
        return dp(0)
    