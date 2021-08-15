class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        major = nums[0]
        
        for k in nums:
            if k== major:
                cnt+= 1
            elif cnt > 0:
                cnt-= 1
            else:
                major = k
        return major
