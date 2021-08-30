#https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(None)
        def dp(start: int, canLast: bool) -> int:
            if start >= n:
                return 0
            if start == n-1:
                return nums[start] if canLast else 0
            
            return max (nums[start]+ dp(start+2, canLast and start > 0), dp(start+1, canLast))
        
        if n <= 3:
            return max(nums)
        return dp(0, True)