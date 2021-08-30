#https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n):
            for j in range(i+1, n):
                d = -nums[i] - nums[j]
                k = bisect_left(nums, d, j+1, n)
                if k < n and nums[k] == d:
                    t= sorted([nums[i], nums[j], nums[k]])
                    if t not in ans:
                        ans.append(t)
        return ans
