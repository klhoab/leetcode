#https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr+= 1
        
        return ""