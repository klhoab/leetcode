#https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.p = []
        t = 0
        for v in nums:
            t+= v
            self.p.append(t)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0 :
            return self.p[right]
        return self.p[right] - self.p[left- 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)