#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = []
        for v in nums1:
            d[v]+= 1
        for v in nums2:
            if d[v]:
                ans+= [v]
                d[v]-= 1
        return ans
        