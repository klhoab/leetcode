# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            curr= curr.next
            l += 1
        
        n= l - n
        if n== 0:
            return head.next
        
        curr= head
        for i in range(n-1):
            curr= curr.next
        curr.next = curr.next.next
        
        return head