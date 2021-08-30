class Solution:
    def minSwaps(self, s: str) -> int:
        n = 0 
        for v in s:
            if v =='[':
                n+= 1
            elif n> 0:
                n-= 1
        return (n+1)//2
