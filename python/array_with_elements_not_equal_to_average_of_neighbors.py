class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n= len(nums)
        m= n//2
        ans = []
        for i in range(m):
            ans.append(nums[i+m])
            ans.append(nums[i])
        
        if n%2 == 1:
            ans.append(nums[n-1])
        
        return ans
