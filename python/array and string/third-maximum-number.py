#https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) < 3:
            return max(list(s))
        return sorted(list(s), reverse=True)[2]