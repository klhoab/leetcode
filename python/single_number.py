class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for k in nums:
            ans ^= k
        return ans
