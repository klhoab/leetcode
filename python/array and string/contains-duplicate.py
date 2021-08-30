#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = sorted(nums)
        n = len(nums2)
        for i in range(n-1):
            if nums2[i] == nums2[i+1]:
                return True
        return False