#https://leetcode.com/contest/weekly-contest-255/problems/find-unique-binary-string/
 
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        total = ["".join(seq) for seq in itertools.product("01", repeat=n)]
        for v in total:
            if v not in nums:
                return v
        return ""