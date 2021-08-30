#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%= len(nums)
        nums2 = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = nums2[i]