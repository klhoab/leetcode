#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d= defaultdict(int)
        for i, v in enumerate(numbers):
            if target- v in d:
                return [d[target-v], i+1]
            else:
                d[v] = i+1
        return []