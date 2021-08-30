#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = n = len(nums)
        
        curr = 0
        for i in range(n):
            if nums[i] == val:
                k-= 1
                continue
            nums[curr] = nums[i]
            curr+= 1
        return k