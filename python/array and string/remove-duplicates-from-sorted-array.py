#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = n = len(nums)
        
        curr = 1
        for i in range(1, n):
            if nums[i] == nums[curr-1]:
                k-= 1
                continue
            nums[curr] = nums[i]
            curr += 1
            
        return k