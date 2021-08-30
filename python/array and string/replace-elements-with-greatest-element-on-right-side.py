#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
 
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = arr
        for i in reversed(range(n-1)):
            mx[i] = max(mx[i], mx[i+1])
        return mx[1:] + [-1]
        