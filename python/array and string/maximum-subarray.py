#https://leetcode.com/problems/maximum-subarray/
 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = curr = -math.inf
        for i in range(len(nums)):
            curr = max(nums[i], curr+ nums[i])
            ans = max(ans, curr)
        return ans