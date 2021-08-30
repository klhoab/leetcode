#https://leetcode.com/contest/weekly-contest-255/problems/minimize-the-difference-between-target-and-chosen-elements/

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        n = len(mat)
        
        @lru_cache(None)
        def dp(start, total):
            if start >= n:
                return abs(total - target)
            
            if total > target:
                mn = 0
                for i in range(start, n):
                    mn += min(mat[i])
                return total+ mn - target
            
            ans = 5000
            for v in mat[start]:
                ans = min(ans, dp(start+1, total+ v))
            return ans
        
        #T= 70*800*70
        return dp(0, 0)