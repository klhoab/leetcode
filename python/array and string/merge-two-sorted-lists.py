#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            head = None
            if l1.val < l2.val:
                head = l1
                head.next = self.mergeTwoLists(l1.next, l2)
            else:
                head = l2
                head.next = self.mergeTwoLists(l1, l2.next)
            return head
                
        