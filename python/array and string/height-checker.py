#https://leetcode.com/problems/height-checker/
 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        n = len(heights)
        return sum([1 for i in range(n) if heights[i]!= expected[i]])