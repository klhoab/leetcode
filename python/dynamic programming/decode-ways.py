#https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mem = [0 for _ in range(n)]
        
        def dp(i):
            if i >= n: return 1
            if mem[i]: return mem[i]
            ans = 0
            #case 1: single digit
            if s[i] != '0':
                ans += dp(i+1)
            
            #case 2: two digits
            if i+1 < n and (s[i]== '1' or (s[i]== '2' and s[i+1] <= '6')):
                ans += dp(i+2)
            mem[i] = ans
            return ans

        return dp(0)
        