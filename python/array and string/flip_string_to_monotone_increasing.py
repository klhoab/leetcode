class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt+= 1
            else:
                ans+= 1
            ans = min(ans, cnt)
        return ans
