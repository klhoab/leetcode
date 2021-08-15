class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = t = nums[0]
        for i in range(1, len(nums)):
            t = max(nums[i], t+ nums[i])
            ans = max(ans, t)
        return ans
