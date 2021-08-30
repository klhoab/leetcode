#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        head1, head2 = m-1, n-1
        p = m+n-1
        while head1>= 0 and head2>= 0:
            if nums1[head1] >nums2[head2]:
                nums1[p] = nums1[head1]
                head1 -= 1
            else:
                nums1[p] = nums2[head2]
                head2 -= 1
            p-= 1
            
        while head2>= 0:
            nums1[p] = nums2[head2]
            head2 -= 1
            p-= 1        
        