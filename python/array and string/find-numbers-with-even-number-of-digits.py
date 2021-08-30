#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigit(n):
            cnt = 0
            while n:
                n//= 10
                cnt+= 1
            return cnt
        
        ans = 0
        for v in nums:
            if countDigit(v)%2== 0:
                ans+= 1
        return ans