#https://leetcode.com/contest/weekly-contest-255/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return gcd(mn, mx)