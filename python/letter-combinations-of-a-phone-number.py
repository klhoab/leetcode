class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        ans = []
        for v in digits:
            i = (int)(v)
            if len(ans) == 0:
                ans = ["".join(x) for x in itertools.product(d[i])]
            else:
                ans = ["".join(x) for x in itertools.product(ans, d[i])]
        return ans
        
