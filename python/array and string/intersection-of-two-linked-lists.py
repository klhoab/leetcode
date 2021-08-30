# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        cnt = 0
        
        while nodeA:
            nodeA = nodeA.next
            cnt+= 1
        
        while nodeB:
            nodeB = nodeB.next
            cnt-= 1
        
        nodeA, nodeB = headA, headB
        while cnt > 0:
            nodeA = nodeA.next
            cnt-= 1
        
        while cnt < 0:
            nodeB = nodeB.next
            cnt+= 1
        
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            
        return None
        
