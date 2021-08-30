#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d= {}
        for i, x in enumerate(nums):
            y = target - x 
            if y in d:
                return [d[y], i]
            else:
                d[x]= i
                
