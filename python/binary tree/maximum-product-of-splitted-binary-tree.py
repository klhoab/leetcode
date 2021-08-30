#https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        d= defaultdict(int)
        def subTreeSum(root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            
            if d[root]: return d[root]
            d[root]= root.val + subTreeSum(root.left) + subTreeSum(root.right) 
            return d[root]
        
        total = subTreeSum(root)
        arr = [y for x, y in d.items()]
        
        ans = 0
        m = 10**9 + 7
        for v in arr:
            ans = max(ans, v * (total- v) )
        
        return ans % m