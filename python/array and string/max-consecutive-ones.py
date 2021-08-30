#https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        ans = cnt= 0
        for v in nums:
            if v:
                cnt+= 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans