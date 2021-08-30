class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mx = max(nums)
        d= defaultdict(int)
        for v in nums:
            d[v]+= v
        
        @lru_cache(None)
        def dp(i: int) -> int:
            if i > mx:
                return 0
            return max(d[i] + dp(i+2), dp(i+1))
        
        return dp(0)