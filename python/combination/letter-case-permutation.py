#https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        curr = list(s)
        ans = []
        
        def per(i):
            if i>= n:
                ans.append("".join(curr))
                return
            
            per(i+1)
            if 'a'<= s[i] <= 'z':
                curr[i] = s[i].upper()
                per(i+1)
                curr[i] = s[i].lower()
                
            elif 'A' <= s[i] <= 'Z':
                curr[i] = s[i].lower()
                per(i+1)
                curr[i] = s[i].upper()
        
        per(0)
        return ans

