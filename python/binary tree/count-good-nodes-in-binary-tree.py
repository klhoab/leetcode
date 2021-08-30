#https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        d = defaultdict(int)  #prev. max
        s = [root]
        d[root] = -10001
        ans = 0
        while s:
            curr = s.pop()
            if curr.val >= d[curr]:
                ans += 1
                
            t= max(d[curr], curr.val)
            d[curr] = t
            
            if curr.left:
                d[curr.left] = t
                s.append(curr.left)
            if curr.right:
                d[curr.right] = t
                s.append(curr.right)
            
        return ans
        