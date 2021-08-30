#https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0:2]
        for i in range(2,len(s)):
            if s[i] != ans[-1] or s[i] != ans[-2]:
                ans = ans + s[i]
        return ans