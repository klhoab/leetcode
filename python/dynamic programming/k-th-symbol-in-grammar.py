#https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    @lru_cache(None)
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (k%2==0) ^self.kthGrammar(n-1, (k+1)//2)
        