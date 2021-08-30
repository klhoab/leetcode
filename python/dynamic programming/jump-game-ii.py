#https://leetcode.com/problems/jump-game-ii
 
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        @lru_cache(None)
        def dp(i) -> int:
            if i>= n-1:
                return 0
            
            ans = n
            for j in reversed(range(0, nums[i])):
                ans = min(ans, 1+ dp(i+j+1))
            return ans
        
        #T= N^2
        return dp(0)
    