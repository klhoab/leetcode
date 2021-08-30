#https://leetcode.com/contest/biweekly-contest-59/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        
        last = 'a'
        for v in word:
            x= (ord(v) - ord(last) + 26) % 26 
            y= (ord(last) - ord(v) + 26) % 26
            ans+= min(x,y)
            last = v
        return ans + len(word)