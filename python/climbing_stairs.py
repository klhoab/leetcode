class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0 for _ in range(n+1)]
        def dp(n):
            if n<=1:
                return 1
            if mem[n]:
                return mem[n]
            mem[n]= dp(n-1) + dp(n-2)
            return mem[n]
        
        return dp(n)
        
