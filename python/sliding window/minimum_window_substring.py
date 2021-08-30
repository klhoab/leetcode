class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s = "ADOBECODEBANC", t = "ABC", n = 1e5
        n = len(s)
        d = Counter(t)
        ans = ""
        
        i = j = 0
        cnt = len(t)
        while j < n:
            matched = False
            
            #slide right
            if s[j] in d.keys():
                d[s[j]] -= 1
                if d[s[j]] >= 0:
                    cnt-= 1
            j+= 1
            
            #slide left, if matched
            while cnt == 0:
                matched = True
                if s[i] in d.keys():
                    d[s[i]] += 1
                    if d[s[i]] > 0:
                        cnt+= 1
                i+= 1
                
            if matched:
                t= s[i-1:j]
                if ans == "" or len(t) < len(ans):
                    ans = t
                
        return ans
        
