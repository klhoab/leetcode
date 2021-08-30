#https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n<= 2:
            return (n+1)//2
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)